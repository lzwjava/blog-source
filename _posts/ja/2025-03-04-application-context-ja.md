---
audio: false
generated: true
lang: ja
layout: post
title: アプリケーションコンテキストへのアクセス
translated: true
---

Springの`ApplicationContextAware`インターフェースを使用して、KafkaコンサマーなどのプレーンなJavaオブジェクトで`ApplicationContext`にアクセスするには、Spring管理のビーンとプレーンなオブジェクトを橋渡しする方法が必要です。以下にその方法を示します。

### 一般的なアプローチ
`ApplicationContextAware`インターフェースは、Spring管理のビーンがSpringから自動的に`ApplicationContext`を受け取ることを許可します。これを使用して、Springによって管理されていないプレーンなJavaオブジェクト（つまり、Springコンテナによって作成されたビーンではない）にコンテキストを利用可能にします。

#### ApplicationContextへのアクセス手順
1. **Spring管理のヘルパークラスを作成する**:
   Springによって管理されるクラスを定義し、`ApplicationContextAware`を実装します（例：`@Component`で注釈付け）。このクラスは、Springアプリケーションが開始されたときに`ApplicationContext`を受け取ります。

   ```java
   import org.springframework.context.ApplicationContext;
   import org.springframework.context.ApplicationContextAware;
   import org.springframework.stereotype.Component;

   @Component
   public class ApplicationContextProvider implements ApplicationContextAware {
       private static ApplicationContext context;

       @Override
       public void setApplicationContext(ApplicationContext applicationContext) {
           context = applicationContext;
       }

       public static ApplicationContext getApplicationContext() {
           return context;
       }
   }
   ```

   - `@Component`は、Springがこのビーンを管理することを保証します。
   - `setApplicationContext`は、Springによって`ApplicationContext`をインジェクトするために呼び出されます。
   - 静的な`context`変数とゲッターは、どこからでもアクセスできるようにします。

2. **プレーンなJavaオブジェクトでコンテキストを取得する**:
   プレーンなJavaオブジェクト（例：手動で作成されたKafkaコンサマー）で、ヘルパークラスを使用して`ApplicationContext`を取得し、Spring管理のビーンを取得します。

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // 必要に応じてサービスや他のビーンを使用
       }
   }
   ```

   - これは、`ApplicationContextProvider`がSpringの起動時に初期化されるため、コンテキストが静的に利用可能になります。

3. **代替案：コンテキストを明示的に渡す**:
   プレーンなJavaオブジェクトがSpring管理のビーンによって作成される場合、そのビーンに`ApplicationContext`を自動的に注入し、コンストラクタまたはセッターを通じてプレーンなオブジェクトに渡すことができます。

   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.context.ApplicationContext;
   import org.springframework.stereotype.Component;

   @Component
   public class KafkaConsumerCreator {
       @Autowired
       private ApplicationContext context;

       public MyKafkaConsumer createConsumer() {
           return new MyKafkaConsumer(context);
       }
   }

   public class MyKafkaConsumer {
       private final ApplicationContext context;

       public MyKafkaConsumer(ApplicationContext context) {
           this.context = context;
       }

       public void processMessage() {
           SomeService service = context.getBean(SomeService.class);
           // サービスを使用
       }
   }
   ```

   - これは、静的変数を避け、依存関係を明示的にし、テスト可能性を向上させます。

### Kafkaコンサマー固有のソリューション
Kafkaコンサマーを使用し、**Spring Kafka**を使用している場合、推奨されるアプローチは、プレーンなJavaオブジェクトとして扱うのではなく、Kafkaコンサマーを直接Springエコシステムに統合することです。

#### `@KafkaListener`の使用
KafkaコンサマーをSpring管理のビーンとして定義し、`@KafkaListener`メソッドを持つようにします。これにより、`ApplicationContext`や他のビーンを直接自動注入できます。

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class MyKafkaConsumer {
    @Autowired
    private ApplicationContext context;

    @Autowired
    private SomeService someService;

    @KafkaListener(topics = "my-topic")
    public void consume(String message) {
        // contextやsomeServiceを直接使用
        SomeService service = context.getBean(SomeService.class); // 必要に応じて
        someService.process(message);
    }
}
```

- Spring Kafkaは、コンサマーのライフサイクルを管理し、スレッドとポーリングを含む。
- 自動注入により、コンテキストを手動で取得する必要がほとんどありません。

#### 手動Kafkaコンサマー
Kafkaクライアントライブラリを直接使用して`KafkaConsumer`を手動で作成する必要がある場合（例：Spring Kafkaを使用せずに）、Spring管理のビーン内で行い、上記の明示的な渡し方を使用して`ApplicationContext`を渡すようにします。

### 推奨事項
- **Kafkaコンサマーの場合**: 可能な限り、Spring Kafkaの`@KafkaListener`をSpring管理のビーンで使用します。これにより、SpringのKafka統合を活用し、`ApplicationContext`や他のビーンへのアクセスが簡単になります。
- **一般的なプレーンなJavaオブジェクトの場合**: 静的な`ApplicationContextProvider`アプローチを使用するか、Spring管理のビーンから`ApplicationContext`を明示的に渡す方法を使用します。明示的な渡し方法が可能な場合は、静的な状態を避け、テスト可能性を向上させるために推奨されます。

これらの方法を使用することで、`ApplicationContextAware`を効果的に使用して、プレーンなJavaオブジェクト、Kafkaコンサマーを含む特定のセットアップにSpringコンテキストを利用可能にすることができます。