from typing import Iterable
import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(scope="module",
                params=[("Volodymyr", "Yahello", "vyahello"),
                        ("python", "paramiko", "ssh"),
                        ("python", "telegram", "bot")])
def target(request: SubRequest) -> Iterable[str]:
    return request.param
