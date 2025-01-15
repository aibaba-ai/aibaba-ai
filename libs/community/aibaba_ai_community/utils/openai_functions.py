# these stubs are just for backwards compatibility

from aibaba_ai_core.utils.function_calling import (
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
