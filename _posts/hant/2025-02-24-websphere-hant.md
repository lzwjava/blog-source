---
audio: false
lang: hant
layout: post
title: WebSphere Liberty Server 指令
translated: true
---

當管理 WebSphere Liberty 伺服器時，經常使用多個命令來執行基本任務，例如創建、啟動、停止和監控伺服器。以下是最常用命令的列表，並附上每個命令的簡要描述：

- **`./server create <server_name>`**
  創建一個具有指定名稱的新伺服器實例。此命令設置必要的目錄結構和預設配置文件（例如 `server.xml`）以供伺服器使用。

- **`./server start <server_name>`**
  以背景模式啟動伺服器。伺服器作為背景進程運行，並將日誌寫入伺服器的日誌文件。

- **`./server stop <server_name>`**
  停止正在運行的伺服器實例。此命令優雅地關閉伺服器。

- **`./server status <server_name>`**
  檢查指定的伺服器是否正在運行。它返回當前狀態（例如啟動或停止）。

- **`./server run <server_name>`**
  以前台模式啟動伺服器。這對於調試或監控非常有用，因為伺服器輸出會直接顯示在控制台中。

- **`./server package <server_name>`**
  將伺服器及其配置和應用程序打包到一個 zip 文件中。這對於將伺服器部署到另一個環境或備份非常有幫助。

- **`./server debug <server_name>`**
  以調試模式啟動伺服器，允許您將調試器附加到伺服器進程以進行故障排除。

這些命令涵蓋了有效管理 WebSphere Liberty 伺服器所需的基本操作。對於更高級的任務，例如安裝功能或管理安全性，還有其他工具可用，例如 `featureUtility` 或 `securityUtility`，但這些工具在日常操作中使用得較少。