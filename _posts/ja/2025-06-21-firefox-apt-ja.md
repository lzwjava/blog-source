---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのAPT経由Firefoxインストール
translated: true
type: note
---

このガイドでは、UbuntuでMozilla APTリポジトリからFirefoxをインストールし、デフォルトのSnapパッケージを置き換える方法について詳しく説明します。

**APT版を使用する理由**

Snap版は便利ですが、より良い統合性とパフォーマンスを求めるユーザーはAPT版を好む場合があります。

**手順:**

1.  **Firefox Snapをアンインストール:**

    ```bash
    sudo snap remove firefox
    ```

2.  **APTキーリングディレクトリを作成 (存在しない場合):**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **Mozilla APTリポジトリ署名キーをインポート:**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *`wget`がない場合は、まずインストール: `sudo apt install wget`*

4.  **sourcesリストにMozillaリポジトリを追加:**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **パッケージ優先度を設定してMozilla DEBを優先:**

    これにより、Ubuntuの移行パッケージがSnapを再インストールするのを防ぎます。

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **Ubuntu Firefox DEBを削除 (存在する場合) し、Mozilla版をインストール:**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

これで、公式Mozilla APTリポジトリからFirefoxがインストールされました！