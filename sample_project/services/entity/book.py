from sample_project.models import Book


class BookService:
    @staticmethod
    def get_books(session):
        books = session.query(Book).all()
        print(f"BOOKS FROM DB ---> {books}")
        return books
