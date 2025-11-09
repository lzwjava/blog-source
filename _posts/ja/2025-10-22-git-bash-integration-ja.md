---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Windows Terminal への Git Bash 統合
translated: true
type: note
---

はい、Git Bashはコンソールウィンドウで実行可能です（デフォルトでは独自のMinTTYターミナルを使用します）し、Windows Terminalともシームレスに統合できます。Windows Terminalの設定でカスタムプロファイルを追加するだけで実現できます―Gitのインストール先にある`bash.exe`実行ファイル（通常は`C:\Program Files\Git\bin\bash.exe`）を指定してください。追加後は、他のシェルと同様に新しいタブやペインで起動できます。

Windows Terminalの制限について誤解されています：PowerShellとコマンドプロンプト以外にも多くの環境をサポートしています。標準でこれら2つに加えて、WSLディストリビューション、Azure Cloud Shell、さらにはGit BashやCygwinのようなカスタムシェルも扱えます。あらゆるコマンドライン環境を柔軟にホストするように設計されています。

[Adding Git-Bash to the new Windows Terminal](https://stackoverflow.com/questions/56839307/adding-git-bash-to-the-new-windows-terminal)  
[Adding Git-Bash to Windows Terminal](https://www.timschaeps.be/post/adding-git-bash-to-windows-terminal/)  
[In Windows Terminal, how do I add bash as one of the shell options?](https://superuser.com/questions/1763652/in-windows-terminal-how-do-i-add-bash-as-one-of-the-shell-options)