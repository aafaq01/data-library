# models/soft_skill.py
from sqlalchemy import Column, Integer, String
from .base import Base

class SoftSkill(Base):
    __tablename__ = 'soft_skills'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
