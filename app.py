import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    men = mongo.db.users.find( { "gender": "male"})
    return render_template("men.html", men=men)


@app.route("/get_women_team")
def get_women_team():
    women = mongo.db.users.find( { "gender": "female"})
    return render_template("women.html", women=women)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "type": request.form.get("membership").lower(),
            "gender": request.form.get("gender"),
            "position": request.form.get("position")
        }
        mongo.db.users.insert_one(signup)

        session["current_user"] = request.form.get("username").lower()
        flash("You are signed up!")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username").capitalize()))
                return redirect(url_for("home_page", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have successfully logged out of your session!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/gameorg", methods=["GET", "POST"])
def gameorg():
    if request.method == "POST":
        
        gameorg = {
            "team": request.form.get("team-opt").lower(),
            "opposition": request.form.get("opposition").lower(),
            "venue": request.form.get("venue").lower()
        }
        mongo.db.game_schedule.insert_one(gameorg)

        flash("Game Fixture Entered!")
    return render_template("gameorg.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
