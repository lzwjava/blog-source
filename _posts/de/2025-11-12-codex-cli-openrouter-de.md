---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration der Codex CLI für OpenRouter
translated: true
type: note
---

### Einrichten der Codex CLI-Konfiguration für OpenRouter

Codex CLI (von OpenAI) ist ein terminalbasierter Coding-Agent, der benutzerdefinierte Model-Provider wie OpenRouter über seine Konfigurationsdatei unterstützt. OpenRouter bietet eine OpenAI-kompatible API, sodass Sie Anfragen darüber routen können, indem Sie einen Provider mit der entsprechenden Basis-URL definieren. Dies ermöglicht den Zugriff auf eine breitere Palette von Modellen (z.B. von Anthropic, Google oder Open-Source-Providern) während Sie Codex verwenden.

Die Konfiguration wird in einer TOML-Datei unter `~/.codex/config.toml` gespeichert (erstellen Sie sie, falls sie nicht existiert). Sie definieren einen **Model-Provider**-Abschnitt für OpenRouter und verweisen dann in einem **Profil** auf bestimmte Modelle.

#### Schritt 1: Besorgen Sie sich Ihren OpenRouter API-Schlüssel
- Melden Sie sich bei [openrouter.ai](https://openrouter.ai) an, falls noch nicht geschehen.
- Generieren Sie einen API-Schlüssel in Ihrem Account-Dashboard.
- Setzen Sie ihn als Environment-Variable:  
  ```
  export OPENROUTER_API_KEY=Ihr_API_Schluessel_hier
  ```
  Fügen Sie dies zu Ihrem Shell-Profil hinzu (z.B. `~/.bashrc` oder `~/.zshrc`), um es dauerhaft zu speichern.

#### Schritt 2: Bearbeiten der Konfigurationsdatei
Öffnen Sie `~/.codex/config.toml` in Ihrem Editor und fügen Sie die folgenden Abschnitte hinzu. Dies setzt die Basis-URL auf den OpenRouter-Endpunkt (`https://openrouter.ai/api/v1`), der OpenAI-kompatibel ist (Codex hängt automatisch `/chat/completions` an).

```toml
# Definiere den OpenRouter-Provider
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # Liest aus Ihrer Env-Variable für die Authentifizierung

# Definiere ein Profil, das diesen Provider verwendet (Beispiel: Verwendung eines GPT-ähnlichen Modells)
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # Ersetzen Sie dies durch eine beliebige OpenRouter-Modell-ID, z.B. "anthropic/claude-3.5-sonnet"
```

- **Erklärte Schlüsselfelder**:
  - `base_url`: Zeigt auf den OpenRouter-API-Endpunkt. Dies überschreibt die standardmäßige OpenAI-Basis-URL.
  - `env_key`: Gibt die Env-Variable für den Bearer-Token-Auth-Header an.
  - `model`: Verwenden Sie exakte Modell-IDs von der [OpenRouter-Modellliste](https://openrouter.ai/models). Für Coding-Aufgaben probieren Sie "openai/codex-mini-latest" oder "meta-llama/llama-3.1-405b-instruct".
  - Sie können mehrere Profile für verschiedene Modelle hinzufügen (z.B. `[profiles.openrouter-claude]` mit `model = "anthropic/claude-3.5-sonnet"`).

#### Schritt 3: Verwenden der Konfiguration
- Installieren Sie Codex CLI falls nötig: `npm install -g @openai/codex` (oder via Homebrew: `brew install codex`).
- Führen Sie Codex mit Ihrem Profil aus:  
  ```
  codex --profile openrouter-gpt
  ```
  Oder setzen Sie ein Standardprofil in der Konfiguration:  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- Testen Sie es: Führen Sie `codex` aus und geben Sie eine einfache Coding-Aufforderung. Überprüfen Sie das OpenRouter-Dashboard auf die Nutzung.

#### Problembehandlung
- **Authentifizierungsfehler**: Stellen Sie sicher, dass `OPENROUTER_API_KEY` gesetzt und exportiert ist.
- **Modell nicht gefunden**: Überprüfen Sie die Modell-ID auf OpenRouter – sie ist case-sensitive und mit Präfix (z.B. "provider/model-name").
- **Versionsprüfung**: Verwenden Sie Codex CLI v0.13+ für volle Provider-Unterstützung. Aktualisieren Sie mit `npm update -g @openai/codex`.
- **Erweiterte Routing-Optionen**: Für OpenRouter-spezifische Features wie kostenoptimiertes Routing, fügen Sie optionale Parameter wie `provider = { sort = "price" }` unter dem Profil hinzu (unterstützt in neueren Versionen).

Dieses Setup hält Ihre Anfragen kompatibel mit der OpenAI-artigen API von Codex, während Sie das OpenRouter-Ökosystem nutzen. Weitere Details finden Sie in der [Codex CLI-Dokumentation auf npm](https://www.npmjs.com/package/@openai/codex) oder im [API-Leitfaden von OpenRouter](https://openrouter.ai/docs). Wenn Sie einen Fork wie Open Codex verwenden, ist die Konfiguration ähnlich, kann aber zusätzliche Gemini-Unterstützung haben.