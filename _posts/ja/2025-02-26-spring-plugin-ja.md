---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot Maven プラグイン
translated: true
type: note
---

MavenベースのSpring Bootプロジェクトで`spring-boot-maven-plugin`を使用するには、以下の手順に従ってプラグインを設定し、アプリケーションのビルド、実行、管理を行います。以下は包括的なガイドです：

---

### **1. プロジェクトがSpring Bootプロジェクトであることを確認する**
`spring-boot-maven-plugin`を使用する前に、プロジェクトがSpring Bootプロジェクトとして設定されていることを確認してください。これには通常、以下が含まれます：

- **`spring-boot-starter-parent`を継承する（推奨）**:
  - `pom.xml`で、Spring Bootの依存関係とプラグインバージョンを管理するために、親として`spring-boot-starter-parent`を設定します。
  - 例：
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- 使用するSpring Bootのバージョンに置き換えてください -->
        <relativePath/> <!-- リポジトリから親を検索 -->
    </parent>
    ```

- **代替案: `spring-boot-dependencies` BOM (Bill of Materials) を使用する**:
  - `spring-boot-starter-parent`を使用できない場合は、`dependencyManagement`セクションで`spring-boot-dependencies` BOMをインポートします。
  - 例：
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- 使用するSpring Bootのバージョンに置き換えてください -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

シンプルさのために`spring-boot-starter-parent`の使用が推奨されます。これはプラグインバージョンを自動的に管理します。

---

### **2. `spring-boot-maven-plugin`を`pom.xml`に追加する**
プラグインを使用するには、`pom.xml`の`<build><plugins>`セクションで宣言する必要があります。

- **`spring-boot-starter-parent`を使用している場合**:
  - バージョンは親によって管理されるため、バージョンを指定せずにプラグインを追加します。
  - 例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

- **`spring-boot-starter-parent`を使用していない場合**:
  - 使用しているSpring Bootのバージョンと一致するバージョンを明示的に指定します。
  - 例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- 使用するSpring Bootのバージョンに置き換えてください -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. プラグインのゴールを利用する**
`spring-boot-maven-plugin`は、Spring Bootアプリケーションのビルド、実行、管理を支援するいくつかのゴールを提供します。以下は最も一般的に使用されるゴールです：

- **`spring-boot:run`**
  - 組み込みWebサーバー（例：Tomcat）を使用して、Mavenから直接Spring Bootアプリケーションを実行します。
  - 開発とテストに有用です。
  - コマンド：
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - `mvn package`によって生成されたJARまたはWARファイルを、すべての依存関係を含む実行可能な「fat JAR」またはWARに再パッケージします。
  - このゴールは、プラグインが設定されている場合、`package`フェーズ中に自動的に実行されます。
  - コマンド：
    ```
    mvn package
    ```
  - 実行後、以下のコマンドでアプリケーションを起動できます：
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` と `spring-boot:stop`**
  - 統合テストで使用され、それぞれ`pre-integration-test`フェーズと`post-integration-test`フェーズ中にアプリケーションを起動および停止します。
  - 例：
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - ビルド情報（例：ビルド時刻、バージョン）を含む`build-info.properties`ファイルを生成します。
  - この情報は、Spring Bootの`BuildProperties` Beanまたは`@Value`アノテーションを使用してアプリケーション内でアクセスできます。
  - コマンド：
    ```
    mvn spring-boot:build-info
    ```

---

### **4. プラグイン設定のカスタマイズ（オプション）**
`pom.xml`に設定オプションを追加することで、`spring-boot-maven-plugin`の動作をカスタマイズできます。以下は一般的なカスタマイズの例です：

- **メインクラスの指定**:
  - プラグインがメインクラスを自動検出できない場合、手動で指定します。
  - 例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.example.MyApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **Fat JARからの依存関係の除外**:
  - 実行時環境（例：外部のサーブレットコンテナ）によって提供される依存関係を除外します。
  - 例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>com.example</groupId>
                            <artifactId>some-dependency</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **アプリケーション引数の設定**:
  - `spring-boot:run`で実行する際にアプリケーションに渡す引数を設定します。
  - `pom.xml`での例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <arguments>
                        <argument>--server.port=8081</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```
  - または、コマンドライン経由で引数を渡します：
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **WARファイルのビルド**:
  - 外部のサーブレットコンテナにデプロイするためのWARファイルをビルドする場合、`pom.xml`でプロジェクトのパッケージングが`war`に設定されていることを確認してください：
    ```xml
    <packaging>war</packaging>
    ```
  - 環境によって提供される組み込みサーブレットコンテナ（例：Tomcat）を除外する必要がある場合があります。以下の依存関係を`provided`として追加します：
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
        </dependency>
    </dependencies>
    ```

---

### **5. 主な注意点**
- **デフォルトの動作**:
  - `mvn package`を実行すると、プラグインは`package`フェーズ中にJAR/WARを自動的に再パッケージして実行可能にします。
  - 再パッケージされた成果物がメインの成果物となり、元のJAR/WARは分類子（例：`original`）が付与されて添付されます。

- **開発ワークフロー**:
  - 迅速な開発とテストには`mvn spring-boot:run`を使用します。
  - デプロイ可能な実行可能JARまたはWARをビルドするには`mvn package`を使用します。

- **統合テスト**:
  - 統合テスト中にアプリケーションのライフサイクルを管理するために`spring-boot:start`と`spring-boot:stop`を使用します。

---

### **まとめ**
`spring-boot-maven-plugin`を使用するには：
1. プロジェクトがSpring Bootプロジェクトであることを確認します（通常は`spring-boot-starter-parent`を継承するか、`spring-boot-dependencies` BOMを使用します）。
2. `pom.xml`の`<build><plugins>`セクションにプラグインを追加します。
3. 以下のようなMavenコマンドを使用します：
   - アプリケーションを実行するには：`mvn spring-boot:run`
   - 実行可能なJAR/WARをビルドするには：`mvn package`
   - 必要に応じて、`spring-boot:start`、`spring-boot:stop`、`spring-boot:build-info`などの他のゴールを使用します。
4. オプションで、高度なユースケースのために`pom.xml`でプラグインの設定をカスタマイズします。

この設定により、Mavenを使用してSpring Bootアプリケーションを効率的にビルド、実行、管理できるようになります。