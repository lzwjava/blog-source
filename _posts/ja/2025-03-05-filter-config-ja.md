---
audio: false
generated: true
lang: ja
layout: post
title: Javaサーブレットにおけるフィルタ設定
translated: true
type: note
---

### `javax.servlet.FilterConfig` の仕組み

Java の Servlet API を使用して構築された Web アプリケーションにおいて、`javax.servlet.FilterConfig` インターフェースはフィルタを設定する上で重要な役割を果たします。フィルタは、HTTP リクエストとレスポンスがサーブレットに到達する前、またはサーブレットから離れた後に、それらをインターセプトして処理するコンポーネントです。`FilterConfig` は、Web コンテナ (Tomcat、Jetty など) によってフィルタが初期化される際に、設定情報をフィルタに渡す標準化された方法を提供します。以下では、`FilterConfig` の仕組み、目的、使用方法について説明します。

---

#### **`FilterConfig` とは何か？**
`FilterConfig` は `javax.servlet` パッケージ内のインターフェースです。Web コンテナが、フィルタの初期化段階でフィルタに設定データを提供するために使用します。Web アプリケーションでフィルタが定義されると (`web.xml` またはアノテーション経由で)、コンテナはフィルタのインスタンスを作成し、その `init` メソッドに `FilterConfig` オブジェクトを渡します。このオブジェクトにより、フィルタは以下にアクセスできるようになります：
- 自身の初期化パラメータ
- Web アプリケーションの `ServletContext`
- 設定で定義された自身の名前

フィルタは `javax.servlet.Filter` インターフェースを実装します。このインターフェースには `init`、`doFilter`、`destroy` の 3 つのメソッドが含まれます。`FilterConfig` オブジェクトは、フィルタがリクエスト処理を開始する前にフィルタをセットアップするために、特に `init` メソッドで使用されます。

---

#### **フィルタと `FilterConfig` のライフサイクル**
`FilterConfig` の仕組みを理解するために、フィルタのライフサイクルにおけるその役割を見てみましょう：
1. **コンテナの起動**: Web アプリケーションが起動すると、コンテナはフィルタ定義 (`web.xml` または `@WebFilter` アノテーションから) を読み取り、各フィルタのインスタンスを作成します。
2. **フィルタの初期化**: 各フィルタに対して、コンテナは `init` メソッドを呼び出し、パラメータとして `FilterConfig` オブジェクトを渡します。これはフィルタインスタンスごとに 1 回だけ実行される操作です。
3. **リクエスト処理**: 初期化後、フィルタの `doFilter` メソッドが一致する各リクエストに対して呼び出されます。`FilterConfig` は `doFilter` に渡されませんが、フィルタは `init` 中に `FilterConfig` から取得した設定データをインスタンス変数に保存し、後で使用できます。
4. **フィルタのシャットダウン**: アプリケーションのシャットダウン時には `destroy` メソッドが呼び出されますが、ここでは `FilterConfig` は関与しません。

`FilterConfig` オブジェクトは、初期化段階において、フィルタがリクエスト処理に備えて自身を準備することを可能にするため、非常に重要です。

---

#### **`FilterConfig` の主なメソッド**
`FilterConfig` インターフェースは、設定情報へのアクセスを提供する 4 つのメソッドを定義しています：

1. **`String getFilterName()`**
   - `web.xml` ファイル ( `<filter-name>` タグ内) または `@WebFilter` アノテーションで指定されたフィルタの名前を返します。
   - ロギング、デバッグ、またはフィルタチェーン内でのフィルタの識別に役立ちます。

2. **`ServletContext getServletContext()`**
   -  Web アプリケーション全体を表す `ServletContext` オブジェクトを返します。
   - `ServletContext` により、フィルタはコンテキスト属性、ロギング機能、リクエストを転送するための `RequestDispatcher` など、アプリケーション全体のリソースにアクセスできます。

3. **`String getInitParameter(String name)`**
   - 特定の名前を持つ初期化パラメータの値を取得します。
   - 初期化パラメータは、`web.xml` ( `<init-param>` タグ内) または `@WebFilter` アノテーションの `initParams` 属性でフィルタに対して定義されたキーと値のペアです。
   - パラメータが存在しない場合は `null` を返します。

4. **`Enumeration<String> getInitParameterNames()`**
   - フィルタに対して定義されたすべての初期化パラメータ名の `Enumeration` を返します。
   - これにより、フィルタはすべてのパラメータを反復処理し、`getInitParameter` を使用してそれらの値を取得できます。

これらのメソッドは、Web コンテナ (Tomcat の内部的な `FilterConfigImpl` など) によって提供される具象クラスによって実装されます。開発者は、このインターフェースを通じてのみ `FilterConfig` と対話します。

---

#### **`FilterConfig` の設定方法**
フィルタとその設定は、以下の 2 つの方法で定義できます：
1. **`web.xml` (デプロイメント記述子) を使用**:
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
   - `<filter-name>` はフィルタの名前を定義します。
   - `<init-param>` はキーと値のペアとして初期化パラメータを指定します。

2. **アノテーションを使用 (Servlet 3.0 以降)**:
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
   - `@WebFilter` アノテーションは、フィルタの名前、URL パターン、および初期化パラメータを定義します。

どちらの場合も、コンテナはこの設定を使用して `FilterConfig` オブジェクトを作成し、それをフィルタの `init` メソッドに渡します。

---

#### **実践的な例**
以下は、フィルタが実際に `FilterConfig` をどのように使用するかの例です：

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // 設定データを保存するためのインスタンス変数

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // フィルタの名前を取得
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // 初期化パラメータを取得
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // 必要に応じて後で使用するために ServletContext を保存
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // excludeURLs を使用してリクエストをフィルタリングするかどうかを決定
        chain.doFilter(request, response); // 次のフィルタまたはサーブレットに進む
    }

    @Override
    public void destroy() {
        // クリーンアップコード
    }
}
```

- **`init` 内**: フィルタは自身の名前、初期化パラメータ (`excludeURLs`)、および `ServletContext` を取得します。`excludeURLs` をインスタンス変数に保存し、`doFilter` で使用できるようにします。
- **`doFilter` 内**: フィルタは保存された設定 (例: `excludeURLs`) を使用してリクエストを処理できます。

---

#### **`FilterConfig` に関する重要なポイント**
- **フィルタ固有のスコープ**: `FilterConfig` 内の初期化パラメータは、フィルタインスタンスに固有です。異なるフィルタが同じ名前で異なる値を持つパラメータを持つことができます。
- **`ServletContext` との対比**: `ServletContext` (`getServletContext()` 経由でアクセス) は、アプリケーション全体の初期化パラメータとリソースを提供します。これは `FilterConfig` 内のフィルタ固有のパラメータとは異なります。
- **ライフサイクル内での単回使用**: `FilterConfig` は `init` にのみ渡されます。フィルタが後でそのデータを必要とする場合 (例: `doFilter` 内)、データをインスタンス変数に保存する必要があります。
- **コンテナ提供**: `FilterConfig` はインターフェースであり、Web コンテナが具象実装を提供します。

---

#### **まとめ**
`javax.servlet.FilterConfig` は、フィルタの初期化中に設定情報をフィルタに提供することで機能します。Web コンテナは `FilterConfig` オブジェクトをフィルタの `init` メソッドに渡し、フィルタが以下を行うことを可能にします：
- 自身の名前 (`getFilterName`) にアクセスする。
- 初期化パラメータ (`getInitParameter`, `getInitParameterNames`) を取得する。
- `ServletContext` (`getServletContext`) を介して Web アプリケーションと対話する。

これにより、フィルタは `web.xml` またはアノテーションを介して柔軟に設定され、HTTP リクエストとレスポンスを効果的に処理する準備が整います。特定の URL を除外する、タイムアウトを設定する、メッセージをログに記録する、といった場合を問わず、`FilterConfig` はフィルタの設定とその実行時の動作との間の橋渡し役となります。