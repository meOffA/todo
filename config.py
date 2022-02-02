import os


class BaseConfig:
    DEBUG = False
    SECRET_KEY = '\xb2\xae\x00\x87\x00\xde\x16L\xa1PD\\\xe7\xcf\x8b\x11'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:dbtodo.database.windows.net,1433;Database=adamtodo123;Uid=adamtodo123;Pwd=Qwerty12#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'



class DevelopmentConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:dbtodo.database.windows.net,1433;Database=adamtodo123;Uid=adamtodo123;Pwd=Qwerty12#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'


class ProductionConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'Driver={ODBC Driver 13 for SQL Server};Server=tcp:dbtodo.database.windows.net,1433;Database=adamtodo123;Uid=adamtodo123;Pwd=Qwerty12#;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'



config = {
    'dev': 'config.DevelopmentConfig',
    'prod': 'config.ProductionConfig'
}
