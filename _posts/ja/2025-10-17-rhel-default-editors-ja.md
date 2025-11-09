---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: RHELミニマムのデフォルトテキストエディタ
translated: true
type: note
---

Red Hat Enterprise Linux (RHEL) では、特に最小インストール（サーバーおよび軽量セットアップのデフォルト）の場合、デフォルトで利用可能なテキストエディタは `vim-minimal` パッケージによって提供される **vi** のみです。これにより、ターミナルでファイルを編集するための基本的で互換性のある古典的な `vi` コマンドの実装が利用できます。

- **完全な `vim`**（より多くの機能、シンタックスハイライトなどを備えた拡張版）はデフォルトではインストールされません。`sudo dnf install vim-enhanced` で追加できます。
- **Nano** および **Emacs** は最小インストールには含まれていません。これらはリポジトリで利用可能ですが、明示的なインストールが必要です：
  - Nano の場合: `sudo dnf install nano`
  - Emacs の場合: `sudo dnf install emacs`

これにより、セキュリティとパフォーマンスを優先するため、最小インストールは軽量（合計約200〜300パッケージ）に保たれています。フルデスクトップまたはサーバーインストール（最小ではない）を行う場合、選択した環境に応じてより多くのツールが含まれる可能性があります。

[Nano を使ってみる (Red Hat)](https://www.redhat.com/en/blog/getting-started-nano)  
[なぜ RHEL にはデフォルトで 2 つの vim がインストールされているのですか？](https://unix.stackexchange.com/questions/699071/why-rhel-has-two-vim-installed-by-default)  
[RHEL 9 パッケージマニフェスト](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)