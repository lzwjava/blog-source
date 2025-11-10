---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ラストにおける2024年版の有効化
translated: true
type: note
---

このエラーは、あなたのRustプロジェクトが現在のCargoバージョン（1.75.0）で安定化されていない `edition2024` 機能を使用しようとしているために発生します。これを解決するには、不安定な `edition2024` 機能を明示的にオプトインする必要があります。

### 修正手順:

1. **`edition2024` 機能を有効化**:
   `Cargo.toml` ファイルを開き、`[package]` セクションの前に以下の行を追加してください:

   ```toml
   cargo-features = ["edition2024"]
   ```

   例えば、`Cargo.toml` は以下のようになります:

   ```toml
   cargo-features = ["edition2024"]

   [package]
   name = "your_project_name"
   version = "0.1.0"
   edition = "2024"
   ```

2. **Nightly Rust ツールチェーンを使用**:
   `edition2024` は不安定な機能であるため、安定版（1.75.0など）はこれをサポートしていないため、nightly Rust ツールチェーンを使用する必要があります。以下のコマンドを実行してください:

   ```bash
   rustup update nightly
   rustup override set nightly
   ```

   最初のコマンドは nightly ツールチェーンを更新し、2番目のコマンドはプロジェクトディレクトリで nightly ツールチェーンを使用するように設定します。

3. **ビルドを再実行**:
   これらの変更を行った後、プロジェクトのビルドを再度試してください:

   ```bash
   cargo build
   ```

### 追加の注意点:
- `edition2024` 機能は実験的であり、変更される可能性があります。そのステータスに関する最新情報は Rust ドキュメントを確認してください: [Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)
- `edition2024` が不要な場合は、`Cargo.toml` で安定版のエディション（例: `edition = "2021"`）に戻すことで、nightly ツールチェーンの使用を避けることができます
- `rustup update` を実行して、`rustup` が最新の状態であることを確認してください

さらに問題が発生した場合は、`Cargo.toml` の内容や新しいエラーメッセージを共有していただければ、より具体的なガイダンスを提供できます。

[Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)