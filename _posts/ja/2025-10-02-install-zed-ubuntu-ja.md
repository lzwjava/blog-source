---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Ubuntu 24.04にZedをインストール
translated: true
type: note
---

Ubuntu 24.04 LTSでは、Zed（高性能コードエディタ）をインストールする最も簡単で公式な方法は、提供されているシェルスクリプトを使用することです。この方法はDebianベースのUbuntuを含むほとんどのLinuxディストリビューションでネイティブに動作し、依存関係を自動的に処理し、最新の安定版を確実に入手できます。

### 推奨インストール方法: 公式スクリプト
ターミナルで以下を実行:
```
curl -f https://zed.dev/install.sh | sh
```
- これによりZedが`~/.local/bin/zed`にインストールされます（必要に応じてPATHに追加: `~/.bashrc`などで`export PATH="$HOME/.local/bin:$PATH"`）。
- 前提条件: システム（glibc 2.39 on kernel 6.14）が要件を満たしていること（x86_64 glibc >= 2.31）。
- インストール後、`zed`コマンドまたはGNOMEのアプリメニューから起動できます。
- プレビューチャンネル（ナイトリービルド）の場合: `curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`

サンドボックス化されたユニバーサルパッケージ（ネイティブ依存関係の心配なし）を希望する場合は、リストからFlathubオプション（`dev.zed.Zed`）をFlatpakで使用:
1. Flatpakが未インストールの場合: `sudo apt update && sudo apt install flatpak`
2. Flathubリポジトリを追加: `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`
3. インストール: `flatpak install flathub dev.zed.Zed`
4. 実行: `flatpak run dev.zed.Zed`

スクリプトは一般的に高速でGNOMEのようなデスクトップ環境との統合性が高いですが、Flatpakは分離を希望する場合や他のアプリですでに使用している場合に優れています。リストの他のオプションは非Debianディストリビューション向けであり、追加設定なしではUbuntuで直接動作しないため避けてください。

### 参考資料
- [Zed Linuxインストールドキュメント](https://zed.dev/docs/linux)
- [Zed on Linux発表記事](https://zed.dev/linux)
- [Repology Zedパッケージ](https://repology.org/project/zed-editor/versions)