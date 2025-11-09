---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 Amazon RDS 搭配 MySQL
translated: true
type: note
---

Amazon RDS (Relational Database Service) for MySQL 是一項託管式資料庫服務，可讓您在雲端輕鬆設定、操作及擴展 MySQL 資料庫。它會處理備份、修補和擴展等例行任務，讓您能專注於應用程式開發。本指南將引導您完成基礎操作：建立 MySQL 資料庫執行個體、連線至該執行個體，以及執行簡單操作。為簡化流程，我們將使用 AWS Management Console。

**費用注意事項：** AWS 免費方案為新帳戶提供有限用量，但超出部分將產生費用。請務必在完成後刪除資源，以避免意外帳單。在生產環境中，請遵循安全性最佳實務，例如使用 VPC、加密和最小權限存取。

## 先決條件
- AWS 帳戶（如需註冊請前往 [aws.amazon.com](https://aws.amazon.com)）
- 對 AWS 主控台和 MySQL 有基本認識
- 為進行安全連線測試，我們將在相同 VPC（虛擬私有雲端）中建立 EC2 執行個體。請確認您的公共 IP 位址（例如透過 [checkip.amazonaws.com](https://checkip.amazonaws.com)）以進行 SSH 存取
- 選擇離您最近的 AWS 區域（例如 US East (N. Virginia)）

**最佳實務：** 使用 VPC 中的私有資料庫執行個體，將存取權限限制僅限受信任的資源。啟用 SSL/TLS 以進行加密連線。

## 步驟 1：建立用於連線的 EC2 執行個體
此步驟將設定一個簡單的 Linux 伺服器，用於連線至您的私有資料庫執行個體。

1. 登入 [AWS Management Console](https://console.aws.amazon.com) 並開啟 EC2 主控台
2. 選擇您的區域
3. 點擊 **Launch instance**
4. 設定：
   - **名稱：** `ec2-database-connect`
   - **AMI：** Amazon Linux 2023（符合免費方案資格）
   - **執行個體類型：** t3.micro（符合免費方案資格）
   - **金鑰對：** 建立或選擇現有金鑰對以進行 SSH 存取
   - **網路設定：** 編輯 > 允許 SSH 流量來自 **My IP**（或您的特定 IP，例如 `192.0.2.1/32`）。為安全起見，請避免使用 `0.0.0.0/0`
   - 儲存和標籤保留預設值
5. 點擊 **Launch instance**
6. 從執行個體詳細資訊中記下執行個體 ID、Public IPv4 DNS 和金鑰對名稱
7. 等待狀態顯示為 **Running**（約 2-5 分鐘）

**安全性提示：** 將 SSH 存取限制僅限您的 IP。請安全下載金鑰對（.pem 檔案）。

## 步驟 2：建立 MySQL 資料庫執行個體
使用「簡易建立」功能，透過預設值快速設定。

1. 開啟 [RDS 主控台](https://console.aws.amazon.com/rds/)
2. 選擇與您的 EC2 執行個體相同的區域
3. 在導覽窗格中，點擊 **Databases** > **Create database**
4. 選擇 **Easy create**
5. 在 **Configuration** 下方：
   - 引擎類型：**MySQL**
   - 範本：**Free tier**（付費帳戶可選擇 **Sandbox**）
   - 資料庫執行個體識別符：`database-test1`（或自訂名稱）
   - 主使用者名稱：`admin`（或自訂名稱）
   - 主密碼：自動產生或設定高強度密碼（請安全記錄）
6. （可選）在 **Connectivity** 下方，選擇 **Connect to an EC2 compute resource** 並選取您的 EC2 執行個體以簡化設定
7. 點擊 **Create database**
8. 檢視憑證彈出視窗（使用者名稱/密碼）—請妥善保存，因為密碼後續無法擷取
9. 等待狀態變更為 **Available**（最多 10-20 分鐘）。從 **Connectivity & security** 標籤記下 **Endpoint**（DNS 名稱）和連接埠（預設：3306）

**最佳實務：** 在生產環境中，使用「標準建立」自訂 VPC、備份（啟用自動化）和儲存。啟用刪除保護和多可用區域以實現高可用性。

## 步驟 3：連線至資料庫執行個體
從您的 EC2 執行個體使用 MySQL 用戶端進行連線。

1. SSH 連線至您的 EC2 執行個體：
   ```
   ssh -i /path/to/your-key-pair.pem ec2-user@your-ec2-public-dns
   ```
   （請替換為您的詳細資訊；例如 `ssh -i ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com`）

2. 在 EC2 執行個體上更新套件：
   ```
   sudo dnf update -y
   ```

3. 安裝 MySQL 用戶端：
   ```
   sudo dnf install mariadb105 -y
   ```

4. 連線至資料庫：
   ```
   mysql -h your-db-endpoint -P 3306 -u admin -p
   ```
   在提示時輸入主密碼

若成功，您將看到 MySQL 提示字元（`mysql>`）

**疑難排解：** 確保安全性群組允許來自 EC2 執行個體在連接埠 3306 上的輸入流量。若需外部連線，請將資料庫設為公開（不建議）或使用堡壘主機/VPN。

**安全性提示：** 使用 `--ssl-mode=REQUIRED` 進行加密連線：`mysql -h endpoint -P 3306 -u admin -p --ssl-mode=REQUIRED`

## 步驟 4：基礎使用
連線成功後，即可執行 SQL 指令。範例：

- 顯示資料庫：`SHOW DATABASES;`
- 建立範例資料庫：`CREATE DATABASE myapp;`
- 使用資料庫：`USE myapp;`
- 建立資料表：
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
  );
  ```
- 插入資料：`INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');`
- 查詢：`SELECT * FROM users;`
- 結束：`EXIT;`

從應用程式（例如 Python、Node.js）中，使用標準 MySQL 驅動程式，並以端點、連接埠、使用者名稱和密碼作為連線字串。

**最佳實務：** 透過 CloudWatch 監控效能、啟用自動化備份，並根據需要垂直擴展（執行個體大小）或水平擴展（讀取複本）。

## 清理：刪除資源
為停止計費：

1. **刪除 EC2 執行個體：** EC2 主控台 > 選擇執行個體 > **Instance state** > **Terminate** > 確認
2. **刪除資料庫執行個體：** RDS 主控台 > 選擇資料庫 > **Actions** > **Delete** > 取消勾選建立快照 > 確認

請檢查 AWS Billing 主控台以確認是否有任何執行中的資源。

如需進階主題（例如遷移、效能調校或 API/CLI 使用），請參閱 AWS 文件。

## 參考資料
- [建立並連線至 MySQL 資料庫執行個體](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
- [開始使用 Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)