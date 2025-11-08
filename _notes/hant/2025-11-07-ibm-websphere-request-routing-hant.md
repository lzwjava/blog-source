---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-4.5-sonnet
title: IBM WebSphere 請求路由詳解
translated: true
type: note
---

讓我解釋 IBM WebSphere Application Server (WAS) 如何處理傳入請求與路由：

## IBM WAS 中的請求流程

當請求送達 IBM WAS 時，典型流程如下：

**1. 網頁伺服器層（可選）**
- 請求首先到達 IBM HTTP Server (IHS) 或其他網頁伺服器
- 網頁伺服器外掛程式將請求路由至適當的 WAS 實例

**2. Web 容器進入點**
請求通過 **Web 容器** 進入 WAS，該容器是主要 servlet 引擎的一部分。關鍵套件結構為：

```
com.ibm.ws.webcontainer.*
```

**3. 請求處理鏈**

路由透過以下幾個組件實現：

**傳輸通道框架**
- `com.ibm.ws.channel.*` - 處理網路通訊
- HTTP 傳輸通道接收請求

**Web 容器處理**
```
com.ibm.ws.webcontainer.servlet.ServletWrapper
com.ibm.ws.webcontainer.filter.WebAppFilterManager
```

**4. 過濾器鏈執行**

過濾器的運作方式與標準 Java Servlet 過濾器完全相同，但由 WAS 管理：

- **在應用程式的 web.xml 中定義**
- 過濾器按照指定順序鏈接
- 每個過濾器可檢查/修改請求和回應
- 使用標準 `javax.servlet.Filter` 介面

```xml
<filter>
    <filter-name>MyFilter</filter-name>
    <filter-class>com.example.MyFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>MyFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**過濾器執行順序：**
1. WAS 在應用程式啟動時載入過濾器配置
2. WebAppFilterManager 建立過濾器鏈
3. 每個請求：請求 → 過濾器1 → 過濾器2 → ... → Servlet

## IBM WAS 中的主要套件

**核心套件：**
- `com.ibm.ws.webcontainer.*` - Web 容器實現
- `com.ibm.ws.runtime.*` - 執行時服務
- `com.ibm.websphere.servlet.*` - WAS 特定 servlet 擴展
- `com.ibm.ws.channel.*` - 傳輸層
- `com.ibm.ejs.*` - EJB 容器服務
- `com.ibm.ws.naming.*` - JNDI 實現

## 路由機制

**虛擬主機路由：**
- 在 WAS 管理控制台中配置
- 將 `主機名稱:端口` 組合映射到應用程式
- 配置路徑：`虛擬主機 → 主機別名 → 應用程式`

**上下文根路由：**
- 每個應用程式都有上下文根（例如 `/myapp`）
- WAS 維護已部署應用程式的註冊表
- URI 映射：`http://伺服器:端口/上下文根/servlet路徑`

**Servlet 映射：**
- 在 web.xml 或註解中定義
- 模式匹配（精確、路徑、擴展名、預設）

## 應用程式啟動順序

當應用程式啟動時：
1. **類別載入器初始化** - 應用程式獲取專屬類別載入器
2. **web.xml 解析** - 載入過濾器、servlet、監聽器
3. **ServletContextListeners 觸發** - `contextInitialized()`
4. **過濾器實例化** - 呼叫 `init()` 方法
5. **啟動時載入的 servlet** - 初始化優先載入的 servlet
6. **應用程式標記為已啟動** - 準備接收請求

路由註冊表會更新，應用程式現在可透過其上下文根進行存取。

這樣是否說明了 WAS 如何處理請求路由與過濾？