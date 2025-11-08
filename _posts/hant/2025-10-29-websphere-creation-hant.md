---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 正確建立 WebSphere Application Server
translated: true
type: note
---

不，指令 `nodeName -name serverName admin create applciation server`（請注意「applciation」的拼寫錯誤）在 IBM WebSphere Application Server (WAS) 中使用 wsadmin 指令碼建立應用程式伺服器是不正確的。

### 正確語法
正確的指令應使用 Jython（wsadmin 推薦的指令碼語言）中的 `AdminTask.createApplicationServer` 方法。它需要：
- **節點名稱** 作為第一個參數（字串）。
- 包含伺服器名稱 `-name` 的**選項列表**作為第二個參數。

**基本範例：**
```jython
AdminTask.createApplicationServer('YourNodeName', ['-name', 'YourServerName'])
```

- 將 `'YourNodeName'` 替換為實際節點名稱（例如 `ndnode1`）。
- 將 `'YourServerName'` 替換為所需的伺服器名稱（例如 `appServer1`）。
- 可選參數可以添加到列表中，例如使用預設伺服器範本的 `'-templateName', 'default'`。

### 執行步驟
1. 以 Jython 模式啟動 wsadmin：`./wsadmin.sh -lang jython -user admin -password pass`。
2. 執行上述指令。
3. 儲存配置：`AdminConfig.save()`。
4. 退出：`quit`。

這將在指定節點上建立一個基礎應用程式伺服器。如需更多選項（例如連接埠、JVM 設定），請參閱完整的 AdminTask 文件。

[AdminTask 物件的 ServerManagement 指令群組](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[使用指令碼建立伺服器](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)