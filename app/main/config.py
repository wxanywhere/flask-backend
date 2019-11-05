import os
from pathlib import Path 
from dotenv import load_dotenv

# load_dotenv
# load_dotenv(verbose=True)

# os.path.abspath(os.curdir)
# env_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..\..', '.env'))
# env_path = os.path.join(os.path.abspath(os.curdir), '.env')
env_path = os.path.abspath(os.path.join(Path('.'), '.env'))
if os.path.exists(env_path):
    load_dotenv(env_path)

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def create_db_url(user, password, host, port, db):
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


def get_env_db_url(env_setting="dev"):
    POSTGRES_USER = get_env_variable("POSTGRES_USER")
    POSTGRES_PASSWORD = get_env_variable("POSTGRES_PASSWORD")
    POSTGRES_HOST = get_env_variable("POSTGRES_HOST")
    POSTGRES_PORT = get_env_variable("POSTGRES_PORT")
    postgres_db = get_env_variable("POSTGRES_DB")
    if env_setting == "test":
        postgres_db = get_env_variable("POSTGRES_TEST_DB")
    return create_db_url(
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, postgres_db)


# DB URIS for each Environment
DEVELOPMENT_DB_URI = get_env_db_url()
TEST_DB_URI = get_env_db_url("test")
PRODUCTION_DB_URI = get_env_db_url("prod")


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DEVELOPMENT_DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DB_URI
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = PRODUCTION_DB_URI


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
