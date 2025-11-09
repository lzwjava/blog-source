---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Docker GHCR TLS 逾時錯誤
translated: true
type: note
---

您遇到的錯誤 `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout`，通常表示 Docker 嘗試從 GitHub Container Registry (GHCR) 拉取映像時出現網絡問題。以下是一些疑難排解和修復步驟：

---

### 1. **檢查網絡連接**
- 確保您的機器擁有穩定的網絡連接。
- 嘗試在瀏覽器中存取 `https://ghcr.io`，以確認能夠連接到該網站。

---

### 2. **檢查 Docker 守護程式狀態**
- 重新啟動 Docker 守護程式：
  ```bash
  sudo systemctl restart docker
  ```
- 確認 Docker 正在運行：
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **配置 Docker DNS**
- 如果您處於公司網絡或代理伺服器後方，Docker 可能需要自訂 DNS 設定。
- 編輯或建立 `/etc/docker/daemon.json`：
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- 重新啟動 Docker：
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **檢查代理伺服器設定**
- 如果您使用代理伺服器，請配置 Docker 使用它：
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- 將 `your-proxy-address:port` 替換為您的實際代理伺服器詳細資料。

---

### 5. **手動重新拉取映像**
- 嘗試手動拉取映像，檢查問題是否持續：
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- 如果成功，請重新執行 `docker-compose up -d`。

---

### 6. **檢查防火牆/網絡限制**
- 確保您的防火牆或網絡沒有封鎖對 `ghcr.io` 的存取。
- 暫時停用防火牆進行測試：
  ```bash
  sudo ufw disable
  ```
  （測試後如需，請重新啟用。）

---

### 7. **更新 Docker 和 Docker-Compose**
- 確保您使用的是最新版本：
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **設定 UID/GID 環境變數**
- 關於 `UID` 和 `GID` 的警告並非關鍵錯誤，但您可以在 `.env` 檔案或 `docker-compose.yml` 中設定它們以隱藏警告：
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **使用其他 Registry 鏡像（可選）**
- 如果 GHCR 持續無法連接，可以嘗試使用鏡像（但不建議在生產環境中使用）：
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
  將此設定加入 `/etc/docker/daemon.json` 並重新啟動 Docker。

---

### 10. **檢查時間同步**
- 確保您的系統時間已同步：
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### 指令摘要表格

| 步驟 | 指令/操作 |
|------|----------------|
| 重新啟動 Docker | `sudo systemctl restart docker` |
| 檢查 Docker 狀態 | `sudo systemctl status docker` |
| 配置 DNS | 編輯 `/etc/docker/daemon.json` |
| 手動拉取映像 | `docker pull ghcr.io/librechat/librechat:latest` |
| 設定 UID/GID | `echo "UID=$(id -u)" >> .env` |

---

如果嘗試以上步驟後問題仍然存在，請提供以下指令的輸出：
```bash
docker info
```
以及執行上述指令時看到的任何錯誤訊息。這將有助於進一步診斷問題！