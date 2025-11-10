---
audio: false
generated: true
lang: de
layout: post
title: Aktualisierung der Claude Code CLI
translated: true
type: note
---

Hallo! Es sieht so aus, als ob du mit dem Claude Code CLI-Tool von Anthropic arbeitest. Basierend auf der von dir eingefügten Ausgabe scheint es bereits versucht zu haben, automatisch auf Version 1.0.61 zu aktualisieren. Falls das nicht funktioniert oder du manuell aktualisieren musst, hier die Vorgehensweise:

So aktualisierst du das Claude Code CLI:
- Öffne dein Terminal.
- Führe den Befehl aus: `claude update`
Dieser integrierte Befehl sollte die neueste Version abrufen und installieren.

Falls das Update fehlschlägt (z.B. aufgrund von Berechtigungs- oder Netzwerkproblemen), kannst du versuchen, es über npm neu zu installieren (vorausgesetzt, du hast Node.js und npm installiert):
- Führe aus: `npm install -g @anthropic-ai/claude-code`

Nach dem Aktualisieren musst du dich möglicherweise erneut anmelden, indem du `claude /login` ausführst (oder manchmal `claude login`, abhängig von der Version). Wenn du weiterhin Fehler siehst, überprüfe deine Internetverbindung, stelle sicher, dass dein API-Schlüssel gültig ist, oder siehe in der offiziellen Fehlerbehebungsdokumentation nach.

Weitere Details zu Befehlen erhältst du, wenn du `claude --help` ausführst, wie du es bereits getan hast. Dies sollte die Optionen in der aktualisierten Version anzeigen.

[CLI-Referenz - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[How to Set Up and Use the Claude CLI Tool Like a Pro](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[Claude Code overview - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/overview)