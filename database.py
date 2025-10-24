from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Soumya@localhost/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
