from abc import ABC, abstractmethod
from typing import Iterator
from bs4 import BeautifulSoup
from bs4.element import Tag
from search.api.requests import Request


class Parser(ABC):
    """Represent the abstraction of parser."""

    @abstractmethod
    def __next__(self) -> str:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Tag]:
        pass


class Soup(ABC):
    """Abstraction for soup web parser."""

    @abstractmethod
    def __iter__(self) -> Iterator[Tag]:
        pass


class SoupLink(Soup):
    """Represent for soup web link parser."""

    def __init__(self, request: Request, features: str, css_selector: str) -> None:
        self._soup = BeautifulSoup(request.response().text(), features)
        self._css_selector = css_selector

    def __iter__(self) -> Iterator[Tag]:
        yield from self._soup.select(self._css_selector)


class PageParserLink(Parser):
    """Represent web page parser."""

    def __init__(self, request: Request, features: str = 'lxml', css_selector: str = '.r a') -> None:
        self._count: Iterator[int] = iter(range(3))
        self._links: Iterator[Tag] = iter(SoupLink(request, features, css_selector))

    def __next__(self) -> Tag:
        next(self._count)
        return next(self._links)

    def __iter__(self) -> Iterator[Tag]:
        return self
