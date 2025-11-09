---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: ブランチ削除によるGit強制プッシュ
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

このスクリプトは、リモートブランチを削除してからローカルブランチをプッシュすることで、
「強制プッシュ」を実行します。これは、リポジトリがブランチ削除を許可しているが
強制プッシュを許可していない場合に機能します。

使用方法: python git_force_push.py <remote> <branch>
例: python git_force_push.py origin main

注意: 十分な権限があり、削除が許可されていることを前提としています。
ブランチを削除するとコミットが失われる可能性があるため注意してください。
"""

import subprocess
import sys

def run_command(command):
    """シェルコマンドを実行し、その出力を返します。"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"コマンド '{command}' の実行中にエラーが発生しました: {e}")
        print(f"標準エラー出力: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python git_force_push.py <remote> <branch>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # リモートブランチを削除
    delete_cmd = f"git push {remote} :{branch}"
    print(f"リモートブランチを削除中: {delete_cmd}")
    run_command(delete_cmd)

    # ローカルブランチをプッシュ
    push_cmd = f"git push {remote} {branch}"
    print(f"ローカルブランチをプッシュ中: {push_cmd}")
    run_command(push_cmd)

    print("強制プッシュが正常に完了しました。")
```

### 動作の仕組み
- **削除ステップ**: `git push origin :main` を実行してリモートブランチを削除します（リポジトリで許可されている場合）。
- **プッシュステップ**: `git push origin main` を実行してローカルブランチをプッシュし、リモートで新しく作成します。
- これにより、リモートの履歴を破棄してローカルの履歴で置き換えることで、実質的に強制プッシュを実現します。
- **安全性/使用上の注意**: 重要なリポジトリで実行する前にテストしてください。適切なGit設定と権限が必要です。リポジトリに追加の保護（フックなど）がある場合、失敗する可能性があります。保証はありません。Git操作は破壊的になる可能性があります。