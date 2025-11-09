---
audio: false
date: 2025-09-06
generated: true
image: false
lang: de
layout: post
title: Zwischenablage zu Git Notizspeicher
translated: true
type: note
---

Absolut — das ist sehr gut machbar mit Python + `pyperclip`. Hier ist ein kleines Daemon-artiges Skript, das die Zwischenablage abfragt und immer dann, wenn es **neuen** Text mit mehr als 500 Zeichen sieht, eine Markdown-Notiz in ein Git-Repo schreibt und committed (und optional pushed, falls konfiguriert).

### Was es tut

*   Fragt die Zwischenablage alle ~0,7s ab.
*   Ignoriert Nicht-Text-Inhalte und Duplikate.
*   Erstellt datierte Notizdateien wie `notes/2025/09/2025-09-06_001530_8c9a8f.md`.
*   Speichert einen kleinen `index.json` mit gespeicherten Hashes, um doppelte Commits zu vermeiden.
*   Auto-`git init` falls nötig; committed; optionales Pushen, falls `PUSH=1` (und dein Remote/Branch bereits eingerichtet sind).

### Abhängigkeiten

```bash
pip install pyperclip
# Nur Linux: Sie benötigen auch systemweit installiertes xclip oder xsel
```

### Das Skript

```python
#!/usr/bin/env python3
import os, time, json, hashlib, subprocess, textwrap, datetime, pathlib, sys
from typing import Optional

try:
    import pyperclip
except Exception as e:
    print("Error: pyperclip not installed. Run `pip install pyperclip`.")
    sys.exit(1)

# ---- Konfiguration ----
REPO_DIR = os.environ.get("CLIP_REPO", os.path.expanduser("~/clipboard-notes"))
NOTES_DIR = "notes"
MIN_LEN = int(os.environ.get("MIN_LEN", "500"))
POLL_SEC = float(os.environ.get("POLL_SEC", "0.7"))
PUSH = os.environ.get("PUSH", "0") == "1"    # set PUSH=1 to enable `git push`

INDEX_PATH = os.path.join(REPO_DIR, ".clip_index.json")  # stores hashes of saved notes

# ---- Hilfsfunktionen ----
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

### Ausführung

1.  Speichere es als `clipwatch.py`.
2.  Lege deinen Repo-Pfad fest (optional):

    ```bash
    export CLIP_REPO=~/my-notes
    export PUSH=1          # optional, enables git push if remote is set
    python3 clipwatch.py
    ```

### Automatischen Start beim Login einrichten (macOS launchd Beispiel)

Erstelle `~/Library/LaunchAgents/com.zw.clipwatch.plist`:

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

Dann:

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### Hinweise und Fallstricke

*   Linux: Installiere `xclip` oder `xsel`, damit `pyperclip` auf die Zwischenablage zugreifen kann.
*   Dies überwacht **nur Text**. Bilder/RTF werden ignoriert.
*   Achte auf Geheimnisse — dies erfasst alles, was du kopierst, das über der Schwelle liegt. Wenn du Ausschlüsse möchtest, füge einen einfachen Blocker hinzu (z.B. Überspringen, wenn der Text `-----BEGIN PRIVATE KEY-----` enthält, oder wenn die aktive App über eine Abfrage mit `osascript` unter macOS einer Ausschlussliste entspricht).
*   Wenn du nach aktiver App/Fenster taggen möchtest (z.B. "aus Safari"), kann ich das hinzufügen.

Wenn du Rust/Go für eine schlankere, plattformübergreifende Binärdatei bevorzugst oder Dateinamen-Regeln möchtest, die dem Jekyll Front-Matter deines Blogs entsprechen, sag Bescheid und ich passe es an.