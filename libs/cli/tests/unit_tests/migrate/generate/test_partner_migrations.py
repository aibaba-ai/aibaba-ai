import pytest

from aiagentsforce_cli.namespaces.migrate.generate.partner import (
    get_migrations_for_partner_package,
)

pytest.importorskip(modname="langchain_openai")


def test_generate_migrations() -> None:
    migrations = get_migrations_for_partner_package("langchain_openai")
    assert migrations == [
        ("aiagentsforce_community.llms.openai.OpenAI", "langchain_openai.OpenAI"),
        ("aiagentsforce_community.llms.openai.AzureOpenAI", "langchain_openai.AzureOpenAI"),
        (
            "aiagentsforce_community.embeddings.openai.OpenAIEmbeddings",
            "langchain_openai.OpenAIEmbeddings",
        ),
        (
            "aiagentsforce_community.embeddings.azure_openai.AzureOpenAIEmbeddings",
            "langchain_openai.AzureOpenAIEmbeddings",
        ),
        (
            "aiagentsforce_community.chat_models.openai.ChatOpenAI",
            "langchain_openai.ChatOpenAI",
        ),
        (
            "aiagentsforce_community.chat_models.azure_openai.AzureChatOpenAI",
            "langchain_openai.AzureChatOpenAI",
        ),
        ("aiagentsforce_community.llms.AzureOpenAI", "langchain_openai.AzureOpenAI"),
        ("aiagentsforce_community.llms.OpenAI", "langchain_openai.OpenAI"),
        (
            "aiagentsforce_community.embeddings.AzureOpenAIEmbeddings",
            "langchain_openai.AzureOpenAIEmbeddings",
        ),
        (
            "aiagentsforce_community.embeddings.OpenAIEmbeddings",
            "langchain_openai.OpenAIEmbeddings",
        ),
        (
            "aiagentsforce_community.chat_models.AzureChatOpenAI",
            "langchain_openai.AzureChatOpenAI",
        ),
        ("aiagentsforce_community.chat_models.ChatOpenAI", "langchain_openai.ChatOpenAI"),
    ]
