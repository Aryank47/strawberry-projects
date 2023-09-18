from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from .base import Base


class Book(Base):
    title: Mapped[str] = Column(String, unique=True, nullable=False)
    author: Mapped[str] = Column(String)
