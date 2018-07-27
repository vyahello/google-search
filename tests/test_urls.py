from typing import Iterable
from search.api.urls import GoogleSearchUrlOf


def test_google_search(target: Iterable[str]) -> None:
    assert GoogleSearchUrlOf(target).gather() == f"https://google.com/search?q={' '.join(target)}"
