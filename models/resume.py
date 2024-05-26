# models/resume.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, index=True)
    file_path = Column(String)
