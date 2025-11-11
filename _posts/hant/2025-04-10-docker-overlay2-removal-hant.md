---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 解決Docker Overlay2移除錯誤
translated: true
type: note
---

該錯誤表示 Docker 無法移除容器的 overlay2 檔案系統 — 核心/虛擬機傳回了底層 I/O 錯誤 (`readdirent merged: bad message`)。在 macOS 上，這通常發生在 Docker 虛擬機或 overlay 儲存處於不良狀態時。以下是您可以嘗試恢復的安全、有序步驟（從破壞性最小 → 更積極的方法）。

**重要提示：** 以下部分指令可能會移除資料（映像/儲存卷）。我將標記破壞性步驟並顯示確切的指令，以便您需要時可以複製/貼上。

---

# 快速檢查（安全）

在終端機中執行：

```bash
# 顯示容器狀態及有問題的容器 ID
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# 嘗試強制移除容器
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

如果 `docker rm -f` 成功，問題就解決了。如果它因相同的 overlay 錯誤而失敗，請繼續下一步。

---

# 重新啟動 Docker（macOS Docker Desktop）— 建議的下一步（安全）

完全退出 Docker Desktop（使用鯨魚圖示 → 退出），然後重新啟動它。或者從命令列執行：

```bash
# macOS — 透過 AppleScript 重新啟動 Docker Desktop
osascript -e 'quit app "Docker"'
open -a Docker
```

Docker 重新啟動後，再次嘗試 `docker compose down` 或 `docker rm -f <id>`。

---

# 重新啟動主機（非常安全）

如果可能重新啟動，重啟 macOS 通常可以清除虛擬機檔案系統問題：

* 重新啟動 Mac，然後啟動 Docker Desktop 並重試。

---

# 如果仍然失敗 — 使用 Docker Desktop 疑難排解動作（安全 / 中等）

開啟 Docker Desktop → 疑難排解：

* 點擊 **Restart Docker**（如果您尚未這樣做）。
* 如果失敗，請嘗試 **Clean / Purge data** 或 **Reset to factory defaults** — **警告**：這些操作會移除映像/容器/儲存卷。僅在您可以承受損失本地 Docker 資料的情況下使用。

---

# 如果您使用 Docker Engine（Linux）或熟悉手動清理（破壞性）

**僅在您了解資料遺失風險時執行此操作。** 停止 Docker 守護行程，移除有問題 ID 的 overlay2 目錄，然後重新啟動 Docker。

```bash
# 停止 docker 守護行程 (Linux)
sudo systemctl stop docker

# 首先備份 overlay2 資料夾（可選，如果您有空間）
sudo cp -a /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f /root/overlay2-backup-7acbf095

# 如果備份完成 / 不需要，則移除該 overlay 的 merged 目錄：
sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f

# （可選）如有需要，移除容器元資料
# 警告：僅移除您確定與損壞容器對應的檔案
sudo rm -rf /var/lib/docker/containers/ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18

# 啟動 docker
sudo systemctl start docker

# 然後嘗試清理懸置項目
docker system prune -a --volumes
```

再次強調：刪除 `/var/lib/docker` 下的檔案具有破壞性，如果操作不當可能會損壞其他容器。僅在您知道要刪除什麼時使用。

---

# 通常有幫助的較低破壞性清理

如果您無法直接刪除 overlay 或偏好較溫和的方法：

```bash
# 嘗試清理未使用的物件
docker system prune -f
docker volume prune -f

# 移除未使用的映像/容器（請小心）
docker image prune -a -f
docker container prune -f
```

這可以釋放空間，有時能讓 Docker 成功重新執行移除操作。

---

# 如果問題重複發生且您使用 Docker Desktop for Mac

* 考慮增加 Docker 虛擬機磁碟大小（Settings → Resources → Disk image size）。
* 如果您依賴重要的本地資料，請在使用 Reset/Purge 之前先匯出儲存卷/容器（`docker export`, `docker save`）。

---

# 要收集的診斷資訊（如果您希望我進一步幫助）

如果以上方法都無法解決問題，請分享以下（非破壞性）指令的輸出，我將建議有針對性的後續步驟：

```bash
docker info
docker ps -a
docker compose version
docker version
# 列出 overlay 目錄 (Linux)
ls -lah /var/lib/docker/overlay2 | head -n 40
```

（如果您使用的是 macOS Docker Desktop，`ls /var/lib/docker` 不會顯示虛擬機內容 — 建議優先重新啟動 Docker Desktop 或使用疑難排解 UI。）

---

如果您願意，請告訴我您執行的是 **Docker Desktop on macOS**（最有可能）還是 **Docker Engine on Linux** — 我將提供一個更短的、量身定制的步驟順序。如果您願意，我也可以產生一個可以按順序執行的單行檢查清單。