import strawberry
from fastapi import APIRouter, FastAPI
from fastapi_sqlalchemy.middleware import DBSession
from strawberry.extensions import Extension
from strawberry.fastapi import GraphQLRouter

from sample_project.core import settings
from sample_project.core.db import db_obj
from sample_project.graphql import DataMutation, DataQuery

# strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()
# strawberry_sqlalchemy_mapper.finalize()


app = FastAPI(title=settings.PROJECT_NAME)
app.add_middleware(DBSession, db_url=settings.SQLALCHEMY_DATABASE_URI)


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["session"] = db_obj.session

    def on_request_end(self):
        self.execution_context.context["session"].close()


schema = strawberry.Schema(
    query=DataQuery, mutation=DataMutation, extensions=[SQLAlchemySession]
)

graphql_app: APIRouter = GraphQLRouter(schema=schema)
app.include_router(graphql_app, prefix="/graphql")
