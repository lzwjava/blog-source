---
audio: false
date: 2025-09-06
generated: true
image: false
lang: es
layout: post
title: Guardar Notas del Portapapeles en Git
translated: true
type: note
---

Absolutamente—esto es muy factible con Python + `pyperclip`. A continuación, un pequeño script estilo demonio que sondea el portapapeles, y cada vez que ve texto **nuevo** de más de 500 caracteres, escribe una nota en Markdown en un repositorio Git y la confirma (opcionalmente la envía si está configurado).

### Qué hace

* Sondea el portapapeles cada ~0.7s.
* Ignora contenido que no es texto y duplicados.
* Crea archivos de notas con fecha como `notes/2025/09/2025-09-06_001530_8c9a8f.md`.
* Almacena un pequeño `index.json` de hashes guardados para evitar confirmaciones duplicadas.
* Auto-`git init` si es necesario; confirma; opcionalmente envía si `PUSH=1` (y tu remoto/rama ya están configurados).

### Dependencias

```bash
pip install pyperclip
# Solo Linux: también necesitarás xclip o xsel instalados en el sistema
```

### El script

```python
#!/usr/bin/env python3
import os, time, json, hashlib, subprocess, textwrap, datetime, pathlib, sys
from typing import Optional

try:
    import pyperclip
except Exception as e:
    print("Error: pyperclip no está instalado. Ejecuta `pip install pyperclip`.")
    sys.exit(1)

# ---- Configuración ----
REPO_DIR = os.environ.get("CLIP_REPO", os.path.expanduser("~/clipboard-notes"))
NOTES_DIR = "notes"
MIN_LEN = int(os.environ.get("MIN_LEN", "500"))
POLL_SEC = float(os.environ.get("POLL_SEC", "0.7"))
PUSH = os.environ.get("PUSH", "0") == "1"    # establece PUSH=1 para habilitar `git push`

INDEX_PATH = os.path.join(REPO_DIR, ".clip_index.json")  # almacena hashes de notas guardadas

# ---- Utilidades ----
def run(cmd: list[str], cwd: Optional[str] = None, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)

def ensure_repo():
    os.makedirs(REPO_DIR, exist_ok=True)
    git_dir = os.path.join(REPO_DIR, ".git")
    if not os.path.isdir(git_dir):
        run(["git", "init"], cwd=REPO_DIR)
        # Opcional: establecer rama por defecto si tu git por defecto no es main
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
    # mantenerlo simple; escapar solo el riesgo de valla de triple guión
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
    fm_title = sanitize_for_frontmatter(snippet if snippet else f"Nota del portapapeles {ts}")

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
    # también añadir el índice para mantenerlo versionado
    run(["git", "add", os.path.relpath(INDEX_PATH, REPO_DIR)], cwd=REPO_DIR, check=False)
    run(["git", "commit", "-m", msg], cwd=REPO_DIR)

def git_push_if_enabled():
    if not PUSH:
        return
    # Enviar al upstream por defecto si está configurado
    try:
        run(["git", "push"], cwd=REPO_DIR, check=False)
    except Exception:
        pass

def main():
    print(f"[clipwatch] repositorio: {REPO_DIR} | min_len: {MIN_LEN} | push: {PUSH}")
    ensure_repo()
    seen_hashes = load_index()
    last_text = None

    while True:
        try:
            txt = pyperclip.paste()
        except Exception as e:
            # En algunos sistemas, paste puede lanzar una excepción si el portapapeles no está disponible
            time.sleep(POLL_SEC)
            continue

        if isinstance(txt, str):
            # Solo procesar texto nuevo del portapapeles
            if txt != last_text and len(txt) >= MIN_LEN:
                h = sha1(txt)
                if h not in seen_hashes:
                    path = write_note(txt, h)
                    seen_hashes.add(h)
                    save_index(seen_hashes)

                    first_line = txt.strip().splitlines()[0] if txt.strip() else ""
                    commit_msg = f"Añadir nota del portapapeles: {first_line[:60]}… ({len(txt)} caracteres)"
                    try:
                        git_commit(path, commit_msg)
                        git_push_if_enabled()
                        print(f"[clipwatch] guardado: {os.path.relpath(path, REPO_DIR)}")
                    except subprocess.CalledProcessError as e:
                        print("[clipwatch] error de git:", e.stderr or e.stdout)

            last_text = txt
        time.sleep(POLL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[clipwatch] adiós.")
```

### Cómo ejecutarlo

1. Guárdalo como `clipwatch.py`.
2. Establece la ruta de tu repositorio (opcional):

   ```bash
   export CLIP_REPO=~/my-notes
   export PUSH=1          # opcional, habilita git push si el remoto está configurado
   python3 clipwatch.py
   ```

### Hacer que se ejecute al iniciar sesión (ejemplo macOS launchd)

Crea `~/Library/LaunchAgents/com.zw.clipwatch.plist`:

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

Luego:

```bash
launchctl load ~/Library/LaunchAgents/com.zw.clipwatch.plist
launchctl start com.zw.clipwatch
```

### Notas y advertencias

* Linux: instala `xclip` o `xsel` para que `pyperclip` pueda acceder al portapapeles.
* Esto vigila **solo texto**. Se ignoran imágenes/RTF.
* Ten cuidado con los secretos—esto capturará cualquier cosa que copies que supere el umbral. Si quieres exclusiones, añade un bloqueador simple (por ejemplo, omitir si el texto contiene `-----BEGIN PRIVATE KEY-----`, o si la aplicación activa coincide con una lista de denegación consultando con `osascript` en macOS).
* Si quieres etiquetar por aplicación/ventana activa (por ejemplo, "desde Safari"), puedo añadirlo.

Si prefieres Rust/Go para un binario más ligero y multiplataforma, o quieres reglas de nombres de archivo que coincidan con el front-matter de Jekyll de tu blog, dime y lo adaptaré.