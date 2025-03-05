---
audio: true
generated: true
lang: ja
layout: post
title: サーブレットでのフィルタ設定
translated: true
---

### `javax.servlet.FilterConfig` の仕組み

JavaでServlet APIを使用して構築されたWebアプリケーションでは、`javax.servlet.FilterConfig`インターフェースはフィルタの設定に重要な役割を果たします。フィルタは、HTTPリクエストとレスポンスをサーブレットに到達する前にまたは離れる後にインターセプトして処理するコンポーネントです。`FilterConfig`は、Webコンテナ（例：Tomcat、Jetty）によってフィルタが初期化される際に設定情報をフィルタに渡す標準的な方法を提供します。以下に、`FilterConfig`の仕組み、目的、そしてその使用方法について説明します。

---

#### **`FilterConfig`とは？**
`FilterConfig`は、`javax.servlet`パッケージ内のインターフェースです。Webコンテナは、フィルタの初期化フェーズ中にフィルタに設定データを供給するために使用します。フィルタがWebアプリケーションで定義される場合（`web.xml`またはアノテーションを通じて）、コンテナはフィルタのインスタンスを作成し、`init`メソッドに`FilterConfig`オブジェクトを渡します。このオブジェクトにより、フィルタは以下をアクセスできます：
- 自身の初期化パラメータ。
- Webアプリケーションの`ServletContext`。
- 設定で定義された自身の名前。

フィルタは、`javax.servlet.Filter`インターフェースを実装し、`init`、`doFilter`、`destroy`の3つのメソッドを含みます。`FilterConfig`オブジェクトは特に`init`メソッドで使用され、フィルタがリクエストの処理を開始する前に設定されます。

---

#### **フィルタと`FilterConfig`のライフサイクル**
`FilterConfig`の仕組みを理解するために、フィルタのライフサイクルにおけるその役割をみてみましょう：
1. **コンテナの起動**：Webアプリケーションが起動すると、コンテナはフィルタの定義（`web.xml`または`@WebFilter`アノテーションから）を読み取り、各フィルタのインスタンスを作成します。
2. **フィルタの初期化**：各フィルタに対して、コンテナは`init`メソッドを呼び出し、`FilterConfig`オブジェクトをパラメータとして渡します。これはフィルタインスタンスごとに一度の操作です。
3. **リクエストの処理**：初期化後、`doFilter`メソッドが各一致するリクエストに対して呼び出されます。`FilterConfig`は`doFilter`に渡されませんが、フィルタは`init`中に`FilterConfig`からの設定データをインスタンス変数に保存して後で使用できます。
4. **フィルタのシャットダウン**：アプリケーションがシャットダウンすると、`destroy`メソッドが呼び出されますが、`FilterConfig`はここでは関与しません。

`FilterConfig`オブジェクトは初期化フェーズにおいて重要であり、フィルタがリクエストの処理に備えることを可能にします。

---

#### **`FilterConfig`の主要なメソッド**
`FilterConfig`インターフェースは、設定情報へのアクセスを提供する4つのメソッドを定義しています：

1. **`String getFilterName()`**
   - `web.xml`ファイル（`<filter-name>`の下）または`@WebFilter`アノテーションで指定されたフィルタの名前を返します。
   - ロギング、デバッグ、またはフィルタチェーン内のフィルタの識別に役立ちます。

2. **`ServletContext getServletContext()`**
   - `ServletContext`オブジェクトを返します。これはWebアプリケーション全体を表します。
   - `ServletContext`は、フィルタがアプリケーション全体のリソース（コンテキスト属性、ロギング施設、またはリクエストを転送するための`RequestDispatcher`など）にアクセスできるようにします。

3. **`String getInitParameter(String name)`**
   - 指定された名前の特定の初期化パラメータの値を取得します。
   - 初期化パラメータは、`web.xml`（`<init-param>`の下）または`@WebFilter`アノテーションの`initParams`属性でフィルタに対して定義されたキー値ペアです。
   - パラメータが存在しない場合は`null`を返します。

4. **`Enumeration<String> getInitParameterNames()`**
   - フィルタに対して定義されたすべての初期化パラメータ名の`Enumeration`を返します。
   - フィルタは、すべてのパラメータを反復処理し、`getInitParameter`を使用してその値を取得できます。

これらのメソッドは、Webコンテナ（例：Tomcatの内部`FilterConfigImpl`）によって提供される具体的なクラスによって実装されます。開発者は、このインターフェースを通じてのみ`FilterConfig`とやり取りします。

---

#### **`FilterConfig`の設定方法**
フィルタとその設定は、2つの方法で定義できます：
1. **`web.xml`（デプロイメント記述子）を使用する場合**：
   ```xml
   <filter>
       <filter-name>MyFilter</filter-name>
       <filter-class>com.example.MyFilter</filter-class>
       <init-param>
           <param-name>excludeURLs</param-name>
           <param-value>/login,/signup</param-value>
       </init-param>
   </filter>
   <filter-mapping>
       <filter-name>MyFilter</filter-name>
       <url-pattern>/*</url-pattern>
   </filter-mapping>
   ```
   - `<filter-name>`はフィルタの名前を定義します。
   - `<init-param>`は初期化パラメータをキー値ペアとして指定します。

2. **アノテーションを使用する場合（Servlet 3.0以降）**：
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // 実装
   }
   ```
   - `@WebFilter`アノテーションはフィルタの名前、URLパターン、初期化パラメータを定義します。

どちらの場合も、コンテナはこの設定を使用して`FilterConfig`オブジェクトを作成し、フィルタの`init`メソッドに渡します。

---

#### **実践的な例**
フィルタが`FilterConfig`を実際に使用する方法は以下の通りです：

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // 設定データを保存するためのインスタンス変数

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // フィルタの名前を取得
        String filterName = filterConfig.getFilterName();
        System.out.println("フィルタの初期化: " + filterName);

        // 初期化パラメータを取得
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("除外URL: " + excludeURLs);
        }

        // 後で使用するためにServletContextを保存（オプション）
        ServletContext context = filterConfig.getServletContext();
        context.log("フィルタ " + filterName + " 初期化済み");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // excludeURLsを使用してリクエストをフィルタリングするかどうかを決定
        chain.doFilter(request, response); // 次のフィルタまたはサーブレットに進む
    }

    @Override
    public void destroy() {
        // クリーンアップコード
    }
}
```

- **`init`**：フィルタは自分の名前、初期化パラメータ（`excludeURLs`）、`ServletContext`を取得し、`doFilter`で使用するために`excludeURLs`をインスタンス変数に保存します。
- **`doFilter`**：フィルタは保存された設定（例：`excludeURLs`）を使用してリクエストを処理できます。

---

#### **`FilterConfig`の重要なポイント**
- **フィルタ固有のスコープ**：`FilterConfig`の初期化パラメータはフィルタインスタンス固有です。異なるフィルタは同じ名前のパラメータを持つことができますが、異なる値を持つことができます。
- **`ServletContext`との対比**：`ServletContext`（`getServletContext()`を通じてアクセス）は、アプリケーション全体の初期化パラメータとリソースを提供し、`FilterConfig`のフィルタ固有のパラメータとは異なります。
- **ライフサイクルでの一回の使用**：`FilterConfig`は`init`にのみ渡されます。フィルタが後でデータを必要とする場合（例：`doFilter`）、インスタンス変数にデータを保存する必要があります。
- **コンテナ提供**：`FilterConfig`はインターフェースであり、Webコンテナが具体的な実装を提供します。

---

#### **まとめ**
`javax.servlet.FilterConfig`は、フィルタに初期化中に設定情報を提供することで動作します。Webコンテナはフィルタの`init`メソッドに`FilterConfig`オブジェクトを渡し、フィルタが以下を実行できるようにします：
- 名前を取得する（`getFilterName`）。
- 初期化パラメータを取得する（`getInitParameter`、`getInitParameterNames`）。
- `ServletContext`を通じてWebアプリケーションとやり取りする（`getServletContext`）。

これにより、フィルタは柔軟に設定できます（`web.xml`またはアノテーションを通じて）し、HTTPリクエストとレスポンスを効果的に処理する準備が整います。特定のURLを除外する、タイムアウトを設定する、メッセージをログに記録するなど、どのような操作を行う場合でも、`FilterConfig`はフィルタの設定とランタイム動作の間の橋渡し役を果たします。