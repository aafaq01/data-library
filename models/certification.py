# models/certification.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Certification(Base):
    __tablename__ = 'certifications'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    issuing_organization = Column(String)
    issue_date = Column(String)
    expiration_date = Column(String, nullable=True)
