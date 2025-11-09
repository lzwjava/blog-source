---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: GitHub Actions マトリックスビルドガイド
translated: true
type: note
---

**GitHub Actions**のマトリックスビルドを使用してテストを並列実行する方法と、マトリックス戦略での`fail-fast`オプションの使い方についてご質問のようですね。以下に詳しく説明します。

---

### GitHub Actionsでのマトリックスビルド
**マトリックス戦略**を使用すると、同じジョブを異なるパラメータで並列実行できます。例えば、複数のPythonやNodeのバージョン、あるいは異なるオペレーティングシステムでのテストなどです。

最小限の例：

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### 主なポイント

- **`matrix`:** ジョブの組み合わせを作成するための変数を定義します。  
  上記の例では、（`python-version`, `os`）のすべての組み合わせでテストが実行されます。

- **並列実行:** マトリックスによって生成された各ジョブは、デフォルトで**並列に**実行されます。

- **`fail-fast`:**
  - デフォルトは`true`です。つまり、1つのジョブが失敗すると、残りのマトリックスジョブはキャンセルされます。
  - 1つのジョブが失敗してもすべてのマトリックスジョブを実行し続けたい場合は、`fail-fast: false`を設定します。

  例：
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **総ジョブ数の制限:** 一部の組み合わせを除外できます：
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### テストの並列実行
- 各**マトリックスジョブは独自のランナーで並列に実行**されるため、特別な設定は必要ありません。
- 各ジョブ内で**並列テスト実行**（例：pytestの`-n auto`）を行いたい場合は、テストコマンドレベルで追加できます。

例：
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **まとめ:**
- `strategy.matrix`を使用して異なるパラメータの組み合わせを定義します。
- 1つのジョブが失敗してもすべてのマトリックスジョブを実行したい場合は、`fail-fast: false`を設定します。
- マトリックスジョブは自動的に並列実行されます。
- 各ジョブ内での実行時間を短縮するには、テストフレームワークの並列化機能（例：pytest-xdist）を使用します。

---

**Node/JavaScriptテスト**をマトリックスで実行する実際の例（複数のNodeバージョン、`fail-fast: false`、`npm test`によるテスト並列化）をお見せしましょうか？