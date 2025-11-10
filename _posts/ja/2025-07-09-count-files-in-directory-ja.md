---
audio: false
generated: true
lang: ja
layout: post
title: ディレクトリ内のファイル数を数える
translated: true
type: note
---

ディレクトリ内のファイル数をカウントするには、使用しているオペレーティングシステムやツールに応じて様々な方法があります。以下に一般的なアプローチを紹介します：

### **Windows (コマンドプロンプト)**
```cmd
dir /a-d | find /c /v ""
```
- ディレクトリ以外のすべてのファイルをリストし、空でない行をカウントします。

### **Windows (PowerShell)**
```powershell
(Get-ChildItem -File).Count
```
- ファイルのみを取得してカウントします。

### **Linux/macOS (ターミナル)**
```bash
ls -l | grep ^- | wc -l
```
- ファイルをリスト表示し（`ls -l`）、通常ファイルをフィルタリングし（`grep ^-`）、カウントします（`wc -l`）。

または、よりシンプルに：
```bash
find . -maxdepth 1 -type f | wc -l
```
- カレントディレクトリ内（`-maxdepth 1`）のファイルのみを検索し（`-type f`）、カウントします。

### **Pythonを使用**
```python
import os
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)
```
- ディレクトリの内容をリストし、ファイルをチェックしてカウントします。

お使いの環境に基づいて方法を選択してください。特定のOSやツールについて詳細が必要な場合は、お知らせください！