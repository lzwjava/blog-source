---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 自動化博客管理草稿（VSCode 重啟）
translated: true
type: post
---

該腳本旨在自動化以結構化方式發布草稿部落格文章的流程。它特別適合部落格作者或內容創作者，他們會在文章準備好發布前將其儲存為草稿。以下是關於該腳本的延伸介紹，以提供更多背景資訊：

## 簡介

管理部落格或任何以內容為主的網站通常涉及在準備好發布前創建和儲存草稿。該腳本專為簡化將草稿文章移動到指定發布目錄的工作流程而設計，特別適用於靜態網站生成器設置，例如使用 Jekyll 或類似框架的情況。

該腳本執行以下關鍵任務：

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """檢查今天創建的草稿文件並將其移動到 _posts/en 目錄。"""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"草稿目錄 '{drafts_dir}' 不存在。沒有文件可發布。")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # 在草稿目錄中查找以今天日期開頭並以 -en.md 結尾的文件模式
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"在 '{drafts_dir}' 中沒有找到以 '{date_str}' 開頭的草稿文件可發布。")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"已將 '{file_name}' 從 '{drafts_dir}' 移動到 '{posts_en_dir}'。")
        except Exception as e:
            print(f"移動 '{file_name}' 時出錯：{e}")

    restart_vscode()

def restart_vscode():
    print("正在優雅地重啟 VSCode 以防止意外重新創建草稿文件...")
    try:
        if sys.platform == 'win32':
            # 優雅關閉，不使用 /f
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # 延遲以進行清理
            subprocess.Popen(['code', '.'])  # 重新打開
        elif sys.platform == 'darwin':
            # 使用 AppleScript 進行優雅退出
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # 使用 SIGTERM 進行優雅終止
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("不支持重啟 VSCode 的平台。")
    except Exception as e:
        print(f"重啟時出錯：{e}。請手動重啟 VSCode。")

if __name__ == "__main__":
    publish_drafts_to_posts()
```