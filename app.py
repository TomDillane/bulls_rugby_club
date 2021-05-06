import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("home.html")


@app.route("/get_men_team")
def get_men_team():
    # filter for men in database
    men = mongo.db.users.find({"gender": "male"})
    return render_template("men.html", men=men)


@app.route("/get_women_team")
def get_women_team():
    # filter for women in database
    women = mongo.db.users.find({"gender": "female"})
    return render_template("women.html", women=women)


@app.route("/news")
def news():
    # return game schedule from database
    games = mongo.db.game_schedule.find()
    return render_template("news.html", games=games)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if user name exists
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # bring user back to signup page
            flash("Username already exists")
            return redirect(url_for("signup"))

        # create object with user sign up details
        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "type": request.form.get("membership").lower(),
            "gender": request.form.get("gender"),
            "position": request.form.get("position")
        }
        # insert in database
        mongo.db.users.insert_one(signup)

        session["current_user"] = request.form.get("username").lower()
        flash("You are signed up!")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # check username, if valid proceed to password check
        if user_exists:
            # check user's password, if correct welcome user to home page
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username").capitalize()))
                return redirect(url_for("home_page", username=session["user"]))
            else:
                # if password incorrect, back to login page
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username invalid, back to login page
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    # end user session
    flash("You have successfully logged out of your session!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/gameorg", methods=["GET", "POST"])
def gameorg():
    if request.method == "POST":
        # create object for game schedule

        gameorg = {
            "team": request.form.get("team-opt").lower(),
            "match_date": datetime.strptime(request.form.get("game-date"), "%b %d, %Y"),
            "date": request.form.get("game-date"),
            "opposition": request.form.get("opposition").lower(),
            "venue": request.form.get("venue").lower(),
            "bullsresult": 'TBC',
            "oppresult": 'TBC'
        }
        # insert in database
        mongo.db.game_schedule.insert_one(gameorg)

        flash("Game Fixture Entered!")
    return render_template("gameorg.html")


@app.route("/gameresult")
def gameresult():
    # return game schedule from database
    women = mongo.db.users.find({"gender": "female"})
    games = mongo.db.game_schedule.find({"team": "women"}).sort("match_date", -1)
    return render_template("gameresult.html", games=games, women=women)


@app.route("/update_score/<game_id>", methods=["GET", "POST"])
def update_score(game_id):
    if request.method == "POST":
        # create object for game result

        score = {
            "team": request.form.get("team").lower(),
            "date": request.form.get("date"),
            "opposition": request.form.get("opposition").lower(),
            "venue": request.form.get("venue").lower(),
            "bullsresult": request.form.get("bullsresult"),
            "oppresult": request.form.get("oppresult")
        }
        # update dictionary in database
        mongo.db.game_schedule.update({"_id": ObjectId(game_id)}, score)
        return redirect(url_for("gameresult"))
        flash("Result Updated!")

    game = mongo.db.game_schedule.find_one({"_id": ObjectId(game_id)})
    return render_template("update_score.html", game=game)


@app.route("/avail", methods=["GET", "POST"])
def avail():
    w_game_date = mongo.db.game_schedule.find({
        "team": "women",
        "bullsresult": "TBC"
        }).sort('match_date', -1)

    if request.method == "POST":
        # create object for player availability option

        avail = {
            "player": session["user"],
            "team": "women",
            "date": request.form.get("date-opt"),
            "available": request.form.get("avail").lower(),
            "meet": request.form.get("meet", "NA").lower()
        }
        this_match = avail['date']
        this_player = avail['player']
        mongo.db.player_avail.update(
            {"date": this_match, "player": this_player}, avail, upsert=True)

        # insert in database
        flash("Successfully entered availability!")
    return render_template("player_avail.html", w_game_date=w_game_date)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
