---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GitHub Copilotのカスタムチャットモード
translated: true
type: note
---

### chatmode.mdとは？

Visual Studio Code（VS Code）の GitHub Copilot 拡張機能において、`chatmode.md` ファイルは **カスタムチャットモード** を定義するために使用されます。これにより、計画立案、セキュリティレビュー、コード実装などのタスクに対して、Copilot Chat が特定のペルソナや動作を採用するように設定できます。各モードは、指示、利用可能なツール（検索、フェッチ、GitHub リポジトリアクセスなど）、さらには使用する AI モデルを指定することができます。この機能は VS Code 1.101 時点でプレビュー段階にあり、ワークフロー全体で一貫性のある応答を実現するのに役立ちます。

カスタムモードは `.chatmode.md` 拡張子を持つ Markdown ファイルとして、ワークスペース（チームで共有するため）またはユーザープロファイル（個人での再利用のため）に保存されます。

### カスタムチャットモードを使用する理由
- **応答のカスタマイズ**: コードを編集せずに計画を生成するなど、ガイドラインを強制できます。
- **ツール制御**: 計画立案ではツールを読み取り専用に制限したり、実装では編集を有効にしたりできます。
- **効率性**: 一般的な役割（例: アーキテクト、レビュアー）に対する設定を再利用できます。

### chatmode.md ファイルの作成方法

1. VS Code で **Chat ビュー**を開きます：
   - タイトルバーの Copilot Chat アイコンをクリックするか、`Ctrl+Alt+I` (Windows/Linux) / `Cmd+Option+I` (macOS) を使用します。

2. Chat ビューで、**Configure Chat > Modes** をクリックし、**Create new custom chat mode file** を選択します。または、コマンドパレット (`Ctrl+Shift+P` / `Cmd+Shift+P`) を開き、**Chat: New Mode File** を実行します。

3. 保存場所を選択します：
   - **ワークスペース**: デフォルトでは `.github/chatmodes/` に保存されます（チームと共有可能）。`chat.modeFilesLocations` 設定でフォルダをカスタマイズできます。
   - **ユーザープロファイル**: プロファイルフォルダに保存され、デバイス間で同期されます。

4. ファイルに名前を付け（例: `planning.chatmode.md`）、VS Code で編集します。

既存のモードを管理するには、**Configure Chat > Modes** または **Chat: Configure Chat Modes** コマンドを使用します。

### ファイル構造と構文

`.chatmode.md` ファイルは Markdown を使用し、メタデータにはオプションで YAML フロントマターを使用します。基本的な構造は以下の通りです：

- **YAML フロントマター** (`---` 行で囲む、オプション）:
  - `description`: チャット入力欄のプレースホルダーおよびドロップダウンのホバー時に表示される短いテキスト。
  - `tools`: ツール名の配列（例: `['fetch', 'search']`）。`githubRepo` などの組み込みツールや拡張機能のツールを使用します。ツールは **Configure Tools** で設定します。
  - `model`: AI モデル（例: `"Claude Sonnet 4"`）。デフォルトは選択されているモデルになります。

- **本文**: AI への指示、ガイドライン、外部ファイルへのリンクなどを含む Markdown 形式の指示。

ツールの優先順位: プロンプトファイル > 参照されたモード > デフォルトモードのツール。

### chatmode.md ファイルの例

これは、コード変更を行わずに実装計画を生成する「Planning」モードを作成します：

```
---
description: 新機能の実装計画または既存コードのリファクタリング計画を生成します。
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
---
# 計画モードの指示

あなたは計画モードです。あなたのタスクは、新機能または既存コードのリファクタリングに対する実装計画を生成することです。コード編集は行わず、計画のみを生成してください。

計画は、以下のセクションを含む Markdown ドキュメントで構成されます：

* **概要**: 機能またはリファクタリングの簡単な説明。
* **要件**: 要件のリスト。
* **実装ステップ**: 実装のための詳細なステップ。
* **テスト**: 検証するテストのリスト。
```

ファイルを保存すると、チャットモードのドロップダウンに表示されます。

### カスタムチャットモードの使用方法

1. 上記のように **Chat ビュー**を開きます。

2. Chat ビューの上部にあるドロップダウン（モードセレクターの隣）で、カスタムモード（例: "Planning"）を選択します。

3. モードの `description` が入力ボックスのプレースホルダーとして表示されます。プロンプトを入力します（例: "ユーザー認証機能の計画を立てて"）。

4. Copilot はモードの指示とツールに従って応答します。ドロップダウンからいつでもモードを切り替えることができます。組み込みモード（Ask, Edit, Agent）も引き続き利用可能です。

その他の例については、[Awesome Copilot リポジトリ](https://github.com/github/awesome-copilot/tree/main)のコミュニティ貢献を確認してください。

### 参考資料
- [VS Code でのカスタムチャットモード](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
- [VS Code でのチャットの開始](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)