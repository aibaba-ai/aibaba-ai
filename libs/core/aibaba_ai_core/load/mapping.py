"""
This file contains a mapping between the lc_namespace path for a given
subclass that implements from Serializable to the namespace
where that class is actually located.

This mapping helps maintain the ability to serialize and deserialize
well-known Aibaba AI objects even if they are moved around in the codebase
across different Aibaba AI versions.

For example,

The code for AIMessage class is located in aibaba_ai_core.messages.ai.AIMessage,
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
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "messages", "AIMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("langchain", "schema", "messages", "BaseMessage"): (
        "aibaba_ai_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("langchain", "schema", "messages", "BaseMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessage"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "messages", "FunctionMessage"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "messages", "HumanMessage"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "messages", "SystemMessage"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "messages", "ToolMessage"): (
        "aibaba_ai_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("langchain", "schema", "messages", "RemoveMessage"): (
        "aibaba_ai_core",
        "messages",
        "modifier",
        "RemoveMessage",
    ),
    ("langchain", "schema", "agent", "AgentAction"): (
        "aibaba_ai_core",
        "agents",
        "AgentAction",
    ),
    ("langchain", "schema", "agent", "AgentFinish"): (
        "aibaba_ai_core",
        "agents",
        "AgentFinish",
    ),
    ("langchain", "schema", "prompt_template", "BasePromptTemplate"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("langchain", "prompts", "chat", "MessagesPlaceholder"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("langchain", "prompts", "image", "ImagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "AgentActionMessageLog"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("langchain", "schema", "output", "ChatGeneration"): (
        "aibaba_ai_core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("langchain", "schema", "output", "Generation"): (
        "aibaba_ai_core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("langchain", "schema", "document", "Document"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("langchain", "schema", "prompt", "PromptValue"): (
        "aibaba_ai_core",
        "prompt_values",
        "PromptValue",
    ),
    ("langchain", "schema", "runnable", "RunnableBinding"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("langchain", "schema", "runnable", "RunnableBranch"): (
        "aibaba_ai_core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("langchain", "schema", "runnable", "RunnableWithFallbacks"): (
        "aibaba_ai_core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("langchain", "schema", "output_parser", "StrOutputParser"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    ("langchain", "schema", "runnable", "RunnableParallel"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("langchain", "schema", "messages", "HumanMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("langchain", "schema", "messages", "FunctionMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("langchain", "schema", "messages", "SystemMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("langchain", "schema", "messages", "ToolMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("langchain", "schema", "output", "GenerationChunk"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    ("langchain", "prompts", "few_shot_with_templates", "FewShotPromptWithTemplates"): (
        "aibaba_ai_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("langchain", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptValue"): (
        "aibaba_ai_core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("langchain", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValue"): (
        "aibaba_ai_core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValueConcrete"): (
        "aibaba_ai_core",
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
        "aibaba_ai_core",
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
        "aibaba_ai_core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnablePassthrough"): (
        "aibaba_ai_core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("langchain", "schema", "runnable", "RunnableSequence"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("langchain", "schema", "runnable", "RunnableEach"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("langchain", "schema", "runnable", "RunnableEachBase"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableAlternatives"): (
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableFields"): (
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("langchain", "schema", "runnable", "RunnableWithMessageHistory"): (
        "aibaba_ai_core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("langchain", "schema", "runnable", "RunnableAssign"): (
        "aibaba_ai_core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("langchain", "schema", "runnable", "RunnableRetry"): (
        "aibaba_ai_core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
    ("aibaba_ai_core", "prompts", "structured", "StructuredPrompt"): (
        "aibaba_ai_core",
        "prompts",
        "structured",
        "StructuredPrompt",
    ),
}

# Needed for backwards compatibility for old versions of Aibaba AI where things
# Were in different place
_OG_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "AIMessage"): (
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "ChatMessage"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "FunctionMessage"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "HumanMessage"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "SystemMessage"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "prompt_template", "ImagePromptTemplate"): (
        "aibaba_ai_core",
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
# with aibaba_ai_core paths.
OLD_CORE_NAMESPACES_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("aibaba_ai_core", "messages", "ai", "AIMessage"): (
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("aibaba_ai_core", "messages", "ai", "AIMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "base", "BaseMessage"): (
        "aibaba_ai_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("aibaba_ai_core", "messages", "base", "BaseMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "chat", "ChatMessage"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("aibaba_ai_core", "messages", "function", "FunctionMessage"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("aibaba_ai_core", "messages", "human", "HumanMessage"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("aibaba_ai_core", "messages", "system", "SystemMessage"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("aibaba_ai_core", "messages", "tool", "ToolMessage"): (
        "aibaba_ai_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("aibaba_ai_core", "agents", "AgentAction"): (
        "aibaba_ai_core",
        "agents",
        "AgentAction",
    ),
    ("aibaba_ai_core", "agents", "AgentFinish"): (
        "aibaba_ai_core",
        "agents",
        "AgentFinish",
    ),
    ("aibaba_ai_core", "prompts", "base", "BasePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("aibaba_ai_core", "prompts", "prompt", "PromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("aibaba_ai_core", "prompts", "chat", "MessagesPlaceholder"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("aibaba_ai_core", "prompts", "chat", "ChatPromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("aibaba_ai_core", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("aibaba_ai_core", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("aibaba_ai_core", "agents", "AgentActionMessageLog"): (
        "aibaba_ai_core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("aibaba_ai_core", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("aibaba_ai_core", "outputs", "chat_generation", "ChatGeneration"): (
        "aibaba_ai_core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("aibaba_ai_core", "outputs", "generation", "Generation"): (
        "aibaba_ai_core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("aibaba_ai_core", "documents", "base", "Document"): (
        "aibaba_ai_core",
        "documents",
        "base",
        "Document",
    ),
    ("aibaba_ai_core", "prompts", "chat", "AIMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("aibaba_ai_core", "runnables", "configurable", "DynamicRunnable"): (
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("aibaba_ai_core", "prompt_values", "PromptValue"): (
        "aibaba_ai_core",
        "prompt_values",
        "PromptValue",
    ),
    ("aibaba_ai_core", "runnables", "base", "RunnableBinding"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("aibaba_ai_core", "runnables", "branch", "RunnableBranch"): (
        "aibaba_ai_core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("aibaba_ai_core", "runnables", "fallbacks", "RunnableWithFallbacks"): (
        "aibaba_ai_core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("aibaba_ai_core", "output_parsers", "string", "StrOutputParser"): (
        "aibaba_ai_core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    ("aibaba_ai_core", "output_parsers", "list", "CommaSeparatedListOutputParser"): (
        "aibaba_ai_core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    ("aibaba_ai_core", "runnables", "base", "RunnableParallel"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("aibaba_ai_core", "outputs", "chat_generation", "ChatGenerationChunk"): (
        "aibaba_ai_core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("aibaba_ai_core", "messages", "chat", "ChatMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "human", "HumanMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "function", "FunctionMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "system", "SystemMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "tool", "ToolMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("aibaba_ai_core", "outputs", "generation", "GenerationChunk"): (
        "aibaba_ai_core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("aibaba_ai_core", "prompts", "chat", "BaseChatPromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("aibaba_ai_core", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    (
        "aibaba_ai_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ): (
        "aibaba_ai_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("aibaba_ai_core", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("aibaba_ai_core", "prompts", "string", "StringPromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("aibaba_ai_core", "prompt_values", "StringPromptValue"): (
        "aibaba_ai_core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("aibaba_ai_core", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "aibaba_ai_core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("aibaba_ai_core", "prompt_values", "ChatPromptValue"): (
        "aibaba_ai_core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("aibaba_ai_core", "prompt_values", "ChatPromptValueConcrete"): (
        "aibaba_ai_core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("aibaba_ai_core", "runnables", "base", "RunnableBindingBase"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("aibaba_ai_core", "runnables", "router", "RouterRunnable"): (
        "aibaba_ai_core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("aibaba_ai_core", "runnables", "passthrough", "RunnablePassthrough"): (
        "aibaba_ai_core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("aibaba_ai_core", "runnables", "base", "RunnableSequence"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("aibaba_ai_core", "runnables", "base", "RunnableEach"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("aibaba_ai_core", "runnables", "base", "RunnableEachBase"): (
        "aibaba_ai_core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    (
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ): (
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("aibaba_ai_core", "runnables", "configurable", "RunnableConfigurableFields"): (
        "aibaba_ai_core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("aibaba_ai_core", "runnables", "history", "RunnableWithMessageHistory"): (
        "aibaba_ai_core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("aibaba_ai_core", "runnables", "passthrough", "RunnableAssign"): (
        "aibaba_ai_core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("aibaba_ai_core", "runnables", "retry", "RunnableRetry"): (
        "aibaba_ai_core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
}

_JS_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("aibaba_ai_core", "messages", "AIMessage"): (
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("aibaba_ai_core", "messages", "AIMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "BaseMessage"): (
        "aibaba_ai_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("aibaba_ai_core", "messages", "BaseMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "ChatMessage"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("aibaba_ai_core", "messages", "ChatMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "FunctionMessage"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("aibaba_ai_core", "messages", "FunctionMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "HumanMessage"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("aibaba_ai_core", "messages", "HumanMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "SystemMessage"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("aibaba_ai_core", "messages", "SystemMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("aibaba_ai_core", "messages", "ToolMessage"): (
        "aibaba_ai_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("aibaba_ai_core", "messages", "ToolMessageChunk"): (
        "aibaba_ai_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("aibaba_ai_core", "prompts", "image", "ImagePromptTemplate"): (
        "aibaba_ai_core",
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
