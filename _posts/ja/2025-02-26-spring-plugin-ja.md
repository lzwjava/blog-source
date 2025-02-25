---
audio: false
lang: ja
layout: post
title: Spring Boot Maven プラグイン
translated: true
---

`spring-boot-maven-plugin` を Maven ベースの Spring Boot プロジェクトで使用するには、以下の手順でプラグインを設定し、ビルド、実行、管理するために利用します。以下は包括的なガイドです。

---

### **1. プロジェクトが Spring Boot プロジェクトであることを確認する**

`spring-boot-maven-plugin` を使用する前に、プロジェクトが Spring Boot プロジェクトとして設定されていることを確認します。通常、以下を含みます：

- **`spring-boot-starter-parent` を継承する（推奨）**：
  - `pom.xml` で `spring-boot-starter-parent` を親として設定し、Spring Boot の依存関係とプラグインのバージョンを管理します。
  - 例：
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- Spring Boot のバージョンを置き換えます -->
        <relativePath/> <!-- リポジトリから親を検索 -->
    </parent>
    ```

- **`spring-boot-dependencies` BOM（ビル・オブ・マテリアル）を使用する**：
  - `spring-boot-starter-parent` を使用できない場合、`dependencyManagement` セクションで `spring-boot-dependencies` BOM をインポートします。
  - 例：
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- Spring Boot のバージョンを置き換えます -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

`spring-boot-starter-parent` を使用することを推奨します。これにより、プラグインのバージョンが自動的に管理されます。

---

### **2. `pom.xml` に `spring-boot-maven-plugin` を追加する**

プラグインを使用するには、`pom.xml` の `<build><plugins>` セクションに宣言する必要があります。

- **`spring-boot-starter-parent` を使用する場合**：
  - バージョンを指定せずにプラグインを追加します。親によって管理されます。
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

- **`spring-boot-starter-parent` を使用しない場合**：
  - 使用している Spring Boot バージョンに一致するバージョンを明示的に指定します。
  - 例：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- Spring Boot のバージョンを置き換えます -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. プラグインのゴールを利用する**

`spring-boot-maven-plugin` は、Spring Boot アプリケーションをビルド、実行、管理するためのいくつかのゴールを提供します。以下は最も一般的に使用されるゴールです：

- **`spring-boot:run`**
  - Maven を使用して、埋め込み Web サーバー（例：Tomcat）を使用して Spring Boot アプリケーションを直接実行します。
  - 開発とテストに便利です。
  - コマンド：
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - `mvn package` によって生成された JAR または WAR ファイルを、すべての依存関係を含む実行可能な「fat JAR」または WAR に再パッケージします。
  - プラグインが設定されている場合、このゴールは `package` フェーズ中に自動的に実行されます。
  - コマンド：
    ```
    mvn package
    ```
  - 実行後、アプリケーションを以下のように開始できます：
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` と `spring-boot:stop`**
  - 統合テスト中に `pre-integration-test` フェーズと `post-integration-test` フェーズでアプリケーションを開始および停止するために使用されます。
  - 例：
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - ビルド情報（例：ビルド時間、バージョン）を含む `build-info.properties` ファイルを生成します。
  - この情報は、Spring Boot の `BuildProperties` ビーンまたは `@Value` アノテーションを使用してアプリケーションでアクセスできます。
  - コマンド：
    ```
    mvn spring-boot:build-info
    ```

---

### **4. プラグインの設定をカスタマイズする（オプション）**

`pom.xml` で設定オプションを追加することで、`spring-boot-maven-plugin` の動作をカスタマイズできます。以下は一般的なカスタマイズです：

- **メインクラスを指定する**：
  - プラグインがメインクラスを自動的に検出できない場合は、手動で指定します。
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

- **Fat JAR から依存関係を除外する**：
  - ランタイム環境（例：外部サーブレットコンテナ）によって提供される依存関係を除外します。
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

- **アプリケーションの引数を設定する**：
  - `spring-boot:run` で実行する際にアプリケーションに渡す引数を設定します。
  - `pom.xml` での例：
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
  - または、コマンドラインから引数を渡す：
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **WAR ファイルのビルド**：
  - 外部サーブレットコンテナにデプロイするための WAR ファイルをビルドする場合、`pom.xml` でプロジェクトのパッケージングを `war` に設定します：
    ```xml
    <packaging>war</packaging>
    ```
  - 環境によって提供される埋め込みサーブレットコンテナ（例：Tomcat）を除外する必要がある場合があります。以下の依存関係を `provided` として追加します：
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

### **5. 重要なポイント**

- **デフォルト動作**：
  - `mvn package` を実行すると、プラグインは `package` フェーズ中に JAR/WAR を自動的に再パッケージして実行可能にします。
  - 再パッケージされたアーティファクトがメインアーティファクトであり、元の JAR/WAR はクラシファイア（例：`original`）を付けてアタッチされます。

- **開発ワークフロー**：
  - `mvn spring-boot:run` を使用して、迅速な開発とテストを行います。
  - `mvn package` を使用して、デプロイ可能な実行可能な JAR または WAR をビルドします。

- **統合テスト**：
  - `spring-boot:start` と `spring-boot:stop` を使用して、統合テスト中のアプリケーションのライフサイクルを管理します。

---

### **まとめ**

`spring-boot-maven-plugin` を使用するには：

1. プロジェクトが Spring Boot プロジェクトであることを確認し、`spring-boot-starter-parent` を継承するか、`spring-boot-dependencies` BOM を使用します。
2. プラグインを `pom.xml` の `<build><plugins>` セクションに追加します。
3. Maven コマンドを使用します：
   - `mvn spring-boot:run` でアプリケーションを実行します。
   - `mvn package` で実行可能な JAR/WAR をビルドします。
   - 必要に応じて `spring-boot:start`、`spring-boot:stop`、`spring-boot:build-info` などの他のゴールを使用します。
4. 高度な使用例のために `pom.xml` でプラグインの設定をカスタマイズします。

この設定により、Maven を使用して Spring Boot アプリケーションを効率的にビルド、実行、管理できます。