---
audio: false
generated: true
image: false
lang: de
layout: post
title: Tool Use vs Function Calling erklärt
translated: true
type: note
---

Lassen Sie uns den Unterschied zwischen **Tool Use** (Werkzeugnutzung) und **Function Calling** (Funktionsaufruf) im Kontext von LLM-APIs aufschlüsseln:

---

## 1. Tool Use (Werkzeugnutzung)

* **Konzept**: Tool Use ist ein breites Konzept, bei dem das LLM mit externen Fähigkeiten erweitert wird. Anstatt nur Text zu generieren, kann es ein "Werkzeug verwenden", um Informationen abzurufen, Code auszuführen, eine Datenbank abzufragen oder ein Bild zu generieren.
* **Implementierung**: In der Praxis sind "Tools" externe APIs oder Systeme, die bei der LLM-Laufzeitumgebung registriert sind (z. B. eine Such-API, eine Python-Ausführungsumgebung oder eine Kalender-API).
* **Rolle des LLM**: Das Modell entscheidet, wann es das Tool aufruft, mit welchen Argumenten, und integriert die Ergebnisse wieder in die Konversation.
* **Beispiel**:

  * Benutzer: "Wie ist das Wetter in Guangzhou?"
  * LLM: Ruft das `weather`-Tool mit `{city: "Guangzhou"}` auf → erhält `28°C, sonnig`.
  * LLM: Antwortet: "Es ist 28°C und sonnig."

Stellen Sie sich **Tool Use** als ein allgemeines Orchestrierungs-Framework vor, bei dem das LLM nicht nur mit Worten antwortet, sondern Aktionen mit externen Systemen koordiniert.

---

## 2. Function Calling (Funktionsaufruf)

* **Konzept**: Function Calling ist ein *strukturierter* Mechanismus, der von einigen LLM-APIs (wie OpenAI, Anthropic usw.) bereitgestellt wird. Dabei definieren Sie Funktionen (mit Namen, Parametern, Schemata), und das LLM kann JSON-Argumente zurückgeben, um sie aufzurufen.
* **Implementierung**: Sie stellen dem Modell JSON-Schemata zur Verfügung, die die Funktionen beschreiben. Die Ausgabe des Modells ist dann entweder Text oder ein strukturiertes Funktionsaufruf-Objekt.
* **Rolle des LLM**: Anstatt API-Aufrufe zu "halluzinieren", gibt das Modell gültige strukturierte Argumente für vordefinierte Funktionen aus.
* **Beispiel**:

  * Sie definieren eine Funktion:

    ```json
    {
      "name": "getWeather",
      "description": "Aktuelles Wetter abrufen",
      "parameters": {
        "type": "object",
        "properties": {
          "city": {"type": "string"}
        },
        "required": ["city"]
      }
    }
    ```
  * Benutzer: "Wie ist das Wetter in Guangzhou?"
  * LLM: Gibt aus → `{ "name": "getWeather", "arguments": {"city": "Guangzhou"} }`
  * Ihr System führt die Funktion aus und leitet die Ergebnisse zurück.

Dies macht **Function Calling** zu einer spezifischen, sicheren, schema-gesteuerten Art, **Tool Use** durchzuführen.

---

## 3. Wichtige Unterschiede

* **Umfang**:

  * Tool Use = allgemeines Konzept (LLM, erweitert um externe Systeme).
  * Function Calling = eine standardisierte API-Design-Implementierung für strukturierte Aufrufe.
* **Kontrolle**:

  * Tool Use kann freier sein (das LLM entscheidet und formatiert).
  * Function Calling erzwingt strikte Schemata, was Mehrdeutigkeit und Halluzinationen reduziert.
* **Interoperabilität**:

  * Tool Use kann viele externe Systeme einbeziehen (Suche, Code-Ausführung, Bildgenerierung).
  * Function Calling eignet sich am besten, wenn Sie präzise, strukturierte Argumente benötigen (wie für APIs oder Datenbankabfragen).

---

## 4. Mentales Modell

* Function Calling ist eine **Teilmenge** von Tool Use.
* Wenn Tool Use die *allgemeine Strategie* ist, dann ist Function Calling die *sichere, strukturierte Methode*, die die meisten APIs bereitstellen.

---

Möchten Sie, dass ich Ihnen auch ein **Workflow-Beispiel im direkten Vergleich** zeige (wie Benutzeranfrage → LLM-Ausgabe → Ausführung), um den Unterschied konkreter zu veranschaulichen?