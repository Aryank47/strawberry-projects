from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from sample_project.core import settings


class DB:
    @property
    def engine(self) -> Engine:
        assert settings.SQLALCHEMY_DATABASE_URI
        return create_engine(settings.SQLALCHEMY_DATABASE_URI)

    @property
    def session(self) -> Session:
        session_maker = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
            expire_on_commit=True,
        )
        return session_maker()


db_obj = DB()
