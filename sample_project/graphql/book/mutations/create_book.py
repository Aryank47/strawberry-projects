import strawberry

from sample_project.core import db_obj
from sample_project.services import BookService


@strawberry.type
class BookMutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str):
        print(f"Adding {title} by {author}")
        bs = BookService(db_obj.session)
        return bs.create_books(author=author, title=title)
