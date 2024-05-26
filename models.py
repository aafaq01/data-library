# data-library/models.py

from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create a metadata object to pass to Alembic
metadata = Base.metadata
