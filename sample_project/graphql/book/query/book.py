from typing import List, cast

import strawberry

# from fastapi_sqlalchemy import db
from strawberry.types import Info

# from sample_project.core import db_obj
from sample_project.services import BookService

from ..node import Book


@strawberry.type
class BookQuery:
    @strawberry.field
    def books(self, info: Info) -> List[Book]:
        print("context -- ", info.context)
        bs = BookService(info.context.get("session", None))
        return cast(List[Book], bs.get_books())
