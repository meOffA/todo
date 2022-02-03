import os
import urllib
from sqlalchemy import create_engine

driver = "{ODBC Driver 17 for SQL Server}"
server = "dbtodo.database.windows.net"
database = "adamtodo123"
user = "adamtodo123"
password = "Qwerty12#"

conn = f"""Driver={driver};Server=tcp:{server},1433;Database={database};
Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

params = urllib.parse.quote_plus(conn)
conn_str = 'mssql+pyodbc:///?autocommit=true&odbc_connect={}'.format(params)
#engine = create_engine(conn_str, echo=True)

#print(engine.table_names())


class BaseConfig:
    DEBUG = False
    SECRET_KEY = '\xb2\xae\x00\x87\x00\xde\x16L\xa1PD\\\xe7\xcf\x8b\x11'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = conn_str



class DevelopmentConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = conn_str


class ProductionConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = conn_str
    



config = {
    'dev': 'config.DevelopmentConfig',
    'prod': 'config.ProductionConfig'
}
