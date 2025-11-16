---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Herunterladen des OpenWebText-Subsets über Hugging Face
translated: true
type: note
---

Der Datensatz, auf den Sie sich beziehen, ist auf Hugging Face unter der Repo-ID `Skylion007/openwebtext` gehostet. Die spezifische Datei `subsets/urlsf_subset00.tar` ist öffentlich zugänglich (keine Authentifizierung erforderlich), sodass Sie sie mit dem Hugging Face CLI-Tool (`huggingface-cli`) herunterladen können. So geht's:

### Voraussetzungen
- Installieren Sie die Hugging Face Hub CLI, falls noch nicht geschehen:
  ```
  pip install huggingface_hub
  ```
- (Optional) Wenn Sie den `huggingface-cli` Befehl als `hf` aliasen (auf einigen Systemen üblich), können Sie diese Kurzform verwenden. Andernfalls verwenden Sie das vollständige `huggingface-cli` Präfix.

### Download-Befehl
Führen Sie dies in Ihrem Terminal aus:
```
huggingface-cli download Skylion007/openwebtext subsets/urlsf_subset00.tar --local-dir ./openwebtext
```
- Dies lädt die Datei nach `./openwebtext/subsets/urlsf_subset00.tar` herunter (erstellt bei Bedarf das `subsets` Unterverzeichnis).
- Die Datei ist ziemlich groß (~1,5 GB unkomprimiert, aber es ist ein Tarball), stellen Sie also sicher, dass Sie genügend Festplattenspeicher und eine stabile Verbindung haben.
- Wenn Sie sie ohne die Repo-Struktur herunterladen möchten (direkt in das aktuelle Verzeichnis), fügen Sie `--repo-type dataset` hinzu (obwohl es hier impliziert ist) oder passen Sie `--local-dir` an.

### Verwendung von Python (Alternative)
Wenn Sie es lieber in Python scripten möchten (z.B. über die `huggingface_hub` Bibliothek):
```python
from huggingface_hub import hf_hub_download

# In das aktuelle Verzeichnis herunterladen
hf_hub_download(
    repo_id="Skylion007/openwebtext",
    filename="subsets/urlsf_subset00.tar",
    local_dir="./openwebtext",  # Optional: gibt das Basisverzeichnis an
    repo_type="dataset"
)
```
Installieren Sie die Bibliothek zuerst: `pip install huggingface_hub`.

### Hinweise
- Dies ist ein Teil des OpenWebText-Datensatzes (ein großer Web-Korpus). Nach dem Download müssen Sie die `.tar`-Datei extrahieren (z.B. mit `tar -xvf subsets/urlsf_subset00.tar`).
- Wenn der Download fehlschlägt (z.B. aufgrund von Netzwerkproblemen), versuchen Sie es erneut oder verwenden Sie `--cache-dir`, um einen benutzerdefinierten Cache-Ort anzugeben.
- Für den vollständigen Datensatz oder andere Teilmengen, besuchen Sie die Repo-Seite: https://huggingface.co/datasets/Skylion007/openwebtext.

Wenn Sie auf Fehler stoßen, teilen Sie die Ausgabe zur Fehlerbehebung mit!