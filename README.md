# Bulls Rugby Club
## Introduction
The purpose of this website is to provide an online presence for a Rugby club.
The site will contain information about the club in general, latest fixtures and 
results and team details. Users will have the option to join the club and 
join a team as a player. As a player, the user will be able to elect availability for each match.
As the manager, the user will be able to input games in the schedule, update results and delete games.

## User Stories

### First Time Users

+ I want to get an overview of the club
+ I want to see latest fixtures and results related to the club teams
+ I want the option to join the club
+ I want the option to join a team in the club

### Returning Users

+ I want to be able to log in
+ I want to be able to edit my game availability
+ I want to see latest fixtures and results related to the club teams

### Manager Users

+ I want to be able to update latest results
+ I want to be able to view all player availability for games
+ I want to be able to remove games from the schedule
+ I want to grow the club membership
+ I want to keep up to date on team memebership

## UX

### Strategy Plane

The site is the online representation of a rugby club. The club manager must be able to 
run the site overall, as is the case with the actual club. New members  must be 
able to join and optionally select a team as a player. Returning players must 
be able to log in and edit their game availability. 

### Scope Plane

The scope of the site is to allow the manager to run the site in terms of content and
 the users to become members, edit their own information only and keep up to date
 in club affairs. 
 The site will include:
 + Home page with club overview
 + Team fixtures and results - both men and women
 + Team details - both men and women
 + Log in option for members
 + Join option for new users
 + Option to join a team as a player
 + Option for players to select game availability
 + Option for the manager to schedule games, update results and delete games


### Structure Plane

#### Frontend

The site will be structured in a consistent manner. The NAV bar will contain 
the menu options as relevant to the user:
+ Home
+ News
+ Men's Rugby
+ Women's Rugby
+ Sign Up / Log Out
+ Log In / Log Out

[Home Wireframe](readme_images/home.png)

[Fixtures and Results Wireframe](readme_images/fixtures_results.png)

[Team Wireframe](readme_images/team-details.png)

[Sign Up Wireframe](readme_images/signup.png)

[Login Wireframe](readme_images/login.png)

[Game Scheduler Wireframe](readme_images/game_fixture.png)

[Match Team Wireframe](readme_images/match_team.png)

[Update Score Team Wireframe](readme_images/update_score.png)

[Game Available selection Team Wireframe](readme_images/player_availability.png)


#### Backend

The database used is MongoDB. It is a non relational file based.
There are three collections:

1. Users
2. Game Schedule
3. Player Availability


[Database Wireframe](readme_images/database_design.png)


##### Users

This allows a new user to become a member of the club. The name and password
are captured for log in.
Where membership type of "Player", is selected, the user will be 
directed to the player form where playing position and gender must be selected.
Gender will direct to the relevant team.
The options of "Volunteer", and "Social", are for the club management to use for event organisation.

##### Game Schedule

This will be populated via front end form only available to user "manager"
 where game fixtures can be set,
results edited, and games deleted if necessary.
This collection will be used to populate the relevant pages fixtures and results.


##### Player Availability

This will be populated via front end form only available to users that are type "player". 
It will be joined using an aggregate function to take players full names for display on 
match team page only available to user "manager".


### Skeleton Plane 

The site will have 5 standard pagers for all users.
Players will have a form to opt in or out for game availability.
Manager will have two pages extra to all others to set game schedules and view players available.
Manager will have a form to edit game results. 

### Surface Plane

The site's colors, typography and layout will be consistent and in line with the club's colors.
The main club colors are red and blue, and this is reflected on the site. 

## Features

#### Current Features

+ The site will allow new users to join.
+ The site will allow returning users to log in.
+ The site will allow users to elect as a player and join a team.
+ The site will allow players to elect availability for matches on the schedule.
+ The site will allow players to change decision on availability with update captured in database without duplication.
+ The site will allow only the "manager", to set games in the schedule.
+ The site will allow only the "manager", to edit the game results.
+ The site will allow only the "manager", to delete games from the schedule.
+ Users can view team members for details of playing position and profile picture.
+ Users can view team game history with results and any upcoming fixtures.
+ Manager can view players available. 

#### Future Features

+ Ability for manager to dynamically organise team based on availability selection.
+ Email integration to auto send mails to players when new fixture entered by "manager".
+ Email integration to auto send mails to team members selected.
+ League table to integrate with results data. 

## Technologies used

#### Frameworks, Tools and Libraries

+ Materialize
+ Font Awesome
+ Google Fonts
+ Balsamiq
+ Github
+ MongoDB
+ Cloudinary for image storage

#### Languages

+ HTML
+ consistent
+ JavaScript
+ Python
+ Jinja

#### Tools

+ Github as version control
+ Heroku to host the site and application
+ Chrome deverloper tools for on going testing
+ Am I responsive to check site responsiveness
+ W3C Markup and CSS validators
+ PEP8 on line validator

## Testing

+ W3C Markup Validator

##### Match Team page

Validator identified stray tag but verified there is none there.

##### Game Result page

Validator identified issue with thead not allowed in table. Structure used 
from Materialize and site responds exactly as expected. Also mentioned stray tags but 
verified there are none there.
Checked line by line on opening and closing tags and looks correct.  

+ W3C CSS Validator

No errors found.

+ PEP8 online validator

All code is PEP8 compliant.

## Deployment

#### Application Deployment

The application is deployed on Heroku. This was accomplished by the following:

+ Create a requirements.txt file and a Procfile
+ Track these two files by committing to GitHub
+ Go to Heroku and create a new application
+ Navigate to the app and deploy using "GitHub" and link to the relevant repository, in this case "TomDillane/bulls_rugby_club"
+ Go to settings in Heroku and select "Reveal Config Vars"
+ Populate the following fields:

[Heroku config Wireframe](readme_images/heroku.config.png)

+ IP - set to 0.0.0.0
+ MONGO_DBNAME - set to bulls_rugby which is the name of the database
+ MONGO_URI - to get this, go to MONGODB Clusters, select "Connect", and choose "Connect your application"
+ Port - set to 5000
+ SECRET_KEY - set to secret key as per key generated and used in untracked file env.Python

+ Finally, navigate to "Deploy" and ensure that the master branch is selected






