---
audio: false
generated: false
lang: ja
layout: post
title: スプリング IoC コンテナ
translated: true
---

Spring IoCコンテナの使用方法を明確かつ実践的な方法で説明します。Spring IoCコンテナはSpringフレームワークの核心であり、アプリケーションオブジェクト（ビーンと呼ばれる）のライフサイクルと設定を管理する責任があります。オブジェクトの作成と依存関係の注入を手動で行うのではなく、コンテナがその処理を行うことで「制御を反転」します。

以下は、始めるためのステップバイステップのガイドです。

---

### 1. **基本を理解する**
- **機能**: IoCコンテナは、提供されたメタデータ（XML、Javaアノテーション、またはJavaコードを介して）に基づいてビーン（アプリケーションオブジェクト）を作成、設定、管理します。
- **主要な概念**:
  - **ビーン**: コンテナによって管理されるオブジェクト。
  - **依存関係注入（DI）**: コンテナは依存関係（他のビーンまたは値）をオブジェクトに注入します。
  - **設定**: コンテナにどのビーンを作成し、どのようにワイヤリングするかを指示します。

---

### 2. **プロジェクトの設定**
Spring IoCを使用するには、Springプロジェクトが必要です。新規作成の場合:
- **Spring Boot**（最も簡単な方法）またはプレーンなSpringを使用します。
- Mavenを使用している場合、`pom.xml`に依存関係を追加します:
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- 最新バージョンを使用 -->
  </dependency>
  ```
- Spring Bootの場合:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- 現在の最新バージョン -->
  </dependency>
  ```

---

### 3. **ビーンを定義する**
ビーンを3つの主要な方法で定義できます。

#### a) **アノテーションを使用する（最も一般的）**
- 簡単なJavaクラスを作成し、`@Component`（または`@Service`、`@Repository`などの専用アノテーション）でアノテートします。
- 例:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **Java設定を使用する**
- `@Configuration`付きの設定クラスを作成し、`@Bean`でビーンを定義します。
- 例:
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

#### c) **XMLを使用する（レガシーアプローチ）**
- ビーンをXMLファイル（例: `beans.xml`）で定義します:
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
ビーンを管理するためにコンテナを起動する必要があります。

#### a) **Spring Bootを使用する**
- Spring Bootは自動的に行います。`@SpringBootApplication`付きのメインクラスを作成します:
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
- コンテナは`@Component`クラスをスキャンし、管理します。

#### b) **プレーンなSpring（アノテーションベース）**
- `AnnotationConfigApplicationContext`を使用します:
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

#### c) **XMLを使用する**
- `ClassPathXmlApplicationContext`を使用します:
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

### 5. **依存関係を注入する**
IoCコンテナはビーンに依存関係を注入できます。

#### a) **コンストラクタ注入（推奨）**
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

#### b) **セッター注入**
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

#### c) **フィールド注入（推奨されない）**
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
- 注入ポイントをマークするために`@Autowired`（Spring固有）または`@Inject`（JSR-330標準）を使用します。

---

### 6. **ビーンを実行し使用する**
- コンテナが実行中の場合、ビーンとその依存関係をワイヤリングします。`context.getBean()`（プレーンなSpring）を使用してビーンを取得するか、Spring Bootが自動的に注入を処理するようにします。

Spring Bootの例:
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
- **スコープ**: デフォルトではビーンはシングルトンです。新しいインスタンスをリクエストごとに作成するには、`@Scope("prototype")`を使用します。
- **コンポーネントスキャン**: ビーンが異なるパッケージにある場合は、設定クラスに`@ComponentScan`を追加します。
- **プロファイル**: 特定の環境（例: "dev"、"prod"）でビーンをアクティブにするには、`@Profile`を使用します。
- **コンテキストを閉じる**: Spring Bootアプリケーション以外では、`context.close()`を呼び出してリソースを解放します。

---

これが概要です！Spring Bootとアノテーションを使用して簡単に始めることをお勧めします。特定の部分で詰まった場合（例: 依存関係のワイヤリングやデバッグ）は、お知らせください。さらに深く掘り下げてお手伝いします！