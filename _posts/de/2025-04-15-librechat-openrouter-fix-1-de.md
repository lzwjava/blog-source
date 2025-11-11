---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Behebung des LibreChat OpenRouter Web-Suchfehlers
translated: true
type: note
---

Der Fehler **"404 No endpoints found that support tool use"** bei der Verwendung der Web-Suchfunktion in LibreChat mit OpenRouter ist ein bekanntes Problem. Hier ist die Erklärung und die Lösung:

---

## **Ursache des Problems**
- **Nicht alle Modelle bei OpenRouter unterstützen "Tool Use"** (wie Websuche, Function Calling, etc.) – nur eine bestimmte Auswahl. Wenn Sie ein Modell auswählen, das keine Tools unterstützt, erhalten Sie diesen 404-Fehler.
- OpenRouter erfordert, dass Sie **explizit ein Modell auswählen, das Tool-/Function Calling unterstützt**, damit Funktionen wie die Websuche funktionieren.
- Die Konfiguration von LibreChat kann Endpoints auch überschreiben, wenn sie nicht korrekt eingerichtet ist, was zu Routing-Problemen führt.

---

## **Problembehebung**

### 1. **Wählen Sie ein Modell mit Tool-Unterstützung**
- Gehen Sie zur [Modellliste von OpenRouter](https://openrouter.ai/models) und **filtern Sie in der Seitenleiste nach "tools"**. Nur Modelle mit Tool-Unterstützung funktionieren mit der Web-Suchfunktion von LibreChat.
- Empfohlene Modelle: Suchen Sie nach Modellen, die als "function calling" oder "tools" unterstützend gekennzeichnet sind (z. B. einige Versionen von GPT-4, Claude oder andere erweiterte Modelle).

### 2. **Aktualisieren Sie die LibreChat-Konfiguration**
- **Verwenden Sie `OPENROUTER_API_KEY` nicht** in Ihrer LibreChat-Konfiguration, da dies den OpenAI-Endpoint überschreiben und Konflikte verursachen kann.
- Stellen Sie in `librechat.yaml` sicher, dass Ihr OpenRouter-Endpoint korrekt konfiguriert ist und nicht durch "Ignored Providers" blockiert oder durch "Allowed Providers" eingeschränkt wird.

### 3. **Entfernen Sie Provider-Beschränkungen**
- Heben Sie in den OpenRouter-Einstellungen die Blockierung aller **"Ignored Providers"** auf und **leeren Sie "Allowed Providers"**, um sicherzustellen, dass LibreChat auf alle verfügbaren Endpoints zugreifen kann.

### 4. **Starten Sie LibreChat neu**
- Starten Sie LibreChat nach diesen Änderungen neu, um die neuen Einstellungen zu übernehmen.

---

## **Funktioniert es immer noch nicht?**
- Lesen Sie die [LibreChat-Dokumentation zu benutzerdefinierten Endpoints](https://www.librechat.ai/docs/quick_start/custom_endpoints) für eine erweiterte Einrichtung.
- Wenn das Problem weiterhin besteht, versuchen Sie, zur offiziellen OpenAI-API (falls verfügbar) oder zu einem anderen Anbieter zu wechseln, der Tool Use unterstützt.