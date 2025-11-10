---
audio: false
generated: true
image: false
lang: de
layout: post
title: Claude Sonnet Laufzeitmetriken erklärt
translated: true
type: note
---

Was du siehst, sind **Runtime-Metriken** vom Inference von `anthropic/claude-sonnet-4` über Google Vertex AI. Lass mich das aufschlüsseln:

* **First Token Latency (2,85s):**
  Das ist die Verzögerung zwischen dem Senden deines Prompts und dem Empfang des allerersten Ausgabe-Tokens. Sie beinhaltet Netzwerklatenz, Request-Queuing und die anfängliche Berechnung des Modells. Für große Modelle wie Claude Sonnet sind ein paar Sekunden normal.

* **Throughput (32,9 Tokens/Sek.):**
  Nachdem das erste Token generiert wurde, streamt das Modell die nachfolgenden Tokens. 32,9 Tokens pro Sekunde ist eine solide Rate – nicht die schnellstmögliche, aber gut für ein großes Modell. Der Durchsatz kann variieren, abhängig von der Modellgröße, der Auslastung des Providers (Vertex) und der Länge deines Prompts.

* **Finish Reason (stop):**
  Dies zeigt einfach an, dass das Modell natürlich stoppte, als es das Ende seines generierten Textes erreicht hat (im Gegensatz zum Erreichen eines Längenlimits, eines Cutoffs oder eines Fehlers).

Also, **"warum?"** → weil diese Zahlen normale Inference-Charakteristiken eines großen LLM beschreiben, wenn es über Vertex läuft:

* Etwas Startlatenz ist erwartet (Kompilierung, Optimierung, Routing).
* Der Durchsatz stabilisiert sich, sobald die Generierung beginnt.
* Stop ist der beabsichtigte Abschlusszustand.

Möchtest du, dass ich diese Zahlen auch mit typischen Leistungsbereichen für andere Modelle (wie GPT-5, Gemini Pro, DeepSeek, etc.) vergleiche, damit du siehst, ob dies im Kontext "schnell" oder "langsam" war?