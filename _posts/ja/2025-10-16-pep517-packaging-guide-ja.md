---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PEP 517 Python パッケージングガイド
translated: true
type: note
---

PEP 517は2016年に採択され、ビルドバックエンド（ディストリビューション作成のロジック）とフロントエンド（プロセスを調整するpipなどのツール）を分離するPythonパッケージの標準化されたインターフェースを定義します。これにより、開発者はsetuptoolsの`setup.py`のようなレガシーシステムに縛られることなく、モダンなビルドツールを使用できるようになります。PEP 518（ビルド依存関係の指定）と組み合わせることで、ソースツリーやソースディストリビューション（sdist）からの信頼性の高い分離ビルドを実現します。2025年現在、PEP 517はモダンなPythonパッケージングの基盤となっており、pip（PEP 518対応はバージョン10から、完全なPEP 517対応はバージョン19から）やPoetry、Flit、PDMなどのツールによってサポートされています。

このガイドでは、動機、主要概念、仕様、ワークフロー、実装、ベストプラクティスについて説明します。

## 動機と背景

Pythonパッケージングは、`distutils`（Python 1.6、2000年に導入）から`setuptools`（2004年）へと進化し、依存関係管理を追加しましたが、問題も導入しました：
- **命令的で脆弱**: ビルドは任意のスクリプトである`python setup.py`の実行に依存し、環境の前提条件（例：拡張機能用のCythonがない）により失敗する可能性がありました。
- **ビルド依存関係の欠如**: ビルドに必要なツール（コンパイラ、Cythonなど）が宣言されず、手動インストールやバージョン競合が発生しました。
- **密結合**: Pipは`setup.py`の呼び出しをハードコードしており、FlitやBentoのような代替ビルドシステムの導入を妨げました。
- **ホスト環境の汚染**: ビルドはユーザーのグローバルPython環境を使用し、副作用のリスクがありました。

これらの問題は革新を妨げ、Gitからのソースインストール中にエラーを引き起こしました。PEP 517は、最小限のインターフェースを標準化することでこれを解決します：フロントエンドは分離環境でバックエンドフックを呼び出します。Wheel（事前ビルド済みバイナリ、2014年導入）はディストリビューションを簡素化します—バックエンドは準拠したwheel/sdistを生成するだけです。PEP 518は`pyproject.toml`でビルド要件を宣言することでこれを補完し、分離を可能にします。

結果：宣言的で拡張可能なエコシステムが実現され、`setup.py`はオプションとなり、pipなどのツールはレガシーフォールバックなしで準拠したプロジェクトをビルドできるようになります。

## 主要概念

### ソースツリーとディストリビューション
- **ソースツリー**: パッケージコードと`pyproject.toml`を含むディレクトリ（例：VCSチェックアウト）。`pip install .`などのツールはこれからビルドします。
- **ソースディストリビューション (Sdist)**: `package-1.0.tar.gz`のようなgzip圧縮tarボール（`.tar.gz`）。`{name}-{version}`ディレクトリに`pyproject.toml`とメタデータ（PKG-INFO）を展開します。リリースやダウンストリームパッケージング（例：Debian）に使用されます。
- **Wheel**: `.whl`バイナリディストリビューション—事前ビルド済み、プラットフォーム固有で、コンパイルなしでインストール可能。PEP 517は再現性のためにwheelを義務付けています。

レガシーsdist（PEP 517以前）は実行可能ツリーに展開されますが、現在は準拠のために`pyproject.toml`を含める必要があります。

### pyproject.toml
このTOMLファイルは設定を一元化します。`[build-system]`セクション（PEP 518/517から）は以下を指定します：
- `requires`: ビルド用のPEP 508依存関係のリスト（例：`["setuptools>=40.8.0", "wheel"]`）。
- `build-backend`: バックエンドへのエントリポイント（例：`"setuptools.build_meta"`または`"poetry.masonry.api"`）。
- `backend-path`（オプション）：セルフホストバックエンド用に`sys.path`に追加されるin-treeパス（例：`["src/backend"]`）。

最小構成の例：
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

要件はDAGを形成します（循環なし；フロントエンドは検出して失敗します）。`[project]`（PEP 621）や`[tool.poetry]`などの他のセクションはメタデータ/依存関係を保持します。

### ビルドバックエンドとフロントエンド
- **バックエンド**: フック（呼び出し可能関数）を介してビルドロジックを実装します。分離のためにサブプロセスで実行されます。
- **フロントエンド**: 調整します（例：pip）。分離を設定し、要件をインストールし、フックを呼び出します。
- **分離**: フロントエンドは`setup.py`ではなく標準化されたフックを呼び出します。これにより、pipの変更なしで多様なバックエンドをサポートできます。

フックは`config_settings`（フラグ用の辞書、例：`{"--debug": true}`）を使用し、stdout/stderr（UTF-8）に出力する場合があります。

## 仕様

### [build-system] の詳細
- `requires`: PEP 508文字列（例：`">=1.0; sys_platform == 'win32'"`）。
- `build-backend`: `module:object`（例：`flit_core.buildapi`は`flit_core`をインポート；`backend = flit_core.buildapi`）。
- sys.path汚染なし—バックエンドは分離を介してインポートします。

### フック
バックエンドはこれらを属性として公開します：

**必須:**
- `build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str`: `wheel_directory`にwheelをビルドし、ベースネーム（例：`"myproj-1.0-py3-none-any.whl"`）を返します。提供されている場合は事前メタデータを使用します。読み取り専用ソースは一時ファイルを介して処理します。
- `build_sdist(sdist_directory, config_settings=None) -> str`: `sdist_directory`にsdistをビルドします（pax形式、UTF-8）。不可能な場合（例：VCSなし）は`UnsupportedOperation`を発生させます。

**オプション（デフォルトは`[]`またはフォールバック）:**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]`: 追加のwheel依存関係（例：`["cython"]`）。
- `prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str`: `{pkg}-{ver}.dist-info`メタデータ（wheel仕様に準拠、RECORDなし）を書き込みます。ベースネームを返します；フロントエンドは欠落している場合wheelから抽出します。
- `get_requires_for_build_sdist(config_settings=None) -> list[str]`: 追加のsdist依存関係。

フックはエラーの場合に例外を発生させます。フロントエンドは分離環境（例：stdlib + 要件のみのvenv）で呼び出します。

### ビルド環境
- 分離venv: `get_requires_*`用のブートストラップ、ビルド用の完全な環境。
- CLIツール（例：`flit`）はPATHにあります。
- 標準入力なし；フックごとにサブプロセス。

## ビルドプロセスの仕組み

### ステップバイステップのワークフロー
`pip install .`（ソースツリー）またはsdistインストールの場合：

1. **発見**: フロントエンドは`pyproject.toml`を読みます。
2. **分離設定**: venvを作成；`requires`をインストール。
3. **要件問い合わせ**: `get_requires_for_build_wheel`を呼び出し（追加をインストール）。
4. **メタデータ準備**: `prepare_metadata_for_build_wheel`を呼び出し（またはwheelをビルドして抽出）。
5. **Wheelビルド**: 分離環境で`build_wheel`を呼び出し；結果のwheelをインストール。
6. **フォールバック**: sdistがサポートされていない場合、wheelをビルド；フックがない場合、レガシー`setup.py`。

sdistの場合：展開し、ソースツリーとして扱います。開発者ワークフロー（例：`pip wheel .`）：
1. 環境を分離。
2. wheel/sdist用にバックエンドフックを呼び出します。

### ビルド分離 (PEP 518)
ビルド用に一時venvを作成し、ホストの汚染を回避します。Pipの`--no-build-isolation`は無効にします（注意して使用）。toxなどのツールはデフォルトで分離を使用します。

旧方式 vs 新方式：
- **旧方式**: ホスト環境で`python setup.py install`—競合のリスク。
- **新方式**: 分離フック—再現可能、安全。

## ビルドバックエンドの実装

作成するには：
1. フックを持つモジュールを定義（例：`mybackend.py`）。
2. `build-backend`をそれに向けます。

最小限の例（純粋なPythonパッケージ）：
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # ソースをwheelディレクトリにコピーし、.whlとして圧縮
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# オプションのフック
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # METADATAなどを書き込み
    return "myproj-1.0.dist-info"
```

`pyproject.toml`内：
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # 実際にはモジュールオブジェクトを指す
```

ボイラープレートには`pyproject-hooks`などのライブラリを使用します。拡張機能の場合、`config_settings`を介してCコンパイラを統合します。

## ツールでのPEP 517の使用

- **pip**: `pyproject.toml`を自動検出；`--use-pep517`を使用（19.1以降デフォルト）。編集可能インストールの場合：`pip install -e .`はフックを呼び出します。
- **Poetry**: 宣言的ツール。以下を生成：
  ```
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  `poetry build`でインストール；pip互換。
- **Flit**: 純粋なPython用にシンプル。以下を使用：
  ```
  [build-system]
  requires = ["flit_core >=3.2,<4"]
  build-backend = "flit_core.buildapi"
  ```
  `flit publish`はビルド/アップロードします。
- **Setuptools**: レガシーブリッジ：
  ```
  [build-system]
  requires = ["setuptools>=40.8.0", "wheel"]
  build-backend = "setuptools.build_meta"
  ```
  宣言的メタデータ用に`setup.cfg`をサポートします。

レガシーの移行：`[build-system]`を追加；`setup.py`呼び出しを削除。

## エラーハンドリングとベストプラクティス

- **エラー**: フックは発生させます（例：無効な設定の`ValueError`）。循環：フロントエンドはメッセージで失敗。サポートされていないsdist：wheelへのフォールバック。
- **ベストプラクティス**:
  - 宣言的（`setup.cfg`または`[project]`）を優先。
  - 正確なビルド依存関係を宣言（例：`cython==0.29`）。
  - 分離をテスト：デバッグ用に`pip wheel . --no-build-isolation`。
  - in-treeバックエンドの場合：`backend-path`を使用；循環を回避。
  - セキュリティ：サブプロセス内のフック；任意のコードなし。
  - 互換性：古いツール用に`setup.py`を含める。

2025年現在、setuptoolsが支配的（調査による）ですが、Poetry/Flitの採用はシンプルさのために増加しています。

## 参考文献
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
- [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
- [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
- [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
- [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)