---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ユニットテストとPytestの主な違い
translated: true
type: note
---

日常のテスト作業で実際に変わることに焦点を当てた、簡潔で表を使わない比較をご紹介します。

# 哲学とスタイル

* **unittest**: xUnitスタイル（Java/JUnit風）。クラスベースのテスト、`setUp/tearDown`のようなライフサイクルフック、メソッド名は`test_`で始まる必要がある。
* **pytest**: Pythonicでミニマル。テスト**関数**またはクラス、豊富なフィクスチャ、アサーションリライティングによるプレーンな`assert`。

# テストディスカバリ

* **unittest**: `python -m unittest discover`（またはスイートのロード）。`test*.py`、`TestCase`のサブクラスを探す。
* **pytest**: `pytest`が`test_*.py`と`*_test.py`を自動発見；`test_*`関数と`Test*`クラスのメソッド。

# アサーション

* **unittest**: 多くの特定のメソッド（`assertEqual`、`assertTrue`、`assertRaises`、…）。
* **pytest**: プレーンな`assert`を使用し、表現力豊かな差分（「左 vs 右」）を表示、`pytest.raises`をサポート。

# フィクスチャとセットアップ

* **unittest**: `setUp()/tearDown()`、`setUpClass/tearDownClass`、`setUpModule/tearDownModule`。
* **pytest**: スコープ（function/class/module/session）を持つ**フィクスチャ**、依存性注入、自動使用、ファイナライザ。小さく再利用可能なセットアップを推奨。

# パラメータ化

* **unittest**: 組み込みなし；ループ/subTestsまたはサードパーティ製ライブラリを使用。
* **pytest**: `@pytest.mark.parametrize`が第一級（入力のマトリックス、クリーンなレポート）。

# スキップ、予期された失敗、マーカー

* **unittest**: `@skip`、`@skipIf`、`@expectedFailure`。
* **pytest**: 同じ考えに加えて、強力な**マーカー**（`@pytest.mark.slow`、`xfail`、`filterwarnings`、カスタムマーク）とコマンドライン選択（`-m slow`）。

# プラグインとエコシステム

* **unittest**: バッテリー付属だがリーン；高度な機能には外部ランナー/ツールに依存。
* **pytest**: 巨大なプラグインエコシステム（並列実行用の`pytest-xdist`、`pytest-randomly`、`pytest-cov`、`pytest-mock`、`pytest-asyncio`、`pytest-django`など）。

# モック

* **unittest**: `unittest.mock`は標準；どこでも動作。
* **pytest**: `unittest.mock`または`pytest-mock`の`mocker`フィクスチャ（よりクリーンなパッチ適用と自動後片付け）を使用。

# 非同期テスト

* **unittest**: 3.8以降、`IsolatedAsyncioTestCase`を持つ（OKだが冗長）。
* **pytest**: `pytest-asyncio`（またはtrioのプラグイン）を使用すると、`@pytest.mark.asyncio`とイベントループ用のフィクスチャサポートを取得。

# パフォーマンスと並列

* **unittest**: 組み込みの並列処理なし；`unittest-parallel`/CIのトリックを使用。
* **pytest**: `pytest-xdist -n auto`が定番。

# IDE/CI/カバレッジ

* 両方ともIDEとCIに統合。カバレッジは`coverage.py`経由：

  * **unittest**: `coverage run -m unittest` → `coverage report`。
  * **pytest**: `pytest --cov=your_pkg`（`pytest-cov`を使用）。

# どちらを選ぶべきか

* **unittestを選ぶ場合**:

  * 標準ライブラリのみが必要（外部依存なし）。
  * レガシー/xUnitコードベースや厳格な組織ポリシーに組み込む。
* **pytestを選ぶ場合**:

  * より速い作成、明確な失敗、強力なフィクスチャ/パラメータ化を望む。
  * そのプラグインエコシステムと並列化の恩恵を受ける。

# 相互運用性と移行

**unittest**スイートを**pytest**で実行可能（pytestは`unittest.TestCase`を発見）。これにより段階的な移行が可能：

1. ランナーとして`pytest`の呼び出しを開始。
2. 既存のテストと並行してpytestテストを追加。
3. 役立つ場所にフィクスチャ/パラメータ化を導入。
4. 後で古い`TestCase`を関数にリファクタリング（任意）。

# 小さな並列例

## 同じテスト

**unittest**

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

if __name__ == "__main__":
    unittest.main()
```

**pytest**

```python
import pytest

@pytest.fixture
def data():
    return [1, 2, 3]

def test_sum(data):
    assert sum(data) == 6

def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## パラメータ化

**unittest (subTest)**

```python
import unittest

class TestParity(unittest.TestCase):
    def test_even(self):
        for n in [0, 2, 4]:
            with self.subTest(n=n):
                self.assertEqual(n % 2, 0)
```

**pytest**

```python
import pytest

@pytest.mark.parametrize("n", [0, 2, 4])
def test_even(n):
    assert n % 2 == 0
```

## モッキング

**unittest.mock**

```python
from unittest.mock import patch

@patch("pkg.api.fetch_user", return_value={"id": 1})
def test_uses_api(mock_fetch):
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

**pytest-mock**

```python
def test_uses_api(mocker):
    mock_fetch = mocker.patch("pkg.api.fetch_user", return_value={"id": 1})
    from pkg.service import get_user
    assert get_user(1)["id"] == 1
    mock_fetch.assert_called_once_with(1)
```

# 実用的な推奨事項

* 新規プロジェクト: 速度、可読性、エコシステムのために**pytest**をデフォルトとする。
* レガシー/標準ライブラリのみの環境: **unittest**に固執するが、テストを書き換えずにより良い出力とプラグインを解放するために**pytest**経由で実行することを検討。
* より高速なCIのために早期に`pytest-xdist`を、カバレッジのために`pytest-cov`を追加。
* 大きなクラスセットアップよりもフィクスチャを使用；それらを小さく構成可能に保つ。
* マーカーを使用してスイート（`slow`、`integration`、`db`）を整理し、CIステージでサブセットを実行。

必要であれば、あなたのプロジェクトレイアウトと制約（標準ライブラリのみ？並列処理が必要？非同期？Django/Flask/FastAPI？）を教えてください。最小限で意見のあるテスト設定を提案します。