---
audio: false
date: 2025-09-06
generated: true
image: false
lang: hi
layout: post
title: क्लिपबोर्ड से गिट नोट सेवर
translated: true
type: note
---

बिल्कुल—यह Python + `pyperclip` के साथ बहुत ही संभव है। नीचे एक छोटा सा डेमन-स्टाइल स्क्रिप्ट है जो क्लिपबोर्ड को पोल करता है, और जब भी यह **नया** टेक्स्ट देखता है जो 500 वर्णों से लंबा होता है, तो यह एक Git रेपो में एक Markdown नोट लिखता है और उसे कमिट कर देता है (वैकल्पिक रूप से पुश करता है अगर कॉन्फ़िगर किया गया हो)।

### यह क्या करता है

* हर ~0.7s पर क्लिपबोर्ड को पोल करता है।
* गैर-टेक्स्ट सामग्री और डुप्लिकेट्स को नज़रअंदाज करता है।
* दिनांकित नोट फाइलें बनाता है जैसे `notes/2025/09/2025-09-06_001530_8c9a8f.md`।
* सेव किए गए हैश का एक छोटा `index.json` स्टोर करता है ताकि डुप्लिकेट कमिट से बचा जा सके।
* जरूरत पड़ने पर ऑटो-`git init`; कमिट करता है; वैकल्पिक रूप से पुश करता है अगर `PUSH=1` (और आपका रिमोट/ब्रांच पहले से सेट है)।

### डिपेंडेंसीज़

```bash
pip install pyperclip
# Linux only: आपको सिस्टम-वाइड xclip या xsel इंस्टॉल करने की आवश्यकता होगी
```

### स्क्रिप्ट

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

### इसे कैसे चलाएं

1. इसे `clipwatch.py` के रूप में सेव करें।
2. अपना रेपो पथ सेट करें (वैकल्पिक):

   ```bash
   export CLIP_REPO=~/my-notes
   export PUSH=1          # optional, enables git push if remote is set
   python3 clipwatch.py
   ```

### इसे लॉगिन पर चलने दें (macOS launchd उदाहरण)

`~/Library/LaunchAgents/com.zw.clipwatch.plist` बनाएं:

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

फिर:

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### नोट्स और सावधानियां

* Linux: `xclip` या `xsel` इंस्टॉल करें ताकि `pyperclip` क्लिपबोर्ड तक पहुंच सके।
* यह केवल **टेक्स्ट** को देखता है। इमेज/RTF को नज़रअंदाज कर दिया जाता है।
* सीक्रेट्स के प्रति सजग रहें—यह थ्रेशोल्ड से ऊपर की कोई भी चीज़ जो आप कॉपी करते हैं, कैप्चर कर लेगा। अगर आप एक्सक्लूजन चाहते हैं, तो एक साधारण ब्लॉकर जोड़ें (जैसे, स्किप करें अगर टेक्स्ट में `-----BEGIN PRIVATE KEY-----` हो, या एक्टिव ऐप `osascript` का उपयोग करके macOS पर क्वेरी करने पर डेनिलिस्ट से मैच करता हो)।
* अगर आप एक्टिव ऐप/विंडो द्वारा टैग करना चाहते हैं (जैसे, "Safari से"), तो मैं इसे जोड़ सकता हूं।

अगर आप एक लीनर, क्रॉस-प्लेटफॉर्म बाइनरी के लिए Rust/Go पसंद करते हैं, या फाइलनाम नियम चाहते हैं जो आपके ब्लॉग के Jekyll फ्रंट-मैटर से मेल खाते हों, तो बस कहें और मैं इसे अनुकूलित कर दूंगा।