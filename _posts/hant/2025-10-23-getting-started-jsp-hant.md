---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: JSP 入門指南
translated: true
type: note
---

JavaServer Pages (JSP) 是一項伺服器端技術，用於在 Java 應用程式中建立動態網頁內容。它允許您將 Java 程式碼直接嵌入 HTML 頁面，從而更容易根據用戶輸入或資料生成動態回應。JSP 是 Jakarta EE（前身為 Java EE）平台的一部分，並能與 Web 應用程式中的 servlet 良好協作。

以下是從設定到部署的 JSP 入門逐步指南。假設您已具備 Java 和 HTML 的基礎知識。

## 1. 先決條件
- **Java Development Kit (JDK)**：安裝 JDK 8 或更高版本（現代應用程式建議使用 JDK 17+）。可從 [Oracle](https://www.oracle.com/java/technologies/downloads/) 下載或使用 OpenJDK。
- **網頁伺服器/容器**：使用 Apache Tomcat（免費且適合初學者）。從 [Apache Tomcat](https://tomcat.apache.org/) 下載。
- **IDE（可選但建議）**：IntelliJ IDEA、Eclipse 或帶有 Java 擴充功能的 VS Code，以便更輕鬆地進行開發。

## 2. 設定環境
1. 安裝 Tomcat：
   - 將 Tomcat 壓縮檔解壓縮到目錄中（例如 Windows 上的 `C:\tomcat` 或 Linux 上的 `/opt/tomcat`）。
   - 執行 `bin/startup.bat`（Windows）或 `bin/startup.sh`（Unix）啟動 Tomcat。在瀏覽器中存取 `http://localhost:8080` 以確認其正常運行。

2. 建立專案結構：
   - 在 Tomcat 的 `webapps` 資料夾中，為您的應用程式建立一個新目錄（例如 `my-jsp-app`）。
   - 在其中建立：
     - `WEB-INF/web.xml`（部署描述符，在 JSP 2.2+ 中為可選，但適合用於配置）。
     - 一個用於 JSP 檔案的根資料夾（例如 `index.jsp`）。

   基本 `web.xml` 範例：
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
            https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
            version="5.0">
       <display-name>My JSP App</display-name>
   </web-app>
   ```

## 3. 編寫您的第一個 JSP 頁面
JSP 檔案具有 `.jsp` 副檔名，並使用小腳本（`<% %>`）、表達式（`<%= %>`）和宣告（`<%! %>`）將 HTML 與 Java 程式碼結合。對於現代最佳實踐，請使用 JSP 表達式語言（EL）和 JSTL（JavaServer Pages 標準標籤庫）以避免使用原始小腳本。

範例：在您的應用程式根目錄中建立 `index.jsp`：
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>  <!-- 若使用 JSTL -->

<html>
<head>
    <title>Hello JSP</title>
</head>
<body>
    <h1>Welcome to JSP!</h1>
    
    <!-- 小腳本：Java 程式碼 -->
    <% 
        String name = request.getParameter("name") != null ? request.getParameter("name") : "World";
        java.util.Date now = new java.util.Date();
    %>
    
    <!-- 表達式：輸出值 -->
    <p>Hello, <%= name %>! The time is <%= now %>.</p>
    
    <!-- 使用 EL（表達式語言）以獲得整潔的輸出 -->
    <p>Your name via EL: ${param.name}</p>
    
    <!-- JSTL 範例：遍歷列表 -->
    <c:set var="fruits" value="${{'Apple', 'Banana', 'Cherry'}}" />
    <ul>
        <c:forEach var="fruit" items="${fruits}">
            <li>${fruit}</li>
        </c:forEach>
    </ul>
</body>
</html>
```

- **關鍵元素**：
  - **指令**：`<%@ page ... %>` 設定頁面屬性；`<%@ taglib ... %>` 導入標籤庫。
  - **小腳本**：嵌入 Java 程式碼（請謹慎使用；建議優先使用 EL/JSTL）。
  - **EL**：`${expression}` 用於在不使用小腳本的情況下存取資料。
  - **JSTL**：從 [Apache Taglibs](https://tomcat.apache.org/taglibs/standard/) 下載並將 JAR 檔案置於 `WEB-INF/lib` 中。

## 4. 部署與運行
1. 將您的應用程式資料夾（例如 `my-jsp-app`）置於 Tomcat 的 `webapps` 目錄中。
2. 重新啟動 Tomcat。
3. 在瀏覽器中存取：`http://localhost:8080/my-jsp-app/index.jsp`。
4. 使用查詢參數測試：`http://localhost:8080/my-jsp-app/index.jsp?name=Grok` 以查看動態輸出。

## 5. 常見功能與最佳實踐
- **表單與用戶輸入**：使用 `<form>` 標籤和 `request.getParameter()` 或 EL（`${param.field}`）來處理提交。
- **會話與 Bean**：使用 `session.setAttribute()` 進行狀態管理；使用 JavaBeans 處理可重複使用的資料。
- **錯誤處理**：在 `web.xml` 中添加 `<error-page>` 或使用 `<%@ page errorPage="error.jsp" %>`。
- **安全性**：清理輸入以防止 XSS；在生產環境中使用 HTTPS。
- **現代替代方案**：JSP 仍在使用中，但對於新專案，請考慮使用 Thymeleaf 或 Spring MVC，因為它們更靈活。
- **除錯**：檢查 Tomcat 日誌（`logs/catalina.out`）以查找錯誤。

## 6. 進階主題
- 與 Servlet 整合：JSP 用於視圖，Servlet 用於邏輯（MVC 模式）。
- 資料庫連接：使用 JDBC 或 JPA（例如與 H2 或 MySQL 搭配使用）。
- 建置工具：使用 Maven/Gradle 管理依賴項，例如 JSTL。

對於動手實踐，請從簡單的 "Hello World" 開始，並逐步添加功能。如果您正在建置完整的 Web 應用程式，請探索 Jakarta EE 教程。

## 參考資料
- [Oracle JSP Tutorial](https://docs.oracle.com/javaee/7/tutorial/jspx.htm)
- [Baeldung: Introduction to JSP](https://www.baeldung.com/jsp-tutorial)
- [Apache Tomcat JSP Examples](https://tomcat.apache.org/tomcat-10.1-doc/jsp-examples/)