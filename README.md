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
There are four collections:

1. Membership
2. Team
3. News
4. NewsLetter


[Database Wireframe](readme_images/database_v1.png)


##### Membership

This allows a new user to become a member of the club. The name, email and password
are captured for log in.
Where membership type of "Player", is selected, the user will be 
directed to the player form where playing position and date of birth must be selected.
Gender will direct to the relevant team.
The options of "Volunteer", and "Social", are for the club management to use for event organisation.

##### Team

This will only apply where "Player", is selected at the "Sign Up", stage.
The user will populate their playing position, DOB and whether they are available to play currently or not.
This will be available for editing by the user so that the team manager has a current state for each player.


##### News

This will only be available for editing by the site admin. It will contain 
latest club updates such as team results, upcoming fixtures and social events.

##### NewsLetter

This will allow users to the site to sign up for a regular newsletter. It will not require sign up to the club.



### Skeleton Plane 

The site will have 7 pages. There will be no reliance on the back button. 
The user will at any point be able to log out or sign up / sign in.

### Surface Plane

The site's colors, typography and layout will be consistent and in line with the club's colors.


