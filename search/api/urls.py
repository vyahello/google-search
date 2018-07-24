from abc import ABC, abstractmethod
from search.target.search import Target


class Url(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def gather(self) -> str:
        pass


class GoogleSearchUrlOf(Url):
    """Gather url components together."""

    def __init__(self, target: Target) -> None:
        self._target = target

    def gather(self) -> str:
        return f"https://google.com/search?q={self._target.gather()}"
