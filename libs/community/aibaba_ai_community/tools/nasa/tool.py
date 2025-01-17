"""
This tool allows agents to interact with the NASA API, specifically
the the NASA Image & Video Library and Exoplanet
"""

from typing import Optional

from aibaba_ai_core.callbacks import CallbackManagerForToolRun
from aibaba_ai_core.tools import BaseTool
from pydantic import Field

from aibaba_ai_community.utilities.nasa import NasaAPIWrapper


class NasaAction(BaseTool):  # type: ignore[override]
    """Tool that queries the Atlassian Jira API."""

    api_wrapper: NasaAPIWrapper = Field(default_factory=NasaAPIWrapper)
    mode: str
    name: str = ""
    description: str = ""

    def _run(
        self,
        instructions: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the NASA API to run an operation."""
        return self.api_wrapper.run(self.mode, instructions)
