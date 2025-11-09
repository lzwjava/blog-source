---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ubuntu 24.04へのChromiumインストール
translated: true
type: note
---

**Ubuntu 24.04** に **Chromium** をインストールするには、いくつかの良い選択肢があります — **公式の Snap バージョン**、**APT (Debian パッケージ)** バージョン、または**手動ダウンロード**のどれを希望するかによって異なります。以下に、それぞれのクリーンなガイドを示します：

---

### 🧩 オプション 1: Snap 経由でインストール (公式の Ubuntu 方式)

これは **デフォルト** で最も安定した方法です。

```bash
sudo snap install chromium
```

次に、以下で実行します：

```bash
chromium
```

✅ *利点:*

* Canonical によって公式にメンテナンスされています。
* 自動的に更新されます。

⚠️ *欠点:*

* 起動が遅い場合があります。
* Snap のサンドボックス化により、システムプロキシやファイルアクセスに問題が発生する可能性があります。

---

### ⚙️ オプション 2: APT 経由でインストール (Debian パッケージ、非 Snap)

**Snap が嫌いな場合**、**サードパーティのリポジトリ**、例えば **ungoogled-chromium** や **OBS** によって提供される公式 Debian ビルドから Chromium をインストールできます。

1.  OBS リポジトリを追加します：

    ```bash
    sudo apt install wget gnupg
    wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
    ```

2.  リポジトリを追加します：

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
    ```

3.  Chromium をインストールします：

    ```bash
    sudo apt update
    sudo apt install ungoogled-chromium
    ```

次に、以下で実行します：

```bash
ungoogled-chromium
```

✅ *利点:*

* Snap への依存がありません。
* プライバシー強化版が利用可能です。

⚠️ *欠点:*

* Snap よりも更新が遅いです。
* 一部の機能（Google Sync など）は無効化されています。

---

### 🧰 オプション 3: Chromium の公式ビルドからインストール (手動)

**最新の開発者バージョン**が必要な場合：

```bash
sudo apt install chromium-browser
```

もし Snap にリダイレクトされ、それを避けたい場合は：

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

または、手動で `.deb` ファイルをダウンロードします：

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 プロキシ設定に関する注意

お使いのシステムが以下を使用しているため：

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

Snap と APT がプロキシを尊重するように、これらを `/etc/environment` またはシェルのプロファイルでエクスポートしてください：

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

Chromium が自動的にそのプロキシを使用するようにする方法（常にそれを経由して接続するように）を示しましょうか？