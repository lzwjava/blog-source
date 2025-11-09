---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Linux 防火牆設定指南
translated: true
type: note
---

好問題——在 Linux 系統（例如 **Red Hat** 或 **Ubuntu**）中設定防火牆主要涉及使用 **`firewalld`** 或 **`ufw`**，具體取決於您的系統。以下是適用於兩大系統系列的清晰指南，方便您選擇合適的方案。

---

### 🔹 在 **Red Hat / CentOS / Fedora** 系統上（使用 firewalld）

#### 1. 檢查 `firewalld` 是否已安裝並運行

```bash
sudo systemctl status firewalld
```

若未運行：

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

#### 2. 基礎操作

檢查活躍區域（區域用於分組介面與規則）：

```bash
sudo firewall-cmd --get-active-zones
```

列出當前區域的所有規則：

```bash
sudo firewall-cmd --list-all
```

#### 3. 允許或封鎖連接埠/服務

允許連接埠（例如 SSH 使用 22 埠）：

```bash
sudo firewall-cmd --permanent --add-port=22/tcp
```

允許已知服務（例如 HTTP）：

```bash
sudo firewall-cmd --permanent --add-service=http
```

封鎖/移除服務：

```bash
sudo firewall-cmd --permanent --remove-service=http
```

重新載入以套用變更：

```bash
sudo firewall-cmd --reload
```

#### 4. 驗證規則

```bash
sudo firewall-cmd --list-all
```

---

### 🔹 在 **Ubuntu / Debian** 系統上（使用 ufw）

Ubuntu 預裝 **UFW**（簡易防火牆），管理更便捷。

#### 1. 啟用 UFW

```bash
sudo ufw enable
```

#### 2. 允許/拒絕連接埠或服務

允許 SSH：

```bash
sudo ufw allow ssh
```

允許 HTTP（80 埠）：

```bash
sudo ufw allow 80/tcp
```

允許特定連接埠範圍：

```bash
sudo ufw allow 1000:2000/tcp
```

拒絕服務：

```bash
sudo ufw deny 23/tcp
```

#### 3. 檢查狀態

```bash
sudo ufw status verbose
```

#### 4. 需要時重設規則

```bash
sudo ufw reset
```

---

### 🔹 通用設定技巧

若要**封鎖所有傳入流量僅開放少數例外**，可執行：

1. 預設拒絕所有傳入流量

   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```

   *（在 `firewalld` 中，可透過區域或丟棄區域實現類似行為）*

2. 隨後選擇性開放特定連接埠（例如 22、80、443）。

---

### 🔹 安全提示

遠端設定防火牆時，務必**先允許 SSH 連接**——否則可能導致自身被鎖定在外。

---

需要我示範**基礎防火牆設定範例**嗎（例如針對僅開放 SSH + HTTP + HTTPS 的典型網頁伺服器）？