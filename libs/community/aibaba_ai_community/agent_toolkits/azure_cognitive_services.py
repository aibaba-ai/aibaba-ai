from __future__ import annotations

import sys
from typing import List

from aibaba_ai_core.tools import BaseTool
from aibaba_ai_core.tools.base import BaseToolkit

from aibaba_ai_community.tools.azure_cognitive_services import (
    AzureCogsFormRecognizerTool,
    AzureCogsImageAnalysisTool,
    AzureCogsSpeech2TextTool,
    AzureCogsText2SpeechTool,
    AzureCogsTextAnalyticsHealthTool,
)


class AzureCognitiveServicesToolkit(BaseToolkit):
    """Toolkit for Azure Cognitive Services."""

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""

        tools: List[BaseTool] = [
            AzureCogsFormRecognizerTool(),  # type: ignore[call-arg]
            AzureCogsSpeech2TextTool(),  # type: ignore[call-arg]
            AzureCogsText2SpeechTool(),  # type: ignore[call-arg]
            AzureCogsTextAnalyticsHealthTool(),  # type: ignore[call-arg]
        ]

        # TODO: Remove check once azure-ai-vision supports MacOS.
        if sys.platform.startswith("linux") or sys.platform.startswith("win"):
            tools.append(AzureCogsImageAnalysisTool())  # type: ignore[call-arg]
        return tools
