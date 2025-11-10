---
audio: false
generated: true
image: false
lang: ja
layout: post
title: プライベート関数エラーの修正
translated: true
type: note
---

エラー `E0603: function run_simple is private` は、`simple.rs` 内の `run_simple` 関数がプライベート（`pub` キーワードが不足している）であるため、`main.rs` からアクセスできないことを示しています。Rustでは、関数はデフォルトでプライベートであり、モジュールの外部からアクセス可能にするには `pub` で明示的に公開する必要があります。

### エラーを修正する手順

1. **`run_simple` を公開する**:
   - `src/simple.rs` を開きます。
   - `run_simple` 関数に `pub` キーワードを追加して、公開します。
   - 例:
     ```rust
     pub fn run_simple() {
         // 既存の関数本体
         println!("Hello from run_simple!");
     }
     ```

2. **適切なモジュール宣言を確認する**:
   - `src/main.rs` で、`simple` モジュールが正しく宣言されていることを確認します:
     ```rust
     mod simple; // simpleモジュールを宣言

     fn main() {
         simple::run_simple(); // 公開関数を呼び出す
     }
     ```

3. **リビルドと実行**:
   - 関数を公開した後、プロジェクトをリビルドします:
     ```bash
     cargo build
     ```
   - ビルドが成功したら、プログラムを実行します:
     ```bash
     cargo run
     ```

4. **他の問題を確認する**:
   - エラーは `src/simple.rs:47:1` を参照しているので、その行の `run_simple` 関数が正しく定義されており、他の問題（構文エラーや依存関係の不足など）がないことを確認してください。
   - `simple.rs` が外部クレートを使用している場合は、それらが `Cargo.toml` の `[dependencies]` にリストされていることを確認してください。

5. **Cargo 警告**:
   - `edition2024` に関する警告は、Rust 1.85 で 2024 edition が安定化されたため、もはや必要のない機能フラグを `Cargo.toml` で使用していることを示唆しています。これをクリーンアップするには、`Cargo.toml` を開き、`edition2024` 機能が存在する場合（例: `[features]` や `cargo-features` の下）は削除します。代わりに、edition を直接設定してください:
     ```toml
     [package]
     name = "example"
     version = "0.1.0"
     edition = "2024"
     ```
   - これにより、非推奨の機能フラグなしで 2024 edition が使用されます。

### ファイルの例

明確にするために、ファイルがどのようにあるべきかの例を示します:

**`src/simple.rs`**:
```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

**`src/main.rs`**:
```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

**`Cargo.toml`** (最小限の例):
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### 追加の注意点
- `run_simple` が他のコードやモジュールに依存している場合、それらも `main.rs` からアクセスされる場合は公開されていることを確認してください。
- エラーが解決しない場合は、`src/simple.rs`（特に47行目付近）と `src/main.rs` の内容を共有していただければ、より具体的なアドバイスができます。
- `rustc --explain E0603` コマンドを実行すると、このエラーに関する詳細なドキュメントが表示され、さらなる理解が深まります。
- `target/debug` ディレクトリには、ビルドが成功した後、コンパイルされたバイナリ (`example`) が含まれます。

これらの手順を試して、さらに問題が発生したらお知らせください！