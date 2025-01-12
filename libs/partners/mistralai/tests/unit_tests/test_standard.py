"""Standard Aibaba AI interface tests"""

from typing import Type

from aibaba-ai-core.language_models import BaseChatModel
from langchain_tests.unit_tests import (  # type: ignore[import-not-found]
    ChatModelUnitTests,  # type: ignore[import-not-found]
)

from langchain_mistralai import ChatMistralAI


class TestMistralStandard(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[BaseChatModel]:
        return ChatMistralAI
