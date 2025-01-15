def test_power_bi_can_be_imported() -> None:
    """Test that powerbi tools can be imported.

    The goal of this test is to verify that langchain users will not get import errors
    when loading powerbi related code if they don't have optional dependencies
    installed.
    """
    from aibaba_ai_community.tools.powerbi.tool import QueryPowerBITool  # noqa
    from aibaba_ai_community.agent_toolkits import PowerBIToolkit, create_pbi_agent  # noqa
    from aibaba_ai_community.utilities.powerbi import PowerBIDataset  # noqa
