---
audio: false
date: 2025-09-06
generated: true
image: false
lang: hant
layout: post
title: 剪貼簿至 Git 筆記儲存器
translated: true
type: note
---

當然可以——使用 Python + `pyperclip` 就能輕鬆實現。以下是一個小型守護行程風格的腳本，它會輪詢剪貼簿，每當發現**新**的文字長度超過 500 個字符時，就會將一個 Markdown 筆記寫入 Git 倉庫並提交（如果配置了推送，還會自動推送）。

### 功能說明

* 每約 0.7 秒輪詢一次剪貼簿。
* 忽略非文字內容和重複內容。
* 建立按日期歸檔的筆記檔案，例如 `notes/2025/09/2025-09-06_001530_8c9a8f.md`。
* 儲存一個小型的 `index.json` 檔案記錄已儲存的雜湊值，避免重複提交。
* 需要時自動執行 `git init`；提交更改；如果設定 `PUSH=1`（且已設定遠端/分支），則可選擇自動推送。

### 依賴項

```bash
pip install pyperclip
# 僅限 Linux：您還需要系統級安裝 xclip 或 xsel
```

### 腳本程式碼

```python
#!/usr/bin/env python3
import os, time, json, hashlib, subprocess, textwrap, datetime, pathlib, sys
from typing import Optional

try:
    import pyperclip
except Exception as e:
    print("Error: pyperclip not installed. Run `pip install pyperclip`.")
    sys.exit(1)

# ---- 配置 ----
REPO_DIR = os.environ.get("CLIP_REPO", os.path.expanduser("~/clipboard-notes"))
NOTES_DIR = "notes"
MIN_LEN = int(os.environ.get("MIN_LEN", "500"))
POLL_SEC = float(os.environ.get("POLL_SEC", "0.7"))
PUSH = os.environ.get("PUSH", "0") == "1"    # 設定 PUSH=1 以啟用 `git push`

INDEX_PATH = os.path.join(REPO_DIR, ".clip_index.json")  # 儲存已儲存筆記的雜湊值

# ---- 工具函數 ----
def run(cmd: list[str], cwd: Optional[str] = None, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)

def ensure_repo():
    os.makedirs(REPO_DIR, exist_ok=True)
    git_dir = os.path.join(REPO_DIR, ".git")
    if not os.path.isdir(git_dir):
        run(["git", "init"], cwd=REPO_DIR)
        # 可選：如果您的 git 預設分支不是 main，請設定預設分支
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
    # 保持簡單；僅轉義可能破壞 frontmatter 分隔符的三連字元
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
    # 同時將索引檔案加入版本控制
    run(["git", "add", os.path.relpath(INDEX_PATH, REPO_DIR)], cwd=REPO_DIR, check=False)
    run(["git", "commit", "-m", msg], cwd=REPO_DIR)

def git_push_if_enabled():
    if not PUSH:
        return
    # 如果配置了預設上游，則推送
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
            # 在某些系統上，如果剪貼簿不可用，paste 可能會拋出異常
            time.sleep(POLL_SEC)
            continue

        if isinstance(txt, str):
            # 僅處理新的剪貼簿文字
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

### 執行方法

1. 將腳本儲存為 `clipwatch.py`。
2. 設定您的倉庫路徑（可選）：

   ```bash
   export CLIP_REPO=~/my-notes
   export PUSH=1          # 可選，如果設定了遠端，則啟用 git push
   python3 clipwatch.py
   ```

### 設定開機自啟（macOS launchd 範例）

建立 `~/Library/LaunchAgents/com.zw.clipwatch.plist`：

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

然後執行：

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### 注意事項與潛在問題

* Linux：安裝 `xclip` 或 `xsel`，以便 `pyperclip` 可以存取剪貼簿。
* 此腳本僅監視**文字**。圖片/RTF 格式會被忽略。
* 注意敏感資訊——此腳本會捕獲您複製的任何超過閾值的內容。如果需要排除某些內容，可以添加簡單的阻擋規則（例如，如果文字包含 `-----BEGIN PRIVATE KEY-----`，或者通過在 macOS 上使用 `osascript` 查詢活動應用程式與黑名單匹配，則跳過）。
* 如果您希望按活動應用程式/視窗（例如「來自 Safari」）添加標籤，我可以添加該功能。

如果您更傾向於使用 Rust/Go 來構建更精簡的跨平台二進制檔案，或者希望檔案命名規則與您的部落格 Jekyll front-matter 匹配，請告訴我，我會為您量身定制。