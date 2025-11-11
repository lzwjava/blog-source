---
audio: false
generated: true
lang: hant
layout: post
title: Java Servlet 中的 HTTP 會話
translated: true
type: note
---

讓我來解答你關於 `javax.servlet` 套件中 `HttpSession` 的工作原理、如何設定 session 值以及如何讀取的問題。我假設你問題中的 "HTTPSession" 是拼寫錯誤，正確的類別名稱應該是 `HttpSession`。

---

### **HttpSession 的工作原理**

`HttpSession` 是 `javax.servlet.http` 套件中的一個介面，用於在 Java 網路應用程式中實現狀態管理。HTTP 本身是無狀態的——客戶端（例如瀏覽器）向伺服器發出的每個請求都是獨立的，不會記住之前的互動。為了克服這個限制並在多個請求間追蹤使用者特定資料（例如使用者在網站訪問期間的資料），`HttpSession` 提供了一種維護「session」的機制。

工作原理如下：

1. **Session 建立**：當使用者首次訪問網路應用程式中的 servlet 時，servlet 容器（例如 Tomcat）會建立一個新的 `HttpSession` 物件。這個 session 會被分配一個唯一的識別符號，稱為 **session ID**。

2. **Session ID 傳輸**：session ID 會發送到客戶端的瀏覽器，通常以名為 `JSESSIONID` 的 cookie 形式傳送。在後續請求中，瀏覽器會包含這個 session ID，讓伺服器能將請求與現有的 session 關聯起來。

3. **備用機制**：如果瀏覽器停用了 cookie，servlet 容器可以使用 **URL 重寫** 作為備用方案。在這種情況下，session ID 會附加在 URL 後（例如 `http://example.com/page;jsessionid=abc123`），但這需要在應用程式程式碼中明確支援。

4. **伺服器端儲存**：實際的 session 資料（屬性）儲存在伺服器上，而非客戶端。客戶端僅持有 session ID，這使得 session 在儲存敏感資訊時比 cookie 更安全。資料通常保存在伺服器記憶體中，但在高級配置中可以持久化到磁碟或資料庫。

5. **Session 生命週期**：Session 有超時時間（例如預設 30 分鐘，可透過 `web.xml` 或程式方式配置）。如果使用者在超時時間內沒有活動，session 會過期，其資料將被丟棄。你也可以手動終止 session，例如在登出時。

這種機制讓伺服器能夠在多個請求間「記住」使用者特定資訊，例如登入狀態或購物車內容。

---

### **如何設定 Session 值**

要將資料儲存在 `HttpSession` 中，你可以使用 `setAttribute` 方法。這個方法將一個鍵（`String` 類型）與一個值（任何 Java 物件）關聯起來。具體步驟如下：

1. **取得 HttpSession 物件**：在 servlet 中，使用 `request.getSession()` 從 `HttpServletRequest` 物件中取得 `HttpSession`。如果 session 不存在，這個方法會建立一個新的 session，否則返回現有的 session。

2. **設定屬性**：在 `HttpSession` 物件上呼叫 `setAttribute(key, value)`。

以下是一個 servlet 中的範例：

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws IOException {
        // 取得 session（如果不存在則建立一個）
        HttpSession session = request.getSession();
        
        // 設定 session 屬性
        session.setAttribute("username", "Alice");
        
        // 回應客戶端
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Session value set: username = Alice");
    }
}
```

在這段程式碼中：
- `request.getSession()` 確保 session 可用。
- `session.setAttribute("username", "Alice")` 將字串 `"Alice"` 儲存在鍵 `"username"` 下。

---

### **如何讀取 Session 值**

要從 session 中讀取值，可以使用 `getAttribute` 方法。由於它返回一個 `Object`，你需要將其轉換為適當的類型。具體步驟如下：

1. **取得 HttpSession 物件**：使用 `request.getSession()` 或 `request.getSession(false)`（後者在沒有 session 存在時返回 `null`，避免建立新的 session）。

2. **取得屬性**：呼叫 `getAttribute(key)` 並轉換結果。

以下是一個範例：

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws IOException {
        // 取得 session（如果沒有 session 存在則返回 null）
        HttpSession session = request.getSession(false);
        
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        if (session != null) {
            // 讀取 session 屬性
            String username = (String) session.getAttribute("username");
            
            if (username != null) {
                out.println("Session value retrieved: username = " + username);
            } else {
                out.println("No username found in session.");
            }
        } else {
            out.println("No active session.");
        }
    }
}
```

在這段程式碼中：
- `request.getSession(false)` 取得現有的 session 或返回 `null`。
- `session.getAttribute("username")` 讀取值，並轉換為 `String`。
- 空值檢查防止 session 或屬性不存在時出現錯誤。

---

### **實際範例**

以下是一個跨請求設定和讀取 session 值的綜合範例：

1. **SetSessionServlet.java**（例如用於登入）：

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
        out.println("User set in session: Bob");
    }
}
```

2. **GetSessionServlet.java**（例如用於受保護頁面）：

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
            out.println("Welcome back, " + user);
        } else {
            out.println("Please log in first.");
        }
    }
}
```

當客戶端訪問 `SetSessionServlet` 時，session 會儲存 `"Bob"`。之後訪問 `GetSessionServlet` 時，會讀取並顯示該值，因為 session 在多個請求間持續存在。

---

### **補充說明**

- **Session 超時**：透過 `session.setMaxInactiveInterval(seconds)` 設定（例如 `session.setMaxInactiveInterval(1800)` 表示 30 分鐘），或在 `web.xml` 中設定：

  ```xml
  <session-config>
      <session-timeout>30</session-timeout> <!-- 單位為分鐘 -->
  </session-config>
  ```
- **結束 Session**：使用 `session.invalidate()`（例如用於登出）。
- **安全性**：使用 HTTPS 保護 session ID 不被攔截。避免在未加密的情況下儲存高度敏感資料。
- **類型轉換**：始終轉換 `getAttribute` 的結果，因為它返回 `Object`。

---

### **總結**

- **工作原理**：`HttpSession` 使用 session ID（透過 cookie 或 URL 重寫）維護使用者狀態，並在伺服器上儲存資料。
- **設定值**：`session.setAttribute("key", value)`。
- **讀取值**：`String value = (String) session.getAttribute("key")`。

這應該能讓你清楚理解 `javax.servlet` 中的 `HttpSession`。如果你需要進一步說明，請告訴我！