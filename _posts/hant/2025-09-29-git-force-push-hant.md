---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 透過分支刪除進行 Git 強制推送
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

此腳本透過先刪除遠端分支，再推送本地分支來實現「強制推送」。這適用於允許分支刪除但不允許強制推送的儲存庫。

用法: python git_force_push.py <remote> <branch>
範例: python git_force_push.py origin main

注意：此操作假設您擁有足夠權限且允許分支刪除。
請謹慎使用，因為刪除分支可能會遺失提交記錄。
"""

import subprocess
import sys

def run_command(command):
    """執行 shell 指令並返回其輸出。"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"執行指令 '{command}' 時發生錯誤: {e}")
        print(f"標準錯誤: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python git_force_push.py <remote> <branch>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # 刪除遠端分支
    delete_cmd = f"git push {remote} :{branch}"
    print(f"正在刪除遠端分支: {delete_cmd}")
    run_command(delete_cmd)

    # 推送本地分支
    push_cmd = f"git push {remote} {branch}"
    print(f"正在推送本地分支: {push_cmd}")
    run_command(push_cmd)

    print("強制推送已成功完成。")
```

### 運作原理
- **刪除步驟**：執行 `git push origin :main` 來刪除遠端分支（如您的儲存庫所允許）。
- **推送步驟**：執行 `git push origin main` 來推送本地分支，在遠端重新建立分支。
- 這透過丟棄遠端歷史記錄並用本地歷史記錄替換，有效實現了強制推送。
- **安全/使用注意事項**：請先在非關鍵儲存庫中測試。此操作需要正確的 Git 設定和權限。如果儲存庫有額外保護（例如透過掛鉤），可能會失敗。不提供任何擔保；Git 操作可能具有破壞性。