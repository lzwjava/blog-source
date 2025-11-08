---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: UbuntuへのRustインストール
translated: true
type: note
---

### Ubuntu 22.04 LTS への Rust インストール

Rust をインストールする最も良い方法は、公式ツールチェーンインストーラの `rustup` を使用することです。この方法はシンプルで、簡単な更新をサポートし、64ビットの Ubuntu 22.04 システムで動作します。基本的な Ubuntu セットアップ以外に、通常、追加の依存関係は必要ありません。

#### ステップバイステップの手順

1. **パッケージリストの更新** (任意ですが推奨):
   ```
   sudo apt update
   ```

2. **rustup を使用して Rust をインストール**:
   以下のコマンドを実行して、インストーラスクリプトをダウンロードし実行します:
   ```
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
   - これは HTTPS 経由でスクリプトを安全にダウンロードします。
   - プロンプトが表示されたら、デフォルトのインストールオプションを選択します (`1` を押して Enter)。
   - インストーラは Rust バイナリを `~/.cargo/bin` に追加し、シェルプロファイル (例: `~/.bashrc` または `~/.profile`) を更新します。

3. **シェル設定の再読み込み**:
   ターミナルを再起動せずに変更をすぐに有効にするには:
   ```
   source ~/.cargo/env
   ```
   または、ターミナルを閉じて再度開きます。

4. **インストールの確認**:
   Rust が正しくインストールされたか確認します:
   ```
   rustc --version
   cargo --version
   ```
   `rustc 1.82.0` (または最新の安定版) のような出力と、Cargo についても同様の出力が表示されるはずです。

#### 追加の注意点
- **アンインストール**: 必要に応じて、`rustup self uninstall` を実行してください。
- **Rust の更新**: 最新バージョンを入手するには `rustup update` を使用してください。
- **IDE/サポート**: 開発には、より良いコード補完のために、エディタ (例: VS Code 拡張機能) 経由で `rust-analyzer` をインストールすることを検討してください。
- これはデフォルトで安定版チャネルをインストールします。ナイトリー版またはベータ版には、セットアップ後に `rustup install nightly` を使用してください。

エラーが発生した場合 (例: curl が見つからない)、`sudo apt install curl` でインストールしてください。

[公式 Rust インストールガイド](https://www.rust-lang.org/tools/install)