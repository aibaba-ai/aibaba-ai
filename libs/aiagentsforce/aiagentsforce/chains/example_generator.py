from typing import List

from aiagentsforce_core.language_models import BaseLanguageModel
from aiagentsforce_core.output_parsers import StrOutputParser
from aiagentsforce_core.prompts.few_shot import FewShotPromptTemplate
from aiagentsforce_core.prompts.prompt import PromptTemplate

TEST_GEN_TEMPLATE_SUFFIX = "Add another example."


def generate_example(
    examples: List[dict], llm: BaseLanguageModel, prompt_template: PromptTemplate
) -> str:
    """Return another example given a list of examples for a prompt."""
    prompt = FewShotPromptTemplate(
        examples=examples,
        suffix=TEST_GEN_TEMPLATE_SUFFIX,
        input_variables=[],
        example_prompt=prompt_template,
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({})
