
=====
Users
=====

Django email_users is a simple Django app which uses email address to identify users instead of the username.

Requirements
---------------
Package was tested with 

* Python 3.6, 3.7, 3.8
* Django 3.0, 3.1, 3.2


If you intend to use it with Django Rest Framework then following versions were tested

3.13.1


Installation 
-------------
For pip use the following command

   $ pip install git+https://github.com/eugenma/django-emailuser.git#egg=django-emailuser

Quick start
-----------
1. Add 'email_user' to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
        ...
        'email_user',
   ]

2. Set AUTH_USER_MODEL to 'email_user.EmailUser' in settings like this::

   AUTH_USER_MODEL = 'email_user.EmailUser' 

3. Run `python manage.py migrate` to create the models.


Settings
-------------
All settings are stored within the dictionary `DJANGO_EMAIL_USER`. The values are

* `STORE_METHOD` configuration of the email case handling

  The possible values are

  * `exact` - save the email as is without modifying the case,
  * `lower` - convert everything to lower case,
  * `normalize` - calls `BaseUserManager.normalize_email() <https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email>`_.
    This is the behaviour of the previous versions.

  Take care if you change this config in a running project. It changes the way how the fields are stored and retrieved.
