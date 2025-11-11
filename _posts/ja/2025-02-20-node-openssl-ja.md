---
audio: false
generated: false
lang: ja
layout: post
title: Node.js OpenSSL 互換性
translated: true
type: note
---

**Node.js 22.9.0** と **npm 10.8.3** を使用して `ng build` を実行すると、以下のエラーが発生します:

```
error 0308010C digital envelope routines::unsupported
```

このエラーは通常、Node.js の新しいバージョン（22.9.0 など、OpenSSL 3.0 以降を使用）と、Angular が内部で使用する Webpack などのツールが依存する特定の暗号化アルゴリズムとの互換性の問題によって発生します。以下に、この問題を解決するためのステップバイステップガイドを示します。

---

### 解決策

#### ステップ 1: OpenSSL レガシープロバイダを有効にする
最も簡単で即効性のある修正方法は、環境変数 `NODE_OPTIONS` を設定して OpenSSL レガシープロバイダを有効にすることです。これにより、Node.js は OpenSSL 3.0+ でデフォルトではサポートされなくなった古い暗号化アルゴリズムを使用できるようになります。

- **macOS/Linux の場合**:
  ターミナルを開いて実行:
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Windows (コマンド プロンプト) の場合**:
  コマンド プロンプトを開いて実行:
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **Windows (PowerShell) の場合**:
  PowerShell を開いて実行:
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

環境変数を設定した後、`ng build` を再度実行してください。これにより、Node.js がサポートされていないルーチンを処理できるようになり、ほとんどの場合でエラーが解決するはずです。

---

#### ステップ 2: Angular CLI の確認と更新（必要な場合）
ステップ 1 の後もエラーが解消しない場合、使用している Angular CLI のバージョンが Node.js 22.9.0 と完全に互換性がない可能性があります。最新バージョンに更新することで改善される場合があります。

- 現在の Angular CLI バージョンを確認:
  ```bash
  ng --version
  ```

- Angular CLI をグローバルに更新:
  ```bash
  npm install -g @angular/cli
  ```

- その後、再度 `ng build` を実行してみてください。

---

#### ステップ 3: プロジェクトの依存関係を確認して更新する（オプション）
それでも問題が解決しない場合、プロジェクト内の古い依存関係が原因である可能性があります。これを解決するには:

- `package.json` ファイルを開き、依存関係（`@angular/core`、`@angular/cli` など）のバージョンを確認します。
- 互換性のある最新バージョンに注意して更新します:
  ```bash
  npm install
  ```
  または、すべての依存関係を更新する場合:
  ```bash
  npm update
  ```

- 再度 `ng build` を実行してテストします。

*注意*: 更新は破壊的変更をもたらす可能性があるため、注意してください。更新後はアプリケーションを十分にテストしてください。

---

#### ステップ 4: Node.js をダウングレードする（最終手段）
上記の解決策のいずれも機能しない場合、Node.js 22.9.0 がプロジェクトの現在の構成でまだ完全にサポートされていない可能性があります。Node.js を **20.x** や **18.x** などの Long-Term Support (LTS) バージョンにダウングレードすることで問題が解決する可能性があります。

- 現在の Node.js バージョンをアンインストールします。
- [公式 Node.js ウェブサイト](https://nodejs.org/) から LTS バージョンをダウンロードしてインストールします。
- インストールされたバージョンを確認:
  ```bash
  node -v
  ```
- プロジェクトの依存関係を再インストール:
  ```bash
  npm install
  ```
- 再度 `ng build` を実行します。

---

### 推奨アプローチ
まずは **ステップ 1**（`NODE_OPTIONS` の設定）から始めてください。これが最速の修正方法であり、Node.js 22.9.0 を使い続けることができます。それでうまくいかない場合は、**ステップ 2**、**ステップ 3** に進んでください。**ステップ 4** は必要に応じてのみ使用してください。Node.js のダウングレードは新しい機能へのアクセスが制限される可能性があります。

これにより "error 0308010C digital envelope routines::unsupported" エラーが解決し、`ng build` コマンドが再び動作するはずです！