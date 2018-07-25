from abc import ABC, abstractmethod
from typing import Iterable
from search.parser.tag import HtmlTag
from search.target.search import SearchTarget


class Url(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def gather(self) -> str:
        pass


class GoogleUrlOf(Url):
    """Gather google url components together."""

    def __init__(self, tag: HtmlTag) -> None:
        self._tag = tag

    def gather(self) -> str:
        return f"https://google.com{self._tag.get()}"


class GoogleSearchUrlOf(Url):
    """Gather google search url components together."""

    def __init__(self, target: Iterable[str]) -> None:
        self._target = SearchTarget(target)

    def gather(self) -> str:
        return f"https://google.com/search?q={self._target.gather()}"
