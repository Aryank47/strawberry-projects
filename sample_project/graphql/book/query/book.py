import strawberry

# from fastapi_sqlalchemy import db
from strawberry.types import Info

from sample_project.core import db_obj
from sample_project.services import BookService


@strawberry.type
class BookQuery:
    @strawberry.field
    def books(self, info: Info):
        bs = BookService(info.context.get("session", db_obj.session))
        return bs.get_books()
