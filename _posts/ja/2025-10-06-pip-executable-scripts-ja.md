---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: パイプパッケージへの実行可能スクリプトの追加
translated: true
type: note
---

### Python Pip パッケージで実行可能スクリプトを作成する

Python パッケージに実行可能スクリプト（コマンドラインツールなど）を含め、`pip` 経由でインストールできるようにするには、パッケージの設定ファイルで **エントリーポイント** を定義します。これにより、ユーザーはインストール後にスクリプトを直接実行できるようになります（例: ターミナルで `my-script`）。

簡単な例を使用します: `greet` という挨拶を表示するスクリプトを持つ `mytools` というパッケージです。

#### ステップ 1: パッケージ構造を設定する
以下のようなディレクトリ構造を作成します:

```
mytools/
├── pyproject.toml          # 現代的な設定ファイル (setup.py よりも推奨)
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # パッケージ化します
        └── greet.py        # スクリプトのロジック
```

`src/mytools/__init__.py` 内 (空またはバージョン情報を記載):
```python
__version__ = "0.1.0"
```

`src/mytools/greet.py` 内 (スクリプトが呼び出す関数):
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### ステップ 2: `pyproject.toml` でエントリーポイントを設定する
`[project.scripts]` セクションを使用してコンソールスクリプトを定義します。これにより、pip は実行可能なラッパーを作成します。

```toml
[build-system]
requires = ["hatchling"]  # または "setuptools", "flit" など
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "A simple tool package"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # 依存関係をここに追加、例: "requests"

[project.scripts]
greet = "mytools.greet:main"  # 形式: script_name = package.module:function
```

- `greet` はユーザーが実行するコマンドです (例: `greet Alice`)。
- `mytools.greet:main` は `greet.py` 内の `main()` 関数を指します。

古い `setup.py` を好む場合 (まだ機能しますが、推奨度は低い):
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... description, install_requires などの他のフィールド
)
```

#### ステップ 3: パッケージをビルドしてインストールする
1. ビルドツールをインストール: `pip install build twine` (またはそのバックエンドを使用する場合は `hatchling`)。

2. パッケージをビルド:
   ```
   python -m build
   ```
   これにより、`.tar.gz` と `.whl` ファイルを含む `dist/` が作成されます。

3. ローカルにインストールしてテスト:
   ```
   pip install -e .  # 編集可能モード (変更が即時反映されます)
   ```
   クリーンなインストールの場合: `pip install dist/mytools-0.1.0-py3-none-any.whl`。

4. テスト: ターミナルで `greet Alice` を実行します。"Hello, Alice!" と出力されるはずです。

#### ステップ 4: 配布 (オプション)
- PyPI にアップロード: `twine upload dist/*` (PyPI アカウントが必要です)。
- ユーザーは `pip install mytools` を実行し、`greet` を実行できます。

#### ヒント
- **複数のスクリプト**: `[project.scripts]` に行を追加します、例: `another-script = mytools.other:main`。
- **引数**: より良い CLI 処理のために `main()` 内で `argparse` を使用します。
- **依存関係**: それらを `[project.dependencies]` にリストします (例: CLI フレームワーク用の `click`)。
- **仮想環境**: 常にそれを使用します (`python -m venv env; source env/bin/activate`) ことで競合を避けます。
- **エラー?** 詳細については `pip install --verbose` を確認してください。関数が引数を取らない (または `sys.argv` を処理する) ことを確認してください。

より高度な設定 (例: Poetry や Flit を使用) については、公式ドキュメントを確認してください。

#### 参考文献
- [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
- [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)