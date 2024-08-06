import sys
import os

# Add your project directory to the sys.path
project_home = '/home/juanduqueo/music-genre-classifier'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set the Flask app's environment variable
os.environ['FLASK_APP'] = 'app.py'

# Import the Flask app
from app import app as application