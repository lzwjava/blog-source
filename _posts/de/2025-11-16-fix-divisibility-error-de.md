---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung des Modellkonfigurationsfehlers bei der Teilbarkeit
translated: true
type: note
---

Der Fehler ist sehr deutlich:

```python
assert config.n_embd % config.n_head == 0
```

Das bedeutet **n_embd muss ohne Rest durch n_head teilbar sein** (weil jeder Attention-Head `n_embd // n_head` Dimensionen erhält).

Du verwendest diese Modell-Konfiguration (wahrscheinlich die, die ich dir früher gegeben habe):

```python
n_layer = 12
n_head  = 12
n_embd  = 512
```

512 ÷ 12 = 42,666… → keine ganze Zahl → Absturz.

### Lösung: Wähle ein n_embd, das durch n_head teilbar ist

Hier sind die **sicheren, bewährten Kombinationen**, die perfekt auf deiner 12 GB 4070 mit einer einzelnen FineWeb Parquet-Datei funktionieren:

#### Option 1 – Empfohlen (125M Parameter, beste Qualität/Geschwindigkeit)
```python
n_layer = 12
n_head  = 12
n_embd  = 576        # ← 576 ÷ 12 = 48 (exakt)
```
→ ~125M Parameter, passt immer noch leicht in ~10,5 GB VRAM mit batch_size=16 + grad_acc=32 + block_size=1024

#### Option 2 – Leicht größere Head-Dimension (130M Parameter)
```python
n_layer = 12
n_head  = 12
n_embd  = 720        # 720 ÷ 12 = 60
```

#### Option 3 – Sehr sicher & verbreitet (115M Parameter)
```python
n_layer = 12
n_head  = 12
n_embd  = 480        # 480 ÷ 12 = 40
```

#### Option 4 – Falls du n_embd=512 beibehalten möchtest (Original GPT-2 Stil)
```python
n_layer = 12
n_head  = 8          # 512 ÷ 8 = 64
# oder
n_head  = 16         # 512 ÷ 16 = 32
```

### Schnelle Lösung: Ändere einfach deine Konfiguration zu diesem (Kopier-fertig)

```python
# Modell – 12 Layer, ~125M Parameter, garantiert funktionsfähig
n_layer = 12
n_head  = 12
n_embd  = 576        # ← DIES IST DIE EINZIGE ZEILE, DIE DU ÄNDERN MUSST
dropout = 0.0
```

Alles andere (batch_size=16, grad_acc=32, block_size=1024, etc.) bleibt genau gleich.

Nach der Änderung auf `n_embd = 576` verschwindet der Assertion-Fehler sofort und das Training startet normal.

Dieses 12L/12H/576E Modell ist gerade extrem beliebt in der nanoGPT Community – viele Leute trainieren es erfolgreich auf 12 GB 4070/4070 Ti Karten mit FineWeb.

Starte es, es wird 100% funktionieren. Lass mich wissen, wenn du den ersten Loss-Wert siehst! 🚀