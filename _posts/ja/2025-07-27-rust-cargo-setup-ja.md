---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Rustプロジェクトセットアップの修正
translated: true
type: note
---

提供された `Cargo.toml` スニペットとファイル構造（`rust` サブディレクトリ内の `example.rs`）に基づいて、シンプルな Rust プロジェクトをセットアップして実行しようとしているようですが、いくつかの問題があり、すぐには動作しません：

- ディレクトリ `/Users/lzwjava/projects/lzwjava.github.io`（あなたの GitHub Pages ルート）は、まだ有効な Rust ワークスペースとして設定されていないため、先ほど rust-analyzer が失敗しました。
- `Cargo.toml` の `edition = "2025"` は無効です。Rust の現在のエディションは 2015、2018、2021、そして 2024（2025年初頭にリリース）です。2025 エディションは利用できません。
- Cargo で管理される Rust プロジェクトは標準的な構造を想定しています：ルートに `Cargo.toml`、ソースファイルは `src/` サブディレクトリ内（例：バイナリ実行ファイルの場合は `src/main.rs`）。あなたの `example.rs` は `rust/` サブディレクトリ内にあり、これはデフォルトでは認識されません。
- `example.rs` がシンプルな実行可能プログラム（例：`fn main()` を含む「Hello, World!」）を含むと仮定すると、主に2つの選択肢があります：シングルファイルスクリプトとして実行する（Cargo 不要）か、適切な Cargo プロジェクトとしてセットアップするかです。

両方のアプローチをステップバイステップで説明します。プロジェクトのルートディレクトリ（`lzwjava.github.io`）でターミナルを使用してください。

### オプション 1: シングルファイルスクリプトとして実行（最速、Cargo 不要）
これは Rust コンパイラ（`rustc`）を使用して `example.rs` を直接コンパイルして実行します。依存関係や完全なプロジェクト設定が不要な場合に理想的です。

1. ファイルを含むディレクトリに移動します：
   ```
   cd rust
   ```

2. ファイルをコンパイルします：
   ```
   rustc example.rs
   ```
   - これにより、`example`（macOS/Linux）または `example.exe`（Windows）という名前の実行ファイルが生成されます。
   - コンパイルが失敗した場合（例：`example.rs` の構文エラーによる）、コードを修正して再試行してください。

3. 実行ファイルを実行します：
   ```
   ./example
   ```
   - 出力は `example.rs` の内容に依存します（例：「Hello, World!」）。

`example.rs` がライブラリ（`fn main()` なし）の場合、これは動作しません。その場合は、プロジェクト設定で `cargo test` を使用してください。

### オプション 2: Cargo プロジェクトとしてセットアップして実行（rust-analyzer と拡張性のために推奨）
これは有効なワークスペースを作成することで rust-analyzer のエラーを修正します。また、`cargo run` を使用して簡単にビルド/実行できるようにします。

1. 専用のプロジェクトディレクトリを作成または移動します（GitHub Pages ルートを散らかさないように）：
   ```
   mkdir rust_project
   cd rust_project
   ```
   - 既存の `rust` ディレクトリを使用する場合は、代わりに `cd rust` として進めてください。

2. 提供された内容で `Cargo.toml` を作成しますが、エディションを修正します：
   ```
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"  # 無効な "2025" から変更
   authors = ["lzwjava@gmail.com"]
   description = "A simple Rust example project"

   [dependencies]
   ```
   - これを現在のディレクトリに `Cargo.toml` として保存します。

3. ソースディレクトリを設定し、ファイルを移動します：
   ```
   mkdir src
   mv ../rust/example.rs src/main.rs  # 必要に応じてパスを調整；バイナリ実行のために main.rs に名前変更
   ```
   - `example.rs` がメインエントリーポイントでない場合は、代わりに `lib.rs` に名前を変更し、ライブラリクレートのために `Cargo.toml` に `[lib]` を追加してください。

4. プロジェクトをビルドします：
   ```
   cargo build
   ```
   - これにより、必要なクレート（ここではなし）がダウンロードされ、コンパイルされます。失敗した場合は、`src/main.rs` のエラーを確認してください。

5. プロジェクトを実行します：
   ```
   cargo run
   ```
   - 必要に応じてビルドし、`src/main.rs` を実行します。

6. VS Code（または類似のエディター）での rust-analyzer エラーを解決するには：
   - `rust_project` フォルダをワークスペースルートとして開きます（**ファイル > フォルダーを開く**）。
   - ウィンドウをリロードします（**Cmd+Shift+P** > **Developer: Reload Window**）。
   - rust-analyzer が `Cargo.toml` を介してプロジェクトを検出するはずです。

### トラブルシューティングのヒント
- **`cargo` がインストールされていない場合**: `rustup update` を実行します（rustup 経由で Rust がインストールされていると仮定）。そうでない場合は、https://rustup.rs/ から Rust をインストールしてください。
- **エディションエラー**: 「2025」を保持し続けると、Cargo は「error: invalid edition: '2025'」と文句を言います。「2024」を使用してください。
- **`example.rs` に `fn main()` がない場合**: 追加してください、例：
  ```
  fn main() {
      println!("Hello, World!");
  }
  ```
- **依存関係が必要ですか？**: `Cargo.toml` の `[dependencies]` の下に追加してください、例：`rand = "0.8"`、その後 `cargo build`。
- **rust-analyzer がまだ失敗しますか？**: エディターの Rust 拡張機能が更新されていることを確認し、プロジェクトがサブディレクトリにある場合はワークスペースの `settings.json` に `"rust-analyzer.linkedProjects": ["./Cargo.toml"]` を追加してください。
- より複雑な設定（例：複数のクレート）の場合、`cargo new --bin example` を使用してテンプレートを生成します。

これがあなたの設定に合わない場合（例：`example.rs` の内容や詳細を提供する）、改良された手順のために知らせてください。

[Announcing Rust 1.88.0](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)  
[Rust | endoflife.date](https://endoflife.date/rust)