---
audio: false
generated: false
lang: zh
layout: post
title: WebSphere Liberty 服务器命令
translated: true
---

在管理 WebSphere Liberty 服务器时，经常使用一些命令来执行创建、启动、停止和监控服务器等基本任务。以下是最常用命令及其简要描述：

- **`./server create <server_name>`**
  创建一个具有指定名称的新服务器实例。此命令设置必要的目录结构和默认配置文件（例如 `server.xml`）。

- **`./server start <server_name>`**
  在后台启动服务器。服务器作为后台进程运行，日志记录到服务器的日志文件中。

- **`./server stop <server_name>`**
  停止正在运行的服务器实例。此命令优雅地关闭服务器。

- **`./server status <server_name>`**
  检查指定服务器是否正在运行。它返回当前状态（例如，已启动或已停止）。

- **`./server run <server_name>`**
  在前台启动服务器。这对于调试或监控很有用，因为服务器输出直接显示在控制台中。

- **`./server package <server_name>`**
  将服务器及其配置和应用程序打包到一个 zip 文件中。这对于将服务器部署到另一个环境或备份很有帮助。

- **`./server debug <server_name>`**
  以调试模式启动服务器，允许您将调试器附加到服务器进程以进行故障排除。

这些命令涵盖了有效管理 WebSphere Liberty 服务器所需的基本操作。对于更高级的任务，例如安装功能或管理安全性，可以使用 `featureUtility` 或 `securityUtility` 等附加工具，但这些工具在日常操作中使用得较少。