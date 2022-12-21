from typing import Optional

from httpx import Client, Response, HTTPError

class GutendexClientError(Exception):
    def __init__(self, message: str, response: Optional[Response] = None):
        self.message = message
        self.response =  response
        super().__init__(self.message)
