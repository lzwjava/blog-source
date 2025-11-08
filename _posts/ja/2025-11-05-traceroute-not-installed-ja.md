---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: デフォルトでインストールされないトレースルート
translated: true
type: note
---

TracerouteはLinuxで確実に利用可能です。これはパケットが宛先までたどる経路を追跡する標準的なネットワーク診断ツールです。しかし、多くの現代的なディストリビューション（Ubuntu、Fedora、Debianの最小インストールなど）では、ベースシステムを軽量に保つために、**デフォルトではインストールされていない**ことがよくあります。それが「trac」のタブ補完に表示されない理由です。

### クイックフィックス
パッケージマネージャーからインストールしてください：
- **Debian/Ubuntu**: `sudo apt update && sudo apt install traceroute`
- **Fedora/RHEL/CentOS**: `sudo dnf install traceroute`（古いバージョンでは `sudo yum install traceroute`）
- **Arch**: `sudo pacman -S traceroute`

インストール後、`trac` + Tab と入力すると、`traceroute`がリストに含まれるようになります。その後、`traceroute example.com`のように実行してテストできます。

コンテナ環境や超最小構成のセットアップ（Alpine Linuxなど）を使用している場合、`tr`がエイリアスとして使われているか、別のパッケージが必要な可能性があります。詳細については使用しているディストリビューションをお知らせください！