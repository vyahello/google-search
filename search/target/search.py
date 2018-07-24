from abc import ABC, abstractmethod
from typing import Iterable


class Target(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def gather(self) -> str:
        pass


class SearchTarget(Target):
    """Represent search target."""

    def __init__(self, targets: Iterable[str]) -> None:
        self._targets = targets

    def gather(self) -> str:
        return ' '.join(self._targets)
