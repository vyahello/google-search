from abc import ABC, abstractmethod
from typing import Generator
from bs4 import BeautifulSoup
from bs4.element import Tag


class Parser(ABC):
    """Represent the abstraction of parser."""

    @abstractmethod
    def links(self) -> Generator[Tag, None, None]:
        pass


class PageParser(Parser):
    """Represent web page parser."""

    def __init__(self, markup: str = '', features: str = None, css_selector: str = None) -> None:
        self._soup = BeautifulSoup(markup, features)
        self._css_selector = css_selector

    def links(self) -> Generator[Tag, None, None]:
        for link in self._soup.select(self._css_selector):
            yield link
