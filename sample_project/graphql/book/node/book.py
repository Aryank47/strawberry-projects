from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from sample_project.models import Book

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(Book)
class Book:
    __exclude__ = ["id"]
