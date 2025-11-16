---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Herunterladen eines Teils von OpenWebText
translated: true
type: note
---

Ah, verstanden — du möchtest bei der **Hugging Face CLI** bleiben, aber trotzdem nur einen kleinen Teil herunterladen. Das Problem ist: Die CLI ist dafür ausgelegt, **komplette Dateien** herunterzuladen, keine Teilstücke. OpenWebText ist in 21 `.tar`-Teildateien aufgeteilt; wenn du die CLI verwendest, lädt sie ganze Tarballs herunter, du kannst also nicht exakt „1 %“ erhalten, ohne große Teile herunterzuladen.

Hier ist ein praktischer Ansatz:

---

### 1. Lade nur einen Teil der Dateien herunter

Anstatt aller 21 Dateien, wähle einfach ein paar Tarballs aus:

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* Jeder Tarball ist ~625 MB groß. Wenn du 1–2 davon herunterlädst, entspricht das ungefähr 1–2 % des Datensatzes.
* Du kannst anpassen, welche Teilmengen du auswählst; HF erzwingt keine sequenzielle Reihenfolge.

---

### 2. Extrahiere nur das, was du benötigst

Nach dem Download:

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

Dann kannst du nur einige Dokumente aus diesen Teilmengen verarbeiten.

---

### 3. Optional: Kombiniere mit HF Transfer

Um CLI-Downloads zu beschleunigen:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

Dann versuche die CLI-Befehle erneut — die Downloads werden viel schneller sein.

---

Falls du möchtest, kann ich einen **kleinen Befehlssnippet erstellen, der automatisch ~1 % von OpenWebText ausschließlich mit der CLI auswählt**, damit du nicht manuell Tarballs auswählen musst. Soll ich das tun?