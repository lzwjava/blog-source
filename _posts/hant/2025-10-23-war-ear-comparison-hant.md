---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 戰爭與企業存檔封裝比較
translated: true
type: note
---

### 概述
在 Java EE（現稱 Jakarta EE）中，WAR（Web 封存檔）與 EAR（企業封存檔）是將應用程式部署至應用伺服器（如 Tomcat、WildFly 或 GlassFish）的標準封裝格式。WAR 專注於網頁層元件，而 EAR 則將多個模組打包成完整的企業應用程式。以下為詳細比較。

| 比較維度           | WAR（網頁封存檔）                                                                 | EAR（企業封存檔）                                                                         |
|--------------------|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **用途**         | 將網頁應用程式（如 servlet、JSP、靜態內容）作為單一單元部署，以實現網頁層功能。 | 透過封裝多個子模組（如 WAR、EJB JAR）來部署企業應用程式，適用於多層式分散式系統。 |
| **內容**         | - 網頁應用檔案：JSP、HTML/CSS/JS、servlet。<br>- 函式庫：WEB-INF/lib 中的 JAR 檔。<br>- 部署描述檔：web.xml（新版本可選）。 | - 多個模組：WAR、EJB JAR、用戶端 JAR。<br>- 共享函式庫。<br>- 部署描述檔：application.xml。<br>- 資源配接器 RAR（可選）。 |
| **結構**         | - 根目錄：靜態資源（如 index.html）。<br>- WEB-INF/：classes、lib、web.xml。 | - 根目錄：META-INF/application.xml。<br>- 各模組的子目錄（如 myapp.war、myejb.jar）。 |
| **檔案副檔名**   | .war                                                                             | .ear                                                                                     |
| **部署範圍**     | 單一模組；可部署至網頁容器（如 Tomcat）或完整應用伺服器。                       | 多模組；僅能部署至完整應用伺服器（如 JBoss、WebLogic），以支援交易等企業功能。 |
| **規模與複雜度** | 較小且簡單；適合獨立的網頁應用程式。                                            | 較大且複雜；支援模組化及跨模組共享資源。        |
| **使用情境**     | 網頁入口網站、REST API、簡單服務（如以 WAR 封裝的 Spring Boot 網頁應用程式）。 | 複雜企業系統（如具網頁介面、商業邏輯與資料存取的銀行應用程式）。 |
| **相依性**       | 依賴容器提供網頁服務；不內建 EJB 支援。                                         | 支援 EJB、JMS 及跨模組相依性；促進鬆散耦合。              |

### 主要差異總結
- **模組化**：WAR 適用於網頁層的單體式結構；EAR 可組合多個 WAR/JAR。
- **伺服器需求**：WAR 可在輕量級網頁伺服器運行；EAR 需完整的 JEE 伺服器。
- **演進**：隨著微服務與雲原生趨勢（如 Spring Boot、Quarkus），WAR 常被用於容器化部署（Docker），而 EAR 雖較少見，但在傳統企業應用中仍具重要性。

實作範例可參考官方 Jakarta EE 文件：[Jakarta EE 教學](https://jakartaee.github.io/tutorial/) 或 Oracle 的 Java EE 存檔：[Java EE 封裝指南](https://docs.oracle.com/javaee/7/tutorial/packaging.htm)。