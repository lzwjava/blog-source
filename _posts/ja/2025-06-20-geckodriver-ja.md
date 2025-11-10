---
audio: false
generated: true
lang: ja
layout: post
title: Selenium GeckoDriver Ubuntu インストール
translated: true
type: note
---

UbuntuにSelenium Firefoxドライバ（geckodriver）をインストールするには、以下の手順に従ってください：

1. **Firefoxのインストール**（未インストールの場合）:
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **geckodriverのダウンロード**:
   - [geckodriverリリースページ](https://github.com/mozilla/geckodriver/releases)にアクセス
   - 使用中のFirefoxバージョンと互換性のある最新バージョンを選択。Ubuntuの場合はLinux 64-bit版（例: `geckodriver-vX.XX.X-linux64.tar.gz`）をダウンロード
   - ダウンロードコマンド例（`X.XX.X`は最新バージョンに置き換え）:
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **ダウンロードファイルの展開**:
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **geckodriverをシステムパスに移動**:
   - 展開した`geckodriver`を`/usr/local/bin`に移動してシステム全体でアクセス可能に:
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - 実行権限を付与:
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **Python用Seleniumのインストール**（Pythonを使用する場合）:
   ```bash
   pip install selenium
   ```

6. **インストールの確認**:
   - geckodriverバージョンの確認:
     ```bash
     geckodriver --version
     ```
   - 簡単なPythonスクリプトでのテスト:
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**注意点**:
- Firefoxバージョンとgeckodriverバージョンの互換性を確認（geckodriver GitHubページのリリースノートを参照）
- 問題が発生した場合は`python3-pip`がインストールされているか確認:
  ```bash
  sudo apt install python3-pip
  ```
- geckodriverが見つからない場合は`/usr/local/bin`を`PATH`に追加:
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

これでUbuntuにSelenium Firefoxドライバがセットアップされます。問題が発生した場合はお知らせください！

---

`geckodriver-v0.36.0-linux-aarch64.tar.gz`と`geckodriver-v0.36.0-linux64.tar.gz`の違いは、対象となるCPUアーキテクチャにあります：

- **linux-aarch64**: 64ビットARMアーキテクチャ（ARMv8-Aなど）用。Raspberry Piや一部のサーバー、最新のARMベースLinuxシステムで使用されます。「aarch64」は64ビットARMアーキテクチャを指します

- **linux64**: 64ビットx86アーキテクチャ（x86_64またはAMD64とも呼ばれる）用。標準的なデスクトップPCやサーバーPCで実行されるLinuxシステム向けです

**重要なポイント**:
- システムが64ビットARMプロセッサの場合は`linux-aarch64`を選択
- システムが64ビットx86プロセッサの場合は`linux64`を選択
- Linuxシステムのアーキテクチャは`uname -m`コマンドで確認可能。`aarch64`と出力される場合はARM版を、`x86_64`と出力される場合はlinux64版を使用してください

`.asc`ファイルは、対応する`.tar.gz`ファイルの完全性と信頼性を検証するためのGPG署名です。