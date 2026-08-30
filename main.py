from hitl import get_user_choice, handle_hitl_choice
from system_prompt import SYSTEM_PROMPT
from hitl import get_user_choice
from guardrails import check_input
import asyncio
import logging

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from mcp_client import get_mcp_tools


logging.getLogger("google_genai.models").setLevel(logging.ERROR)
logging.getLogger("google_genai").setLevel(logging.ERROR)
logging.getLogger("langchain_google_genai").setLevel(logging.ERROR)


load_dotenv()


async def main():

    print("Loading MCP tools...")

    tools = await get_mcp_tools()

    print(f"Loaded {len(tools)} MCP tools.")


    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
    )


    agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
    )


    print("\nAI Learning Assistant")
    print("\nType exit to quit")


    while True:

        user = input("\nYou: ")

        if user.lower() == "exit":
            print("\nGoodbye\n")
            break

        is_safe, message = check_input(user)

        if not is_safe:
            print("\nAI:", message)
            continue


        try:

            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user,
                        }
                    ]
                }
            )


            # Get the final response
            final_response = response["messages"][-1]

            print("\nAI:", final_response.text)
            print()

            choice = get_user_choice()

            await handle_hitl_choice(
                choice=choice,
                user_query=user,
                llm=llm,
                agent=agent
            )

            


        except Exception as e:
            print("\nERROR:", e)
            print()


if __name__ == "__main__":
    asyncio.run(main())