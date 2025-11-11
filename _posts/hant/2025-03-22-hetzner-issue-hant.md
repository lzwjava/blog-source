---
audio: false
generated: true
lang: hant
layout: post
title: Hetzner API 問題
translated: true
type: note
---

讓我們分析您遇到的錯誤，並解釋您的程式碼發生了什麼情況：

### 錯誤：
```
為伺服器 sg5 建立快照時發生錯誤：無法執行操作，因為伺服器已被鎖定 (locked, f21b9dc9d1535310)
```

此錯誤來自 Hetzner Cloud API（透過 `hcloud` Python SDK），表示為名為 `sg5` 的伺服器建立快照的操作失敗，因為該伺服器**已被鎖定**。伺服器被鎖定意味著另一個操作（例如，先前的快照、重啟或調整大小）目前正在進行中，在該過程完成之前，伺服器暫時無法接受新的操作。

### 程式碼解析：
以下是您的腳本，附帶解釋以及錯誤發生的位置：

```python
from hcloud import Client
import os

# 從環境變數取得 API 令牌
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("錯誤：未設定 HERTZNER_API_KEY 環境變數。")
    exit(1)

# 建立客戶端實例
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"已為伺服器 {server.name} 建立快照，ID 為：{response.image.id}")
    except Exception as e:
        print(f"為伺服器 {server.name} 建立快照時發生錯誤：{e}")

# 列出所有伺服器
servers = client.servers.get_all()

# 列印伺服器詳細資訊並建立快照
for server in servers:
    print(f"伺服器 ID：{server.id}")
    print(f"伺服器名稱：{server.name}")
    print(f"伺服器狀態：{server.status}")
    print(f"伺服器 IPv4：{server.public_net.ipv4.ip}")
    print(f"伺服器 IPv6：{server.public_net.ipv6.ip}")
    print(f"伺服器類型：{server.server_type.name}")
    print(f"伺服器位置：{server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1. **API 令牌設定**：
   - 腳本從環境變數 (`HERTZNER_API_KEY`) 中獲取 Hetzner API 金鑰。如果未設定，則會顯示錯誤並退出。

2. **客戶端初始化**：
   - 使用 API 令牌建立一個 `Client` 實例，以與 Hetzner Cloud API 進行互動。

3. **`create_snapshot` 函數**：
   - 此函數嘗試使用 `client.servers.create_image()` 為給定的伺服器建立快照。
   - 參數：
     - `server`：要建立快照的伺服器物件。
     - `description`：快照的名稱（例如 `sg5-snapshot`）。
     - `type="snapshot"`：指定映像類型為快照（與備份或 ISO 相對）。
   - 如果成功，則列印快照 ID；否則，它會捕獲並列印任何異常（就像您看到的這個）。

4. **伺服器列表**：
   - `client.servers.get_all()` 檢索與您的 Hetzner 帳戶關聯的所有伺服器列表。
   - 腳本遍歷它們，列印其詳細資訊（ID、名稱、狀態、IP 等），並為每個伺服器呼叫 `create_snapshot()`。

5. **錯誤發生的位置**：
   - 在 `create_snapshot()` 函數內部，`client.servers.create_image()` 呼叫因伺服器 `sg5` 被鎖定而失敗。`hcloud` 庫根據 API 回應引發了異常訊息 (`cannot perform operation because server is locked`)。

### 為什麼伺服器被鎖定？
當一個操作正在進行時，伺服器會變成鎖定狀態。常見原因包括：
- 正在建立另一個快照。
- 伺服器正在重啟、調整大小或重建。
- 先前的操作尚未完成。

錯誤訊息中的鎖定 ID (`f21b9dc9d1535310`) 是鎖定伺服器的正在進行操作的唯一識別碼。

### 如何修復：
以下是解決問題並改進腳本的步驟：

#### 1. **在繼續之前檢查鎖定狀態**
修改腳本，如果伺服器被鎖定則跳過快照建立。您可以使用 `client.actions.get_all()` 檢查伺服器當前的操作，或等待鎖定清除。

更新後的 `create_snapshot` 函數：
```python
def create_snapshot(server):
    try:
        # 透過檢查其操作來確認伺服器是否被鎖定
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"跳過 {server.name} 的快照：伺服器因操作 {action.id} 而被鎖定")
                return
        # 如果沒有正在執行的操作，則繼續建立快照
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"已為伺服器 {server.name} 建立快照，ID 為：{response.image.id}")
    except Exception as e:
        print(f"為伺服器 {server.name} 建立快照時發生錯誤：{e}")
```

#### 2. **等待鎖定清除**
如果您想等待而不是跳過，可以輪詢伺服器的操作直到鎖定消失：
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"等待伺服器 {server.name} 解除鎖定...")
        time.sleep(5)  # 等待 5 秒後再次檢查

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"已為伺服器 {server.name} 建立快照，ID 為：{response.image.id}")
    except Exception as e:
        print(f"為伺服器 {server.name} 建立快照時發生錯誤：{e}")
```

#### 3. **手動調查鎖定**
- 使用 Hetzner Cloud Console 或 API 檢查 ID 為 `f21b9dc9d1535310` 的操作狀態。
- 範例 API 呼叫（透過 Python）：
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"操作狀態：{action.status}, 指令：{action.command}")
  ```
- 如果它卡住了，您可能需要聯繫 Hetzner 支援。

#### 4. **再次執行腳本**
一旦伺服器不再被鎖定（操作完成或您手動解決問題後），重新執行腳本。

### 補充說明：
- **速率限制**：在迴圈中為許多伺服器建立快照可能會觸及 Hetzner 的 API 速率限制。如果需要，請在請求之間新增延遲（例如 `time.sleep(1)`）。
- **錯誤處理**：目前的腳本在第一個錯誤處停止。如果您希望它繼續處理其他伺服器，請確保異常不會停止迴圈（在您的情況下不會，這是好的）。

如果您需要幫助實施任何這些修復或進一步除錯，請告訴我！