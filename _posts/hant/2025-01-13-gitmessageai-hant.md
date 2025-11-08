---
audio: false
generated: false
image: false
lang: hant
layout: post
title: AI 驅動 Git 提交消息
translated: true
type: post
---

此 Python 腳本應放置在系統 PATH 中的目錄中，例如 `~/bin`。

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
        print("錯誤：MISTRAL_API_KEY 環境變數未設置。")
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
            print(f"Mistral API 錯誤：無效的回應格式：{response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API 錯誤：{e}")
        if e.response:
            print(f"回應狀態碼：{e.response.status_code}")
            print(f"回應內容：{e.response.text}")
        return None

def call_gemini_api(prompt):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("錯誤：GEMINI_API_KEY 環境變數未設置。")
        return None
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, json=payload, params=params)
        response.raise_for_status()  # 對於壞狀態碼引發異常
        response_json = response.json()
        if response_json and 'candidates' in response_json and response_json['candidates']:
            return response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Gemini API 錯誤：無效的回應格式：{response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Gemini API 錯誤：{e}")
        if e.response:
            print(f"回應狀態碼：{e.response.status_code}")
            print(f"回應內容：{e.response.text}")
        return None

def call_deepseek_api(prompt):
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("錯誤：DEEPSEEK_API_KEY 環境變數未設置。")
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
            print("錯誤：API 無回應。")
            return None
    except Exception as e:
        print(f"API 呼叫錯誤：{e}")
        print(e)
        return None

def gitmessageai(push=True, only_message=False, api='deepseek'):
    # 暫存所有更改
    subprocess.run(["git", "add", "-A"], check=True)

    # 獲取更改的簡短摘要
    files_process = subprocess.run(["git", "diff", "--staged", "--name-only"], capture_output=True, text=True, check=True)
    changed_files = files_process.stdout

    if not changed_files:
        print("無更改可提交。")
        return

    # 為 AI 準備提示
    prompt = f"""
生成一個簡潔的提交訊息，使用 Conventional Commits 格式，針對以下代碼更改。
使用以下類型之一：feat、fix、docs、style、refactor、test、chore、perf、ci、build 或 revert。
如果適用，包括括號中的範圍以描述受影響的代碼庫部分。
提交訊息不應超過 70 個字符。

更改的文件：
{changed_files}

提交訊息：
"""

    if api == 'deepseek':
        commit_message = call_deepseek_api(prompt)
        if not commit_message:
            return
    elif api == 'gemini':
        commit_message = call_gemini_api(prompt)
        if not commit_message:
            print("錯誤：Gemini API 無回應。")
            return
    elif api == 'mistral':
        commit_message = call_mistral_api(prompt)
        if not commit_message:
            print("錯誤：Mistral API 無回應。")
            return
    else:
        print(f"錯誤：指定的 API 無效：{api}")
        return

    # 檢查提交訊息是否為空
    if not commit_message:
        print("錯誤：生成的提交訊息為空。中止提交。")
        return

    if only_message:
        print(f"建議的提交訊息：{commit_message}")
        return

    # 使用生成的訊息進行提交
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # 推送更改
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("更改已本地提交，但未推送。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用 AI 生成提交訊息並提交更改。")
    parser.add_argument('--no-push', dest='push', action='store_false', help='本地提交更改而不推送。')
    parser.add_argument('--only-message', dest='only_message', action='store_true', help='僅打印 AI 生成的提交訊息。')
    parser.add_argument('--api', type=str, default='deepseek', choices=['deepseek', 'gemini', 'mistral'], help='用於生成提交訊息的 API（deepseek、gemini 或 mistral）。')
    args = parser.parse_args()
    gitmessageai(push=args.push, only_message=args.only_message, api=args.api)
```

此腳本可以使用不同的 API 調用。例如：

```bash
python ~/bin/gitmessageai.py
python ~/bin/gitmessageai.py --no-push
python ~/bin/gitmessageai.py --only-message
python ~/bin/gitmessageai.py --api gemini
python ~/bin/gitmessageai.py --api mistral --no-push
python ~/bin/gitmessageai.py --api deepseek --only-message
```

然後，在你的 `~/.zprofile` 文件中添加以下內容：

```bash
alias gpa='python ~/bin/gitmessageai.py'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'
```

有幾個改進。

* 一個是只發送文件名更改，而不是使用 `git diff` 讀取文件的詳細更改。我們不想給 AI 服務 API 提供太多詳細信息。在這種情況下，我們不需要它，因為很少有人會仔細閱讀提交訊息。

* 有時 Deepseek API 會失敗，因為最近它非常受歡迎。我們可能需要改用 Gemini。