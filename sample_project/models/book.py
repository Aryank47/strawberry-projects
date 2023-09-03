from sqlalchemy import Column, String

from .base import Base


class Book(Base):
    title: Column[str] = Column(String, unique=True, nullable=False)
    author: Column[str] = Column(String)
