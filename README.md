# Django School Management System
This is an open-source school management system API developed using Django and the Django REST framework. It is designed to manage school or college operations, offering APIs for administration, admissions, attendance, scheduling, and results. Additionally, it provides various user permissions to access different applications based on their access levels.


# Quick Install
You should have at least basic django and django-rest framework experience to run django-project. We test only in PostgreSQL database.

### Create a virtual environment

There are several ways depending on the OS and package you choose. Here's my favorite  
`sudo apt-get install python3-pip`  
`pip3 install virtualenv`  
Then either  
`python3 -m venv venv`  
or  
`python -m venv venv`  
or  
`virtualenv venv` (you can call it venv or anything you like)

#### Activate the virtual environment  

in Mac or Linux
`source venv/bin/activate`  
in windows
`venv/Scripts/activate.bat`  

# Apps

*School Information System (SIS)*
This module manages student data along with their parent/guardian and contact information. It also includes records for basic class details and school year information. As the core module of django-scms, it is essential for the functionality of any other module, while all other modules remain optional.

*Admissions*
This module monitors prospective students and their registration procedures. It facilitates the addition of various admission levels and tracks the steps required to progress through these levels. Additionally, it records any open houses attended by the student and the sources through which they learned about the school.

