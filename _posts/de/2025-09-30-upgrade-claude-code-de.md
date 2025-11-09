---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Aktualisierung des Claude-Codes auf die neueste Version
translated: true
type: note
---

Um Claude Code von v2.0.0 auf die neueste Version upzugraden, verwenden Sie eine der folgenden Methoden, basierend auf Ihrem Installationstyp (alle Versionen unterstützen standardmäßig Auto-Updates, die beim nächsten Start des Tools angewendet werden; Sie können sie deaktivieren, indem Sie `DISABLE_AUTOUPDATER=1` setzen):

### Über den integrierten Befehl von Claude Code
Führen Sie den manuellen Update-Befehl in Ihrem Terminal aus:
```
claude update
```
Dies wendet automatisch die neueste Version an. [1][2]

### Über npm (falls global installiert)
Falls Sie ursprünglich via npm installiert haben, aktualisieren Sie mit:
```
npm update -g @anthropic-ai/claude-code
```
Oder erzwingen Sie die Installation der neuesten Version:
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### Über Native Binary (Beta Installer)
Für native Installationen führen Sie das Installationsskript erneut für die neueste Version aus:
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**Verifikation:** Überprüfen Sie nach dem Upgrade Ihre Version mit `claude --version`, um zu bestätigen, dass sie aktualisiert wurde (z.B. auf den aktuellen Stable Release). Falls Sie auf Probleme stoßen, stellen Sie sicher, dass npm auf dem neuesten Stand ist (`npm install -g npm@latest`). Einstellungen und Konfigurationen werden über Updates hinweg beibehalten. [1][3][4]

Zitate:
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/