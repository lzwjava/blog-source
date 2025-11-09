---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 変更 VS コード カーソル ライン
translated: true
type: note
---

### VS Code でブロック（四角形）カーソルを修正する方法

カーソルがブロック/四角形スタイル（上書きモードやデフォルト設定でよく発生）に変わってしまい、編集しやすい細い縦線の**ライン**スタイルに戻したいのですね。これは簡単な設定変更で修正できます。以下の手順を正確に実行してください：

#### 設定UIを使用する方法（最も簡単）：
1. VS Codeを開きます。
2. `Ctrl + ,`（Windows/Linux）または `Cmd + ,`（macOS）を押して設定を開きます。
3. 上部の検索ボックスに「**cursor style**」と入力します。
4. **Editor: Cursor Style**（Text Editor > Cursor の下）を探します。
5. ドロップダウンをクリックして **Line** を選択します（現在は「Block」と表示されているかもしれません）。
6. 変更は即座に反映されます。ファイルで入力して細いラインカーソルを確認してください。

まだ更新されない場合は、VS Codeを閉じて再度開くか、完全に再起動してください。

#### settings.jsonを使用する方法（正確な設定）：
1. コマンドパレットを開きます：`Ctrl + Shift + P`（macOSでは `Cmd + Shift + P`）。
2. 入力して選択：**Preferences: Open User Settings (JSON)**。
3. `{}` の中に以下の行を追加または更新します（空の場合は作成）：
   ```json:disable-run
   "editor.cursorStyle": "line"
   ```
4. ファイルを保存します（`Ctrl + S` または `Cmd + S`）。

#### 追加のヒント：
- **上書きモードですか？** 誤って「上書き」モード（文字をブロックするモード）になっている場合は、キーボードの **Insert** キーを押して挿入モードに切り替えてください。
- **点滅の問題ですか？** ラインがぎくしゃくしている場合は、設定で **cursor blinking** を検索し、**Blink** または **Smooth** に設定してください。
- **拡張機能の干渉ですか？** Vimなどの拡張機能を一時的に無効にして（拡張機能ビュー > 右クリック > Disable）テストしてください。

これでクリーンなラインカーソルがすぐに表示されるはずです。これでもまだ四角形のままの場合は、OSやスクリーンショットを共有していただければ、より具体的なヘルプを提供できます！

[VS Code カーソルドキュメント](https://code.visualstudio.com/docs/editor/codebasics#_cursor-style)