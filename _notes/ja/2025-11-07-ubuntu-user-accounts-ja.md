---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ubuntuユーザーアカウントの作成
translated: true
---

### Ubuntu Linuxでの新規ユーザー作成

Ubuntuでは、コマンドラインとグラフィカルな方法の両方でユーザーを作成できます。コマンドラインアプローチは簡単で全てのエディション（サーバー含む）で動作し、GUIはデスクトップ版で利用可能です。

#### コマンドライン方法（推奨）
1. ターミナルを開く（Ctrl+Alt+T）
2. 以下のコマンドを実行し、`username`を希望のユーザー名に置き換える：
   ```
   sudo adduser username
   ```
   - これにより、新しいユーザーの強力なパスワード設定が促されます
   - 氏名、部屋番号、勤務先電話番号などのオプション情報も尋ねられます。Enterキーを押してスキップするか、必要に応じて情報を入力してください
3. （オプション）新しいユーザーに管理（sudo）権限を付与する：
   ```
   sudo usermod -aG sudo username
   ```
   - これによりユーザーが`sudo`グループに追加され、昇格した権限でコマンドを実行できるようになります

新しいユーザーは`/home/username`にホームディレクトリを持ち、すぐにログインできます。

#### グラフィカル方法（デスクトップ版のみ）
1. **設定**アプリを開く（アクティビティ概要で検索）
2. サイドバーの**ユーザー**に移動
3. 右上の**ロック解除**をクリックし、管理者パスワードを入力
4. **ユーザーの追加**をクリック
5. アカウントタイプ（標準または管理者）、氏名、ユーザー名、パスワードを入力
6. **追加**をクリック

#### 検証
- `su - username`で新しいユーザーに切り替えるか、ログアウトしてログインし直す
- `cat /etc/passwd | grep username`でユーザーを確認する

この手順はUbuntu 24.04 LTS以降のバージョンで動作します。

[ユーザー管理 - Ubuntu Server documentation](https://documentation.ubuntu.com/server/how-to/security/user-management/)  
[新しいユーザーアカウントの追加 - Ubuntu Documentation](https://help.ubuntu.com/stable/ubuntu-help/user-add.html.en)