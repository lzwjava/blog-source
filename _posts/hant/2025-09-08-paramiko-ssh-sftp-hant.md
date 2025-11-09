---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Paramiko SSH 與 SFTP 指南
translated: true
type: note
---

### 安裝
Paramiko 是一個用於 SSH 和 SFTP 的 Python 函式庫。可透過 pip 安裝：

```bash
pip install paramiko
```

### 基本用法
Paramiko 允許你連接 SSH 伺服器、執行指令及傳輸檔案。請務必安全地處理私鑰並使用高強度密碼——Paramiko 支援金鑰認證與密碼認證。

核心概念：
- **Client**：使用 `paramiko.SSHClient()` 建立連線
- **Transport**：需進行底層控制時，使用 `paramiko.Transport()`
- 透過 `client.connect()` 進行認證，需提供主機名稱、使用者名稱，以及密碼或金鑰（例如透過 `paramiko.RSAKey.from_private_key_file()`）

### 範例：連接並執行指令
以下是連接 SSH 伺服器、執行指令並輸出結果的完整腳本。請替換佔位符為你的實際資料。

```python
import paramiko

# 建立 SSH client
client = paramiko.SSHClient()

# 自動加入主機金鑰（生產環境請謹慎使用，建議改為載入 known_hosts）
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 建立連接（可使用密碼或金鑰檔案）
    client.connect(
        hostname='your.server.com',
        port=22,  # 預設 SSH 端口
        username='your_username',
        password='your_password',  # 或使用 key_filename='path/to/private_key.pem'
    )

    # 執行指令
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # 讀取輸出
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("輸出:", output)
    print("錯誤:", error)

except paramiko.SSHException as e:
    print(f"SSH 錯誤: {e}")
finally:
    client.close()
```

### 進階範例：使用金鑰認證與檔案傳輸
如需使用金鑰認證，請先產生金鑰對（例如透過 `ssh-keygen`），將公鑰加入伺服器的 `~/.ssh/authorized_keys`，接著使用：

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 金鑰認證連接
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # 私鑰檔案路徑
    )

    # 執行指令
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # SFTP 範例：傳輸檔案
    sftp = client.open_sftp()
    sftp.put('local_file.txt', 'remote_file.txt')  # 上傳
    sftp.get('remote_file.txt', 'local_copy.txt')  # 下載
    sftp.close()

except Exception as e:
    print(f"錯誤: {e}")
finally:
    client.close()
```

### 技巧與最佳實踐
- **安全性**：建議優先使用金鑰認證而非密碼。生產環境應停用 `AutoAddPolicy`，並透過 `client.load_host_keys()` 驗證主機金鑰
- **錯誤處理**：務必捕捉 `paramiko.SSHException`，並透過 `exit_status = stdout.channel.recv_exit_status()` 檢查退出狀態碼
- **執行緒**：Paramiko 預設不具執行緒安全性，必要時請使用鎖定機制
- **文件**：詳情請參閱 [官方 Paramiko 文件](https://docs.paramiko.org/)。可搭配 OpenSSH 的 `sshd` 或本地虛擬機進行測試

以上內容可協助你快速入門，請根據實際需求調整使用！