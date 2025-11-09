---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Integración de Git Bash con Windows Terminal
translated: true
type: note
---

Sí, Git Bash puede ejecutarse en una ventana de consola (por defecto usa su propia terminal MinTTY) y se integra perfectamente con Windows Terminal. Solo necesitas agregar un perfil personalizado para él en la configuración de Windows Terminal—dirígelo al ejecutable `bash.exe` en tu instalación de Git (normalmente `C:\Program Files\Git\bin\bash.exe`). Una vez agregado, puedes iniciarlo en una nueva pestaña o panel como cualquier otro shell.

Estás equivocado acerca de las limitaciones de Windows Terminal: es compatible con mucho más que solo PowerShell y Command Prompt. De forma nativa, maneja esos dos más distribuciones de WSL, Azure Cloud Shell, e incluso shells personalizados como Git Bash o Cygwin. Está diseñado como un host flexible para prácticamente cualquier entorno de línea de comandos.

[Añadir Git-Bash al nuevo Windows Terminal](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[Añadir Git-Bash a Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)  
[En Windows Terminal, ¿cómo agrego bash como una de las opciones de shell?](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)