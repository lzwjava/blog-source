---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Großsprachmodelle, Codeverständnis und Werkzeugnutzung
translated: true
type: note
---

Gute Frage! Du fragst im Grunde, wie etwas wie **Anthropic's Claude (und ähnliche LLMs)** intern folgendes handhabt:

1.  **Code-Ausführung oder codebezogene Schlussfolgerungen**
2.  **JSON-Schema-Prüfung/Validierung strukturierter Ausgaben**
3.  **Tool-Nutzung und Routing zwischen Tools**

Lass mich das im Detail aufschlüsseln.

---

### 1. Code-Schlussfolgerungen & Ausführung
Claude (und andere fortschrittliche LLMs) führen Code nicht direkt im Modell aus – sie **simulieren Code-Schlussfolgerungen**, indem sie Token für Code oder logische Schritte vorhersagen.

- Im **normalen Textmodus** kann Claude Code "schreiben", indem es ein Muster fortsetzt, führt ihn aber nicht intern aus.
- Wenn es mit einem **Backend (wie Anthropic's Workbench oder OpenAI's Code Interpreter)** verwendet wird, kann das System diese Code-Schnipsel abfangen und sie dann tatsächlich in einer sandboxed Umgebung *ausführen*.
- Die Ergebnisse können dann dem Modell als Kontext zurückgegeben werden, sodass es Schlussfolgerungen wie folgt verketten kann:
  → Code generieren → Extern ausführen → Ausgabe erhalten → Nächsten Schritt entscheiden.

Die Intelligenz liegt also in der Schleife: LLM generiert → externer Runner führt aus → LLM interpretiert Ergebnisse.

---

### 2. JSON-Schema-Prüfung
Viele APIs (Claude, OpenAI, etc.) unterstützen nun den **strukturierten Ausgabemodus**, bei dem man ein JSON-Schema anhängen kann. So funktioniert das intern:

- Man übergibt eine **JSON-Schema-Definition** mit der Anfrage.
- Das LLM wird angeleitet, **ausschließlich gültiges JSON** auszugeben, das konform ist.
- Wenn es versucht, ungültiges JSON auszugeben, erkennt das System dies (mit einem Validator wie [jsonschema](https://pypi.org/project/jsonschema/)) und fordert das Modell auf, die Ausgabe zu "reparieren".
- Hinter den Kulissen ist dies oft ein **Constrained Decoding** oder **Grammar-Based Decoding** Mechanismus – im Grunde wird die Token-Generierung so eingeschränkt, dass nur `"gültige nächste Token im Schema"` erlaubt sind.

Dies stellt sicher, dass die Ausgabe syntaktisch und semantisch korrektes JSON ist, was für die Automatisierung der Tool-Nutzung entscheidend ist.

---

### 3. Tool-Nutzung & Routing
Die Tool-Nutzung wird über eine Art **Router-Ebene** zwischen dem LLM und einer Tool-Ausführungsumgebung abgewickelt:

- **Routing-Logik**: Das Modell wird aufgefordert zu *entscheiden, welches Tool aufgerufen werden soll* (oder direkt zu antworten).
- **Schema-Durchsetzung**: Jedes Tool hat ein Eingabeschema. Das LLM muss gültiges JSON für dieses Tool erzeugen.
- **Ausführungs-Adapter**: Die Orchestrierungsebene (außerhalb des Modells) nimmt das JSON des LLM, validiert es gegen das Schema, führt das Tool aus und speist die Ergebnisse dann als Kontext zurück.
- **Verkettete Schlussfolgerungen (ReAct-Stil)**: Das LLM "denkt laut" (könnte dem Benutzer verborgene Denkschritte produzieren), gibt dann bei Bedarf Tool-Aufrufe aus und gelangt schrittweise zu einer endgültigen Antwort.

Zum Beispiel:
```json
{
  "tool": "web_search",
  "query": "neueste Forschung zu Quantenfehlerkorrektur"
}
```
→ Der Router sieht `"tool": "web_search"`, validiert das Schema, führt die Websuche aus, fügt die Ergebnisse zurück in den Kontext des Modells ein, und das Modell setzt seine Schlussfolgerungen fort.

Anthropic's Claude, OpenAI's GPTs, LangChain und andere unterstützen alle dieses Muster.

---

### 🔑 Zusammenfassung
- **Claude Code**: Führt Code nicht intern aus; generiert Code → Sandbox führt aus → Ergebnisse werden zurückgegeben → Iteratives Schließen.
- **JSON-Schema-Prüfung**: Verwendet Constrained Decoding / Schema-Validierung, um eine gültige strukturierte Ausgabe zu gewährleisten.
- **Tool-Use-Routing**: LLM wählt Tool-Aufrufe in JSON aus, die Orchestrierungs-Engine validiert & führt sie aus, speist Ergebnisse in einer Schleife zurück.

---

👉 Möchtest du, dass ich **ein Diagramm zeichne**, das den Ablauf (LLM ↔ Tool-Router ↔ Schema-Validator ↔ Ausführungs-Engine) zeigt, damit es visuell klarer wird?