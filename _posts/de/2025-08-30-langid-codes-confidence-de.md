---
audio: false
generated: true
image: false
lang: de
layout: post
title: Langid-Sprachcodes und Konfidenz
translated: true
type: note
---

In `langid` gibt die Funktion `classify(text)` ein Tupel `(lang, confidence)` zurück, wobei:

*   **`lang`** ein zweibuchstabiger ISO 639-1-Sprachcode ist (manchmal erweitert mit Regionscodes wie `zh-cn` oder `zh-tw`).
*   **`confidence`** ein Float-Wert zwischen 0 und 1 ist, der angibt, wie sicher das Modell ist.

Die Menge der möglichen Werte für `lang` stammt aus den von `langid.py` unterstützten Sprachen. Standardmäßig sind **97 Sprachen** enthalten. Einige gängige Beispiele:

*   `en` → Englisch
*   `zh` / `zh-cn` / `zh-tw` → Chinesisch (allgemein / Vereinfacht / Traditionell)
*   `ja` → Japanisch
*   `ko` → Koreanisch
*   `fr` → Französisch
*   `de` → Deutsch
*   `es` → Spanisch
*   `hi` → Hindi
*   `ar` → Arabisch
*   `ru` → Russisch

Und viele andere – die vollständige Liste deckt die meisten großen Weltsprachen ab (Afrikaans, Bengalisch, Griechisch, Hebräisch, Italienisch, Portugiesisch, Swahili, Thailändisch, Türkisch, Vietnamesisch, etc.).

👉 Falls gewünscht, kann ich Ihnen die **vollständige Liste aller 97 von `langid` unterstützten Codes** geben. Soll ich diese ausgeben?