---
audio: false
generated: true
image: false
lang: ja
layout: post
title: APT GPG署名エラーの修正
translated: true
type: note
---

このエラーは、APTがShiftKeyリポジトリからの更新をGPG署名の検証ができないために拒否していることを意味します。これを修正するには2つの簡単な方法があります：

---

## 1. **壊れたリポジトリを削除または無効化する**

もし実際に `https://apt.packages.shiftkey.dev/ubuntu` が必要ない場合は、単に無効化してください：

```bash
# そのリポジトリを定義しているファイルを探す（/etc/apt/sources.list.d/内にある）
ls /etc/apt/sources.list.d/shiftkey*

# それを削除する（実際のファイル名に置き換えて）
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# その後、更新とインストールを実行
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **リポジトリの署名キーをインポートする**

もしShiftKeyのパッケージを使い続けたい場合は、その公開鍵を取得してインストールする必要があります：

```bash
# GPGキーをダウンロード＆dearmorしてAPTのキーリングに保存
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# リポジトリファイルを編集してそのキーリングを参照するようにする
# /etc/apt/sources.list.d/shiftkey*.list をエディタで開き、deb行を以下に変更：
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# その後、更新とインストールを実行
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

APTがGPGエラーなしで更新できるようになれば、`pkg-config` と `libssl-dev` を自由にインストールし、リビルドできるようになります：

```bash
cargo clean
cargo run
```