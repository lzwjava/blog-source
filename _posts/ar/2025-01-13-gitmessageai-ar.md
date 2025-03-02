---
audio: false
generated: false
lang: ar
layout: post
title: رسائل الالتزام في Git التي يعمل بالذكاء الاصطناعي
translated: true
---

يجب وضع هذا البرنامج النصي لـ Python في دليل مضمن في مسار النظام الخاص بك، مثل `~/bin`.

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import requests

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
        "model": "mistral-large-latest",
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
            return response_json['choices'][0]['message']['content']
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

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # Stage all changes
    subprocess.run(["git", "add", "-A"], check=True)

    # Get a brief summary of the changes
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("No changes to commit.")
        return

    # Prepare the prompt for the AI
    prompt = f"""
Generate a concise commit message in Conventional Commits format for the following code changes.
Use one of the following types: feat, fix, docs, style, refactor, test, chore, perf, ci, build, or revert.
If applicable, include a scope in parentheses to describe the part of the codebase affected.
The commit message should not exceed 70 characters.

Changed files:
{changed_files}

Commit message:
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
    else:
        print(f"Error: Invalid API specified: {api}")
        return

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
        subprocess.run(["git", "push"], check=True)
    else:
        print("Changes committed locally, but not pushed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate commit message with AI and commit changes.")
    parser.add_argument('--no-push', dest='push', action='store_false', help='Commit changes locally without pushing.')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='Only print the AI generated commit message.')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='API to use for commit message generation (deepseek, gemini, or mistral).')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

يمكن استدعاء هذا البرنامج النصي باستخدام واجهات برمجة التطبيقات المختلفة. على سبيل المثال:

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

ثم ، في ملف `~/.zprofile` الخاص بك ، أضف ما يلي:

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

هناك العديد من التحسينات.

* واحدة هي إرسال تغييرات أسماء الملفات فقط ، وليس قراءة التغييرات التفصيلية للملف باستخدام `git diff`. لا نريد إعطاء الكثير من التفاصيل لواجهة برمجة تطبيقات الخدمة الذكية. في هذه الحالة ، لا نحتاج إليها ، لأن القليل من الأشخاص سيقرأون رسائل الالتزام بعناية.

* في بعض الأحيان ، قد تفشل واجهة برمجة تطبيقات Deepseek ، لأنها شائعة الاستخدام حديثًا. قد نحتاج إلى استخدام Gemini بدلاً من ذلك.