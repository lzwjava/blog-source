---
audio: true
lang: ja
layout: post
title: AIが生成するGitコミットメッセージ
translated: true
---

```python
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse

load_dotenv()

def gitmessageai(push=True):
    """
    ステージングされた変更に基づいてAIを使用してコミットメッセージを生成し、コミットします。

    Args:
        push (bool, optional): コミット後に変更をプッシュするかどうか。デフォルトはTrue。
    """
    # すべての変更をステージング
    subprocess.run(["git", "add", "-A"], check=True)

    # ステージングされた変更の差分を取得
    diff_process = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True, check=True)
    diff = diff_process.stdout

    if not diff:
        print("コミットする変更がありません。")
        return

    # AIへのプロンプトを準備
    prompt = f"""
以下のコード変更に対して、Conventional Commits形式で簡潔なコミットメッセージを生成してください。
次のいずれかのタイプを使用してください: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert。
該当する場合は、影響を受けるコードベースの部分を説明するために括弧内にスコープを含めてください。
コミットメッセージは70文字を超えないようにしてください。

コード変更:
{diff}

コミットメッセージ:
"""    

    # DeepSeek APIにプロンプトを送信
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("エラー: DEEPSEEK_API_KEY環境変数が設定されていません。")
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
            commit_message = commit_message.replace('`', '')
        else:
            print("エラー: APIからの応答がありません。")
            return
    except Exception as e:
        print(f"API呼び出し中にエラーが発生しました: {e}")
        return

    # デバッグ: APIの応答を表示
    print(f"API応答: {response}")


    # コミットメッセージが空かどうかを確認
    if not commit_message:
        print("エラー: 空のコミットメッセージが生成されました。コミットを中止します。")
        return

    # 生成されたメッセージでコミット
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # 変更をプッシュ
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        print("変更はローカルでコミットされましたが、プッシュされていません。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AIを使用してコミットメッセージを生成し、変更をコミットします。")
    parser.add_argument('--no-push', dest='push', action='store_false', help='変更をローカルでコミットし、プッシュしません。')
    args = parser.parse_args()
    gitmessageai(push=args.push)
```

次に、`~/.zprofile`ファイルに以下を追加します:

```
function gitpush {
  python ~/bin/gitmessageai.py
}

function gitcommit {
  python ~/bin/gitmessageai.py --no-push
}

alias gpa=gitpush
alias gca=gitcommit
```