---
audio: false
generated: true
image: false
lang: ja
layout: post
title: WARとEARパッケージングガイド
translated: true
type: note
---

以下は、Mavenの**WAR**と**EAR**パッケージングの実践的な比較と、実際のプロジェクトでの使用方法についての表を使わない説明です。

# 各パッケージングの目的

* **WAR (`packaging: war`)** – 単一のWebアプリケーション: サーブレット/Jakarta REST、JSP/JSF、Spring MVC/Boot (WARとして) など。サーブレットコンテナ (Tomcat/Jetty) またはフルアプリケーションサーバーのWeb層にデプロイされます。
* **EAR (`packaging: ear`)** – フルJava EE/Jakarta EEアプリケーションサーバー (WildFly/JBoss EAP、WebLogic、WebSphere) にまとめてデプロイするための、複数モジュールのバンドル。通常、1つ以上のWAR、EJB JAR、および共有ライブラリが含まれ、1つのデプロイメント単位を構成します。

# 典型的な選択基準

* **WAR** を選択する場合: 単一のWebアプリケーションまたはSpring Bootアプリケーションであり、EJBやマルチモジュールのサーバー機能が必要ないとき。
* **EAR** を選択する場合: 複数のモジュール (例: EJB + 複数のWAR + 共有ライブラリ) を一緒にデプロイする必要がある場合、モジュール間でアプリケーションサーバーサービス (XA、集中化されたセキュリティレルム、JMS、分散トランザクション) が必要な場合、または組織でEARの使用が義務付けられている場合。

# アーティファクトの内容

* **WAR** の内容: `/WEB-INF/classes`, `/WEB-INF/lib`, オプションの `web.xml` (またはアノテーション)、静的アセット。ほとんどのサーバーではWARごとに1つのクラスローダーが使用されます。
* **EAR** の内容: `*.war`, `*.jar` (EJB/ユーティリティ), `META-INF/application.xml` (またはアノテーション/スキニー構成)、およびモジュール間で共有されるライブラリ用のオプションの `lib/`。すべてのモジュールから参照可能なEARレベルのクラスローダーを提供します。

# 依存関係とクラスローディングの考慮事項

* **WAR**: サーブレット/Jakarta EE API は `provided` として宣言します。その他すべては `/WEB-INF/lib` に配置されます。分離がシンプルで、バージョン競合が少なくなります。
* **EAR**: 共通ライブラリはEARの `lib/` に配置します (`maven-ear-plugin` 経由)。これにより、すべてのモジュールが1つのバージョンを共有します。モジュールのライブラリとサーバー提供のAPI間の競合に注意し、バージョンを合わせ、必要に応じて `provided` を使用してください。

# 使用するMavenプラグイン

* **WAR プロジェクト**: `maven-war-plugin`
* **EAR アグリゲーター**: `maven-ear-plugin`
* **EJB モジュール (もしあれば)**: `maven-ejb-plugin`
* 親/アグリゲーターは、モジュールをまとめるために `packaging: pom` を使用することが多いです。

# 最小限の例

単一のWebアプリケーション (WAR):

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- サーバーAPIには provided を使用 -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- あなたのアプリの依存関係 -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- オプション: webResources, warName, filtering の設定 -->
      </plugin>
    </plugins>
  </build>
</project>
```

WARとEJBを含むマルチモジュールEAR:

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- @EJBインジェクションを可能にする -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- すべてのモジュールで共有される EAR/lib に配置するライブラリ -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- オプション: application.xml を生成、またはカスタムのものを提供 -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

ビルド結果:

* `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
* `mvn -pl ear-assembly -am clean package` → WAR、EJB、および `lib/` を含む `ear-assembly-1.0.0.ear`

# 重要な運用上の違い

* **デプロイメントターゲット**

  * WAR: サーブレットコンテナまたはアプリケーションサーバーのWeb層。
  * EAR: フルアプリケーションサーバー。すべてのモジュールをアトミックにデプロイします。
* **トランザクションとメッセージング**

  * WAR単体では、コンテナが公開する機能を使用します。複雑なXA/JMS設定は、多くの場合EAR内のEJBに存在します。
* **バージョニングとロールアウト**

  * WAR: 単一のアプリをリビルドして再デプロイするのが簡単です。
  * EAR: 多くのモジュールのバージョンを調整します。一貫性のために1つのデプロイメント単位です。
* **起動時間とローカル開発**

  * WAR: フィードバックが速く、ランタイムが軽量です。
  * EAR: 重い。IDE/サーバー統合は役立ちますが、サイクルは遅くなります。
* **モダンなSpring Bootに関する注意**

  * Bootは実行可能な**JAR**を推奨します。外部コンテナにデプロイする場合はWARがサポートされています。
  * Bootは**EAR**をターゲットにしていません。アプリケーションサーバーを使用する必要がある場合は、BootをWARとしてデプロイし、プラットフォームが要求しない限りEARは避けてください。

# 一般的な落とし穴とヒント

* サーバーAPIには `provided` を使用して、それらをバンドルしないようにします。
* EARの場合、各WAR/EJB内での重複コピーを防ぐために、共有ライブラリを `defaultLibBundleDir` に配置します。
* モジュール間でJakarta EEのバージョンを合わせます。不一致はクラスローディングエラーの原因となります。
* WebLogic/WebSphereでは、クラスローダーポリシー (parent-first vs parent-last) に注意してください。ベンダー固有の記述子が必要な場合があります。
* EJB/XAが必要ない場合は、プレーンなWAR (またはBoot JAR) の方がシンプルで、通常は移植性が高くなります。

使用するアプリケーションサーバー (Tomcat vs WildFly/WebLogic/など) と、EJBまたは複数のWebアプリケーションがあるかどうかを教えていただければ、必要な正確なPOMとデプロイメント記述子のスケッチをお伝えできます。