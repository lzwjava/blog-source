---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Windows Taskkill 指令指南
translated: true
type: note
---

在 Windows 系統中，`taskkill` 是一個內建的命令列工具，可用於透過**程序 ID (PID)** 或**映像名稱 (執行檔名稱)** 來停止（終結）程序。

### 基本語法

```bat
taskkill /PID <程序_id> [/F]
taskkill /IM <映像名稱> [/F]
```

* `/PID <程序_id>` → 透過程序 ID 終結程序。
* `/IM <映像名稱>` → 透過程序名稱終結程序（例如 `notepad.exe`）。
* `/F` → 強制終結程序。
* `/T` → 終結指定程序及其所有子程序。

---

### 範例

1. **透過 PID 終結程序：**

```bat
taskkill /PID 1234
```

這將嘗試停止 PID 為 1234 的程序。

2. **透過 PID 強制終結程序：**

```bat
taskkill /PID 1234 /F
```

3. **透過名稱終結程序：**

```bat
taskkill /IM notepad.exe
```

4. **透過名稱強制終結程序：**

```bat
taskkill /IM notepad.exe /F
```

5. **終結程序及其子程序：**

```bat
taskkill /IM cmd.exe /T /F
```

---

### 尋找 PID

若不知道 PID：

```bat
tasklist
```

這將列出所有執行中的程序及其 PID。接著便可對目標程序使用 `taskkill /PID`。

---

⚠️ **注意事項**

* 部分系統程序無法被終結。
* 終結受保護的程序時，可能需要以**管理員身份**執行命令提示字元。

---

需要我示範如何將 `tasklist` 和 `taskkill` 結合使用嗎（例如自動終結所有符合名稱的程序）？