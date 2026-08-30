def get_user_choice():

    print("\nWould you like additional learning resources?")
    print("1. Structured Roadmap")
    print("2. Relevant YouTube Videos")
    print("3. Both Roadmap and YouTube Videos")
    print("4. No, thanks")

    choice = input("\nEnter your choice (1-4): ").strip()

    return choice


async def generate_roadmap(user_query, llm):

    roadmap_prompt = f"""
The user asked:

{user_query}

Create a clear and structured learning roadmap based on
the user's request.

Include:

1. Beginner Stage
2. Intermediate Stage
3. Advanced Stage
4. Important concepts to learn
5. Recommended learning order

Make the roadmap practical, concise, and easy for a student
to follow.

Use clear headings and bullet points.
"""

    roadmap_response = llm.invoke(roadmap_prompt)

    print("\n========== STRUCTURED ROADMAP ==========\n")
    print(roadmap_response.text)
    print("\n========================================\n")


async def find_youtube_videos(user_query, agent):

    video_prompt = f"""
The user originally asked:

{user_query}

Find relevant YouTube videos that can help the user learn
this topic.

IMPORTANT TOOL INSTRUCTION:

Use the YouTube MCP tools to search for relevant videos.
Do not use Playwright or browser tools unless absolutely
necessary.

For each recommendation, provide:

- Video title
- Channel name
- Video link if available
- A short explanation of why the video is useful

Keep the response concise and structured.
"""

    video_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": video_prompt
                }
            ]
        }
    )

    final_response = video_response["messages"][-1]

    print("\n========== YOUTUBE RESOURCES ==========\n")
    print(final_response.text)
    print("\n=======================================\n")


async def handle_hitl_choice(
    choice,
    user_query,
    llm,
    agent
):

    # OPTION 1
    if choice == "1":

        print("\nGenerating a structured roadmap...\n")

        await generate_roadmap(
            user_query,
            llm
        )


    # OPTION 2
    elif choice == "2":

        print("\nFinding relevant YouTube videos...\n")

        await find_youtube_videos(
            user_query,
            agent
        )


    # OPTION 3
    elif choice == "3":

        print("\nGenerating roadmap and YouTube resources...\n")

        await generate_roadmap(
            user_query,
            llm
        )

        await find_youtube_videos(
            user_query,
            agent
        )


    # OPTION 4
    elif choice == "4":

        print(
            "\nOkay! No additional resources requested.\n"
        )


    # INVALID CHOICE
    else:

        print(
            "\nInvalid choice. Continuing normally.\n"
        )