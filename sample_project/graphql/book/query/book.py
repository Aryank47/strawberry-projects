import typing

import strawberry
from strawberry.types import Info

from sample_project.core import db
from sample_project.services import BookService

from ..node import Book


@strawberry.type
class BookQuery:
    @strawberry.field
    def books(self, info: Info) -> typing.List[Book]:
        return BookService.get_books(info.context.get("session", db.session()))
