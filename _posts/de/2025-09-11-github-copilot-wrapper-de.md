---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Inoffizieller Python-Wrapper für GitHub Copilot
translated: true
type: note
---

Das **GitHub-Repository [ericc-ch/copilot-api](https://github.com/ericc-ch/copilot-api)** ist ein **inoffizieller Python-Wrapper** für die Interaktion mit der **GitHub Copilot API** (dem KI-gestützten Code-Vervollständigungstool). Es ermöglicht Entwicklern, programmgesteuert Code-Vorschläge, Vervollständigungen und Erklärungen unter Verwendung der Copilot-Backend-Infrastruktur zu generieren, ohne sich auf die offizielle VS Code-Erweiterung oder andere IDE-Integrationen zu verlassen.

---

## **Wofür wird es verwendet?**
Dieser API-Wrapper kann verwendet werden, um:
1. **Code-Vervollständigungen** zu generieren (wie in VS Code, aber programmgesteuert).
2. **Erklärungen** für Code-Snippets zu erhalten.
3. **Copilot in benutzerdefinierte Anwendungen** zu integrieren (z.B. CLI-Tools, Web-Apps oder automatisierte Workflows).
4. **Mit Copilot-Antworten zu experimentieren**, ohne eine IDE zu benötigen.
5. **Rate Limits zu umgehen** (bei vorsichtiger Verwendung, was jedoch gegen die GitHub-Nutzungsbedingungen verstoßen kann).

⚠️ **Warnung:**
- Dies ist eine **inoffizielle** API, was bedeutet, dass GitHub den Zugriff jederzeit ändern oder blockieren könnte.
- Die Nutzung könnte **gegen die GitHub Copilot Nutzungsbedingungen** verstoßen, wenn sie ohne Genehmigung für Automatisierung oder kommerzielle Zwecke verwendet wird.
- **Rate Limits gelten** (GitHub könnte Konten bei übermäßigen Anfragen sperren).

---

## **Wie wird es verwendet?**
### **1. Installation**
Klonen Sie das Repository und installieren Sie die Abhängigkeiten:
```bash
git clone https://github.com/ericc-ch/copilot-api.git
cd copilot-api
pip install -r requirements.txt
```

### **2. Authentifizierung**
Sie benötigen ein **GitHub Copilot-Token** (nicht dasselbe wie ein persönliches GitHub-Zugriffstoken).
#### **Wie erhält man ein Copilot-Token?**
1. **Über Browser-DevTools (Empfohlen)**
   - Öffnen Sie **VS Code** mit aktiviertem Copilot.
   - Öffnen Sie die **Developer Tools** (`F12` oder `Strg+Umschalt+I`).
   - Gehen Sie zum Tab **Network**.
   - Filtern Sie nach `copilot`-Anfragen.
   - Suchen Sie nach einer Anfrage an `https://api.github.com/copilot_internal/v2/token`.
   - Kopieren Sie das **Authorization-Token** aus der Antwort.

2. **Über ein Skript (falls verfügbar)**
   Einige Forks dieses Repos beinhalten ein Token-Extraktor-Skript.

#### **Token in Python setzen**
```python
from copilot import Copilot

copilot = Copilot(
    auth_token="IHR_COPILOT_TOKEN",  # Von den DevTools
    proxy="http://ihr-proxy:port"    # Optional (wenn hinter einem Proxy)
)
```

---

### **3. Grundlegende Verwendungsbeispiele**
#### **Code-Vervollständigungen abrufen**
```python
response = copilot.get_completion(
    prompt="def calculate_factorial(n):",
    language="python",
    n=3  # Anzahl der Vorschläge
)
print(response)
```
**Beispielausgabe:**
```python
[
    "def calculate_factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * calculate_factorial(n-1)",
    "def calculate_factorial(n):\n    result = 1\n    for i in range(1, n+1):\n        result *= i\n    return result",
    "def calculate_factorial(n):\n    return 1 if n <= 1 else n * calculate_factorial(n - 1)"
]
```

#### **Code-Erklärung abrufen**
```python
explanation = copilot.explain_code(
    code="def factorial(n): return 1 if n <= 1 else n * factorial(n - 1)",
    language="python"
)
print(explanation)
```
**Beispielausgabe:**
```
Dies ist eine rekursive Funktion zur Berechnung der Fakultät einer Zahl `n`.
- Wenn `n` 0 oder 1 ist, gibt sie 1 zurück (Basisfall).
- Andernfalls gibt sie `n * factorial(n-1)` zurück, wodurch das Problem in kleinere Teilprobleme zerlegt wird.
```

#### **Mit Copilot chatten (falls unterstützt)**
Einige Versionen ermöglichen konversationelle Interaktionen:
```python
response = copilot.chat(
    message="Wie sortiere ich eine Liste in Python?",
    context="python"
)
print(response)
```

---

### **4. Erweiterte Verwendung**
#### **Verwendung in einem benutzerdefinierten CLI-Tool**
```python
import argparse
from copilot import Copilot

parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, required=True)
parser.add_argument("--language", type=str, default="python")
args = parser.parse_args()

copilot = Copilot(auth_token="IHR_TOKEN")
completions = copilot.get_completion(args.prompt, args.language, n=3)

for i, code in enumerate(completions, 1):
    print(f"--- Vorschlag {i} ---")
    print(code)
    print()
```

#### **Integration mit FastAPI (Web-App)**
```python
from fastapi import FastAPI
from copilot import Copilot

app = FastAPI()
copilot = Copilot(auth_token="IHR_TOKEN")

@app.get("/complete")
def complete_code(prompt: str, language: str = "python"):
    return copilot.get_completion(prompt, language, n=1)
```

---

## **Einschränkungen & Risiken**
✅ **Vorteile:**
- Funktioniert ohne VS Code.
- Kann in benutzerdefinierte Workflows integriert werden.
- Nützlich für Automatisierung (falls erlaubt).

❌ **Nachteile:**
- **Inoffizielle API** (kann jederzeit brechen).
- **Rate Limits** (GitHub könnte Ihr Konto sperren).
- **Ethische Bedenken** (prüfen Sie die GitHub-Nutzungsbedingungen vor der Verwendung).
- **Kein offizieller Support**.

---

## **Alternativen**
Wenn Sie einen **legalen** Weg suchen, Copilot programmgesteuert zu nutzen:
1. **Offizielle GitHub Copilot CLI** (falls in Zukunft veröffentlicht).
2. **GitHub Copilot Labs** (experimentelle Erweiterungen).
3. **Andere KI-Code-Assistenten** (z.B. **Amazon CodeWhisperer**, **TabNine**, **Sourcegraph Cody**).

---

## **Abschließende Gedanken**
Dieses Repository ist nützlich für **Experimente** und um zu **lernen, wie Copilot intern funktioniert**, aber **verwenden Sie es verantwortungsbewusst**. Wenn Sie ein Produktionstool entwickeln, sollten Sie in Betracht ziehen, auf eine offizielle API zu warten oder genehmigte Alternativen zu verwenden.

Benötigen Sie Hilfe mit einem bestimmten Anwendungsfall? 🚀