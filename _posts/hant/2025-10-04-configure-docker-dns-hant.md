---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 Docker 守護程式 DNS 伺服器
translated: true
type: note
---

要為 Docker 守護程式配置 DNS 伺服器（將由容器使用，除非在容器層級被覆寫），您可以編輯 `/etc/docker/daemon.json` 檔案。此檔案允許您自訂 Docker 的運行時行為。

### 配置 DNS 的步驟

1. **編輯 daemon.json 檔案**：
   - 如果檔案不存在，請使用 root 權限建立它（例如使用 `sudo nano /etc/docker/daemon.json` 或您偏好的編輯器）。
   - 新增或更新 `dns` 鍵值作為 DNS 伺服器的 IP 地址陣列。例如，要使用 Google 的公共 DNS（8.8.8.8 和 8.8.4.4）：

     ```json
     {
       "dns": ["8.8.8.8", "8.8.4.4"]
     }
     ```

     - 您可以根據需要新增更多伺服器（例如 Cloudflare 的 1.1.1.1）。
     - 此設定將應用於所有使用預設網路建立的容器，除非另有指定。

2. **驗證 JSON**：
   - 確保檔案是有效的 JSON。您可以使用像 `jq` 這樣的工具來檢查：`jq . /etc/docker/daemon.json`。如果出現錯誤，請修正語法。

3. **重新啟動 Docker 服務**：
   - 透過重新啟動 Docker 來應用變更：
     ```
     sudo systemctl restart docker
     ```
     - 在非 systemd 系統上（例如較舊的 Linux 發行版），請使用 `sudo service docker restart`。
   - 驗證狀態：`sudo systemctl status docker`。

4. **測試配置**：
   - 運行一個測試容器並檢查其 DNS 解析：
     ```
     docker run --rm busybox nslookup google.com
     ```
     - 它應該使用您配置的 DNS 伺服器進行解析。

### 注意事項
- **範圍**：此配置用於主機上的 Docker 守護程式的 DNS，影響容器的出站名稱解析。它不會變更主機的系統 DNS。
- **覆寫**：如果容器需要不同的 DNS（例如透過 `docker run` 中的 `--dns` 標誌），它將覆寫此守護程式層級的設定。
- **安全性**：對於大多數情況，使用像 8.8.8.8 這樣的公共 DNS 是可以的，但在企業環境中考慮使用內部 DNS。
- **文件**：有關更多選項（例如 DNS 搜尋網域），請參閱 [官方 Docker 關於 daemon.json 的文件](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)。

如果您遇到錯誤（例如權限問題或 JSON 解析錯誤），請分享詳細資訊以進行進一步的故障排除。