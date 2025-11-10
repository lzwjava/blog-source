---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JavaサーブレットAPIガイドの基礎
translated: true
type: note
---

以下は、従来の **`javax.servlet.*`** 名前空間（Servlet 2.x–4.x 時代）における Java **Servlet** API の実用的なエンドツーエンドガイドです。また、**`jakarta.servlet.*`** への移行後の変更点についても記載しているため、将来に備えることができます。

# 1) Servlet とは？

**Servlet** は、**Servlet コンテナ**（Tomcat、Jetty、WebSphere、WebLogic など）内で動作し、HTTP リクエスト/レスポンスを処理する Java クラスです。コンテナは以下を管理します：

* ライフサイクル（ロード、init、service、destroy）
* マルチスレッドとリクエストルーティング
* セッション、セキュリティ、リソース、設定

# 2) コアパッケージと主要インターフェース (javax.\*)

* `javax.servlet.Servlet`, `ServletConfig`, `ServletContext`
* `javax.servlet.http.HttpServlet`, `HttpServletRequest`, `HttpServletResponse`, `HttpSession`, `Cookie`
* `javax.servlet.Filter`, `FilterChain`, `FilterConfig`
* `javax.servlet.ServletRequestListener` およびその他のリスナー
* `javax.servlet.annotation.*` (3.0 以降: `@WebServlet`, `@WebFilter`, `@WebListener`, `@MultipartConfig`)
* 3.0 以降: **非同期** (`AsyncContext`)、プログラムによる登録
* 3.1 以降: **ノンブロッキング I/O** (`ServletInputStream`/`ServletOutputStream` と `ReadListener`/`WriteListener`)
* 4.0 以降: HTTP/2 サポート（例: `PushBuilder`）

> Jakarta への切り替え: **Servlet 5.0**（Jakarta EE 9）以降、パッケージ名は `jakarta.servlet.*` に変更されました。ほとんどの API は同じです。移行時はインポートと依存関係を更新してください。

# 3) Servlet のライフサイクルとスレッドモデル

* **Load**: コンテナがクラスをロードし、宣言ごとに単一のインスタンスを作成します。
* **`init(ServletConfig)`**: 一度呼び出されます。初期化パラメータを読み取り、負荷の高いリソースをキャッシュします。
* **`service(req, res)`**: リクエストごとに呼び出されます。`HttpServlet` は `doGet`、`doPost` などに振り分けます。
* **`destroy()`**: シャットダウンまたは再デプロイ時に一度呼び出されます。

**スレッド**: コンテナは同じインスタンスに対して `service` を並行して呼び出します。
**ルール**: 可変のインスタンスフィールドは避けてください。必要な場合は、スレッドセーフな構造または適切な同期を使用してください。ローカル変数を優先します。

# 4) 最小限の Servlet（アノテーション）

```java
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import javax.servlet.ServletException;
import java.io.IOException;

@WebServlet(name = "HelloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {
    resp.setContentType("text/plain;charset=UTF-8");
    resp.getWriter().println("Hello, Servlet!");
  }
}
```

# 5) `web.xml` とアノテーション

**アノテーション (3.0+)** は、シンプルなアプリケーションに最も簡単です。
**`web.xml`** は、順序の指定、オーバーライド、またはレガシーコンテナの場合にまだ有用です。

最小限の `web.xml`:

```xml
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
  <servlet>
    <servlet-name>HelloServlet</servlet-name>
    <servlet-class>com.example.HelloServlet</servlet-class>
    <init-param>
      <param-name>greeting</param-name>
      <param-value>Hi</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>
</web-app>
```

# 6) HTTP リクエスト/レスポンスの基本

## リクエストデータの読み取り

```java
String q = req.getParameter("q");        // クエリ/フォームフィールド
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // 生のボディテキスト
ServletInputStream in = req.getInputStream(); // バイナリボディ
String header = req.getHeader("X-Token");
```

**ヒント**: パラメータを読み取る前に常にエンコーディングを設定してください：

```java
req.setCharacterEncoding("UTF-8");
```

## レスポンスの書き込み

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet と doPost とその他

* `doGet`: べき等な読み取り。クエリ文字列を使用します。
* `doPost`: フォームまたは JSON ボディを使用した作成/更新。
* `doPut`/`doDelete`/`doPatch`: RESTful セマンティクス（クライアントがサポートする必要があります）。
* 常に入力を検証し、コンテンツタイプを明示的に処理してください。

# 8) セッションと Cookie

```java
HttpSession session = req.getSession(); // 存在しない場合は作成
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // ログアウト
```

セッション Cookie フラグは、コンテナまたはプログラムで設定します：

* `HttpOnly`（JS からの保護）、`Secure`（HTTPS）、`SameSite=Lax/Strict`
  水平スケーリングの場合はステートレストークンを検討してください。それ以外の場合は、スティッキーセッションまたは外部セッションストアを使用します。

# 9) フィルター（横断的関心事）

**フィルター**をロギング、認証、CORS、圧縮、エンコーディングなどに使用します。

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(urlPatterns = "/*")
public class LoggingFilter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    long start = System.nanoTime();
    try {
      chain.doFilter(req, res);
    } finally {
      long ms = (System.nanoTime() - start) / 1_000_000;
      req.getServletContext().log("Handled in " + ms + " ms");
    }
  }
}
```

# 10) リスナー（アプリとリクエストのフック）

一般的なもの：

* `ServletContextListener`: アプリの起動/シャットダウン（プールの初期化、キャッシュのウォームアップ）
* `HttpSessionListener`: セッションの作成/破棄（メトリクス、クリーンアップ）
* `ServletRequestListener`: リクエストごとのフック（トレース ID）

例：

```java
@WebListener
public class AppBoot implements javax.servlet.ServletContextListener {
  public void contextInitialized(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App starting...");
  }
  public void contextDestroyed(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App stopping...");
  }
}
```

# 11) 非同期とノンブロッキング I/O

## 非同期 (Servlet 3.0)

バックエンド呼び出しの実行中にコンテナスレッドを解放できます。

```java
@WebServlet(urlPatterns="/async", asyncSupported=true)
public class AsyncDemo extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    AsyncContext ctx = req.startAsync();
    ctx.start(() -> {
      try {
        // 遅いサービスを呼び出す...
        ctx.getResponse().getWriter().println("done");
      } catch (Exception e) {
        ctx.complete();
      } finally {
        ctx.complete();
      }
    });
  }
}
```

## ノンブロッキング (Servlet 3.1)

ストリームに `ReadListener`/`WriteListener` を登録して、イベント駆動型の I/O を実現します。スレッドをブロックせずに大きなボディをストリーミングする場合に有用です。

# 12) ファイルアップロード (Multipart)

```java
import javax.servlet.annotation.MultipartConfig;

@MultipartConfig(maxFileSize = 10 * 1024 * 1024)
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    Part file = req.getPart("file");
    String filename = file.getSubmittedFileName();
    try (InputStream is = file.getInputStream()) {
      // 保存...
    }
    resp.getWriter().println("Uploaded " + filename);
  }
}
```

クライアントが `Content-Type: multipart/form-data` を送信することを確認してください。

# 13) ディスパッチとテンプレート

* **Forward**: サーバーサイドの内部ディスパッチ。元の URL が維持されます。

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **Include**: 別のリソースの出力を含めます。

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **Redirect**: クライアントを 302/303/307 で新しい URL にリダイレクトします。

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) 文字エンコーディングと国際化 (i18n)

小さな**エンコーディングフィルター**で文字化けを防ぎます：

```java
@WebFilter("/*")
public class Utf8Filter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    req.setCharacterEncoding("UTF-8");
    res.setCharacterEncoding("UTF-8");
    chain.doFilter(req, res);
  }
}
```

`HttpServletRequest#getLocale()` から取得した `Locale` とリソースバンドルを i18n に使用します。

# 15) セキュリティの基本

* **トランスポート**: 常に HTTPS を使用します。`Secure` Cookie を設定します。
* **認証**: コンテナ管理（FORM/BASIC/DIGEST）、または JWT/セッションを使用したカスタムフィルター。
* **CSRF**: セッションごとのトークンを生成します。状態変更リクエストで検証します。
* **XSS**: 出力を HTML エスケープします。`Content-Security-Policy` を設定します。
* **クリックジャッキング**: `X-Frame-Options: DENY` または CSP の `frame-ancestors 'none'`。
* **CORS**: フィルターでヘッダーを追加します：

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) エラーハンドリング

* `web.xml` またはフレームワーク経由でエラーページをマッピングします：

```xml
<error-page>
  <error-code>404</error-code>
  <location>/WEB-INF/errors/404.jsp</location>
</error-page>
<error-page>
  <exception-type>java.lang.Throwable</exception-type>
  <location>/WEB-INF/errors/500.jsp</location>
</error-page>
```

* コードでは、ステータスコードを設定し、API の場合は一貫した JSON エラースキーマをレンダリングします。

# 17) ロギングとオブザーバビリティ

* `ServletContext#log` を使用するか、より良い方法として SLF4J + Logback/Log4j2 を使用します。
* フィルターでリクエスト ID（UUID）を追加します。ログとレスポンスヘッダーに含めます。
* ヘルスエンドポイントを公開します。フィルター/サーブレット経由で Prometheus と統合します。

# 18) パッケージングとデプロイ

**WAR レイアウト**:

```
myapp/
  WEB-INF/
    web.xml
    classes/            # コンパイルされた .class ファイル
    lib/                # サードパーティの jar
  index.html
  static/...
```

Maven/Gradle でビルドし、**WAR** を生成して、コンテナの `webapps`（Tomcat）または管理コンソール経由でデプロイします。組み込みスタイルの場合は、**Jetty** または **Tomcat embedded** を `main()` でサーバーをブートストラップして使用します。

# 19) Servlet のテスト

* **単体テスト**: `HttpServletRequest/Response` をモックします。

  * Spring を使用していなくても、Spring の `org.springframework.mock.web.*` が便利です。
  * または Mockito で独自のスタブを作成します。
* **統合テスト**: 組み込みの Jetty/Tomcat を起動し、HTTP クライアント（REST Assured/HttpClient）でエンドポイントにリクエストを送信します。
* **エンドツーエンドテスト**: ブラウザ自動化（Selenium/WebDriver）で完全なフローをテストします。

# 20) パフォーマンスのヒント

* 高コストなリソース（`DataSource` 経由の DB プール）を再利用します。`destroy()` でクリーンアップします。
* 静的コンテンツにキャッシュヘッダーを設定します。静的アセットはリバースプロキシ/CDN にオフロードします。
* GZIP 圧縮を使用します（コンテナ設定またはフィルター）。
* 長時間の操作にはブロッキング I/O を避けます。非同期またはキューイングを検討します。
* 割り当てと GC をプロファイリングします。大きなペイロードにはストリーミングレスポンスを維持します。

# 21) 一般的な落とし穴

* **インスタンスフィールド**がスレッドセーフでない → 競合状態。
* パラメータを読み取る前に `req.setCharacterEncoding("UTF-8")` を忘れる。
* バッファリングせずにボディを 2 回読み取る。
* 例外を飲み込んで `5xx` ステータスを設定しない。
* 同じレスポンスで `getWriter()` と `getOutputStream()` を混在させる。

# 22) `javax.servlet.*` から `jakarta.servlet.*` へ

Jakarta EE 9+ にアップグレードする場合：

* インポートを `javax.servlet.*` → `jakarta.servlet.*` に変更します。
* Jakarta をサポートするコンテナ（Tomcat 10+、Jetty 11+）を使用します。
* リビルドします。ほとんどのコード変更はインポートの名前変更です。
* ライブラリも Jakarta 互換である必要があります（推移的依存関係に注意）。

# 23) 最小限の REST スタイルの例

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // 例: /api/users/42
    if (id == null) {
      resp.getWriter().write("[{\"id\":1,\"name\":\"A\"}]");
    } else {
      resp.getWriter().write("{\"id\":"+id+",\"name\":\"A\"}");
    }
  }
  private String pathParam(HttpServletRequest req, int idx) {
    String path = req.getPathInfo();        // "/42"
    if (path == null) return null;
    String[] parts = path.split("/");
    return parts.length > idx ? parts[idx] : null;
  }
}
```

# 24) ビルド依存関係（従来の `javax.servlet`）

**Provided** スコープを Maven で使用します。コンテナが実行時に API を提供するためです：

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

**Jakarta** の場合：

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

---

対象のコンテナ（Tomcat/Jetty/Liberty）、Java バージョン、および同期、非同期、ノンブロッキング I/O のいずれを希望するかをお知らせいただければ、ロギング、CORS、セキュリティヘッダー、クリーンな Maven/Gradle レイアウトを備えた、あなたのスタックに合わせた本番環境対応のスケルトンを（表なしで、厳選されたコードと手順で）作成できます。