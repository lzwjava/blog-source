---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ja
layout: post
title: クリップボードからGitノート保存
translated: true
type: note
---

もちろん、Python + `pyperclip`で実現可能です。以下は、クリップボードを監視し、500文字以上の**新しい**テキストを検出するたびにGitリポジトリにMarkdownノートを書き込み、コミットする（設定によりプッシュも可能）デーモン形式のスクリプトです。

### 機能

* 約0.7秒ごとにクリップボードを監視
* 非テキストコンテンツと重複を無視
* `notes/2025/09/2025-09-06_001530_8c9a8f.md` のような日付ベースのノートファイルを作成
* 保存済みハッシュを小さな `index.json` に保存し、重複コミットを防止
* 必要に応じて自動で `git init` を実行、コミット、`PUSH=1` 設定時はプッシュも実行（リモート/ブランチが設定済みの場合）

### 依存関係

```bash
pip install pyperclip
# Linuxのみ: システムに xclip または xsel をインストールする必要があります
```

### スクリプト

```python
#!/usr/bin/env python3
import os, time, json, hashlib, subprocess, textwrap, datetime, pathlib, sys
from typing import Optional

try:
    import pyperclip
except Exception as e:
    print("Error: pyperclip not installed. Run `pip install pyperclip`.")
    sys.exit(1)

# ---- 設定 ----
REPO_DIR = os.environ.get("CLIP_REPO", os.path.expanduser("~/clipboard-notes"))
NOTES_DIR = "notes"
MIN_LEN = int(os.environ.get("MIN_LEN", "500"))
POLL_SEC = float(os.environ.get("POLL_SEC", "0.7"))
PUSH = os.environ.get("PUSH", "0") == "1"    # PUSH=1 を設定すると `git push` が有効になります

INDEX_PATH = os.path.join(REPO_DIR, ".clip_index.json")  # 保存済みノートのハッシュを格納

# ---- ユーティリティ ----
def run(cmd: list[str], cwd: Optional[str] = None, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)

def ensure_repo():
    os.makedirs(REPO_DIR, exist_ok=True)
    git_dir = os.path.join(REPO_DIR, ".git")
    if not os.path.isdir(git_dir):
        run(["git", "init"], cwd=REPO_DIR)
        # オプション: gitのデフォルトブランチがmainでない場合、デフォルトブランチを設定
        # run(["git", "checkout", "-b", "main"], cwd=REPO_DIR, check=False)

def load_index() -> set[str]:
    if os.path.isfile(INDEX_PATH):
        try:
            with open(INDEX_PATH, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def save_index(hashes: set[str]):
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(list(hashes)), f, ensure_ascii=False, indent=2)

def sha1(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8", errors="replace")).hexdigest()

def sanitize_for_frontmatter(s: str) -> str:
    # シンプルに保つ; トリプルダッシュのフェンスリスクのみエスケープ
    return s.replace("---", "—")

def write_note(content: str, h: str) -> str:
    now = datetime.datetime.now()
    y = f"{now.year:04d}"
    m = f"{now.month:02d}"
    subdir = os.path.join(REPO_DIR, NOTES_DIR, y, m)
    os.makedirs(subdir, exist_ok=True)
    ts = now.strftime("%Y-%m-%d_%H%M%S")
    fname = f"{ts}_{h[:6]}.md"
    path = os.path.join(subdir, fname)

    snippet = content.strip().splitlines()[0][:120]
    fm_title = sanitize_for_frontmatter(snippet if snippet else f"Clipboard note {ts}")

    body = textwrap.dedent(f"""\
    ---
    title: "{fm_title}"
    created: "{now.isoformat(timespec='seconds')}"
    source: "clipboard"
    length: {len(content)}
    hash: "{h}"
    ---

    {content}
    """)
    with open(path, "w", encoding="utf-8") as f:
        f.write(body)
    return path

def git_commit(path: str, msg: str):
    rel = os.path.relpath(path, REPO_DIR)
    run(["git", "add", rel], cwd=REPO_DIR)
    # インデックスもバージョン管理対象に追加
    run(["git", "add", os.path.relpath(INDEX_PATH, REPO_DIR)], cwd=REPO_DIR, check=False)
    run(["git", "commit", "-m", msg], cwd=REPO_DIR)

def git_push_if_enabled():
    if not PUSH:
        return
    # 設定済みの場合、デフォルトのアップストリームにプッシュ
    try:
        run(["git", "push"], cwd=REPO_DIR, check=False)
    except Exception:
        pass

def main():
    print(f"[clipwatch] repo: {REPO_DIR} | min_len: {MIN_LEN} | push: {PUSH}")
    ensure_repo()
    seen_hashes = load_index()
    last_text = None

    while True:
        try:
            txt = pyperclip.paste()
        except Exception as e:
            # 一部のシステムでは、クリップボードが利用できない場合に例外が発生する可能性があります
            time.sleep(POLL_SEC)
            continue

        if isinstance(txt, str):
            # 新しいクリップボードテキストのみ処理
            if txt != last_text and len(txt) >= MIN_LEN:
                h = sha1(txt)
                if h not in seen_hashes:
                    path = write_note(txt, h)
                    seen_hashes.add(h)
                    save_index(seen_hashes)

                    first_line = txt.strip().splitlines()[0] if txt.strip() else ""
                    commit_msg = f"Add clipboard note: {first_line[:60]}… ({len(txt)} chars)"
                    try:
                        git_commit(path, commit_msg)
                        git_push_if_enabled()
                        print(f"[clipwatch] saved: {os.path.relpath(path, REPO_DIR)}")
                    except subprocess.CalledProcessError as e:
                        print("[clipwatch] git error:", e.stderr or e.stdout)

            last_text = txt
        time.sleep(POLL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[clipwatch] bye.")
```

### 実行方法

1. `clipwatch.py` として保存
2. リポジトリパスを設定（オプション）:

   ```bash
   export CLIP_REPO=~/my-notes
   export PUSH=1          # オプション、リモートが設定済みの場合 git push を有効化
   python3 clipwatch.py
   ```

### ログイン時に実行する設定（macOS launchd の例）

`~/Library/LaunchAgents/com.zw.clipwatch.plist` を作成:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
 <dict>
  <key>Label</key><string>com.zw.clipwatch</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/env</string>
    <string>bash</string>
    <string>-lc</string>
    <string>CLIP_REPO="$HOME/clipboard-notes" PUSH=1 python3 "$HOME/clipwatch.py"</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>$HOME/clipwatch.log</string>
  <key>StandardErrorPath</key><string>$HOME/clipwatch.err</string>
 </dict>
</plist>
```

その後:

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### 注意点

* Linux: `pyperclip` がクリップボードにアクセスできるように `xclip` または `xsel` をインストール
* **テキスト**のみ監視。画像/RTFは無視
* 機密情報に注意 - 閾値を超えるテキストはすべてキャプチャされます。除外したい場合は、簡単なブロッカーを追加（例: テキストに `-----BEGIN PRIVATE KEY-----` が含まれる場合はスキップ、またはmacOSで `osascript` を使用してアクティブなアプリが拒否リストに一致する場合はスキップ）
* アクティブなアプリ/ウィンドウでタグ付けしたい場合（例: "Safariから"）、追加可能です

より軽量なクロスプラットフォームバイナリとしてRust/Goを希望する場合、またはブログのJekyll front-matterに合わせたファイル名ルールが必要な場合は、お知らせください。合わせて調整します。