
<!-- Creating django Project -->

Django is a Python web framework that allows you to rapidly develop web applications.
Django uses the MVT (Model-View-Template) pattern, which is similar to MVC (Model-View-Controller) pattern.
Use the `django-admin startproject new_project` command to create a new project.
Use the `python manage.py runserver` command to run the project using the Django development web server.
Press `Ctrl-C (or Cmd-C)` to stop the Django development web server.

<!-- Saving installed versions and enables same installation on another pc -->

The requirements.txt file contains all dependencies for a specific Django project. It also contains the dependencies of dependencies.
Creating requirements.txt
`pip freeze > requirements.txt`

When you move the project to a new server e.g., a test or production server, you can install all the dependencies used by the current Django project using the following pip command:
`pip install -r requirements.txt`

<!-- Creating django App -->

To create an application, you use the startapp command as follows:
`python manage.py startapp app_name`
For example, you can create an application called blog using the startapp command like this: `python manage.py startapp blog`

<!-- Registering an app to project -->

After creating an application, you need to register it to the project especially when the application uses templates and interacts with a database.
To register the blog app, you add the `blog.apps.BlogConfig` class to the `INSTALLED_APPS` list in the `settings.py` of the project:
`INSTALLED_APPS = [ 'blog' ]`

