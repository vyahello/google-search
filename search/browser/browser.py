from abc import ABC, abstractmethod
from bs4.element import Tag
from search.api.urls import Url, GoogleUrlOf
import webbrowser


class Browser(ABC):
    """Represent the abstraction of browser."""

    @abstractmethod
    def open(self) -> None:
        pass


class WebBrowser(Browser):
    """Represent web browser object."""

    def __init__(self, parser: Tag) -> None:
        self._url: Url = GoogleUrlOf(parser)
        self._browser = webbrowser

    def open(self) -> None:
        self._browser.open(self._url.gather())
