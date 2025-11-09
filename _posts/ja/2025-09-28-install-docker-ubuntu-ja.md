---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-sonnet-4
title: UbuntuでのDockerインストールガイド
translated: true
type: note
---

お使いのUbuntuシステムの出力に基づき、Dockerをインストールするにはいくつかの選択肢があります。以下に推奨される方法を示します：

## オプション1: Docker Engineのインストール（推奨）

最も一般的で推奨される方法は、Dockerの公式リポジトリからDocker Engineをインストールすることです：

```bash
# パッケージインデックスを更新
sudo apt update

# 前提条件のパッケージをインストール
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Docker公式GPGキーを追加
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Dockerリポジトリを追加
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# パッケージインデックスを再度更新
sudo apt update

# Docker Engineをインストール
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## オプション2: APT経由での簡易インストール（より簡単）

ターミナルに表示された選択肢から、以下のコマンドを使用できます：

```bash
sudo apt install docker.io
```

## インストール後の設定

インストール後、以下の設定を行うことをお勧めします：

1. **Dockerサービスの起動と有効化：**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **ユーザーをdockerグループに追加**（sudoなしでDockerを実行するため）：
```bash
sudo usermod -aG docker $USER
```

その後、ログアウトして再度ログインするか、以下のコマンドを実行します：
```bash
newgrp docker
```

3. **インストールの確認：**
```bash
docker --version
docker run hello-world
```

## どちらのオプションを選ぶべきか？

- **オプション1**はDocker Inc.から直接最新バージョンのDockerを提供します
- **オプション2**はより簡単ですが、Ubuntuのリポジトリから提供されるため若干古いバージョンの場合があります

ほとんどのユーザーにとって、オプション2（`sudo apt install docker.io`）は十分に問題なく、はるかに簡単です。通常の使用ではバージョンの違いはほとんど重要ではありません。

これらの手順の詳細について説明が必要ですか？