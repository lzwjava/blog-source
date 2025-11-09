---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PoetryによるPython依存関係管理
translated: true
type: note
---

### Poetryとは

PoetryはPythonにおける依存関係管理とパッケージングのためのツールです。プロジェクトが依存するライブラリを宣言し、それらのインストール、更新、解決を自動的に処理しながら、再現可能な環境を保証します。

### 主な目的
Poetryは、単一の設定ファイル（`pyproject.toml`）を通じて依存関係を管理し、異なるマシン間で一貫したインストールを実現するためのロックファイルを作成し、配布（例: PyPIへのアップロード）のためのプロジェクトビルドをサポートすることで、Pythonプロジェクトのワークフローを簡素化します。`pip`、`pipenv`、`setuptools`のような断片化されたツールを、統一されたユーザーフレンドリーなアプローチで置き換えることを目的としています。

### 主な機能
- **依存関係解決**: 依存関係を自動的にインストール、更新し、衝突をインテリジェントに解決します。
- **ロックファイル**: 再現可能なビルドのため、正確なバージョンを固定する`poetry.lock`を生成します。
- **仮想環境**: グローバル環境を汚染しないよう、プロジェクトごとに分離された環境を作成します。
- **パッケージング**: 配布を容易にするためのwheelまたはsdistをビルドします。
- **マルチプラットフォーム対応**: Linux、macOS、Windowsで動作します。
- **シェル統合**: Bash、Fish、Zsh用のタブ補完をサポートします。
- **Python 3.9+ 互換**: モダンなPythonバージョンを必要とします。

### インストール
`pipx`を使用して、競合なしでグローバルにアクセスできる分離された環境にPoetryをインストールします（推奨）:

1. 必要に応じて`pipx`をインストールします（OSのパッケージマネージャー経由、または`python -m pip install --user pipx`）。
2. 実行: `pipx install poetry`。

更新する場合: `pipx upgrade poetry`。  
アンインストールする場合: `pipx uninstall poetry`。

シェル補完を有効にします（例: Bashの場合: `poetry completions bash >> ~/.bash_completion`）。

### 基本的な使い方
新しいプロジェクトを初期化: `poetry init`。  
依存関係を追加: `poetry add requests`。  
ロックファイルからインストール: `poetry install`。  
スクリプトを実行: `poetry run python script.py`。  
パッケージをビルド: `poetry build`。

全てのコマンドについては、ドキュメントを確認してください。

[Poetry Documentation](https://python-poetry.org/docs/)