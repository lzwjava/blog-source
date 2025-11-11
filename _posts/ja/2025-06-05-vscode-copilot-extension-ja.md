---
audio: false
generated: true
lang: ja
layout: post
title: VSCode拡張機能からGitHub Copilotを呼び出す方法
translated: true
type: note
---

GitHub Copilotは、Visual Studio Code（VSCode）とIntelliJ IDEAにそれぞれのプラグインを通じて統合された強力なAI搭載のコーディングアシスタントです。Copilotを直接呼び出すための公開REST APIは存在しませんが、開発者はVSCode拡張機能内でVSCode Chat API、Language Model API、またはコマンドベースのインタラクションを使用して、その機能をプログラム的に操作できます。このブログ記事では、カスタムプロンプトでCopilotのチャット機能をトリガーし、Copilotへの「API呼び出し」を効果的にシミュレートするVSCode拡張機能の作成方法を解説し、開発を効率化するためにCopilot自体を活用する方法を説明します。

## VSCodeにおけるCopilotの統合を理解する

GitHub Copilotは、直接的なプログラムアクセスのための従来のAPI（例：RESTエンドポイント）を公開していません。代わりに、その機能は以下を通じて利用可能です：
- **VSCode Chat API**：拡張機能がCopilotのチャットシステムと対話するカスタムチャット参加者を作成し、自然言語クエリを処理できます。
- **VSCode Language Model API**：拡張機能がCopilotの大規模言語モデル（LLM）にアクセスし、コード生成や分析などのタスクを実行できます。
- **VSCodeコマンド**：事前定義されたプロンプトでチャットウィンドウを開くなど、Copilotの組み込み機能をトリガーできます。

このガイドでは、Copilotの機能を拡張機能に統合する最も簡単な方法として、`workbench.action.chat.open`コマンドを使用してCopilotのチャットインターフェースをトリガーすることに焦点を当てます。

## ステップバイステップ：CopilotチャットをトリガーするVSCode拡張機能の構築

以下は、カスタムプロンプトでCopilotのチャットウィンドウを開き、ユーザー定義のクエリを処理するためにCopilotを効果的に「呼び出す」VSCode拡張機能を作成するステップバイステップガイドです。

### 1. VSCode拡張機能のセットアップ

1. **プロジェクトのスキャフォールディング**：
   - Yeoman VSCode拡張機能ジェネレーターをインストール：`npm install -g yo generator-code`
   - `yo code`を実行し、「New Extension (TypeScript)」を選択してTypeScriptベースの拡張機能を作成
   - 拡張機能に名前を付ける（例：`copilot-api-caller`）

2. **`package.json`の設定**：
   - Copilotチャットをトリガーするコマンドを定義
   - `package.json`の例：

```json
{
  "name": "copilot-api-caller",
  "displayName": "Copilot API Caller",
  "description": "Triggers GitHub Copilot Chat with a custom prompt",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.85.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onCommand:copilot-api-caller.triggerCopilotChat"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "copilot-api-caller.triggerCopilotChat",
        "title": "Trigger Copilot Chat"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./"
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    "@types/node": "^20.2.5",
    "typescript": "^5.1.3"
  }
}
```

   - **Copilotの活用**：`package.json`を編集中、Copilotは`contributes.commands`や`activationEvents`などのフィールドを入力時に提案する可能性があります。`Tab`キーでこれらを受け入れてセットアップを高速化できます。

### 2. 拡張機能コードの記述

ユーザー提供のプロンプトでCopilotのチャットを開くコマンドを登録する拡張機能ロジックを作成します。

- **ファイル**: `src/extension.ts`
- **コード**:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Copilotチャットをトリガーするコマンドを登録
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // プロンプトのユーザー入力を取得
    const prompt = await vscode.window.showInputBox({
      prompt: 'GitHub Copilotへのクエリを入力',
      placeHolder: '例: 配列をソートするJavaScript関数を書いて'
    });

    if (prompt) {
      try {
        // プロンプトでCopilotチャットを開くコマンドを実行
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('プロンプトをCopilotチャットに送信しました！');
      } catch (error) {
        vscode.window.showErrorMessage(`Copilotチャットのトリガーに失敗しました: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **動作の仕組み**：
  - `copilot-api-caller.triggerCopilotChat`コマンドを登録
  - ユーザーにクエリ（例：「文字列を反転するPython関数を書いて」）の入力を促す
  - `vscode.commands.executeCommand('workbench.action.chat.open', prompt)`を使用して、プロンプトでCopilotのチャットウィンドウを開く
- **Copilotの活用**：VSCodeで`import * as vscode`と入力すると、Copilotは完全なインポートを提案します。`// Copilotチャットを開くコマンドを登録`のようなコメントを追加すると、Copilotは`vscode.commands.registerCommand`構造を提案する可能性があります。コマンド実行では、`// プロンプトでCopilotチャットを開く`と入力すると、Copilotは`executeCommand`呼び出しを提案するかもしれません。

### 3. コンテキストでの拡張（オプション）

拡張機能をより強力にするために、選択されたコードなどエディタからのコンテキストを含め、Copilotに追加情報を提供します。

- **修正されたコード**（`src/extension.ts`）:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // アクティブなエディタから選択されたテキストを取得
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // ユーザー入力のプロンプト
    const prompt = await vscode.window.showInputBox({
      prompt: 'GitHub Copilotへのクエリを入力',
      placeHolder: '例: このコードを説明して',
      value: context ? `このコードについて: \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('プロンプトをCopilotチャットに送信しました！');
      } catch (error) {
        vscode.window.showErrorMessage(`Copilotチャットのトリガーに失敗しました: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **動作の仕組み**：
  - アクティブなエディタから選択されたテキストを取得し、プロンプトのコンテキストとして含める
  - 選択されたコードをMarkdownコードブロックとしてフォーマットし、入力ボックスに事前入力する
  - 結合されたプロンプトをCopilotのチャットインターフェースに送信
- **Copilotの活用**：`// エディタから選択されたテキストを取得`とコメントすると、Copilotは`vscode.window.activeTextEditor`を提案する可能性があります。フォーマットでは、`// コードをmarkdownとしてフォーマット`と入力すると、Copilotはトリプルバッククォート構文を提案するかもしれません。

### 4. 拡張機能のテスト

1. VSCodeで`F5`を押してExtension Development Hostを起動
2. コマンドパレット（`Ctrl+Shift+P`または`Cmd+Shift+P`）を開き、`Trigger Copilot Chat`を実行
3. プロンプトを入力（例：「TypeScriptでREST APIクライアントを生成して」）またはコードを選択してコマンドを実行
4. Copilotのチャットウィンドウがプロンプトで開き、応答を提供することを確認
5. **Copilotの活用**：エラーが発生した場合、`// コマンド実行のエラーを処理`のようなコメントを追加すると、Copilotはtry-catchブロックやエラーメッセージを提案する可能性があります。

### 5. 高度な使用法：VSCode Chat APIの使用

より制御が必要な場合は、VSCode Chat APIを使用してCopilotの言語モデルと統合するカスタムチャット参加者を作成し、拡張機能内で自然言語処理を可能にします。

- **コード例**（`src/extension.ts`）:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // チャット参加者を登録
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('クエリを処理中...\n');
    // Language Model APIを使用して応答を生成
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('適切なモデルが利用できません。');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **動作の仕組み**：
  - Copilotチャットビューで呼び出し可能なチャット参加者（`@copilot-api-caller.myParticipant`）を作成
  - Language Model APIを使用してCopilotの`gpt-4`モデル（または他の利用可能なモデル）にアクセスし、プロンプトを処理
  - 応答をチャットビューにストリーミングで返す
- **Copilotの活用**：`// Copilot用のチャット参加者を作成`とコメントすると、Copilotは`vscode.chat.createChatParticipant`構造を提案する可能性があります。Language Model APIでは、`// CopilotのLLMにアクセス`とコメントすると、Copilotは`vscode.lm.selectChatModels`を提案するかもしれません。

### 6. パッケージ化とデプロイ

1. `vsce`をインストール：`npm install -g @vscode/vsce`
2. `vsce package`を実行して`.vsix`ファイルを作成
3. VSCodeで拡張機能ビューを介して拡張機能をインストールするか、`.vsix`ファイルを他のユーザーと共有
4. **Copilotの活用**：`package.json`に`// 拡張機能をパッケージ化するスクリプトを追加`のようなコメントを追加すると、Copilotは`vscode:prepublish`スクリプトを提案する可能性があります。

## 開発中のCopilotの活用

GitHub Copilotは拡張機能開発を大幅に高速化できます：
- **コード提案**：`src/extension.ts`で入力すると、Copilotはインポート、コマンド登録、エラー処理を提案します。例えば、`vscode.commands.`と入力すると、`registerCommand`のような提案が表示されます。
- **プロンプトエンジニアリング**：`// ユーザープロンプトでCopilotチャットをトリガー`のような明確なコメントを使用して、Copilotの提案を導きます。提案が不正確な場合はコメントを改良します。
- **デバッグ**：拡張機能が失敗した場合、`// エラーの詳細をログ`のようなコメントを追加すると、Copilotは`console.log`や`vscode.window.showErrorMessage`を提案する可能性があります。

## 制限事項

- **直接APIアクセス不可**：Copilotは公開REST APIを公開していません。VSCode Chat APIとLanguage Model APIが主なプログラムインターフェースです。
- **認証**：ユーザーはアクティブなCopilotサブスクリプション（無料または有料）を持ち、GitHubアカウントでVSCodeにサインインしている必要があります。
- **Chat APIの範囲**：Chat APIはチャットインターフェースに限定されています。Copilotのコード補完エンジンへの直接アクセスはプログラム的に利用できません。
- **環境**：拡張機能がカスタムVSCode拡張機能に関する組織ポリシーに準拠していることを確認してください。

## 結論

VSCodeのコマンドシステムまたはChat APIを使用することで、開発者はカスタム拡張機能からGitHub Copilotを効果的に「呼び出し」、そのAI機能とのプログラム的な対話を可能にできます。上記の例は、カスタムプロンプトでCopilotのチャットをトリガーする方法を示し、エディタのコンテキストで強化され、Language Model APIを使用したより高度な統合の基盤を提供します。開発中のCopilotの支援により、このような拡張機能の作成はより迅速かつ直感的になります。

さらなる探求のために、カスタム参加者のためのChat APIの実験や、より豊富なプロンプトのための追加のエディタコンテキストの統合を検討してください。Happy coding!