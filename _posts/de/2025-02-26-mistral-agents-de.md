---
audio: false
generated: true
lang: de
layout: post
title: Mistral KI Agenten
translated: true
type: note
---

Mistral AI Agents sind autonome Systeme, die von großen Sprachmodellen (LLMs) angetrieben werden und dazu entwickelt sind, komplexe Aufgaben auf der Grundlage von allgemeinen Anweisungen auszuführen. Durch den Einsatz fortschrittlicher Natural Language Processing können diese Agents spezifische Ziele verstehen und umsetzen, was sie für eine Vielzahl von Anwendungen geeignet macht, wie z.B. Kundensupport, Datenanalyse, Workflow-Automatisierung und Coding-Assistenz. Sie können planen, Tools nutzen, Aktionen ausführen und sogar zusammenarbeiten, um bestimmte Ziele zu erreichen, und bieten so ein neues Maß an Automatisierung und Intelligenz.

---

## Erstellen von Agents

Mistral AI bietet zwei Hauptmethoden zum Erstellen von Agents: den **La Plateforme Agent Builder** und die **Agent API**.

### 1. La Plateforme Agent Builder
Der Agent Builder bietet eine benutzerfreundliche Oberfläche zum Erstellen von Agents ohne umfangreiche technische Kenntnisse. So erstellen Sie einen Agent:

- Navigieren Sie zum Agent Builder unter [https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new).
- Passen Sie den Agent an, indem Sie ein Modell auswählen, die Temperatur festlegen und optionale Anweisungen hinzufügen.
- Nach der Konfiguration kann der Agent über die API oder Le Chat bereitgestellt und genutzt werden.

### 2. Agent API
Für Entwickler ermöglicht die Agent API die programmatische Erstellung und Integration von Agents in bestehende Workflows. Nachfolgend finden Sie Beispiele, wie Sie einen Agent über die API erstellen und nutzen können:

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

## Anpassen von Agents

Mistral AI Agents können über mehrere Optionen an spezifische Anforderungen angepasst werden:

- **Modellauswahl**: Wählen Sie das Modell, das den Agent antreibt. Optionen sind:
  - "Mistral Large 2" (Standard, `mistral-large-2407`)
  - "Mistral Nemo" (`open-mistral-nemo`)
  - "Codestral" (`codestral-2405`)
  - Feinabgestimmte Modelle (Fine-tuned models)

- **Temperatur**: Passen Sie die Sampling-Temperatur (zwischen 0.0 und 1.0) an, um die Zufälligkeit der Antworten des Agents zu steuern. Höhere Werte machen die Ausgaben kreativer, während niedrigere Werte sie fokussierter und deterministischer machen.

- **Anweisungen**: Geben Sie optionale Anweisungen an, um spezifisches Verhalten über alle Interaktionen hinweg zu erzwingen. Sie können beispielsweise einen Agent erstellen, der nur Französisch spricht oder Python-Code ohne Erklärungen generiert.

### Beispiel: Erstellen eines französischsprachigen Agents
So erstellen Sie einen Agent, der nur auf Französisch antwortet:
- Setzen Sie das Modell auf "Mistral Large 2".
- Verwenden Sie Anweisungen wie: "Antworte immer auf Französisch, unabhängig von der Sprache der Eingabe."
- Geben Sie Few-Shot-Beispiele an, um das Verhalten zu verstärken.

---

## Anwendungsfälle

Mistral AI Agents können in verschiedenen Branchen und für verschiedene Aufgaben eingesetzt werden. Einige bemerkenswerte Anwendungsfälle sind:

- **Kundensupport**: Automatisieren Sie Antworten auf häufige Anfragen, bearbeiten Sie FAQs und eskalieren Sie komplexe Probleme an menschliche Agents.
- **Datenanalyse**: Erstellen Sie Agents, die Datensätze analysieren, Berichte generieren oder Berechnungen auf der Grundlage von Benutzereingaben durchführen.
- **Workflow-Automatisierung**: Integrieren Sie Agents in Tools wie E-Mail, CRM-Systeme oder Zahlungsabwicklung, um repetitive Aufgaben zu automatisieren.
- **Coding-Assistenz**: Entwerfen Sie Agents, die Code generieren, Debugging-Vorschläge machen oder Unit-Tests erstellen.

### Spezifische Beispiele
- **Französischsprachiger Agent**: Ein Agent, der so konfiguriert ist, dass er nur auf Französisch antwortet – nützlich für Unternehmen, die französischsprachige Kunden ansprechen.
- **Python-Code-Generator**: Ein Agent, der Python-Code-Snippets ohne Erklärungen ausgibt, ideal für Entwickler, die schnellen, sauberen Code benötigen.

---

## Bereitstellung

Sobald ein Agent erstellt wurde, kann er auf zwei Arten bereitgestellt und genutzt werden:

- **API-Integration**: Verwenden Sie die Mistral AI API, um den Agent in Ihre Anwendungen zu integrieren. Details finden Sie in den Codebeispielen im Abschnitt "Erstellen von Agents".
- **Le Chat**: Schalten Sie die Option um, um direkt auf der Mistral Le Chat-Plattform mit dem Agent zu chatten.

Agents können einfach innerhalb von Organisationen geteilt werden. Mit den fortschrittlichen Reasoning-Fähigkeiten von Modellen wie Mistral Large 2 können Sie komplexe Workflows mit mehreren Agents aufbauen.

---

Diese Dokumentation bietet einen umfassenden Leitfaden zum Verständnis, Erstellen, Anpassen und Bereitstellen von Mistral AI Agents, basierend auf der offiziellen Dokumentation unter [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/). Durch die Nutzung dieser Tools können Sie Aufgaben automatisieren, die Produktivität steigern und neue Effizienzstufen in Ihren Workflows erreichen. Weitere Details finden Sie in der [Mistral AI-Dokumentation](https://docs.mistral.ai/capabilities/agents/).