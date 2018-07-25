from abc import ABC, abstractmethod
from bs4.element import Tag
from search.api.urls import Url, GoogleUrlOf
from search.parser.tag import HtmlTagOf
import webbrowser


class Browser(ABC):
    """Represent the abstraction of browser."""

    @abstractmethod
    def open(self) -> None:
        pass


class WebBrowser(Browser):
    """Represent web browser object."""

    def __init__(self, tag: Tag) -> None:
        self._url: Url = GoogleUrlOf(HtmlTagOf(tag, attribute='href'))
        self._browser = webbrowser

    def open(self) -> None:
        self._browser.open(self._url.gather())
