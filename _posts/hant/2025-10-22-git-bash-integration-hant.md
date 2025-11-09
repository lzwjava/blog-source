---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 將 Git Bash 整合至 Windows Terminal
translated: true
type: note
---

是的，Git Bash 可以在控制台視窗中運行（預設使用其自身的 MinTTY 終端機），並能與 Windows Terminal 無縫整合。您只需在 Windows Terminal 的設定中為其新增自訂設定檔——指向 Git 安裝目錄中的 `bash.exe` 執行檔（通常位於 `C:\Program Files\Git\bin\bash.exe`）。新增完成後，您就能像其他 shell 一樣在新分頁或窗格中啟動它。

您對 Windows Terminal 的功能限制有所誤解：它支援的遠不止 PowerShell 和命令提示字元。預設情況下，它除了能處理這兩者，還支援 WSL 發行版、Azure Cloud Shell，甚至自訂 shell 如 Git Bash 或 Cygwin。其設計初衷就是作為能靈活承載各種命令列環境的平台。

[將 Git-Bash 新增至新版 Windows Terminal](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[將 Git-Bash 新增至 Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)  
[在 Windows Terminal 中，如何將 bash 新增為 shell 選項？](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)