# Simple organizer
#### Django REST API + AngularJS

Please use Python 3.

## Quick start API

* Install all packages from [requirements.txt](requirements.txt)
* Run in command line:

```
python manage.py collectstatic
python manage.py makemigrations accounts diary task password budget contacts thumbnail
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### API endpoints
* `accounts/` - app Accounts
* `budget/` - app Budget
* `contacts/` - app Contacts
* `diary/` - app Diary
* `password-organizer/` - app Password Organizer
* `task/` - app Task

## Front part
In frontend used AngularJS