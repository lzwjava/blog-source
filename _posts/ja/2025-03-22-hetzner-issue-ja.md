---
audio: false
generated: true
lang: ja
layout: post
title: ヘッツナーAPIの問題
translated: true
type: note
---

遭遇しているエラーを分析し、コードで何が起こっているのか説明します：

### エラー：
```
Error creating snapshot for server sg5: cannot perform operation because server is locked (locked, f21b9dc9d1535310)
```

このエラーはHetzner Cloud API（`hcloud` Python SDK経由）からのもので、サーバー `sg5` のスナップショット作成操作が、サーバーが **ロックされている** ために失敗したことを示しています。サーバーがロックされているというのは、別の操作（以前のスナップショット作成、再起動、リサイズなど）が現在進行中であり、そのプロセスが完了するまでサーバーが一時的に新しい操作を受け付けない状態にあることを意味します。

### コードの詳細：
以下はあなたのスクリプトと、エラーが発生する箇所の説明です：

```python
from hcloud import Client
import os

# 環境変数からAPIトークンを取得
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# クライアントインスタンスを作成
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")

# 全てのサーバーをリストアップ
servers = client.servers.get_all()

# サーバーの詳細を表示し、スナップショットを作成
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1. **APIトークンの設定**:
   - スクリプトは環境変数 (`HERTZNER_API_KEY`) からHetzner APIキーを取得します。設定されていない場合はエラーで終了します。

2. **クライアントの初期化**:
   - APIトークンを使用してHetzner Cloud APIと対話するための `Client` インスタンスが作成されます。

3. **`create_snapshot` 関数**:
   - この関数は、`client.servers.create_image()` を使用して、指定されたサーバーのスナップショット作成を試みます。
   - パラメータ:
     - `server`: スナップショットを撮るサーバーオブジェクト。
     - `description`: スナップショットの名前（例: `sg5-snapshot`）。
     - `type="snapshot"`: イメージタイプがスナップショットであることを指定します（バックアップやISOとは異なります）。
   - 成功した場合はスナップショットIDを表示し、そうでない場合は（表示されているような）例外をキャッチして表示します。

4. **サーバーのリストアップ**:
   - `client.servers.get_all()` は、あなたのHetznerアカウントに関連付けられた全てのサーバーのリストを取得します。
   - スクリプトはそれらをループ処理し、詳細（ID、名前、ステータス、IPなど）を表示し、それぞれに対して `create_snapshot()` を呼び出します。

5. **エラーが発生する箇所**:
   - `create_snapshot()` 関数内の `client.servers.create_image()` 呼び出しが、サーバー `sg5` に対して失敗します。なぜならロックされているからです。例外メッセージ (`cannot perform operation because server is locked`) は、APIレスポンスに基づいて `hcloud` ライブラリによって発生させられます。

### なぜサーバーはロックされているのか？
サーバーは、操作が既に進行中の場合にロックされます。一般的な理由は以下の通りです：
- 別のスナップショットが作成されている。
- サーバーが再起動、リサイズ、または再構築されている。
- 以前の操作がまだ完了していない。

エラーメッセージ内のロックID (`f21b9dc9d1535310`) は、サーバーをロックしている進行中のアクションの一意の識別子です。

### 修正方法：
問題を解決し、スクリプトを改善するための手順を以下に示します：

#### 1. **処理を進める前にロック状態をチェックする**
サーバーがロックされている場合、スナップショット作成をスキップするようにスクリプトを修正します。`client.actions.get_all()` を使用してサーバーの現在のアクションをチェックするか、ロックが解除されるのを待つことができます。

更新された `create_snapshot` 関数：
```python
def create_snapshot(server):
    try:
        # サーバーのアクションを調べてロックされているかチェック
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"Skipping snapshot for {server.name}: Server is locked by action {action.id}")
                return
        # 実行中のアクションがなければ、スナップショットを続行
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 2. **ロックが解除されるのを待つ**
スキップする代わりに待機したい場合は、サーバーのアクションをロックがなくなるまでポーリングできます：
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"Waiting for server {server.name} to unlock...")
        time.sleep(5)  # 再度チェックする前に5秒待機

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 3. **ロックを手動で調査する**
- Hetzner Cloud ConsoleまたはAPIを使用して、ID `f21b9dc9d1535310` のアクションのステータスを確認します。
- API呼び出しの例（Python経由）：
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"Action Status: {action.status}, Command: {action.command}")
  ```
- 固まっている場合は、Hetznerサポートに連絡する必要があるかもしれません。

#### 4. **スクリプトを再度実行する**
サーバーがもはやロックされていない状態（アクションが完了するか、手動で解決した後）になったら、スクリプトを再実行してください。

### 追加の注意点：
- **レート制限**: ループ内で多くのサーバーのスナップショットを作成すると、HetznerのAPIレート制限に達する可能性があります。必要に応じてリクエスト間に遅延（例: `time.sleep(1)`）を追加してください。
- **エラーハンドリング**: 現在のスクリプトは最初のエラーで停止します。他のサーバーに対して処理を継続させたい場合は、例外がループを停止させないようにしてください（あなたの場合、それは良い状態です）。

これらの修正の実装やさらなるデバッグにヘルプが必要な場合はお知らせください！