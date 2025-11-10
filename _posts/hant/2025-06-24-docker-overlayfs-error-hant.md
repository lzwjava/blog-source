---
audio: false
generated: true
image: false
lang: hant
layout: post
model: google/gemini-2.5-flash
title: 修復 Docker OverlayFS 移除錯誤
translated: true
type: note
---

你所遇到的錯誤，特別是這一行：
`Error response from daemon: container ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18: driver "overlay2" failed to remove root filesystem: readdirnames /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged: readdirent merged: bad message`
表示 **Docker 儲存驅動程式（特別是 OverlayFS (overlay2)）出現問題**，這通常與主機上的檔案系統狀態損毀有關。此類問題通常發生在 Docker daemon 無法存取或正確清理容器檔案時。

以下是由侵入性最低的方法開始的逐步解決方案。

-----

## 1. 停止並強制移除容器

容器 `chat-mongodb` 移除失敗。你需要針對該特定容器進行操作。

### A. 嘗試強制移除

再次嘗試移除容器，但這次使用強制標記 (`-f`) 以確保容器不在運行中，並嘗試更積極的移除方式：

```bash
docker rm -f chat-mongodb
```

或使用容器 ID：

```bash
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18
```

### B. 停止 Docker Compose 堆疊

如果該容器是你嘗試拆除的較大堆疊的一部分（從 `[+] Running 3/3` 推斷），請先嘗試優雅地停止服務，然後再嘗試移除：

```bash
docker compose stop
# 然後再次嘗試原始指令
# 例如：docker compose down
```

-----

## 2. 重啟 Docker Daemon

簡單地重啟 Docker 服務通常可以清除暫時性的儲存驅動程式錯誤和鎖定檔案。

### 對於 Linux 系統（使用 systemd）：

```bash
sudo systemctl restart docker
```

### 對於 Docker Desktop (macOS/Windows)：

1.  點擊系統匣/選單列中的 **Docker 圖示**。
2.  導航至 **疑難排解**（或 **Settings** $\rightarrow$ **Daemon** $\rightarrow$ **Restart**）。
3.  點擊 **Restart**。

重啟後，再次嘗試移除容器。

-----

## 3. 手動清理損毀的目錄

**⚠️ 警告：** 此步驟涉及直接操作 Docker 的內部檔案結構，**僅應作為最後手段**，並且**必須在 Docker daemon 停止的狀態下進行**。不正確的手動刪除可能導致進一步損毀。

錯誤訊息指向 OverlayFS 儲存中的特定目錄：`/var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f/merged`。

1.  **停止 Docker daemon：**

    ```bash
    sudo systemctl stop docker
    ```

2.  **手動移除有問題的目錄：**

    ```bash
    # 僅移除 YOUR 錯誤訊息中顯示的目錄
    sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f
    ```

    *如果找不到確切的目錄，你可能需要嘗試更廣泛的清理（請參閱下一步）。*

3.  **啟動 Docker daemon：**

    ```bash
    sudo systemctl start docker
    ```

4.  **再次嘗試移除容器/堆疊。**

-----

## 4. 清理未使用的資料

如果上述步驟失敗，你可以使用 Docker 內建的清理指令。此指令會移除所有已停止的容器、所有未被任何容器使用的網路、所有懸置的映像檔以及所有建置快取。

```bash
docker system prune
```

**注意：** 此指令會要求確認，並移除你可能想保留但未主動使用的資料（例如已停止的容器）。使用 `-a` 標記來移除所有未使用的映像檔（不僅僅是懸置的映像檔）。