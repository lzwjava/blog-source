---
audio: false
generated: true
lang: ja
layout: post
title: JavaテストにおけるSpringRunnerの使用
translated: true
type: note
---

JavaテストでJUnitの`@RunWith`ランナーと`SpringRunner`を使用するには、以下の手順に従ってください。なお、クエリ内の「SpringRuner」はタイプミスであり、`SpringRunner`を意味していると仮定します。完全なガイドを以下に示します：

### ステップ1：Spring Test依存関係を追加する
`SpringRunner`を使用するには、プロジェクトにSpring Testモジュールが必要です。Mavenを使用している場合は、`pom.xml`に以下の依存関係を追加してください：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

`${spring.version}`は使用しているSpringのバージョン（例：`5.3.22`）に置き換えてください。Gradleを使用している場合は、`build.gradle`に以下を追加してください：

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

これにより、`SpringRunner`およびその他のSpringテストユーティリティが利用可能になります。

### ステップ2：テストクラスに`@RunWith(SpringRunner.class)`を付与する
`@RunWith`アノテーションは、JUnitにデフォルトのランナーの代わりに特定のランナーを使用するように指示します。Spring統合の場合は、Spring TestContext Frameworkの一部である`SpringRunner`を使用します。このアノテーションをテストクラスに追加してください：

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // テストコードをここに記述
}
```

`SpringRunner`は、依存性の注入やコンテキストの読み込みなどのSpring機能をテストで有効にします。`@RunWith`はJUnit 4のアノテーションであるため、このアプローチはJUnit 4を使用していることを前提としています。JUnit 5の場合は、代わりに`@ExtendWith(SpringExtension.class)`を使用しますが、「RunWith runner」という言及からJUnit 4を想定しています。

### ステップ3：`@ContextConfiguration`でSpringアプリケーションコンテキストを設定する
テストでSpring管理のBeanを使用するには、Springアプリケーションコンテキストを読み込む必要があります。`@ContextConfiguration`アノテーションは、その方法を指定します。例えば、設定クラス（例：`AppConfig`）がある場合は、以下を使用します：

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // テストコードをここに記述
}
```

設定がXMLファイル（例：`applicationContext.xml`）にある場合は、以下を使用します：

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

これにより、テストで使用するBeanと設定を`SpringRunner`に指示します。

### ステップ4：`@Autowired`でSpring Beanを注入する
コンテキストが読み込まれたら、`@Autowired`を使用してSpring管理のBeanをテストクラスに注入できます。例えば、`MyService`というサービスがある場合：

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // テストメソッドをここに記述
}
```

これにより、注入されたBeanをテストで使用できます。

### ステップ5：`@Test`でテストメソッドを記述する
JUnitの`@Test`アノテーションを使用してテストメソッドを定義します。例：

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Expected result", result);
    }
}
```

`@Test`アノテーションは、JUnitがテストとして実行するメソッドをマークします。`SpringRunner`を使用すると、これらのメソッドはSpringコンテキストと対話できます。

### 例：すべてをまとめる
完全な例を以下に示します：

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// テスト用の設定クラス
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// テスト対象のサービスクラス
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// テストクラス
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Hello, Spring!", result);
    }
}
```

### 追加の注意点
- **目的**：`SpringRunner`は、Springの依存性注入やコンテキスト機能が必要な統合テストに最適です。単体テストの場合は、代わりにMockitoまたはプレーンなJUnitを検討してください。
- **一般的な問題**：`spring-test`依存関係が含まれていることを確認してください。含まれていない場合、`ClassNotFoundException`などのエラーが発生します。また、`@ContextConfiguration`が有効な設定を指していることを確認してください。
- **オプションのアノテーション**：データベースを変更するテスト（変更をロールバックするため）には`@Transactional`を、プロファイル（例：「test」）を指定するには`@ActiveProfiles`を使用してください。

この設定により、Springのテストサポートを活用したJUnitテストを実行でき、依存性の注入やコンテキスト管理などの機能を利用できます。