---
audio: false
generated: true
image: false
lang: de
layout: post
title: Kernbestandteile von LLM-Anwendungen
translated: true
type: note
---

Ja, du denkst in die richtige Richtung. Für die meisten realen Anwendungen, die auf LLMs (oder einem beliebigen Agent-Framework) aufbauen, läuft die *wesentliche Information* auf einige feste Bestandteile hinaus. Alles andere kann in der Regel dynamisch generiert oder gerüstartig erstellt werden. Lass mich das aufschlüsseln:

---

### 1. **Angepasster oder Vertikal-spezifischer Agent-Code**

Dies ist der einzigartige "Klebstoff" deiner Anwendung. Er definiert:

* Die **spezialisierte Logik** für deine Branche (Finanzen, Gesundheitswesen, E-Commerce, etc.).
* Die **Integrationspunkte** (APIs, Datenbanken, interne Tools).
* Die **Workflow-Orchestrierung** (wie der Agent Schritt für Schritt reagiert, welche Funktionen er aufruft, welchen Zustand er behält).

Das ist es, was deine App von einem generischen Chatbot unterscheidet.

---

### 2. **Originale Logs / Daten**

Die **echten Daten** deiner Anwendung sind Gold wert.

* Transaktionsprotokolle, Wissensdatenbanken, Benutzerverläufe, Produktkataloge, etc.
* Dies ist die Quelle der Wahrheit, die deinen Agenten kontextuell relevant und nützlich macht.

Je strukturierter und vertrauenswürdiger diese Daten sind, desto stärker wird deine Anwendung.

---

### 3. **Prompt und Kontext**

Hier teilst du dem Modell mit:

* **Wie es denken soll**: Regeln, Tonfall, Grenzen, aufgabenspezifische Anweisungen.
* **Was es sehen soll**: Einspielen relevanter Kontextinformationen (aus Logs, Benutzeranfragen, Gedächtnis oder Retrieval).

Prompts sind die "Schnittstelle" zwischen dem rohen Modell und deinem angepassten Code bzw. deinen Daten.

---

### 4. **Alles andere kann generiert werden**

UI-Gerüste, Boilerplate-Vorlagen, Zusammenfassungen, natürlichsprachige Erweiterungen, sogar Teile des Integrationscodes – diese können oft automatisch oder halbautomatisch generiert werden. Die Unterscheidungsmerkmale (Logik, Daten, Prompt-/Kontext-Design) sind die Teile, die man nicht allein durch Generierung auslagern kann.

---

👉 Deine Zusammenfassung ist also treffend:
Die **essentiellen Bestandteile** sind (1) deine Agenten-Logik/Code, (2) deine echten Logs/Daten und (3) die Gestaltung von Prompt/Kontext. Der Rest (wie Antwortformatierung, Hilfetext oder generische Abläufe) kann tatsächlich generiert werden.

---

Möchtest du, dass ich ein **minimales Stack-Diagramm** skizziere, das diese Ebenen (essentiell vs. generierbar) visuell darstellt? Das könnte die Trennung verdeutlichen.