---
audio: false
generated: true
lang: de
layout: post
title: Mistral AI-Agenten
translated: true
---

Mistral AI Agents sind autonome Systeme, die von großen Sprachmodellen (LLMs) angetrieben werden und so gestaltet sind, dass sie komplexe Aufgaben auf der Grundlage von hochrangigen Anweisungen ausführen. Durch den Einsatz fortschrittlicher natürlicher Sprachverarbeitung können diese Agenten spezifische Ziele verstehen und ausführen, was sie für eine Vielzahl von Anwendungen wie Kundensupport, Datenanalyse, Workflow-Automatisierung und Code-Assistenz geeignet macht. Sie können planen, Werkzeuge nutzen, Maßnahmen ergreifen und sogar zusammenarbeiten, um spezifische Ziele zu erreichen, und bieten so ein neues Niveau an Automatisierung und Intelligenz.

---

## Agenten erstellen

Mistral AI bietet zwei Hauptmethoden zur Erstellung von Agenten: den **La Plateforme Agent Builder** und die **Agent API**.

### 1. La Plateforme Agent Builder
Der Agent Builder bietet eine benutzerfreundliche Oberfläche zur Erstellung von Agenten ohne umfangreiches technisches Wissen. Um einen Agenten zu erstellen:

- Navigieren Sie zum Agent Builder unter [https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new).
- Passen Sie den Agenten an, indem Sie ein Modell auswählen, die Temperatur einstellen und optionale Anweisungen geben.
- Sobald konfiguriert, kann der Agent über die API oder Le Chat bereitgestellt und aufgerufen werden.

### 2. Agent API
Für Entwickler ermöglicht die Agent API die programmatische Erstellung und Integration von Agenten in bestehende Workflows. Unten sind Beispiele dafür, wie man einen Agenten über die API erstellt und verwendet:

#### Python-Beispiel
```python
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id="your-agent-id",
    messages=[{"role": "user", "content": "What is the best French cheese?"}],
)
print(chat_response.choices[0].message.content)
```

#### JavaScript-Beispiel
```javascript
import { Mistral } from '@mistralai/mistralai';

const apiKey = process.env.MISTRAL_API_KEY;
const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.agents.complete({
    agentId: "your-agent-id",
    messages: [{ role: 'user', content: 'What is the best French cheese?' }],
});
console.log('Chat:', chatResponse.choices[0].message.content);
```

---

## Agenten anpassen

Mistral AI Agenten können durch mehrere Optionen an spezifische Bedürfnisse angepasst werden:

- **Modellauswahl**: Wählen Sie das Modell, das den Agenten antreibt. Optionen umfassen:
  - "Mistral Large 2" (Standard, `mistral-large-2407`)
  - "Mistral Nemo" (`open-mistral-nemo`)
  - "Codestral" (`codestral-2405`)
  - Feinabgestimmte Modelle

- **Temperatur**: Passen Sie die Sampling-Temperatur (zwischen 0,0 und 1,0) an, um die Zufälligkeit der Antworten des Agenten zu steuern. Höhere Werte machen die Ausgaben kreativer, während niedrigere Werte sie fokussierter und deterministischer machen.

- **Anweisungen**: Geben Sie optionale Anweisungen an, um spezifische Verhaltensweisen über alle Interaktionen hinweg durchzusetzen. Zum Beispiel können Sie einen Agenten erstellen, der nur Französisch spricht oder Python-Code ohne Erklärungen generiert.

### Beispiel: Erstellen eines französischsprachigen Agenten
Um einen Agenten zu erstellen, der nur auf Französisch antwortet:
- Setzen Sie das Modell auf "Mistral Large 2".
- Verwenden Sie Anweisungen wie: "Antworte immer auf Französisch, unabhängig von der Sprache der Eingabe."
- Geben Sie wenige Beispiele an, um das Verhalten zu verstärken.

---

## Anwendungsfälle

Mistral AI Agenten können in verschiedenen Branchen und Aufgaben eingesetzt werden. Einige bemerkenswerte Anwendungsfälle umfassen:

- **Kundensupport**: Automatisieren Sie Antworten auf häufige Anfragen, bearbeiten Sie FAQs und eskalieren Sie komplexe Probleme an menschliche Agenten.
- **Datenanalyse**: Erstellen Sie Agenten, die Datensätze analysieren, Berichte generieren oder Berechnungen basierend auf Benutzereingaben durchführen.
- **Workflow-Automatisierung**: Integrieren Sie Agenten mit Tools wie E-Mail, CRM-Systemen oder Zahlungsabwicklung, um wiederholende Aufgaben zu automatisieren.
- **Code-Assistenz**: Entwickeln Sie Agenten, die Code generieren, Debugging-Vorschläge geben oder Unit-Tests erstellen.

### Spezifische Beispiele
- **Französischsprachiger Agent**: Ein Agent, der so konfiguriert ist, dass er nur auf Französisch antwortet, nützlich für Unternehmen, die französischsprachige Kunden ansprechen.
- **Python-Code-Generator**: Ein Agent, der Python-Code-Snippets ohne Erklärungen ausgibt, ideal für Entwickler, die schnellen, sauberen Code benötigen.

---

## Bereitstellung

Sobald ein Agent erstellt wurde, kann er auf zwei Arten bereitgestellt und aufgerufen werden:

- **API-Integration**: Verwenden Sie die Mistral AI API, um den Agenten in Ihre Anwendungen zu integrieren. Siehe die Codebeispiele im Abschnitt "Agenten erstellen" für Details.
- **Le Chat**: Aktivieren Sie die Option, um direkt mit dem Agenten auf der Mistral Le Chat-Plattform zu chatten.

Agenten können leicht innerhalb von Organisationen geteilt werden, und mit den fortschrittlichen Schlussfolgerungsfähigkeiten von Modellen wie Mistral Large 2 können Sie komplexe Workflows mit mehreren Agenten erstellen.

---

Diese Dokumentation bietet eine umfassende Anleitung zum Verständnis, Erstellen, Anpassen und Bereitstellen von Mistral AI Agenten, basierend auf der offiziellen Dokumentation unter [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/). Durch die Nutzung dieser Tools können Sie Aufgaben automatisieren, die Produktivität steigern und neue Effizienzniveaus in Ihren Workflows freisetzen. Für weitere Details erkunden Sie die [Mistral AI-Dokumentation](https://docs.mistral.ai/capabilities/agents/).