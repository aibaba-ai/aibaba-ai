# these stubs are just for backwards compatibility

from aiagentsforce_core.utils.function_calling import (
    FunctionDescription,
    ToolDescription,
    convert_pydantic_to_openai_function,
    convert_pydantic_to_openai_tool,
)

__all__ = [
    "FunctionDescription",
    "ToolDescription",
    "convert_pydantic_to_openai_function",
    "convert_pydantic_to_openai_tool",
]
