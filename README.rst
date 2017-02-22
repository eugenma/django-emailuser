=====
Users
=====

Users is a simple Django app which uses email address to identify users instead of an username.

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


