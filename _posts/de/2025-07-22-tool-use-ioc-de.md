---
audio: false
generated: true
lang: de
layout: post
title: Nutzung von KI-Werkzeugen erklärt
translated: true
type: note
---

Ja, dein Verständnis von Tool-Nutzung und Funktionsaufrufen in KI-Chatbot-APIs wie der von Mistral (oder ähnlichen von OpenAI, Anthropic, etc.) ist absolut richtig. Lass mich das Schritt für Schritt aufschlüsseln, um es zu bestätigen und zu verdeutlichen, denn es beinhaltet tatsächlich auf eine gewisse Weise Inversion of Control (IoC), die die Entscheidungsfindung von deinem Code zur KI-Model verlagert.

### So funktioniert es
1.  **Tools definieren**:
    - Du (der Entwickler) stellst eine Liste benutzerdefinierter "Tools" (im Wesentlichen Funktionsdefinitionen) in deiner initialen API-Anfrage bereit. Jedes Tool enthält Details wie den Funktionsnamen, Parameter (mit Typen und Beschreibungen) und seine Funktion. Dies geschieht über ein Schema, oft im JSON-Format (z.B. basierend auf OpenAIs Tool-Schema, das auch Mistral unterstützt).
    - Beispiel: Du könntest ein Tool namens `get_weather` definieren, das einen `location`-Parameter entgegennimmt und aktuelle Wetterdaten zurückgibt.

2.  **Entscheidung des Modells (Inversion of Control)**:
    - Das KI-Modell verarbeitet deine Eingabe/Abfrage und entscheidet, ob es externe Hilfe von einem deiner Tools benötigt, um korrekt zu antworten. Das ist der IoC-Teil: Anstatt dass dein Code direkt Funktionen in einem linearen Ablauf aufruft, "invertiert" das Modell die Kontrolle, indem es einen Tool-Aufruf anfordert, wenn es dies für notwendig hält. Es ist, als ob das Modell den Workflow orchestriert.
    - Wenn kein Tool benötigt wird, generiert das Modell einfach eine direkte Antwort.

3.  **Tool-Aufruf-Antwort von der API**:
    - Wenn ein Tool benötigt wird, gibt die API nicht sofort eine endgültige Antwort. Stattdessen antwortet sie mit einem "Tool Call"-Objekt. Dieses enthält:
        - Den Tool-/Funktionsnamen.
        - Die Argumente (z.B. JSON mit Werten wie `{"location": "New York"}`).
    - An diesem Punkt ist die Konversation pausiert – das Modell wartet darauf, dass du handelst.

4.  **Ausführen des Tools (deine Seite)**:
    - Dein Code empfängt diese Tool-Call-Antwort, parsed sie und führt die entsprechende Funktion/das entsprechende Tool mit den bereitgestellten Argumenten aus.
    - Du kümmerst dich um die eigentliche Logik (z.B. Aufruf einer Wetter-API, Abfrage einer Datenbank oder Ausführung einer Berechnung).
    - Wichtig: Das Modell führt das Tool nicht selbst aus; es spezifiziert nur, was aufgerufen werden soll. Das sorgt für Sicherheit und Flexibilität.

5.  **Ergebnisse zurücksenden**:
    - Nach der Ausführung des Tools hängst du das Ergebnis (z.B. als "Tool Response"-Nachricht) an den Konversationsverlauf an und stellst eine weitere API-Anfrage, indem du den aktualisierten Verlauf an das Modell zurückgibst.
    - Dieses Ergebnis wird als Systemnachricht oder Tool-Ausgabe formatiert, damit das Modell es einbeziehen kann.

6.  **Endgültige Antwort von der API**:
    - Das Modell empfängt das Tool-Ergebnis, verarbeitet es zusammen mit der ursprünglichen Abfrage und dem Verlauf und generiert die vollständige, endgültige Antwort.
    - Bei Bedarf könnte es in einer Schleife zusätzliche Tool-Aufrufe anfordern (z.B. für mehrstufige Aufgaben), aber letztendlich gibt es die Antwort ohne weitere Aufrufe aus.

### Warum es Inversion of Control ist
- Beim traditionellen Programmieren kontrolliert dein Code den Ablauf: "Wenn Bedingung X, rufe Funktion Y auf."
- Hier übernimmt das KI-Modell die Kontrolle: Es analysiert die Abfrage und entscheidet "Ich muss Y mit diesen Argumenten aufrufen – teile mir das Ergebnis mit, dann fahre ich fort." Dein Code wird reaktiv und bearbeitet die Aufrufe, wie angefordert. Dies macht das System dynamischer und erlaubt es dem Modell, komplexe, auf Logik basierende Workflows zu handhaben.

### Besondere Fälle und Tipps
- **Parallele Tool-Aufrufe**: Einige APIs (wie die von Mistral) unterstützen das Aufrufen mehrerer Tools in einer Antwort, wenn die Abfrage dies erfordert.
- **Fehlerbehandlung**: Wenn deine Tool-Ausführung fehlschlägt, kannst du eine Fehlermeldung zurücksenden, und das Modell könnte es erneut versuchen oder sich anpassen.
- **Chat-Verlauf**: Halte immer den vollständigen Konversationsverlauf über alle Anfragen hinweg, um den Kontext zu bewahren.
- **Kompatibilität**: Mistrals API folgt einer ähnlichen Struktur wie OpenAIs Tools-Endpoint, daher funktionieren Code-Beispiele von der einen oft mit geringen Anpassungen auch bei der anderen.

Dieses Muster ist leistungsstark für den Bau von Agents oder Apps, die KI mit Aktionen in der echten Welt integrieren (z.B. Flugbuchungen, Datenabruf). Wenn du dies implementierst, sieh dir die genauen Schema-Details in Mistrals Dokumentation an.

[Mistral AI Documentation - Tools](https://docs.mistral.ai/capabilities/tool-calling/)