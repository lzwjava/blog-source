---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: JSP入門
translated: true
type: note
---

JavaServer Pages (JSP) は、Java アプリケーションで動的な Web コンテンツを作成するためのサーバーサイド技術です。HTML ページに直接 Java コードを埋め込むことを可能にし、ユーザー入力やデータに基づいて動的なレスポンスを生成することを容易にします。JSP は Jakarta EE (旧称 Java EE) プラットフォームの一部であり、Web アプリケーションにおけるサーブレットと連携して動作します。

以下は、セットアップからデプロイまでの JSP 入門のステップバイステップガイドです。これは Java と HTML の基本的な知識を前提としています。

## 1. 前提条件
- **Java Development Kit (JDK)**: JDK 8 以降をインストール (モダンなアプリでは JDK 17+ を推奨)。[Oracle](https://www.oracle.com/java/technologies/downloads/) からダウンロードするか、OpenJDK を使用します。
- **Web サーバー/コンテナ**: Apache Tomcat (初心者向けで無料) を使用します。[Apache Tomcat](https://tomcat.apache.org/) からダウンロードします。
- **IDE (任意ですが推奨)**: IntelliJ IDEA, Eclipse, または Java 拡張機能が入った VS Code を開発効率向上のために使用します。

## 2. 環境のセットアップ
1. Tomcat のインストール:
   - Tomcat アーカイブをディレクトリ (例: Windows では `C:\tomcat`、Linux では `/opt/tomcat`) に展開します。
   - `bin/startup.bat` (Windows) または `bin/startup.sh` (Unix) を実行して Tomcat を起動します。ブラウザで `http://localhost:8080` にアクセスし、動作を確認します。

2. プロジェクト構造の作成:
   - Tomcat の `webapps` フォルダ内に、アプリ用の新しいディレクトリ (例: `my-jsp-app`) を作成します。
   - その中に以下を作成します:
     - `WEB-INF/web.xml` (デプロイメント記述子。JSP 2.2+ では任意ですが設定に便利です)。
     - JSP ファイル用のルートフォルダ (例: `index.jsp`)。

   基本的な `web.xml` の例:
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

## 3. 最初の JSP ページを書く
JSP ファイルは `.jsp` 拡張子を持ち、スクリプトレット (`<% %>`)、式 (`<%= %>`)、宣言 (`<%! %>`) を使用して HTML と Java コードを組み合わせます。モダンなベストプラクティスとしては、生のスクリプトレットを避けるために、JSP 式言語 (EL) と JSTL (JavaServer Pages Standard Tag Library) を使用します。

例: アプリのルートに `index.jsp` を作成:
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>  <!-- JSTL 使用時 -->

<html>
<head>
    <title>Hello JSP</title>
</head>
<body>
    <h1>Welcome to JSP!</h1>
    
    <!-- スクリプトレット: Java コード -->
    <% 
        String name = request.getParameter("name") != null ? request.getParameter("name") : "World";
        java.util.Date now = new java.util.Date();
    %>
    
    <!-- 式: 値を出力 -->
    <p>Hello, <%= name %>! The time is <%= now %>.</p>
    
    <!-- よりクリーンな出力のための EL (Expression Language) の使用 -->
    <p>Your name via EL: ${param.name}</p>
    
    <!-- JSTL の例: リストをループ処理 -->
    <c:set var="fruits" value="${{'Apple', 'Banana', 'Cherry'}}" />
    <ul>
        <c:forEach var="fruit" items="${fruits}">
            <li>${fruit}</li>
        </c:forEach>
    </ul>
</body>
</html>
```

- **主な要素**:
  - **ディレクティブ**: `<%@ page ... %>` はページプロパティを設定; `<%@ taglib ... %>` はタグライブラリをインポート。
  - **スクリプトレット**: Java コードを埋め込む (控えめに使用し、EL/JSTL を優先)。
  - **EL**: `${expression}` でスクリプトレットなしでデータにアクセス。
  - **JSTL**: [Apache Taglibs](https://tomcat.apache.org/taglibs/standard/) からダウンロードし、JAR ファイルを `WEB-INF/lib` に配置。

## 4. デプロイと実行
1. アプリフォルダ (例: `my-jsp-app`) を Tomcat の `webapps` ディレクトリに配置します。
2. Tomcat を再起動します。
3. ブラウザでアクセス: `http://localhost:8080/my-jsp-app/index.jsp`。
4. クエリパラメータでテスト: `http://localhost:8080/my-jsp-app/index.jsp?name=Grok` にアクセスして動的な出力を確認します。

## 5. 一般的な機能とベストプラクティス
- **フォームとユーザー入力**: `<form>` タグと `request.getParameter()`、または EL (`${param.field}`) を使用して送信を処理します。
- **セッションと Bean**: 状態管理に `session.setAttribute()` を使用; 再利用可能なデータには JavaBeans を使用します。
- **エラーハンドリング**: `web.xml` に `<error-page>` を追加するか、`<%@ page errorPage="error.jsp" %>` を使用します。
- **セキュリティ**: XSS を防ぐため入力をサニタイズ; 本番環境では HTTPS を使用します。
- **モダンな代替技術**: JSP はまだ使用されていますが、より柔軟な Thymeleaf や Spring MVC を新規プロジェクトで検討してください。
- **デバッグ**: エラーについては Tomcat ログ (`logs/catalina.out`) を確認します。

## 6. 高度なトピック
- サーブレットとの統合: ビューに JSP、ロジックにサーブレット (MVC パターン) を使用。
- データベース接続: JDBC または JPA (例: H2 や MySQL と共に) を使用。
- ビルドツール: JSTL などの依存関係管理に Maven/Gradle を使用。

実践的な学習には、シンプルな "Hello World" から始め、徐々に機能を追加していきます。本格的な Web アプリを構築する場合は、Jakarta EE チュートリアルを探求してください。

## 参考資料
- [Oracle JSP Tutorial](https://docs.oracle.com/javaee/7/tutorial/jspx.htm)
- [Baeldung: Introduction to JSP](https://www.baeldung.com/jsp-tutorial)
- [Apache Tomcat JSP Examples](https://tomcat.apache.org/tomcat-10.1-doc/jsp-examples/)