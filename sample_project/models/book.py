from sqlalchemy import Column, String

from .base import Base


class Book(Base):
    title: str = Column(String, unique=True, nullable=False)
    author: str = Column(String)
