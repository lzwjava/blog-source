---
audio: false
generated: true
lang: ja
layout: post
title: Node.js OpenSSL 互換性
translated: true
---

`ng build`を実行すると、`Node.js 22.9.0`と`npm 10.8.3`で以下のエラーが発生します：

```
error 0308010C digital envelope routines::unsupported
```

このエラーは、Node.jsの新しいバージョン（例：22.9.0、OpenSSL 3.0以降を使用）と、Webpackなどのツールが依存している特定の暗号化アルゴリズムとの互換性問題により、一般的に発生します。以下に、この問題を解決するためのステップバイステップのガイドを示します。

---

### ソリューション

#### ステップ 1: OpenSSL レガシープロバイダーを有効にする
最も簡単で迅速な修正方法は、`NODE_OPTIONS`環境変数を設定してOpenSSLレガシープロバイダーを有効にすることです。これにより、Node.jsがOpenSSL 3.0以降でデフォルトでサポートされなくなった古い暗号化アルゴリズムを使用できるようになります。

- **macOS/Linux**:
  ターミナルを開き、以下を実行します：
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Windows（コマンドプロンプト）**:
  コマンドプロンプトを開き、以下を実行します：
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Windows（PowerShell）**:
  PowerShellを開き、以下を実行します：
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

環境変数を設定した後、`ng build`を再度実行してください。これにより、Node.jsが未サポートのルーチンを処理できるようになり、エラーが解消されるはずです。

---

#### ステップ 2: Angular CLIのバージョンを確認し、必要に応じて更新する
ステップ 1でエラーが解消されない場合、Angular CLIのバージョンがNode.js 22.9.0と完全に互換性がない可能性があります。最新バージョンに更新することで解決することができます。

- 現在のAngular CLIバージョンを確認します：
  ```bash
  ng --version
  ```

- Angular CLIをグローバルに更新します：
  ```bash
  npm install -g @angular/cli
  ```

- そして、`ng build`を再度実行してください。

---

#### ステップ 3: プロジェクトの依存関係を確認し、必要に応じて更新する（オプション）
問題が解決されない場合、プロジェクト内の古い依存関係が原因である可能性があります。これを解決するには：

- `package.json`ファイルを開き、依存関係（例：`@angular/core`、`@angular/cli`など）のバージョンを確認します。
- 互換性のある最新バージョンに慎重に更新します：
  ```bash
  npm install
  ```
  または、すべての依存関係を更新する場合：
  ```bash
  npm update
  ```

- `ng build`を再度実行してテストします。

*注意*: 更新には破壊的な変更が含まれる可能性があるため、更新後はアプリケーションを徹底的にテストしてください。

---

#### ステップ 4: Node.jsをダウングレードする（最終手段）
上記のソリューションがいずれも効果がない場合、Node.js 22.9.0は現在のプロジェクトの設定と完全に互換性がない可能性があります。Long-Term Support (LTS) バージョンのNode.js（例：20.xまたは18.x）にダウングレードすることで問題が解決するかもしれません。

- 現在のNode.jsバージョンをアンインストールします。
- [公式Node.jsウェブサイト](https://nodejs.org/)からLTSバージョンをダウンロードしてインストールします。
- インストールされたバージョンを確認します：
  ```bash
  node -v
  ```
- プロジェクトの依存関係を再インストールします：
  ```bash
  npm install
  ```
- `ng build`を再度実行します。

---

### 推奨されるアプローチ
まず**ステップ 1**（`NODE_OPTIONS`の設定）から始めると、Node.js 22.9.0を引き続き使用できる最も迅速な修正方法です。これが効果がない場合は、**ステップ 2**と**ステップ 3**に進みます。**ステップ 4**は必要な場合にのみ使用してください。Node.jsをダウングレードすると、新しい機能へのアクセスが制限される可能性があります。

これにより、「error 0308010C digital envelope routines::unsupported」エラーが解消され、`ng build`コマンドが再度動作するはずです！