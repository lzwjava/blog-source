---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Git Force Push durch Branch-Löschung
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
git_force_push.py

Dieses Skript führt einen "Force Push" durch, indem es zuerst den Remote-Branch löscht
und dann den lokalen Branch überträgt. Dies funktioniert, wenn das Repository Branch-Löschungen
erlaubt, aber keine Force Pushes.

Verwendung: python git_force_push.py <remote> <branch>
Beispiel: python git_force_push.py origin main

Hinweis: Dies setzt voraus, dass Sie ausreichende Berechtigungen haben und dass Löschungen erlaubt sind.
Seien Sie vorsichtig, da das Löschen eines Branches Commits verlieren kann.
"""

import subprocess
import sys

def run_command(command):
    """Führt einen Shell-Befehl aus und gibt dessen Ausgabe zurück."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen des Befehls '{command}': {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Verwendung: python git_force_push.py <remote> <branch>")
        sys.exit(1)

    remote = sys.argv[1]
    branch = sys.argv[2]

    # Lösche den Remote-Branch
    delete_cmd = f"git push {remote} :{branch}"
    print(f"Lösche Remote-Branch: {delete_cmd}")
    run_command(delete_cmd)

    # Übertrage den lokalen Branch
    push_cmd = f"git push {remote} {branch}"
    print(f"Übertrage lokalen Branch: {push_cmd}")
    run_command(push_cmd)

    print("Force Push erfolgreich abgeschlossen.")
```

### Funktionsweise
- **Löschschritt**: Führt `git push origin :main` aus, um den Remote-Branch zu löschen (wie in Ihrem Repository erlaubt).
- **Push-Schritt**: Führt `git push origin main` aus, um den lokalen Branch zu übertragen und ihn auf dem Remote neu zu erstellen.
- Dies erreicht effektiv einen Force Push, indem der Remote-Verlauf verworfen und durch den lokalen Verlauf ersetzt wird.
- **Sicherheits-/Verwendungshinweise**: Testen Sie zuerst in einem nicht-kritischen Repository. Dies erfordert eine korrekte Git-Einrichtung und Berechtigungen. Wenn das Repository zusätzliche Schutzmaßnahmen hat (z.B. via Hooks), könnte es fehlschlagen. Keine Gewährleistung; Git-Operationen können zerstörerisch sein.