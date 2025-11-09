---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Integriere DeepSeek mit LibreChat Anleitung
translated: true
type: note
---

Hier ist der schnellste Weg, um **DeepSeek in LibreChat zum Laufen zu bringen**. Ich zeige zwei Optionen – verwende die **offizielle DeepSeek API** (empfohlen) oder gehe über **OpenRouter**.

---

## Option A — Verwende die offizielle DeepSeek API (empfohlen)

1. **Hole dir einen DeepSeek API-Schlüssel**
   Erstelle einen in deinem DeepSeek-Konto und notiere dann die Basis-URL:
   `https://api.deepseek.com` (oder die OpenAI-kompatible `https://api.deepseek.com/v1`). ([DeepSeek API Docs][1], [deepseek.apidog.io][2])

2. **Füge einen DeepSeek-Endpunkt in `librechat.yaml` hinzu**
   Füge dies unter `endpoints:` → `custom:` ein:

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3 (allgemein)
      - deepseek-coder       # code-zentriert
      - deepseek-reasoner    # R1 Reasoning
  titleConvo: true
  dropParams: null
```

LibreChat liefert eine **DeepSeek**-Konfigurationsanleitung und bestätigt die Modellnamen (`deepseek-chat`, `deepseek-coder`, `deepseek-reasoner`) sowie Hinweise dazu, dass R1 seinen "Gedankenprozess" streamen kann. ([LibreChat][3])

3. **Lege den API-Schlüssel über `.env` offen**
   In deiner LibreChat `.env`-Datei:

```
DEEPSEEK_API_KEY=sk-...
```

LibreChat unterstützt benutzerdefinierte OpenAI-kompatible Anbieter über `librechat.yaml` + `.env`. ([LibreChat][4])

4. **Starte deinen Stack neu**
   Aus deinem LibreChat-Ordner:

```bash
docker compose down
docker compose up -d --build
```

(Erforderlich, damit der API-Container `librechat.yaml` und `.env` neu lädt.) Wenn deine benutzerdefinierten Endpunkte nicht erscheinen, überprüfe die `api`-Container-Logs auf Konfigurationsfehler. ([GitHub][5])

---

## Option B — Verwende DeepSeek über OpenRouter

Wenn du OpenRouter bereits verwendest, registriere einfach die DeepSeek-Modelle in einem OpenRouter-Endpunktblock.

`librechat.yaml`:

```yaml
- name: openrouter
  apiKey: ${OPENROUTER_KEY}
  baseURL: https://openrouter.ai/api/v1
  models:
    default: deepseek/deepseek-chat
    list:
      - deepseek/deepseek-chat
      - deepseek/deepseek-coder
      - deepseek/deepseek-reasoner
```

Zwei wichtige Hinweise aus der LibreChat-Dokumentation:
• Setze nicht den Umgebungsvariablennamen `OPENROUTER_API_KEY` (verwende einen anderen Namen wie `OPENROUTER_KEY`), sonst überschreibst du versehentlich den OpenAI-Endpunkt.
• OpenRouter ist erstklassig in LibreChats Liste der benutzerdefinierten Endpunkte. ([LibreChat][6])

OpenRouter stellt DeepSeek-Modelle über eine OpenAI-kompatible Oberfläche bereit. ([OpenRouter][7])

---

## Tipps & Fallstricke

*   **R1 / `deepseek-reasoner`**: Es kann seinen Chain-of-Thought ("Gedankenprozess") streamen. Einige OpenAI-Parameter sind möglicherweise nicht anwendbar. Wenn du seltsame Ausgaben siehst, teste zuerst mit `deepseek-chat`. ([LibreChat][3])
*   **Modell-Abruf**: Die Einstellung `fetch: true` ermöglicht es LibreChat, die neueste Modellliste abzurufen, wenn dies unterstützt wird; andernfalls wird die von dir angegebene `list:` verwendet. ([LibreChat][8])
*   **Wo diese Einstellungen gespeichert sind**: `librechat.yaml` ist die Datei für benutzerdefinierte Endpunkte; `.env` enthält Schlüssel und Proxy-Einstellungen. ([LibreChat][8])

Wenn du möchtest, füge deine aktuelle `librechat.yaml` ein, und ich werde sie sauber um DeepSeek erweitern (keine Tabellen, versprochen).

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"