import logging
from flask_user import UserManager, SQLAlchemyAdapter

def init_app(app, db, extra_config_settings={}):
    """
    Initialize Flask applicaton
    """

    # Initialize app config settings
    app.config.from_object('app.startup.settings')          # Read config from 'app/startup/settings.py' file
    app.config.update(extra_config_settings)                # Overwrite with 'extra_config_settings' parameter
    if app.testing:
        app.config['WTF_CSRF_ENABLED'] = False              # Disable CSRF checks while testing

    # Setup Flask-User to handle user account related forms
    from app.users.models import UserAuth, User
    from app.users.forms import MyRegisterForm
    from app.users.views import user_profile_page
    db_adapter = SQLAlchemyAdapter(db, User,        # Setup the SQLAlchemy DB Adapter
            UserAuthClass=UserAuth)                 #   using separated UserAuth/User data models
    user_manager = UserManager(db_adapter, app,     # Init Flask-User and bind to app
            register_form=MyRegisterForm,           #   using a custom register form with UserProfile fields
            user_profile_view_function = user_profile_page,
            )

    # Load all models.py files to register db.Models with SQLAlchemy
    from app.users import models

    # Load all views.py files to register @app.routes() with Flask
    from app.pages import views
    from app.users import views

    return app
