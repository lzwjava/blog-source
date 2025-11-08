---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: SubstraitのProtocバージョンエラーを修正
translated: true
type: note
---

### エラーの理解

このビルド失敗は、GreptimeDBがクロスランゲージクエリプランニングに使用する `substrait` クレート（v0.58.0）で発生しています。エラーの原因は、プロトコルバッファコンパイラ (`protoc`) が `substrait/algebra.proto` ファイルを拒否していることです。このファイルは proto3 構文で "optional" フィールドを使用していますが、この機能には以下のいずれかが必要です:

- Protoc バージョン ≥3.21 (サポートが安定しており、特別なフラグは不要)、または
- 古い protoc (例: 3.15–3.20) で、コンパイル時に `--experimental_allow_proto3_optional` フラグを渡すこと。

`substrait` のビルドスクリプト内の `prost-build` ツールはこのフラグを渡さないため、互換性のある protoc バージョンを想定しています。お使いのシステムの `protobuf-compiler` (おそらく Ubuntu 22.04 以前の `apt` からのもの、~3.12.4 を提供) は古すぎてこのフラグをサポートしておらず、パニックを引き起こしています。

GreptimeDB のドキュメントでは protoc ≥3.15 を指定していますが、この依存関係では実質的に ≥3.21 が必要です。

### クイックフィックス: Protoc を ≥3.21 にアップグレード

最も簡単で root 権限が不要な方法は、公式のバイナリリリースをダウンロードしてインストールすることです (コンパイルは不要)。手順は以下の通りです:

1.  **最新の Protoc をダウンロード**:
    - [Protocol Buffers リリース](https://github.com/protocolbuffers/protobuf/releases) にアクセスします。
    - 最新の `protoc-<バージョン>-linux-x86_64.zip` (例: `protoc-28.1-linux-x86_64.zip` または現在の最新版 — ≥3.21 のものであれば何でも可) を取得します。
    - 直接リンクの例 (バージョンは調整してください):  
      `wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip`

2.  **インストール**:
    ```
    unzip protoc-*.zip -d protoc-install
    sudo mv protoc-install/bin/protoc /usr/local/bin/
    sudo chmod +x /usr/local/bin/protoc
    rm -rf protoc-install protoc-*.zip  # クリーンアップ
    ```

3.  **確認**:
    ```
    protoc --version
    ```
    `libprotoc 27.3` (またはそれ以上) が出力されるはずです。まだ古いバージョンが表示される場合は、PATH (`echo $PATH`) を確認してください — `/usr/local/bin` が `/usr/bin` より前にあるべきです。

4.  **ビルドを再試行**:
    ```
    make clean  # 古いターゲットをクリア
    make
    ```

これにより、`apt` パッケージと競合することなく、システムの `protoc` が上書きされます。Ubuntu 24.04+ のような新しいディストリビューションを使用している場合、`apt install protobuf-compiler` で既に ≥3.21 が提供されている可能性があります — まずはお使いのバージョンを再確認してください。

### アップグレードできない場合 (稀なケース)
- 古いシステムに固定されている場合、`substrait` の `build.rs` をパッチして (`Command::new(protoc).arg("--experimental_allow_proto3_optional")` 経由で) フラグを追加する必要がありますが、これにはクレートをフォークし、GreptimeDB の `Cargo.toml` を更新する必要があり、煩雑で推奨されません。
- あるいは、一部のクレートは最近の protoc をバンドルする `protobuf-src` 機能を提供していますが、`substrait` はデフォルトでそれを有効にしていません。

### 追加のヒント
- 他の前提条件を確認してください: `build-essential` (GCC用)、`libc6-dev` (glibc ヘッダ用)。
- ビルドが成功しても、後で C++ の依存関係 (例: Arrow) で失敗する場合は、conda または apt 経由で `libarrow-dev` をインストールしてください。
- CI/CD または Docker の場合: ダウンロードステップを環境に追加してください。

これで問題は解決するはずです — `substrait` は最新の環境ではクリーンにコンパイルされます。別の問題が発生した場合は、`protoc --version` とお使いのディストリビューションを共有してください。

[GreptimeDB ビルドドキュメント](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf リリース](https://github.com/protocolbuffers/protobuf/releases)  
[Proto3 オプショナルフィールド](https://protobuf.dev/programming-guides/proto3/#optional)