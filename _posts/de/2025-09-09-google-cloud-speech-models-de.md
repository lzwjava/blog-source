---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Vergleich von Google Cloud Speech-to-Text-Modellen
translated: true
type: note
---

Hier ist eine übersichtliche Aufschlüsselung der Unterschiede zwischen den verschiedenen Speech-to-Text-Modellen in Google Clouds API V2 – nach Modellfamilien und Anwendungsfällen gegliedert, ohne Tabellen, um die Lesbarkeit zu erhalten:

---

## Chirp-Familie (Universal Speech Models - USM)

### **`chirp`**

* **Beschreibung**: Googles ursprüngliches Universal Speech Model (USM), das vielfältige mehrsprachige Transkription in nicht-streamenden Kontexten unterstützt.([Google Cloud][1])
* **Verwendung**: Funktioniert mit synchronen (`Recognize`) und Batch-Methoden (`BatchRecognize`); unterstützt **kein** Streaming.([Google Cloud][1])
* **Einschränkungen**:

  * Keine Streaming-Unterstützung
  * Fehlende Konfidenzscores, Diarisierung, Adaptation, Forced Normalization und Wort-level Konfidenz([Google Cloud][1])

### **`chirp_2`**

* **Beschreibung**: Universal Speech Model der nächsten Generation, genauer und effizienter als das Original, mit Unterstützung für Streaming, synchrone und Batch-Verarbeitung. Bietet mehrsprachige Transkription und Übersetzung sowie Modell-Adaptation.([Google Cloud][2], [Medium][3])

### **`chirp_3`**

* **Beschreibung**: Die neueste Generation mit weiteren Verbesserungen bei Genauigkeit und Geschwindigkeit. Unterstützt Streaming, synchrone und Batch-Erkennung, sowie Sprecher-Diarisierung und automatische Spracherkennung.([Google Cloud][4])
* **Funktionsunterstützung**:

  * Streaming (`StreamingRecognize`), synchrone (`Recognize`) und Batch-Verarbeitung (`BatchRecognize`) werden alle unterstützt([Google Cloud][4])
  * Unterstützt Diarisierung und Spracherkennung([Google Cloud][4])
  * Unterstützt keine Wort-level Zeitstempel oder Adaptation([Google Cloud][4])

---

## Legacy-/Allzweck-Modelle

Dies sind Modelle mit älterer Architektur, die hauptsächlich aus Gründen der Abwärtskompatibilität beibehalten werden:

* **`long`**: Geeignet für Long-Form-Inhalte wie Medien oder spontane Gespräche.([Google Cloud][2])
* **`short`**: Optimiert für sehr kurze Äußerungen (einige Sekunden) – ideal für Befehle.([Google Cloud][2])
* **`telephony` / `telephony_short`**: Zugeschnitten für Telefonie-Audio (typischerweise 8 kHz). Die "Short"-Variante verarbeitet kurze oder Ein-Wort-Äußerungen.([Google Cloud][2])
* **Medizinische Modelle**:

  * `medical_conversation`: Für Dialoge zwischen medizinischem Personal und Patient, mit Sprechertrennung.
  * `medical_dictation`: Für Diktate eines einzelnen Sprechers.([Google Cloud][2])

---

## Zusammenfassung der Modellunterschiede nach Anwendungsfall

* **Beste Genauigkeit im Non-Streaming, mehrsprachig?** → **`chirp`**
* **Streaming-Unterstützung + mehrsprachig + Adaptation benötigt?** → **`chirp_2`**
* **Streaming, Diarisierung, automatische Spracherkennung und höchste Genauigkeit gewünscht?** → **`chirp_3`**
* **Einfache Transkription langer Inhalte?** → **`long`**
* **Verarbeitung kurzer Sprachbefehle?** → **`short`**
* **Telefonaufnahmen?** → **`telephony`** oder **`telephony_short`**
* **Medizinische Anwendungsfälle?** → **`medical_conversation`** oder **`medical_dictation`**

---

## Kontext aus der Google-Dokumentation

Die Google-Seite "Select a transcription model" (aktualisiert am 4. September 2025) enthält alle oben genannten Modellkennungen und Beschreibungen. Sie weist auch darauf hin, dass die Legacy-Modelle nicht aktiv gepflegt, aber für die Abwärtskompatibilität beibehalten werden.([Google Cloud][2])

Eine frühere Anmerkung zu "latest\_long" / "latest\_short" bezieht sich auf einen weiteren Satz von Conformer-basierten Modellen – diese gehören jedoch nicht zur Chirp-Linie und sind nicht relevant, wenn der Fokus speziell auf den Chirp- oder Legacy-Modellen liegt.([Google Cloud][5])

---

## TL;DR – So treffen Sie die Auswahl:

* **Höchste Qualität + neue Features (Diarisierung, Streaming, etc.)** → **`chirp_3`**
* **Streaming & Modell-Adaptation Unterstützung** → **`chirp_2`**
* **Non-Streaming mehrsprachige Basis** → **`chirp`**
* **Kurze Äußerungen, lange Audio, Telefonie, Medizin** → verwenden Sie das entsprechende Legacy-Modell (`short`, `long`, `telephony`, `medical_*`)

---

Lassen Sie mich wissen, wenn Sie Hilfe bei der Auswahl des richtigen Modells basierend auf Ihrem spezifischen Audiotyp, Ihrer Sprache oder Ihren Anforderungen an Streaming vs. Batch-Verarbeitung benötigen!

[1]: https://cloud.google.com/speech-to-text/v2/docs/chirp-model?utm_source=chatgpt.com "Chirp: Universal speech model"
[2]: https://cloud.google.com/speech-to-text/v2/docs/transcription-model?utm_source=chatgpt.com "Select a transcription model - Cloud Speech-to-Text"
[3]: https://medium.com/google-cloud/transcribe-everything-everywhere-all-at-once-with-chirp-2-615ac362947d?utm_source=chatgpt.com "Transcribe everything everywhere all at once with Chirp 2"
[4]: https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model?utm_source=chatgpt.com "Chirp 3 Transcription: Enhanced multilingual accuracy"
[5]: https://cloud.google.com/speech-to-text/docs/latest-models?utm_source=chatgpt.com "Introduction to Latest Models | Cloud Speech-to-Text ..."