---
audio: false
generated: true
lang: ja
layout: post
title: Windows上のMINGW64におけるパス処理
translated: true
type: note
---

MINGW64はMSYS2プロジェクトの一部であり、Windows上でUnixライクな環境を提供し、bashシェルコマンドやUnixスタイルのツールを使用できるようにします。この環境で作業する際の重要な側面がファイルパスの扱いです。特にWindowsとUnixシステムでは異なる規則が使用されているため注意が必要です。以下では、MINGW64でのパス管理方法、例（スペースを含む場合）、コマンドの絶対パスを使用するタイミングについて説明します。

#### 1. **MINGW64でのパス規則**
- **Windowsパス**: 通常はバックスラッシュを使用（例: `C:\Users`）
- **Unixパス**: スラッシュを使用（例: `/usr/bin`）。MINGW64では、Windowsドライブは`/`の下にマウントされるため、`C:\`は`/c/`に、`D:\`は`/d/`になります
- **一般規則**: MINGW64ではスラッシュを使用したUnixスタイルのパスを優先します。例えば、`C:\Program Files`は`/c/Program Files`と記述します

#### 2. **スペースを含むパスの扱い**
Unixライクなシェル（MINGW64のbashシェルなど）では、スペースは引数を区切る特殊文字です。パスにスペースが含まれる