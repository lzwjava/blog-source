---
audio: false
generated: true
image: false
lang: de
layout: post
title: Sichere LLM-API-Validierungsebenen
translated: true
type: note
---

Wenn Sie eine **LLM API** erstellen oder verwenden, möchten Sie in der Regel Sicherheitsvorkehrungen treffen, um sicherzustellen, dass die Antworten sicher, gültig und nützlich sind. Hier sind die wichtigsten Methoden, um Prüfungen hinzuzufügen:

---

### 1. **Eingabevalidierung**

* **Schema-Checks**: Stellen Sie sicher, dass die JSON-Anfrage dem erwarteten Schema entspricht, bevor sie an das LLM gesendet wird.
* **Prompt-Bereinigung**: Entfernen oder maskieren Sie unerwünschte Zeichen, bösartige Anweisungen oder Injection-Versuche.
* **Längenprüfungen**: Erzwingen Sie maximale Token-/Zeichenlimits für Eingaben, um unnötige Kosten oder Abschneiden zu vermeiden.

---

### 2. **Ausgabevalidierung**

* **JSON-Schema-Validierung**: Wenn das LLM JSON zurückgeben soll, führen Sie es durch `json.loads()` und validieren Sie es gegen ein Schema (z.B. mit `pydantic`, `jsonschema`).
* **Regex-/Formatprüfungen**: Erzwingen Sie Muster für E-Mails, URLs oder Zahlen.
* **Typüberprüfung**: Stellen Sie sicher, dass Felder den richtigen Typ haben (String, Integer, Liste, etc.).
* **Bereichsprüfungen**: Stellen Sie sicher, dass numerische oder Datumswerte innerhalb der erwarteten Grenzen liegen.

---

### 3. **Sicherheits- und Inhaltsprüfungen**

* **Toxizitäts- oder Obszönitätsfilter**: Lassen Sie die Ausgabe durch einen Klassifikator laufen (z.B. Perspective API, OpenAI Moderation API).
* **Richtlinienfilter**: Definieren Sie Regeln, um Antworten zu blockieren, die bestimmte Schlüsselwörter oder Kategorien enthalten.
* **Halluzinationserkennung**: Fügen Sie Faktenprüfungen hinzu (durch retrieval-augmentierte Prüfungen, Kreuzvalidierung mit mehreren Modellen oder regelbasierte Plausibilitätsprüfungen).

---

### 4. **Geschäftslogik-Beschränkungen**

* **Konsistenzregeln**: Wenn die Antwort mit Systemdaten übereinstimmen muss (z.B. verfügbarer Kontostand, Konfigurationswerte), führen Sie eine Kreuzprüfung durch, bevor Sie sie an den Benutzer zurückgeben.
* **Guardrails**: Verwenden Sie Bibliotheken wie **Guardrails AI**, **LMQL** oder **Instructor**, um strukturierte Ausgaben und Beschränkungen deklarativ durchzusetzen.
* **Nachbearbeitungshooks**: Versehen Sie LLM-Antworten mit benutzerdefinierter Logik (Groß-/Kleinschreibung normalisieren, Standardwerte erzwingen, unerwartete Antworten ablehnen).

---

### 5. **Redundanz & Kreuzvalidierung**

* **Selbstprüfungs-Prompts**: Bitten Sie das LLM, seine eigene Antwort erneut zu validieren oder zu erklären.
* **Dual-Model-Checking**: Verwenden Sie ein kleineres/schnelleres LLM, um die Ausgabe des Hauptmodells zu überprüfen (z.B. "Entspricht diese Antwort dem Schema X?").
* **Abstimmung/Konsens**: Führen Sie mehrere Aufrufe durch und vergleichen Sie die Antworten auf Stabilität.

---

### 6. **Betriebliche Sicherheitsvorkehrungen**

* **Ratenbegrenzung**: Verhindern Sie den Missbrauch der API.
* **Timeouts**: Brechen Sie Anfragen ab, die hängen bleiben.
* **Protokollierung und Audit-Trails**: Führen Sie Aufzeichnungen über Anfragen und gefilterte Antworten.
* **Fallbacks**: Wenn die Validierung fehlschlägt, wiederholen Sie den Vorgang mit angepasstem Prompt oder geben Sie eine sichere Standardantwort/einen Fehler zurück.

---

👉 In der Praxis schichtet ein guter LLM-API-Stack diese Maßnahmen:

1. Eingabe validieren.
2. LLM aufrufen.
3. Ausgabe gegen Schema + Geschäftsregeln validieren.
4. Sicherheits-/Inhaltsfilter anwenden.
5. Nur zurückgeben, wenn alle Prüfungen bestanden sind (andernfalls Wiederholung/Fallback).

---

Möchten Sie, dass ich Ihnen ein **Python-Beispiel** zeige, in dem wir einen LLM-API-Aufruf mit JSON-Schema-Validierung und Moderationsprüfungen umschließen?