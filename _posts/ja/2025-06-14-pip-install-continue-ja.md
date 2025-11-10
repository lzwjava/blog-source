---
audio: false
generated: true
lang: ja
layout: post
title: 失敗を無視したPipインストール
translated: true
type: note
---

混乱を避けるためにお詫び申し上げますが、`--skip-existing` フラグは `pip` の有効なオプションではありません。requirements ファイルからのパッケージインストールを失敗にもかかわらず続行するには、依存関係の衝突を避けるために `--no-dependencies` フラグを使用するか、エラーを手動で処理してください。しかし、失敗したパッケージをスキップして他のパッケージのインストールを続行する最良の方法は、シェルスクリプトでループを使用することです。以下は、`requirements.top.txt` から各パッケージを個別にインストールしようと試み、失敗を無視するワンライナーコマンドです：

```bash
while read -r package; do pip install --ignore-installed "$package" || true; done < scripts/requirements/requirements.top.txt
```

### 説明：
- `while read -r package`: requirements ファイルから各行（パッケージ）を読み取ります
- `pip install --ignore-installed "$package"`: 各パッケージのインストールを試み、既にインストールされているバージョンを無視します
- `|| true`: パッケージのインストールが失敗しても（例：`tensorflow` と Python 3.13 のバージョン非互換性による）、ループが続行されることを保証します
- `< scripts/requirements/requirements.top.txt`: requirements ファイルへのパスを指定します

### 注意点：
- **TensorFlow の問題**: 以前発生したエラーは、`tensorflow` が Python 3.13 と互換性がないことを示しています。`tensorflow` を使用するには Python 3.12 またはそれ以前のバージョンを使用する必要があります。続行するには：
  1. Python 3.12 で仮想環境を作成：
     ```bash
     python3.12 -m venv venv
     source venv/bin/activate
     ```
  2. アクティベートされた環境で上記のコマンドを実行
- **依存関係**: 依存関係の衝突を避けるために、ループ内の `pip install` コマンドに `--no-dependencies` を追加できます（`pip install --ignore-installed --no-dependencies "$package" || true`）が、パッケージが特定の依存関係に依存している場合には問題が発生する可能性があります
- **代替案**: `tensorflow` のような問題のあるパッケージを除外したい場合は、`requirements.top.txt` を編集してそれらを削除するか、互換性のあるバージョンを指定してください（例：Python 3.12 用に `tensorflow==2.17.0`）

さらに問題が発生したり、requirements ファイルの変更についてサポートが必要な場合は、お知らせください！