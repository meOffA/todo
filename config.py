import os


class BaseConfig:
    DEBUG = False
    SECRET_KEY = '\xb2\xae\x00\x87\x00\xde\x16L\xa1PD\\\xe7\xcf\x8b\x11'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class DevelopmentConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    
class ProductionConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    

config = {
    'dev': 'config.DevelopmentConfig',
    'prod': 'config.ProductionConfig'
}
