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
- I want content that helps build the brand or business
- I want to view the gym classes 
- I want to comment and review the gym classes 
- I want to mark myself as attending gym classses
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

For this section, each page will have a screenshot, a rationale for the page  & the user stories (where applicable) covered by the page.

![](readme/assets/index.png)

**Rationale:**

This page serves to provide the user with the purpose of the site, a hub to direct users around the site after forms and signposting that we want users to register.

**User stories covered:**
- I want to be able to navigate the entire site regardless of device  *Fulfilled by Nav bar and Footer*
- I want a visual cue that after interacting with the site, something has happened  *Users will be redirected here with a message alert with the event success or failure*
- I want content that is only available to registered users *The Login and Register Buttons will alternate to Profile/Logout and Profile Picture on larger screens*
- I want visual clarity/cues for when I am logged in or out *The Login and Register Buttons will alternate to Profile/Logout and Profile Picture on larger screens*
- I want to pick the level of membership I want *Future Feature - Users have the cards available with the memberships. If an ecommerce model was added, the HTML template is ready*

![](readme/assets/gymclasses.png)

**Rationale:**

This page serves to provide the user with information on premium services that are on offer for members alongside an output for Personal Trainers for the gym classes they host.

**User stories covered:**
- I want to view the gym classes *Each post will be visible regardless of user authentication*

![](readme/assets/gymclasspost.png)

**Rationale:**

This page serves to provide the user with additional information on that specific gym class and interacting with other users. In future I would like this page to record attendance and allow Personal Trainers to show their team credentials and information. 

**User stories covered:**
- I want to comment and review the gym classes *When logged in, a "Add Comment" button will appear. All comments are visible to users!*
- I want to delete comments and reviews *An Edit/Delete button will appear if the user who made the comment is logged in*
- I want content that is only available to registered users *The Create/Edit/Delete is only available to registered users*

![](readme/assets/register.png)

**Rationale:**

This page serves to provide the user the option to register with the website

**User stories covered:**
- I want to create an account to interact with the site *Upon providing the information requested, a User will be created alongside a Profile*
- I want my data to be secure *Using Form Validation from Django for password which will encrypt your information* 

![](readme/assets/login.png)

**Rationale:**

This page serves to provide the user the option to login to the site.

**User stories covered:**
- I want to easily log out and log back in *A quick login page and Logout will redirect you to the homepage in a logged out state*

![](readme/assets/editprofile.png)

**Rationale:**

This page serves to provide the user with additional aspects of their profile they can edit. This allows users to stand out with their profile pictures, alongside basic details for the gym to hold. 

**User stories covered:**
- I want to be able to edit my profile to my liking *Users will be prompted to fill this in after the base User form. You can edit this to your liking*
- I want a visual cue that after interacting with the site, something has happened *Users will be redirected to homepage with a message alert with the event success or failure*

![](readme/assets/editsettings.png)

**Rationale:**

This page serves to provide the user with the ability to edit your registration information in the event of a mistake or needing a change. 

**User stories covered:**
- I want to be able to reset my password *Users can change their password here, assuming it is a valid format while logged in. Other users cannot access this area as it is specific to your logged in user*
- I want to update my profile or settings if needed *Settings can be changed here for first name, second name, username, password and email* 
- I want a visual cue that after interacting with the site, something has happened *Users will be redirected to homepage with a message alert with the event success or failure*

![](readme/assets/profile.png)

**Rationale:**

This page serves to provide the user with a hub for everything about their profile in a private area. In the future, I would like this to include a users membership information and the ability to change their finanical information. 

**User stories covered:**
- I want to be able to edit my profile to my liking *Users will be prompted to fill this in after the base User form. You can edit this to your liking*
- I want to be able to delete my profile *Takes the user to a delete profile page where they confirm the deletion*
- I want visual clarity/cues for when I am logged in or out *The Profile page and edit sections are only available to logged in users*
- I want to delete comments and reviews *IF a user deletes their profile, all comments/reviews will be deleted as well*
- I want to check my profile & setting details easily *Users will see a basic rundown of their information on the page*
- I want a visual cue that after interacting with the site, something has happened *Users will see the changes from their settings/profiles here*

![](readme/assets/contact.png)

**Rationale:**

This page serves to provide all users with an easy way to communicate to the business with any queries. 

**User stories covered:**
- I want to contact your business easily

![](readme/assets/ourclubs.png)
![](readme/assets/ourteam.png)

**Rationale:**

These pages serves to provide users with additional information to build trust, ultimately resulting in a user converting by registering. In future, they would be interlinked with the gym classes provided with the respective locations and staff information running the class.

**User stories covered:**
- I want content that helps build the brand or business

# Wireframes

My wireframes were my rough initial designs. I have made alterations to the templates to benefit user experience when using the site depending on their device or my own limitations with time and implementation after my first meeting with my tutor. For example, removing profile pictures on mobile due to the condensed and busy design or Classes with functionality. 

For wireframes intended purpose, I have tried to stay as close as possible to the initial ideas. Any other pages are built using All Auth's base templates or developed using the base.html that is shown via the home page wireframe. 

### Home Page 
<details><summary>click to expand</summary>
<img src="readme/assets/wireframes/wf-index.png">
</details>

### Our Clubs
<details><summary>click to expand</summary>
<img src="readme/assets/wireframes/wf-our-clubs.png">
</details>

### Classes 
<details><summary>click to expand</summary>
<img src="readme/assets/wireframes/wf-classes.png">
</details>

### Team
<details><summary>click to expand</summary>
<img src="readme/assets/wireframes/wf-team.png">
</details>

### Profile
<details><summary>click to expand</summary>
<img src="readme/assets/wireframes/wf-profile.png">
</details>

# Design

The website is intended to have a simple layout with emphasis on clean, readable designs. 

During the initial planning stage of the project, I settled on the following: 

- A black background.
- White text to compliment the black background.
- Using btn-success (Green) for Register and btn-primary (Blue) for Profile as an easy visual cues for users.
- Bootstrap for layout of pages. This is due to my familiarity with the frontend framework over other available frameworks.
- Default text fonts provided by Bootstrap. This is due to accessability and usability while being practical with time.
- The logo colours and typography can be found in this document: <details><summary>click to expand</summary>
<img src="readme/assets/brandguidelines.png">
</details>

The intention behind these choices are to create a modern, trendy website that fits the rural/techno vibes of the locations while also appealing to athletes as it does what it says on the tin without needing to make bold design choices. A simple, clean design!


# Agile Development Plan

Utilising an agile methodology, I have used MoSCoW prioritization within a Github project kanban board to track user stories and features. This approach enabled me to develop the Minimal Viable Product early on and then begin to prioritise my time within the project to the absolutely neccassary features for users. 

I used the following:

- Must-Have
- Should-Have
- Could-Have
- Won't-Have
- Feature (This was an extra to help identify features vs user stories criteria)

The development cycle over the course of this project has allowed me to cover the majority of user stories (Done Section), however some remain as future features (Future features section) such as attendance, e-commerce intergration and staff setting up gym classes which provides their details. As I have been working, I was slowly progressing the User Stories across the project board from Todo and In Progress respectively. (Admittedly I could have and likely should have used this more as the project expanded, future learnings for myself!)

[See the project here.](https://github.com/users/Karlsberg62/projects/6)

# Database

![My initial database model](readme/assets/DatabaseGraph.png)

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
