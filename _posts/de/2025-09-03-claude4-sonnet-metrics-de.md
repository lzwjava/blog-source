---
audio: false
generated: true
image: false
lang: de
layout: post
title: Claude-4-Sonnet-Abschlussmetriken erklärt
translated: true
type: note
---

Kurzversion: Es endete normal.
`finish_reason: "stop"` bedeutet, dass das Modell ein natürliches Ende seiner Antwort erreicht hat (auf eine Stoppsequenz wie das Assistant-End-Token gestoßen ist) und **nicht** an eine Längenbeschränkung, einen Fehler oder einen Abbruch gelangt ist.

Hier ist, was der Rest dieses Datensatzes dir auf einfachem Deutsch sagt:

* **Modell & Route**
  Du hast **anthropic/claude-4-sonnet-20250522** über **Google Vertex** (`provider_name: "Google"`) aufgerufen. Deshalb siehst du einen `provider_responses`-Eintrag mit Status 200.

* **Zeitmessung / Geschwindigkeit**

  * `latency: 2850` → \~2,85 s bis der **erste Token** angezeigt wurde.
  * `generation_time: 76365` → insgesamt etwa **76,4 s**, um die Antwort zu beenden.
  * Bei `tokens_completion: 2376` entspricht das einer Durchsatzrate von ungefähr **31 Token/Sekunde** über die gesamte Generierung (2376 ÷ 76,4 ≈ 31,1).

* **Token-Anzahlen (zwei Sätze)**

  * `tokens_prompt: 8446`, `tokens_completion: 2376` → die Zählungen deines Aggregators.
  * `native_tokens_prompt: 9007`, `native_tokens_completion: 2511` → die **eigene Tokenizer-/Abrechnungsmethode des Providers**. Diese unterscheiden sich oft aufgrund verschiedener Tokenizer, System-Wrapper oder versteckter Steuer-Tokens.
  * `native_tokens_reasoning: 0` → dieser Durchlauf verwendete keinen "Reasoning-Tokens"-Zähler (einige Provider stellen dies frei, wenn ein spezieller Reasoning-Modus aktiviert ist).
  * `native_tokens_cached: 0` → kein Prompt-Caching-Treffer.

* **Streaming & Abbruch**

  * `streamed: true` → Token wurden an dich gestreamt.
  * `cancelled: false` → du hast es nicht unterbrochen.

* **Warum nicht "length"?**
  Wenn die maximale Token-Grenze erreicht worden wäre, würdest du `finish_reason: "length"` sehen. Das ist nicht der Fall, also hat das Modell vor Erreichen einer Grenze abgeschlossen.

* **Wann ist das passiert?**
  `created_at: "2025-09-02T17:26:45.92824+00:00"` (UTC). In deiner Zeitzone (Asia/Taipei, UTC+8) ist das **2025-09-03 01:26:45**.

* **Kosten/Nutzungsfelder**

  * `usage: 0.064686` → die Kosten-/Nutzungsmetrik deines Systems (die Einheiten hängen von deiner Abrechnungsebene ab).
  * Mehrere `null`-Felder bedeuten lediglich, dass dein Router keine zusätzlichen Details aufgezeichnet hat (Moderations-Latenz, Suchergebnisse, etc.).

* **Verschiedenes**

  * `finish_reason: "stop"` (nochmals) ist der Schlüssel: Normaler Stopp via Stopp-Token.
  * `origin: ""`, `app_id: null` → kein spezifischer App-Tag.
  * `is_byok: false` → kein Bring-Your-Own-Key-Aufruf.

Wenn du möchtest, füge ein zweites Beispiel ein, bei dem du `length` oder `cancelled` gesehen hast, und ich werde sie zeilenweise gegenüberstellen (ohne Tabellen).