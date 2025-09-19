---
audio: false
generated: false
image: false
lang: ja
layout: post
title: ブログ管理のためのVSCode再起動による自動ドラフト
translated: true
---

以下は提供されたMarkdownテキストの日本語訳です：

---

提供されたスクリプトは、ブログ記事の下書きを構造化された方法で公開するプロセスを自動化するために設計されています。このスクリプトは、記事を公開する準備が整うまで下書きとして管理するブロガーやコンテンツクリエイターに特に役立ちます。以下にスクリプトについての拡張された紹介を提供します：

## はじめに

ブログやコンテンツ主体のウェブサイトを管理する際、公開準備が整うまで下書きを作成して保存することがよくあります。このスクリプトは、静的サイトジェネレータのセットアップ（Jekyllなどのフレームワークを使用する場合など）で、下書き記事を指定された公開ディレクトリに移動するワークフローを効率化するためにカスタマイズされています。

このスクリプトは、以下の主要なタスクを実行します：

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """本日の日付で始まる下書きファイルを検索し、_posts/enディレクトリに移動します。"""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"下書きディレクトリ'{drafts_dir}'が存在しません。公開するファイルはありません。")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # 下書きディレクトリ内で、本日の日付で始まり、-en.mdで終わるファイルを検索するパターン
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"'{drafts_dir}'内に'{date_str}'で始まる下書きファイルが見つかりませんでした。")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"'{file_name}'を'{drafts_dir}'から'{posts_en_dir}'に移動しました。")
        except Exception as e:
            print(f"'{file_name}'の移動中にエラーが発生しました: {e}")

    restart_vscode()

def restart_vscode():
    print("下書きファイルの意図しない再作成を防ぐために、VSCodeを優雅に再起動します...")
    try:
        if sys.platform == 'win32':
            # /fなしで優雅に終了
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # クリーンアップのための遅延
            subprocess.Popen(['code', '.'])  # 再開
        elif sys.platform == 'darwin':
            # 優雅な終了のためにAppleScriptを使用
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # 優雅な終了のためにSIGTERMを使用
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("VSCodeの再起動に対応していないプラットフォームです。")
    except Exception as e:
        print(f"再起動中にエラーが発生しました: {e}。手動でVSCodeを再起動してください。")

if __name__ == "__main__":
    publish_drafts_to_posts()
```