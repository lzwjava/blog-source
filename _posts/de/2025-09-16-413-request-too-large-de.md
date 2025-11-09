---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-oss-120b
title: Behebung von 413 Request Too Large Fehlern
translated: true
type: note
---

## Was der Fehler bedeutet

- **413 Request Too Large** ist ein HTTP-Statuscode, der anzeigt, dass der Server die Verarbeitung der Anfrage verweigert hat, weil die Nutzlast die erlaubte Größe überschreitet. Im Kontext des Inference-Dienstes von OpenAI bezieht sich die "Nutzlast" auf die Gesamtanzahl der Token (Eingabe + Ausgabe), die in einer einzelnen Anfrage gesendet werden. [1]

- **Tokens pro Minute (TPM) Limit**: Das Modell `openai/gpt-oss-120b` ist für den On-Demand-Service-Tarif mit einem Maximum von **8.000 TPM** konfiguriert. Die von Ihnen gesendete Anfrage enthielt **13.701 Token**, was **5.701 Token über dem Limit** liegt. [1]

- **Warum es passiert**:
  1. **Großer Prompt** – der Eingabetext (einschließlich Systemanweisungen, Benutzernachrichten und angehängter Daten) könnte sehr lang sein.
  2. **Hohe `max_tokens`-Einstellung** – wenn die Anfrage das Modell auffordert, eine lange Completion zu generieren, wird die prognostizierte Anzahl der Ausgabe-Token zur Eingabeanzahl addiert.
  3. **Schnelle aufeinanderfolgende Aufrufe** – wenn viele Anfragen in kurzer Folge gestellt werden, können die kumulierten Token in der laufenden Minute das TPM-Kontingent überschreiten, selbst wenn jede einzelne Anfrage unter dem Limit liegt.

## Wie man das Problem löst

| Option | Vorgehensweise | Auswirkung |
|--------|------------|--------|
| **Prompt kürzen** | Unnötigen Text entfernen, präzise Anweisungen verwenden oder Daten komprimieren (z. B. große Textblöcke vor dem Senden zusammenfassen). | Verringert die Anzahl der Eingabe-Token. |
| **`max_tokens` reduzieren** | Eine kürzere Completion anfordern (z. B. `max_tokens` auf 500 statt 2000 setzen). | Verringert die prognostizierte Anzahl der Ausgabe-Token. |
| **Anfrage aufteilen** | Ein umfangreiches Dokument in mehrere kleinere Teile zerlegen und das Modell sequenziell aufrufen, um die Ergebnisse anschließend zusammenzufügen. | Hält jeden Aufruf unter dem TPM-Limit. |
| **Tarif wechseln** | Zu einem Tarif mit höherer Kapazität wechseln (z. B. Dev Tier), in dem das TPM-Limit größer oder unbegrenzt ist. | Ermöglicht größere Nutzlasten pro Anfrage ohne Fehler. |
| **Aufrufe drosseln** | Eine kurze Verzögerung zwischen Anfragen einfügen oder Rate-Limiting implementieren, um die Gesamt-Token pro Minute ≤ **8.000** zu halten. | Verhindert das Überschreiten des kumulierten TPM-Limits. |

## Schnell-Checkliste vor dem Senden einer Anfrage

1. **Token zählen** – das Tokenizer-Tool von OpenAI (oder `tiktoken`) verwenden, um die Gesamttoken (Prompt + max Tokens) abzuschätzen.
2. **Bei ≤ 8.000 TPM** für den On-Demand-Tarif bleiben.
3. **Wenn das Limit fast erreicht ist**, eine der oben genannten Lösungsmöglichkeiten in Betracht ziehen.

Indem Sie sicherstellen, dass die Anfrage innerhalb des Kontingents von 8.000 Token pro Minute bleibt, wird der 413 "Request Too Large"-Fehler vermieden. [1]

Zitate:
[1] https://www.reddit.com/r/OpenAI/comments/1nbtl2p/wow_weve_been_burning_money_for_6_months/