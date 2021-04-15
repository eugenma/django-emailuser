
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

TODO


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


