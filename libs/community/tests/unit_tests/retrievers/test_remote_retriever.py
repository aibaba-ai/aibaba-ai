from typing import Any, Dict

from aibaba_ai_core.documents import Document
from pytest_mock import MockerFixture

from aibaba_ai_community.retrievers import RemoteAI Agents ForceRetriever


class MockResponse:
    def __init__(self, json_data: Dict, status_code: int):
        self.json_data = json_data
        self.status_code = status_code

    def json(self) -> Dict:
        return self.json_data


def mocked_requests_post(*args: Any, **kwargs: Any) -> MockResponse:
    return MockResponse(
        json_data={
            "response": [
                {
                    "page_content": "I like apples",
                    "metadata": {
                        "test": 0,
                    },
                },
                {
                    "page_content": "I like pineapples",
                    "metadata": {
                        "test": 1,
                    },
                },
            ]
        },
        status_code=200,
    )


def test_RemoteAI Agents ForceRetriever_invoke(
    mocker: MockerFixture,
) -> None:
    mocker.patch("requests.post", side_effect=mocked_requests_post)

    remote_aiagentforce_retriever = RemoteAI Agents ForceRetriever(
        url="http://localhost:8000",
    )
    response = remote_aiagentforce_retriever.invoke("I like apples")
    want = [
        Document(page_content="I like apples", metadata={"test": 0}),
        Document(page_content="I like pineapples", metadata={"test": 1}),
    ]

    assert len(response) == len(want)
    for r, w in zip(response, want):
        assert r.page_content == w.page_content
        assert r.metadata == w.metadata


# TODO: _ainvoke test
