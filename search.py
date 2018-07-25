import sys
from search.api.requests import Get
from search.api.urls import GoogleSearchUrlOf
from search.browser.browser import WebBrowser
from search.parser.page import PageParserLink


def _search() -> None:
    for link in PageParserLink(Get(GoogleSearchUrlOf(target=sys.argv[1:]))):
        WebBrowser(link).open()


if __name__ == '__main__':
    _search()
