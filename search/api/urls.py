from abc import ABC, abstractmethod
from typing import Iterable
from search.target.search import SearchTarget
from bs4.element import Tag


class Url(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def gather(self) -> str:
        pass


class GoogleUrlOf(Url):
    """Gather google url components together."""

    def __init__(self, tag: Tag) -> None:
        self._tag = tag

    def gather(self) -> str:
        return f"https://google.com{self._tag.get('href')}"


class GoogleSearchUrlOf(Url):
    """Gather google search url components together."""

    def __init__(self, target: Iterable[str]) -> None:
        self._target = SearchTarget(target)

    def gather(self) -> str:
        return f"https://google.com/search?q={self._target.gather()}"
