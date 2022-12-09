from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SECRET_KEY = 'afernandez-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser='postgres@jseijas-dbsrv.postgres.database.azure.com',
    dbpass='Pa$$w0rd1990',
    dbhost='jseijas-dbsrv.postgres.database.azure.com',
    dbname='afernandez-assignment-prod-db'
    )

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser='postgres@jseijas-dbsrv.postgres.database.azure.com',
    dbpass='Pa$$w0rd1990',
    dbhost='jseijas-dbsrv.postgres.database.azure.com',
    dbname='afernandez-assignment-dev-db'
    )
    DEBUG = True

