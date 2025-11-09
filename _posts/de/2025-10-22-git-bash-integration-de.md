---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Integration von Git Bash in Windows Terminal
translated: true
type: note
---

Ja, Git Bash kann in einem Konsolenfenster ausgeführt werden (standardmäßig verwendet es sein eigenes MinTTY-Terminal) und integriert sich nahtlos in Windows Terminal. Sie müssen lediglich ein benutzerdefiniertes Profil dafür in den Einstellungen des Windows Terminals hinzufügen – verweisen Sie es auf die `bash.exe`-Ausführbare Datei in Ihrer Git-Installation (normalerweise `C:\Program Files\Git\bin\bash.exe`). Sobald es hinzugefügt wurde, können Sie es wie jede andere Shell in einem neuen Tab oder Fensterbereich starten.

Sie irren sich bezüglich der Einschränkungen des Windows Terminals: Es unterstützt weit mehr als nur PowerShell und Command Prompt. Standardmäßig verwaltet es diese beiden plus WSL-Distributionen, Azure Cloud Shell und sogar benutzerdefinierte Shells wie Git Bash oder Cygwin. Es ist als flexibler Host für so ziemlich jede Kommandozeilenumgebung konzipiert.

[Adding Git-Bash to the new Windows Terminal](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[Adding Git-Bash to Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)  
[In Windows Terminal, how do I add bash as one of the shell options?](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)