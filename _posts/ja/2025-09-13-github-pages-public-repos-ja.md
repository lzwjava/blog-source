---
audio: false
date: 2025-09-13
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: GitHub Pagesは公開リポジトリを必要とします
translated: true
type: note
---

そうですね — GitHub Pages のリポジトリをプライベートにすると、無料の GitHub Pages ホスティングが利用できなくなります。

GitHub Pages は、リポジトリが **パブリック** の場合にのみ自動的に機能します。リポジトリがプライベートの場合、**プライベートリポジトリ用の Pages が有効な GitHub Enterprise プラン**（これは有料機能で、無料または標準の個人アカウントには含まれていません）に加入していない限り、`github.io` サイトは公開されません。

したがって、`username.github.io` の個人ブログの場合：

* **パブリックリポジトリ** → GitHub Pages がビルドされ、`https://username.github.io/` で提供されます。
* **プライベートリポジトリ（無料アカウント）** → GitHub Pages は無効になります。
* **プライベートリポジトリ（Enterprise）** → 引き続き機能しますが、組織がプライベートリポジトリ用の Pages を有効にしている場合に限ります。

回避策（メインリポジトリはプライベートに保ちつつ、`_site` 出力のみを別のパブリックリポジトリに同期して公開する方法など）についても説明しましょうか？