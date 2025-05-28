from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///sports.db")
engine = create_engine("sqlite:///app.db")  # this creates a file named app.db in the root of your project

Session = sessionmaker(bind=engine)
Base = declarative_base()
