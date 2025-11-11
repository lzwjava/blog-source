---
audio: false
generated: true
lang: ja
layout: post
title: npmパッケージのインストール元
translated: true
type: note
---

`@ngx-formly/bootstrap`パッケージのインストールソースをローカルの`.tgz`ファイルからnpmレジストリに変更するには、以下の手順に従ってください。

### 1. ローカルにインストールされたパッケージをアンインストールする
以前にローカルの`.tgz`ファイルから`@ngx-formly/bootstrap`をインストールした場合、現在はプロジェクトの`node_modules`ディレクトリに存在しています。これを削除するには、ターミナルで以下のコマンドを実行してください：

```bash
npm uninstall @ngx-formly/bootstrap
```

このコマンドはパッケージを`node_modules`から削除します。パッケージが`package.json`ファイルの`dependencies`または`devDependencies`に手動で追加されていた場合、そこからも削除されます。`package.json`にリストされていなかった場合（保存せずに`.tgz`ファイルからインストールした場合によくある）、プロジェクトからは削除されます。

### 2. npmレジストリからパッケージをインストールする
次に、npmレジストリからパッケージをインストールします：

```bash
npm install @ngx-formly/bootstrap
```

このコマンドは、npmレジストリ（別のレジストリを設定していない限り、通常は`https://registry.npmjs.org/`）から`@ngx-formly/bootstrap`の最新バージョンを取得し、`node_modules`ディレクトリにインストールします。また、パッケージを`package.json`ファイルの`dependencies`に追加します（最近のnpmバージョンではデフォルト）。これにより、プロジェクトの一部として追跡されます。

### オプション：レジストリの確認（必要な場合）
以前にnpmレジストリを変更したことがあり、デフォルトのnpmレジストリに設定されていることを確認したい場合は、以下で確認できます：

```bash
npm config get registry
```

出力が`https://registry.npmjs.org/`の場合、デフォルトのレジストリを使用しており、`npm install`コマンドは期待通りに動作します。別のレジストリに設定されており、デフォルトに戻したい場合は、以下を実行してください：

```bash
npm config set registry https://registry.npmjs.org/
```

ただし、すでにレジストリを設定済みとのことなので、このステップは必要ないかもしれません。

### 注意点
- **バージョン管理**：`.tgz`ファイルと同じバージョンが必要な場合は、アンインストール前に`node_modules/@ngx-formly/bootstrap/package.json`でバージョン番号を確認してください。その後、特定のバージョンをインストールします：
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  バージョンを指定しない場合、レジストリから最新バージョンがインストールされます。
- **依存関係のタイプ**：通常の依存関係ではなく、開発依存関係としてパッケージをインストールしたい場合は、以下を使用します：
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

これらの手順に従うことで、`@ngx-formly/bootstrap`のインストール方法をローカルの`.tgz`ファイルからnpmレジストリへ正常に切り替えることができます。