---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python APIテストフレームワーク
translated: true
type: note
---

### APIエンドポイントテストのための推奨Pythonテストフレームワーク

Java（例：Spring Boot）で書かれたサーバーエンドポイントをテストするには、Pythonフレームワークを使用して統合テストやエンドポイントテストを実行できます。HTTPリクエスト（GET、POST、PUT、DELETEなど）を送信し、レスポンスコード、ヘッダー、ボディコンテンツを検証します。サーバーがJavaで書かれているため、ブラックボックスAPIとして扱い、PythonのHTTPクライアントライブラリ（`requests`や`httpx`など）を使用して対話します。最も一般的なセットアップは、テストランナーフレームワークとHTTPライブラリを組み合わせたものです。

以下に、人気度とユースケースへの適合性に基づいて優先順位をつけた強力な選択肢を示します（2025年時点での最新の推奨事項に基づく）。HTTPインタラクションとレスポンス検証を容易にサポートするものに焦点を当てます：

#### 1. **pytest（requestsまたはhttpxライブラリと併用）**
   - **推奨理由**：pytestは、ユニットテスト、統合テスト、APIテストにおいて最も人気のあるPythonテストフレームワークです。柔軟性が高く、シンプルな構文を持ち、フィクスチャによるセットアップ/ティアダウン（例：テストサーバーの起動やモック作成）をサポートします。GET/POSTリクエストを送信し、ステータスコード（例：200 OK）やJSONレスポンスに対してアサーションを行うテストを書くことができます。`pytest-httpx`のようなプラグインによる非同期テストの拡張も可能です。
   - **このシナリオでの使用方法**：
     - インストール：`pip install pytest requests`（非同期の場合は`pip install pytest httpx`）。
     - テスト例：
       ```python
       import requests
       import pytest

       @pytest.fixture
       def base_url():
           return "http://your-java-server:8080"

       def test_get_endpoint(base_url):
           response = requests.get(f"{base_url}/api/resource")
           assert response.status_code == 200
           assert "expected_key" in response.json()

       def test_post_endpoint(base_url):
           data = {"key": "value"}
           response = requests.post(f"{base_url}/api/resource", json=data)
           assert response.status_code == 201
           assert response.json()["status"] == "created"
       ```
     - 長所：可読性が高く、コミュニティプラグインが豊富、並列実行可能、CI/CDに最適。
     - 短所：ある程度のコーディングが必要。純粋な宣言型ではない。
   - **最適な用途**：カスタムロジックが必要な統合テスト。

#### 2. **Tavern**
   - **推奨理由**：Tavernは、RESTful APIテストに特化したpytestプラグインです。YAMLファイルを使用してテストを宣言的に定義するため、多くのPythonコードを書かずにHTTPメソッド、ペイロード、期待されるレスポンスを簡単に指定できます。ステータスコードやJSONスキーマチェックを含むエンドポイント検証に最適です。
   - **このシナリオでの使用方法**：
     - インストール：`pip install tavern`。
     - YAMLテストファイル例：
       ```yaml
       test_name: Test GET endpoint
       stages:
         - name: Get resource
           request:
             url: http://your-java-server:8080/api/resource
             method: GET
           response:
             status_code: 200
             json:
               expected_key: expected_value

       test_name: Test POST endpoint
       stages:
         - name: Post resource
           request:
             url: http://your-java-server:8080/api/resource
             method: POST
             json: { "key": "value" }
           response:
             status_code: 201
             json:
               status: created
       ```
     - 実行：`pytest your_test.yaml`。
   - 長所：人間が読みやすいYAML、pytestと統合、自動リトライと検証。
   - 短所：複雑なロジックには純粋なPythonに比べて柔軟性が低い。
   - **最適な用途**：エンドポイントに焦点を当てた迅速で宣言的なAPIテスト。

#### 3. **PyRestTest**
   - **推奨理由**：YAMLまたはJSON設定を使用したREST APIテストのための軽量なPythonツールです。基本的なテストではコード不要で、ベンチマークをサポートし、Javaエンドポイントのような外部サーバーからのHTTPレスポンスの検証に適しています。
   - **このシナリオでの使用方法**：
     - インストール：`pip install pyresttest`。
     - YAML例：
       ```yaml
       - config:
           url: http://your-java-server:8080
       - test:
           name: GET test
           url: /api/resource
           method: GET
           expected_status: [200]
           validators:
             - {jsonpath_mini: 'expected_key', expected: 'expected_value'}
       - test:
           name: POST test
           url: /api/resource
           method: POST
           body: '{"key": "value"}'
           expected_status: [201]
           validators:
             - {jsonpath_mini: 'status', expected: 'created'}
       ```
     - 実行：`pyresttest http://base-url test.yaml`。
   - 長所：シンプルなセットアップ、ボイラープレートコードが不要、ポータブル。
   - 短所：pytestに比べてコミュニティが限定的。古いツールだがメンテナンスは継続。
   - **最適な用途**：マイクロベンチマークとシンプルな統合テスト。

#### 4. **Robot Framework（RequestsLibraryと併用）**
   - **推奨理由**：受け入れテストとAPIテストのためのキーワード駆動型フレームワークです。`RequestsLibrary`を使用すると、HTTPリクエストをネイティブに処理し、統合テスト向けに拡張可能です。読みやすくコードではないテストを好むチームに適しています。
   - **このシナリオでの使用方法**：
     - インストール：`pip install robotframework robotframework-requests`。
     - テストファイル例：
       ```
       *** Settings ***
       Library    RequestsLibrary

       *** Test Cases ***
       Test GET Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${response}=    GET On Session    mysession    /api/resource
           Status Should Be    200    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['expected_key']}    expected_value

       Test POST Endpoint
           Create Session    mysession    http://your-java-server:8080
           ${data}=    Create Dictionary    key=value
           ${response}=    POST On Session    mysession    /api/resource    json=${data}
           Status Should Be    201    ${response}
           ${json}=    To Json    ${response.content}
           Should Be Equal    ${json['status']}    created
       ```
     - 実行：`robot your_test.robot`。
   - 長所：キーワードベース（非開発者にも容易）、レポート機能が組み込み。
   - 短所：冗長な構文。Python純粋主義者には学習曲線がやや急。
   - **最適な用途**：BDDスタイルの統合テスト。

#### 追加のヒント
- **共通ライブラリ: requests**：ほとんどすべてのフレームワークがHTTP呼び出しにこれと組み合わせて使用します。シンプル（`response = requests.get(url)`）で、JSONを自動処理し、実績があります。
- **requestsの代替: httpx**：高スループットテストなど、非同期サポートが必要な場合に使用します。`pip install httpx`でインストール。
- **Javaサーバーのセットアップ**：Javaサーバーがローカルまたはリモートで実行されていることを確認してください。統合テストでは、CI/CDでSpring Bootアプリを起動するためにDockerの使用を検討してください。
- **総合的な最適な選択**：柔軟性が必要ならpytest + requestsから始めてください。宣言的なテストを好む場合は、TavernまたはPyRestTestを選択してください。
- **考慮事項**：これらは標準的なHTTPを使用するため、言語を跨いで動作します。スキーマ検証には、`jsonschema`のようなライブラリを追加します。JenkinsやGitHub ActionsのようなツールでCI/CD内で実行します。

### 参考文献
[2025年に切り替えるべきトップPythonテストフレームワーク](https://medium.com/@hadiyolworld007/top-python-testing-frameworks-in-2025-you-should-switch-to-6ddeb679ccd5)  
[2025年に注目すべき10のベストPythonテストフレームワーク](https://www.lambdatest.com/blog/top-python-testing-frameworks/)  
[2025年のテストにおける14のベストPython自動化ツール](https://apidog.com/blog/best-python-testing-tools-2025/)  
[2025年のベストオープンソースAPIテストツール](https://testguild.com/12-open-source-api-testing-tools-rest-soap-services/)