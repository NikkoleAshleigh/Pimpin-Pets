# Pimpin Pets -Django Project

## Project Collaborators:

Nikkole Hardy - https://github.com/NikkoleAshleigh    
Ledarius Franklin - https://github.com/lederius   
Adrian Diaz - https://github.com/adiaz-banyan   
Allison Kroboth - https://github.com/42-allison-k   
Aryn Davis - https://github.com/aryndavis   
Lillie Schachter - https://github.com/lschachter   
Darien Davis - https://github.com/DDavis-CP   
Owen Arthur - https://github.com/owenarthur   
 
## To start building the project:

Once the user has cloned the repo and dedicate the repo in its respective directory:

### 1. Create a virtual environment

At the root folder of the repository run:
```
python3 -m venv venv
```
Make sure to call your virtual environment "venv"

### 2. Run virtual environment
#### On Windows:
Windows Powershell users:
```
venv\Scripts\activate.bat
```
Bash users:
```
source venv/Scripts/activate
```
#### On Unix or MacOS:
```
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run Django
```
python manage.py runserver
```
And go to `http://localhost:8000`

### How to use application:

Once user has loaded the sitem, they will initially view the homepage of the Pimpin Pets site. This page displays some images and some simple information about the site and two links as buttons. 
<!-- Pimpin homepage image -->
<!-- Furever Link Image -->
<img src="pimpin_main\pimpin_app\static\pawfrenceLink.png">
<div style="width:60px ; height:60px">
![Pawfrence Link](pimpin_main\pimpin_app\static\pawfrenceLink.png?raw=true "What's Your Pawfrence Link")
<div>
The first link takes the user to the Furever Homes page at the URL 
`http://localhost:8000/furever'. 
The Furever home page displays : .
<!-- Image -->
The second link takes the user to the What's Your Pawfrence page at the URL 
`http://localhost:8000/pawfrence/`. 
<div style="width:60px ; height:60px">
![Pawfrence Page](pimpin_main\pimpin_app\static\pawfrencePage.png?raw=true "What's Your Pawfrence Page")
<div>
The What's Your Pawfrence page displays a form designed to be a message in which the user may fill out the fields given. Once the form has been filled out correctly, the contact's first name in which the form was intended will then be displayed in an unordered list. The user can then, click on any name and will be redirected to the message's detail page at the URL 
`http://localhost:8000/pawfrence/<user id>`.
<div style="width:60px ; height:60px">
![Pawfrence Detail Page](pimpin_main\pimpin_app\static\pawfrenceDetailPage.png?raw=true "Pawfrence Detail Page")
<div>
The message datail page displays a form pre-filled with the information given by the user with which they may edit or delete altogether using either the update or delete buttons displayed. There is also a text box in which the user can make their own descriptive tag about the pet in which they are reffering. Then upon clicking the Add button, the descriptive tag is displayed in an unordered list beneath the text box in which it was written. 
<div style="width:60px ; height:60px">
![Adding a Tag](pimpin_main\pimpin_app\static\addingTag.png?raw=true "Adding A Tag")
<div>
<div style="width:60px ; height:60px">
![Tag Added](pimpin_main\pimpin_app\static\tagAdded.png?raw=true "Tag Added")
<div>