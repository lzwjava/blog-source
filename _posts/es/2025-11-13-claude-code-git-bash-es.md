---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Claude Code Usa Git Bash en Windows
translated: true
type: note
---

Sí, según desarrollos recientes, Claude Code (una herramienta de codificación con IA de Anthropic) en Windows sí activa `git-bash.exe` para ejecutar comandos de shell. Frecuentemente utiliza Git Bash como entorno para ejecutar comandos, especialmente en configuraciones nativas de Windows sin WSL. Esto puede resultar en la aparición de terminales emergentes durante la ejecución de comandos, y existen configuraciones, extensiones (como en VS Code) y pasos de solución de problemas conocidos relacionados con asegurar que Git Bash sea detectado y utilizado correctamente.

Por ejemplo:
- En instalaciones nativas de Windows, Claude Code depende de Git Bash para obtener compatibilidad tipo Unix y manejar scripts y comandos.
- Si está configurado como terminal predeterminado (por ejemplo, en herramientas integradas como VS Code o Cursor), lanzará `git-bash.exe` para las tareas.
- Existen bugs reportados y guías para manejar problemas de rutas o espacios en el directorio de instalación de Git que afectan esta integración.

Si estás experimentando problemas, verifica la variable PATH de tu sistema, asegúrate de que Git esté instalado correctamente y comprueba el perfil del terminal en tu IDE.

Referencias:  
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