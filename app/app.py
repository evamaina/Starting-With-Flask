from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
'''
We pass in instance_relative_config which allow us to connect
to the instance/ folder when the app instance is created.
The app.config.from_pyfile('config.py') connects to the config.py
file and all its contents are appended to the app.config.
We then store the movie base URL inside the app/config file.
'''
# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views


'''
To make our application use the new configuration we import
our DevConfig subclass in our __init__.py file.
 We then useapp.config.from_object() method to set up configuration
  and pass in the DevConfig subclass.
  '''


