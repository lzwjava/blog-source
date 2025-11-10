---
audio: false
generated: true
image: false
lang: ja
layout: post
title: サスペンドコマンドエラーの解決
translated: true
type: note
---

エラー `sudo: suspend: command not found` は、システムで `suspend` コマンドが利用できないか、インストールされていないことを示しています。`suspend` コマンドは通常、Linux システムをサスペンド（スリープ）状態にするために使用されますが、デフォルトでは存在しないか、ディストリビューションによって異なる名前を持っている可能性があります。

この問題を解決する方法は以下の通りです：

### 1. **正しいコマンドを使用する**
多くの Linux ディストリビューションでは、システムをサスペンドするコマンドは `suspend` ではなく、以下のいずれかです：

- **`systemctl suspend`**:
  これは `systemd` を使用するシステム（例: Ubuntu、Debian、Fedora など）での標準的なコマンドです。
  ```bash
  sudo systemctl suspend
  ```

- **`pm-suspend`**:
  システムが `pm-utils` パッケージを使用している場合、以下を使用できます：
  ```bash
  sudo pm-suspend
  ```
  注: まだインストールされていない場合は、`pm-utils` をインストールする必要があるかもしれません：
  ```bash
  sudo apt-get install pm-utils  # Debian/Ubuntu の場合
  sudo dnf install pm-utils      # Fedora の場合
  ```

- **`echo mem > /sys/power/state`**:
  低レベルなアプローチとして、システムの電源状態に直接書き込むことができます：
  ```bash
  echo mem | sudo tee /sys/power/state
  ```
  これには root 権限が必要であり、カーネル設定によってはすべてのシステムで動作しない可能性があります。

### 2. **`systemd` が利用可能か確認する**
`systemctl suspend` は現代的な Linux ディストリビューションで最も一般的な方法なので、`systemd` が実行されているか確認してください：
```bash
pidof systemd
```
これが PID を返す場合、システムは `systemd` を使用しており、`systemctl suspend` は動作するはずです。そうでない場合は、`pm-suspend` または別の方法を使用する必要があるかもしれません。

### 3. **不足しているツールをインストールする**
`systemctl` も `pm-suspend` も利用できない場合、適切なパッケージをインストールする必要があるかもしれません：
- Ubuntu/Debian の場合：
  ```bash
  sudo apt-get update
  sudo apt-get install pm-utils
  ```
- Fedora の場合：
  ```bash
  sudo dnf install pm-utils
  ```

### 4. **権限を確認する**
十分な権限があることを確認してください。`sudo` コマンドは管理者として実行しようとしていることを示唆していますが、ユーザーが `sudoers` ファイルに含まれているか再確認してください：
```bash
sudo -l
```
権限がない場合は、システム管理者に連絡する必要があるかもしれません。

### 5. **代替方法: デスクトップ環境を使用する**
グラフィカルなデスクトップ環境（例: GNOME、KDE）を実行している場合、GUI を介してシステムをサスペンドできます（例: 電源メニューをクリックして「サスペンド」を選択）。または、以下を使用できます：
- GNOME の場合：
  ```bash
  gnome-session-quit --power-off
  ```
- KDE の場合：
  ```bash
  qdbus org.kde.ksmserver /KSMServer org.kde.KSMServerInterface.logout 0 1 0
  ```

### 6. **ハードウェアサポートを確認する**
一部のシステムは、ハードウェアまたはカーネルの問題によりサスペンドをサポートしていない可能性があります。サスペンドがサポートされているか確認してください：
```bash
cat /sys/power/state
```
出力に `mem` がリストされている場合、サスペンドはサポートされています。そうでない場合は、ハードウェアまたはカーネル設定のトラブルシューティングが必要かもしれません。

### 7. **特定の `suspend` コマンドが必要な場合**
特定の `suspend` コマンド（例: カスタムスクリプトやパッケージの一部）を探している場合、それがインストールされていない可能性があります。検索してください：
```bash
sudo apt-cache search suspend
```
または、別のパッケージの一部かどうかを確認してください。カスタムスクリプトやエイリアスを意図していた場合は、その場所を確認し、実行可能であることを確認してください：
```bash
which suspend
```

### ワークフローの例
典型的な Ubuntu セットアップでシステムをサスペンドするには：
```bash
sudo systemctl suspend
```
これにより、システムは低電力のスリープ状態になります。再開するときは、セッションのロックを解除する必要があるかもしれません。

まだ問題が発生する場合は、使用している Linux ディストリビューションとセットアップに関する追加の詳細を教えてください。より適切なアドバイスを提供できます。

[Ubuntu ドキュメント：電源管理](https://help.ubuntu.com/stable/ubuntu-help/power-suspend.html)
[systemd suspend man ページ](https://www.freedesktop.org/software/systemd/man/systemctl.html)