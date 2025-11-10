---
audio: false
generated: true
lang: ja
layout: post
title: Rust Edition 2024のエラーを修正
translated: true
type: note
---

エラーメッセージ `feature edition2024 is required` は、あなたのプロジェクトが Rust の `edition2024` を使用するように設定されているが、現在の Cargo バージョン (1.84.1) は安定版リリースではまだこれをサポートしていないことを示しています。Edition 2024 はまだ不安定版/ナイトリー版の機能と見なされています。

修正方法と Cargo の最新バージョンに関する情報は以下の通りです。

### 修正方法

主に2つの選択肢があります。

**1. ナイトリー版 Rust ツールチェーンを使用する (`edition2024` の場合に推奨)**

`edition2024` は不安定な機能であるため、プロジェクトをコンパイルするには Rust と Cargo のナイトリービルドを使用する必要があります。

  * **ナイトリーツールチェーンのインストール:** まだインストールしていない場合は、`rustup` を使用してナイトリーツールチェーンをインストールします:
    ```bash
    rustup toolchain install nightly
    ```
  * **ビルドにナイトリーツールチェーンを使用する:** Cargo に、このコマンドに対して特にナイトリーツールチェーンを使用するように指示できます:
    ```bash
    OPENSSL_STATIC=yes cargo +nightly build --release
    ```
  * **(オプション) プロジェクトのデフォルトをナイトリーに設定する:** このプロジェクトで常にナイトリーを使用したい場合は、プロジェクトのルートディレクトリに `rust-toolchain.toml` ファイルを作成し、以下の内容を記述します:
    ```toml
    [toolchain]
    channel = "nightly"
    ```
    その後、通常通り `OPENSSL_STATIC=yes cargo build --release` を実行するだけで、`rustup` はこのプロジェクトに対して自動的にナイトリーツールチェーンを選択します。

**2. プロジェクトの Edition をダウングレードする (`edition2024` の機能が必須でない場合)**

プロジェクトが `edition2024` の機能に厳密に依存していない場合は、`Cargo.toml` で edition を `2021` (現在の安定版 edition) に戻すことができます。

  * **`Cargo.toml` を編集する:** プロジェクトの `Cargo.toml` ファイル (エラーで示されている `/Users/lzwjava/projects/seeker/seeker/Cargo.toml`) を開き、`edition` フィールドを変更します:
    ```toml
    [package]
    name = "your-package-name"
    version = "0.1.0"
    edition = "2021" # これを "2024" から "2021" に変更
    ```
  * **`cargo fix --edition` を実行する (オプションだが推奨):** edition を変更した後、古い edition との互換性のために一部のコードを自動更新する必要がある場合があります。その場合は `cargo fix --edition` を実行してください。

### Cargo の最新バージョンは？

2025年7月現在、Cargo (および Rust) の最新の**安定**バージョンは **1.88.0** です。

`edition2024` 機能はまだナイトリーチャンネルにあり、これは活発に開発中で、まだ安定版リリースの一部ではないことを意味します。この機能は、将来のリリース、おそらく Rust 1.89.0 (現在ベータ版) で安定化されることが期待されています。