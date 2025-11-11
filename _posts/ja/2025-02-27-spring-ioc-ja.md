---
audio: false
generated: true
lang: ja
layout: post
title: Spring IoC コンテナ
translated: true
type: note
---

Spring IoC（Inversion of Control）コンテナの使い方を明確かつ実践的に解説します。Spring IoCコンテナはSpring Frameworkの核となる機能で、アプリケーションオブジェクト（Beanと呼ばれる）のライフサイクルと設定を管理します。オブジェクトの作成と依存性の注入を手動で行うのではなく、コンテナが代行することで、制御を「逆転」させます。

以下に、始めるためのステップバイステップガイドを示します：

---

### 1. **基本を理解する**
- **役割**: IoCコンテナは、提供されたメタデータ（XML、Javaアノテーション、Javaコードによる）に基づいてBean（アプリケーションオブジェクト）の作成、設定、管理を行います。
- **主要な概念**:
  - **Bean**: コンテナによって管理されるオブジェクト。
  - **依存性の注入（DI）**: コンテナがオブジェクトに依存関係（他のBeanや値）を注入します。
  - **設定**: コンテナにどのBeanを作成し、どのように連携させるかを指示します。

---

### 2. **プロジェクトをセットアップする**
Spring IoCを使用するには、Springプロジェクトが必要です。新規で始める場合：
- **Spring Boot**（最も簡単な方法）またはプレーンなSpringを使用します。
- `pom.xml`（Mavenを使用する場合）に依存関係を追加します：
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- 最新バージョンを使用 -->
  </dependency>
  ```
- Spring Bootの場合は：
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- 現時点での最新 -->
  </dependency>
  ```

---

### 3. **Beanを定義する**
Beanを定義する主な方法は3つあります：

#### a) **アノテーションを使用（最も一般的）**
- 単純なJavaクラスを作成し、`@Component`（または`@Service`、`@Repository`などの特殊化されたアノテーション）で注釈します。
- 例：
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **Java Configurationを使用**
- `@Configuration`を付けた設定クラスを作成し、`@Bean`でBeanを定義します。
- 例：
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;

  @Configuration
  public class AppConfig {
      @Bean
      public MyService myService() {
          return new MyService();
      }
  }
  ```

#### c) **XMLを使用（レガシーなアプローチ）**
- XMLファイル（例：`beans.xml`）でBeanを定義します：
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **IoCコンテナを初期化する**
Beanを管理するためにコンテナを起動する必要があります。

#### a) **Spring Bootの場合**
- Spring Bootはこれを自動的に行います。`@SpringBootApplication`を付けたメインクラスを作成するだけです：
  ```java
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  public class MyApp {
      public static void main(String[] args) {
          SpringApplication.run(MyApp.class, args);
      }
  }
  ```
- コンテナは`@Component`クラスをスキャンして管理します。

#### b) **プレーンSpring（アノテーションベース）の場合**
- `AnnotationConfigApplicationContext`を使用します：
  ```java
  import org.springframework.context.annotation.AnnotationConfigApplicationContext;

  public class Main {
      public static void main(String[] args) {
          AnnotationConfigApplicationContext context = 
              new AnnotationConfigApplicationContext(AppConfig.class);
          MyService service = context.getBean(MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

#### c) **XMLの場合**
- `ClassPathXmlApplicationContext`を使用します：
  ```java
  import org.springframework.context.support.ClassPathXmlApplicationContext;

  public class Main {
      public static void main(String[] args) {
          ClassPathXmlApplicationContext context = 
              new ClassPathXmlApplicationContext("beans.xml");
          MyService service = context.getBean("myService", MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

---

### 5. **依存性を注入する**
IoCコンテナはBeanに依存性を注入できます。

#### a) **コンストラクタインジェクション（推奨）**
```java
@Component
public class MyController {
    private final MyService myService;

    public MyController(MyService myService) {
        this.myService = myService;
    }

    public void execute() {
        myService.doSomething();
    }
}
```

#### b) **セッターインジェクション**
```java
@Component
public class MyController {
    private MyService myService;

    @Autowired
    public void setMyService(MyService myService) {
        this.myService = myService;
    }
}
```

#### c) **フィールドインジェクション（あまり推奨されない）**
```java
@Component
public class MyController {
    @Autowired
    private MyService myService;

    public void execute() {
        myService.doSomething();
    }
}
```
- 注入ポイントをマークするには、`@Autowired`（Spring固有）または`@Inject`（JSR-330標準）を使用します。

---

### 6. **Beanを実行して使用する**
- コンテナが起動すると、Beanとその依存関係が連携されます。Beanは`context.getBean()`（プレーンSpring）で取得するか、Spring Bootでは注入を通じて自動的に処理させることができます。

Spring Bootの例：
```java
@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(MyApp.class, args);
        MyController controller = context.getBean(MyController.class);
        controller.execute();
    }
}
```

---

### 7. **追加のヒント**
- **スコープ**: デフォルトではBeanはシングルトンです。リクエストごとに新しいインスタンスが必要な場合は`@Scope("prototype")`を使用します。
- **コンポーネントスキャン**: Beanが異なるパッケージにある場合は、設定クラスに`@ComponentScan`を追加します。
- **プロファイル**: 特定の環境（例：「dev」、「prod」）でBeanを有効にするには`@Profile`を使用します。
- **コンテキストのクローズ**: Spring Boot以外のアプリでは、リソースを解放するために`context.close()`を呼び出します。

---

これがその要点です！簡単さを求めるなら、Spring Bootとアノテーションから始めてください。特定の部分（例えば、複雑な依存関係の連携やデバッグ）で行き詰まった場合は、お気軽に質問してください。さらに深く解説します！