---
audio: false
generated: true
image: false
lang: ja
layout: post
title: OpenSSLビルド失敗の修正
translated: true
type: note
---

システムに pkg-config ツールまたは OpenSSL 開発ヘッダーがインストールされていないために、典型的な「openssl-sys」ビルドエラーが発生しています。Ubuntu/Debian では、以下の方法で簡単に修正できます：

1. **pkg-config と OpenSSL 開発ヘッダーをインストール**

   ```bash
   sudo apt update
   sudo apt install pkg-config libssl-dev
   ```

   * `pkg-config` は Rust のビルドスクリプトが OpenSSL の場所を検出できるようにします。
   * `libssl-dev` はヘッダーとライブラリを提供します（「–dev」パッケージ）。

2. **ビルドを再実行**

   ```bash
   cargo clean
   cargo run
   ```

---

### 代替案: 「vendored」機能を使用

システムの OpenSSL に依存したくない場合（または root アクセス権がない場合）、クレートに OpenSSL のバンドル版をソースからビルドするように指示できます：

1. **Cargo.toml** で依存関係を以下のように変更：

   ```toml
   [dependencies]
   openssl = { version = "0.10", features = ["vendored"] }
   ```
2. 再度ビルドを実行：

   ```bash
   cargo clean
   cargo run
   ```

これにより OpenSSL 自体がコンパイルされ、それに対してリンクされるため、システムインストールは不要になります。

---

### （オプション）カスタム OpenSSL インストール

標準以外の場所に OpenSSL がインストールされている場合は、ビルドにその場所を指定できます：

```bash
export OPENSSL_DIR=/path/to/your/openssl
export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib
export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
```

その後、`cargo run` を再実行してください。これにより openssl-sys にヘッダーとライブラリの正確な場所が伝えられます。

---

> **注意:** `edition2024` が安定化されたという警告は無害です。この機能を `Cargo.toml` から削除することはできますが、ビルドを妨げるものではありません。