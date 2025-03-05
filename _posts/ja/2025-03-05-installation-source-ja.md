---
audio: false
generated: true
lang: ja
layout: post
title: npmパッケージのインストールソース
translated: true
---

`@ngx-formly/bootstrap` パッケージのインストールソースをローカルの `.tgz` ファイルから npm レジストリに変更するには、以下の手順に従ってください。

### 1. ローカルにインストールされたパッケージをアンインストール
以前に `@ngx-formly/bootstrap` をローカルの `.tgz` ファイルからインストールしたため、現在プロジェクトの `node_modules` ディレクトリにあります。これを削除するには、ターミナルで次のコマンドを実行してください：

```bash
npm uninstall @ngx-formly/bootstrap
```

このコマンドは、パッケージを `node_modules` から削除します。パッケージが `package.json` ファイルの `dependencies` または `devDependencies` に手動で追加されていた場合、ここからも削除されます。`.tgz` ファイルからインストールして保存せずにインストールした場合、通常は `package.json` にリストされていないため、プロジェクトから削除されます。

### 2. npm レジストリからパッケージをインストール
次に、npm レジストリからパッケージをインストールするには、次のコマンドを実行してください：

```bash
npm install @ngx-formly/bootstrap
```

このコマンドは、npm レジストリ（通常は `https://registry.npmjs.org/` で、異なるレジストリを設定していない限り）から `@ngx-formly/bootstrap` の最新バージョンを取得し、それを `node_modules` ディレクトリにインストールします。また、パッケージを `dependencies` に追加するため、プロジェクトの一部として追跡されます（最近の npm バージョンではデフォルト）。

### オプション: レジストリの確認（必要に応じて）
以前に npm レジストリを変更し、デフォルトの npm レジストリに設定されていることを確認するには、次のコマンドを実行してください：

```bash
npm config get registry
```

出力が `https://registry.npmjs.org/` の場合、デフォルトのレジストリを使用しており、`npm install` コマンドは予想通りに動作します。異なるレジストリに設定されている場合、デフォルトに戻すには次のコマンドを実行してください：

```bash
npm config set registry https://registry.npmjs.org/
```

ただし、レジストリの設定がすでに完了しているため、この手順は必要ないかもしれません。

### 注意点
- **バージョン管理**: `.tgz` ファイルにあるバージョンと同じバージョンが必要な場合は、アンインストールする前に `node_modules/@ngx-formly/bootstrap/package.json` でバージョン番号を確認し、次のように特定のバージョンをインストールしてください：
  ```bash
  npm install @ngx-formly/bootstrap@<version>
  ```
  バージョンを指定しない場合、レジストリから最新バージョンがインストールされます。
- **依存関係の種類**: 開発依存関係としてパッケージをインストールする場合は、次のように実行してください：
  ```bash
  npm install @ngx-formly/bootstrap --save-dev
  ```

これらの手順に従うことで、`@ngx-formly/bootstrap` をローカルの `.tgz` ファイルからインストールするのではなく、npm レジストリからインストールするように切り替えることができます。