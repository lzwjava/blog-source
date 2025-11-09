---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfiguration des GitHub Copilot LLM-Routers
translated: true
type: note
---

Um Ihren LLM-Router so zu konfigurieren, dass er ausschließlich die LLM-API von GitHub Copilot in einer Unternehmensumgebung verwendet, fügen Sie einen dedizierten Provider dafür hinzu und passen die Router-Einstellungen an, um den gesamten Datenverkehr über diesen Provider zu leiten.

-   **GitHub Copilot Provider hinzufügen**: Fügen Sie einen neuen Eintrag im "Providers"-Array mit der entsprechenden API-Basis-URL, Ihrem GitHub Personal Access Token (PAT) als API-Schlüssel und den unterstützten Modellen hinzu.
-   **Router-Standardwerte aktualisieren**: Ändern Sie alle Router-Felder (z.B. "default", "think"), so dass sie ausschließlich auf den neuen Provider-Namen verweisen, um sicherzustellen, dass keine anderen Provider aufgerufen werden.
-   **Unternehmensbeschränkungen beachten**: Verwenden Sie den PAT Ihres Enterprise-GitHub-Kontos mit den erforderlichen Scopes und nutzen Sie die vorhandene "PROXY_URL", wenn Ihre Umgebung aus Compliance-Gründen Proxy-Routing erfordert.
-   **Testen und Überprüfen**: Validieren Sie nach den Aktualisierungen, dass alle API-Aufrufe ausschließlich an den Copilot-Endpunkt gerichtet werden, um Richtlinien zu entsprechen, die nur Copilot-API-Interaktionen erlauben.

### Schritt-für-Schritt-Konfiguration
1.  **GitHub PAT generieren**: Melden Sie sich bei Ihrem GitHub Enterprise-Konto an und erstellen Sie ein Personal Access Token mit Scopes wie `copilot` für Chat-Zugriff oder `models:read` für breitere Modell-Inferenz. Dies gewährleistet eine sichere Authentifizierung, ohne umfassendere Berechtigungen preiszugeben.
2.  **Providers-Array modifizieren**: Hängen Sie ein neues Objekt an die "Providers"-Liste in Ihrer Konfigurations-JSON an. Setzen Sie "name" auf etwas Deskriptives wie "github_copilot", "api_base_url" auf "https://api.githubcopilot.com/chat/completions" (für Copilot Agents) oder "https://models.github.ai/inference/chat/completions" (für allgemeine GitHub Models Inferenz), "api_key" auf Ihren PAT und listen Sie kompatible Modelle auf.
3.  **Router-Abschnitt anpassen**: Ersetzen Sie alle Werte im "Router"-Objekt durch Ihren neuen Provider-Namen (z.B. "github_copilot"), um die ausschließliche Nutzung durchzusetzen. Dies verhindert ein Fallback auf andere Provider wie OpenRouter.
4.  **Unternehmensspezifische Überlegungen**: Bestätigen Sie in restriktiven Umgebungen, dass Ihre Netzwerkrichtlinien ausgehende Aufrufe an die GitHub-Domains erlauben. Aktualisieren Sie bei Bedarf die "PROXY_URL", um über einen genehmigten Unternehmensproxy zu routen. Aktivieren Sie die Protokollierung ("LOG": true), um Aufrufe zu überwachen und Compliance sicherzustellen.

### Beispiel einer aktualisierten Konfiguration
So könnte Ihre Konfiguration nach den Änderungen aussehen (ersetzen Sie die Platzhalter durch Ihren tatsächlichen PAT und bevorzugten Endpunkt):

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "z-ai/glm-4.6",
        "x-ai/grok-code-fast-1",
        "x-ai/grok-4-fast",
        "minimax/minimax-m2",
        "moonshotai/kimi-k2-thinking"
      ],
      "transformer": {
        "use": [
          "openrouter"
        ]
      }
    },
    {
      "name": "github_copilot",
      "api_base_url": "https://api.githubcopilot.com/chat/completions",
      "api_key": "ghp_YourPersonalAccessTokenHere",
      "models": [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620"
      ],
      "transformer": {
        "use": [
          "github_copilot"
        ]
      }
    }
  ],
  "Router": {
    "default": "github_copilot",
    "background": "github_copilot",
    "think": "github_copilot",
    "longContext": "github_copilot",
    "longContextThreshold": 30000,
    "webSearch": "github_copilot"
  }
}
```

Dieses Setup stellt sicher, dass der Router nur mit der Copilot-API interagiert und somit den Unternehmensrichtlinien entspricht, die Aufrufe auf genehmigte Endpunkte beschränken.

---

In Unternehmensumgebungen erfordert die Integration von LLM-APIs wie GitHub Copilot eine sorgfältige Konfiguration, um Sicherheitsrichtlinien einzuhalten, die ausgehende Aufrufe oft auf bestimmte genehmigte Dienste beschränken. Die bereitgestellte Router-Konfiguration scheint ein benutzerdefiniertes Setup für das Routing von LLM-Anfragen über verschiedene Provider zu sein, ähnlich wie Tools wie OpenRouter oder LiteLLM, wobei "Providers" API-Endpunkte und Modelle definieren und "Router" das Fallback- oder kategoriespezifische Routing festlegt. Um dies für die ausschließliche Nutzung der GitHub Copilot LLM-API anzupassen – und sicherzustellen, dass keine anderen externen Dienste aufgerufen werden – müssen Sie Copilot als Provider integrieren und dies über alle Router-Pfade hinweg durchsetzen. Dieser Ansatz unterstützt Szenarien, in denen Unternehmensfirewalls oder Compliance-Regeln nur GitHub-gehostete APIs erlauben, und nutzt die OpenAI-kompatible Schnittstelle von Copilot für Chat Completions.

GitHub Copilot bietet LLM-Zugang hauptsächlich über zwei Wege: den dedizierten Copilot-LLM-Endpunkt zum Erstellen von Agents und Extensions und die breitere GitHub Models API für allgemeine Inferenz. Der Copilot-spezifische Endpunkt unter `https://api.githubcopilot.com/chat/completions` ist für Enterprise-fähige Agent-Entwicklung maßgeschneidert und unterstützt POST-Anfragen im OpenAI Chat Completions-Format. Die Authentifizierung verwendet einen Bearer-Token, der von einem GitHub Personal Access Token (PAT) abgeleitet wird, typischerweise über einen `Authorization`-Header übergeben. Eine Beispielanfrage könnte beispielsweise Header wie `Authorization: Bearer <Ihr-PAT>` und `Content-Type: application/json` enthalten, mit einem Body, der `messages` (ein Array von User/System-Prompts) und optionale Parameter wie `stream: true` für Echtzeit-Antworten enthält. Modelle sind in der Dokumentation nicht explizit aufgeführt, stimmen aber mit Copilots zugrundeliegenden Providern wie GPT-4-Varianten und Claude-Modellen überein, wobei für Drittanbieter-Agents strikte Ratenbegrenzungen gelten, um Missbrauch zu verhindern.

Alternativ bietet die GitHub Models API unter `https://models.github.ai/inference/chat/completions` einen vielseitigeren Inferenz-Service, der Zugang zu einem Modell-Katalog nur mit GitHub-Anmeldedaten ermöglicht. Dies ist ideal für Prototyping und die Integration in Workflows wie GitHub Actions. Die Authentifizierung erfordert einen PAT mit dem Scope `models:read`, der über Ihre GitHub-Einstellungen (https://github.com/settings/tokens) erstellt wird. In Unternehmenssetups kann dies auf Organisationsebene erweitert oder in CI/CD-Pipelines verwendet werden, indem `permissions: models: read` zu Workflow-YAML-Dateien hinzugefügt wird. Verfügbare Modelle umfassen Industriestandards wie `openai/gpt-4o`, `openai/gpt-4o-mini`, `anthropic/claude-3-5-sonnet-20240620`, Metas Llama-3.1-Serie und Mistral-Varianten, die alle über das gleiche OpenAI-kompatible API-Format aufgerufen werden können. Diese Kompatibilität macht es einfach, sie in Ihre Router-Konfiguration einzubinden, ohne größere Änderungen am nachgelagerten Code vornehmen zu müssen.

Für unternehmensspezifische Konfigurationen verbessert GitHub Copilot Enterprise das Standard-Copilot mit organisationweiten Kontrollen, wie z.B. feinabgestimmten Modellen auf Basis Ihrer Codebase, aber der API-Zugriff folgt den gleichen Mustern. Das Netzwerkmanagement ist entscheidend: Sie können abonnementbasiertes Routing konfigurieren, um sicherzustellen, dass Copilot-Datenverkehr genehmigte Pfade verwendet, was erfordert, dass Benutzer ihre IDE-Erweiterungen (z.B. VS Code) auf Mindestversionen aktualisieren, die dies unterstützen. Wenn Ihre Umgebung Proxies vorschreibt, aktualisieren Sie die "PROXY_URL" in der Konfiguration auf Ihren Unternehmensproxy-Server und erwägen Sie benutzerdefinierte Zertifikate für SSL-Inspektion. Tools wie LiteLLM können als Zwischenproxy für weitere Kontrolle dienen – installieren Sie sie via `pip install litellm[proxy]`, definieren Sie Modelle in einer YAML-Konfiguration, starten Sie den Server auf einem lokalen Port und leiten Sie Copilot-Anfragen darüber für Protokollierung, Ratenbegrenzung und Fallback-Behandlung. Da Ihr Ziel jedoch Exklusivität ist, vermeiden Sie Fallbacks im Router, um der Richtlinie "nur Copilot-Aufrufe sind erlaubt" zu entsprechen.

Um dies in Ihrer Konfiguration zu implementieren, beginnen Sie damit, ein neues Provider-Objekt anzuhängen. Wählen Sie den Endpunkt basierend auf Ihrem Anwendungsfall: Verwenden Sie den Copilot-Agent-Endpunkt, wenn Sie Erweiterungen bauen, oder GitHub Models für allgemeines LLM-Routing. Listen Sie Modelle auf, die sich mit Ihren vorhandenen überschneiden (z.B. Claude- und GPT-Varianten), um Kompatibilität zu wahren. Überschreiben Sie dann alle "Router"-Felder, so dass sie nur auf diesen neuen Provider verweisen, und entfernen Sie Kommas oder Fallbacks wie ",minimax/minimax-m2". Aktivieren Sie die Protokollierung, um die Compliance zu überwachen, und testen Sie durch Simulieren von Anfragen, um zu überprüfen, dass keine unbefugten Endpunkte aufgerufen werden. Wenn Sie mit VS Code oder anderen IDEs integrieren, passen Sie Einstellungen wie `github.copilot.advanced.debug.overrideProxyUrl` an, um bei Bedarf über Ihren konfigurierten Proxy zu routen.

Hier ist eine Vergleichstabelle der beiden Haupt-GitHub-LLM-API-Optionen, die bei der Entscheidung hilft, welchen Endpunkt Sie in Ihrer Provider-Konfiguration verwenden sollten:

| Aspekt                   | GitHub Copilot LLM API (für Agents)               | GitHub Models API                                  |
|--------------------------|---------------------------------------------------|----------------------------------------------------|
| Endpunkt                 | https://api.githubcopilot.com/chat/completions    | https://models.github.ai/inference/chat/completions |
| Hauptverwendungszweck    | Erstellen von Copilot-Erweiterungen und Agents    | Allgemeines Prototyping, Inferenz und Workflows    |
| Authentifizierung        | Bearer PAT (über Authorization-Header)            | PAT mit models:read Scope                          |
| Unterstützte Modelle     | Implizit (z.B. GPT-4, Claude-Varianten)           | Expliziter Katalog: gpt-4o, claude-3-5-sonnet, Llama 3.1, etc. |
| Enterprise-Features      | Ratenbegrenzung für Drittanbieter; Integration mit Copilot Enterprise | Nutzbar in GitHub Actions; Bring-Your-Own-Key-Unterstützung |
| Ratenbegrenzungen/Kontingente | Streng für Nicht-GitHub-Agents                  | Free-Tier für Prototyping; skalierbar für Enterprise |
| Kompatibilität           | OpenAI Chat-Format                                | OpenAI-kompatibel; einfache Router-Integration     |

Diese Tabelle hebt hervor, warum GitHub Models für breitere Router-Nutzung vorzuziehen sein könnte, da es explizitere Modellauswahl und Enterprise-Workflow-Integration bietet.

Mögliche Herausforderungen sind das Ablaufen von Tokens (PATs halten typischerweise 30-90 Tage), also automatisieren Sie die Erneuerung in Unternehmensskripten. Wenn Ihre Umgebung GitHub Enterprise Cloud verwendet, aktivieren Sie Copilot auf Organisationsebene für nahtlosen Zugang. Für erweiterte Setups erkunden Sie Bring-Your-Own-API-Keys (BYOK) in GitHub Models, um über bevorzugte Provider zu routen und dennoch innerhalb des GitHub-Ökosystems zu bleiben. Priorisieren Sie stets die primäre GitHub-Dokumentation für die neuesten Scopes und Endpunkte, da sich die Features schnell weiterentwickeln. Wenn direkte API-Aufrufe aufgrund von Netzwerkbeschränkungen fehlschlagen, erwägen Sie die Verwendung von GitHub's Proxy-Konfigurationsoptionen oder die Integration mit Azure für hybride Enterprise-Bereitstellungen.

Zusammenfassend transformiert diese Konfiguration Ihren Router in ein Copilot-exklusives System, das sich mit Unternehmensrichtlinien deckt und gleichzeitig die Funktionalität für codebezogene oder allgemeine LLM-Aufgaben beibehält.

**Wichtige Quellen:**
-   [Using GitHub Copilot's LLM for your agent](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-extensions/build-a-copilot-agent/use-copilots-llm)
-   [Quickstart for GitHub Models](https://docs.github.com/en/github-models/quickstart)
-   [GitHub Copilot | liteLLM](https://docs.litellm.ai/docs/tutorials/github_copilot_integration)
-   [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/enterprise-cloud%40latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/manage-network-access)
-   [Configuring network settings for GitHub Copilot](https://docs.github.com/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot)
-   [Prototyping with AI models](https://docs.github.com/github-models/prototyping-with-ai-models)
-   [Using your own API keys in GitHub Models](https://docs.github.com/en/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)