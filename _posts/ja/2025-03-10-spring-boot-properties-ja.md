---
audio: false
generated: true
lang: ja
layout: post
title: Spring Bootにおけるプロパティの仕組み
translated: true
type: note
---

Spring Bootにおけるプロパティの動作方法を探ってみましょう。YAMLや`.properties`ファイルの使用方法、`-D`のようなコマンドライン引数での上書き方法、プロパティを初期化する様々な方法、そして効果的なテスト方法について説明します。

---

### **Spring Bootでのプロパティの動作**
Spring Bootは、キーと値のペアであるプロパティを通じて、アプリケーション設定を管理する柔軟なシステムを提供します。これらのプロパティは複数のソースで定義でき、Spring Bootは特定の優先順位に基づいてそれらを解決します。これにより、異なる環境やデプロイシナリオに合わせてアプリケーションをカスタマイズできます。プロパティは**Spring Environment**に読み込まれ、アプリケーション全体でアクセス可能になります。

プロパティの主なソースは以下の通りです：
- 設定ファイル（例：`application.properties` または `application.yml`）
- コマンドライン引数（例：`--server.port=8081`）
- システムプロパティ（例：`-Dserver.port=8081`）
- 環境変数
- Javaコード（例：`@Value` または `@ConfigurationProperties`経由）

---

### **YAMLまたはプロパティファイルの使用**
Spring Bootは設定ファイルに対して2つの主要なフォーマットをサポートしており、どちらも通常`src/main/resources`に配置されます：

#### **1. `.properties` ファイル**
これはシンプルなフラットなキー値形式です：
```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

#### **2. `.yml` または `.yaml` ファイル**
これはインデントを使用した構造化された階層形式です：
```yaml
server:
  port: 8080
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mydb
```

**重要なポイント：**
- シンプルな設定には`.properties`を、ネストされたまたは複雑な設定には`.yml`を使用します。
- 環境固有の設定には、プロファイル固有のファイル（例：`application-dev.yml`）を使用できます。
- 例：`server.port=8080`を設定すると、Spring Bootアプリケーションが実行されるポートが変更されます。

---

### **コマンドライン引数を使用したプロパティの上書き**
設定ファイルで定義されたプロパティは、2つの方法でコマンドライン引数を使用して上書きできます：

#### **1. Spring Bootプロパティに `--` を使用する**
アプリケーション実行時にプロパティを直接渡します：
```bash
java -jar myapp.jar --server.port=8081 --spring.datasource.url=jdbc:mysql://localhost:3306/testdb
```
これらは設定ファイルよりも優先されます。

#### **2. システムプロパティに `-D` を使用する**
`-D`でシステムプロパティを設定します。Spring Bootもこれを認識します：
```bash
java -Dserver.port=8081 -Dspring.datasource.url=jdbc:mysql://localhost:3306/testdb -jar myapp.jar
```
システムプロパティも設定ファイルの値を上書きします。

---

### **プロパティを初期化する様々な方法**
Spring Bootは、ファイルやコマンドライン引数以外にも、プロパティを定義または初期化するいくつかの方法を提供します：

#### **1. 環境変数**
プロパティは環境変数を介して設定できます。例えば：
- 環境で`SERVER_PORT=8081`を設定すると、Spring Bootはそれを`server.port`にマッピングします。
- **命名規則：** プロパティ名を大文字に変換し、ドット（`.`）をアンダースコア（`_`）に置き換えます。例：`spring.datasource.url`は`SPRING_DATASOURCE_URL`になります。

#### **2. Javaコード**
プログラムでプロパティを初期化できます：
- **`@Value`を使用：** 特定のプロパティをフィールドに注入します。
  ```java
  @Value("${server.port}")
  private int port;
  ```
- **`@ConfigurationProperties`を使用：** プロパティのグループをJavaオブジェクトにバインドします。
  ```java
  @Component
  @ConfigurationProperties(prefix = "app")
  public class AppProperties {
      private String name;
      // getters and setters
  }
  ```
  これは`app.name`のようなプロパティを`name`フィールドにバインドします。

#### **3. デフォルト値**
プロパティが定義されていない場合のフォールバック値を提供します：
- `@Value`で：`@Value("${server.port:8080}")`は、`server.port`が未設定の場合に`8080`を使用します。
- 設定ファイルで：`application.properties`またはYAMLでデフォルトを設定します。

---

### **プロパティの優先順位**
Spring Bootは、複数のソースからプロパティを次の順序で解決します（高い優先順位が低いものを上書きします）：
1. コマンドライン引数（`--property=value`）
2. システムプロパティ（`-Dproperty=value`）
3. 環境変数
4. 設定ファイル（`application.properties` または `application.yml`）
5. コード内のデフォルト値

**例：** `application.properties`に`server.port=8080`があっても、`java -jar myapp.jar --server.port=8081`を実行すると、ポートは`8081`になります。

---

### **プロパティのテスト方法**
プロパティをテストすることで、アプリケーションが期待通りに動作することを確認します。一般的なアプローチは以下の通りです：

#### **1. `@TestPropertySource`の使用**
ユニットテストでプロパティを上書きします：
```java
@SpringBootTest
@TestPropertySource(properties = {"server.port=9090"})
public class MyTest {
    // テストコード
}
```

#### **2. `application-test.properties`の使用**
テスト固有のファイルを`src/test/resources`に配置します：
```properties
server.port=9090
```
Spring Bootはテスト中にこれを自動的に読み込みます。

#### **3. プログラムによる上書き**
テスト設定でプロパティを設定します：
```java
@SpringBootTest
public class MyTest {
    @BeforeEach
    public void setup() {
        System.setProperty("server.port", "9090");
    }
}
```

#### **4. `@ActiveProfiles`の使用**
プロファイル固有のプロパティを有効化します：
- テスト設定で`application-test.yml`を定義します。
- 使用法：
  ```java
  @SpringBootTest
  @ActiveProfiles("test")
  public class MyTest {
      // テストコード
  }
  ```

---

### **まとめ**
- **設定ファイル：** デフォルト設定に`application.properties`または`application.yml`を使用します。
- **コマンドライン引数：** `--property=value`または`-Dproperty=value`で上書きします。
- **初期化方法：** 環境変数、Javaコード（`@Value`、`@ConfigurationProperties`）、またはデフォルト値を活用します。
- **テスト：** `@TestPropertySource`、テスト固有ファイル、プログラムによる上書き、またはプロファイルを使用します。

これでSpring Bootでのプロパティ操作の基本をカバーしました。さらに詳細な情報が必要な場合はお知らせください！