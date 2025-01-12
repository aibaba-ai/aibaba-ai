"""Standard Aibaba AI interface tests"""

from typing import Type

from aibaba_ai_core.language_models import BaseChatModel
from langchain_tests.unit_tests.chat_models import (
    ChatModelUnitTests,
)

from langchain_groq import ChatGroq


class TestGroqStandard(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[BaseChatModel]:
        return ChatGroq
