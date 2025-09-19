import os
import sys
import argparse
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from deepseek_tool_client import call_deepseek_api
from post_utils import get_recent_posts, extract_post_data
from output_utils import determine_output_filename, write_recommendations_file
from api_utils import build_prompt, setup_tools, setup_initial_messages


def handle_tool_calls(response_message, messages, title_to_link):
    """Handle tool calls from the API response."""
    if hasattr(response_message, "tool_calls") and response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            if function_name == "get_links":
                try:
                    args = json.loads(tool_call.function.arguments)
                    titles = args["titles"]
                    links_response = {}
                    for title in titles:
                        link = title_to_link.get(title)
                        if link:
                            links_response[title] = {"link": link}
                        else:
                            links_response[title] = {"error": "Title not found"}
                    tool_response = json.dumps(links_response)
                except Exception as e:
                    tool_response = json.dumps(
                        {"error": f"Error processing tool call: {str(e)}"}
                    )

                messages.append(
                    {
                        "role": "tool",
                        "content": tool_response,
                        "tool_call_id": tool_call.id,
                    }
                )
        return True
    return False


def generate_recommendations(
    output_file=None, years=1, recommend_desc="10-year experienced backend engineer"
):
    """Generate AI-based blog post recommendations for a target audience using tool calls."""
    # Fetch and process blog post data
    recent_posts = get_recent_posts(years=years)
    post_data = extract_post_data(recent_posts)
    post_titles = sorted([item["title"] for item in post_data])
    title_to_link = {item["title"]: item["link"] for item in post_data}

    # Prepare prompt and tools
    prompt = build_prompt(post_titles, years, recommend_desc)
    tools = setup_tools()
    messages = setup_initial_messages(prompt)

    print(
        f"Initial prompt prepared with {len(post_titles)} post titles for audience: {recommend_desc}"
    )
    print("Making initial API call...")

    # Initial API call
    response_message = call_deepseek_api(messages=messages, tools=tools)
    messages.append(
        vars(response_message)
        if not isinstance(response_message, dict)
        else response_message
    )

    print("Messages:", messages)

    print("Initial API response received.")

    # Handle tool calls and make a follow-up API call if needed
    if handle_tool_calls(response_message, messages, title_to_link):
        print("Tool calls detected, making follow-up API call...")
        response_message = call_deepseek_api(messages=messages, tools=tools)
        messages.append(
            vars(response_message)
            if not isinstance(response_message, dict)
            else response_message
        )
        print("Follow-up API response received.")
    else:
        print("No tool calls detected, proceeding with initial response.")

    # Extract and save the final response
    ai_response = (
        response_message.content if hasattr(response_message, "content") else ""
    )
    final_output_file = determine_output_filename(output_file, recommend_desc)
    print(f"Saving recommendations to file: {final_output_file}")
    write_recommendations_file(final_output_file, ai_response, years, recommend_desc)
    print("Recommendations saved successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate blog post recommendations for backend engineers."
    )
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        help="Output markdown file name (e.g., '2025-07-22-recommend-for-engineers-en.md'). If not provided, uses today's date and a generated name.",
    )
    parser.add_argument(
        "--years",
        type=int,
        default=1,
        help="Number of years to consider for recent posts.",
    )
    parser.add_argument(
        "--recommend-desc",
        type=str,
        default="10-year experienced backend engineer",
        help="Description of the target audience for recommendations (e.g., '10-year experienced backend engineer').",
    )
    args = parser.parse_args()

    generate_recommendations(
        output_file=args.file, years=args.years, recommend_desc=args.recommend_desc
    )
