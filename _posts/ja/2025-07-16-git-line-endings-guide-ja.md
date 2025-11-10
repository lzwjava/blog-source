---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Git 改行コード制御ガイド
translated: true
type: note
---

`git config core.autocrlf`は、リポジトリからファイルをチェックアウトするときやコミットするときに、Gitが改行コードをどのように処理するかを制御します。これは、Windowsが改行コードに**CRLF** (`\r\n`)を使用するのに対し、LinuxとmacOSは**LF** (`\n`)を使用するため重要です。この処理がないと、誰が編集するかによってファイルのフォーマットが変わってしまい、「ダーティ」な差分や不要な変更が発生する可能性があります。

---

### 仕組み

* ファイルを**チェックアウト（読み取り）**するとき、Gitは改行コードをあなたのOSの慣習に合わせて変換することがあります（エディタで自然に表示されるように）。
* ファイルを**コミット（書き込み）**するとき、Gitは改行コードをLF（リポジトリ内でのクロスプラットフォーム標準）に変換することがあります。

---

### 設定

以下のコマンドで設定します：

```bash
git config --global core.autocrlf <value>
```

主な値:

* `true`
  チェックアウト時に **LF → CRLF** に変換し、コミット時に **CRLF → LF** に変換します。
  Windowsのエディタでコードを編集する**Windows開発者**に最適です。

* `input`
  チェックアウト時にはファイルを変更**しません**が、コミット時に **CRLF → LF** に変換します。
  LFのみのリポジトリを保証したい**Linux/macOS開発者**に最適です。

* `false`
  一切変換しません。Gitはファイルをあるがままに保存し、チェックアウトします。
  チームやエディタが一貫して改行コードを処理する場合に最適です。

---

### 一般的な推奨設定

* **Windows**:

  ```bash
  git config --global core.autocrlf true
  ```
* **Linux/macOS**:

  ```bash
  git config --global core.autocrlf input
  ```

混合チームの場合、リポジトリに `.gitattributes` ファイルを追加して一貫した改行コードを強制することも有効です。例：

```
* text=auto
```

---

クロスプラットフォームチームでうまく機能する、推奨される **`.gitattributes` セットアップ**もご紹介しましょうか？（`core.autocrlf`のみに依存しないようにするため）