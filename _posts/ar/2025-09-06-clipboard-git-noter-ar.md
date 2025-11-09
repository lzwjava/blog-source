---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ar
layout: post
title: حافظة الملاحظات من الحافظة إلى جيت
translated: true
type: note
---

بالتأكيد — هذا ممكن جدًا باستخدام Python + `pyperclip`. فيما يلي برنامج نصي صغير على شكل خفي (daemon) يراقب الحافظة، وعندما يرى نصًا **جديدًا** أطول من 500 حرف، يكتب ملاحظة Markdown في مستودع Git ويُسجلها (ويدفعها إذا تم التهيئة).

### ما يفعله

* يتحقق من الحافظة كل ~0.7 ثانية.
* يتجاهل المحتوى غير النصي والمكرر.
* ينشئ ملفات ملاحظات مؤرَّخة مثل `notes/2025/09/2025-09-06_001530_8c9a8f.md`.
* يخزن ملف `index.json` صغيرًا يحتوي على تجزئات القيم المحفوظة لتجنب التسجيلات المكررة.
* يُنشئ مستودع Git تلقائيًا (`git init`) إذا لزم الأمر؛ يُسجل التغييرات؛ ويدفعها اختياريًا إذا كان `PUSH=1` (وتم تعيين المسار البعيد والفرع مسبقًا).

### التبعيات

```bash
pip install pyperclip
# Linux only: you'll also need xclip or xsel installed system-wide
```

### البرنامج النصي

```python
#!/usr/bin/env python3
import os, time, json, hashlib, subprocess, textwrap, datetime, pathlib, sys
from typing import Optional

try:
    import pyperclip
except Exception as e:
    print("Error: pyperclip not installed. Run `pip install pyperclip`.")
    sys.exit(1)

# ---- Config ----
REPO_DIR = os.environ.get("CLIP_REPO", os.path.expanduser("~/clipboard-notes"))
NOTES_DIR = "notes"
MIN_LEN = int(os.environ.get("MIN_LEN", "500"))
POLL_SEC = float(os.environ.get("POLL_SEC", "0.7"))
PUSH = os.environ.get("PUSH", "0") == "1"    # set PUSH=1 to enable `git push`

INDEX_PATH = os.path.join(REPO_DIR, ".clip_index.json")  # stores hashes of saved notes

# ---- Utilities ----
def run(cmd: list[str], cwd: Optional[str] = None, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)

def ensure_repo():
    os.makedirs(REPO_DIR, exist_ok=True)
    git_dir = os.path.join(REPO_DIR, ".git")
    if not os.path.isdir(git_dir):
        run(["git", "init"], cwd=REPO_DIR)
        # Optional: set default branch if your git default is not main
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
    # keep it simple; escape only triple-dashes fence risk
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
    # also add index to keep it versioned
    run(["git", "add", os.path.relpath(INDEX_PATH, REPO_DIR)], cwd=REPO_DIR, check=False)
    run(["git", "commit", "-m", msg], cwd=REPO_DIR)

def git_push_if_enabled():
    if not PUSH:
        return
    # Push to default upstream if configured
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
            # On some systems paste can throw if clipboard is not available
            time.sleep(POLL_SEC)
            continue

        if isinstance(txt, str):
            # Only process new clipboard text
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

### كيفية التشغيل

1. احفظه باسم `clipwatch.py`.
2. عيّن مسار المستودع (اختياري):

   ```bash
   export CLIP_REPO=~/my-notes
   export PUSH=1          # optional, enables git push if remote is set
   python3 clipwatch.py
   ```

### جعله يعمل عند تسجيل الدخول (مثال لـ macOS launchd)

أنشئ `~/Library/LaunchAgents/com.zw.clipwatch.plist`:

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

ثم:

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### ملاحظات وتحذيرات

* Linux: قم بتثبيت `xclip` أو `xsel` حتى يتمكن `pyperclip` من الوصول إلى الحافظة.
* هذا يراقب **النص** فقط. يتم تجاهل الصور و RTF.
* كن حذرًا بشأن الأسرار — سيقوم هذا بالتقاط أي شيء تنسخه فوق الحد المطلوب. إذا كنت تريد استثناءات، أضف مانعًا بسيطًا (مثل تخطي النص إذا كان يحتوي على `-----BEGIN PRIVATE KEY-----`، أو إذا تطابق التطبيق النشط مع قائمة حظر عن طريق الاستعلام باستخدام `osascript` على macOS).
* إذا كنت تريد إضافة وسم باسم التطبيق/النافذة النشط (مثل "من Safari")، يمكنني إضافته.

إذا كنت تفضل Rust/Go للحصول على ملف ثنائي أخف وزنًا ومتعدد المنصات، أو تريد قواعد لأسماء الملفات تتطابق مع front-matter في Jekyll لمدونتك، قل لي وسأعدلها لك.