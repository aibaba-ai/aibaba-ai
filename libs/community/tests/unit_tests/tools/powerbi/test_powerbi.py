def test_power_bi_can_be_imported() -> None:
    """Test that powerbi tools can be imported.

    The goal of this test is to verify that langchain users will not get import errors
    when loading powerbi related code if they don't have optional dependencies
    installed.
    """
    from aiagentsforce_community.tools.powerbi.tool import QueryPowerBITool  # noqa
    from aiagentsforce_community.agent_toolkits import PowerBIToolkit, create_pbi_agent  # noqa
    from aiagentsforce_community.utilities.powerbi import PowerBIDataset  # noqa
