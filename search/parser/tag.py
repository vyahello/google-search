from abc import ABC, abstractmethod
from bs4.element import Tag


class HtmlTag(ABC):
    """Abstraction for a tag."""

    @abstractmethod
    def get(self) -> str:
        pass


class HtmlTagOf(HtmlTag):
    """Represent html tag."""

    def __init__(self, tag: Tag, attribute: str) -> None:
        self._tag = tag
        self._attr = attribute

    def get(self) -> str:
        return self._tag.get(self._attr)
