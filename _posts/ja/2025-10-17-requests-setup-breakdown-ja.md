---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: リクエストのSetup.pyファイル解説
translated: true
type: note
---

### 概要
これは`setup.py`ファイルで、`setuptools`と共に使用される標準的なPythonスクリプトであり、Pythonパッケージを定義およびビルドするために使用されます。特にこれは、**Requests**ライブラリ（Pythonの人気HTTPクライアント）用のものです。このスクリプトは、パッケージ名、バージョン、依存関係、分類子（PyPI配信用）などのメタデータを処理します。`pip install requests`を実行すると、このスクリプト（またはそのビルド成果物）がバックグラウンドで実行され、パッケージがインストールされます。

このスクリプトは単一の`setup()`関数呼び出しとして構成されていますが、いくつかのガード、ヘルパー、および他のファイルからの動的な読み込みを含んでいます。セクションごとに分解して説明します。

### 1. インポートとPythonバージョンチェック
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # エラーメッセージと終了
    sys.exit(1)
```
- **Shebang (`#!/usr/bin/env python`)**: Unix系システムでファイルを実行可能にし、システムのPythonインタープリターで実行します。
- **インポート**: システムとの相互作用のために`os`と`sys`を持ち込み、非ASCIIを安全に処理するために（UTF-8ファイル読み取り用に）`codecs.open`を持ち込み、パッケージビルドのために`setuptools`から`setup`を持ち込みます。
- **バージョンチェック**: ユーザーがPython 3.9以上を実行していることを確認します。そうでない場合は、アップグレードを提案するか、古いRequestsバージョン（<2.32.0）に固定することを示す有用なエラーメッセージを表示し、コード1（失敗）で終了します。これは互換性を強制します。Requestsは古いPythonのサポートを廃止したためです。

### 2. 公開ショートカット
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- メンテナのための便宜: `python setup.py publish`を実行すると、以下のことを行います:
  - `dist/`フォルダにソースディストリビューション（`sdist`）とホイール（`bdist_wheel`）アーカイブをビルドします。
  - `twine`（安全なアップローダー）を使用してそれらをPyPIにアップロードします。
- これは手動コマンドなしで新しいバージョンをリリースするための迅速な方法です。実行後に終了します。

### 3. 依存関係
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`**: `pip install requests`を実行したときにインストールされるコアの依存関係です。これらはエンコーディング（`charset_normalizer`）、国際化ドメイン名（`idna`）、HTTPトランスポート（`urllib3`）、SSL証明書（`certifi`）を処理します。
- **`test_requirements`**: テストを実行する場合（例: `pip install -e '.[tests]'`経由）にのみインストールされます。HTTPモッキング、カバレッジ、並列テスト用の`pytest`バリアントなどのテストツールを含みます。`PySocks`はテストでのSOCKSプロキシサポート用です。

### 4. 動的メタデータ読み込み
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **`about`辞書**: `exec()`を使用して`src/requests/__version__.py`（例: `__title__`、`__version__`、`__description__`など）からメタデータを読み取ります。これにより、バージョン情報が一元化されます—一度更新すると、`setup.py`がそれを取り込みます。
- **`readme`**: PyPI上のパッケージの長い説明のために、`README.md`ファイル全体を文字列として読み込みます。

### 5. メインの`setup()`呼び出し
これはファイルの核心部分です。パッケージのビルド/インストールを構成します:
```python
setup(
    name=about["__title__"],  # 例: "requests"
    version=about["__version__"],  # 例: "2.32.3"
    description=about["__description__"],  # 短い概要
    long_description=readme,  # 完全なREADME
    long_description_content_type="text/markdown",  # PyPI上でMarkdownとしてレンダリングされる
    author=about["__author__"],  # 例: "Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # 例: GitHubリポジトリ
    packages=["requests"],  # 'requests'パッケージをインストール
    package_data={"": ["LICENSE", "NOTICE"]},  # 非Pythonファイルを含む
    package_dir={"": "src"},  # ソースコードは'src/'内
    include_package_data=True,  # すべてのデータファイルを取り込む
    python_requires=">=3.9",  # バージョンチェックを反映
    install_requires=requires,  # 前述のものから
    license=about["__license__"],  # 例: "Apache 2.0"
    zip_safe=False,  # インストールされたファイルの編集を許可（ライブラリで一般的）
    classifiers=[  # PyPIでの発見可能性のためのカテゴリ
        "Development Status :: 5 - Production/Stable",
        # ... （完全なリストにはPythonバージョン、OS、トピックが含まれる）
    ],
    tests_require=test_requirements,  # `pip install -e '.[tests]'`用
    extras_require={  # オプションの依存関係
        "security": [],  # 空 - 将来の使用のためかもしれない
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # SOCKSプロキシサポート
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # レガシー文字セットフォールバック
    },
    project_urls={  # PyPIページ上のリンク
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **主な引数**:
  - **Name/Version/Description**: メンテナンスを容易にするために`__version__.py`から引き出されます。
  - **Packages/Package Dir**: setuptoolsにパッケージが`src/requests/`の下にあり、`import requests`としてインストールすることを伝えます。
  - **Classifiers**: パッケージを分類する文字列のリスト（例: 安定版、Python 3.9+、Apacheライセンス、Web/HTTPトピック）。これはユーザーがPyPIでそれを見つけるのに役立ちます。
  - **Extras Require**: ユーザーがオプション機能をインストールできるようにします。例えば、プロキシサポートのために`pip install requests[socks]`のようにします。
  - **Project URLs**: PyPIページ上でドキュメントとソースへのクリック可能なリンクを追加します。

### 実際の動作
- **インストール**: `pip install .`（リポジトリから）または`pip install requests`（PyPIから）を実行すると、これが実行され、ファイルがコピーされ、依存関係がインストールされ、パッケージがセットアップされます。
- **ビルド**: `python setup.py sdist`は配布可能なアーカイブを作成します。
- **この構造の理由**: これは「srcレイアウト」（コードが`src/`内）であり、開発中の誤ったインポートを避けるための現代的なベストプラクティスです。このファイルは自己完結型ですが、詳細を`__version__.py`などの他のファイルに委任します。

このsetup.pyは公式のRequestsリポジトリからのもので、バージョンが変わってもあまり変更されていません—信頼性のために十分にテストされています。

### 参考文献
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Requests GitHub Repository](https://github.com/psf/requests)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)