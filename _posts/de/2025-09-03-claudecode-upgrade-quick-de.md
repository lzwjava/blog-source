---
audio: false
generated: true
image: false
lang: de
layout: post
title: Claude Code Schnell Upgrade Jetzt
translated: true
type: note
---

Wenn Sie **Claude Code upgraden möchten**, den Command-Line-Coding-Agent von Anthropic, finden Sie hier eine Anleitung – und wie Sie die neuesten Funktionen wie Lernmodi und benutzerdefinierte Subagents zum Laufen bringen.

---

### So upgraden Sie Claude Code

1. **Überprüfen Sie Ihre aktuelle Version**
   Führen Sie aus:

   ```
   claude --version
   ```

   So sehen Sie, welche Version Sie aktuell verwenden.

2. **Update via npm**
   Die einfachste Update-Methode ist:

   ```
   npm install -g @anthropic-ai/claude-code@latest
   ```

   Dies lädt die neueste Version von npm herunter.
   Nutzer auf Reddit berichten, dass dies Bugs behoben und die Reaktionsfähigkeit verbessert hat. Einer schrieb:

   > „Nach dem Update auf die neueste Version (1.0.18) ist es wie Tag und Nacht – es fühlt sich viel intelligenter und reaktionsschneller an.“
   > ([Reddit][1], [Anthropic][2])

3. **Alternativ: Verwenden Sie den nativen Installer (Beta)**
   Wenn Sie ein eigenständiges Binary (anstatt npm) bevorzugen, versuchen Sie:

   ```
   curl -fsSL https://claude.ai/install.sh | bash -s latest
   ```

   (Unter Windows verwenden Sie die PowerShell-Version)
   ([Anthropic][3])

4. **Verifizieren Sie das Update**
   Starten Sie nach der Installation Ihr Terminal neu und führen Sie erneut `claude --version` aus, um zu bestätigen, dass die neue Version aktiv ist.

5. **Fehlerbehebung bei Installationsproblemen**
   Wenn Sie auf Probleme stoßen, versuchen Sie, zuerst zu deinstallieren:

   ```
   npm uninstall -g @anthropic-ai/claude-code
   npm install -g @anthropic-ai/claude-code
   ```

   Einige Nutzer fanden, dass diese Abfolge Update-Probleme behob. ([Anthropic][4], [Reddit][1], [Anthropic][5], [The Verge][6])

---

### Was ist neu in den letzten Updates?

#### Lernmodi

Anthropic hat kürzlich zwei neue Lernstile in Claude Code hinzugefügt: **„Explanatory“** und **„Learning“**. Diese helfen Ihnen, die Logik hinter generiertem Code zu verstehen, anstatt nur Lösungen zu liefern. So aktivieren Sie sie:

1. Stellen Sie sicher, dass Sie Claude Code aktualisiert haben.
2. Führen Sie `/output-styles` in Ihrer Claude Code-Sitzung aus.
3. Wählen Sie zwischen **Default**, **Explanatory** oder **Learning** Style.
   Diese Funktion wurde am **14. August 2025** veröffentlicht. ([Tom's Guide][7])

#### Benutzerdefinierte Subagents

Claude Code unterstützt jetzt **Subagents** – spezialisierte KI-Assistenten für bestimmte Aufgaben (z.B. Bugfixing, Refactoring, Dokumentation). Sie können für jeden verschiedene System-Prompts, Tool-Berechtigungen und Kontextfenster festlegen.
So richten Sie einen ein:

1. Führen Sie `/agents` aus
2. Wählen Sie „Create New Agent“ (entweder auf Benutzer- oder Projektebene)
3. Definieren Sie sein Verhalten, erlaubte Tools und speichern Sie es
   Subagents helfen dabei, Ihren Workflow sauberer, fokussierter und kontextbewusster zu halten. ([Anthropic][8])

---

### Kurze Zusammenfassung (Keine Tabellen, nur klare Schritte)

* **Zum Upgraden**:

  ```
  npm install -g @anthropic-ai/claude-code@latest
  ```

  oder verwenden Sie die native Installation mit `curl | bash -s latest`.

* **Lernmodi aktivieren**:

  * Updaten
  * Innerhalb von Claude Code: `/output-styles` ausführen und den Modus wählen.

* **Subagents erstellen**:

  * Innerhalb von Claude Code: `/agents` ausführen
  * Tool-Zugriff, System-Prompt und Verhalten anpassen.

---

### Abschließende Gedanken

Claude Code zu upgraden ist unkompliziert – verwenden Sie npm oder den nativen Installer, prüfen Sie, ob Sie die neueste Version haben, und erkunden Sie dann die neuen Funktionen **Lernmodi** und **Subagents**. Diese Ergänzungen verändern Claude Code von einem reinen Coding-Assistenten hin zu etwas, das eher einem Lehrpartner und agentenbasierten Mitarbeiter in Ihrem Entwicklungs-Workflow ähnelt.

Wenn Sie Hilfe beim Erstellen Ihres ersten Subagents oder bei der effektiven Nutzung des Lernmodus benötigen, helfe ich Ihnen gerne dabei!

[1]: https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/?utm_source=chatgpt.com "Don't forget to update your Claude CLI! It makes a huge ..."
[2]: https://www.anthropic.com/solutions/agents?utm_source=chatgpt.com "Claude Agents | Intelligent AI Solutions \ Anthropic"
[3]: https://docs.anthropic.com/en/docs/claude-code/quickstart?utm_source=chatgpt.com "Quickstart - Claude Code"
[4]: https://docs.anthropic.com/en/docs/claude-code/settings?utm_source=chatgpt.com "Claude Code settings"
[5]: https://docs.anthropic.com/en/docs/claude-code/overview?utm_source=chatgpt.com "Claude Code overview"
[6]: https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources?utm_source=chatgpt.com "Anthropic launches tool to connect AI systems directly to datasets"
[7]: https://www.tomsguide.com/ai/claudes-new-learning-modes-take-on-chatgpts-study-mode-heres-what-they-do?utm_source=chatgpt.com "Claude's new 'learning modes' take on ChatGPT's Study Mode - here's what they do"
[8]: https://docs.anthropic.com/en/docs/claude-code/sub-agents?utm_source=chatgpt.com "Subagents"