---
audio: false
generated: true
image: false
lang: de
layout: post
title: Einfach Erklärte LLM-Tokens
translated: true
type: note
---

Gute Frage — Tokens in LLM-APIs können anfangs etwas verwirrend sein. Lass mich das klar aufschlüsseln.

---

## Was Tokens sind

* Ein **Token** ist die kleinste Texteinheit, die das Modell verarbeitet.
* Es ist **nicht genau ein Wort**. Tokens sind normalerweise Wortteile, vollständige Wörter, Satzzeichen oder sogar Leerzeichen, abhängig von der Sprache und dem Tokenizer.
* LLMs (wie OpenAI GPT-Modelle) teilen Text mithilfe eines vordefinierten **Tokenizers** in Tokens auf.

Zum Beispiel:

* `"cat"` → 1 Token
* `"cats"` → könnte aufgeteilt werden als `"cat"` + `"s"` → 2 Tokens
* `"You're handsome."` → wird aufgeteilt in etwa `"You"`, `"'re"`, `" handsome"`, `"."` → **4 Tokens**

Tokens sind also **Subword-Einheiten**, die so optimiert sind, dass das Modell viele Sprachen und seltene Wörter effizient verarbeiten kann.

---

## Warum Tokens in APIs wichtig sind

1. **Abrechnung** – Die meisten LLM-APIs berechnen nach Tokens (Eingabe + Ausgabe).
2. **Limits** – Modelle haben maximale Token-Limits (z.B. GPT-4 Turbo 128k bedeutet bis zu 128.000 Tokens insgesamt für Eingabe + Ausgabe).
3. **Effizienz** – Du solltest Tokens in Prompts minimieren, um Kosten zu senken und innerhalb der Limits zu bleiben.

---

## Umgang mit Tokens in der Praxis

* **Tokens schätzen**: Eine grobe Faustregel sind \~4 Zeichen pro Token im Englischen. Ein englischer Aufsatz mit 1.000 Wörtern (≈5.000 Zeichen) entspricht also \~1.200–1.300 Tokens.
* **Tokens genau prüfen**: Die meisten SDKs (wie `tiktoken` in Python für OpenAI) erlauben es, Tokens vor dem Senden zu zählen.
* **Prompts optimieren**:

  * Entferne unnötige Leerzeichen/Wörter.
  * Verwende präzise Anweisungen.
  * Fasse Kontext zusammen, anstatt Rohtext zu verwenden.

---

## Beispiel

```python
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
text = "You're handsome."
tokens = enc.encode(text)
print(tokens)        # Liste der Token-IDs
print(len(tokens))   # Anzahl der Tokens
```

Dies würde etwa `[9125, 3938, 13]` → 3 Tokens ausgeben (abhängig von der genauen Tokenizer-Version).

---

✅ Also: **Tokens ≠ Wörter**. Sie sind die Bausteine, die das LLM sieht. `"You're handsome."` sind etwa 3–4 Tokens, nicht 2 Wörter.

---

Möchtest du, dass ich dir zeige, **wie du Tokens mit deinem eigenen Text (z.B. Transkripten, Aufsätzen, Code) zählen kannst**, damit du Kosten/Limits vor dem API-Aufruf siehst?