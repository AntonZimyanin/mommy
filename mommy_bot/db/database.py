from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///../mommy_bot/facts.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


Base = declarative_base()


SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)