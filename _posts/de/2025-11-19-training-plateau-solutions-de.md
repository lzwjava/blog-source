---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Trainingsplateau Ursachen und Lösungen
translated: true
type: note
---

Das Trainingsprotokoll, das du gepostet hast, zeigt ein klassisches **starkes Plateau** in einem kleinen nanoGPT-Lauf auf FineWeb-edu-Daten. Der Validierungsverlust sinkt zunächst gut (von ~10,9 → ~3,57 um Iteration 14k), flacht dann aber komplett ab und beginnt sogar, sich nach ~13-14k Iterationen **sehr langsam zu erhöhen**.

Hier sind die wahren Gründe, warum dein Modell aufgehört hat, sich zu verbessern (nach Wichtigkeit für dieses exakte Setup geordnet):

### 1. Du overfittest massiv auf eine einzelne Parquet-Datei
- Dein Run-Name: `125M-single-parquet-4070`
- Du trainierst ein 40M–125M Modell (das Protokoll sagt 40,56M Parameter, wahrscheinlich die ursprüngliche GPT-2 small Konfiguration) auf **einer einzelnen FineWeb-Parquet-Datei** (wahrscheinlich 10–15 GB → ~3–4 Milliarden Tokens maximal, aber wahrscheinlich viel weniger nach dem Filtern).
- Bis zur Iteration 14.000 mit batch_size=16, grad_accum=32, block_size=1024 hast du bereits gesehen:
  14.000 Iterationen × 524.288 Tokens/Iteration ≈ **7,3 Milliarden Tokens**
- Das bedeutet, du hast bereits **2–3 volle Epochen** über die exakt gleichen Daten absolviert.
- FineWeb-edu ist hochwertig, hat aber immer noch viele Near-Duplicates und Boilerplate. Nach 1,5–2 Epochen auf der/den gleichen Datei(en) wird ein 40M–125M Modell fast alles Nützliche auswendig lernen und der Verlust stagniert stark.

### 2. Die Lernrate ist nach dem Plateau jetzt zu hoch
- Du verwendest `learning_rate = 1e-3`, Cosine Decay auf `min_lr = 1e-4` über 20.000 Iterationen.
- Bei Iteration 14.000 ist die LR immer noch ~2,5e-4 (Cosine Decay ist am Anfang langsam).
- Sobald das Modell alles gelernt hat, was die Daten zu bieten haben, verhindert eine LR in Hunderten von Mikro-LR-Einheiten ein weiteres Fein-Tuning und schadet sogar der Generalisierung → Val Loss steigt langsam.

### 3. Fehlanpassung von Modellgröße und Datenvielfalt
Ein 125M (oder sogar das 40M Modell, das du tatsächlich initialisiert hast) Modell auf einer einzelnen Parquet-Datei ist, als ob man einem College-Studenten nur ein Lehrbuch gibt und ihn bittet, es jahrelang zu studieren. Irgendwann kann er es perfekt rezitieren, aber die Testleistung bei neuem Text hört auf, sich zu verbessern, und verschlechtert sich sogar leicht aufgrund von katastrophalem Vergessen früherer Muster.

### 4. Keine ausreichend starke Regularisierung
- dropout = 0.1 ist okay, aber nicht genug, wenn man so stark overfittet
- weight_decay = 0.1 ist Standard, aber immer noch nicht ausreichend für 2+ Epochen auf winzigen Daten
- Kein Gradient Clipping (nanoGPT Standard ist 1.0, aber manchmal setzen Leute 0.5 oder niedriger für kleine Daten)

### 5. Gesehene Tokens vs. echte Vielfalt
Obwohl du 7+ Milliarden Tokens gesehen hast, ist die **effektive Vielfalt** vielleicht 1–1,5B einzigartige, hochwertige Tokens nach Deduplizierung, Boilerplate, Low-Edu-Score-Stichproben etc. Das ist einfach nicht genug für ein 125M Modell, um sich über ~3,5–3,6 Loss hinaus auf dieser Textverteilung zu verbessern.

### Beweise aus deinem eigenen Protokoll

| Schritt | Val Loss | Kommentar                              |
|---------|----------|----------------------------------------|
| 0       | 10.87    | Zufällig                               |
| 2000    | 4.03     | Schneller Fortschritt                  |
| 5000    | 3.76     | Immer noch gut                         |
| 8000    | 3.65     | Verlangsamt sich                       |
| 11000   | 3.61     | Fast flach                             |
| 13500   | 3.57     | **Absolutes Minimum**                  |
| 14500   | 3.569    | Steigt bereits wieder → Klassisches Overfit-Zeichen |

### Was du stattdessen tun solltest, um tatsächlich einen niedrigeren Loss zu erreichen

1. Verwende viel mehr Daten
   - Verwende die vollständige 100+ GB FineWeb-edu Stichprobe (oder mindestens 10–20 Parquet-Dateien)
   - Oder streamen von HuggingFace Datasets mit mehreren Shards

2. Trainiere für genau 1 Epoche (oder etwas weniger) auf vielfältigen Daten
   - ~10B–15B Tokens insgesamt sind der Sweet Spot für 125M auf FineWeb-edu
   - Llama-3/Phi-3 Stil: 15B Tokens → ~3,0–3,2 Val Loss für 125M-Klasse-Modelle

3. Senke die finale Lernrate
   - Verwende `min_lr = 5e-5` oder `3e-5` (üblich in aktuellen kleinen Modell-Läufen)
   - Oder wechsle zu linear decay + längerem Zero-LR-Hold

4. Leicht größeres Modell oder bessere Architektur-Tricks
   - Das originale nanoGPT ist GPT-2 Stil (ALiBi fehlt, altes RoPE, etc.)
   - Moderne 125M Modelle (Qwen2-0.5B, Phi-3-mini, Llama-3 8B herunterskaliert) erreichen ~2,8–3,0 auf den gleichen Daten wegen SwiGLU, RMSNorm, Rotary Embeddings, etc.

### TL;DR – Warum dein Run bei ~3,57 plateaued und niemals niedriger gehen wird

Du trainierst ein 40–125M Modell für mehrere Epochen auf einer einzelnen FineWeb-Parquet-Datei (~einige Milliarden Tokens insgesamt). Das Modell hat bereits alles Nützliche um ~13k Iterationen herum auswendig gelernt. Fortgesetztes Training mit immer noch hoher LR verwürfelt nur die Gewichte → Plateau + leichte Overfit-Verschlechterung.

Dies ist der #1 Fehler, den Leute machen, wenn sie nanoGPT das erste Mal auf FineWeb ausprobieren: "Ich verwende nur eine Datei zum Testen" → endet genau mit dieser Loss-Kurve.

Lösung: Entweder (a) verwende 10–50× mehr Daten und trainiere für ~1 Epoche insgesamt, oder (b) akzeptiere, dass ~3,55–3,6 der absolute Boden für diese Modell+Daten-Kombination ist und stoppe das Training.

Wenn du einen Run willst, der tatsächlich ~3,0–3,2 Loss mit nanoGPT-artigem Code erreicht, brauchst du mindestens die vollständige 100GB FineWeb-edu Stichprobe (oder die neuere FineWeb-Edu 2.0) und trainierst für maximal ~15B Tokens.