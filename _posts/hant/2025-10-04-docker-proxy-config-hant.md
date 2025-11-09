---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 Docker 守護進程代理設定
translated: true
type: note
---

### 配置 Docker 守護程式的代理設定

Docker 守護程式可設定使用 HTTP/HTTPS 代理，以便在企業防火牆後執行如拉取映像或建置容器等操作。此設定需透過編輯（或建立）`/etc/docker/daemon.json` 檔案來完成。請注意，此配置僅適用於守護程式本身（例如用於 `docker pull` 或 `docker build`），而非個別容器（容器需使用環境變數或 Docker 建置參數）。

#### 先決條件
- 您需要在 Linux 系統上擁有 root 或 sudo 權限（這是 Docker 守護程式配置的主要作業系統；若使用 Windows/Mac 的 Docker Desktop，請改用圖形介面設定）。
- 已安裝並執行 Docker。
- 了解您的代理伺服器詳細資訊（例如 HTTP/HTTPS 代理的 `http://proxy.company.com:8080` 及任何無代理例外規則）。

#### 逐步配置說明

1. **定位或建立守護程式配置檔案**：
   - 開啟終端機並導航至 `/etc/docker/`（若目錄不存在請建立：`sudo mkdir -p /etc/docker`）。
   - 使用文字編輯器編輯 `daemon.json` 檔案（例如 `sudo nano /etc/docker/daemon.json` 或 `sudo vim /etc/docker/daemon.json`）。
   - 若檔案不存在，請建立新檔案。若是全新檔案，請從空 JSON 物件 `{}` 開始。

2. **新增代理配置**：
   - 在 JSON 檔案中加入 `"proxies"` 區段。以下為基本範例：

     ```json
     {
       "proxies": {
         "http-proxy": "http://proxy.company.com:8080",
         "https-proxy": "http://proxy.company.com:8080",
         "no-proxy": "localhost,127.0.0.1,*.company.com,10.0.0.0/8"
       }
     }
     ```

     - **說明**：
       - `"http-proxy"`：HTTP 代理的 URL（用於非 HTTPS 請求）。
       - `"https-proxy"`：HTTPS 代理的 URL（通常與 HTTP 代理相同）。
       - `"no-proxy"`：應繞過代理的主機/網域/IP 範圍清單（以逗號分隔），例如本機位址或內部網域。此設定可避免無限迴圈。
       - 若需要驗證，請使用格式 `http://username:password@proxy.company.com:8080`。
       - 對於 SOCKS 代理，請使用 `"http-proxy": "socks5://proxy.company.com:1080"`。

     - 若 `daemon.json` 已有現有內容（例如其他設定如 `"log-driver": "json-file"`），請將 `"proxies"` 區段合併至其中，避免重複鍵值。確保 JSON 語法正確（如有需要可使用 `jsonlint` 等工具驗證）。

3. **儲存並重啟 Docker 守護程式**：
   - 儲存檔案。
   - 重啟 Docker 服務以套用變更：
     ```
     sudo systemctl restart docker
     ```
     - 在舊版系統或非 systemd 環境中，請使用 `sudo service docker restart`。
   - 驗證守護程式是否執行：
     ```
     sudo systemctl status docker
     ```
     - 若出現問題請檢查日誌：`sudo journalctl -u docker.service`。

4. **驗證配置**：
   - 透過拉取映像進行測試（現在應透過代理路由）：
     ```
     docker pull hello-world
     ```
   - 檢查代理設定是否已套用，可檢視守護程式配置：
     ```
     docker info | grep -i proxy
     ```
     - 您應看到類似輸出：
       ```
       HTTP Proxy: http://proxy.company.com:8080
       HTTPS Proxy: http://proxy.company.com:8080
       No Proxy: localhost,127.0.0.1,*.company.com,10.0.0.0/8
       ```
   - 若您在建置情境中使用 Docker，請透過以下指令測試：
     ```
     docker build -t test-proxy .
     ```
     （假設使用會拉取基礎映像的簡單 Dockerfile。）

#### 補充說明
- **安全性**：在共享系統中避免將憑證硬編碼於 `daemon.json`。請盡可能使用環境變數，或進階設定工具如 `docker config`。
- **常見問題**：
  - **語法錯誤**：無效的 JSON 會導致守護程式無法啟動。請透過 `cat /etc/docker/daemon.json` 和 JSON 驗證工具雙重檢查。
  - **防火牆/SELinux**：請確保代理可連線，且無安全模組阻擋。
  - **Docker 版本**：此設定適用於 Docker 20.10+ 版本（早期版本使用不同的環境變數如 `HTTP_PROXY`）。請透過 `docker --version` 檢查版本，必要時進行升級。
  - **特定註冊庫代理**：對於私有註冊庫，您可能需要在 `daemon.json` 中額外配置 `"registry-mirrors"` 或不安全註冊庫設定。
- **容器設定**：若您需要在*運行中容器內部*設定代理（非守護程式），請在 Dockerfile 中設定環境變數（例如 `ENV http_proxy=http://proxy.company.com:8080`）或透過 `docker run -e http_proxy=...` 設定。
- **Docker Desktop (Windows/Mac)**：請前往 Settings > Resources > Proxies 啟用/配置代理，無需編輯 JSON 檔案。

更多詳細資訊，請參閱官方 Docker 文件：[Configure the Docker daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)。若遇到錯誤，請分享確切輸出內容以便排查問題！