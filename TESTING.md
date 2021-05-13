# Testing

## Code Validation

+ W3C Markup Validator

No errors found. Warnings relating to headings is acknowledged and choice is to proceed with layout as intended.

[HTML validator](readme_images/html_validator.png) 

+ W3C CSS Validator

No errors found.

[CSS validator](readme_images/css_validator.png)

+ JS validator

No errors. 

[JS validator](readme_images/js_validator.png)

+ PEP8 online validator

All code is PEP8 compliant.

[PEP8 validator](readme_images/css_validator.png)

## Site Performance 

The site performance was good as tested over different devices with screens of varying resolulions.

[Device testing](readme_images/device_speed_test.png)

I tested the site on Chrome, Edge, Safari using different devices with no issues in either function or performance. 

## Site Function Testing

### Game availability button and function

+ Expected "Game Availability" Button only be available for user type "player"
+ Actual result - button only available for user type "player".
+ Expected "Game Availability" form to allow user to choose date for games with result TBC only, and "available / unavailable". 
 If "available" selected, option on where to meet appears.
+ Actual result - only games with result "TBC", available in dropdown and if available selected, drop down on "meet", appears.
+ Expected form to empty on submission for subsequent game availability selection.
+ Actual result - form empties and subsequent elections on availability can be made.
+ Expected update to availability of particular player on given date to update previous choice and not duplicate.
+ Actual result - changing choice results in update in database and not duplication of record.

### Game Result Edit and Game Remove

+ Expected "Edit", button to take "manager", to score update form
+ Actual result - manager is taken to score update form
+ Expected submission of score to take manager user back to home page
+ Actual result - manager is returned to home page
+ Expected result to be captured in database and reflected on relevant page
+ Actual result - database updated and relevant result page displaying correct score
+ Expected "Remove", button to remove game from database and relevant result table
+ Actual result - game removed from table and relevant result page
+ Expected user "manager", to be returned to game schedule form
+ Actual result - user "manager", is returned to game schedule form

### Sign up function

+ Expected username field to flash message and return user to sign up form if not unique username
+ Actual result - flash message and user returned to sign up form
+ Expected password to be min 5 and max 15 characters with alpha upper, lower and numbers allowed
+ Actual result - password between 5 and 15 with alpha upper, lower and numbers allowed
+ Excpected selection of membership type "player", to trigger dropdowns for gender, position, profile pic
+ Actual result - selection of membership type "player", triggered dropdowns for gender, position, profile pic
+ Expected to be taken to login page on submission
+ Actual result - on submission, returned to login page

### Log In

+ Expected field to flash message and return user to log in form if username / password incorrect
+ Actual result - flash message and returned user to log in form

### Game schedule

+ Expected form only to be available to user "manager"
+ Actual result - form only available to user "manager"
+ Expected flash message and form clears on submission
+ Actual result - flash messaged and form cleared on submission

## General testing

+ Clicked through the site as each user type and all pages opened
+ No reliance on back button
+ Links opened in a new tab
+ Flash messages worked on each page as Expected

## User Stories

### First Time Users

+ I want to get an overview of the club
+ Result - overview available along with team detail
+ I want to see latest fixtures and results related to the club teams
+ Result - Team results available along with fixtures
+ I want the option to join the club
+ Result - signup option available
+ I want the option to join a team in the club
+ Result - option to join a team at sign up

### Returning Users

+ I want to be able to log in
+ Result - log in for returning users
+ I want to be able to edit my game availability
+ Result - ability to update and amend availability for game schedule for players
+ I want to see latest fixtures and results related to the club teams
+ Result - latest fixtures and results available

### Manager Users

+ I want to be able to update latest results
+ Result - facility to update game results for the user "manager"
+ I want to be able to view all player availability for games
+ Result - player availability per game captured in database and presented in page to manager
+ I want to be able to remove games from the schedule
+ Result - button for manager to remove games from schedule
+ I want to grow the club membership
+ Result - subjective but with ability to join club and team, I believe membership of team will grow
+ I want to keep up to date on team memebership
+ Result - ability to view team make up

#### Site Owner

+ I want to attract and retain players and supporters
+ Result - subjective but I believe is successful
+ I want a site where users can get information on the club teams
+ Result - team details along with players available including fixtures and results
+ I want players to be able to register for a team
+ Result - ability to join teams
+ I want players to be able to opt in for availability for games
+ Result - ability for players to self serve for their own availability
+ I want the team manager to be able to see player availability
+ Result - manager can view player availability
+ I want the team manager to be able to set the game schedule
+ Result - manager sets schedule
+ I want the team manager to be able to update results and remove games
+ Result - manager can remove games from schedule and database