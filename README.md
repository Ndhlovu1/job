# Job-Finder
A web application designed to help students find employment with prospective cheap labour market

## APPLICATION SCREENSHOTS
#### LANDING PAGE / LOGIN PAGE
![Screenshot from 2023-06-20 18-11-35](https://github.com/Ndhlovu1/job/assets/46927702/46feafe4-240e-4a43-98f1-78a9ea874c93)

#### REGISTRATION PAGE
![Screenshot from 2023-06-20 18-11-57](https://github.com/Ndhlovu1/job/assets/46927702/ef2b057e-3330-4db0-a389-b1b51048c8bc)

#### DASHBOARD PAGE
![Screenshot from 2023-06-20 18-12-13](https://github.com/Ndhlovu1/job/assets/46927702/09e6ba45-37d5-40ac-adf4-869966f71f99)

#### PROFILE EDIT PAGE
![Screenshot from 2023-06-20 18-12-27](https://github.com/Ndhlovu1/job/assets/46927702/26c5f240-264c-4dc4-b8df-967ed325c98a)

#### SIGNED OUT PAGE
![Screenshot from 2023-06-20 18-12-42](https://github.com/Ndhlovu1/job/assets/46927702/26f950ef-60cf-451e-a4c7-abec7731bb39)


#### FORGOT PASSWORD PAGE
![Screenshot from 2023-06-20 18-16-58](https://github.com/Ndhlovu1/job/assets/46927702/a016733b-5ab3-48e4-af70-759bd2cd8db2)

## Authentication
### Django Authentication Framework
It is found in the ```django.contrib.auth``` and it is added by default there are two middleware found in the MIDDLEWARE setting of the Project

##### Middleware are classes with methods that are globally executed during the request and responses phases

1. AuthenticationMiddleware - Links up User Request with Sessions
2. SessionMiddleware - Manages the current session across requests

#### THE DEFAULT MODELS FOUND IN THE AUTHENTICATION FRAMEWORK

1. User - User Model with basic fields: 
```username, password, email, first_name, last_name, isactive```

2. Group - A model to categorize Users

3. Permission - Flags for user or groups to be able to do certain tasks

### CREATING A LOGIN VIEW
TASKS
1. ACCEPT USER LOGIN THROUGH PASSWORD AND USERNAME
2. Verify if User is not blocked
3. Log into the website and begin authenticated session
4. Verify if User is registered in the database

--> Create a forms.py

Utilize the Cross Site Request Forgery (CSRF) to protect from Cyber Attacks

### Django Authentication Views
https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/urls.py

```python
from django.urls import path, include

path('', include('django.contrib.auth.urls'))
```

### User Registration
Visit the forms.py
```python
from django.contrib.auth.models import User
```

### User Profile
Handle Images for the Profile
```shell
pipenv install Pillow==7.0.0
or
pip install pillow==7.0.0
```

#### To allow Django to serve the images to uploaded by a User
Edit the settings.py and add the code beneath this
```python
MEDIA_URL = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
```
1. MEDIA_URL is the base URL used to serve the media files uploaded by users
2. MEDIA_ROOT is the local path where they reside. The Path is built dynamically to the project path


### Forms
1. UserEditForm - Allow Users to edit first name, last name, email, which are attributes of the built-in Django user model

2. ProfileEditForm - Allows users to edit their data that will be saved to the Profile's Table

### Front-End Development
1. Created Custom Navbar with Login & Logout Logic
2. Created the Design for the Login View

Below is a description of going through each field at a time for a ModelForm i.e. ```form.as_table```
```html
<tr>
    <td>{{ form.username.label_tag }}</td>
    <td>{{ form.username }}</td>
</tr>
<tr>
    <td>{{ form.password.label_tag }}</td>
    <td>{{ form.password }}</td>
</tr>
</table>
```

#### WHEN MIGRATING TO DIFFERENT PLATFORM SIMPLY CREATE A VIRTUAL ENV, THEN INSTALL ALL THE DEPENDENCIES
ALSO : YOU CAN DECIDE THE VERSION OF PIPENV TO USE i.e
```pipenv --python 3.8```







