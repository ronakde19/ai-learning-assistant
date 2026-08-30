import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient


# Load variables from .env
load_dotenv()


async def get_mcp_tools():

    client = MultiServerMCPClient(
        {
            "playwright": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "@playwright/mcp@latest"
                ]
            },

            "youtube": {
                "transport": "stdio",
                "command": "npx",
                "args": [
                    "-y",
                    "zubeid-youtube-mcp-server"
                ]
            }
        }
    )

    tools = await client.get_tools()

    return tools


async def main():

    try:
        print("\nConnecting to MCP servers...\n")

        tools = await get_mcp_tools()

        print("Successfully connected!\n")
        print("Available MCP tools:\n")

        for tool in tools:
            print("-", tool.name)

    except Exception as e:
        print("\nMCP Connection Error:")
        print(e)


if __name__ == "__main__":
    asyncio.run(main())