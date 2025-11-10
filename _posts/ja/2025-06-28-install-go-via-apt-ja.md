---
audio: false
generated: true
lang: ja
layout: post
title: Debian での APT を使用した Go のインストール
translated: true
type: note
---

DebianベースのLinuxシステム（例: Ubuntu）で `apt` を使用してGoをインストールするには、以下の手順に従ってください。`apt` でインストールされるGoのバージョンが古い場合があることに注意してください（例: Ubuntu 22.04では1.18）。プロジェクトの要件を満たしているか確認する必要があります（`~/Projects/clash-core` 内の `go.mod` ファイルで必要なGoのバージョンを確認してください）。

### APTを使用したGoのインストール手順

1. **パッケージインデックスの更新**
   - パッケージリストを最新の状態にします:
     ```bash
     sudo apt update
     ```

2. **Goのインストール**
   - Goパッケージをインストールします:
     ```bash
     sudo apt install golang-go
     ```
   - これにより、Goコンパイラ、ツール、および標準ライブラリがインストールされます。

3. **インストールの確認**
   - インストールされたGoのバージョンを確認します:
     ```bash
     go version
     ```
   - 以下のような出力が表示されます:
     ```
     go version go1.18.1 linux/amd64
     ```
     （バージョンはディストリビューションのパッケージリポジトリによって異なります。）

4. **GOPATHの設定（オプション）**
   - 現代のGoバージョン（1.13以降）ではモジュールを使用するため、`GOPATH` はオプションですが、一部のプロジェクトでは設定しておくと便利です。
   - シェルのプロファイルファイル（例: `~/.bashrc` または `~/.zshrc`）を編集します:
     ```bash
     nano ~/.bashrc
     ```
   - 以下を追加します:
     ```bash
     export GOPATH=$HOME/go
     export PATH=$PATH:$GOPATH/bin
     ```
   - 保存してシェル設定をリロードします:
     ```bash
     source ~/.bashrc
     ```

5. **ビルドの再試行**
   - プロジェクトディレクトリに移動します:
     ```bash
     cd ~/Projects/clash-core
     ```
   - 再度 `make` コマンドを実行します:
     ```bash
     make
     ```

### 注意点
- **バージョンチェック**: プロジェクトが新しいGoバージョン（例: 1.20以降）を必要とする場合、`apt` のバージョンは古い可能性があります。必要なバージョンを `go.mod` またはプロジェクトのドキュメントで確認してください。必要に応じて、tarballを [https://go.dev/dl/](https://go.dev/dl/) からダウンロードして手動でインストールしてください（前回の回答で説明した通り）。
- **代替リポジトリ**: `apt` で新しいバージョンを入手するには、サードパーティのPPA（例: Ubuntuでの `ppa:longsleep/golang-backports`）を追加できます。以下を実行します:
  ```bash
  sudo add-apt-repository ppa:longsleep/golang-backports
  sudo apt update
  sudo apt install golang-go
  ```
- **トラブルシューティング**:
  - `go` が見つからない場合は、`/usr/bin/go` が存在するか確認してください（`ls /usr/bin/go`）。存在しない場合は、`sudo apt install --reinstall golang-go` で再インストールします。
  - 依存関係エラーが発生した場合は、`sudo apt install -f` を実行して修正します。
  - 権限の問題がある場合は、`sudo` 権限があることを確認してください。

### 参考情報
- Ubuntu Goインストールガイド: [https://ubuntu.com/server/docs/programming-go](https://ubuntu.com/server/docs/programming-go)
- 一般的なaptの使用方法: [https://help.ubuntu.com/community/AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)

インストールされたバージョンが古すぎる場合や問題が発生した場合は、お使いのLinuxディストリビューション（例: Ubuntu 22.04）と必要なGoのバージョンをお知らせください。さらに詳しく案内します！