---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Claude Code Utilise Git Bash sur Windows
translated: true
type: note
---

Oui, selon les développements récents, Claude Code (un outil de codage IA d'Anthropic) sur Windows déclenche bien l'exécution de `git-bash.exe` pour exécuter des commandes shell. Il utilise souvent Git Bash comme environnement pour l'exécution des commandes, particulièrement dans les configurations Windows natives sans WSL. Cela peut entraîner l'apparition de terminaux contextuels pour l'exécution des commandes, et il existe des configurations, des extensions (comme dans VS Code) et des étapes de dépannage connues concernant la détection et l'utilisation correcte de Git Bash.

Par exemple :
- Dans les installations Windows natives, Claude Code s'appuie sur Git Bash pour la compatibilité de type Unix afin de gérer les scripts et les commandes.
- S'il est défini comme terminal par défaut (par exemple dans les outils intégrés comme VS Code ou Cursor), il lancera `git-bash.exe` pour les tâches.
- Il existe des bugs signalés et des guides pour gérer les problèmes de chemin d'accès ou les espaces dans le répertoire d'installation de Git qui affectent cette intégration.

Si vous rencontrez des problèmes, vérifiez le PATH de votre système, assurez-vous que Git est installé correctement et vérifiez le profil du terminal dans votre IDE.

Références :  
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