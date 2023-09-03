from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from sample_project.core import settings


class DB:
    @property
    def engine(self) -> Engine:
        return create_engine(settings.SQLALCHEMY_DATABASE_URI)

    @property
    def session(self) -> Session:
        session_maker = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        return session_maker()
