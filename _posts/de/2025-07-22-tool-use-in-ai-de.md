---
audio: false
generated: true
lang: de
layout: post
title: KI-Werkzeugnutzung in APIs erklärt
translated: true
type: note
---

### Was ist Tool Use in KI-APIs?

Tool Use, oft auch als "Tool Calling" oder "Function Calling" bezeichnet, ist eine Funktion in KI-APIs, die es großen Sprachmodellen (LLMs) ermöglicht, mit externen Tools, Funktionen oder APIs zu interagieren. Anstatt Antworten ausschließlich auf Basis ihres internen Wissens zu generieren, kann das Modell entscheiden, vordefinierte Funktionen aufzurufen, um Echtzeitdaten abzurufen, Berechnungen durchzuführen oder Aktionen auszuführen. Dies macht die KI dynamischer und nützlicher für Aufgaben wie das Abfragen von Wetterdaten, das Durchsuchen von Datenbanken oder die Integration mit anderen Diensten.

Der Prozess funktioniert typischerweise wie folgt:
- Sie definieren Tools (Funktionen) mit Beschreibungen und Parametern im JSON-Format.
- Das Modell analysiert die Anfrage des Benutzers und gibt, falls nötig, einen "Tool Call" mit dem Funktionsnamen und den Argumenten aus.
- Ihre Anwendung führt die Funktion aus und füttert das Ergebnis zurück an das Modell.
- Das Modell generiert dann eine endgültige Antwort, die die Ausgabe des Tools einbezieht.

Dies ist häufig von OpenAIs Function Calling API inspiriert, und viele Anbieter wie Mistral und DeepSeek unterstützen kompatible Implementierungen.

### Mistral oder DeepSeek für Tool Use?

Sowohl Mistral AI als auch DeepSeek AI unterstützen Tool Calling in ihren APIs, was sie geeignet für den Bau von Agenten oder Anwendungen macht, die externe Integrationen erfordern. Hier ist ein kurzer Vergleich basierend auf verfügbaren Informationen:

- **Unterstützung für Tool Use**:
  - Beide folgen einer ähnlichen Struktur wie die OpenAI-API und ermöglichen eine einfache Integration von Tools über JSON-Schemata.
  - Mistral unterstützt es bei Modellen wie Mistral Large und Medium, mit Optionen für agentenbasierte Workflows.
  - DeepSeek unterstützt es primär durch sein "deepseek-chat"-Modell und ist vollständig kompatibel mit OpenAIs SDK.

- **Vor- und Nachteile**:
  - **Mistral**: Vielseitiger für allgemeine Aufgaben, schnellere Inferenz in einigen Benchmarks und besser geeignet für europäische Datenschutzanforderungen. Es glänzt durch schnelle Antworten und hat starke multilinguale Fähigkeiten. Allerdings kann es teurer sein (z.B. sind Input/Output-Kosten höher im Vergleich zu DeepSeek).
  - **DeepSeek**: Deutlich günstiger (bis zu 28x kostengünstiger in einigen Vergleichen), stark in Mathematik, Coding und Reasoning-Aufgaben. Es ist ideal für budgetbewusste Nutzer oder bei hohem Nutzungsvolumen. Nachteile sind potentiell langsamere Leistung bei nicht-technischen Aufgaben und weniger Fokus auf multimodale Features.
  - **Was wählen?** Wenn die Kosten Priorität haben und Ihr Anwendungsfall Coding/Mathe mit Tools beinhaltet, wählen Sie DeepSeek. Für breitere Anwendungen, schnellere Antworten oder Enterprise-Features wie Agents ist Mistral besser. Beide sind open-source-freundlich und leistungsstark, aber testen Sie sie für Ihre spezifischen Bedürfnisse.

Letztendlich ist keines strikt "besser" für Tool Use – beide funktionieren gut. DeepSeek könnte bei Kosteneinsparungen vorn liegen, während Mistral ausgereifterere Agent-Integrationen bietet.

### Wie man Tool Use verwendet

Um Tool Calling zu verwenden, benötigen Sie einen API-Schlüssel vom jeweiligen Anbieter (registrieren Sie sich auf mistral.ai für Mistral oder platform.deepseek.com für DeepSeek). Beide verwenden Python-SDKs, die denen von OpenAI ähneln. Nachfolgend finden Sie Schritt-für-Schritt-Beispiele für ein einfaches Tool zur Wetterabfrage.

#### Verwendung von Tool Use mit Mistral AI
Mistrals API unterstützt Tool Calling über ihren `MistralClient` in Chat Completions. Installieren Sie das SDK mit `pip install mistralai`.

**Beispiel Python-Code** (angepasst aus offiziellen und Community-Quellen):
```python
from mistralai import Mistral

# Client mit Ihrem API-Schlüssel initialisieren
api_key = "YOUR_MISTRAL_API_KEY"
model = "mistral-large-latest"  # Unterstützt Tool Calling
client = Mistral(api_key=api_key)

# Tools (Funktionen) definieren
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city, e.g., San Francisco"}
                },
                "required": ["location"]
            }
        }
    }
]

# Benutzernachricht
messages = [{"role": "user", "content": "What's the weather in Hangzhou?"}]

# Erster API-Aufruf: Modell entscheidet, ob ein Tool benötigt wird
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # Entscheidet automatisch über Tool-Nutzung
)

# Auf Tool Calls prüfen
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # Die Antwort des Modells an die Nachrichten anhängen
    messages.append(response.choices[0].message)
    
    # Ausführung des Tools simulieren (im echten Code eine echte API aufrufen)
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C and sunny"  # Ersetzen durch echten Funktionsaufruf
        
        # Tool-Ergebnis anhängen
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # Zweiter API-Aufruf: Modell generiert endgültige Antwort
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

Dieser Code sendet eine Abfrage, prüft auf einen Tool Call, führt ihn aus (hier simuliert) und erhält die endgültige Antwort. Für agentenbasierte Setups verwenden Sie Mistrals Beta Agents API für komplexere Workflows.

#### Verwendung von Tool Use mit DeepSeek AI
DeepSeeks API ist OpenAI-kompatibel, daher können Sie das OpenAI Python SDK verwenden. Installieren Sie es mit `pip install openai`.

**Beispiel Python-Code** (aus offizieller Dokumentation):
```python
from openai import OpenAI

# Client mit DeepSeek Base URL und API-Schlüssel initialisieren
client = OpenAI(
    api_key="YOUR_DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)

# Tools definieren
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# Funktion zum Senden von Nachrichten
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # Unterstützt Tool Calling
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# Benutzernachricht
messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

# Tool Call verarbeiten
tool = message.tool_calls[0]
messages.append(message)

# Tool-Ausführung simulieren (durch echte Funktion ersetzen)
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# Endgültige Antwort erhalten
message = send_messages(messages)
print(f"Model>\t {message.content}")
```

Dies folgt demselben Ablauf: Abfrage → Tool Call → Ausführung → endgültige Antwort. DeepSeek begrenzt die Kontextlänge, halten Sie Nachrichten daher prägnant.

Für fortgeschrittene Nutzung, prüfen Sie Rate Limits, Kosten und modellspezifische Dokumentation. Testen Sie in einer Sandbox, um Fehler wie ungültige Parameter zu behandeln.

### Referenzen
- [Mistral AI Function Calling Dokumentation](https://docs.mistral.ai/agents/function_calling/)
- [DeepSeek API Function Calling Guide](https://api-docs.deepseek.com/guides/function_calling)
- [Mistral AI Function Calling Beispiel mit Code](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral: A Comprehensive AI Models Comparison](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Mistral Large vs DeepSeek-V3 Comparison](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)