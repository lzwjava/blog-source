---
audio: false
generated: true
lang: ja
layout: post
title: クイックコード選択とAI編集
translated: true
type: note
---

以下は、**Visual Studio Code (VS Code)**、**Cursor**、および**IntelliJ IDEA** でショートカットを使用して関数やメソッドを素早く選択する方法の概要と、その後、それらのAI機能を活用して選択したコードを修正または編集する方法です。

### Visual Studio Code (VS Code)
VS Codeには、カーソルが関数/メソッド内にあるときにその全体を直接選択するショートカットはありませんが、以下の方法を使用できます。
- **選択範囲の拡大**: `Ctrl+Shift+.` (Windows/Linux) または `Cmd+Shift+.` (Mac) を押して、選択範囲のスコープを拡大します。繰り返し押すと、囲んでいるブロック（例: 関数本体、その後関数全体）が選択されます。これは JavaScript、Python などでうまく機能します。
- **スマート選択**: `Ctrl+Shift+Right Arrow` (Windows/Linux) または `Cmd+Shift+Right Arrow` (Mac) を使用して、構文に基づいて選択範囲を拡大します（関数全体を取得するには複数回押す必要がある場合があります）。
- **拡張機能: Select By**: "Select By" 拡張機能をインストールし、キーバインド（例: `Ctrl+K, Ctrl+S`）を設定して、言語固有のパターンに基づいて囲んでいる関数/メソッドを選択します。

**GitHub Copilot によるAI編集**:
- 関数を選択した後、`Ctrl+I` (Windows/Linux) または `Cmd+I` (Mac) を押して Copilot のインラインチャットを開きます。「この関数のバグを修正」や「アロー関数を使用するようにリファクタリング」などのプロンプトを入力します。
- または、選択部分を右クリックし、「Copilot > Fix」または「Copilot > Refactor」を選択してAIによる提案を表示します。
- Copilot Chat ビュー (`Ctrl+Alt+I`) で、選択したコードを貼り付け、編集を依頼します（例: 「この関数を最適化」）。

### Cursor AI Code Editor
Cursor は VS Code を基盤として構築されており、選択機能とAI統合を強化しています。
- **囲んでいるブロックの選択**: `Ctrl+Shift+.` (Windows/Linux) または `Cmd+Shift+.` (Mac) を押して、囲んでいる関数/メソッドまで選択範囲を拡大します。VS Code と同様です。Cursor の言語モデル認識により、Python や TypeScript などの言語ではこれがより正確になることが多いです。
- **カスタムキーバインド**: `settings.json` でカスタムキーバインド（例: `editor.action.selectToBracket`）を設定して、関数スコープを直接選択できます。

**Cursor でのAI編集**:
- 関数を選択した後、`Ctrl+K` (Windows/Linux) または `Cmd+K` (Mac) を押し、変更内容を記述します（例: 「この関数にエラーハンドリングを追加」）。Cursor はAI生成による編集の差分プレビューを表示します。
- `Ctrl+I` を使用して Agent Mode を起動し、ファイルをまたいだ関数の修正や最適化を反復的なフィードバックとともに自律的に実行します。
- Composer Mode (UIからアクセス可能) を使用すると、関数がコードベースの他の部分に影響を与える場合のマルチファイル編集が可能です。

### IntelliJ IDEA
IntelliJ IDEA は、関数/メソッドを選択するための強力なショートカットを提供します。
- **コードブロックの選択**: メソッド内にカーソルを置き、`Ctrl+W` (Windows/Linux) または `Cmd+W` (Mac) を押して、囲んでいるブロックを段階的に選択します。繰り返し押すとメソッド全体（シグネチャを含む）に拡大されます。これは Java、Kotlin、Python などで機能します。
- **選択範囲の縮小**: `Ctrl+Shift+W` (Windows/Linux) または `Cmd+Shift+W` (Mac) を使用して、選択範囲を広げすぎた場合に縮小します。
- **構造を意識した選択**: `Ctrl+Alt+Shift+Up` (Windows/Linux) または `Cmd+Option+Shift+Up` (Mac) を押して、構造ツリーを介して囲んでいるメソッドを直接選択します。

**JetBrains AI Assistant によるAI編集**:
- メソッドを選択した後、`Alt+Enter` を押すか、右クリックして「AI Actions」>「Fix with AI」または「Suggest Refactoring」を選択します。AI Assistant はコンテキストを考慮した提案を差分ビューアーで提供します。
- インラインプロンプト（`/` を入力し、続いてリクエスト（例: `/refactor to use streams`）を入力し、`Tab` を押す）を使用して、選択したメソッドを直接編集します。
- AI Assistant ツールウィンドウを開き、複雑な変更（例: 「このメソッドにロギングを追加」）を記述し、生成されたコードを適用します。

### まとめ
- **VS Code**: 選択範囲の拡大に `Ctrl+Shift+.` を使用し、その後 `Ctrl+I` で Copilot AI 編集を行います。
- **Cursor**: 同じ選択ショートカット (`Ctrl+Shift+.`) と `Ctrl+K` による正確なAI主導の編集。
- **IntelliJ IDEA**: 素早いメソッド選択に `Ctrl+W` を使用し、その後 `Alt+Enter` で AI Assistant による修正を行います。

IntelliJ はメソッド選択において最も正確な組み込みショートカット (`Ctrl+W`) を持ち、Cursor のAI統合は選択したコードの編集において最もシームレスです。VS Code は柔軟ですが、より高速な関数選択には拡張機能が必要な場合があります。

参考文献:  
[Visual Studio Code でのコードナビゲーション](https://code.visualstudio.com/docs/editor/editingevolved)  
[Cursor AI: 10の実践例によるガイド](https://www.datacamp.com/tutorial/cursor-ai-code-editor)  
[IntelliJ IDEA でのコード編集](https://www.jetbrains.com/help/idea/working-with-source-code.html)  
[エディターでAIを使用 | IntelliJ IDEA ドキュメント](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)