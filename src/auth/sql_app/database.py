import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MYSQL_HOST = os.getenv("MYSQL_HOST", '127.0.0.1')
MYSQL_USER = os.getenv("MYSQL_USER", 'root')
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", 'mdzz123456')
MYSQL_DB = os.getenv("MYSQL_DB", 'auth')
MYSQL_PORT = os.getenv("MYSQL_PORT", '3306')

MYSQL_HOST = '127.0.0.1'
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'mdzz123456'
# MYSQL_DB = 'auth'
# MYSQL_PORT = '3306'

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'\
    .format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()