import os
import requests

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"


def call_mistral_api_with_tools(prompt, tools=None):
    api_key = MISTRAL_API_KEY
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None

    url = MISTRAL_API_URL
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": prompt}],
    }

    if tools:
        data["tools"] = tools

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and response_json["choices"]:
            content = response_json["choices"][0]["message"]["content"]
            return content
        else:
            print(f"Mistral API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None


if __name__ == "__main__":
    # Tool for generating a filename with specific format
    filename_tool = [
        {
            "type": "function",
            "function": {
                "name": "generate_filename",
                "description": "Generate a short, unique filename segment with exactly 3 lowercase English words connected by hyphens.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filename": {
                            "type": "string",
                            "description": "A filename segment with 3 lowercase English words connected by hyphens, e.g., recommend-for-engineers",
                        }
                    },
                    "required": ["filename"],
                },
            },
        }
    ]

    recommend_desc = "software engineers"
    default_name_prompt = f"""Generate a short, unique filename segment for a blog post recommending content for a {recommend_desc}. The format must be exactly 3 lowercase English words connected by hyphens, like 'recommend-for-engineers'. Only output the filename segment without quotes or additional text."""

    result = call_mistral_api_with_tools(default_name_prompt, tools=filename_tool)
    print(result)
