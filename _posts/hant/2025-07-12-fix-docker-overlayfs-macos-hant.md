---
audio: false
generated: true
image: false
lang: hant
layout: post
model: google/gemini-2.5-flash
title: 修復 macOS 上的 Docker OverlayFS 損毀問題
translated: true
type: note
---

您遇到的錯誤 `driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/.../merged: readdirent merged: bad message`，表明 Docker 的儲存機制（OverlayFS）出現深度損毀，通常是由操作中斷或主機檔案系統問題引起。

由於您使用的是 **macOS**（運行 Docker Desktop），Docker 守護程式及其儲存是在專用的 **Linux 虛擬機（VM）** 內管理的。您無法像在原生 Linux 系統上那樣直接存取 `/var/lib/docker/overlay2`，這使得修復變得更簡單、更安全，只需專注於 Docker Desktop 應用程式本身即可。

以下是在 macOS 上解決此問題最安全且最有效的步驟順序：

-----

## 1. 強制停止並強制移除容器

失敗的容器是 `chat-mongodb`（ID: `ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18`）。首先，嘗試使用其名稱或 ID 進行強制移除。

1.  **停止整個堆疊**（以確保沒有後台進程持有鎖）：

    ```bash
    docker compose stop
    ```

2.  使用 `-f` 標記**強制移除特定容器**：

    ```bash
    docker rm -f chat-mongodb
    # 或者使用 ID：
    # docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
    ```

3.  **再次嘗試運行您原始的命令**（`docker compose down` 或等效命令）。如果錯誤仍然存在，請轉到步驟 2。

-----

## 2. 重啟 Docker Desktop

簡單的重啟通常可以清除內部 VM 中的暫時性鎖定問題或損毀狀態。

### 選項 A：使用選單列（推薦）

1.  點擊 macOS 選單列中的 **Docker 鯨魚圖示**。
2.  選擇 **Restart**。

### 選項 B：使用終端機

您可以強制結束並重新開啟應用程式：

```bash
killall Docker && open /Applications/Docker.app
```

Docker 重啟後，請等待約 30 秒讓它完全啟動，然後再次嘗試運行您原始的命令。

-----

## 3. 清除 Docker 的快取和未使用資料（清理）

如果重啟失敗，一個強大的清理命令通常可以解決更深層的損毀問題，方法是移除可能與錯誤相關的未使用或「懸空」元件。

**警告：** 此命令將移除所有已停止的容器、未使用的網路和懸空的映像。如果您有想要保留（已停止但未移除）的容器，請備份它們或跳過此步驟。

在終端機中運行以下命令：

```bash
docker system prune -a --volumes
```

  * **`-a`** (全部) 會移除所有未使用的映像（不僅僅是懸空的映像）。
  * **`--volumes`** 會移除未使用的匿名卷（這可能是 `overlay2` 損毀的來源）。

系統將要求您確認。輸入 `y` 並按 Enter。清理完成後，再次嘗試運行您原始的命令。

-----

## 4. 將 Docker Desktop 恢復出廠設定

這是最後的手段，因為它將**刪除您所有的容器、映像和卷**（包括您儲存在非掛載卷中的任何本地資料）。它會強制內部 Docker VM 完全重新開始。

1.  點擊 macOS 選單列中的 **Docker 鯨魚圖示**。
2.  前往 **Settings (或 Preferences)** $\rightarrow$ **Troubleshoot**。
3.  點擊 **Reset to factory settings...**

重置後，Docker 將以一個乾淨的狀態重新啟動，您應該能夠運行 `docker compose up` 命令來重新構建您的環境。