"""**Prompt** is the input to the model.

Prompt is often constructed
from multiple components and prompt values. Prompt classes and functions make constructing
 and working with prompts easy.

**Class hierarchy:**

.. code-block::

    BasePromptTemplate --> PipelinePromptTemplate
                           StringPromptTemplate --> PromptTemplate
                                                    FewShotPromptTemplate
                                                    FewShotPromptWithTemplates
                           BaseChatPromptTemplate --> AutoGPTPrompt
                                                      ChatPromptTemplate --> AgentScratchPadChatPromptTemplate



    BaseMessagePromptTemplate --> MessagesPlaceholder
                                  BaseStringMessagePromptTemplate --> ChatMessagePromptTemplate
                                                                      HumanMessagePromptTemplate
                                                                      AIMessagePromptTemplate
                                                                      SystemMessagePromptTemplate

"""  # noqa: E501

from aiagentsforce_core.prompts.base import (
    BasePromptTemplate,
    aformat_document,
    format_document,
)
from aiagentsforce_core.prompts.chat import (
    AIMessagePromptTemplate,
    BaseChatPromptTemplate,
    ChatMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from aiagentsforce_core.prompts.few_shot import (
    FewShotChatMessagePromptTemplate,
    FewShotPromptTemplate,
)
from aiagentsforce_core.prompts.few_shot_with_templates import FewShotPromptWithTemplates
from aiagentsforce_core.prompts.loading import load_prompt
from aiagentsforce_core.prompts.pipeline import PipelinePromptTemplate
from aiagentsforce_core.prompts.prompt import PromptTemplate
from aiagentsforce_core.prompts.string import (
    StringPromptTemplate,
    check_valid_template,
    get_template_variables,
    jinja2_formatter,
    validate_jinja2,
)

__all__ = [
    "AIMessagePromptTemplate",
    "BaseChatPromptTemplate",
    "BasePromptTemplate",
    "ChatMessagePromptTemplate",
    "ChatPromptTemplate",
    "FewShotPromptTemplate",
    "FewShotPromptWithTemplates",
    "FewShotChatMessagePromptTemplate",
    "HumanMessagePromptTemplate",
    "MessagesPlaceholder",
    "PipelinePromptTemplate",
    "PromptTemplate",
    "StringPromptTemplate",
    "SystemMessagePromptTemplate",
    "load_prompt",
    "format_document",
    "aformat_document",
    "check_valid_template",
    "get_template_variables",
    "jinja2_formatter",
    "validate_jinja2",
]
