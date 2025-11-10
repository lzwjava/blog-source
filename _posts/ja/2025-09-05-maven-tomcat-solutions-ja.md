---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Maven Tomcat プラグインの問題に対する解決策
translated: true
type: note
---

あなた自身のログに重要な手がかりがあります：

> `[INFO] Skipping non-war project`

何も起動しなかったのは、**tomcat7-maven-plugin は WAR としてパッケージされた Web アプリケーション**（クラシックな `src/main/webapp` レイアウト）のみを実行するためです。あなたのプロジェクトはほぼ確実に現在 JAR としてパッケージされているので、プラグインはビルド後に終了します。

さらに2つ目の落とし穴があります：あなたは **Tomcat 11** (Jakarta `jakarta.*` API を使用) を実行していますが、依存関係は **Spring 5.2.x** (`javax.*` を使用) です。この不一致は、たとえ Tomcat が起動したとしても、移行なしでは Tomcat 11 への単純なデプロイが失敗することを意味します。Spring 5 には Tomcat 9 (javax) を使用するか、Tomcat 10/11 用にアプリを Spring 6/Jakarta にアップグレードしてください。

以下に、クリーンな解決策を示します。どれか1つを選べば動作します：

### パス 1 — Spring 5 を維持し、Jetty プラグインでローカル実行（最速）

WAR は不要。開発に最適。

1. プラグインを追加：

   ```xml
   <plugin>
     <groupId>org.eclipse.jetty</groupId>
     <artifactId>jetty-maven-plugin</artifactId>
     <version>9.4.54.v20240208</version>
   </plugin>
   ```
2. 実行：

   ```bash
   mvn jetty:run -Djetty.port=8080
   ```

これは Spring 5 に一致する `javax.*` を使用します。

### パス 2 — Spring 5 を維持し、WAR をビルドして Tomcat7 プラグインを使用

1. `pom.xml` で WAR パッケージングを設定：

   ```xml
   <packaging>war</packaging>
   ```
2. Web アプリケーションレイアウトが存在することを確認：

   ```
   src/main/webapp/
   src/main/webapp/WEB-INF/web.xml   # Servlet 3 初期化子がある場合はオプション
   ```
3. （オプション）プラグイン設定を追加：

   ```xml
   <plugin>
     <groupId>org.apache.tomcat.maven</groupId>
     <artifactId>tomcat7-maven-plugin</artifactId>
     <version>2.2</version>
     <configuration>
       <path>/</path>
       <port>8080</port>
     </configuration>
   </plugin>
   ```
4. 実行：

   ```bash
   mvn tomcat7:run            # 展開された Web アプリ用
   # または
   mvn package && mvn tomcat7:run-war
   ```

### パス 3 — Spring 5 を維持し、スタンドアロンの Tomcat 9 にデプロイ

コードを変更せずに `javax.*` に一致します。

```bash
brew install tomcat@9
/opt/homebrew/opt/tomcat@9/bin/catalina start
```

WAR をビルドし、`.../tomcat@9/libexec/webapps/` に配置します。

### パス 4 — アプリを Spring 6/Jakarta にアップグレードし、Tomcat 11 を継続使用

モダンな Tomcat が必要な場合：

* Spring Framework 6.x / Spring Boot 3.x にアップグレード。
* インポートを `javax.*` から `jakarta.*` に変更。
* その後は Tomcat 10/11 が問題なく動作します。

---

#### `mvn tomcat7:run` が成功を表示したのに「何も起こらなかった」理由

* Maven フェーズは正常に完了しましたが、プラグインは **非 WAR パッケージング** を検出したため、組み込み Tomcat を**起動しませんでした**。これがまさに "Skipping non-war project" の意味です。

---

どのパスを希望するか教えていただければ、その設定に必要な正確な `pom.xml` と最小限のファイル（小さなコントローラと `http://localhost:8080/hello` でアクセスする方法を含む）をお伝えします。