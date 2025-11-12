---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuへのOutlineクライアントのインストール
translated: true
type: note
---

はい、UbuntuにOutline Clientをインストールすることができます。UbuntuはDebianベースのLinuxディストリビューションであり、Outline ClientはDebianパッケージとして提供されており、Ubuntuと互換性があります。インストール方法は2つあります：リポジトリを使用する推奨方法と、Debianパッケージを直接ダウンロードする代替方法です。以下では、推奨されるリポジトリ方法を使用したインストール方法を説明します。この方法は、Ubuntuのパッケージマネージャーと統合され、アップデートの管理が容易になるため好ましい方法です。

### UbuntuへのOutline Clientインストール手順（推奨方法）

以下の手順に従って、UbuntuシステムにOutline Clientをインストールしてください：

1. **ターミナルを開く**  
   Ubuntuシステムでターミナルアプリケーションを起動します。アプリケーションメニューで「ターミナル」を検索するか、`Ctrl + Alt + T`を押して起動できます。

2. **Outlineのリポジトリキーをインストール**  
   以下のコマンドを実行して、リポジトリの署名キーをダウンロードし、システムの信頼済みキーに追加します。これにより、リポジトリからのパッケージが真正性を確認されます：
   ```bash
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   ```

3. **Outline Clientリポジトリを追加**  
   以下のコマンドを実行して、Outline Clientリポジトリをシステムのソースリストに追加します。これにより、UbuntuはOutline Clientパッケージの場所を認識します：
   ```bash
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
   - 注記：`[arch=amd64]`の部分は、64ビットシステム用であることを指定しています。ほとんどの最新Ubuntuインストールは64ビットですが、システムのアーキテクチャは`uname -m`を実行して確認できます。`x86_64`と出力された場合は、64ビットシステムを使用しており、このコマンドはそのまま機能します。

4. **パッケージリストを更新**  
   新しく追加されたOutlineリポジトリを含めるために、システムのパッケージリストを更新します：
   ```bash
   sudo apt update
   ```

5. **Outline Clientをインストール**  
   以下のコマンドで最新バージョンのOutline Clientをインストールします：
   ```bash
   sudo apt install outline-client
   ```

### インストール後

- **Outline Clientの起動**：インストール後、アプリケーションメニューでOutline Clientを見つけるか、ターミナルで`outline-client`と入力して起動できます。
- **アップデートの管理**：アップデートを確認してインストールするには、Ubuntuの標準アップデートコマンドを使用します：
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
  これらのコマンドは、インストールされているすべてのパッケージ（Outline Clientを含む）を更新します。Linux用Outline Clientではバージョン1.15以降、アプリ内自動アップデートは無効化されているため、パッケージマネージャーに依存することが最新版を維持する最良の方法です。
- **アンインストール**：Outline Clientを削除する必要がある場合は、以下を実行します：
  ```bash
  sudo apt purge outline-client
  ```

### 推奨方法を使用する理由

リポジトリ方法が推奨される理由：
- Ubuntuの`apt`パッケージマネージャーと統合され、他のシステムパッケージと一緒にOutline Clientを更新できます。
- 代替方法のように各アップデートごとにダウンロードとインストールプロセスを繰り返す必要がありません。

### 前提条件と要件

- **Ubuntuバージョン**：手順では最小Ubuntuバージョンを指定していませんが、UbuntuはDebianベースでパッケージは64ビットシステムを対象としているため、最近の64ビットUbuntuバージョンであれば動作するはずです。安全のため、開始前にシステムが最新であることを`sudo apt update && sudo apt upgrade`を実行して確認してください。
- **アーキテクチャ**：これらの手順は64ビットシステム（amd64）を想定しています。異なるアーキテクチャ（32ビットやARMなど）を使用している場合、この方法は提供された通りには機能せず、代替パッケージを確認するかOutlineサポートに連絡する必要があります。

### 代替方法（オプション）

リポジトリを追加したくない場合は、Debianパッケージを直接ダウンロードしてインストールできます：
1. パッケージをダウンロード：
   ```bash
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   ```
2. インストール：
   ```bash
   sudo apt install ./outline-client.deb
   ```
ただし、アップデートごとにこのプロセスを手動で繰り返す必要があり、不便です。

### 結論

推奨されるリポジトリ方法を使用すれば、UbuntuにOutline Clientを簡単にインストールし、維持することができます。上記の手順に従うだけで、システムのパッケージマネージャーを通じて簡単にアップデートできる状態で実行可能になります。