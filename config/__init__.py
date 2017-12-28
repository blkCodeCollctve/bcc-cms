import os
from os.path import dirname, join
from distutils.util import strtobool
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

# Django
DEBUG = strtobool(os.environ.get('DEBUG'))
SECRET_KEY = os.environ.get('SECRET_KEY')

# Meetup
MEETUP_API = os.environ.get('MEETUP_API')
REFRESH_EVENTS = int(os.environ.get('REFRESH_EVENTS'))

# Database
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
HEROKU_DB_URL = os.environ.get('DATABASE_URL')
