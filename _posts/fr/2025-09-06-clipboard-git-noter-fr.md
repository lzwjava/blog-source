---
audio: false
date: 2025-09-06
generated: true
image: false
lang: fr
layout: post
title: Sauvegarde de Notes du Presse-papiers vers Git
translated: true
type: note
---

Absolument — c'est tout à fait réalisable avec Python + `pyperclip`. Voici un petit script de type démon qui surveille le presse-papiers, et chaque fois qu'il détecte un **nouveau** texte de plus de 500 caractères, il écrit une note au format Markdown dans un dépôt Git et effectue un commit (et pousse éventuellement si configuré).

### Fonctionnalités

* Surveille le presse-papiers toutes les ~0,7s.
* Ignore le contenu non textuel et les doublons.
* Crée des fichiers de notes datés comme `notes/2025/09/2025-09-06_001530_8c9a8f.md`.
* Stocke un petit `index.json` des hachages sauvegardés pour éviter les commits en double.
* Effectue un `git init` automatique si nécessaire ; commit ; pousse optionnellement si `PUSH=1` (et si votre dépôt distant/branche sont déjà configurés).

### Dépendances

```bash
pip install pyperclip
# Linux uniquement : vous devrez aussi installer xclip ou xsel au niveau du système
```

### Le script

```python
#!/usr/bin/env python3
import os, time, json, hashlib, subprocess, textwrap, datetime, pathlib, sys
from typing import Optional

try:
    import pyperclip
except Exception as e:
    print("Erreur : pyperclip non installé. Exécutez `pip install pyperclip`.")
    sys.exit(1)

# ---- Configuration ----
REPO_DIR = os.environ.get("CLIP_REPO", os.path.expanduser("~/clipboard-notes"))
NOTES_DIR = "notes"
MIN_LEN = int(os.environ.get("MIN_LEN", "500"))
POLL_SEC = float(os.environ.get("POLL_SEC", "0.7"))
PUSH = os.environ.get("PUSH", "0") == "1"    # définir PUSH=1 pour activer `git push`

INDEX_PATH = os.path.join(REPO_DIR, ".clip_index.json")  # stocke les hachages des notes sauvegardées

# ---- Utilitaires ----
def run(cmd: list[str], cwd: Optional[str] = None, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)

def ensure_repo():
    os.makedirs(REPO_DIR, exist_ok=True)
    git_dir = os.path.join(REPO_DIR, ".git")
    if not os.path.isdir(git_dir):
        run(["git", "init"], cwd=REPO_DIR)
        # Optionnel : définir la branche par défaut si ce n'est pas main
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
    # rester simple ; échapper uniquement le risque de délimiteur triple tiret
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
    fm_title = sanitize_for_frontmatter(snippet if snippet else f"Note presse-papiers {ts}")

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
    # ajoute aussi l'index pour le versionner
    run(["git", "add", os.path.relpath(INDEX_PATH, REPO_DIR)], cwd=REPO_DIR, check=False)
    run(["git", "commit", "-m", msg], cwd=REPO_DIR)

def git_push_if_enabled():
    if not PUSH:
        return
    # Pousse vers le dépôt distant par défaut si configuré
    try:
        run(["git", "push"], cwd=REPO_DIR, check=False)
    except Exception:
        pass

def main():
    print(f"[clipwatch] dépôt : {REPO_DIR} | long_min : {MIN_LEN} | push : {PUSH}")
    ensure_repo()
    seen_hashes = load_index()
    last_text = None

    while True:
        try:
            txt = pyperclip.paste()
        except Exception as e:
            # Sur certains systèmes, paste peut échouer si le presse-papiers n'est pas disponible
            time.sleep(POLL_SEC)
            continue

        if isinstance(txt, str):
            # Ne traite que le nouveau texte du presse-papiers
            if txt != last_text and len(txt) >= MIN_LEN:
                h = sha1(txt)
                if h not in seen_hashes:
                    path = write_note(txt, h)
                    seen_hashes.add(h)
                    save_index(seen_hashes)

                    first_line = txt.strip().splitlines()[0] if txt.strip() else ""
                    commit_msg = f"Ajouter note presse-papiers : {first_line[:60]}… ({len(txt)} caractères)"
                    try:
                        git_commit(path, commit_msg)
                        git_push_if_enabled()
                        print(f"[clipwatch] sauvegardé : {os.path.relpath(path, REPO_DIR)}")
                    except subprocess.CalledProcessError as e:
                        print("[clipwatch] erreur git :", e.stderr or e.stdout)

            last_text = txt
        time.sleep(POLL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[clipwatch] au revoir.")
```

### Comment l'exécuter

1. Sauvegardez sous `clipwatch.py`.
2. Définissez le chemin de votre dépôt (optionnel) :

   ```bash
   export CLIP_REPO=~/my-notes
   export PUSH=1          # optionnel, active git push si le dépôt distant est configuré
   python3 clipwatch.py
   ```

### Pour l'exécuter au démarrage (exemple macOS launchd)

Créez `~/Library/LaunchAgents/com.zw.clipwatch.plist` :

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

Puis :

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### Remarques et pièges

* Linux : installez `xclip` ou `xsel` pour que `pyperclip` puisse accéder au presse-papiers.
* Cela surveille uniquement le **texte**. Les images/RTF sont ignorées.
* Attention aux secrets — cela capturera tout ce que vous copiez au-delà du seuil. Si vous voulez des exclusions, ajoutez un simple bloqueur (par exemple, ignorer si le texte contient `-----BEGIN PRIVATE KEY-----`, ou si l'application active correspond à une liste noire en interrogeant avec `osascript` sur macOS).
* Si vous voulez étiqueter par application/fenêtre active (par exemple, "depuis Safari"), je peux l'ajouter.

Si vous préférez Rust/Go pour un binaire plus léger et multiplateforme, ou si vous voulez des règles de nommage de fichiers qui correspondent au front-matter Jekyll de votre blog, dites-le et je l'adapterai.