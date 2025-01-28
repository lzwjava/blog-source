---
audio: true
lang: ja
layout: post
title: AIパワードのGitコミットメッセージ
translated: true
---

このPythonスクリプトは、システムのPATHに含まれるディレクトリ、例えば`~/bin`に配置する必要があります。

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
        print("Error: MISTRAL_API_KEY環境変数が設定されていません。")
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
            print(f"Mistral APIエラー: 無効なレスポンス形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral APIエラー: {e}")
        if e.response:
            print(f"レスポンスステータスコード: {e.response.status_code}")
            print(f"レスポンス内容: {e.response.text}")
        return None

def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY環境変数が設定されていません。")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # ステータスコードが悪い場合に例外を発生させます
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Gemini APIエラー: 無効なレスポンス形式: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Gemini APIエラー: {e}")
        if e.response:
            print(f"レスポンスステータスコード: {e.response.status_code}")
            print(f"レスポンス内容: {e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY環境変数が設定されていません。")
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
            print("Error: APIからのレスポンスがありません。")
            return None
    except Exception as e:
        print(f"API呼び出し中のエラー: {e}")
        print(e)
        return None

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # すべての変更をステージング
    subprocess.run(["git", "add", "-A"], check=True)

    # 変更の簡単なサマリーを取得
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("コミットする変更はありません。")
        return

    # AIのためのプロンプトを準備
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
            print("Error: Gemini APIからのレスポンスがありません。")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("Error: Mistral APIからのレスポンスがありません。")
            return
    else:
        print(f"Error: 無効なAPIが指定されました: {api}")
        return

    # コミットメッセージが空かどうかを確認
    if not commit_message:
        print("Error: 空のコミットメッセージが生成されました。コミットを中止します。")
        return

    if only_message:
        print(f"提案されたコミットメッセージ: {commit_message}")
        return

    # 生成されたメッセージでコミット
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # 変更をプッシュ
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("変更はローカルでコミットされましたが、プッシュされませんでした。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AIを使用してコミットメッセージを生成し、変更をコミットします。")
    parser.add_argument('--no-push', dest='push', action='store_false', help='変更をローカルでコミットし、プッシュしません。')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='AIが生成したコミットメッセージのみを表示します。')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='コミットメッセージ生成に使用するAPI (deepseek, gemini, またはmistral)。')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

このスクリプトは異なるAPIで呼び出すことができます。例:

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

その後、`~/.zprofile`ファイルに以下を追加します:

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

いくつかの改善点があります。

* 一つは、`git diff`を使用してファイルの詳細な変更を読み取るのではなく、ファイル名の変更のみを送信することです。AIサービスAPIに多くの詳細を提供したくありません。このケースでは、コミットメッセージを注意深く読む人は少ないため、必要ありません。

* 最近非常に人気があるため、Deepseek APIが失敗することがあります。その場合、Geminiを使用する必要があります。