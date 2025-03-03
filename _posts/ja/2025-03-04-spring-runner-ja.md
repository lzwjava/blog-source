---
audio: false
generated: true
lang: ja
layout: post
title: SpringRunnerをJavaテストで使用する
translated: true
---

`SpringRunner` を JUnit の `@RunWith` ランナーで Java テストで使用するには、以下の手順に従ってください。質問で「SpringRuner」と記載されているのはタイプミスであり、`SpringRunner` を指していると仮定しています。以下に完全なガイドを示します。

### ステップ 1: Spring テスト依存関係を追加する
`SpringRunner` を使用するには、プロジェクトに Spring テストモジュールが必要です。Maven を使用している場合は、`pom.xml` に次の依存関係を追加してください：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

`${spring.version}` を使用している Spring のバージョン（例：`5.3.22`）に置き換えてください。Gradle を使用している場合は、`build.gradle` に次のように追加してください：

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

これにより、`SpringRunner` および他の Spring テストユーティリティが利用可能になります。

### ステップ 2: テストクラスに `@RunWith(SpringRunner.class)` アノテーションを追加する
`@RunWith` アノテーションは、JUnit に特定のランナーを使用するように指示します。Spring 統合のためには、`SpringRunner` を使用します。これは Spring TestContext Framework の一部です。テストクラスに次のアノテーションを追加してください：

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // テストコードをここに記述
}
```

`SpringRunner` は、依存性注入やコンテキストの読み込みなどの Spring の機能をテストで有効にします。`@RunWith` は JUnit 4 のアノテーションなので、このアプローチは JUnit 4 を使用していることを前提としています。JUnit 5 の場合は `@ExtendWith(SpringExtension.class)` を使用しますが、「RunWith ランナー」の言及から JUnit 4 を使用していると推測されます。

### ステップ 3: Spring アプリケーションコンテキストを `@ContextConfiguration` で設定する
テストで Spring 管理されたビーンを使用するには、Spring アプリケーションコンテキストを読み込む必要があります。`@ContextConfiguration` アノテーションはその方法を指定します。例えば、設定クラス（例：`AppConfig`）がある場合は、次のようにします：

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // テストコードをここに記述
}
```

設定が XML ファイル（例：`applicationContext.xml`）にある場合は、次のようにします：

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

これにより、`SpringRunner` にテスト用にどのビーンと設定を読み込むかが指示されます。

### ステップ 4: `@Autowired` で Spring ビーンを注入する
コンテキストが読み込まれると、`@Autowired` を使用して Spring 管理されたビーンをテストクラスに注入できます。例えば、`MyService` というサービスがある場合は、次のようにします：

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

これにより、テストで注入されたビーンを使用できます。

### ステップ 5: `@Test` でテストメソッドを記述する
JUnit の `@Test` アノテーションを使用してテストメソッドを定義します。例えば、次のようにします：

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

`@Test` アノテーションは、JUnit にテストとして実行するメソッドをマークします。`SpringRunner` を使用すると、これらのメソッドは Spring コンテキストと相互作用できます。

### 例：すべてをまとめる
以下に完全な例を示します：

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
- **目的**：`SpringRunner` は、依存性注入やコンテキスト機能が必要な統合テストに最適です。ユニットテストには Mockito やプレーンな JUnit を検討してください。
- **一般的な問題**：`spring-test` 依存関係が含まれていないと、`ClassNotFoundException` などのエラーが発生します。また、`@ContextConfiguration` が有効な設定を指していることを確認してください。
- **オプションのアノテーション**：データベースを変更するテストには `@Transactional` を使用し、変更をロールバックするか、`@ActiveProfiles` を使用してプロファイル（例：`test`）を指定します。

この設定により、Spring のテストサポートを使用して JUnit テストを実行し、依存性注入やコンテキスト管理などの機能を活用できます。