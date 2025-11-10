---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Springリクエストコンテキスト実装の選択肢
translated: true
type: note
---

Springで小さな「リクエストコンテキスト」を使う優れたユースケースです。スタックに基づいていくつかのクリーンな選択肢があります：

### 1) リクエストスコープのBean（シンプルで安全）

テストユーザーIDをリクエストスコープのBeanに保存し、`TestUserFilter`が設定し、任意のコンポーネントが注入/読み取り可能にします。

```java
// 単一のHTTPリクエストのライフタイム中に値を保持する
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
    chain.doFilter(req, res); // リクエスト終了後、リクエストスコープBeanは自動的にクリーンアップされる
  }
}
```

任意の場所で使用：

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // 提供されていない場合はnull
  }
}
```

**理由：** 手動クリーンアップ不要。同じリクエスト内のコントローラー/サービス/DAO間で動作。

---

### 2) Spring Securityコンテキスト（既にSpring Securityを使用している場合に推奨）

フィルターが`Authentication`を設定し、すべてのコンポーネントが`SecurityContextHolder`または`@AuthenticationPrincipal`経由で読み取り可能にします。

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

任意の場所で使用：

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

またはコントローラーで`Principal`/`Authentication`を注入。

**理由：** メソッドセキュリティ、監査、ログなどと適切に連携。

---

### 3) ThreadLocalホルダー（Web/セキュリティ依存関係なしで動作。クリアを忘れずに）

リクエストスコープやSecurityを使用しない場合：

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
      TestUserHolder.clear(); // スレッドプールでは必須
    }
  }
}
```

非同期タスクを実行し伝播が必要な場合は、ThreadLocalをコピーする`TaskDecorator`を追加します。

---

### クイックヒント

* IDを`X-Test-User-Id`のようなヘッダー（Postman/MockMvcから渡しやすい）またはローカルテスト用のクエリパラメータに配置します。
* MockMvcを使用した単体テストの場合：`.header("X-Test-User-Id", "u123")`
* 同じHTTPリクエスト内の任意のBeanに表示されるシンプルな「バッグ」が必要な場合は**オプション1**を推奨。
* 既にSpring Securityを使用している場合、または認証/監査統合が必要な場合は**オプション2**を推奨。
* Springスコープ/セキュリティを使用したくない場合にのみ**オプション3**を使用。リークを避けるためクリアに細心の注意を払ってください。