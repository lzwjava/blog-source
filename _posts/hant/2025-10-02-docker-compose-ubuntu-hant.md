---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: Ubuntu 的 Docker Compose 安裝指南
translated: true
type: note
---

根據您的系統資訊，您正在 **x86_64** 架構上運行 **Ubuntu 24.04.2 LTS**。要從提供的 GitHub 發布版本 (v2.39.4) 下載適合您系統的 **Docker Compose** 二進位檔案，您應該選擇與 Linux x86_64 相容的二進位檔案。

### 推薦下載
您應該下載 **docker-compose-linux-x86_64** 二進位檔案，該檔案在提供的資源中未明確列出，但在 Docker Compose 發布版本中是 Linux x86_64 系統的標準二進位檔案。然而，從列出的資源來看，最適合您系統的選項是：

- **docker-compose-linux-aarch64** **不**適用，因為它是用於 ARM64 (aarch64) 架構，而您的系統是 x86_64。
- **darwin** 二進位檔案（例如 `docker-compose-darwin-x86_64`）是用於 macOS，而非 Linux。
- 原始碼選項（`Source code (zip)` 或 `Source code (tar.gz)`）需要手動編譯，這是不必要的，因為通常有預編譯的二進位檔案可用。

由於 **docker-compose-linux-x86_64** 二進位檔案在您提供的資源中未明確列出，但在 Docker Compose 發布版本中是標準的，您很可能可以在 GitHub 發布頁面的完整資源列表中找到它。如果不可用，您可以使用原始碼或透過替代方法（例如套件管理員或 pip）安裝 Docker Compose。

### 下載與安裝步驟
1. **確認二進位檔案**：訪問 v2.39.4 的 GitHub 發布頁面以確認 `docker-compose-linux-x86_64` 的可用性。發布頁面通常位於：
   [Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)

2. **下載二進位檔案**：
   如果 `docker-compose-linux-x86_64` 可用，請下載它。例如：
   ```bash
   curl -L "https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64" -o docker-compose
   ```

3. **驗證下載**：
   使用提供的校驗和來驗證下載檔案的完整性。例如，如果 `docker-compose-linux-x86_64.sha256` 檔案可用：
   ```bash
   echo "<sha256> docker-compose" | sha256sum --check
   ```
   將 `<sha256>` 替換為發布資源中的相應雜湊值（例如，`docker-compose-darwin-x86_64.sha256` 的 `df7ff3dd8080134b851e1e49265028697d27de71f9bdc187e3d833357b934f36`，但您需要 Linux 的等效值）。

4. **安裝二進位檔案**：
   將二進位檔案移動到您的 PATH 中的目錄，例如 `/usr/local/bin`：
   ```bash
   chmod +x docker-compose
   sudo mv docker-compose /usr/local/bin/docker-compose
   ```

5. **驗證安裝**：
   檢查安裝的版本：
   ```bash
   docker-compose --version
   ```
   它應該輸出 `Docker Compose version v2.39.4`。

### 替代安裝方法
如果 `docker-compose-linux-x86_64` 二進位檔案不可用，或者您偏好更簡單的方法，您可以使用套件管理員或 pip 安裝 Docker Compose，因為您的系統已安裝 Python 3.13.4：

#### 透過套件管理員（推薦用於 Ubuntu）
Docker Compose 通常可在 Ubuntu 的軟體庫或 Docker 的官方軟體庫中找到：
```bash
sudo apt update
sudo apt install docker-compose-plugin
```
這將安裝 Docker Compose 外掛，這是使用 Docker Compose 的現代方式（使用 `docker compose` 而非 `docker-compose`）。請注意，Ubuntu 軟體庫中的版本可能不是 exactly v2.39.4，請使用以下命令檢查：
```bash
docker compose version
```

#### 透過 pip (Python)
由於您有 Python 3.13.4，您可以透過 pip 安裝 Docker Compose：
```bash
pip3 install docker-compose==2.39.4
```
這將安裝特定版本。使用以下命令驗證：
```bash
docker-compose --version
```

### 注意事項
- `checksums.txt` 檔案（SHA256: `1a9c3370b88825ab2b229bb90eda6f703d84018ea1d56b5ba573f8893c9ab6b4`）可用於驗證下載檔案的完整性。
- 如果您選擇從原始碼編譯（`Source code (zip)` 或 `Source code (tar.gz)`），您將需要 Go（您的系統資訊中未列出）和額外的設定，這更為複雜，除非必要，否則不推薦。
- 此發布版本包含改進和修復（例如，支援 `develop.watch.initial_sync`、無專案的 volume ls 以及 bake 的 TLS），如果您使用這些功能，這些改進和修復是相關的。

如果您需要幫助找到確切的 `docker-compose-linux-x86_64` 二進位檔案或遇到問題，請告訴我，我可以進一步指導您！

[Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)