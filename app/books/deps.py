
from books.clients import GutendexClient
from books.services import BookService

def get_book_service() -> BookService:
    return BookService(GutendexClient())