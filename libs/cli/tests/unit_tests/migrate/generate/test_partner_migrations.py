import pytest

from aibaba_ai_cli.namespaces.migrate.generate.partner import (
    get_migrations_for_partner_package,
)

pytest.importorskip(modname="langchain_openai")


def test_generate_migrations() -> None:
    migrations = get_migrations_for_partner_package("langchain_openai")
    assert migrations == [
        ("aibaba_ai_community.llms.openai.OpenAI", "langchain_openai.OpenAI"),
        ("aibaba_ai_community.llms.openai.AzureOpenAI", "langchain_openai.AzureOpenAI"),
        (
            "aibaba_ai_community.embeddings.openai.OpenAIEmbeddings",
            "langchain_openai.OpenAIEmbeddings",
        ),
        (
            "aibaba_ai_community.embeddings.azure_openai.AzureOpenAIEmbeddings",
            "langchain_openai.AzureOpenAIEmbeddings",
        ),
        (
            "aibaba_ai_community.chat_models.openai.ChatOpenAI",
            "langchain_openai.ChatOpenAI",
        ),
        (
            "aibaba_ai_community.chat_models.azure_openai.AzureChatOpenAI",
            "langchain_openai.AzureChatOpenAI",
        ),
        ("aibaba_ai_community.llms.AzureOpenAI", "langchain_openai.AzureOpenAI"),
        ("aibaba_ai_community.llms.OpenAI", "langchain_openai.OpenAI"),
        (
            "aibaba_ai_community.embeddings.AzureOpenAIEmbeddings",
            "langchain_openai.AzureOpenAIEmbeddings",
        ),
        (
            "aibaba_ai_community.embeddings.OpenAIEmbeddings",
            "langchain_openai.OpenAIEmbeddings",
        ),
        (
            "aibaba_ai_community.chat_models.AzureChatOpenAI",
            "langchain_openai.AzureChatOpenAI",
        ),
        ("aibaba_ai_community.chat_models.ChatOpenAI", "langchain_openai.ChatOpenAI"),
    ]
