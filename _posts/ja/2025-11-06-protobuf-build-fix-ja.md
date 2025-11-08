---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: プロトバフコンパイラのビルドエラーを修正
translated: true
type: note
---

### エラーの理解

このビルド失敗は、`greptime-proto` クレート内の Protocol Buffers (`.proto` ファイル) のコンパイル中に発生しています。ビルドスクリプト (`prost-build` を使用) は、これらの proto 定義から Rust コードを生成するために `protoc` バイナリを必要としますが、システム上で見つけることができません。これは、内部通信に gRPC と protobuf に依存する GreptimeDB のようなプロジェクトをビルドする際に、前提条件を見落とす一般的な問題です。

リストされている `.proto` ファイル (例: `database.proto`, `health.proto`) は、メタデータ、リージョン、WAL などの GreptimeDB のコア定義であるため、このステップをスキップするとビルド全体がブロックされます。

### クイックフィックス

1.  **Protobuf コンパイラをインストール** (≥ 3.15 必須):
    - Debian/Ubuntu の場合 (エラーのヒントに一致):
      ```
      sudo apt update
      sudo apt install protobuf-compiler
      ```
    - Fedora/RHEL の場合:
      ```
      sudo dnf install protobuf-compiler
      ```
    - macOS の場合 (該当すれば):
      ```
      brew install protobuf
      ```
    - 手動ダウンロード (クロスプラットフォーム): [Protocol Buffers リリース](https://github.com/protocolbuffers/protobuf/releases) から最新リリースを取得し、展開して `bin/protoc` を PATH に追加します。

2.  **インストールを確認**:
    ```
    protoc --version
    ```
    `libprotoc 3.21.12` のような出力が得られるはずです (またはそれ以上; ≥ 3.15 であれば動作します)。

3.  **ビルドを再試行**:
    ```
    make clean  # オプション、部分的な成果物をクリアするため
    make
    ```
    `protoc` がインストールされているにも関わらず見つからない場合 (例: PATH の問題)、環境変数を設定します:
    ```
    export PROTOC=/usr/bin/protoc  # 必要に応じてパスを調整
    make
    ```

### 追加のヒント
- 他の前提条件が満たされていることを確認してください: Nightly Rust (以前のエラーから持っているようです)、GCC/G++ (`sudo apt install build-essential` でインストール)、glibc 開発ヘッダー (`sudo apt install libc6-dev`)。
- コンテナやカスタム環境にいる場合は、そこにインストールステップを追加してください。
- ビルド後のテスト用: `cargo run --bin greptime -- standalone start`。

これにより、proto のコンパイルを通過できるはずです。もし他のもの (例: C++ の依存関係) で失敗する場合は、完全な前提条件を確認してください。

### 参考資料
- [GreptimeDB GitHub: ソースからビルド](https://github.com/GreptimeTeam/greptimedb#build-from-source)
- [prost-build ドキュメント: Protoc の調達](https://docs.rs/prost-build/#sourcing-protoc)