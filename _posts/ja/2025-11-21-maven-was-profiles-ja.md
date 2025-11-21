---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4.1-fast
title: WAS環境設定のためのMavenプロファイル
translated: true
type: note
---

IBM WebSphere Application Server（従来のWAS、Libertyではない）の場合、標準的なパッケージングは**EAR**ファイルです（単純なWebアプリであっても、WASはスタンドアロンのWARよりもEARを優先します）。ローカル開発（テスト用の固定/ハードコードされたログインユーザー）とサーバー/本番環境（SSOまたは適切なセキュリティレルム）のような異なる環境を扱うためのベストプラクティスは、単一の`pom.xml`で**Mavenビルドプロファイル**を使用することです。これにより、複数の別個のPOMファイル（例：`pom.xml`と`build_pom.xml`）をメンテナンスする必要がなくなり、エラーが発生しにくく、Mavenの慣用的な使い方に沿ったものになります。

### 複数のPOMではなくプロファイルを使用する理由
- 単一の情報源（単一のPOM）
- 簡単なアクティベーション：`mvn package -Plocal` または `mvn package -Pserver`
- プロファイルは、リソースのフィルタリング、ファイルのオーバーライド、プラグイン設定の変更、バインディングの調整（例：WAS固有の認証のための`ibm-web-bnd.xml`、`ibm-application-ext.xml`）が可能
- 認証設定を含む、開発/テスト/本番環境の差異に対して一般的に使用される

### 推奨される構造
Maven Resources Pluginとフィルタリング＋プロファイル固有のリソースディレクトリを使用して、設定ファイル（例：`web.xml`、`properties`ファイル、Springセキュリティ設定、またはWASバインディング）を切り替えます。

ディレクトリレイアウトの例：
```
src/
├── main/
│   ├── resources/          (共通設定)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (共通または基本バージョン)
│   │   │   └── ibm-web-bnd.xml (オプション、JNDI/認証バインディング用)
│   └── ...
├── local/                   (プロファイル固有のリソース、ローカル用にのみコピー/フィルタリング)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (フォームログイン＋ハードコードされたユーザー/ロール、またはセキュリティなしのローカルバージョン)
│           └── ...
└── server/                  (本番/SSO用のプロファイル固有)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (SSOのための<auth-method>CLIENT-CERT</auth-method>またはSPNEGOを含むサーバーバージョン)
            └── ...
```

### pom.xml スニペットの例
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- またはWARとしてデプロイする場合はwar、ただしWASではEARが推奨 -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- または使用するJavaのバージョン -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- アプリの依存関係 -->
        <!-- WASコンパイル時API用（providedスコープ） -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- 使用するWASのバージョンに合わせて調整（例：8.5.5 または 9.0） -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- EARのビルド（必要に応じてWAR用に調整） -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- EARの設定、モジュールなど -->
                </configuration>
            </plugin>

            <!-- リソースフィルタリング & プロファイル固有のオーバーライド -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- プロファイル -->
    <profiles>
        <!-- ローカル/開発プロファイル：固定ユーザー、フォームログインまたはセキュリティなし -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- ローカルビルドのデフォルト -->
            </activation>
            <build>
                <resources>
                    <!-- 共通リソース -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- ローカル固有のファイルでオーバーライド -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- ローカル用ハードコードユーザーのフィルタリングプロパティ例 -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- サーバー/本番プロファイル：実際のSSO（例：SPNEGO、LTPA、またはOpenIDConnect） -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- 本番用プロパティ、例：SSOフラグを有効化 -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### 認証の差異に関する重要なポイント
- **ローカル**: `web.xml`またはプロパティファイル内のシンプルなユーザー/ロールを使用したFORMログインを使用するか、セキュリティを完全に無効化する（`<security-constraint>`を削除）。
- **サーバー**: `web.xml`でWAS固有のSSOを設定する（例：SPNEGOを使用した`<auth-method>FORM</auth-method>`、またはLibertyスタイルのOpenID Connect機能を使用するが、従来のWASではしばしばLTPA + グローバルセキュリティレルム）。ユーザー/ロールマッピングのために、WASバインディング（`ibm-web-bnd.xml`）もプロファイルごとにオーバーライド可能。
- Spring Securityまたは類似のものを使用する場合、同じ方法で`applicationContext-security.xml`またはプロパティを切り替える。
- ハードコードされたローカルユーザーの場合：実際のハードコードされた認証情報は避け、ローカルの`users.properties`にマップされたテストユーザーを使用するか、フラグを介して認証チェックを無効にする。

### ビルドコマンド
- ローカル（デフォルト）: `mvn clean package`
- サーバー/本番: `mvn clean package -Pserver`

これにより、**同じコードベース**から各環境に合わせた異なるEARが生成されます。本当に別々のアーティファクト名（例：`myapp-local.ear` vs `myapp.ear`）が必要な場合は、プロファイル固有の`<build>`セクションに`<finalName>${project.artifactId}-${profile}</finalName>`を追加してください。

[Maven Profiles Guide](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[IBM WAS Maven Integration](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)