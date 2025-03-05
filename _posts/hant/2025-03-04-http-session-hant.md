---
audio: false
generated: true
lang: hant
layout: post
title: HTTP 會話在 Java Servlets
translated: true
---

讓我來回答你關於 `javax.servlet` 套件中的 `HttpSession` 如何運作、如何設置會話值以及如何檢索它的問題。我會假設你在問題中提到的 "HTTPSession" 是打字錯誤，實際上你是指 `HttpSession`，因為這是 `javax.servlet` 套件中的正確類名。

---

### **HttpSession 如何運作？**

`HttpSession` 是 `javax.servlet.http` 套件中的一個介面，它使 Java Web 應用程序能夠進行狀態管理。HTTP 本質上是無狀態的——每個來自客戶端（例如瀏覽器）到伺服器的請求都是獨立的，沒有記憶之前的互動。為了克服這個限制並跨多個請求追蹤用戶特定的數據（例如在用戶訪問網站期間），`HttpSession` 提供了一種維護 "會話" 的機制。

以下是它的工作原理：

1. **會話創建**：當用戶首次訪問 Web 應用程序中的 Servlet 時，Servlet 容器（例如 Tomcat）會創建一個新的 `HttpSession` 物件。該會話被分配一個唯一的標識符，稱為 **會話 ID**。

2. **會話 ID 傳輸**：會話 ID 通常以名為 `JSESSIONID` 的 Cookie 形式發送到客戶端的瀏覽器。在後續的請求中，瀏覽器會包含這個會話 ID，從而允許伺服器將請求與現有的會話關聯起來。

3. **備用機制**：如果在瀏覽器中禁用了 Cookie，Servlet 容器可以使用 **URL 重寫** 作為備用方案。在这种情况下，會話 ID 會附加到 URL（例如 `http://example.com/page;jsessionid=abc123`），但這需要應用程序代碼中的顯式支持。

4. **伺服器端存儲**：實際的會話數據（屬性）存儲在伺服器端，而不是客戶端。客戶端只保存會話 ID，這使得會話比 Cookie 更安全地存儲敏感信息。數據通常保存在伺服器內存中，但在高級配置中可以持久化到磁盤或數據庫。

5. **會話生命週期**：會話有一個超時期限（例如，默認 30 分鐘，可以通過 `web.xml` 或以編程方式配置）。如果用戶在這段時間內沒有活動，會話將過期並丟棄其數據。你也可以手動終止一個會話，例如在登出時。

這種機制使伺服器能夠在多個請求之間 "記住" 用戶特定的信息，例如登錄狀態或購物車內容。

---

### **如何設置會話值**

要在 `HttpSession` 中存儲數據，使用 `setAttribute` 方法。該方法將一個鍵（`String`）與一個值（任何 Java 物件）關聯起來。以下是如何做到的：

1. **獲取 HttpSession 物件**：在 Servlet 中，使用 `request.getSession()` 從 `HttpServletRequest` 物件獲取 `HttpSession`。該方法在不存在會話的情況下創建一個新會話，或者返回現有的會話。

2. **設置屬性**：在 `HttpSession` 物件上調用 `setAttribute(key, value)`。

以下是 Servlet 中的示例：

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // 获取会话（如果不存在则创建一个）
        HttpSession session = request.getSession();

        // 设置会话属性
        session.setAttribute("username", "Alice");

        // 回应客户端
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("会话值已设置：username = Alice");
    }
}
```

在這段代碼中：
- `request.getSession()` 確保會話可用。
- `session.setAttribute("username", "Alice")` 將字符串 `"Alice"` 存儲在鍵 `"username"` 下。

---

### **如何獲取會話值**

要從會話中檢索值，使用 `getAttribute` 方法。由於它返回一個 `Object`，你需要將其轉型為適當的類型。以下是過程：

1. **獲取 HttpSession 物件**：使用 `request.getSession()` 或 `request.getSession(false)`（後者在不存在會話的情況下返回 `null`，避免創建新會話）。

2. **獲取屬性**：調用 `getAttribute(key)` 並轉型結果。

以下是示例：

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // 获取会话（如果不存在则返回 null）
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null) {
            // 检索会话属性
            String username = (String) session.getAttribute("username");

            if (username != null) {
                out.println("会话值已检索：username = " + username);
            } else {
                out.println("会话中未找到用户名。");
            }
        } else {
            out.println("没有活动会话。");
        }
    }
}
```

在這段代碼中：
- `request.getSession(false)` 檢索現有會話或返回 `null`。
- `session.getAttribute("username")` 獲取值，轉型為 `String`。
- Null 檢查防止在會話或屬性不存在的情況下出錯。

---

### **實際示例**

以下是一個結合示例，展示了在請求之間設置和獲取會話值：

1. **SetSessionServlet.java**（例如，用於登錄）：

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession();
        session.setAttribute("user", "Bob");

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("用户已设置在会话中：Bob");
    }
}
```

2. **GetSessionServlet.java**（例如，用於受保護頁面）：

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null && session.getAttribute("user") != null) {
            String user = (String) session.getAttribute("user");
            out.println("欢迎回来，" + user);
        } else {
            out.println("请先登录。");
        }
    }
}
```

當客戶端訪問 `SetSessionServlet` 時，會話存儲 `"Bob"`。稍後，訪問 `GetSessionServlet` 會檢索並顯示它，因為會話在請求之間持續存在。

---

### **附加說明**

- **會話超時**：通過 `session.setMaxInactiveInterval(seconds)`（例如，`session.setMaxInactiveInterval(1800)` 為 30 分鐘）或在 `web.xml` 中設置：

  ```xml
  <session-config>
      <session-timeout>30</session-timeout> <!-- 以分钟为单位 -->
  </session-config>
  ```
- **結束會話**：使用 `session.invalidate()`（例如，用於登出）。
- **安全性**：使用 HTTPS 保護會話 ID 不被攔截。避免不加密存儲高度敏感數據。
- **類型轉換**：始終轉換 `getAttribute` 結果，因為它返回 `Object`。

---

### **總結**

- **如何運作**：`HttpSession` 使用會話 ID（通過 Cookie 或 URL 重寫）維護用戶狀態，並在伺服器端存儲數據。
- **設置值**：`session.setAttribute("key", value)`。
- **獲取值**：`String value = (String) session.getAttribute("key")`。

這應該能讓你對 `javax.servlet` 中的 `HttpSession` 有清晰的理解！如果你需要進一步的澄清，請告訴我！