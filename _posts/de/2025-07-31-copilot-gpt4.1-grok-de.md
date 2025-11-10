---
audio: false
generated: true
image: false
lang: de
layout: post
title: Konfiguration von Copilot für benutzerdefinierte Modelle
translated: true
type: note
---

Wenn Sie in GitHub Copilot "verwaltete Modelle" auswählen und weiterhin GPT-4.1 als Standard sehen oder die Grok- oder Kimi-Modelle von OpenRouter nicht wie erwartet nutzen können, gibt es einige mögliche Gründe und Schritte, um dies zu beheben. Hier ist eine Aufschlüsselung des Problems und wie Sie Copilot so konfigurieren, dass es Grok- oder Kimi-Modelle über OpenRouter verwendet:

### Warum GPT-4.1 weiterhin verwendet wird
1.  **Standardmodell-Einstellung**: GitHub Copilot verwendet standardmäßig GPT-4.1 für Copilot Chat, Edits und den Agent Mode, sofern dies nicht explizit geändert wird. Selbst wenn Sie "verwaltete Modelle" auswählen, kann das Standardmodell bestehen bleiben, wenn Sie die OpenRouter-Integration nicht vollständig konfiguriert oder ein bestimmtes Modell ausgewählt haben.[](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
2.  **Kontextspezifische Modellnutzung**: Das "Fix Box" (Inline-Chat oder Code-Vervollständigung) in Copilot unterstützt möglicherweise in bestimmten Kontexten nicht den Wechsel zu benutzerdefinierten Modellen wie Grok oder Kimi. Beispielsweise könnte das Copilot Chat-Panel oder Inline-Vorschläge das Standardmodell (GPT-4.1) verwenden, sofern Sie nicht explizit in der immersiven Ansicht oder im Agent Mode zu einem benutzerdefinierten Modell wechseln.[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
3.  **OpenRouter-Integrationsbeschränkungen**: OpenRouter ermöglicht den Zugriff auf Modelle wie Grok (erstellt von xAI) und Kimi (von Moonshot AI), aber die Integration von Copilot mit OpenRouter erfordert einen spezifischen Setup, und möglicherweise sind nicht alle Modelle sofort verfügbar aufgrund von API-Beschränkungen oder Konfigurationsproblemen. Beispielsweise könnte die OpenRouter-API die Tool-Unterstützung nicht für alle Modelle ankündigen, was den Agent Mode oder bestimmte Funktionen mit Grok oder Kimi verhindern kann.[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
4.  **Abonnement- oder Konfigurationsbeschränkungen**: Wenn Sie einen kostenlosen Tarif oder ein nicht-Pro/Business Copilot-Abonnement verwenden, sind Sie möglicherweise auf Standardmodelle wie GPT-4.1 beschränkt. Zusätzlich erfordern einige Modelle (z.B. Grok oder Kimi) möglicherweise spezifische Konfigurationen oder Premium-Zugang über OpenRouter.[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

### So verwenden Sie Grok- oder Kimi-Modelle in Copilot über OpenRouter
Um Grok- oder Kimi-Modelle von OpenRouter in Copilot zu verwenden, insbesondere für die "Fix Box" (Inline-Chat oder Code-Vervollständigung), befolgen Sie diese Schritte:

1.  **OpenRouter mit Copilot einrichten**:
    *   **OpenRouter API-Schlüssel besorgen**: Melden Sie sich bei [openrouter.ai](https://openrouter.ai) an und erhalten Sie einen API-Schlüssel. Stellen Sie sicher, dass Sie Credits oder einen Tarif haben, der Zugang zu Grok (xAI) und Kimi (Moonshot AI K2) Modellen unterstützt.[](https://openrouter.ai/models)[](https://openrouter.ai)
    *   **OpenRouter in VS Code konfigurieren**:
        *   Öffnen Sie Visual Studio Code (VS Code) und stellen Sie sicher, dass die neueste GitHub Copilot-Erweiterung installiert ist (v1.100.2 oder höher).[](https://github.com/microsoft/vscode-copilot-release/issues/10193)
        *   Gehen Sie zum Copilot-Dashboard in der Statusleiste, oder öffnen Sie die Befehlspalette (`Strg+Umschalt+P` oder `Befehl+Umschalt+P` auf dem Mac) und geben Sie `GitHub Copilot: Manage Models` ein.
        *   Fügen Sie Ihren OpenRouter API-Schlüssel hinzu und konfigurieren Sie den Endpunkt, um OpenRouter-Modelle einzubeziehen. Möglicherweise müssen Sie der OpenRouter-Dokumentation zur Integration in die VS Code Copilot-Erweiterung folgen.[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
    *   **Modellverfügbarkeit überprüfen**: Nachdem Sie den OpenRouter-Endpunkt hinzugefügt haben, überprüfen Sie den Abschnitt "Manage Models" in Copilot. Modelle wie `openrouter/xai/grok` oder `openrouter/moonshotai/kimi-k2` sollten in der Modellauswahl erscheinen. Wenn nicht, stellen Sie sicher, dass Ihr OpenRouter-Konto Zugriff auf diese Modelle hat und dass es keine Einschränkungen gibt (z.B. durch kostenlose Tarife).[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

2.  **Modelle für die Fix Box wechseln**:
    *   **Für Inline-Chat (Fix Box)**: Bei der "Fix Box" handelt es sich wahrscheinlich um die Inline-Chat- oder Code-Vervollständigungsfunktion von Copilot. Um das Modell für den Inline-Chat zu ändern:
        *   Öffnen Sie die Copilot Chat-Oberfläche in VS Code (über das Symbol in der Titelleiste oder Seitenleiste).
        *   Wählen Sie in der Chat-Ansicht das Dropdown-Menü `CURRENT-MODEL` (normalerweise unten rechts) und wählen Sie `openrouter/xai/grok` oder `openrouter/moonshotai/kimi-k2`, falls verfügbar.[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
        *   Wenn das Dropdown-Menü Grok oder Kimi nicht anzeigt, könnte dies daran liegen, dass die OpenRouter-API die Tool-Unterstützung für diese Modelle nicht ankündigt, was deren Verwendung in bestimmten Copilot-Funktionen wie dem Agent Mode oder Inline-Fixes einschränken kann.[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
    *   **Für Code-Vervollständigung**: Um das Modell für Code-Vervollständigungen (nicht nur Chat) zu ändern:
        *   Öffnen Sie die Befehlspalette (`Strg+Umschalt+P` oder `Befehl+Umschalt+P`) und geben Sie `GitHub Copilot: Change Completions Model` ein.
        *   Wählen Sie das gewünschte OpenRouter-Modell (z.B. Grok oder Kimi) aus der Liste aus. Beachten Sie, dass möglicherweise nicht alle OpenRouter-Modelle die Code-Vervollständigung unterstützen, aufgrund der aktuellen Einschränkung von VS Code, die nur Ollama-Endpunkte für benutzerdefinierte Modelle unterstützt, obwohl OpenRouter mit einem Proxy-Workaround funktionieren kann.[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-completion-model)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)

3.  **Workaround für OpenRouter-Modelle**:
    *   **Proxy-Lösung**: Da die OpenRouter-API nicht immer die Tool-Unterstützung ankündigt (erforderlich für den Agent Mode oder erweiterte Funktionen), können Sie einen Proxy wie `litellm` verwenden, um Grok oder Kimi in Copilot zu aktivieren. Bearbeiten Sie die `config.yaml` Datei, um Folgendes einzubeziehen:
        ```yaml
        model_list:
          - model_name: grok
            litellm_params:
              model: openrouter/xai/grok
          - model_name: kimi-k2
            litellm_params:
              model: openrouter/moonshotai/kimi-k2
        ```
        *   Befolgen Sie die Setup-Anleitungen von Quellen wie [Bas codes](https://bas.codes) oder [DEV Community](https://dev.to) für detaillierte Schritte zur Konfiguration des Proxys.[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
    *   **VS Code neu starten**: Nach der Konfiguration des Proxys starten Sie VS Code neu, um sicherzustellen, dass die neuen Modelle in der Modellauswahl verfügbar sind.

4.  **Abonnement und Berechtigungen überprüfen**:
    *   **Copilot-Abonnement**: Stellen Sie sicher, dass Sie ein Copilot Pro oder Business Abonnement haben, da Benutzer mit kostenlosen Tarifen möglicherweise nicht die Option haben, benutzerdefinierte Modelle hinzuzufügen.[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
    *   **Business-Beschränkungen**: Wenn Sie ein Copilot Business Abonnement verwenden, muss Ihre Organisation den Modellwechsel aktivieren. Überprüfen Sie dies bei Ihrem Administrator oder lesen Sie die GitHub-Dokumentation zur Verwaltung von Copilot-Richtlinien.[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
    *   **OpenRouter-Credits**: Vergewissern Sie sich, dass Ihr OpenRouter-Konto über ausreichend Credits verfügt, um auf Premium-Modelle wie Grok oder Kimi zuzugreifen, da diese möglicherweise mehr Credits verbrauchen als andere.[](https://www.reddit.com/r/GithubCopilot/comments/1la87wr/why_are_gh_copilot_pro_models_so_much_worse_than/)

5.  **Fehlerbehebung für die Fix Box**:
    *   Wenn die Fix Box weiterhin GPT-4.1 verwendet, könnte dies daran liegen, dass die Inline-Chat-Funktion in bestimmten Kontexten (z.B. nicht-immersive Ansicht) auf das Standardmodell gesperrt ist. Versuchen Sie, zur immersiven Ansicht von Copilot Chat (`https://github.com/copilot`) zu wechseln, um explizit Grok oder Kimi auszuwählen.[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
    *   Wenn Grok oder Kimi nicht in der Modellauswahl erscheinen, überprüfen Sie die OpenRouter-Integration in `Manage Models` erneut. Möglicherweise müssen Sie die Modellliste aktualisieren oder den OpenRouter API-Schlüssel erneut hinzufügen.[](https://github.com/microsoft/vscode-copilot-release/issues/10193)
    *   Wenn das Problem weiterhin besteht, testen Sie die Modelle zuerst im Agent Mode oder der Chat-Oberfläche von Copilot, um zu bestätigen, dass sie funktionieren, und versuchen Sie dann, sie auf Inline-Fixes anzuwenden.

6.  **Alternative Tools**:
    *   Wenn die OpenRouter-Integration mit Copilot weiterhin problematisch bleibt, ziehen Sie in Betracht, Grok direkt über [grok.com](https://grok.com) oder die Grok iOS/Android Apps zu verwenden, die kostenlosen Zugang mit Nutzungskontingenten bieten. Kimi-Modelle können auch über die OpenRouter-Chat-Oberfläche getestet werden, um sicherzustellen, dass sie zugänglich sind.[](https://openrouter.ai)
    *   Für eine nahtlosere Erfahrung könnten Sie andere IDEs oder Tools wie Cursor erkunden, von dem berichtet wurde, dass es gut mit dem Kimi K2-Modell von OpenRouter funktioniert.[](https://openrouter.ai)

### Zusätzliche Hinweise
*   **Modellleistung**: Grok ist für Reasoning und Truth-Seeking optimiert, was es für komplexe Debugging- oder Architekturaufgaben geeignet macht, während Kimi (K2) in bestimmten Codierungsszenarien hervorstechen könnte. Testen Sie beide, um zu sehen, welche für Ihren Anwendungsfall besser abschneidet.[](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
*   **Community-Feedback**: Einige Benutzer berichten von Problemen, dass OpenRouter-Modelle nicht in der Modellauswahl von Copilot erscheinen, insbesondere bei kostenlosen Konten. Dies erfordert möglicherweise einen kostenpflichtigen OpenRouter-Plan oder ein Copilot Pro-Abonnement, um es zu beheben.[](https://github.com/microsoft/vscode-copilot-release/issues/10193)[](https://www.reddit.com/r/GithubCopilot/comments/1la87wr/why_are_gh_copilot_pro_models_so_much_worse_than/)
*   **Laufende Einschränkungen**: Es gibt eine offene Diskussion darüber, benutzerdefinierte API-Endpunkte direkt in Copilot zu aktivieren (siehe [microsoft/vscode-copilot-release#7518](https://github.com/microsoft/vscode-copilot-release/issues/7518)). Bis dies implementiert ist, ist der Proxy-Workaround die zuverlässigste Methode, um Grok oder Kimi zu verwenden.[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)

### Zitate
*   [Changing the AI model for Copilot Chat - GitHub Docs](https://docs.github.com/en/copilot/managing-copilot/changing-the-ai-model-for-copilot-chat)[](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model)
*   [How to Use Third Party Models in GitHub Copilot Agent Mode - Bas codes](https://bas.codes)[](https://bas.codes/posts/how-to-use-third-party-models-in-copilot-agent-mode/)
*   [Openrouter - openrouter.ai](https://openrouter.ai)[](https://openrouter.ai/models)
*   [Agent Mode With Third-Party Models in Copilot - DEV Community](https://dev.to)[](https://dev.to/bascodes/agent-mode-with-third-party-models-in-copilot-317k)
*   [Openrouter - openrouter.ai](https://openrouter.ai)[](https://openrouter.ai)
*   [r/LocalLLaMA on Reddit: Github Copilot now supports Ollama and OpenRouter Models](https://www.reddit.com)[](https://www.reddit.com/r/LocalLLaMA/comments/1jslnxb/github_copilot_now_supports_ollama_and_openrouter/)
*   [Which AI model should I use with GitHub Copilot? - The GitHub Blog](https://github.blog)[](https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/)
*   [OpenAI GPT-4.1 is now generally available in GitHub Copilot - GitHub Changelog](https://github.blog)[](https://github.blog/changelog/2025-05-08-openai-gpt-4-1-is-now-generally-available-in-github-copilot-as-the-new-default-model/)
*   [OpenRouter (free) Models Missing from Manage Models - GitHub Issues](https://github.com/microsoft/vscode-copilot-release/issues/10193)[](https://github.com/microsoft/vscode-copilot-release/issues/10193)

Wenn Sie auf spezifische Fehler stoßen oder weitere Hilfe beim Setup benötigen, geben Sie bitte mehr Details an (z.B. Fehlermeldungen, VS Code-Version oder Abonnementtyp), und ich kann die Lösung weiter anpassen!