---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用 Psutil 終止端口進程
translated: true
type: note
---

### 使用 psutil 偵測並終止指定連接埠的處理程序 (Windows)

Psutil 是一個跨平台的 Python 函式庫，用於擷取執行中處理程序的資訊與系統使用率。你可以使用它來尋找監聽特定連接埠的處理程序（例如，識別像是 npm 開發伺服器是否正在該連接埠上執行），然後終止該處理程序。這在 Windows 上可行，但請注意：

- **權限**：在 Windows 上，終止處理程序通常需要管理員權限（請以管理員身分執行你的 Python 腳本）。否則可能會引發 `AccessDenied` 例外。
- **連接埠偵測**：我們將專注於「inet」類型的 TCP 連線（涵蓋 IPv4 和 IPv6）。這對於由 `npm run dev` 或類似指令啟動的網頁伺服器來說很常見。
- **假設**：我們假設你要檢查的是監聽（伺服器）連接埠（例如，本地綁定的東西）。如果你指的是對某連接埠的輸出連線，方法會略有不同——如需澄清請告知。

#### 步驟 1：安裝 psutil
如果尚未安裝：
```bash
pip install psutil
```

#### 步驟 2：偵測與終止的範例程式碼
這是一個完整的 Python 腳本。它定義了一個函式來尋找監聽指定連接埠的 PID（使用你指定的 `kind='inet'`），然後終止它。在 Windows 上，`terminate()` 比 `kill()` 更受推薦，因為它允許優雅關閉（相當於 Unix 上的 SIGTERM）。

```python
import psutil
import time  # 用於可選的延遲

def get_pid_listening_on_port(port, kind='inet'):
    """
    掃描網路連線，尋找監聽指定連接埠的處理程序。
    回傳 PID 列表（通常只有一個，但在罕見情況下可能有多個）。
    """
    pids = []
    for conn in psutil.net_connections(kind=kind):
        # 檢查是否為監聽連線 (status='LISTEN') 且本地地址的連接埠符合
        if conn.status == 'LISTEN' and conn.laddr and conn.laddr.port == port:
            if conn.pid:
                pids.append(conn.pid)
    return pids

def kill_process_on_port(port, kind='inet'):
    """
    尋找並終止監聽指定連接埠的處理程序。
    如果有多個處理程序，則全部終止（並發出警告）。
    """
    pids = get_pid_listening_on_port(port, kind)
    if not pids:
        print(f"在連接埠 {port} 上未找到任何監聽中的處理程序。")
        return
    
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"正在終止連接埠 {port} 上的處理程序 {proc.name()} (PID {pid})...")
            # 使用 terminate() 進行優雅關閉；它發送類似 SIGTERM 的信號
            proc.terminate()
            # 可選：等待一段時間，如果沒有結束則強制終止
            gone, still_alive = psutil.wait_procs([proc], timeout=3)
            if still_alive:
                print(f"正在強制終止 PID {pid}...")
                still_alive[0].kill()
        except psutil.AccessDenied:
            print(f"存取遭拒：無法終止 PID {pid}。請以管理員身分執行？")
        except psutil.NoSuchProcess:
            print(f"處理程序 {pid} 已不存在。")

# 使用範例：將 3000 替換為你的目標連接埠（例如，npm 開發伺服器常使用 3000）
if __name__ == "__main__":
    kill_process_on_port(3000)  # 如有需要可調整 kind（例如，'inet4' 僅限 IPv4）
```

#### 關鍵說明
- **`psutil.net_connections(kind='inet')`**：這會擷取 'inet' 類型的網路連線（包含 IPv4 和 IPv6）。每個連線都是一個具名元組，包含以下欄位：
  - `laddr`：本地地址（例如 ('0.0.0.0', 8080) – IP 與連接埠）。
  - `status`：'LISTEN' 表示伺服器正在等待連線。
  - `pid`：擁有者的處理程序 ID。
  - 我們過濾 `status == 'LISTEN'` 來尋找伺服器（如 npm 的開發連接埠），而非用戶端連線。
- **PID 擷取**：腳本直接從連線元組取得 PID。如果你只想偵測而不終止，請使用 `get_pid_listening_on_port(port)`，它會回傳 PID(s)。
- **終止處理程序**：
  - `psutil.Process(pid).terminate()`：發送終止信號。在 Windows 上，這類似於 CTRL+C。
  - 如果它沒有結束，我們可選地用 `kill()` 強制終止（相當於 SIGKILL）。
  - Psutil 的 `wait_procs()` 會等待處理程序結束。
- **inet 類型的特定性**：'inet' 包含 IPv4 和 IPv6。如果你知道是 IPv4，請改為 `kind='inet4'`。此名稱直接符合你對「inet 類型」的要求。
- **Windows 特定注意事項**：
  - Psutil 能良好處理 Windows 內部細節，但在某些情況下，網路資訊可能需要提升的權限。
  - 對於低於 1024 的連接埠（特權連接埠），只有系統服務可以綁定，但偵測應該仍然有效。
- **錯誤處理**：加入了基本檢查，處理無處理程序或存取問題的情況。
- **測試**：執行類似 `npm run dev` 的指令來佔用連接埠 3000，然後執行此腳本。

如果這不完全符合你的需求（例如，如果「npm run port」意指其他東西，或者你想偵測非監聽連線），請提供更多細節以便改進！為了安全起見，請確保你只終止目標處理程序。