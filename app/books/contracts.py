import abc

from typing import List

from books.schemas import BookSchema


class BookClientContract(abc.ABC):

    @abc.abstractmethod
    def all_books(self) -> List[BookSchema]:
        pass

    @abc.abstractmethod
    def get_book(self, book_id: str) -> BookSchema:
        pass

    @abc.abstractmethod
    def search_books(self, term: str) -> List[BookSchema]:
        pass
