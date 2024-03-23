# Forge Fitness (Capstone Project)

![index](/readme/assets/index.png)

[ForgeFitness](https://forge-fitness-abbd672aefb0.herokuapp.com) is a website that provides information about the gym, its locations, classes and staff to potential clients that wish to join their gym service. The overall goal of the site is to increase awareness of the brand and create a community, which would provide both monetary  and intangible value such as reputation in the businesses future. 

## Table of contents

* [Purpose](#purpose)
* [UX Design](#ux-design)
  * [User Stories](#user-stories)
  * [Structure](#structure)
* [Wireframes](#wireframes)
* [Design](#design)
* [Agile Development Plan](#agile-development-plan)
* [Database](#database)
* [Features](#features)
  * [Future Features](#future-features)
* [Testing](#testing)
  * [User Story Testing](#user-story-testing)
  * [Manual Testing](#manual-testing)
  * [Automated Testing](#automated-testing)
      * [Code Validation](#code-validation)
      * [Lighthouse](#lighthouse)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Programs Frameworks Libraries](#Programs-Frameworks-Libraries)
* [Deployment](#deployment)
* [Credits](#credits)

# Purpose
This website was designed as a capstone project for the Code Institute's Full Stack Developer Bootcamp. In keeping with Code Institute's Learning Objectives, this ReadMe covers both the development process for other developers understanding as well as sign posting where Learning Objectives have been met. 

# UX Design
## User stories
Target Audience:

- Fitness Beginners who are looking for their first gym that will provide a friendly and proffesional service.
- Athletes who are already committed, but need the neccessary equipment to train. 
- Personal Trainers who are looking for work that see an opportunity to join the gym and create their workflow.

The first two types of users are currently catered for within the scope of the website. The third, Personal Trainers, would require an admin to provide them with staff priviliges to create their gym classes for other users to view. 

### As a **first time user:**

- I want to be able to navigate the entire site regardless of device
- I want to create an account to interact with the site
- I want to easily log out and log back in
- I want a visual cue that after interacting with the site, something has happened
- I want to be able to navigate to all pages easily
- I want content that is only available to registered users 
- I want to view the gym classes 
- I want to comment and review the gym classes 
- I want to delete comments and reviews
- I want to be able to edit my profile to my liking
- I want to be able to delete my profile
- I want to pick the level of membership I want
- I want visual clarity/cues for when I am logged in or out
- I want to contact your business easily

### As a **returning user:**

- I want my data to be secure
- I want to check my profile & setting details easily
- I want to update my profile or settings if needed
- I want to delete my profile if needed
- I want to be able to reset my password 

## Structure

![](readme/assets/index.png)

User stories covered:
- I want to be able to navigate the entire site regardless of device  *Fulfilled by Nav bar and Footer*
- I want a visual cue that after interacting with the site, something has happened  *Users will be redirected here with a message alert with the event success or failure*
- I want content that is only available to registered users *The Login and Register Buttons will alternate to Profile/Logout and Profile Picture on larger screens*
- I want visual clarity/cues for when I am logged in or out *The Login and Register Buttons will alternate to Profile/Logout and Profile Picture on larger screens*
- I want to pick the level of membership I want *Future Feature - Users have the cards available with the memberships. If an ecommerce model was added, the HTML template is ready*

![](readme/assets/gymclasses.png)
User stories covered:
- I want to view the gym classes *Each post will be visible regardless of user authentication*

![](readme/assets/gymclasspost.png)
User stories covered:
- I want to comment and review the gym classes *When logged in, a "Add Comment" button will appear. All comments are visible to users!*
- I want to delete comments and reviews *An Edit/Delete button will appear if the user who made the comment is logged in*
- I want content that is only available to registered users *The Create/Edit/Delete is only available to registered users*

![](readme/assets/register.png)
User stories covered:
- I want to create an account to interact with the site *Upon providing the information requested, a User will be created alongside a Profile*
- I want my data to be secure *Using Form Validation from Django for password which will encrypt your information* 

![](readme/assets/login.png)
User stories covered:
- I want to easily log out and log back in *A quick login page and Logout will redirect you to the homepage in a logged out state*

![](readme/assets/editprofile.png)
User stories covered:
- I want to be able to edit my profile to my liking *Users will be prompted to fill this in after the base User form. You can edit this to your liking*
- I want a visual cue that after interacting with the site, something has happened *Users will be redirected to homepage with a message alert with the event success or failure*

![](readme/assets/editsettings.png)
User stories covered:
- I want to be able to reset my password *Users can change their password here, assuming it is a valid format while logged in. Other users cannot access this area as it is specific to your logged in user*
- I want to update my profile or settings if needed *Settings can be changed here for first name, second name, username, password and email* 
- I want a visual cue that after interacting with the site, something has happened *Users will be redirected to homepage with a message alert with the event success or failure*

![](readme/assets/profile.png)
User stories covered:
- I want to be able to edit my profile to my liking *Users will be prompted to fill this in after the base User form. You can edit this to your liking*
- I want to be able to delete my profile *Takes the user to a delete profile page where they confirm the deletion*
- I want visual clarity/cues for when I am logged in or out *The Profile page and edit sections are only available to logged in users*
- I want to delete comments and reviews *IF a user deletes their profile, all comments/reviews will be deleted as well*
- I want to check my profile & setting details easily *Users will see a basic rundown of their information on the page*
- I want a visual cue that after interacting with the site, something has happened *Users will see the changes from their settings/profiles here*

![](readme/assets/contact.png)
User stories covered:
- I want to contact your business easily






# Wireframes

# Design

# Agile Development Plan

# Database

# Features
## Future Features

# Testing
## User Story Testing
## Manual Testing
## Automated Testing
### Code Validation
### Lighthouse

# Technologies
## Languages
## Programs Frameworks Libraries

# Deployment

# Credits
