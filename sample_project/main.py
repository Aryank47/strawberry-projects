import strawberry
from fastapi import Depends, FastAPI
from fastapi_sqlalchemy.middleware import DBSessionMiddleware
from sqlalchemy_utils import database_exists
from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from sample_project.core.db import DB
from sample_project.graphql import DataQuery
from sample_project.models import Base

if not database_exists(DB.engine.url):
    Base.metadata.create_all(bind=DB.engine)


def custom_context_dependency():
    return DB.session


async def get_context(custom_value=Depends(custom_context_dependency)):
    return {"session": custom_value}


strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()
strawberry_sqlalchemy_mapper.finalize()


app = FastAPI()


app.add_middleware(DBSessionMiddleware, custom_engine=DB.engine)


schema = strawberry.Schema(query=DataQuery)
graphql_app = GraphQLRouter(schema, context_getter=get_context)


app.include_router(graphql_app, prefix="/graphql")
