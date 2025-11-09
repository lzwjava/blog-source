---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Arbeiten mit OpenAI Chat Completions Modellen
translated: true
type: note
---

Sie haben auf den Microsoft Learn-Artikel **„Work with chat completions models“** (veröffentlicht am **1. September 2025**) verlinken. Hier ist eine klare und prägnante Zusammenfassung der Kernpunkte:

---

### Wichtige Highlights

*   **Chat-orientierte Modelle**
    Die neueren Chat-Modelle unterscheiden sich von früheren GPT-3-Modellen. Anstelle von „Text-in, Text-out“ verwenden sie ein **Konversation-in, Nachricht-out** Format. Im Wesentlichen ist die Eingabe wie ein Transkript strukturiert (Rollen wie *system*, *user*, *assistant*), und das Modell gibt eine Nachricht zurück, um die Konversation fortzusetzen ([Microsoft Learn][1]).

*   **Für Dialoge konzipiert**
    Diese Struktur ist für mehrfache Hin-und-Her-Gespräche optimiert. Sie funktioniert auch gut für Szenarien mit einer einzelnen Eingabeaufforderung, aber das Konversationsformat ermöglicht flüssigere Interaktionen ([Microsoft Learn][1]).

*   **Behandeln Sie sie nicht wie ältere Modelle**
    Diese Chat-Modelle sind gesprächiger und liefern oft weniger nützliche Antworten, wenn man sie wie GPT-3 behandelt. Es wird empfohlen, die neue Chat-Oberfläche für die besten Ergebnisse zu verwenden ([Microsoft Learn][1]).

*   **Codebeispiel**
    Der Artikel enthält ein grundlegendes Codebeispiel in Python-ähnlicher Syntax für den Aufruf der Azure Chat Completions API:

    ```python
    from openai import OpenAI
    import os

    client = OpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
    )

    response = client.chat.completions.create(
        model="gpt-4o",  # or deployment_name
        messages=[
            {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
            {"role": "user", "content": "Who were the founders of Microsoft?"}
        ]
    )

    print(response.model_dump_json(indent=2))
    print(response.choices[0].message.content)
    ```

    Dies zeigt, wie Nachrichten richtig gesendet (mit Rollentrennung) und die Antwort des Modells abgerufen werden ([Microsoft Learn][1]).

---

### Warum das wichtig ist

1.  **Verbesserter Konversationskontext** — Chat-Modelle erhalten den Gesprächsfluss und Kontext über mehrere Interaktionen hinweg besser.
2.  **Verbesserte Benutzerfreundlichkeit** — Die Verwendung von Rollen (System, Benutzer, Assistent) ermöglicht klarere Anweisungen, das Setzen eines Persönlichkeitsprofils oder von Einschränkungen.
3.  **Fehler vermeiden** — Die Behandlung von Chat-Modellen wie Modelle früherer Generationen kann zu schlechter Antwortqualität führen; verwenden Sie die Chat-API-Schnittstelle wie vorgesehen.

---

Lassen Sie mich wissen, wenn Sie Hilfe beim Durcharbeiten des Codebeispiels, bei der Anpassung an Ihr Setup oder bei der Erkundung verwandter Anleitungen benötigen – ich helfe gerne!

Und wie von Ihnen bevorzugt, habe ich dies in einem einfachen, lesbaren Format ohne Tabellen gehalten.

[1]: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt?utm_source=chatgpt.com "Work with chat completion models - Azure OpenAI in ..."