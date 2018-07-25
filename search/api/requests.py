from abc import ABC, abstractmethod
from typing import Dict, Any
import urllib3
from requests import Session
from search.api.responses import Response, HttpResponse
from search.api.urls import Url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def response(self) -> Response:
        pass


class Get(Request):
    """Represent an api ``get`` request."""

    def __init__(self, url: Url, **data: Dict[Any, Any]) -> None:
        self._session: Session = Session()
        self._data = data
        self._url = url

    def response(self) -> Response:
        return HttpResponse(self._session.get(self._url.gather(), **self._data, verify=False))
