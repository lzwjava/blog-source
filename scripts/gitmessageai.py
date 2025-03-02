import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import requests
import re
import json

load_dotenv()

def call_mistral_api(prompt):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "mistral-small-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
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


def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Gemini API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Gemini API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY environment variable not set.")
        return None
    
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
            commit_message = commit_message.replace('`', '')
            return commit_message
        else:
            print("Error: No response from the API.")
            return None
    except Exception as e:
        print(f"Error during API call: {e}")
        print(e)
        return None

def call_grok_api(prompt):
    api_key = os.environ.get("GROK_API_KEY")
    if not api_key:
        print("Error: GROK_API_KEY environment variable not set.")
        return None

    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "grok-2-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        json_response = response.json()
        if 'choices' in json_response and json_response['choices']:
            first_choice = json_response['choices'][0]
            if 'message' in first_choice and 'content' in first_choice['message']:
                return first_choice['message']['content']
            else:
                print("Unexpected response format: message or content missing")
                return None
        else:
            print("No choices found in the response")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

def gitmessageai(push=True, only_message=False, api='deepseek', allow_pull_push=False):
    # Stage all changes
    subprocess.run(["git", "add", "-A"], check=True)    

    # Get a detailed summary of the changes
    diff_process = subprocess.run(["git", "diff", "--staged", "--unified=0"], capture_output=True, text=True, check=True)
    diff_output = diff_process.stdout

    if not diff_output:
        print("No changes to commit.")
        return
    
    file_changes = []
    current_file = None
    lines = diff_output.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("diff --git"):
            parts = line.split(" ")
            if len(parts) >= 4:
                file_a = parts[2][2:]
                file_b = parts[3][2:]
                if file_a == file_b:
                    if i + 1 < len(lines) and "deleted file mode" in lines[i+1]:
                        file_changes.append(f"Deleted file {file_a}")
                        i += 1
                    elif i + 1 < len(lines) and "new file mode" in lines[i+1]:
                        file_changes.append(f"Added file {file_a}")
                        i += 1
                    elif i + 1 < len(lines):
                        file_changes.append(f"Updated file {file_a}")
                        i +=1
                else:
                    if i + 1 < len(lines) and "similarity index" in lines[i+1]:
                        file_changes.append(f"Renamed file {file_a} to {file_b}")
                        i += 1
        i += 1
    
    for change in file_changes:
        print(change)
    
    if not file_changes:
        print("No changes to commit.")
        return

    # Prepare the prompt for the AI
    prompt = f"""
Generate a concise commit message in Conventional Commits format for the following code changes.
Use one of the following types: feat, fix, docs, style, refactor, test, chore, perf, ci, build, or revert.
If applicable, include a scope in parentheses to describe the part of the codebase affected.
The commit message should not exceed 70 characters. Just give the commit message, without any leading or trailing notes.

Changed files:
{', '.join(file_changes[:20])}

"""    

    if api == 'deepseek':
        commit_message = call_deepseek_api(prompt)
        if not commit_message:
            return
    elif api == 'gemini':
        commit_message = call_gemini_api(prompt)
        if not commit_message:
            print("Error: No response from Gemini API.")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("Error: No response from Mistral API.")
            return
    elif api == 'grok':
        commit_message = call_grok_api(prompt)
        if not commit_message:
            print("Error: No response from Grok API.")
            return
    else:
        print(f"Error: Invalid API specified: {api}")
        return
    
    if commit_message and "```" in commit_message:
        commit_message = commit_message.replace("```", "")

    # Check if the commit message is empty
    if not commit_message:
        print("Error: Empty commit message generated. Aborting commit.")
        return
    
    if only_message:
        print(f"Suggested commit message: {commit_message}")
        return

    # Commit with the generated message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push the changes
    if push:
        try:
            subprocess.run(["git", "push"], check=True)
        except subprocess.CalledProcessError as e:
            if allow_pull_push:
                print("Push failed, attempting pull and push...")
                subprocess.run(["git", "pull", "--rebase"], check=True)
                subprocess.run(["git", "push"], check=True)
            else:
                print("Push failed.")
                raise e
    else:
        print("Changes committed locally, but not pushed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate commit message with AI and commit changes.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='Commit changes locally without pushing.')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='Only print the AI generated commit message.')
    parser.add_argument('--api', type=str, default='mistral', choices=['deepseek', 'gemini', 'mistral', 'grok'], help='API to use for commit message generation (deepseek, gemini, mistral, grok).')
    parser.add_argument('--allow-pull-push', dest='allow_pull_push', action='store_true', help='Allow git pull and push if git push failed.')

    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api, allow_pull_push=args.allow_pull_push)