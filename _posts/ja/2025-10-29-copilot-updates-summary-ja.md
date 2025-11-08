---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GitHub Copilot拡張機能アップデート概要
translated: true
type: note
---

### GitHub Copilot Extension for VS Code (バージョン 1.388.0)

GitHub Copilot 拡張機能のバージョン 1.388.0 は、2025年10月24日にリリースされました。これは、特に最新の VS Code リリース (1.105) との安定性と互換性の向上に焦点を当てたマイナーアップデートのようです。マーケットプレイスや GitHub ブログで具体的なリリースノートは公開されていませんが、ユーザーレポートによると、インライン生成中の不要なコード挿入や、サジェッション中断時の余分なタグ補完などの問題が修正されています。これは、強化されたエージェントモードやモデル選択を含む最近の Copilot 機能とシームレスに統合されます。

#### 過去6か月間の主な更新 (2025年5月～10月)
GitHub Copilot の主要な機能強化は、通常、月次の VS Code リリースと合わせて発表されます。この期間中の拡張機能および関連機能の重要な更新を以下にまとめます。

- **2025年10月 (VS Code 1.105 / 拡張機能 ~1.388)**:
  - Copilot Pro+ サブスクライバー向けに、OpenAI Codex 統合が VS Code Insiders で利用可能に。エディター内で直接高度なコード合成が可能。
  - Copilot コーディングエージェントのタスクをセッション間で割り当て、指示し、追跡するための新しい「ミッションコントロール」インターフェース。
  - エージェントセッションビューが拡張され、ローカルおよびクラウドベースのエージェントを管理する GitHub Copilot CLI をサポート。

- **2025年9月 (VS Code 1.104 / 拡張機能 ~1.38x)**:
  - 実験的な GitHub Copilot-SWE モデルが VS Code Insiders にロールアウト。コード編集、リファクタリング、小規模な変換に最適化。タスク指向で、任意のチャットモードで動作。最適な結果には詳細なプロンプトが推奨。
  - ターミナルエラーのインラインチャットが改善され、説明と修正が向上。

- **2025年8月 (VS Code 1.103 / 拡張機能 ~1.37x)**:
  - マルチラインのコンテキスト認識と、@workspace との統合によるプロジェクト構造全体の生成を備えた、強化されたコミットメッセージのサジェッション。
  - フルビューを開かずに素早く対話できる、軽量なインラインチャットのアップグレード。

- **2025年7月 (VS Code 1.102 / 拡張機能 ~1.36x)**:
  - 単一のプロンプトによるマルチファイル編集の調整が改善。プロジェクト構造を分析して一貫性のある変更を実現。
  - 古いモデル (一部の Claude、OpenAI、Gemini バリアント) が非推奨となり、GPT-4.1 などの新しい高速なオプションが優先。

- **2025年6月 (VS Code 1.101 / 拡張機能 ~1.35x)**:
  - Copilot の動作を再利用可能なガイドラインと組織の知識でカスタマイズするための、プロンプトおよび指示ファイルの導入。
  - GitHub Pull Requests 統合が拡張: VS Code ビューから直接 PR や issue を Copilot に割り当て可能に。進捗追跡のための新しい "Copilot on My Behalf" クエリを追加。

- **2025年5月 (VS Code 1.100 / 拡張機能 ~1.34x)**:
  - エージェントモードに Model Context Protocol (MCP) サポートを追加。サードパーティモデル用のカスタム API キーが使用可能に。
  - OpenAI GPT-4.1 と Anthropic Claude Sonnet による高速なエージェント編集を実現。特に大規模ファイルで効果を発揮。
  - セマンティックコード発見とコードベース全体のサジェッションのための、リポジトリ検索の改善。

これらの更新は、エージェントを活用したワークフロー、モデルのパフォーマンス、そして VS Code エコシステムとのシームレスな統合を重視しています。拡張機能の完全な履歴については、VS Code マーケットプレイスを確認してください。主要な発表は、多くの場合、VS Code の月次リリースサイクルに関連しています。

[GitHub Copilot in VS Code gets upgraded](https://github.blog/changelog/2025-10-28-github-copilot-in-visual-studio-code-gets-upgraded/)  
[Copilot-SWE model rolling out to Visual Studio Code Insiders](https://github.blog/changelog/2025-09-22-copilot-swe-model-rolling-out-to-visual-studio-code-insiders/)  
[GitHub Copilot in VS Code April release (v1.100)](https://github.blog/changelog/2025-05-08-github-copilot-in-vs-code-april-release-v1-100/)  
[GitHub Copilot in VS Code March release (v1.99)](https://github.blog/changelog/2025-04-03-github-copilot-in-vs-code-march-release-v1-99/)  
[September 2025 (version 1.105) - Visual Studio Code](https://code.visualstudio.com/updates)  
[GitHub Copilot Marketplace Page](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)