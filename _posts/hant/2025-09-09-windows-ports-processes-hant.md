---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 管理 Windows 連接埠與程序
translated: true
type: note
---

在 Windows 系統上，你可以使用 `netstat` 指令檢查哪些端口正在被監聽（以及由哪個行程（PID）監聽），然後使用 `taskkill` 管理或終止這些行程。在除錯後端專案（例如 Java Spring Boot 應用程式、Redis 或 MySQL）時，這通常很有用。方法如下：

---

### 1. 檢查監聽端口

以**系統管理員身份**執行**命令提示字元 (cmd)** 或 **PowerShell**：

```bash
netstat -ano | findstr LISTENING
```

* `-a` → 顯示所有連線和監聽端口
* `-n` → 以數字形式顯示地址和端口
* `-o` → 包含 PID（行程識別碼）

範例輸出：

```
TCP    0.0.0.0:8080     0.0.0.0:0     LISTENING     12345
TCP    0.0.0.0:3306     0.0.0.0:0     LISTENING     6789
```

這裡：

* 端口 `8080` 由 PID `12345` 使用（可能是你的 Spring Boot 應用程式）。
* 端口 `3306` 由 PID `6789` 使用（MySQL）。

---

### 2. 找出該 PID 對應的行程

你可以將 PID 與行程名稱匹配：

```bash
tasklist | findstr 12345
```

輸出可能顯示：

```
java.exe                  12345 Console                    1     512,000 K
```

這表示你的 Spring Boot 應用程式正在端口 8080 上執行。

---

### 3. 如有需要，終止行程

如果你想停止該行程：

```bash
taskkill /PID 12345 /F
```

* `/PID` → 指定行程識別碼
* `/F` → 強制終止

---

### 4. 常見後端服務的典型端口

* **Spring Boot (Java 應用程式):** 8080、8081 等
* **MySQL:** 3306
* **Redis:** 6379
* **PostgreSQL:** 5432

因此，如果你在 `netstat` 輸出中看到這些端口，就會知道哪個服務正在執行。

---

👉 專業提示：你可以將這些指令組合為一個命令，直接找出哪個行程正在使用特定端口（例如 8080）：

```bash
netstat -ano | findstr :8080
```

然後取得 PID 並使用 `tasklist` 檢查。

---

你想讓我為你展示一個 **PowerShell 單行指令**，可以直接將端口映射到行程名稱，而無需單獨使用 `tasklist` 檢查嗎？