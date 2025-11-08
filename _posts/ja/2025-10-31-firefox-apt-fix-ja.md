---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Firefox APT リポジトリエラーの修正
translated: true
type: note
---

表示されているエラーは、Mozilla Firefox APTリポジトリ（`https://packages.mozilla.org/apt`）に特有の問題で、`binary-all/Packages`インデックスファイルの取得が400 Bad Requestで失敗しています。これは他のUbuntu/Debianユーザーからも報告されている既知の断続的な問題で、プロキシ設定（ローカルプロキシ`127.0.0.1:7890`はClash、V2Rayなどのツールを示唆しており、これらがAPTのHTTPSリクエストを妨害する可能性があります）に関連することが多いです。良い知らせは、APTがこの失敗を無視し、キャッシュされた/古いインデックスを使用するため、システムアップデートはブロックされないことですが、最新のFirefox debパッケージの取得を妨げる可能性があります。

### 試すべき簡単な修正（順不同）
1. **APTキャッシュをクリア**（これにより、破損または古いインデックスファイルが解決され、複数のユーザーで修正されました）:
   ```
   sudo apt clean
   sudo apt update
   ```

2. **APTに対してプロキシを一時的にバイパス**（400エラーはプロキシがリポジトリのHTTPSを妨害していることが原因であることが多いため）:
   ```
   unset http_proxy https_proxy all_proxy
   sudo -E apt update
   ```
   - これを同じターミナルセッションで実行してください。もし動作すれば、`unset`行を`~/.bashrc`に追加する（またはAPTコマンドの直前に実行する）か、プロキシアプリを一時的に無効化することで恒久化できます。
   - プロキシがシステム全体で設定されている場合（例：`/etc/environment`内）、APTを除外するか、一時的に行をコメントアウトするためにそのファイルを編集してください。

3. **APTに対してグローバルにプロキシを無効化**（上記が動作するが、設定して忘れられるオプションが欲しい場合）:
   ```
   echo 'Acquire::http::Proxy "";
   Acquire::https::Proxy "";' | sudo tee /etc/apt/apt.conf.d/99no-proxy
   sudo apt update
   ```
   - これはAPTにプロキシを完全に無視するように指示します。必要に応じて`/etc/apt/apt.conf.d/99no-proxy`を削除して元に戻せます。

### リポジトリなしで最新のFirefoxが必要な場合
リポジトリが失敗し続け、更新されたFirefoxのみを希望する場合:
- **Snapに切り替え**（Ubuntuのデフォルト、簡単なアップデート、リポジトリの手間なし）:
  ```
  sudo snap install firefox
  ```
- **またはFlatpak**（好みの場合）:
  ```
  sudo apt install flatpak
  flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
  flatpak install flathub org.mozilla.firefox
  ```

### 予防/注意点
- Mozillaリポジトリは最先端のFirefox debを取得するための非公式のものです - debが特に必要でない限り、Ubuntuのsnap版を使用することを検討してください。
- これらがどれも動作しない場合は、プロキシログ（例：Clashダッシュボード）で`packages.mozilla.org`への拒否されたリクエストを確認するか、プロキシを完全に外してテストしてください。
- 修正後に`sudo apt update`を再度実行して確認してください。

これらで解決しない場合は、プロキシ設定や`/etc/apt/sources.list.d/mozilla.list`の完全な内容などの詳細を共有して、より深いトラブルシューティングを行ってください。

[Ubuntu 23.10 - Update Problems](https://askubuntu.com/questions/1507571/ubuntu-23-10-update-problems-some-index-files-failed-to-download)  
[Firefox apt repository error](https://www.reddit.com/r/firefox/comments/1ois308/firefox_apt_repository_error/)