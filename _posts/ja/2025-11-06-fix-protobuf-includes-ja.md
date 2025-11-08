---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 不足しているProtobufインクルードファイルの修正
translated: true
type: note
---

### エラーの理解

この `greptime-proto` (GreptimeTeam リポジトリのコミット `14b9dc40` にピン留め) の失敗は、protobuf のコンパイル中に発生しています。具体的には、`protoc` が標準の Google 既知の型 `google/protobuf/duration.proto` (およびおそらく `timestamp.proto` などの他の型) を見つけることができません。これが波及して、GreptimeDB 自身の protos でインポートエラーが発生します (例: `ddl.proto` が Duration をインポートしているため、`database.proto` で未定義の型エラーが発生します)。

根本原因: あなたの `protoc` インストール (手動アップグレードによるもの) にはバイナリ (`/usr/local/bin/protoc`) のみが含まれており、Google のコア protos を含むインクルードファイルが含まれていません。クレートの `build.rs` 内の `prost-build` は、Google のインクルードへの `--proto_path` を明示的に設定せずに `protoc` を実行するため、`"google/protobuf/duration.proto"` のような相対インポートで失敗します。

これはバイナリのみの protobuf インストールで一般的です。完全な SDK は `/usr/include/google/protobuf/` (または同等のもの) を提供します。

### クイックフィックス: Protobuf インクルードファイルをインストール

最近の `protoc` バイナリを既にお持ちなので、ダウングレードせずに不足しているインクルードファイルを追加してください:

1.  **完全な Protobuf リリースをダウンロード** (お使いの protoc バージョン、例えば 27.3 または最新版に一致するもの):
    ```
    wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip
    unzip protoc-27.3-linux-x86_64.zip -d protoc-full
    ```

2.  **インクルードファイルをインストール**:
    ```
    sudo mkdir -p /usr/local/include/google/protobuf
    sudo cp -r protoc-full/include/google /usr/local/include/
    sudo chmod -R a+r /usr/local/include/google/protobuf  # 読み取り可能性を確保
    rm -rf protoc-full protoc-*.zip  # クリーンアップ
    ```

3.  **検証**:
    *   protoc を確認: `protoc --version` (≥3.21 であるべき)。
    *   インクルードをテスト: `ls /usr/local/include/google/protobuf/duration.proto` (存在するべき)。
    *   簡単なスモークテスト: `protoc --proto_path=/usr/local/include proto/greptime/v1/ddl.proto --decode_raw=stdin < /dev/null` (プロジェクトディレクトリから; 出力は無視し、"File not found" がないことのみ確認)。

4.  **ビルドを再試行**:
    ```
    make clean  # 部分的なビルドをクリア
    make
    ```

`apt` が利用可能なディストリビューション (例: Ubuntu) の場合、代替手段は `sudo apt install libprotobuf-dev` です — しかし、これは古いバージョン (例: 3.12) をインストールし、手動でインストールした protoc と競合する可能性があります。その場合は、手動でのインクルードコピーに固執し、明示的に `PROTOC=/usr/local/bin/protoc` を設定してください。

### 追加のヒント
*   エラーが続く場合 (例: `wrappers.proto` のような他の不足している protos)、完全な `include/google/` コピーがそれらをカバーするはずです。
*   コンテナ化されたビルド (Docker) の場合、これらの手順を Dockerfile に追加してください。
*   ビルド後、`cargo run --bin greptime -- standalone start` でテストし、protos が正しく統合されていることを確認してください。
*   この greptime-proto のリビジョンは最近のもの (2024年10月頃) です。問題が解決しない場合は、リポジトリで上流の修正を確認してください。

[GreptimeDB ビルドドキュメント](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf 既知の型](https://protobuf.dev/reference/protobuf/google.protobuf/)