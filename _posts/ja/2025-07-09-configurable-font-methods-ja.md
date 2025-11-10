---
audio: false
generated: true
lang: ja
layout: post
title: LaTeXにおける設定可能なフォント
translated: true
type: note
---

LaTeX文書の先頭で変数を定義することで、フォントを設定可能にすることができます。いくつかの方法を紹介します：

## 方法1：シンプルな変数定義（推奨）

## 方法2：異なるシステム向けの条件分岐を使用

OSの自動検出を備えた、より洗練されたバージョンを作成しましょう：

## 方法3：別設定ファイルの使用

フォント設定用に別ファイルを作成することもできます：

そしてメイン文書では：

## 一般的なLinuxフォント代替案

Linuxシステム向けの優れたフォント代替案をいくつか紹介します：

**中国語/CJKフォント用：**
- `Noto Sans CJK SC`（推奨）
- `Source Han Sans SC`
- `WenQuanYi Micro Hei`
- `Droid Sans Fallback`

**英語フォント用：**
- `Liberation Serif`（Times New Romanの代替）
- `DejaVu Serif`
- `Linux Libertine`
- `TeX Gyre Termes`

## 使用方法

1. **方法1**は最もシンプル - 必要な時にLinuxフォント行のコメントを解除するだけ
2. **方法2**では1つの変数（`\fontsystem`）を変更するだけで異なるシステム間で切り替え可能
3. **方法3**ではフォント設定を分離でき、異なるバージョンの管理が容易

あなたのワークフローに最適な方法を選択してください！