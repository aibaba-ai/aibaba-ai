import logging
from typing import Any, Dict, List, Optional, Union

from alibaba_ai_core._api.deprecation import deprecated
from alibaba_ai_core.callbacks import CallbackManagerForLLMRun
from alibaba_ai_core.language_models.llms import LLM
from alibaba_ai_core.utils import get_from_dict_or_env
from pydantic import BaseModel, ConfigDict, model_validator

from aibaba_ai_community.llms.utils import enforce_stop_tokens

logger = logging.getLogger(__name__)


@deprecated(
    since="0.3.28",
    removal="1.0",
    alternative_import="langchain_predictionguard.PredictionGuard",
)
class PredictionGuard(LLM):
    """Prediction Guard large language models.

    To use, you should have the ``predictionguard`` python package installed, and the
    environment variable ``PREDICTIONGUARD_API_KEY`` set with your API key, or pass
    it as a named parameter to the constructor.

    Example:
        .. code-block:: python

            llm = PredictionGuard(
                model="Hermes-3-Llama-3.1-8B",
                predictionguard_api_key="your Prediction Guard API key",
            )
    """

    client: Any = None  #: :meta private:

    model: Optional[str] = "Hermes-3-Llama-3.1-8B"
    """Model name to use."""

    max_tokens: Optional[int] = 256
    """Denotes the number of tokens to predict per generation."""

    temperature: Optional[float] = 0.75
    """A non-negative float that tunes the degree of randomness in generation."""

    top_p: Optional[float] = 0.1
    """A non-negative float that controls the diversity of the generated tokens."""

    top_k: Optional[int] = None
    """The diversity of the generated text based on top-k sampling."""

    stop: Optional[List[str]] = None

    predictionguard_input: Optional[Dict[str, Union[str, bool]]] = None
    """The input check to run over the prompt before sending to the LLM."""

    predictionguard_output: Optional[Dict[str, bool]] = None
    """The output check to run the LLM output against."""

    predictionguard_api_key: Optional[str] = None
    """Prediction Guard API key."""

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that the api_key and python package exists in environment."""
        pg_api_key = get_from_dict_or_env(
            values, "predictionguard_api_key", "PREDICTIONGUARD_API_KEY"
        )

        try:
            from predictionguard import PredictionGuard

            values["client"] = PredictionGuard(
                api_key=pg_api_key,
            )

        except ImportError:
            raise ImportError(
                "Could not import predictionguard python package. "
                "Please install it with `pip install predictionguard`."
            )

        return values

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {"model": self.model}

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "predictionguard"

    def _get_parameters(self, **kwargs: Any) -> Dict[str, Any]:
        # input kwarg conflicts with LanguageModelInput on BaseChatModel
        input = kwargs.pop("predictionguard_input", self.predictionguard_input)
        output = kwargs.pop("predictionguard_output", self.predictionguard_output)

        params = {
            **{
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
                "top_p": self.top_p,
                "top_k": self.top_k,
                "input": (
                    input.model_dump() if isinstance(input, BaseModel) else input
                ),
                "output": (
                    output.model_dump() if isinstance(output, BaseModel) else output
                ),
            },
            **kwargs,
        }

        return params

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Call out to Prediction Guard's model API.
        Args:
            prompt: The prompt to pass into the model.
        Returns:
            The string generated by the model.
        Example:
            .. code-block:: python
                response = llm.invoke("Tell me a joke.")
        """

        params = self._get_parameters(**kwargs)

        stops = None
        if self.stop is not None and stop is not None:
            raise ValueError("`stop` found in both the input and default params.")
        elif self.stop is not None:
            stops = self.stop
        else:
            stops = stop

        response = self.client.completions.create(
            model=self.model,
            prompt=prompt,
            **params,
        )

        for res in response["choices"]:
            if res.get("status", "").startswith("error: "):
                err_msg = res["status"].removeprefix("error: ")
                raise ValueError(f"Error from PredictionGuard API: {err_msg}")

        text = response["choices"][0]["text"]

        # If stop tokens are provided, Prediction Guard's endpoint returns them.
        # In order to make this consistent with other endpoints, we strip them.
        if stops:
            text = enforce_stop_tokens(text, stops)

        return text
