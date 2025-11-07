---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von Authentifizierungsfehlern der Übersetzungs-API
translated: true
---

### Analyse des Workflows und der Fehlerursache

Ihr GitHub Actions Workflow für "Translate Recent Notes" ist insgesamt gut strukturiert – er checkt das Repo aus, richtet Python ein, installiert Abhängigkeiten, führt ein Übersetzungsskript für die N neuesten Beiträge aus und committed Änderungen in `_notes/`. Basierend auf den zuvor geteilten Logs (mit den 401-Fehlern während der Übersetzung in Sprachen wie ar, de, fr, etc.) liegt das Problem jedoch in der Authentifizierung für die API-Aufrufe der Übersetzungs-API innerhalb von `scripts/translation/update_lang_notes.py`.

#### Grundursache
- Der Fehler `"No cookie auth credentials found"` (HTTP 401) ist spezifisch für die **OpenRouter API** (oder einen Python-Client/eine Bibliothek, die mit ihr interagiert, wie LiteLLM oder ein inoffizielles SDK). Dies tritt auf, wenn der API-Request keine korrekten Authentifizierungs-Header enthält.
- OpenRouter erwartet `Authorization: Bearer <ihr_openrouter_api_key>` in Requests. Wenn der Schlüssel nicht korrekt übergeben wird, fallen einige Clients auf (oder interpretieren die Notwendigkeit einer) cookie-basierten Sitzungsauthentifizierung zurück, was genau diesen Fehler auslöst.
- In Ihrem Workflow:
  - Sie setzen `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}`, was einen Secret-Wert an die Umgebung des Skripts übergibt.
  - Aber das Skript liest/verwendet diese Umgebungsvariable wahrscheinlich nicht korrekt. Typische Fehlanpassungen:
    - Das Skript erwartet `OPENAI_API_KEY` (für OpenAI-kompatible Endpoints wie OpenRouter).
    - Oder es verwendet eine Bibliothek (z.B. das `openai` Python SDK), ohne die Basis-URL auf `https://openrouter.ai/api/v1` zu setzen.
    - Der Secret `DEEPSEEK_API_KEY` könnte tatsächlich Ihren **OpenRouter API-Schlüssel** enthalten (der zu DeepSeek/Grok-Modellen weitergeleitet wird), aber wenn es ein direkter DeepSeek-Schlüssel ist, funktioniert er nicht für OpenRouter.
- Aus den Logs geht hervor, dass das Skript das Modell `'x-ai/grok-4-fast'` (Grok 4 via OpenRouter) verwendet und Front Matter/Titel erfolgreich verarbeitet, aber bei der Inhaltsübersetzung pro Sprache fehlschlägt.
- Dies ist kein GitHub Actions Problem – es liegt am API-Client-Setup im Python-Skript. Der Workflow fährt mit dem Commit-Schritt fort (daher der `git config user.name "github-actions[bot]"` Log), aber ohne Übersetzungen werden nur englische Dateien hinzugefügt.

#### Empfohlene Lösungen
1. **Umgebungsvariablen im Workflow aktualisieren**:
   - An gängige OpenRouter-Setups (OpenAI-kompatibel) anpassen. Ändern Sie den `env`-Block im "Translate posts" Schritt zu:
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # Variable umbenennen in das, was das Skript erwartet
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # Erforderlich für das Routing zu OpenRouter
     ```
   - Wenn `DEEPSEEK_API_KEY` Ihr OpenRouter-Schlüssel ist, gut. Wenn es ein direkter DeepSeek-Schlüssel ist, erstellen Sie einen neuen Secret `OPENROUTER_API_KEY` in den Repository-Einstellungen mit Ihrem tatsächlichen OpenRouter-Schlüssel (holen Sie sich einen unter [openrouter.ai/keys](https://openrouter.ai/keys)).
   - Test: Fügen Sie `echo $OPENAI_API_KEY` (zensiert) zum Run-Step hinzu, um das Debugging in den Logs zu ermöglichen.

2. **Das Python-Skript (`update_lang_notes.py`) reparieren**:
   - Stellen Sie sicher, dass es den OpenAI-Client wie folgt initialisiert (angenommen, `openai`-Bibliothek):
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # Standardmäßig OpenAI, falls nicht gesetzt
     )

     # Dann client.chat.completions.create(..., model="x-ai/grok-4-fast") verwenden
     ```
   - Wenn Sie LiteLLM verwenden (üblich für Multi-Provider): Installieren Sie es, falls nicht in `requirements.txt` enthalten, und rufen Sie `completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)` auf.
   - Für die Übersetzungsschleife: Fügen Sie eine Fehlerbehandlung pro Sprache hinzu (z.B. `try/except` um API-Aufrufe, protokollieren Sie Fehler, überspringen Sie bei 401).
   - Cookies explizit handhaben? Wahrscheinlich nicht nötig – bleiben Sie bei API-Schlüsseln. Wenn das Skript Browser/Selenium-Code enthält, entfernen Sie ihn für die Zuverlässigkeit der CI.

3. **Workflow-Verbesserungen**:
   - **Eingabevalidierung**: Fügen Sie eine Prüfung für N=0 oder ungültiges `--n` hinzu, um zu vermeiden, dass nichts verarbeitet wird.
   - **Bedingter Commit**: Ihr `git diff --cached --quiet || git commit` ist gut, aber aktualisieren Sie die Nachricht, um alle Sprachen widerzuspiegeln: `-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`.
   - **Caching**: Fügen Sie `actions/cache` für `pip` hinzu, um Installationen zu beschleunigen.
   - **Debug-Modus**: Fügen Sie eine optionale Eingabe `debug: true` und ein `--debug`-Flag zum Skript für ausführliche Protokollierung hinzu.
   - **Berechtigungen**: Stellen Sie sicher, dass die `github-pages`-Umgebung Lese-/Schreibzugriff hat, falls benötigt.
   - Vollständiges aktualisiertes YAML-Snippet für den "Translate posts" Schritt:
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **Testschritte**:
   - **Lokaler Test**: Führen Sie `python scripts/translation/update_lang_notes.py --n 1` lokal mit exportierten Umgebungsvariablen aus (z.B. `export OPENAI_API_KEY=ihr_schluessel`).
   - **Workflow-Test**: Lösen Sie ihn mit `workflow_dispatch` und N=1 aus, überprüfen Sie die Logs auf API-Aufrufe.
   - **Secret verifizieren**: Bestätigen Sie in den Repository-Einstellungen > Secrets, dass `DEEPSEEK_API_KEY` einen gültigen OpenRouter-Schlüssel hat (beginnt mit `sk-or-...`).
   - Wenn es immer noch fehlschlägt, fügen Sie `--verbose` zum Skript hinzu und inspizieren Sie die Request-Header (z.B. via `print(client.api_key)`).

Dies sollte die 401er beheben und die Übersetzungen zum Laufen bringen. Wenn Sie Ausschnitte aus `update_lang_notes.py` teilen (z.B. die API-Client-Initialisierung), kann ich genauer eingrenzen.

#### Referenzen
- [OpenRouter Quickstart (API Auth Setup)](https://openrouter.ai/docs/quickstart)
- [LiteLLM OpenRouter Integration](https://docs.litellm.ai/docs/providers/openrouter) (falls verwendet)
- [GitHub Issue zu ähnlichem OpenRouter Auth Fehler](https://github.com/mendableai/firecrawl/issues/1352)
- [Reddit Thread zu OpenRouter 401 Fehlern](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)