---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: Pytestフィクスチャの使い方理解
translated: true
type: note
---

## `@pytest.fixture`とは？

`@pytest.fixture`は、関数を**フィクスチャ**としてマークするデコレータです。フィクスチャは、テストデータ、セットアップ、またはティアダウン機能をテストに提供する特別な関数です。フィクスチャはpytestの最も強力な機能の1つであり、多くの開発者がPythonの組み込み`unittest`モジュールよりもpytestを好む主な理由です。

## フィクスチャの仕組み

フィクスチャはシンプルかつ強力なパターンに従います：

1. **セットアップ**: `yield`文の前のコードがテスト前に実行される
2. **テスト実行**: テストが`yield`文に到達した時点で実行される
3. **ティアダウン**: `yield`文の後のコードがテスト完了後に実行される

### 基本的なフィクスチャの例

```python
import pytest

@pytest.fixture
def sample_data():
    # セットアップコード
    data = {"name": "John", "age": 30}
    yield data  # テストがここで実行される
    # ティアダウンコード（テスト後に実行）
    print("Cleaning up sample data")
```

## フィクスチャが必要な理由

フィクスチャはいくつかの一般的なテスト問題を解決します：

1. **テストの分離**: 各テストが新鮮で予測可能なデータで実行されることを保証
2. **コードの再利用**: 複数のテスト間でのセットアップ/ティアダウンコードの重複を回避
3. **リソース管理**: データベース接続、ファイル、ネットワーク接続などのリソースを適切に処理
4. **テストの明確さ**: テスト関数をセットアップではなくテスト対象に集中させる
5. **依存性注入**: 各テストに必要なものを正確に提供

## フィクスチャの主な機能

### 1. 依存性注入

フィクスチャは他のフィクスチャに依存でき、依存関係グラフを作成します：

```python
@pytest.fixture
def database_connection():
    # データベース接続のセットアップ
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    # database_connectionフィクスチャを使用
    create_table(database_connection, "users")
    yield
    drop_table(database_connection, "users")
```

### 2. スコープ制御

フィクスチャは異なるライフタイムを持つことができます：

```python
@pytest.fixture(scope="function")  # デフォルト - テストごとに1回実行
def per_test_fixture():
    pass

@pytest.fixture(scope="module")  # モジュールごとに1回実行
def per_module_fixture():
    pass

@pytest.fixture(scope="session")  # テストセッションごとに1回実行
def per_session_fixture():
    pass
```

### 3. 自動使用フィクスチャ

フィクスチャは要求されなくても自動的に実行できます：

```python
@pytest.fixture(autouse=True)
def always_run_this():
    # これはモジュール内のすべてのテストの前に実行される
    yield
    # これはすべてのテストの後に実行される
```

### 4. パラメータ化されたフィクスチャ

フィクスチャは複数のデータセットを生成できます：

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param  # 1、2、3でテストを実行する
```

## APIテストでの実践例

以下は、フィクスチャが金融ヘッダーのテストシナリオでどのように役立つかの例です：

```python
import pytest
import requests

@pytest.fixture
def financial_header():
    # セットアップ - ヘッダーを作成
    headers = create_financial_header()  # 作成ロジック
    yield headers  # これらのヘッダーでテストが実行される

    # ティアダウン - ヘッダーを削除
    delete_financial_header(headers)  # クリーンアップロジック

def test_submit_transaction(financial_header):
    # フィクスチャが自動的にヘッダーを提供
    response = requests.post(
        "https://api.example.com/transactions",
        headers=financial_header,
        json={"amount": 100}
    )
    assert response.status_code == 201

def test_validate_header(financial_header):
    # 同じフィクスチャが別のテストで使用される
    response = requests.get(
        "https://api.example.com/validate",
        headers=financial_header
    )
    assert response.json()["valid"] is True
```

## unittestとの比較

| 機能                  | pytestフィクスチャ                | unittest setUp/tearDown         |
|-----------------------|-----------------------------------|---------------------------------|
| 依存性注入            | ✅ 対応                           | ❌ 非対応                        |
| スコープ制御          | ✅ 関数、クラス、モジュール、セッション | ❌ メソッド/クラスレベルのみ     |
| クリーンな構文        | ✅ シンプルなデコレータ           | ❌ 継承が必要                    |
| テストの分離          | ✅ 各テストが新鮮なフィクスチャを取得 | ❌ 共有状態が問題を引き起こす可能性 |
| パラメータ化          | ✅ 組み込みサポート               | ❌ 手動実装が必要                |

## フィクスチャを使用するタイミング

以下の場合にフィクスチャを使用します：
- テストデータやオブジェクトをセットアップする場合
- 外部リソース（DB接続、ファイルなど）を管理する場合
- テスト後にクリーンアップを実行する場合
- 共通のテスト依存関係を共有する場合
- 異なるテスト環境を作成する場合
- 複雑なセットアップ/ティアダウンロジックを実装する場合

フィクスチャはAPIテスト（金融ヘッダーのケースのように）で特に価値があります。なぜなら、テストリソースのライフサイクルをクリーンかつ予測可能に管理するのに役立つからです。