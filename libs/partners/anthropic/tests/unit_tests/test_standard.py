"""Standard AI Agents Force interface tests"""

from typing import Type

from aiagentsforce_core.language_models import BaseChatModel
from langchain_tests.unit_tests import ChatModelUnitTests

from langchain_anthropic import ChatAnthropic


class TestAnthropicStandard(ChatModelUnitTests):
    @property
    def chat_model_class(self) -> Type[BaseChatModel]:
        return ChatAnthropic

    @property
    def chat_model_params(self) -> dict:
        return {"model": "claude-3-haiku-20240307"}
