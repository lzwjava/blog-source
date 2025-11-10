---
audio: false
generated: true
image: false
lang: ja
layout: post
title: プロジェクトディレクトリ構成のベストプラクティス
translated: true
type: note
---

良い質問です。

一般的な慣例は以下の通りです：

* **`scripts/`** はアプリケーションコード（本番環境で実行したいものやプロジェクトの一部として実行するもの）用です
* **`tests/`** はテストコード（スクリプトやモジュールの正しさを検証するもの）用です

そのため、新しいテストファイルを追加する場合は、通常 `scripts/` ではなく **`tests/llm/`** の下に配置すべきです。

例：

```
scripts/
  llm/
    main.py
    utils.py
tests/
  llm/
    test_main.py
    test_utils.py
```

このようにすることで、テストは実装から分離され、`pytest` のようなツールが簡単にテストを発見できます。

👉 例えば以下のようなコードを追加できます：

```python
# tests/llm/test_basic.py
import pytest
from scripts.llm import utils

def test_addition():
    assert utils.add(2, 3) == 5
```

そして実行：

```bash
pytest tests/llm/
```

`tests/llm/` ファイル間でフィクスチャを共有できるように `conftest.py` を設定する方法もお見せしましょうか？