# from typing import Optional

import strawberry
from fastapi import Depends, FastAPI

# from starlette.background import BackgroundTasks
# from starlette.requests import HTTPConnection, Request
# from starlette.responses import Response
from strawberry.fastapi import GraphQLRouter

from sample_project.core import settings

# from sample_project.core.db import DB
from sample_project.graphql import DataMutation, DataQuery

# from strawberry.fastapi.context import CustomContext
# from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper


# from fastapi_sqlalchemy import db
# from fastapi_sqlalchemy.middleware import DBSessionMiddleware


def custom_context_dependency() -> str:
    return "John"


async def get_context(
    custom_value=Depends(custom_context_dependency),
):
    return {
        "custom_value": custom_value,
    }


# strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()
# strawberry_sqlalchemy_mapper.finalize()


app = FastAPI(title=settings.PROJECT_NAME)


# app.add_middleware(DBSessionMiddleware, db_url=DB().engine.url)


schema = strawberry.Schema(query=DataQuery, mutation=DataMutation)
graphql_app = GraphQLRouter(
    schema=schema,
    context_getter=get_context,
)


app.include_router(graphql_app, prefix="/graphql")
