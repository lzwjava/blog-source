---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Python tarfile モジュール使用ガイド
translated: true
type: note
---

### tarfileモジュールのインポート
Pythonで`tarfile`ライブラリを使用するには、まずインポートします：
```python
import tarfile
```
このモジュールはPythonの標準ライブラリの一部なので、インストールは不要です。POSIX tar形式に基づいており、圧縮または非圧縮のtarアーカイブの読み書きをサポートしています。

### tarアーカイブのオープンと作成
- **既存のtarファイルを開く**: `tarfile.open()`をモード指定で使用します。モードには`'r'`（読み込み）、`'w'`（空の書き込み）、`'a'`（追記）、またはgzip用の`'r:gz'`のような圧縮バリエーションがあります。
  ```python
  import tarfile
  
  # 読み込み用に開く（非圧縮）
  with tarfile.open('example.tar', 'r') as tar:
      # ここでtarを操作
      pass
  ```
- **新しいtarファイルを作成**: `'w'`モードで空のアーカイブを作成します。gzip用の`'w:gz'`やbzip2用の`'w:bz2'`のような圧縮プレフィックスを追加できます。
  ```python
  # 圧縮されたtar.gzファイルを作成
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      pass
  ```

### アーカイブへのファイル追加
- **単一ファイルの追加**: tarファイルオブジェクトで`add()`を呼び出し、ファイルパスを渡します。アーカイブ内での別名をarcnameで指定できます。
  ```python
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      tar.add('file.txt')  # file.txtをそのまま追加
      tar.add('data.csv', arcname='renamed_data.csv')  # アーカイブ内で名前変更
  ```
- **複数ファイルまたはディレクトリの追加**: ループ内で`add()`を使用するか、ディレクトリ全体を再帰的に追加します。
  ```python
  import os
  
  with tarfile.open('backup.tar', 'w') as tar:
      for root, dirs, files in os.walk('my_folder'):
          for file in files:
              tar.add(os.path.join(root, file))
  ```

### アーカイブからのファイル抽出
- **全ファイルの抽出**: `extractall()`を使用して指定したディレクトリに抽出します（デフォルトはカレントディレクトリ）。
  ```python
  with tarfile.open('archive.tar.gz', 'r:gz') as tar:
      tar.extractall(path='extracted_folder')  # 必要に応じてフォルダを作成
  ```
- **特定ファイルの抽出**: まず`getmembers()`でメンバーをリストし、`extract()`を使用します。
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      members = tar.getmembers()
      for member in members:
          if 'important' in member.name:  # フィルタ例
              tar.extract(member, path='output_dir')
  ```
- 注意：セキュリティのため、パストラバーサル攻撃を防ぐためにパスをフィルタリングしてください（例：`..`を避ける）。`tarfile`はいくつかのチェックを行いますが、信頼できないアーカイブでは手動でのフィルタリングが推奨されます。

### アーカイブ内容の一覧表示
- **ファイルの反復処理**: `getmembers()`を使用するか、tarオブジェクトを直接反復処理してTarInfoオブジェクトを取得します。
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      for member in tar.getmembers():
          print(f"{member.name}: {member.size} bytes")
  ```

### 主要モードと圧縮
- `'r'`: 非圧縮tarの読み込み
- `'r:gz'`, `'r:bz2'`, `'r:xz'`: 圧縮形式の読み込み
- `'w'`: 新しい非圧縮tarの書き込み（上書き）
- `'a'`: 既存のtarへの追記
- 読み込み時は圧縮を自動検出、書き込み時は指定が必要

### ヒントとベストプラクティス
- ファイルが確実に閉じられるように、常にコンテキストマネージャ（`with`文）を使用してください
- 大規模なアーカイブの場合、メモリ節約のためフィルタリングや選択的抽出を検討してください
- `tarfile`は暗号化アーカイブを直接扱えません。必要な場合は外部ツールを使用するか、手動で`gzip`と組み合わせてください
- エラーハンドリング：アーカイブの問題には`tarfile.TarError`をキャッチしてください
- 完全なドキュメント：カスタムフィルタなどの高度な機能については、Python公式の[tarfileドキュメント](https://docs.python.org/3/library/tarfile.html)を参照してください