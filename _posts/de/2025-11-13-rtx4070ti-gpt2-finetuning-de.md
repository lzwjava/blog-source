---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: RTX 4070 Ti GPT-2 Feinabstimmungsleitfaden
translated: true
type: note
---

## Einrichten Ihrer Umgebung

Stellen Sie vor dem Training sicher, dass Ihre NVIDIA RTX 4070 Ti korrekt eingerichtet ist. Diese GPU verfügt über 12 GB VRAM, was mehr als ausreichend für GPT-2 Small (124M Parameter) während des Fine-Tunings ist. Das Training von Grund auf auf einem massiven Datensatz wie OpenWebText ist auf einer einzelnen Consumer-GPU aufgrund von Zeit- und Rechenanforderungen unpraktisch – es würde Wochen oder Monate dauern. Konzentrieren Sie sich stattdessen darauf, das vortrainierte Modell für bestimmte Aufgaben auf Ihrem eigenen Datensatz feinzutrainieren.

### 1. NVIDIA-Treiber und CUDA installieren
- Laden Sie die neuesten NVIDIA-Treiber für Ihre RTX 4070 Ti von der offiziellen NVIDIA-Website herunter und installieren Sie sie. Stellen Sie sicher, dass es Version 535 oder höher für volle Kompatibilität ist.
- Installieren Sie das CUDA Toolkit. Die RTX 4070 Ti (Compute Capability 8.9) unterstützt CUDA 12.x. Empfohlen wird CUDA 12.4:
  - Laden Sie es aus dem NVIDIA CUDA Toolkit-Archiv herunter.
  - Befolgen Sie den Installationsleitfaden für Ihr Betriebssystem (Windows/Linux).
- Installieren Sie cuDNN (CUDA Deep Neural Network library), das Ihrer CUDA-Version entspricht (z.B. cuDNN 8.9 für CUDA 12.4).
- Überprüfen Sie die Installation:
  ```
  nvidia-smi  # Sollte Ihre GPU und CUDA-Version anzeigen
  nvcc --version  # Bestätigt die CUDA-Installation
  ```

### 2. Python-Umgebung einrichten
- Verwenden Sie Python 3.10 oder 3.11. Installieren Sie es via Anaconda oder Miniconda für eine einfachere Verwaltung.
- Erstellen Sie eine virtuelle Umgebung:
  ```
  conda create -n gpt2-train python=3.10
  conda activate gpt2-train
  ```

### 3. Erforderliche Bibliotheken installieren
- Installieren Sie PyTorch mit CUDA-Unterstützung. Für CUDA 12.4:
  ```
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  ```
  Überprüfung:
  ```
  python -c "import torch; print(torch.cuda.is_available())"  # Sollte True zurückgeben
  ```
- Installieren Sie Hugging Face Bibliotheken und andere:
  ```
  pip install transformers datasets accelerate sentencepiece pandas tqdm
  ```

## Vorbereiten Ihres Datensatzes
- Wählen Sie einen Textdatensatz aus oder bereiten Sie ihn vor (z.B. eine .txt-Datei mit einem Beispiel pro Zeile oder eine CSV mit einer 'text'-Spalte).
- Verwenden Sie beispielsweise einen öffentlichen Datensatz von Hugging Face Datasets:
  ```python
  from datasets import load_dataset
  dataset = load_dataset("bookcorpus")  # Oder Ihren benutzerdefinierten Datensatz: load_dataset("text", data_files="your_data.txt")
  ```
- Bei Bedarf in Trainings-/Testdaten aufteilen:
  ```python
  dataset = dataset["train"].train_test_split(test_size=0.1)
  ```

## Fine-Tuning von GPT-2 Small
Verwenden Sie die Hugging Face Transformers-Bibliothek für Einfachheit. Hier ist ein vollständiges Skript für kausale Sprachmodellierung (Vorhersage des nächsten Tokens).

### Skript-Beispiel
Speichern Sie dies als `train_gpt2.py` und führen Sie es mit `python train_gpt2.py` aus.

```python
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# Tokenizer und Modell laden (GPT-2 Small)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # Padding-Token setzen
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Datensatz laden und vorverarbeiten (ersetzen Sie dies mit Ihrem Datensatz)
dataset = load_dataset("bookcorpus")
dataset = dataset["train"].train_test_split(test_size=0.1)

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512, padding="max_length")

tokenized_dataset = dataset.map(preprocess, batched=True, remove_columns=["text"])

# Data Collator für Sprachmodellierung
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Trainingsargumente (für einzelne GPU optimiert)
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=4,  # An VRAM anpassen; starten Sie niedrig, um OOM zu vermeiden
    per_device_eval_batch_size=4,
    num_train_epochs=3,  # Nach Bedarf anpassen
    weight_decay=0.01,
    fp16=True,  # Gemischte Präzision für schnelleres Training und weniger VRAM
    gradient_accumulation_steps=4,  # Effektive Batch-Größe = batch_size * accumulation_steps
    save_steps=1000,
    logging_steps=500,
    report_to="none",  # Oder "wandb" für Tracking
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    data_collator=data_collator,
)

# Trainieren
trainer.train()

# Modell speichern
trainer.save_model("./gpt2-finetuned")
```

### Ausführung des Trainings
- Überwachen Sie die GPU-Nutzung mit `nvidia-smi` in einem anderen Terminal.
- Wenn Sie Out-of-Memory (OOM) Fehler erhalten:
  - Reduzieren Sie `per_device_train_batch_size` auf 2 oder 1.
  - Erhöhen Sie `gradient_accumulation_steps`, um die effektive Batch-Größe beizubehalten.
  - Verwenden Sie eine kleinere max_length (z.B. 256 statt 512).
- Trainingszeit: Auf einer 4070 Ti, für einen mittelgroßen Datensatz (z.B. 100k Beispiele), erwarten Sie 1-5 Stunden pro Epoche, abhängig von der Batch-Größe.

## Evaluation und Inferenz
Nach dem Training:
```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-finetuned", device=0)  # device=0 für GPU
output = generator("Ihr Prompt hier", max_length=50, num_return_sequences=1)
print(output)
```

- Evaluieren Sie die Perplexität (niedriger ist besser):
  ```python
  import math
  eval_results = trainer.evaluate()
  perplexity = math.exp(eval_results["eval_loss"])
  print(f"Perplexity: {perplexity}")
  ```

## Tipps und Problembehandlung
- Verwenden Sie gemischte Präzision (`fp16=True`), um VRAM zu sparen und das Training zu beschleunigen.
- Wenn Sie von Grund auf trainieren (nicht empfohlen): Implementieren Sie eine benutzerdefinierte Transformer-Architektur (z.B. via NanoGPT oder ähnliche Repos) und verwenden Sie einen riesigen Datensatz, aber erwarten Sie sehr lange Laufzeiten.
- Für größere Datensätze verwenden Sie verteiltes Training, wenn Sie mehrere GPUs haben, aber das geht über eine einzelne 4070 Ti hinaus.
- Häufige Probleme: Wenn PyTorch die GPU nicht erkennt, installieren Sie die Treiber/CUDA neu. Stellen Sie sicher, dass keine anderen Prozesse die GPU verwenden.

## Referenzen
- [Fine-Tuning GPT-2: A Practical Guide](https://mr-amit.medium.com/fine-tuning-gpt-2-a-practical-guide-2805b4af738b)
- [Training GPT-2 From Scratch: A Step-by-Step Guide](https://youssefh.substack.com/p/training-gpt-2-from-scratch-a-step)
- [How To Train Your Own GenAI Model](https://developer.squareup.com/blog/how-to-train-your-own-genai-model/)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [RTX 4070 CUDA version](https://www.reddit.com/r/pytorch/comments/1kwb5fh/rtx_4070_cuda_version/)
- [Geforce RTX 4070 Ti Super CUDA support for Deep Learning](https://forums.developer.nvidia.com/t/geforce-rtx-4070-ti-super-cuda-support-for-deep-learning/282154)
- [CUDA compatibility with RTX 4070](https://forums.developer.nvidia.com/t/cuda-compatibility-with-rtx-4070/287989)