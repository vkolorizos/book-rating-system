from typing import List, Optional

from fastapi import APIRouter
from fastapi import status, Query, Depends

from books import schemas
from books.deps import get_book_service
from books.services import BookService

from database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/books', tags=['books'])


@router.get("/", response_model=schemas.BookSearchSchema)
async def get_books(books_service: BookService = Depends(get_book_service),
                    search: Optional[str] = Query(default=None, min_length=3, max_length=50)):
    return {'books': books_service.get(term=search)}


@router.get("/{book_id}/", response_model=schemas.BookDetailsSchema)
async def get_book_details(book_id: str, books_service: BookService = Depends(get_book_service)):
    return books_service.find(book_id=book_id)


@router.post("/{book_id}/review/", status_code=status.HTTP_201_CREATED)
async def review_book(book_id: str, review: schemas.BookReviewCreateSchema,
                      books_service: BookService = Depends(get_book_service),
                      db:Session =  Depends(get_db)):
    book = books_service.find(book_id=book_id)

    if book:
        books_service.review(book_id=book_id, review=review, db=db)
    else:
        raise HTTPException(status_code=404, detail="Book not found")
