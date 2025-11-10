---
audio: false
generated: true
lang: ja
layout: post
title: Rustの出力先オプション
translated: true
type: note
---

素晴らしい質問です！これはRustプロジェクトの典型的な構造とビルド方法に関わる内容ですね。

`rustc`を直接使用する場合、出力先を指定する主な方法は2つあります：

1. **`-o <出力ファイル名>`**: このオプションはコンパイルされた実行ファイルやライブラリの*完全なパスとファイル名*を指定します。

    ```bash
    rustc scripts/rust/example.rs -o test/example
    ```

    これは`example.rs`をコンパイルし、`example`という名前の実行ファイルを`test/`ディレクトリに直接配置します。`test/`が存在しない場合、`rustc`が作成します。

2. **`--out-dir <出力ディレクトリ>`**: このオプションは`rustc`がすべての生成ファイル（実行ファイル/ライブラリ、および`.d`、`.rmeta`などの中間ファイル）を配置する*ディレクトリ*を指定します。

    ```bash
    rustc scripts/rust/example.rs --out-dir test/
    ```

    この場合、`rustc`は`example.rs`をコンパイルし、実行ファイル（デフォルトではソースファイル名から派生した`example`という名前）を`test/`ディレクトリ内に配置します。

**推奨：プロジェクトではCargoを使用**

`rustc`を直接使用すると細かい制御ができますが、ほとんどのRustプロジェクトでは**Cargo**を使用することをお勧めします。CargoはRustのビルドシステム兼パッケージマネージャーで、依存関係の管理、ビルド、テスト、コードの実行を簡素化します。

Cargoを使用すると、出力バイナリは通常プロジェクトルート内の`target`ディレクトリに配置されます。例えば、Cargoで設定されたプロジェクトがある場合：

```
my_project/
├── Cargo.toml
└── src/
    └── main.rs
```

`cargo build`または`cargo run`を実行すると、コンパイルされた実行ファイルは`my_project/target/debug/my_project`（デバッグビルド用）または`my_project/target/release/my_project`（リリースビルド用）に配置されます。

Cargoの`target`ディレクトリを制御したい場合は：

  * **`CARGO_TARGET_DIR`環境変数**:

    ```bash
    CARGO_TARGET_DIR=./test cargo build
    ```

    これにより、`target`ディレクトリ全体（`debug`、`release`などを含む）が`test/`ディレクトリ内に配置されます。実行ファイルは`test/debug/my_project`になります。

  * **Cargoの`--target-dir`コマンドラインオプション**:

    ```bash
    cargo build --target-dir test/
    ```

    これは環境変数と同じことを行います。

  * **`.cargo/config.toml`**: マシン上のすべてのCargoプロジェクトまたは特定のワークスペースに対して、`.cargo/config.toml`ファイルにデフォルトの`target-dir`を設定できます。

**Cargoを使用する理由**

  * **標準化されたプロジェクトレイアウト:** Cargoは共通のプロジェクト構造を強制し、他のRust開発者があなたのコードを理解しやすくします。
  * **依存関係管理:** Cargoはプロジェクトの依存関係のダウンロードとコンパイルを自動的に処理します。
  * **テストとベンチマーク:** Cargoにはテスト（`cargo test`）とベンチマーク（`cargo bench`）を実行するための組み込みコマンドがあります。
  * **リリース管理:** Cargoはリリースビルド（`cargo build --release`）の作成とcrates.ioへのクレートの公開を支援します。

特別な理由がない限り、RustコードをCargoプロジェクトとして整理することを強くお勧めします。

**あなたの`git status`出力から：**

`git status`が`example`と`scripts/rust/`を未追跡として表示していることから、Cargoプロジェクトの外で`scripts/rust/example.rs`を直接`rustc`でコンパイルしている可能性があります。

もし`example`がコンパイルされたバイナリであるなら、前回の`rustc scripts/rust/example.rs`コマンドはそれを現在のディレクトリ（`lzwjava.github.io`）に配置しました。

`test/example`に配置するという目標を達成するには（`test`が`lzwjava.github.io`のルートにあるディレクトリと仮定して）、以下を使用します：

```bash
rustc scripts/rust/example.rs -o test/example
```

これが`rustc`を使用して特定の出力パスを取得する最も直接的な方法です。