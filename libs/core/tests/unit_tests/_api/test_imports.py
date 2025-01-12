from aibaba_ai_core._api import __all__

EXPECTED_ALL = [
    "beta",
    "deprecated",
    "AI Agents ForceBetaWarning",
    "AI Agents ForceDeprecationWarning",
    "suppress_aiagentforce_beta_warning",
    "surface_aiagentforce_beta_warnings",
    "suppress_aiagentforce_deprecation_warning",
    "surface_aiagentforce_deprecation_warnings",
    "warn_deprecated",
    "as_import_path",
    "get_relative_path",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
