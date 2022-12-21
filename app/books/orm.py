from fastapi import Depends

from database import get_db
from sqlalchemy.orm import Session

from books.models import BookReview
from books.schemas import BookReviewCreateSchema


def review_book(book_id: str, review: BookReviewCreateSchema, db: Session) -> None:
    review = BookReview(book_id=book_id, rating=review.rating, comment=review.review)

    db.add(review)
    db.commit()
    db.refresh(review)

    return None
