import abc
from typing import Optional, List

from books.contracts import BookClientContract
from books.schemas import BookSchema, BookReviewCreateSchema
from books.orm import review_book

from sqlalchemy.orm import Session


class BookService:
    def __init__(self, client: BookClientContract):
        self.client = client

    def get(self, term: Optional[str]) -> List[BookSchema]:
        if term:
            return self.search(term=term)
        else:
            return self.client.all_books()

    def find(self, book_id: str) -> BookSchema:
        return self.client.get_book(book_id=book_id)

    def search(self, term: str) -> List[BookSchema]:
        return self.client.search_books(term=term)

    def review(self, book_id: str, review: BookReviewCreateSchema,  db: Session) -> None:
        review_book(book_id=book_id, review=review, db=db)
        return None
