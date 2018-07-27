from typing import Iterable
from search.target.search import SearchTarget


def test_search_target(target: Iterable[str]) -> None:
    assert SearchTarget(target).gather() == ' '.join(target)
