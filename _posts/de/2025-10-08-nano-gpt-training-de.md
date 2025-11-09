---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Training benutzerdefinierter Datensätze mit nanoGPT
translated: true
type: note
---

### Vorbereitung und Training eines benutzerdefinierten Textdatensatzes mit nanoGPT

nanoGPT ist für einfaches Training mit Textdaten konzipiert, einschließlich benutzerdefinierter Datensätze. Der Prozess umfasst die Vorbereitung Ihres Textes in binäre Token-Dateien, die Konfiguration der Trainingsparameter und das Ausführen des Trainingsskripts. Im Folgenden skizziere ich die Schritte basierend auf den Beispielen aus dem Repository (z. B. Shakespeare oder OpenWebText). Sie benötigen Python 3.8+ und eine GPU für effizientes Training (CPU funktioniert, ist aber langsamer).

#### 1. Abhängigkeiten installieren
Richten Sie zunächst die Umgebung ein:
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch`: Für PyTorch (mit CUDA installieren, falls GPU verwendet wird: z. B. `pip install torch --index-url https://download.pytorch.org/whl/cu118`).
- Die anderen kümmern sich um Tokenisierung, Datenladung und Protokollierung.

#### 2. Bereiten Sie Ihren benutzerdefinierten Datensatz vor
nanoGPT erwartet Ihre Daten als binäre Dateien (`train.bin` und `val.bin`), die tokenisierte Ganzzahlen enthalten. Sie müssen ein einfaches Vorbereitungsskript schreiben, um Ihren Rohtext zu verarbeiten.

- **Platzieren Sie Ihre Textdatei**: Legen Sie Ihren Rohtext (z. B. `input.txt`) in einem neuen Ordner unter `data/` ab, z. B. `data/mein_datensatz/`.
  
- **Erstellen Sie ein Vorbereitungsskript**: Kopieren und passen Sie ein Beispiel aus dem Repo an (z. B. `data/shakespeare_char/prepare.py` für Character-Level oder `data/openwebtext/prepare.py` für GPT-2 BPE Token-Level).
  
  **Beispiel für Character-Level-Tokenisierung** (einfach für kleine Datensätze; behandelt jedes Zeichen als Token):
  ```python
  # Speichern als data/mein_datensatz/prepare.py
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # Laden Sie Ihren Text (ersetzen Sie durch Ihren Dateipfad)
  with open('data/mein_datensatz/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # Als Zeichen kodieren
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # Den gesamten Text tokenisieren
  data = torch.tensor(encode(text), dtype=torch.long)

  # In Train/Val aufteilen (90/10)
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # Als .bin-Dateien speichern
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/mein_datensatz/train.bin')
  val_data.tofile('data/mein_datensatz/val.bin')

  # Statistiken ausgeben
  print(f"Länge des Datensatzes in Zeichen: {len(data)}")
  print(f"Vocab-Größe: {vocab_size}")
  ```
  Führen Sie es aus:
  ```
  python data/mein_datensatz/prepare.py
  ```
  Dies erstellt `train.bin` und `val.bin`.

- **Für GPT-2 BPE-Tokenisierung** (besser für größere Datensätze; verwendet Subwords):
  Passen Sie `data/openwebtext/prepare.py` an. Sie müssen `tiktoken` installieren (bereits in den Abhängigkeiten enthalten) und Ihren Text ähnlich verarbeiten, aber `tiktoken.get_encoding("gpt2").encode()` anstelle der Zeichenkodierung verwenden. Teilen Sie Ihren Text in Train/Val-Blöcke auf (z. B. 90/10) und speichern Sie sie als NumPy-Arrays in `.bin`.

- **Tipps**:
  - Halten Sie Ihren Datensatz sauber (z. B. entfernen Sie ggf. Sonderzeichen).
  - Für sehr große Dateien: Verarbeiten Sie in Blöcken, um Speicherprobleme zu vermeiden.
  - Vocab-Größe: ~65 für Chars (Shakespeare); ~50k für BPE.

#### 3. Training konfigurieren
Erstellen Sie eine Konfigurationsdatei, indem Sie ein Beispiel kopieren (z. B. `config/train_shakespeare_char.py`) nach `config/train_mein_datensatz.py` und bearbeiten Sie es.

Wichtige Parameter zum Anpassen:
```python
# Beispiel-Konfigurationsausschnitt
out_dir = 'out-mein_datensatz'  # Ausgabeordner für Checkpoints
dataset = 'mein_datensatz'      # Entspricht Ihrem Datenordner-Namen
batch_size = 64                 # Anpassen basierend auf GPU-Speicher (z. B. 12 für kleine GPU)
block_size = 256                # Kontextlänge (Tokens pro Beispiel)
n_layer = 6                     # Transformer-Layers
n_head = 6                      # Attention-Heads
n_embd = 384                    # Embedding-Dimension
max_iters = 5000                # Trainingsschritte
lr = 6e-4                       # Lernrate
dropout = 0.2                   # Dropout-Rate
init_from = 'scratch'           # 'scratch' für neues Modell; 'gpt2' zum Laden eines vortrainierten
```
- Für Finetuning (Start von vortrainiertem GPT-2): Setzen Sie `init_from = 'gpt2'` (oder 'gpt2-medium').
- Für Apple Silicon: Fügen Sie `device = 'mps'` hinzu.
- Checkpoints werden standardmäßig alle 500 Iterationen gespeichert.

#### 4. Training ausführen
Trainieren Sie von Grund auf oder führen Sie Finetuning durch:
```
python train.py config/train_mein_datensatz.py
```
- Für Multi-GPU (z. B. 8 GPUs): `torchrun --standalone --nproc_per_node=8 train.py config/train_mein_datensatz.py`.
- Überwachen Sie mit WandB (protokolliert Losses, Samples; in Konfiguration mit `wandb_log = True` aktivieren).
- Trainingszeit: Minuten für kleine Modelle auf GPU; Stunden/Tage für größere.

#### 5. Beispiele generieren (Modell testen)
Nach dem Training können Sie Text generieren:
```
python sample.py --out_dir=out-mein_datensatz --start="Ihr Prompt hier"
```
Dies lädt den neuesten Checkpoint und generiert Text.

#### Häufige Probleme
- **Speicherfehler**: Reduzieren Sie `batch_size` oder `block_size`.
- **Keine GPU**: Fügen Sie `--device=cpu --compile=False` zu den Befehlen hinzu.
- **Große Datensätze**: Verwenden Sie verteiltes Training für Skalierung.

Weitere Details finden Sie in der README des Repos und den Daten/Konfigurationsbeispielen.

[nanoGPT GitHub](https://github.com/karpathy/nanoGPT)