---
audio: false
generated: true
lang: ja
layout: post
title: macOSでrustupを使ってRustをインストール
translated: true
type: note
---

## rustupを使用したRustのインストール

1. **ターミナルを開く**  
   ターミナルは**アプリケーション > ユーティリティ**から見つけるか、Spotlightで検索できます。

2. **rustupとRustをインストール**  
   以下のコマンドを実行して、rustupインストールスクリプトをダウンロードして実行します：

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

   スクリプトは続行するか確認します。デフォルトのインストールには`1`を押してください。

3. **シェルの設定**  
   インストール後、Rustをシステムの`PATH`に追加する必要がある場合があります。インストーラーは以下のようなコマンドを提供します：

    ```sh
    source $HOME/.cargo/env
    ```

   この行をシェル設定ファイル（例：`.zshrc`、`.bashrc`、`.bash_profile`）に追加して、将来のセッションでRustが利用できるようにします。

4. **インストールの確認**  
   Rustが正しくインストールされたか確認します：

    ```sh
    rustc --version
    ```

   インストールが成功していれば、Rustコンパイラのバージョンが表示されます。

---

## Homebrewを使用したRustのインストール

別の方法として、[Homebrew](https://brew.sh/)を使用してRustをインストールすることもできますが、`rustup`は通常、更新やバージョン管理が容易なため推奨されます。

1. **Homebrewをインストール**（まだインストールされていない場合）：

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **HomebrewでRustをインストール**：

    ```sh
    brew install rust
    ```

3. **インストールの確認**：

    ```sh
    rustc --version
    ```

---

## Rustコードのコンパイル

1. **Rustプログラムを書く**  
   以下の内容で`main.rs`というファイルを作成します：

    ```rust
    fn main() {
         println!("Hello, World!");
    }
    ```

2. **プログラムをコンパイル**  
   ターミナルで、ファイルを含むディレクトリに移動して実行します：

    ```sh
    rustc main.rs
    ```

3. **コンパイルされたプログラムを実行**：

    ```sh
    ./main
    ```

---

このセットアップで、macOSでのRust開発を始めることができます。問題がある場合は、お気軽にお問い合わせください！