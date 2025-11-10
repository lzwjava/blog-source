---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 春季請求上下文實作選項
translated: true
type: note
---

Spring 微型「請求上下文」的絕佳應用場景。根據你的技術堆疊，有幾種簡潔方案可選：

### 1) 請求作用域 Bean（簡單安全）

將測試用戶 ID 儲存在請求作用域的 Bean 中，由 `TestUserFilter` 設置，任何元件均可注入讀取。

```java
// 在單次 HTTP 請求生命週期內保持數值
@Component
@RequestScope
public class TestUserContext {
  private String userId;
  public String getUserId() { return userId; }
  public void setUserId(String userId) { this.userId = userId; }
}
```

```java
@Component
public class TestUserFilter extends OncePerRequestFilter {
  private final TestUserContext ctx;
  public TestUserFilter(TestUserContext ctx) { this.ctx = ctx; }

  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain)
      throws ServletException, IOException {
    String id = req.getHeader("X-Test-User-Id");
    if (id == null) id = req.getParameter("testUserId");
    if (id != null && !id.isBlank()) ctx.setUserId(id);
    chain.doFilter(req, res); // 請求結束後請求作用域 Bean 會自動清理
  }
}
```

任意位置使用：

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // 未提供時返回 null
  }
}
```

**優勢：** 無需手動清理，同一請求內的控制器/服務/DAO 皆可運作。

---

### 2) Spring Security 上下文（若已使用 Spring Security 推薦首選）

透過篩選器設置 `Authentication`，所有元件均可透過 `SecurityContextHolder` 或 `@AuthenticationPrincipal` 讀取。

```java
@Component
public class TestUserFilter extends OncePerRequestFilter {
  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    String id = req.getHeader("X-Test-User-Id");
    if (id == null) id = req.getParameter("testUserId");

    if (id != null && !id.isBlank()) {
      var auth = new UsernamePasswordAuthenticationToken(
          id, "N/A", List.of(new SimpleGrantedAuthority("ROLE_TEST")));
      SecurityContextHolder.getContext().setAuthentication(auth);
    }
    try {
      chain.doFilter(req, res);
    } finally {
      SecurityContextHolder.clearContext();
    }
  }
}
```

任意位置使用：

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

或於控制器中注入 `Principal`/`Authentication`。

**優勢：** 完美整合方法級安全控制、審計紀錄與日誌等功能。

---

### 3) ThreadLocal 持有者（無需 Web/Security 依賴，切記清除）

若未使用請求作用域或 Security 組件：

```java
public final class TestUserHolder {
  private static final ThreadLocal<String> USER_ID = new InheritableThreadLocal<>();
  public static void set(String id) { USER_ID.set(id); }
  public static String get() { return USER_ID.get(); }
  public static void clear() { USER_ID.remove(); }
}
```

```java
@Component
public class TestUserFilter extends OncePerRequestFilter {
  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    String id = req.getHeader("X-Test-User-Id");
    if (id == null) id = req.getParameter("testUserId");
    if (id != null && !id.isBlank()) TestUserHolder.set(id);
    try {
      chain.doFilter(req, res);
    } finally {
      TestUserHolder.clear(); // 對線程池環境至關重要
    }
  }
}
```

若執行異步任務需傳遞上下文，可透過 `TaskDecorator` 複製 ThreadLocal。

---

### 實用技巧

* 將 ID 置於標頭如 `X-Test-User-Id`（便於從 Postman/MockMvc 傳遞）或查詢參數供本地測試
* 使用 MockMvc 進行單元測試：`.header("X-Test-User-Id", "u123")`
* 若需要對同次 HTTP 請求內所有 Bean 可見的簡易「儲存袋」，首選**方案 1**
* 若已使用 Spring Security 或需整合授權/審計功能，首選**方案 2**
* 僅在不想使用 Spring 作用域/Security 時採用**方案 3**，務必仔細清理避免記憶體洩漏