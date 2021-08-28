import os

DEBUG = False
SECRET_KEY = 'c9144660f9768975e97e06cb'

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = os.environ[uri]
SQLALCHEMY_TRACK_MODIFICATIONS = False