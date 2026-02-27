
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base ,sessionmaker
engine = create_engine('sqlite:///quiz.db', echo=False)
SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    return SessionLocal()
