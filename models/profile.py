# models/profile.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
