# models/contact.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    phone = Column(String)
    address = Column(String)
