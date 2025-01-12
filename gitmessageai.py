import subprocess
import json
import os

def gitmessageai():
    # Stage all changes
    subprocess.run(["git", "add", "-A"], check=True)

    # Get the diff of staged changes
    diff_process = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
    diff = diff_process.stdout

    # Prepare the prompt for the AI
    prompt = f"Generate a concise and meaningful commit message for the following code changes:\n\n{diff}"

    # Send the prompt to the DeepSeek API
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY environment variable not set.")
        return

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 100
    }
    
    try:
        response_process = subprocess.run(
            ["curl", "-s", "-X", "POST", "https://api.deepseek.com/v1/chat/completions",
             "-H", "Content-Type: application/json",
             "-H", f"Authorization: Bearer {api_key}",
             "-d", json.dumps(data)],
            capture_output=True,
            text=True,
            check=True
        )
        response = response_process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error during API call: {e}")
        print(f"Response: {e.stderr}")
        return

    # Debug: Print the API response
    print(f"API Response: {response}")

    # Extract the generated commit message from the API response
    try:
        response_json = json.loads(response)
        commit_message = response_json['choices'][0]['message']['content'].strip()
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error parsing API response: {e}")
        return

    # Check if the commit message is empty
    if not commit_message:
        print("Error: Empty commit message generated. Aborting commit.")
        return

    # Commit with the generated message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push the changes
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    gitmessageai()