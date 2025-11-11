---
audio: false
generated: true
lang: ja
layout: post
title: クリーンなZipファイル
translated: true
type: note
---

1. **ZIPファイルを読み込み**、`zipfile.ZipFile`を使用して内部の全ファイルリストを取得します。
2. ディレクトリ（末尾が`/`のエントリ）を保持しつつ、**拡張子のないファイルを除外**します。
3. **除外されたファイルをログ出力**し、ユーザーにどのファイルが除外されたかを通知します。
4. 有効なファイル（拡張子があるファイルまたはディレクトリ）のみを含む**新しいZIPファイルを作成**します。
5. **`argparse`を使用してコマンドライン引数としてZIPファイルのパスを受け取ります**。

これにより、ディレクトリ構造を保持しつつ適切なファイルのみが残ります。🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # 有効なファイルと拡張子のないファイルを分離（ディレクトリは除く）
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("拡張子を持つ有効なファイルが見つかりませんでした。終了します。")
            return
        
        # 除外されたファイルをログ出力
        if removed_files:
            print("以下のファイルを除外します（拡張子が検出されませんでした）:")
            for f in removed_files:
                print(f" - {f}")
        
        # 無効なファイルを除外した新しいZIPファイルを作成
        with zipfile.ZipFile(output_path, 'w') as clean_zip:
            for file in valid_files:
                with zip_ref.open(file) as source:
                    clean_zip.writestr(file, source.read())

    print(f"クリーンアップされたZIPファイルが作成されました: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="拡張子のないファイルを除去してZIPファイルをクリーンアップします")
    parser.add_argument("zip_path", help="入力ZIPファイルのパス")
    args = parser.parse_args()
    clean_zip(args.zip_path)
```