# models/tech_stack.py
from sqlalchemy import Column, Integer, String
from .base import Base

class TechStack(Base):
    __tablename__ = 'tech_stacks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
