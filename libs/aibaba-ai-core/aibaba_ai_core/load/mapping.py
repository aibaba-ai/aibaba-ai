"""
This file contains a mapping between the lc_namespace path for a given
subclass that implements from Serializable to the namespace
where that class is actually located.

This mapping helps maintain the ability to serialize and deserialize
well-known Aibaba AI objects even if they are moved around in the codebase
across different Aibaba AI versions.

For example,

The code for AIMessage class is located in aibaba-ai-core.messages.ai.AIMessage,
This message is associated with the lc_namespace
["langchain", "schema", "messages", "AIMessage"],
because this code was originally in langchain.schema.messages.AIMessage.

The mapping allows us to deserialize an AIMessage created with an older
version of Aibaba AI where the code was in a different location.
"""

# First value is the value that it is serialized as
# Second value is the path to load it from
SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "messages", "AIMessage"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "messages", "AIMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("langchain", "schema", "messages", "BaseMessage"): (
        "aibaba-ai-core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("langchain", "schema", "messages", "BaseMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessage"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "messages", "FunctionMessage"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "messages", "HumanMessage"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "messages", "SystemMessage"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "messages", "ToolMessage"): (
        "aibaba-ai-core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("langchain", "schema", "messages", "RemoveMessage"): (
        "aibaba-ai-core",
        "messages",
        "modifier",
        "RemoveMessage",
    ),
    ("langchain", "schema", "agent", "AgentAction"): (
        "aibaba-ai-core",
        "agents",
        "AgentAction",
    ),
    ("langchain", "schema", "agent", "AgentFinish"): (
        "aibaba-ai-core",
        "agents",
        "AgentFinish",
    ),
    ("langchain", "schema", "prompt_template", "BasePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("langchain", "chains", "llm", "LLMChain"): (
        "langchain",
        "chains",
        "llm",
        "LLMChain",
    ),
    ("langchain", "prompts", "prompt", "PromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("langchain", "prompts", "chat", "MessagesPlaceholder"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("langchain", "llms", "openai", "OpenAI"): (
        "langchain_openai",
        "llms",
        "base",
        "OpenAI",
    ),
    ("langchain", "prompts", "chat", "ChatPromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("langchain", "prompts", "image", "ImagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "AgentActionMessageLog"): (
        "aibaba-ai-core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("langchain", "schema", "agent", "ToolAgentAction"): (
        "langchain",
        "agents",
        "output_parsers",
        "tools",
        "ToolAgentAction",
    ),
    ("langchain", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("langchain", "schema", "output", "ChatGeneration"): (
        "aibaba-ai-core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("langchain", "schema", "output", "Generation"): (
        "aibaba-ai-core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("langchain", "schema", "document", "Document"): (
        "aibaba-ai-core",
        "documents",
        "base",
        "Document",
    ),
    ("langchain", "output_parsers", "fix", "OutputFixingParser"): (
        "langchain",
        "output_parsers",
        "fix",
        "OutputFixingParser",
    ),
    ("langchain", "prompts", "chat", "AIMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("langchain", "output_parsers", "regex", "RegexParser"): (
        "langchain",
        "output_parsers",
        "regex",
        "RegexParser",
    ),
    ("langchain", "schema", "runnable", "DynamicRunnable"): (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("langchain", "schema", "prompt", "PromptValue"): (
        "aibaba-ai-core",
        "prompt_values",
        "PromptValue",
    ),
    ("langchain", "schema", "runnable", "RunnableBinding"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("langchain", "schema", "runnable", "RunnableBranch"): (
        "aibaba-ai-core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("langchain", "schema", "runnable", "RunnableWithFallbacks"): (
        "aibaba-ai-core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("langchain", "schema", "output_parser", "StrOutputParser"): (
        "aibaba-ai-core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    ("langchain", "chat_models", "openai", "ChatOpenAI"): (
        "langchain_openai",
        "chat_models",
        "base",
        "ChatOpenAI",
    ),
    ("langchain", "output_parsers", "list", "CommaSeparatedListOutputParser"): (
        "aibaba-ai-core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    ("langchain", "schema", "runnable", "RunnableParallel"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("langchain", "chat_models", "azure_openai", "AzureChatOpenAI"): (
        "langchain_openai",
        "chat_models",
        "azure",
        "AzureChatOpenAI",
    ),
    ("langchain", "chat_models", "bedrock", "BedrockChat"): (
        "langchain_aws",
        "chat_models",
        "bedrock",
        "ChatBedrock",
    ),
    ("langchain", "chat_models", "anthropic", "ChatAnthropic"): (
        "langchain_anthropic",
        "chat_models",
        "ChatAnthropic",
    ),
    ("langchain_groq", "chat_models", "ChatGroq"): (
        "langchain_groq",
        "chat_models",
        "ChatGroq",
    ),
    ("langchain", "chat_models", "fireworks", "ChatFireworks"): (
        "langchain_fireworks",
        "chat_models",
        "ChatFireworks",
    ),
    ("langchain", "chat_models", "google_palm", "ChatGooglePalm"): (
        "langchain",
        "chat_models",
        "google_palm",
        "ChatGooglePalm",
    ),
    ("langchain", "chat_models", "vertexai", "ChatVertexAI"): (
        "langchain_google_vertexai",
        "chat_models",
        "ChatVertexAI",
    ),
    ("langchain", "chat_models", "mistralai", "ChatMistralAI"): (
        "langchain_mistralai",
        "chat_models",
        "ChatMistralAI",
    ),
    ("langchain", "chat_models", "bedrock", "ChatBedrock"): (
        "langchain_aws",
        "chat_models",
        "bedrock",
        "ChatBedrock",
    ),
    ("langchain_google_genai", "chat_models", "ChatGoogleGenerativeAI"): (
        "langchain_google_genai",
        "chat_models",
        "ChatGoogleGenerativeAI",
    ),
    ("langchain", "schema", "output", "ChatGenerationChunk"): (
        "aibaba-ai-core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("langchain", "schema", "messages", "HumanMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("langchain", "schema", "messages", "FunctionMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("langchain", "schema", "messages", "SystemMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("langchain", "schema", "messages", "ToolMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("langchain", "schema", "output", "GenerationChunk"): (
        "aibaba-ai-core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("langchain", "llms", "openai", "BaseOpenAI"): (
        "langchain",
        "llms",
        "openai",
        "BaseOpenAI",
    ),
    ("langchain", "llms", "bedrock", "Bedrock"): (
        "langchain_aws",
        "llms",
        "bedrock",
        "BedrockLLM",
    ),
    ("langchain", "llms", "fireworks", "Fireworks"): (
        "langchain_fireworks",
        "llms",
        "Fireworks",
    ),
    ("langchain", "llms", "google_palm", "GooglePalm"): (
        "langchain",
        "llms",
        "google_palm",
        "GooglePalm",
    ),
    ("langchain", "llms", "openai", "AzureOpenAI"): (
        "langchain_openai",
        "llms",
        "azure",
        "AzureOpenAI",
    ),
    ("langchain", "llms", "replicate", "Replicate"): (
        "langchain",
        "llms",
        "replicate",
        "Replicate",
    ),
    ("langchain", "llms", "vertexai", "VertexAI"): (
        "langchain_vertexai",
        "llms",
        "VertexAI",
    ),
    ("langchain", "output_parsers", "combining", "CombiningOutputParser"): (
        "langchain",
        "output_parsers",
        "combining",
        "CombiningOutputParser",
    ),
    ("langchain", "schema", "prompt_template", "BaseChatPromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    ("langchain", "prompts", "few_shot_with_templates", "FewShotPromptWithTemplates"): (
        "aibaba-ai-core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("langchain", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptValue"): (
        "aibaba-ai-core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("langchain", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValue"): (
        "aibaba-ai-core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValueConcrete"): (
        "aibaba-ai-core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("langchain", "schema", "runnable", "HubRunnable"): (
        "langchain",
        "runnables",
        "hub",
        "HubRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnableBindingBase"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("langchain", "schema", "runnable", "OpenAIFunctionsRouter"): (
        "langchain",
        "runnables",
        "openai_functions",
        "OpenAIFunctionsRouter",
    ),
    ("langchain", "schema", "runnable", "RouterRunnable"): (
        "aibaba-ai-core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnablePassthrough"): (
        "aibaba-ai-core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("langchain", "schema", "runnable", "RunnableSequence"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("langchain", "schema", "runnable", "RunnableEach"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("langchain", "schema", "runnable", "RunnableEachBase"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableAlternatives"): (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableFields"): (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("langchain", "schema", "runnable", "RunnableWithMessageHistory"): (
        "aibaba-ai-core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("langchain", "schema", "runnable", "RunnableAssign"): (
        "aibaba-ai-core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("langchain", "schema", "runnable", "RunnableRetry"): (
        "aibaba-ai-core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
    ("aibaba-ai-core", "prompts", "structured", "StructuredPrompt"): (
        "aibaba-ai-core",
        "prompts",
        "structured",
        "StructuredPrompt",
    ),
}

# Needed for backwards compatibility for old versions of Aibaba AI where things
# Were in different place
_OG_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "AIMessage"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "ChatMessage"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "FunctionMessage"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "HumanMessage"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "SystemMessage"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "prompt_template", "ImagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "OpenAIToolAgentAction"): (
        "langchain",
        "agents",
        "output_parsers",
        "openai_tools",
        "OpenAIToolAgentAction",
    ),
}

# Needed for backwards compatibility for a few versions where we serialized
# with aibaba-ai-core paths.
OLD_CORE_NAMESPACES_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("aibaba-ai-core", "messages", "ai", "AIMessage"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("aibaba-ai-core", "messages", "ai", "AIMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "base", "BaseMessage"): (
        "aibaba-ai-core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("aibaba-ai-core", "messages", "base", "BaseMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "chat", "ChatMessage"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("aibaba-ai-core", "messages", "function", "FunctionMessage"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("aibaba-ai-core", "messages", "human", "HumanMessage"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("aibaba-ai-core", "messages", "system", "SystemMessage"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("aibaba-ai-core", "messages", "tool", "ToolMessage"): (
        "aibaba-ai-core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("aibaba-ai-core", "agents", "AgentAction"): (
        "aibaba-ai-core",
        "agents",
        "AgentAction",
    ),
    ("aibaba-ai-core", "agents", "AgentFinish"): (
        "aibaba-ai-core",
        "agents",
        "AgentFinish",
    ),
    ("aibaba-ai-core", "prompts", "base", "BasePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("aibaba-ai-core", "prompts", "prompt", "PromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("aibaba-ai-core", "prompts", "chat", "MessagesPlaceholder"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("aibaba-ai-core", "prompts", "chat", "ChatPromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("aibaba-ai-core", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("aibaba-ai-core", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("aibaba-ai-core", "agents", "AgentActionMessageLog"): (
        "aibaba-ai-core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("aibaba-ai-core", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("aibaba-ai-core", "outputs", "chat_generation", "ChatGeneration"): (
        "aibaba-ai-core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("aibaba-ai-core", "outputs", "generation", "Generation"): (
        "aibaba-ai-core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("aibaba-ai-core", "documents", "base", "Document"): (
        "aibaba-ai-core",
        "documents",
        "base",
        "Document",
    ),
    ("aibaba-ai-core", "prompts", "chat", "AIMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("aibaba-ai-core", "runnables", "configurable", "DynamicRunnable"): (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("aibaba-ai-core", "prompt_values", "PromptValue"): (
        "aibaba-ai-core",
        "prompt_values",
        "PromptValue",
    ),
    ("aibaba-ai-core", "runnables", "base", "RunnableBinding"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("aibaba-ai-core", "runnables", "branch", "RunnableBranch"): (
        "aibaba-ai-core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("aibaba-ai-core", "runnables", "fallbacks", "RunnableWithFallbacks"): (
        "aibaba-ai-core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("aibaba-ai-core", "output_parsers", "string", "StrOutputParser"): (
        "aibaba-ai-core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    ("aibaba-ai-core", "output_parsers", "list", "CommaSeparatedListOutputParser"): (
        "aibaba-ai-core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    ("aibaba-ai-core", "runnables", "base", "RunnableParallel"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("aibaba-ai-core", "outputs", "chat_generation", "ChatGenerationChunk"): (
        "aibaba-ai-core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("aibaba-ai-core", "messages", "chat", "ChatMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "human", "HumanMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "function", "FunctionMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "system", "SystemMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "tool", "ToolMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("aibaba-ai-core", "outputs", "generation", "GenerationChunk"): (
        "aibaba-ai-core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("aibaba-ai-core", "prompts", "chat", "BaseChatPromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("aibaba-ai-core", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    (
        "aibaba-ai-core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ): (
        "aibaba-ai-core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("aibaba-ai-core", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("aibaba-ai-core", "prompts", "string", "StringPromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("aibaba-ai-core", "prompt_values", "StringPromptValue"): (
        "aibaba-ai-core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("aibaba-ai-core", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("aibaba-ai-core", "prompt_values", "ChatPromptValue"): (
        "aibaba-ai-core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("aibaba-ai-core", "prompt_values", "ChatPromptValueConcrete"): (
        "aibaba-ai-core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("aibaba-ai-core", "runnables", "base", "RunnableBindingBase"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("aibaba-ai-core", "runnables", "router", "RouterRunnable"): (
        "aibaba-ai-core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("aibaba-ai-core", "runnables", "passthrough", "RunnablePassthrough"): (
        "aibaba-ai-core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("aibaba-ai-core", "runnables", "base", "RunnableSequence"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("aibaba-ai-core", "runnables", "base", "RunnableEach"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("aibaba-ai-core", "runnables", "base", "RunnableEachBase"): (
        "aibaba-ai-core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ): (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("aibaba-ai-core", "runnables", "configurable", "RunnableConfigurableFields"): (
        "aibaba-ai-core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("aibaba-ai-core", "runnables", "history", "RunnableWithMessageHistory"): (
        "aibaba-ai-core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("aibaba-ai-core", "runnables", "passthrough", "RunnableAssign"): (
        "aibaba-ai-core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("aibaba-ai-core", "runnables", "retry", "RunnableRetry"): (
        "aibaba-ai-core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
}

_JS_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("aibaba-ai-core", "messages", "AIMessage"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("aibaba-ai-core", "messages", "AIMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "BaseMessage"): (
        "aibaba-ai-core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("aibaba-ai-core", "messages", "BaseMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "ChatMessage"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("aibaba-ai-core", "messages", "ChatMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "FunctionMessage"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("aibaba-ai-core", "messages", "FunctionMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "HumanMessage"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("aibaba-ai-core", "messages", "HumanMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "SystemMessage"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("aibaba-ai-core", "messages", "SystemMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("aibaba-ai-core", "messages", "ToolMessage"): (
        "aibaba-ai-core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("aibaba-ai-core", "messages", "ToolMessageChunk"): (
        "aibaba-ai-core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("aibaba-ai-core", "prompts", "image", "ImagePromptTemplate"): (
        "aibaba-ai-core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "chat_models", "bedrock", "ChatBedrock"): (
        "langchain_aws",
        "chat_models",
        "ChatBedrock",
    ),
    ("langchain", "chat_models", "google_genai", "ChatGoogleGenerativeAI"): (
        "langchain_google_genai",
        "chat_models",
        "ChatGoogleGenerativeAI",
    ),
    ("langchain", "chat_models", "groq", "ChatGroq"): (
        "langchain_groq",
        "chat_models",
        "ChatGroq",
    ),
    ("langchain", "chat_models", "bedrock", "BedrockChat"): (
        "langchain_aws",
        "chat_models",
        "ChatBedrock",
    ),
}
