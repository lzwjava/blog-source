import subprocess
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

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
    
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        if response and response.choices:
            commit_message = response.choices[0].message.content.strip()
        else:
            print("Error: No response from the API.")
            return
    except Exception as e:
        print(f"Error during API call: {e}")
        return

    # Debug: Print the API response
    print(f"API Response: {response}")


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