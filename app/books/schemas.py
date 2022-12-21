from typing import List, Union
from pydantic import BaseModel


class AuthorSchema(BaseModel):
    name: str
    birth_year: Union[int, None]
    death_year: Union[int, None]


class BookSchema(BaseModel):
    id: str
    title: str
    authors: List[AuthorSchema]
    languages: List[str]
    download_count: int


class BookSearchSchema(BaseModel):
    books: List[BookSchema] = []


class BookDetailsSchema(BookSchema):
    rating: int = 0
    reviews: List[str] = []


class BookReviewCreateSchema(BaseModel):
    rating: int
    review: Union[str, None]



