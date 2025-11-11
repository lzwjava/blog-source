---
audio: false
generated: true
lang: hant
layout: post
title: TCP 連接的 Python 腳本
translated: true
type: note
---

PowerShell 指令 `Get-NetTCPConnection -LocalPort 80` 可擷取 Windows 系統上使用指定本機連接埠（此處為連接埠 80）的 TCP 連線資訊。要在 Python 中實現類似功能，可使用 `psutil` 程式庫，該程式庫提供跨平台的系統詳細資訊存取，包括網路連線。

以下是一個 Python 腳本，可根據指定本機連接埠（例如連接埠 80）篩選並列出 TCP 連線，功能類似於 PowerShell 指令：

```python
import psutil

def get_tcp_connections_by_port(local_port):
    # 擷取所有網路連線
    connections = psutil.net_connections(kind='tcp')
    
    # 根據本機連接埠篩選連線
    matching_connections = [
        conn for conn in connections
        if conn.laddr.port == local_port and conn.status == 'LISTEN'
    ]
    
    # 輸出符合條件的連線詳細資訊
    if not matching_connections:
        print(f"未發現監聽連接埠 {local_port} 的 TCP 連線")
        return
    
    print(f"監聽連接埠 {local_port} 的 TCP 連線：")
    print("PID\t本機位址\t\t遠端位址\t\t狀態")
    print("-" * 50)
    
    for conn in matching_connections:
        local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        pid = conn.pid if conn.pid is not None else "N/A"
        status = conn.status if conn.status else "N/A"
        print(f"{pid}\t{local_addr}\t{remote_addr}\t{status}")

if __name__ == "__main__":
    target_port = 80  # 指定要篩選的連接埠（例如 80）
    get_tcp_connections_by_port(target_port)
```

### 說明：
1. **安裝 `psutil`**：
   - 需要安裝 `psutil` 程式庫以存取網路連線詳細資訊。請透過以下指令安裝：
     ```bash
     pip install psutil
     ```

2. **腳本詳情**：
   - `psutil.net_connections(kind='tcp')` 可擷取所有 TCP 連線
   - 腳本會篩選本機連接埠符合指定 `local_port`（例如 80）且狀態為 `LISTEN` 的連線（模擬 `Get-NetTCPConnection` 對監聽連接埠的行為）
   - 針對每個符合條件的連線，會輸出：
     - **PID**：使用該連線的應用程式行程 ID
     - **本機位址**：本機 IP 與連接埠
     - **遠端位址**：遠端 IP 與連接埠（若適用；未連線時顯示 "N/A"）
     - **狀態**：連線狀態（例如 "LISTEN"）

3. **輸出**：
   - 輸出格式模擬 `Get-NetTCPConnection` 的表格形式，顯示 PID、本機位址、遠端位址及狀態

### 範例輸出：
若有網頁伺服器（例如 Apache 或 Nginx）正在監聽連接埠 80，輸出可能如下：
```
監聽連接埠 80 的 TCP 連線：
PID     本機位址             遠端位址            狀態
--------------------------------------------------
1234    0.0.0.0:80          N/A                 LISTEN
```

若無行程監聽連接埠 80：
```
未發現監聽連接埠 80 的 TCP 連線
```

### 注意事項：
- **跨平台相容**：`psutil` 程式庫可在 Windows、Linux 和 macOS 上執行，與僅限 Windows 的 `Get-NetTCPConnection` 不同
- **權限要求**：在某些系統上（例如 Linux 或 macOS），可能需要 root/管理員權限才能存取特定連線詳細資訊
- **篩選條件**：腳本預設篩選 `LISTEN` 狀態連線以符合 `Get-NetTCPConnection -LocalPort 80` 的典型使用情境。可修改篩選條件（例如移除 `conn.status == 'LISTEN'`）以包含其他連線狀態（如 `ESTABLISHED`）
- **擴充資訊**：可透過 `psutil.Process(conn.pid).name()` 延伸腳本功能以包含更多詳細資訊（例如行程名稱），前提是 PID 可用

此腳本提供了與 PowerShell 指令對等的 Python 實現，具備相似功能與輸出格式。如需額外功能或有特定需求，歡迎告知！