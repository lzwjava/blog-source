---
audio: false
generated: true
lang: ja
layout: post
title: VSCode拡張機能の作成
translated: true
type: note
---

Visual Studio Code（VSCode）拡張機能の作成は、開発ワークフローを強化したりコミュニティに貢献したりするための充実した方法です。VSCodeプラグインの開発を始めるための包括的なガイドをご紹介します：

### 1. 前提条件
- **Node.jsとnpm**：Node.jsとnpmがインストールされていることを確認してください。[nodejs.org](https://nodejs.org/)からダウンロードできます。
- **YeomanとVSCode拡張機能ジェネレーター**：npmを使用してYeomanとVSCode拡張機能ジェネレーターをグローバルにインストールします。

```bash
npm install -g yo generator-code
```

### 2. 開発環境のセットアップ
- **Visual Studio Codeのインストール**：VSCodeがインストールされていることを確認してください。[code.visualstudio.com](https://code.visualstudio.com/)からダウンロードできます。

### 3. 新しい拡張機能の生成
Yeomanジェネレーターを使用して新しい拡張機能のスキャフォールディングを作成します。ターミナルを開いて以下を実行します：

```bash
yo code
```

プロンプトに従って拡張機能をセットアップします。以下の情報が求められます：
- 拡張機能のタイプ（例：New Extension、New Color Themeなど）
- 拡張機能の名前
- 識別子（例：`my-extension`）
- 説明
- gitリポジトリの初期化
- 言語の選択（TypeScriptまたはJavaScript）
- 必要な依存関係のインストール

### 4. プロジェクト構造の理解
新しい拡張機能は以下の構造になります：
- `.vscode/`：デバッグ用の起動設定が含まれます。
- `src/`：拡張機能のソースコードが含まれます。
- `package.json`：拡張機能のマニフェストファイル。
- `tsconfig.json`：TypeScript設定ファイル（TypeScriptを使用する場合）。

### 5. 拡張機能の作成
- **アクティベーション**：`package.json`の`activationEvents`フィールドで拡張機能がいつアクティブになるかを定義します。
- **コントリビューションポイント**：拡張機能がVSCodeに提供するコマンド、ビュー、言語などを`package.json`の`contributes`セクションで定義します。

### 6. コマンドの実装
ユーザーが呼び出せるコマンドを作成します。`package.json`で定義し、メインの拡張機能ファイル（例：`src/extension.ts`または`src/extension.js`）で実装します。

`package.json`でのコマンドの例：

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

`src/extension.ts`でのコマンドの実装：

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. 拡張機能のデバッグ
- `F5`キーを押して、拡張機能が読み込まれた新しいVSCodeウィンドウを開きます。
- ブレークポイントを設定し、デバッグコンソールを使用して拡張機能をテストします。

### 8. パッケージ化と公開
- **拡張機能のパッケージ化**：`vsce`ツールを使用して拡張機能をパッケージ化します。

```bash
npm install -g vsce
vsce package
```

- **マーケットプレイスへの公開**：[VSCode Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)の指示に従って拡張機能を公開します。

### 9. ドキュメントとベストプラクティス
- **ドキュメント**：`README.md`ファイルで拡張機能の明確なドキュメントを提供します。
- **テスト**：拡張機能が期待通りに動作することを確認するためのテストを作成します。
- **バージョン管理**：拡張機能のリリースではセマンティックバージョニングに従います。

### 10. 追加リソース
- **VSCode APIドキュメント**：[vscode-api](https://code.visualstudio.com/api)
- **拡張機能サンプル**：[vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

これらの手順に従うことで、機能的な有用なVSCode拡張機能を作成する道筋ができます。Happy coding！