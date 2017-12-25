import os
from os.path import dirname, join
from distutils.util import strtobool
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

DEBUG = strtobool(os.environ.get('DEBUG'))
SECRET_KEY = os.environ.get('SECRET_KEY')

MEETUP_API = os.environ.get('MEETUP_API')
REFRESH_EVENTS = int(os.environ.get('REFRESH_EVENTS'))