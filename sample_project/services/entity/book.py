from sqlalchemy.orm import Session

from sample_project.models import Book


class BookService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_books(self):
        books = self.session.query(Book).all()
        print(f"BOOKS FROM DB ---> {books}")
        return books

    def create_books(self, author: str, title: str):
        new_book = Book(author=author, title=title)  # type:ignore
        self.session.add(new_book)
        self.session.commit()
        self.session.refresh(new_book)
        # print(f"BOOKS FROM DB ---> {books}")
        return new_book
