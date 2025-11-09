---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure Application Insights 設定指南
translated: true
type: note
---

## 什麼是 Azure Application Insights？

Azure Application Insights 是 Azure Monitor 中的應用程式效能管理 (APM) 服務，可協助您監控即時 Web 應用程式。它提供用於偵測問題、診斷問題以及透過遙測數據（如請求、相依性、追蹤、計量和日誌）了解使用者行為的工具。現已由 OpenTelemetry 提供支援，以實現更廣泛的兼容性。

## 必要條件
- 有效的 Azure 訂閱。
- 在 Azure 中建立資源的權限（例如，擁有者或參與者角色）。
- 您的應用程式程式碼（支援 .NET、Java、Node.js、Python 等）。

## 步驟 1：建立 Application Insights 資源
1. 登入 [Azure 入口網站](https://portal.azure.com)。
2. 點擊左上角選單中的 **建立資源**。
3. 搜尋 "Application Insights" 並從 **監視 + 管理** 下的結果中選擇它。
4. 填寫詳細資訊：
   - **訂閱**：選擇您的 Azure 訂閱。
   - **資源群組**：選擇現有群組或建立新群組。
   - **名稱**：為您的資源提供唯一名稱。
   - **區域**：選擇靠近您的使用者或應用程式的區域。
   - **工作區**：可選擇性地連結到現有的 Log Analytics 工作區；否則將自動建立新工作區。
5. 檢閱並點擊 **建立**。部署需要幾分鐘時間。
6. 建立完成後，前往您資源的 **概觀** 頁面並複製 **連接字串**（將滑鼠懸停在其上並點擊複製圖示）。這用於識別您的應用程式發送遙測數據的位置。

**提示**：為開發、測試和生產環境使用獨立的資源，以避免數據混雜。

## 步驟 2：檢測您的應用程式
添加 OpenTelemetry 支援以自動收集遙測數據（請求、異常、計量等）。透過名為 `APPLICATIONINSIGHTS_CONNECTION_STRING` 的環境變數設定連接字串（建議用於生產環境）。

### 對於 .NET (ASP.NET Core)
1. 安裝 NuGet 套件：
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. 在 `Program.cs` 中：
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. 使用您的連接字串設定環境變數並執行應用程式。

### 對於 Java
1. 下載 Azure Monitor OpenTelemetry Distro JAR（例如 `applicationinsights-agent-3.x.x.jar`）。
2. 在同一目錄中建立設定檔 `applicationinsights.json`：
   ```json
   {
     "connectionString": "您的連接字串"
   }
   ```
3. 使用代理程式執行您的應用程式：`java -javaagent:applicationinsights-agent-3.x.x.jar -jar your-app.jar`。

### 對於 Node.js
1. 安裝套件：
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. 在您的應用程式進入點中進行設定：
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. 設定環境變數並啟動您的應用程式。

### 對於 Python
1. 安裝套件：
   ```
   pip install azure-monitor-opentelemetry
   ```
2. 在您的應用程式中：
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="您的連接字串")
   ```
3. 執行應用程式。

對於其他語言或自動檢測（例如，對於 Azure App Service），請查閱官方文件。建議先在本機進行測試。

## 步驟 3：檢視和分析數據
1. 執行您已檢測的應用程式並產生一些活動（例如，發送請求）。
2. 在 Azure 入口網站中，開啟您的 Application Insights 資源。
3. 檢查 **概觀** 頁面：查看即時計量、請求數量和回應時間（數據約在 1-2 分鐘內出現）。
4. 探索功能：
   - **即時計量**：適用於生產應用程式的即時數據流。
   - **失敗**：深入分析異常和追蹤。
   - **效能**：分析相依性和慢速請求。
   - **使用量**：追蹤使用者工作階段和自訂事件。
   - **警示**：針對問題設定通知（例如，高失敗率）。
5. 在 **日誌** 中使用 Kusto 查詢語言 (KQL) 查詢數據以進行自訂分析。

## 最佳實踐
- 從基本遙測開始；根據需要添加自訂事件/計量。
- 透過 **使用量和估計成本** 頁面監控成本（透過 Log Analytics 計費）。
- 對於瀏覽器監控，請將 JavaScript SDK 程式碼片段添加到您的網頁中。

[建立和設定 Application Insights 資源](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[在 Application Insights 中啟用 OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[Application Insights 概觀](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)