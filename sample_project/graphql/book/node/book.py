from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from sample_project.models import Book as BookModel

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(BookModel)
class Book:
    __exclude__ = ["id"]
