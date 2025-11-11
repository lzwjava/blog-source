---
audio: false
generated: true
lang: hant
layout: post
title: 建置與部署 Docker 映像檔
translated: true
type: note
---

以下係逐步指南，教你將 Spring Boot 應用程式構建成 Docker 映像檔並部署到伺服器：

### 前置準備
1. 本地安裝 **Java**（例如 JDK 17 或相容版本）
2. 安裝 **Maven** 或 **Gradle**（根據你的 Spring Boot 專案設定）
3. 本地機器及伺服器上安裝 **Docker**
4. 準備好可容器化的 **Spring Boot 專案**
5. 具備 **伺服器存取權限**（例如透過 SSH）且已安裝 Docker

---

### 步驟 1：準備你的 Spring Boot 應用程式
確保你的 Spring Boot 應用程式在本地正常運作。使用以下指令測試：
```bash
mvn spring-boot:run  # 如使用 Maven
# 或
gradle bootRun       # 如使用 Gradle
```

確認應用程式構建成功：
```bash
mvn clean package    # Maven
# 或
gradle build         # Gradle
```
此指令會生成 `.jar` 檔案（例如 `target/myapp-1.0.0.jar`）

---

### 步驟 2：建立 Dockerfile
在專案根目錄（`.jar` 檔案所在位置）建立名為 `Dockerfile` 的檔案，內容如下：

```dockerfile
# 使用官方 OpenJDK 運行環境作為基礎映像檔
FROM openjdk:17-jdk-slim

# 設定容器內的工作目錄
WORKDIR /app

# 將 Spring Boot JAR 檔案複製到容器內
COPY target/myapp-1.0.0.jar app.jar

# 暴露 Spring Boot 應用程式運行的端口（預設為 8080）
EXPOSE 8080

# 運行 JAR 檔案
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**注意事項：**
- 請將 `myapp-1.0.0.jar` 替換為你的實際 JAR 檔案名稱
- 如果應用程式使用不同 Java 版本，請調整版本號（`openjdk:17-jdk-slim`）

---

### 步驟 3：構建 Docker 映像檔
在包含 `Dockerfile` 的目錄中執行：
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` 為映像檔標記為 `myapp` 並設定版本為 `latest`
- `.` 指示 Docker 使用當前目錄作為構建上下文

驗證映像檔是否建立：
```bash
docker images
```

---

### 步驟 4：本地測試 Docker 映像檔
本地運行容器以確保正常運作：
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` 將本機的 8080 端口映射到容器內的 8080 端口
- 開啟瀏覽器或使用 `curl` 測試（例如 `curl http://localhost:8080`）

使用 `Ctrl+C` 停止容器，或透過 `docker ps` 查找容器 ID 後停止：
```bash
docker stop <container-id>
```

---

### 步驟 5：推送映像檔到 Docker Registry（可選）
要部署到伺服器，你需要將映像檔推送到像 Docker Hub 這樣的 registry（或私有 registry）。如果跳過此步驟，則需手動傳輸映像檔

1. 登入 Docker Hub：
   ```bash
   docker login
   ```
2. 為映像檔標記：
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. 推送映像檔：
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### 步驟 6：部署到伺服器
#### 選項 1：使用 Registry
1. SSH 連線到伺服器：
   ```bash
   ssh user@server-ip
   ```
2. 拉取映像檔：
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. 運行容器：
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` 在後台運行容器（分離模式）

#### 選項 2：手動傳輸
如果未使用 registry：
1. 本地將映像檔儲存為 `.tar` 檔案：
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. 傳輸到伺服器（例如透過 SCP）：
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. SSH 連線到伺服器：
   ```bash
   ssh user@server-ip
   ```
4. 載入映像檔：
   ```bash
   docker load -i myapp.tar
   ```
5. 運行容器：
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### 步驟 7：驗證部署
檢查容器是否運行：
```bash
docker ps
```

從伺服器或外部測試應用程式：
- 如在伺服器上：`curl http://localhost:8080`
- 如從外部：使用伺服器 IP（例如 `http://server-ip:8080`），確保伺服器防火牆已開放該端口

---

### 可選增強功能
- **環境變數**：傳遞配置到應用程式：
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**：對於多容器設置，使用 `docker-compose.yml` 檔案
- **重啟策略**：添加 `--restart unless-stopped` 確保容器在伺服器重啟時自動重啟

如有任何特定步驟需要協助，請隨時告知！

---

從你提供的錯誤輸出中，我們發現有幾個問題導致 `docker build` 指令無法成功。讓我們逐步分析並解決這些問題：

---

### 識別到的問題
1. **缺少 `docker-buildx` 外掛**  
   錯誤：`fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`  
   這表示 Docker 嘗試使用 `buildx` 外掛（現代化構建工具），但該外掛未正確安裝或配置

2. **舊版建構器棄用警告**  
   警告：`DEPRECATED: The legacy builder is deprecated...`  
   Docker 建議切換到 BuildKit（`buildx`），但系統回退到舊版建構器且執行失敗

3. **Docker Daemon 未運行**  
   錯誤：`Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`  
   Docker daemon（管理容器的背景服務）未在你的系統上運行

4. **檔案存取錯誤**  
   錯誤：`Can't add file ... to tar: io: read/write on closed pipe` 和 `Can't close tar writer...`  
   這些是因 daemon 未運行導致建構過程失敗所產生的次要問題

5. **偵測到代理設定**  
   你的系統正在使用代理（`HTTP_PROXY` 和 `HTTPS_PROXY`）。如果未正確配置，可能會干擾 Docker 運作

---

### 逐步修復

#### 1. 驗證 Docker Daemon 是否運行
核心問題是 Docker daemon 未運行。修復方法如下：

- **在 macOS 上**（假設使用 Docker Desktop）：
  1. 從應用程式資料夾或 Spotlight 開啟 Docker Desktop
  2. 確保它正在運行（選單列的 Docker 鯨魚圖示應顯示為綠色）
  3. 如果無法啟動：
     - 退出 Docker Desktop 並重新啟動
     - 檢查更新：Docker Desktop > Check for Updates
     - 如果仍然失敗，請從 [docker.com](https://www.docker.com/products/docker-desktop/) 重新安裝 Docker Desktop

- **透過終端機檢查**：
  執行：
  ```bash
  docker info
  ```
  如果 daemon 正在運行，你會看到系統資訊。如果沒有，你會收到相同的「無法連接」錯誤

- **手動重啟 Daemon**（如需要）：
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

當 daemon 運行後，繼續下一步驟

---

#### 2. 安裝 `buildx` 外掛（可選但建議）
既然舊版建構器已被棄用，讓我們設置 `buildx`：

1. **安裝 `buildx`**：
   - 手動下載二進位檔或使用 Docker 的說明：
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     （請檢查 [最新版本](https://github.com/docker/buildx/releases) 以符合你的作業系統/架構，例如 M1/M2 Mac 使用 `darwin-arm64`）

2. **驗證安裝**：
   ```bash
   docker buildx version
   ```

3. **將 BuildKit 設為預設**（可選）：
   在 `~/.docker/config.json` 中添加：
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

或者，你可以暫時跳過此步驟並使用舊版建構器（見步驟 4）

---

#### 3. 處理代理設定
你的代理設定（`http://127.0.0.1:7890`）可能會干擾 Docker 獲取映像檔。配置 Docker 使用這些代理：

1. **透過 Docker Desktop**：
   - 開啟 Docker Desktop > Settings > Resources > Proxies
   - 啟用「Manual proxy configuration」並輸入：
     - HTTP Proxy：`http://127.0.0.1:7890`
     - HTTPS Proxy：`http://127.0.0.1:7890`
   - 應用並重啟

2. **透過 CLI**（如未使用 Desktop）：
   建立或編輯 `~/.docker/config.json`：
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   編輯後重啟 Docker

---

#### 4. 重新嘗試構建
現在 daemon 正在運行且代理已配置，重新嘗試構建：

```bash
docker build -t myapp:latest .
```

- 如果你安裝了 `buildx`，它將預設使用 BuildKit
- 如果你跳過了 `buildx`，添加 `--progress=plain` 強制使用舊版建構器：
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. 排查 `.git/hooks` 錯誤（如持續出現）
`.git/hooks/pre-rebase.sample` 錯誤表示 Docker 嘗試在構建上下文中包含不必要的檔案。透過 `.dockerignore` 檔案排除它們：

1. 在 `Dockerfile` 同目錄建立 `.dockerignore`：
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. 這告訴 Docker 忽略 `.git` 資料夾和 `target/` 中的所有內容（除了你的 JAR 檔案）

3. 重新嘗試構建：
   ```bash
   docker build -t myapp:latest .
   ```

---

### 最終驗證
- 檢查映像檔：
  ```bash
  docker images
  ```
- 本地運行：
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- 使用 `curl http://localhost:8080` 測試

---

### 後續步驟
當映像檔成功構建後，請按照我先前的回應中的部署步驟操作（例如推送到 registry 或傳輸到伺服器）。如遇到更多問題，請隨時告知！