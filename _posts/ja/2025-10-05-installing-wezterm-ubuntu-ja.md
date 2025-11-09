---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: UbuntuへのWezTermインストール
translated: true
type: note
---

エラー「Unable to locate package wezterm」は、WezTermがUbuntuのデフォルトリポジトリで利用できないために発生します。まず公式のサードパーティリポジトリを追加する必要があります。以下はネイティブAPT方式による修正手順です（シームレスな統合のために推奨）：

1. リポジトリのGPGキーを追加：  
   ```
   curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
   ```

2. ソースリストにリポジトリを追加：  
   ```
   echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
   ```

3. キーファイルの権限を適切に設定：  
   ```
   sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
   ```

4. パッケージリストを更新：  
   ```
   sudo apt update
   ```

5. WezTermをインストール：  
   ```
   sudo apt install wezterm
   ```

インストール後は、ターミナルで`wezterm`を実行して起動できます。安定版ではなくナイトリー版（最先端）を使用したい場合は、手順5で`sudo apt install wezterm-nightly`を使用してください（ただし安定版と共存できません）。

### 代替案：Flatpak（リポジトリ不要）
APTソースを変更せずにサンドボックス環境でインストールする場合：  
1. Flatpakが未インストールなら追加：`sudo apt install flatpak`  
2. Flathubを追加：`flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`  
3. インストール：`flatpak install flathub org.wezfurlong.wezterm`  
4. 実行：`flatpak run org.wezfurlong.wezterm`（またはエイリアス追加：`alias wezterm='flatpak run org.wezfurlong.wezterm'`）  

Flatpakは隔離環境のため高度な機能が制限される可能性がありますが、テスト目的ではより簡便です。

[WezTerm Linux Installation Guide](https://wezterm.org/install/linux.html)