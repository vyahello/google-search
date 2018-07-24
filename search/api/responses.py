from abc import ABC, abstractmethod
import requests


class Response(ABC):
    """The abstraction of a response from an api request."""

    @abstractmethod
    def text(self) -> str:
        pass


class HttpResponseError(Exception):
    """Represent http response error object."""

    pass


class HttpResponse(Response):
    """Represent an HTTP response from an api request."""

    def __init__(self, response: requests.Response) -> None:
        self._response: requests.Response = response

    def text(self) -> str:
        return self._response.text
