---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ghosttyでの全画面表示終了
translated: true
type: note
---

UbuntuのGhosttyターミナルで全画面モードを終了するには、**Ctrl + Enter**を押してください。これは全画面表示を切り替えるデフォルトのキーバインドです。

もし動作しない場合（カスタム設定などが原因）、以下の代替方法をお試しください：
- ターミナルウィンドウ内で右クリックし、コンテキストメニュー内の「Leave Fullscreen」または類似のオプションを探す
- メニューバーが表示されている場合は、**View > Leave Fullscreen**に移動（画面上部にホバーして表示させる必要がある場合があります）
- 最終手段として、別のターミナルで`ghostty`を実行してGhosttyを再起動するか、`pkill ghostty`でプロセスを終了して再起動する

[ghostty-shortcuts.md](https://gist.github.com/hensg/43bc71c21d1f79385892352a390aa2ca)  
[Keybindings for Midnight Commander (Reddit)](https://www.reddit.com/r/Ghostty/comments/1lfxvsf/keybindings_for_midnight_commander/)