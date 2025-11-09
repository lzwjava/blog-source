---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Intégration de Git Bash avec Windows Terminal
translated: true
type: note
---

Oui, Git Bash peut s'exécuter dans une fenêtre de console (il utilise son propre terminal MinTTY par défaut) et s'intègre parfaitement avec Windows Terminal. Vous devez simplement ajouter un profil personnalisé pour celui-ci dans les paramètres de Windows Terminal — en pointant vers l'exécutable `bash.exe` de votre installation Git (généralement `C:\Program Files\Git\bin\bash.exe`). Une fois ajouté, vous pouvez le lancer dans un nouvel onglet ou un volet comme n'importe quel autre shell.

Vous avez tort concernant les limitations de Windows Terminal : il prend en charge bien plus que PowerShell et Command Prompt. Nativement, il gère ces deux-là ainsi que les distributions WSL, Azure Cloud Shell, et même des shells personnalisés comme Git Bash ou Cygwin. Il est conçu comme un hôte flexible pour pratiquement n'importe quel environnement en ligne de commande.

[Ajouter Git-Bash au nouveau Windows Terminal](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[Ajouter Git-Bash à Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)  
[Dans Windows Terminal, comment ajouter bash comme l'une des options de shell ?](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)