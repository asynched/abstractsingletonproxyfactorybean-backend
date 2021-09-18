from os import environ
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = environ.get('SECRET_KEY')
ENVIRONMENT = environ.get('ENVIRONMENT')
DEFAULT_DATABASE = environ.get('DEFAULT_DATABASE')
DATABASE_USERNAME = environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = environ.get('DATABASE_PASSWORD')
DATABASE_CONNECTION_STRING = environ.get('DATABASE_CONNECTION_STRING')
