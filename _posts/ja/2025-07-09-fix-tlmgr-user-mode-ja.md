---
audio: false
generated: true
lang: ja
layout: post
title: TeX Live tlmgr ユーザーモードの修正
translated: true
type: note
---

エラーは、Debian/Ubuntuシステムで`tlmgr`ユーザーモードが初期化されていないことを示しています。これはUbuntuリポジトリからのTeX Liveインストールでよくある問題です。修正方法は以下の通りです：

## 解決策1：tlmgrユーザーモードの初期化

まず、ユーザーモードを初期化します：

```bash
tlmgr init-usertree
```

もし動作しない場合は、以下を試してください：

```bash
tlmgr --usermode init-usertree
```

## 解決策2：aptを使用する（Ubuntu推奨）

Ubuntu/Debianを使用している場合、システムのパッケージマネージャーを使用する方が簡単です：

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

これによりFontAwesome5と他のフォントパッケージがインストールされます。

## 解決策3：FontAwesome5が既にインストールされているか確認

既にインストールされている可能性があります。簡単なLaTeXファイルを作成してテストしてください：

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

以下のコマンドでコンパイル：
```bash
pdflatex test.tex
```

## 解決策4：最新バージョンが必要な場合

特に最新のFontAwesome5バージョンが必要な場合は：

1. CTANから手動でパッケージをダウンロード
2. ローカルのtexmfディレクトリにインストール：

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# ダウンロードしたパッケージをこのディレクトリに展開
texhash ~/texmf
```

## クイックチェック

現在インストールされているTeXパッケージを確認するには：

```bash
dpkg -l | grep texlive
```

ほとんどのユーザーにとって、`sudo apt install texlive-fonts-extra`がtlmgrユーザーモードの問題を完全に回避する最も簡単な解決策です。