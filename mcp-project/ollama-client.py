from llama_index.llm.ollama import Ollama
from llama_core import settings
from llama_index.tool.mcp import McpToolSpec
from llama_index.core.agent.workflow import FunctionAgent

# setup our LLM
llm = Ollama(model_name="llama3.2:latest")
settings.llm = llm


# define system prompt.
SYSTEM_PROMPT = """\
    You are a helpful assistant.
    You have access to the following tools:
    1. get_data(query: str) -> str
    2. write_data(query: str) -> str
    
    """

async def get_agent(tools: McpToolSpec):
    tools = await tools.to_tool_list_async()

    # define our agent
    agent = FunctionAgent(
        name="sqlite-mcp-agent",
        description="SQLite MCP Agent",
        llm=llm,
        system_prompt=SYSTEM_PROMPT,
        tools=tools
        )
    return agent
    





