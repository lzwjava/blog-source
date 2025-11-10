---
audio: false
generated: true
lang: ja
layout: post
title: AI駆動型コード編集ツール
translated: true
type: note
---

### Visual Studio Code (VS Code) with GitHub Copilot
VS Codeは、GitHub Copilot（AI拡張機能）によって強化され、コード（関数など）を選択し、AIを使用して修正、編集、リファクタリングすることをサポートします。主な機能は以下の通りです：
- **インライン チャット**: コードを選択し、`Ctrl+I`（Windows/Linux）または `Cmd+I`（Mac）を押し、「このバグを修正」や「async/awaitを使用するようにリファクタリング」などのプロンプトを入力します。Copilotはエディタ内で直接編集を提案します。
- **エラーの修正**: コンパイラエラー（赤い波線）に対して、ホバーして「Fix using Copilot」を選択すると、AIが生成した修正案が表示されます。
- **チャットビュー**: Copilot チャット (`Ctrl+Alt+I`) を開き、コードを選択して、説明、編集、テストの生成を依頼します。エージェントモードではマルチファイル編集を扱えます。
- **アクションメニュー**: コードを選択して右クリックし、説明、名前変更、レビューなどのAIアクションを実行できます。

Copilotは制限付きで無料、または無制限利用で有料です。

### Cursor AI Code Editor
Cursorは、VS CodeからフォークされたAIファーストのコードエディタで、AI支援編集に特化して設計されています。コードを選択しAIで修正する点に優れています：
- **Ctrl+Kで編集**: 関数やコードブロックを選択し、`Ctrl+K`（Macでは `Cmd+K`）を押して変更内容（例：「この関数をパフォーマンスのために最適化」）を記述します。Cursorは差分を生成し、プレビューと適用が可能です。
- **Composerモード**: ファイルを跨ぐ複雑な編集では、Composerインターフェースを使用してマルチファイル変更をプロンプトし、差分を確認し、反復処理できます。
- **エージェントモード**: `Ctrl+I`を押し、（例：「このモジュールのバグを修正」）といった広範なタスクを指示すると、自律的に計画、編集、コマンド実行を行い、ユーザーに状況を伝えます。
- **次の編集提案**: AIは変更内容に基づいて、続けて行う可能性のある編集を予測し提案します。

Cursorは基本無料で、高度なモデルにはProプランがあります。VS Code拡張機能をシームレスにインポートします。

### IntelliJ IDEA with JetBrains AI Assistant
IntelliJ IDEA（および他のJetBrains IDE）には、組み込みのAI Assistantプラグインがあり、コードを選択してAIによる修正や編集を行えます：
- **AIアクションメニュー**: コードを選択し、`Alt+Enter`を押すか右クリックして、「AI Actions」> 「リファクタリングを提案」、「問題を発見」、「AIで修正」などのオプションを選択します。コンテキストを分析し、差分ビューアで変更を提案します。
- **インラインプロンプト**: エディタに直接プロンプト（例：「この関数をリファクタリング」）を入力し、`Tab`を押すと、AIがコードをインラインで生成/編集します。
- **エラー修正**: ハイライトされたエラーに対して、「Fix with AI」を選択すると、コンテキストを考慮した提案が得られます。
- **コード生成/リファクタリング**: メニューから呼び出して、コードの説明、型アノテーションの追加、セクションの再生成などを行います。

AI Assistantを使用するにはJetBrains AIライセンス（無料トライアルあり）が必要で、Mellumなどのモデルによる補完が提供されます。

これらのツールはすべてAIを深く統合していますが、Cursorは最もAI中心、VS Code/Copilotは柔軟で広く使用され、IntelliJのAIはエンタープライズ/Java中心のワークフローに特化しています。お好みのエコシステムに基づいて選択してください。

参考文献:
[GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
[Get started with GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/getting-started)
[Features | Cursor - The AI Code Editor](https://cursor.com/en/features)
[Cursor AI: A Guide With 10 Practical Examples](https://www.datacamp.com/tutorial/cursor-ai-code-editor)
[Use AI in editor | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-ai-in-editor.html)
[AI Assistant in JetBrains IDEs | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/ai-assistant-in-jetbrains-ides.html)
[Use AI prompts to explain and refactor your code | IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/use-prompts-to-explain-and-refactor-your-code.html)