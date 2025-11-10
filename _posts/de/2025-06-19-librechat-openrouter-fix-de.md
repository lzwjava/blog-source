---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Behebung des LibreChat OpenRouter Modellfehlers
translated: true
type: note
---

Dieser Fehler tritt auf, wenn **LibreChat** mit **OpenRouter** als Backend verwendet wird und das ausgewählte Modell (`gpt-5-chat` oder ähnlich) nicht verfügbar ist oder nicht korrekt weitergeleitet wird. Hier ist eine Aufschlüsselung des Problems und wie es behoben werden kann:

---

## **Warum dieser Fehler auftritt**
- **OpenRouter** fungiert als Proxy für verschiedene KI-Modelle, aber nicht alle Modelle sind standardmäßig verfügbar oder aktiviert.
- Der Fehler `404 No endpoints found that support tool use` bedeutet, dass das von Ihnen ausgewählte Modell (`gpt-5-chat`) entweder:
  - Von OpenRouter nicht unterstützt wird.
  - Nicht in Ihrem LibreChat-Setup konfiguriert ist.
  - Einen anderen Anbieter oder einen anderen API-Schlüssel erfordert.

---

## **Wie man es behebt**

### 1. **Verfügbare Modelle in OpenRouter prüfen**
- Besuchen Sie die [Modellliste von OpenRouter](https://openrouter.ai/models), um zu sehen, welche Modelle verfügbar sind.
- Derzeit ist `gpt-5-chat` kein offizielles OpenAI-Modell (das neueste ist GPT-4o). Wenn Sie GPT-4 meinen, verwenden Sie `openai/gpt-4` oder ähnliches.

### 2. **LibreChat-Konfiguration aktualisieren**
- Gehen Sie in LibreChat zu **Einstellungen** > **Modellauswahl**.
- Wählen Sie ein Modell, das **von OpenRouter unterstützt wird** (z.B. `openai/gpt-4`, `mistralai/mistral-7b`, etc.).
- Wenn Sie OpenAI direkt verwenden möchten, wechseln Sie den **API-Anbieter** zu **OpenAI** anstelle von OpenRouter.

### 3. **API-Schlüssel überprüfen**
- Stellen Sie sicher, dass Sie einen gültigen **OpenRouter API-Schlüssel** (bei Verwendung von OpenRouter) oder einen **OpenAI API-Schlüssel** (bei Verwendung von OpenAI) haben.
- Fügen Sie den Schlüssel in LibreChats **Einstellungen** > **API-Schlüssel** hinzu.

### 4. **LibreChat neu starten**
- Starten Sie LibreChat nach dem Ändern der Einstellungen neu, um die Änderungen zu übernehmen.

### 5. **LibreChat-Dokumentation prüfen**
- Konsultieren Sie die [OpenRouter-Einrichtungsanleitung von LibreChat](https://github.com/danny-avila/LibreChat#openrouter) für detaillierte Anweisungen.

---

## **Alternative Lösungen**
- Wenn Sie die Modelle von OpenAI verwenden möchten, stellen Sie den Anbieter auf **OpenAI** ein und wählen Sie `gpt-4`, `gpt-4o` oder `gpt-3.5-turbo`.
- Wenn Sie OpenRouter verwenden möchten, wählen Sie ein Modell aus deren [Liste der unterstützten Modelle](https://openrouter.ai/models).

---