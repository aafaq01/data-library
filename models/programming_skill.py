# models/programming_skill.py
from sqlalchemy import Column, Integer, String
from .base import Base

class ProgrammingSkill(Base):
    __tablename__ = 'programming_skills'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(String)
