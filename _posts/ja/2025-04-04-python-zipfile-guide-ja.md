---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Python ZipFile パッケージガイド
translated: true
type: note
---

### ZipFile パッケージの概要
Pythonの`zipfile`モジュールを使うと、外部ツールなしでZIPアーカイブファイルの読み書きができます。標準ライブラリの一部なので（Python 2.3以降）、インストールは不要です。プログラムでZIPファイルを圧縮、解凍、または操作するために使用します。DEFLATEなどのさまざまな圧縮方式をサポートしています。

インポートは: `import zipfile`

### ZIPファイルの読み込み
既存のZIPファイルを抽出または検査するには:

1. **ZIPファイルを読み込み用に開く**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' は読み込みモード
   ```

2. **内容をリストする**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # ファイル名のリストを返す
       print(file_list)
   ```

3. **ファイルを抽出する**:
   - すべてを抽出: `zip_ref.extractall('destination_folder')`
   - 1つを抽出: `zip_ref.extract('file_inside.zip', 'path')`

4. **抽出せずにファイル内容を読み込む**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('file_inside.zip') as file:
           content = file.read()
           print(content.decode())  # テキストの場合
   ```

注意: 自動クローズのためには常に`with`を使用してください。パスワード保護されたZIPの場合は、`ZipFile()`に`pwd=b'password'`を追加します。

### ZIPファイルの書き込み
新規または既存のZIPファイルを作成または追加するには:

1. **新しいZIPファイルを作成する**:
   ```python
   with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
       # 'w' は書き込みモード (存在する場合は上書き)
   ```

2. **ファイルを追加する**:
   - 1つ追加: `zip_ref.write('source_file.txt', 'arcname.txt')` (オプションのarcnameで内部の名前を変更)
   - 複数追加: ファイルのリストをループして`write()`を呼び出す。

3. **書き込み時に圧縮する** (デフォルトはDEFLATE):
   ```python
   with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('large_file.txt')
   ```
   オプション: `ZIP_STORED` (圧縮なし), `ZIP_DEFLATED`, `ZIP_BZIP2` など。

4. **既存のZIPに追加する** ('w' モードの代わりに 'a' モードを使用)。

### 一般的な操作とヒント
- **ファイルが有効なZIPかチェック**: `zipfile.is_zipfile('file.zip')`を使用。
- **ファイル情報を取得**: `zip_ref.getinfo('file.txt')`は、サイズ、日付などの詳細を含むZipInfoオブジェクトを返す。
- **大きなファイルを扱う**: 大きなファイルの読み込み/抽出はメモリを消費する可能性がある。ストリーミングには`open()`メソッドを使用。
- **エラーハンドリング**: `BadZipFile` または `LargeZipFile` 例外をキャッチ。
- **クロスプラットフォーム**: Windows, macOS, Linuxで動作するが、パス区切り文字に注意 (`/`を使用)。
- **暗号化**: 基本的なパスワード保護はサポートされているが、弱い。セキュリティにはより強力なツールを使用。
- **高レベル**: より多くの機能 (例: shutil連携) には、ZIP作成のために`shutil.make_archive()`と組み合わせる。

フォルダをZIP化する完全なスクリプト例:
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('my_folder', 'output.zip')
```

完全なドキュメントは、[公式Pythonドキュメント](https://docs.python.org/3/library/zipfile.html)を確認してください。特定のタスク (例: 「メモリに抽出する方法」) がある場合は、詳細を提供してください！