---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Ubuntu向けNode.jsアップグレードガイド
translated: true
type: note
---

UbuntuでNode.jsをアップグレードするにはいくつかの方法があります。最も信頼性が高く推奨される方法は、**`nvm` (Node Version Manager)** または **NodeSourceリポジトリ** を使用する方法です。以下に両方の方法のステップバイステップの手順を示します。

---

## **方法1: NVMを使用（推奨）**
NVMを使用すると、複数のNode.jsバージョンを簡単にインストールおよび管理できます。

### 1. NVMのインストール
ターミナルを開いて以下を実行:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
その後、シェルをリロード:
```bash
source ~/.bashrc
```
または
```bash
source ~/.zshrc
```
(使用しているシェルに応じて)

### 2. 最新のNode.jsバージョンをインストール
利用可能なバージョンを一覧表示:
```bash
nvm ls-remote
```
最新のLTSバージョンをインストール（ほとんどのユーザーに推奨）:
```bash
nvm install --lts
```
または特定のバージョンをインストール（例: 20.x）:
```bash
nvm install 20
```

### 3. デフォルトバージョンを設定
```bash
nvm alias default 20
```

### 4. 確認
```bash
node -v
npm -v
```

---

## **方法2: NodeSourceリポジトリを使用**
この方法ではシステム全体にNode.jsをインストールします。

### 1. 古いNode.jsを削除（apt経由でインストール済みの場合）
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. NodeSourceリポジトリを追加
**Node.js 20.x**の場合（2025年8月時点でLTS）:
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
**Node.js 22.x**の場合（利用可能な場合）:
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. Node.jsをインストール
```bash
sudo apt install -y nodejs
```

### 4. 確認
```bash
node -v
npm -v
```

---

## **方法3: Ubuntuデフォルトリポジトリを使用（非推奨）**
Ubuntuのデフォルトリポジトリには古いNode.jsバージョンが含まれることが多いです。それでも使用したい場合:
```bash
sudo apt update
sudo apt install nodejs npm
```
ただし、バージョンが通常古いため、開発には**推奨されません**。

---

## **どの方法を使用すべきか？**
- **NVMを使用**: Node.jsバージョンを簡単に切り替えたい場合、または最新機能が必要な場合
- **NodeSourceを使用**: システム全体に安定したインストールが必要な場合