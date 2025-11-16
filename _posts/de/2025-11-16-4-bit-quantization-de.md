---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: 4-Bit-Quantisierung für effiziente LLMs
translated: true
type: note
---

### Was ist 4-Bit-Quantisierung (im Kontext von QLoRA oder GPTQ)?

4-Bit-Quantisierung ist eine Technik, um den Speicherbedarf von Large Language Models (LLMs) drastisch zu reduzieren, indem jeder Gewichtungswert mit nur 4 Bit anstelle der üblichen 16-Bit (FP16/BF16) oder 32-Bit (FP32) Genauigkeit gespeichert wird.

Normale (Full-Precision) Modelle:
- FP32: 4 Bytes pro Parameter → 7B Modell ≈ 28 GB
- FP16/BF16: 2 Bytes pro Parameter → 7B Modell ≈ 14 GB

4-Bit-Quantisierung:
- ~0,5 Bytes pro Parameter → 7B Modell ≈ 3,5–4 GB (etwa 1/4 bis 1/8 der ursprünglichen Größe, je nach Methode)

Es gibt zwei gängige 4-Bit-Ansätze, die man heute häufig sieht:

| Methode | Vollständiger Name                | Hauptarbeit / Jahr | Typischer Anwendungsfall          | Hauptmerkmale                                                                          |
|---------|------------------------------------|--------------------|-----------------------------------|----------------------------------------------------------------------------------------|
| GPTQ    | GPTQ                               | 2023               | Post-Training-Quantisierung (nur Inferenz) | One-Shot, sehr genau, kein Retraining nötig. Rundet Gewichte nach dem Training auf 4-Bit. |
| QLoRA   | Quantized Low-Rank Adaptation     | 2023 (Jun)         | Effizientes Fine-Tuning / Instruction Tuning | Kombiniert 4-Bit-Speicher + LoRA-Adapter + Paged Optimizers. Ermöglicht Fine-Tuning von 65B+ Modellen auf einer einzelnen 24–48 GB GPU. |

#### QLoRA im Detail (die Methode, die meist gemeint ist, wenn man „4-Bit QLoRA“ sagt)
QLoRA macht vier clevere Dinge gleichzeitig:

1. 4-Bit NormalFloat (NF4) Quantisierung  
   - Ein spezieller 4-Bit-Datentyp, optimiert für normalverteilte Gewichte (die meisten LLM-Gewichte sind nach dem Training ≈ Gaußverteilt).
   - Besser als einfaches INT4; theoretisch optimal für normalverteilte Daten.

2. Doppelte Quantisierung  
   - Sogar die Quantisierungskonstanten (Skalierungsfaktoren) werden von FP16 → 8-Bit quantisiert, spart einige weitere MB.

3. Paged Optimizers  
   - Optimizer-Zustände (AdamW Moments) werden im CPU-RAM gespeichert und per NVIDIA Unified Memory zur GPU gepaget. Verhindert OOM während des Trainings.

4. LoRA-Adapter  
   - Es werden nur kleine Low-Rank-Matrizen trainiert (r=64 oder weniger), während das Basis-4-Bit-Modell eingefroren bleibt.

Ergebnis: Man kann ein 65B Llama/Mistral-Modell vollständig auf einer 48 GB RTX A6000 fine-tunen oder sogar ein 70B-Modell auf einer einzelnen 80 GB A100 mit QLoRA, während normales Full Fine-Tuning 8×A100s oder mehr benötigen würde.

#### GPTQ (die auf Inferenz fokussierte Methode)
- Wird nach Abschluss des Trainings durchgeführt.
- Nutzt Informationen zweiter Ordnung (Hessische Matrix), um den Rundungsfehler bei der Komprimierung der Gewichte auf 4-Bit zu minimieren.
- Extrem genau – normalerweise <0,1 Perplexity-Verschlechterung im Vergleich zu FP16.
- Beliebt in Tools wie AutoGPTQ, ExLlama, vLLM und llama.cpp (GGUF hat auch GPTQ-ähnliche Modi).

### Gradient Checkpointing (auch „Activation Checkpointing“ genannt)

Eine völlig separate, speichersparende Technik, die während des Trainings verwendet wird.

So funktioniert es:
- Normalerweise muss die Backpropagation alle Zwischenaktivierungen aus dem Forward Pass speichern → der Speicherbedarf wächst linear mit Modelltiefe/Batch-Größe/Sequenzlänge.
- Gradient Checkpointing tauscht Rechenleistung gegen Speicher:
  - Während des Forward Pass werden nur wenige „Checkpoint“-Aktivierungen gespeichert.
  - Während des Backward Pass werden die fehlenden Aktivierungen on-the-fly neu berechnet.

Typische Speichereinsparung: 50–80 % des Aktivierungsspeichers, auf Kosten von ~20–30 % langsamerer Trainingsgeschwindigkeit.

Es wird fast immer zusammen mit QLoRA oder jedem Fine-Tuning großer Modelle verwendet, denn selbst mit 4-Bit-Gewichten sprengen die Aktivierungen immer noch den GPU-Speicher.

### TL;DR Zusammenfassung

„4-Bit-Quant (QLoRA-Stil oder GPTQ) + Gradient Checkpointing“ ist das moderne Rezept für:

- Das Ausführen oder Fine-Tunen riesiger Modelle (33B, 70B, 405B) auf Consumer- oder Single-Enterprise-GPUs.
- QLoRA-artige 4-Bit → Fine-Tuning mit sehr geringem GPU-Speicherbedarf.
- GPTQ-artige 4-Bit → Schnelle Inferenz mit sehr geringem GPU-Speicherbedarf.
- Gradient Checkpointing → Macht den eigentlichen Backward Pass bei langen Sequenzen ohne OOM möglich.

Zusammen sind sie der Grund, warum man heute Leute sieht, die Llama-3-70B auf einer einzelnen 3090/4090 fine-tunen.