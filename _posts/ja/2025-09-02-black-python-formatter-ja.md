---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 黒いPythonコードフォーマッターガイド
translated: true
type: note
---

PyPIの`black`パッケージは**Pythonコードフォーマッタ**です。Pythonコードを自動的に再フォーマットし、一貫したスタイル規則（PEP 8互換ですが、より厳格な独自の基準）に従わせます。使用方法は以下の通りです：

---

### 1. Blackのインストール

```bash
pip install black
```

常に最新の安定版を入手したい場合は：

```bash
pip install -U black
```

---

### 2. ファイルまたはディレクトリのフォーマット

ファイルに対してBlackを実行：

```bash
black my_script.py
```

ディレクトリ全体（再帰的）に対してBlackを実行：

```bash
black src/
```

デフォルトでは、フォーマットされたコードでファイルがその場で上書きされます。

---

### 3. 変更を加えずにフォーマットを確認

`--check`を使用して、ファイルの再フォーマットが必要かどうかを確認：

```bash
black --check my_script.py
```

これはCIパイプラインでスタイルの一貫性を確保するのに便利です。

---

### 4. 一般的なオプション

* `--line-length 88` → 行の長さを変更（デフォルト：88）
* `--diff` → ファイルを変更せずに、どのような変更が行われるかを表示
* `--skip-string-normalization` → 文字列のクォートを変更しない
* `--exclude` → 特定のファイル/フォルダをスキップ

例：

```bash
black --line-length 100 --diff src/
```

---

### 5. 統合

* **IDEサポート**：BlackはPyCharm、VS Code、Vim、Emacsなどのプラグインとして利用可能
* **Pre-commitフック**：コードがコミット前にフォーマットされるように`.pre-commit-config.yaml`にBlackを追加：

  ```yaml
  repos:
    - repo: https://github.com/psf/black
      rev: stable
      hooks:
        - id: black
  ```
* **CI/CD**：CIパイプラインに`black --check .`を追加

---

👉 **VSCodeやPyCharmでの自動フォーマット設定**方法も表示しましょうか？これにより、手動で`black`を実行する必要がなくなります。