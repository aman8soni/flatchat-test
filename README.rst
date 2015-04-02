test app for flatchat intern hiring
========

Installation
--------

**Create a new virtualenv**

Find a Python 2.7 executable using ``python --version`` and ``which python``.

Run this command once:

::

  mkvirtualenv -p /full/path/to/python2.7 my_app
  workon my_app

where the result of ``which python`` can be used instead of ``/full/path/to/python2.7``,
and where ``my_app`` is the name of the new virtualenv.

**Install Fabric**

Fabric is a build and deployment tool that uses the Python language for its scripts.
Though the product name is 'Fabric', the command line tool is 'fab'.

::

  cd my_app
  pip install python-dev
  pip install python-setuptools
  pip install fabric

See also: http://www.fabfile.org/installing.html

**Install required Python packages**

::

  cd my_app
  cd ~/my_app
  fab update_env

**Initialize the Database**

::

  cd my_app
  cd ~/my_app
  fab reset_db         # Warning: This will delete all data in the database!

**Update configuration settings**

Before we can use this application, we will have to configure the database URL

Instead of editing app/config/settings.py and checking in sensitive information into
the code repository, these settings can be set using OS environment variables
in your ``.bashrc`` or ``.bash_profile`` shell configuration file.

::

    export DATABASE_URL='sqlite:///app.sqlite'
    export ADMIN1='"Admin One" <admin1@example.com>'


Running the app
--------

**Start the development webserver**

Flask comes with a convenient WSGI web application server for development environments.

::

  cd my_app
  cd ~/my_app
  fab runserver

Point your web browser to http://localhost:5000/

``fab reset_db`` will create one user with username 'admin' and password 'Password1'.
