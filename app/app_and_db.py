# This file declares the Flask Singletons 'app' and 'db'
# 'app' and 'db' are defined in a separate file to avoid circular imports
# Usage: from app.app_and_db import app, db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This is the WSGI compliant web application object
app = Flask(__name__)

# This is the SQLAlchemy ORM object
db = SQLAlchemy(app)
