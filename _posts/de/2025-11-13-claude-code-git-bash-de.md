---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Claude Code verwendet Git Bash unter Windows
translated: true
type: note
---

Ja, basierend auf aktuellen Entwicklungen triggert Claude Code (ein KI-Codierungstool von Anthropic) unter Windows tatsächlich `git-bash.exe`, um Shell-Befehle auszuführen. Es verwendet häufig Git Bash als Umgebung für die Befehlsausführung, insbesondere in nativen Windows-Setups ohne WSL. Dies kann zu aufpoppenden Terminals für die Befehlsausführung führen, und es gibt bekannte Konfigurationen, Erweiterungen (wie in VS Code) und Troubleshooting-Schritte in Bezug auf die ordnungsgemäße Erkennung und Nutzung von Git Bash.

Beispielsweise:
- Bei nativen Windows-Installationen verlässt sich Claude Code auf Git Bash für Unix-ähnliche Kompatibilität, um Skripte und Befehle zu verarbeiten.
- Wenn es als Standard-Terminal festgelegt ist (z.B. in integrierten Tools wie VS Code oder Cursor), startet es `git-bash.exe` für Aufgaben.
- Es gibt gemeldete Bugs und Anleitungen zum Umgang mit Pfadproblemen oder Leerzeichen im Git-Installationsverzeichnis, die diese Integration beeinflussen.

Wenn Sie auf Probleme stoßen, überprüfen Sie Ihren System-PATH, stellen Sie sicher, dass Git korrekt installiert ist, und verifizieren Sie das Terminal-Profil in Ihrer IDE.

Referenzen:  
[Claude Code Native Windows Bash output not seen - Reddit](https://www.reddit.com/r/ClaudeAI/comments/1m06s2l/claude_code_native_windows_bash_output_not_seen/)  
[BUG Claude Code VS Code Extension Fails to Detect Git Bash on GitHub](https://github.com/anthropics/claude-code/issues/8674)  
[Troubleshooting Claude Code Installation on Windows - Medium](https://medium.com/%40tomhag_17/troubleshooting-claude-code-installation-on-windows-from-tty-errors-to-success-1f44af03c9f2)  
[Running Claude Code on Windows Without WSL - Blog](https://blog.shukebeta.com/2025/06/25/running-claude-code-on-windows-without-wsl/)  
[AI Agent Claude 4 runs commands in PowerShell even when default is Git Bash - Forum](https://forum.cursor.com/t/ai-agent-claude-4-runs-commands-in-powershell-even-when-default-terminal-is-git-bash/137164)  
[How To Install Claude Code on Windows Complete Guide 2025 - Itecsonline](https://itecsonline.com/post/how-to-install-claude-code-on-windows)  
[BUG Claude Code fails to resolve Git Bash path with space - GitHub](https://github.com/anthropics/claude-code/issues/4507)  
[Install Claude Code on Windows Without WSL Step-by-Step Guide - YouTube](https://www.youtube.com/watch?v=LtnxvLZjxAI)  
[47 Claude Code WSL Tricks Every Windows User Should Know - Medium](https://medium.com/%40joe.njenga/47-claude-code-wsl-tricks-every-windows-user-should-know-5d42aaee2d93)  
[Claude Code Installation Guide for Windows 11 Setting Up with WSL2 - Claude AI](https://claude.ai/public/artifacts/03a4aa0c-67b2-427f-838e-63770900bf1d)