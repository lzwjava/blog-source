---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung von Claude Code DeepSeek Konfigurationsrouting
translated: true
type: note
---

Verstanden. Deine Konfiguration sendet **Claude Codes Anthropic-artigen Traffic** an **OpenRouters OpenAI-artigen Endpunkt** für DeepSeek V3.1. Wenn Claude Code (der IDE-Agent) versucht, tools/plan/stream zu verwenden, stimmen die Nachrichtenschemata nicht überein → Fehler.

Unten findest du eine saubere Methode, dies so zu verkabeln, dass **Anthropic-Modelle** weiterhin ein Anthropic-artiges Gateway verwenden, während **DeepSeek V3.1** (OpenAI-artig) bei `/chat/completions` bleibt. Ich zeige dir die genauen Änderungen, die du übernehmen kannst.

---

### 1) Überprüfe den DeepSeek V3.1 Slug

Der Chat-Model-Slug von OpenRouter lautet:

```
deepseek/deepseek-chat-v3.1
```

(Das ist das Instruct/Chat-Modell – zu unterscheiden vom "Base"-Modell.) ([OpenRouter][1])

---

### 2) Füge einen Anthropic-format Proxy für Claude Code hinzu

Claude Code erwartet **Anthropic Messages** (`/messages`, `tool_use`-Blöcke). Die einfachste Lösung ist, einen kleinen Proxy zu betreiben, der Anthropic→OpenAI (OpenRouter) konvertiert und zurück. Es gibt einen fertigen: **maxnowack/anthropic-proxy**. Starte ihn wie folgt (Umgebungsvariable ist dein OpenRouter-Key):

```bash
OPENROUTER_API_KEY=DEIN_KEY npx anthropic-proxy
```

Er hört lokal ab und übersetzt die Schemata für dich. ([GitHub][2])

Füge nun einen **zweiten Provider** hinzu, der den Claude Code Traffic zu diesem Proxy leitet.

#### 🔧 Ersetze dein JSON mit diesen fokussierten Änderungen

**Füge diesen Provider hinzu (behalte deinen aktuellen `openrouter` Provider unverändert):**

```json
{
  "name": "anthropic-proxy",
  "api_base_url": "http://127.0.0.1:3000/v1/messages",
  "api_key": "",
  "models": [
    "anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4"
  ]
}
```

**Behalte deinen bestehenden OpenRouter-Provider (es ist korrekt, `/chat/completions` für DeepSeek und andere OpenAI-Schema-Modelle zu verwenden).** OpenRouter normalisiert zu einem OpenAI-kompatiblen Schema und unterstützt Extras wie Reasoning-Tokens, Tools etc. ([OpenRouter][3])

---

### 3) Leite Modelle zum richtigen Provider

Weise Anthropic-Modelle dem **anthropic-proxy** zu; weise DeepSeek/GPT/Gemini/Qwen dem **openrouter** zu.

Beispiel-Router-Block, den du übernehmen kannst:

```json
"Router": {
  "default": "openrouter,openai/gpt-5-mini",

  "background": "openrouter,google/gemini-2.5-flash",
  "think": "openrouter,qwen/qwen3-coder",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "longContextThreshold": 2000,
  "webSearch": "openrouter,mistralai/mistral-medium-3.1",

  "overrides": {
    "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",

    "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
  }
}
```

> Falls dein Router keine `overrides`-Map unterstützt, ist das Äquivalent: Erstelle separate "Profile" in deiner App (z.B. "Claude Code via anthropic-proxy" vs. "General chat via openrouter") und wähle das Profil pro Aktion.

---

### 4) Vermeide Reasoning-Stream-Kollisionen bei DeepSeek (optional, aber sicherer)

DeepSeek V3.1 unterstützt **"Thinking"-Tokens**. Viele Wrapper stolpern, wenn diese mitten im Stream erscheinen. Auf OpenRouter kannst du **Reasoning ausschließen** mit einem Request-Flag. Wenn dein Router pro-Model-Parameter setzen lässt, füge hinzu:

```json
"params": {
  "reasoning": { "exclude": true }
}
```

(oder `include_reasoning: false`, abhängig von der Parameternamen-Konvention deines Routers). Dies verhindert, dass `