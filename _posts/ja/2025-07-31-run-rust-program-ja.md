---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ディレクトリからのRustプログラム実行
translated: true
type: note
---

提供されたディレクトリ構造からシンプルなRustプログラムを実行するには、Rustプロジェクト（`lzwjava.github.io/rust`）内で作業しているようで、`src`フォルダに`main.rs`と`simple.rs`が含まれています。以下は、`main.rs`または`simple.rs`のコードを実行する方法です。

### Rustプログラムの実行手順

1. **プロジェクト構造の確認**:
   - プロジェクトには`Cargo.toml`ファイルがあり、Cargo（Rustのビルドツール）で管理されているRustプロジェクトであることを示しています。
   - `src/main.rs`ファイルは、Rustバイナリアプリケーションのデフォルトエントリーポイントです。
   - `simple.rs`ファイルはおそらくモジュールまたは別のソースファイルですが、`main.rs`で参照されるか`Cargo.toml`でバイナリとして設定されない限り直接実行できません。

2. **Cargoを使用したプログラムの実行**:
   - `src/main.rs`のコードを実行したい場合、プロジェクトルート（`~/projects/lzwjava.github.io/rust`）から次のコマンドを使用します:
     ```bash
     cargo run
     ```
     このコマンドは:
     - プロジェクトをコンパイルします（依存関係の解決とコードのビルド）。
     - `src/main.rs`から生成されたバイナリを実行します。
     - 出力はターミナルに表示されます。

3. **`simple.rs`を実行したい場合**:
   - デフォルトでは、Cargoはメインエントリーポイントを`src/main.rs`と想定します。`simple.rs`がモジュールの場合、`main.rs`で参照する必要があります。例:
     ```rust
     mod simple; // simpleモジュールを宣言

     fn main() {
         simple::some_function(); // simple.rsの関数を呼び出し
     }
     ```
     その後、上記のように`cargo run`を実行します。
   - `simple.rs`がスタンドアロンバイナリとして意図されている場合、`Cargo.toml`で設定する必要があります:
     ```toml
     [[bin]]
     name = "simple"
     path = "src/simple.rs"
     ```
     その後、以下を実行:
     ```bash
     cargo run --bin simple
     ```

4. **代替案: Cargoなしでの実行**:
   - 単一ファイル（例: `simple.rs`）をCargoなしでコンパイル・実行したい場合、`main`関数があることを確認し、`rustc`コンパイラを使用します:
     ```bash
     rustc src/simple.rs
     ./simple
     ```
     これにより、カレントディレクトリに`simple`という名前の実行ファイルが生成され、実行されます。注: この方法は依存関係を扱えないため、シンプルで自己完結したプログラムにのみ適しています。

5. **エラーの確認**:
   - エラーが発生した場合、以下を確認してください:
     - RustとCargoがインストールされていること（`rustc --version`と`cargo --version`で確認）。
     - `Cargo.toml`が必要な依存関係で正しく設定されていること。
     - `main.rs`または`simple.rs`のコードに有効な`fn main()`関数があること。
   - バイナリをビルドせずにコードを検証するには`cargo check`を実行:
     ```bash
     cargo check
     ```

6. **`simple.rs`の例**:
   `simple.rs`に以下のような内容が含まれている場合:
   ```rust
   fn main() {
       println!("Hello from simple!");
   }
   ```
   かつ`Cargo.toml`でバイナリとして追加されている場合、`cargo run --bin simple`を実行すると`Hello from simple!`と表示されます。

### 注意点
- `target/debug`ディレクトリにはコンパイルされた成果物が含まれています。バイナリを直接`./target/debug/<project_name>`で実行できますが（`<project_name>`は`Cargo.toml`の名前に置き換え）、`cargo run`の方がコンパイルと実行を扱うため推奨されます。
- `simple.rs`がモジュールの場合、`mod simple;`で正しく`main.rs`に統合されていることを確認してください。
- より複雑な設定や`simple.rs`の特定のコードについては、`simple.rs`や`Cargo.toml`の内容を共有していただければ、具体的なガイダンスを提供します。

「run simple here」で特定の意味（特定の関数や設定など）を意図していた場合は、詳細を提供していただければ回答を調整します！