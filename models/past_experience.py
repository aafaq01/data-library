# models/past_experience.py
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class PastExperience(Base):
    __tablename__ = 'past_experiences'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    description = Column(Text)
    start_date = Column(String)
    end_date = Column(String, nullable=True)
