# The 'fabfile.py' is used by Fabric and must reside in the application root directory.

from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from contextlib import contextmanager


@task
def update_env():
    """
    Install required Python packages using pip and requirements.txt
    """
    local('pip install -r requirements.txt')


@task
def reset_db():
    """
    Drop all tables, Create empty tables, and populate tables
    """
    local('PYTHONPATH=. python app/startup/reset_db.py')

@task
def runserver():
    """
    Start the web application using a development WSGI webserver provided by Flask
    """
    local('python runserver.py')


@task
def deploy():
    """
    Deploy web application to Heroku.
    Requires: heroku git:remote -a PROJECTNAME
    """
    local('git push heroku master')
