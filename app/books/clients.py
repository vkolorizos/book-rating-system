import abc
from typing import Type, List

from httpx import Client, Response, HTTPError

from books.exceptions import GutendexClientError
from books.contracts import BookClientContract
from books.schemas import BookSchema


class GutendexClient(BookClientContract):
    base_url: str = "https://gutendex.com/"
    base_error: Type[GutendexClientError] = GutendexClientError

    def __init__(self):
        self.client = Client()
        self.client.headers.update({
            'Content-Type': 'application/json'
        })

    def __perform_request(self, method: str, path: str, *args, **kwargs) -> Response:
        response = None

        try:
            response = getattr(self.client, method)(f"{self.base_url}{path}", *args, **kwargs)

            response.raise_for_status()
        except HTTPError:
            raise self.base_error(
                f"{self.__class__.__name__} request failure:\n"
                f"{method.upper()}: {path}\n"
                f"Message: {response is not None and response.text}",
                response=response
            )

        return response

    @classmethod
    def __respond_with_books(cls, response: Response) -> List[BookSchema]:
        books = response.json()
        return books['results']

    def all_books(self) -> List[BookSchema]:
        response = self.__perform_request('get', 'books/')

        return self.__respond_with_books(response)


    def get_book(self, book_id: str) -> BookSchema:
        response = self.__perform_request('get', f"books/{book_id}/")

        return response.json()

    def search_books(self, term: str) -> List[BookSchema]:
        response = self.__perform_request('get', 'books/', params={
            "search": term
        })

        return self.__respond_with_books(response)
