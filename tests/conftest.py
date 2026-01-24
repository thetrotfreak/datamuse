import json
import random
import string
from collections.abc import Callable

import pytest
from urllib3.response import HTTPResponse

from datamuse import Datamuse


@pytest.fixture(scope="function")
def datamuse_mock(mocker) -> Callable[..., Datamuse]:
    def fixture(method: str, url: str, response, **matchers: dict[str, str]):
        muse = Datamuse()

        def request(*args, **kwargs):
            assert kwargs["method"] == method
            assert kwargs["url"] == url
            assert kwargs["fields"] == matchers["match_query"]

            return HTTPResponse(
                status=200,
                body=json.dumps(response).encode(),
                request_method=method,
            )

        mocker.patch.object(
            muse._Datamuse__pool,  # pyright: ignore[reportAttributeAccessIssue]
            "request",
            autospec=True,
            side_effect=request,
        )
        return muse

    return fixture


@pytest.fixture(scope="function")
def word_mock() -> str:
    return "".join(
        random.choices(
            string.ascii_lowercase, k=random.randint(1, len(string.ascii_lowercase))
        )
    )


@pytest.fixture(scope="function")
def words_mock() -> Callable[[int], list[str]]:
    def wrapped(words: int = 1):
        return [
            "".join(
                random.choices(
                    string.ascii_lowercase,
                    k=random.randint(1, len(string.ascii_lowercase)),
                )
            )
            for _ in range(words)
        ]

    return wrapped
