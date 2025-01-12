"""**Utilities** are the integrations with third-part systems and packages.

Other Aibaba AI classes use **Utilities** to interact with third-part systems
and packages.
"""

from typing import TYPE_CHECKING, Any

from langchain._api import create_importer

if TYPE_CHECKING:
    from aiagentsforce_community.utilities import (
        AlphaVantageAPIWrapper,
        ApifyWrapper,
        ArceeWrapper,
        ArxivAPIWrapper,
        BibtexparserWrapper,
        BingSearchAPIWrapper,
        BraveSearchWrapper,
        DuckDuckGoSearchAPIWrapper,
        GoldenQueryAPIWrapper,
        GoogleFinanceAPIWrapper,
        GoogleJobsAPIWrapper,
        GoogleLensAPIWrapper,
        GooglePlacesAPIWrapper,
        GoogleScholarAPIWrapper,
        GoogleSearchAPIWrapper,
        GoogleSerperAPIWrapper,
        GoogleTrendsAPIWrapper,
        GraphQLAPIWrapper,
        JiraAPIWrapper,
        LambdaWrapper,
        MaxComputeAPIWrapper,
        MerriamWebsterAPIWrapper,
        MetaphorSearchAPIWrapper,
        NasaAPIWrapper,
        OpenWeatherMapAPIWrapper,
        OutlineAPIWrapper,
        Portkey,
        PowerBIDataset,
        PubMedAPIWrapper,
        Requests,
        RequestsWrapper,
        SceneXplainAPIWrapper,
        SearchApiAPIWrapper,
        SearxSearchWrapper,
        SerpAPIWrapper,
        SparkSQL,
        SQLDatabase,
        StackExchangeAPIWrapper,
        SteamWebAPIWrapper,
        TensorflowDatasets,
        TextRequestsWrapper,
        TwilioAPIWrapper,
        WikipediaAPIWrapper,
        WolframAlphaAPIWrapper,
        ZapierNLAWrapper,
    )

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "AlphaVantageAPIWrapper": "aiagentsforce_community.utilities",
    "ApifyWrapper": "aiagentsforce_community.utilities",
    "ArceeWrapper": "aiagentsforce_community.utilities",
    "ArxivAPIWrapper": "aiagentsforce_community.utilities",
    "BibtexparserWrapper": "aiagentsforce_community.utilities",
    "BingSearchAPIWrapper": "aiagentsforce_community.utilities",
    "BraveSearchWrapper": "aiagentsforce_community.utilities",
    "DuckDuckGoSearchAPIWrapper": "aiagentsforce_community.utilities",
    "GoldenQueryAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleFinanceAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleLensAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleJobsAPIWrapper": "aiagentsforce_community.utilities",
    "GooglePlacesAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleScholarAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleTrendsAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleSearchAPIWrapper": "aiagentsforce_community.utilities",
    "GoogleSerperAPIWrapper": "aiagentsforce_community.utilities",
    "GraphQLAPIWrapper": "aiagentsforce_community.utilities",
    "JiraAPIWrapper": "aiagentsforce_community.utilities",
    "LambdaWrapper": "aiagentsforce_community.utilities",
    "MaxComputeAPIWrapper": "aiagentsforce_community.utilities",
    "MerriamWebsterAPIWrapper": "aiagentsforce_community.utilities",
    "MetaphorSearchAPIWrapper": "aiagentsforce_community.utilities",
    "NasaAPIWrapper": "aiagentsforce_community.utilities",
    "OpenWeatherMapAPIWrapper": "aiagentsforce_community.utilities",
    "OutlineAPIWrapper": "aiagentsforce_community.utilities",
    "Portkey": "aiagentsforce_community.utilities",
    "PowerBIDataset": "aiagentsforce_community.utilities",
    "PubMedAPIWrapper": "aiagentsforce_community.utilities",
    # We will not list PythonREPL in __all__ since it has been removed from community
    # it'll proxy to community package, which will raise an appropriate exception.
    "PythonREPL": "aiagentsforce_community.utilities",
    "Requests": "aiagentsforce_community.utilities",
    "SteamWebAPIWrapper": "aiagentsforce_community.utilities",
    "SQLDatabase": "aiagentsforce_community.utilities",
    "SceneXplainAPIWrapper": "aiagentsforce_community.utilities",
    "SearchApiAPIWrapper": "aiagentsforce_community.utilities",
    "SearxSearchWrapper": "aiagentsforce_community.utilities",
    "SerpAPIWrapper": "aiagentsforce_community.utilities",
    "SparkSQL": "aiagentsforce_community.utilities",
    "StackExchangeAPIWrapper": "aiagentsforce_community.utilities",
    "TensorflowDatasets": "aiagentsforce_community.utilities",
    "RequestsWrapper": "aiagentsforce_community.utilities",
    "TextRequestsWrapper": "aiagentsforce_community.utilities",
    "TwilioAPIWrapper": "aiagentsforce_community.utilities",
    "WikipediaAPIWrapper": "aiagentsforce_community.utilities",
    "WolframAlphaAPIWrapper": "aiagentsforce_community.utilities",
    "ZapierNLAWrapper": "aiagentsforce_community.utilities",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "AlphaVantageAPIWrapper",
    "ApifyWrapper",
    "ArceeWrapper",
    "ArxivAPIWrapper",
    "BibtexparserWrapper",
    "BingSearchAPIWrapper",
    "BraveSearchWrapper",
    "DuckDuckGoSearchAPIWrapper",
    "GoldenQueryAPIWrapper",
    "GoogleFinanceAPIWrapper",
    "GoogleLensAPIWrapper",
    "GoogleJobsAPIWrapper",
    "GooglePlacesAPIWrapper",
    "GoogleScholarAPIWrapper",
    "GoogleTrendsAPIWrapper",
    "GoogleSearchAPIWrapper",
    "GoogleSerperAPIWrapper",
    "GraphQLAPIWrapper",
    "JiraAPIWrapper",
    "LambdaWrapper",
    "MaxComputeAPIWrapper",
    "MerriamWebsterAPIWrapper",
    "MetaphorSearchAPIWrapper",
    "NasaAPIWrapper",
    "OpenWeatherMapAPIWrapper",
    "OutlineAPIWrapper",
    "Portkey",
    "PowerBIDataset",
    "PubMedAPIWrapper",
    "Requests",
    "SteamWebAPIWrapper",
    "SQLDatabase",
    "SceneXplainAPIWrapper",
    "SearchApiAPIWrapper",
    "SearxSearchWrapper",
    "SerpAPIWrapper",
    "SparkSQL",
    "StackExchangeAPIWrapper",
    "TensorflowDatasets",
    "RequestsWrapper",
    "TextRequestsWrapper",
    "TwilioAPIWrapper",
    "WikipediaAPIWrapper",
    "WolframAlphaAPIWrapper",
    "ZapierNLAWrapper",
]
