"""Integration test for Bing Search API Wrapper."""

from alibaba_ai_core.utils import get_from_env

from aibaba_ai_community.utilities.passio_nutrition_ai import (
    ManagedPassioLifeAuth,
    NutritionAIAPI,
)


def test_call() -> None:
    """Test that call gives the correct answer."""
    api_key = get_from_env("", "NUTRITIONAI_SUBSCRIPTION_KEY")
    search = NutritionAIAPI(
        nutritionai_subscription_key=api_key, auth_=ManagedPassioLifeAuth(api_key)
    )
    output = search.run("Chicken tikka masala")
    assert output is not None
    assert "Chicken tikka masala" == output["results"][0]["displayName"]
