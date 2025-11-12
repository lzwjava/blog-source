---
audio: false
generated: true
lang: ja
layout: post
title: Springアプリケーションコンテキストへのアクセス
translated: true
type: note
---

Springの`ApplicationContextAware`インターフェースを使用して、KafkaコンシューマーなどのプレーンなJavaオブジェクト内で`ApplicationContext`にアクセスするには、Spring管理のBeanとプレーンオブジェクトを連携させる方法が必要です。以下にその方法を示します：

### 一般的なアプローチ
`ApplicationContextAware`インターフェースを使用すると、Spring管理のBeanがSpringから自動的に`ApplicationContext`を受け取ることができます。これを使用して、Springによって管理されていない（つまり、Springコンテナによって作成されたBeanではない）プレーンJavaオブジェクトでコンテキストを利用可能にすることができます。

#### ApplicationContextにアクセスする手順
1. **Spring管理のヘルパークラスを作成**：
   `ApplicationContextAware`を実装し、Springによって管理される（例：`@Component`で注釈された）クラスを定義します。このクラスは、Springアプリケーションの起動時に`ApplicationContext`を受け取ります。

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

   - `@Component`は、SpringがこのBeanを管理することを保証します。
   - `setApplicationContext`は、Springによって`ApplicationContext`を注入するために呼び出されます。
   - 静的`context`変数とgetterにより、どこからでもアクセスできます。

2. **プレーンJavaオブジェクト内でコンテキストにアクセス**：
   プレーンJavaオブジェクト（例：手動で作成されたKafkaコンシューマー）で、ヘルパークラスを使用して`ApplicationContext`を取得し、それを使用してSpring管理のBeanを取得します。

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // 必要に応じてサービスや他のBeanを使用
       }
   }
   ```

   - これは、`ApplicationContextProvider`が起動時にSpringによって初期化され、コンテキストが静的に利用可能になるため機能します。

3. **代替案：コンテキストを明示的に渡す**：
   プレーンJavaオブジェクトがSpring管理のBeanによって作成される場合、そのBeanに`ApplicationContext`を自動注入し、コンストラクターまたはセッターを介してプレーンオブジェクトに渡すことができます。

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

   - これにより、静的変数が回避され、依存関係が明示的になり、テスト容易性が向上します。

### Kafkaコンシューマー固有のソリューション
Kafkaコンシューマーを扱っており、**Spring Kafka**を使用している場合、推奨されるアプローチは、コンシューマーをプレーンJavaオブジェクトとして扱うのではなく、直接Springエコシステムに統合することです。

#### `@KafkaListener`の使用
KafkaコンシューマーをSpring管理のBeanとして`@KafkaListener`メソッドで定義します。これにより、`ApplicationContext`や他のBeanを直接自動注入できます。

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
        // contextまたはsomeServiceを直接使用
        SomeService service = context.getBean(SomeService.class); // 必要であれば
        someService.process(message);
    }
}
```

- Spring Kafkaは、スレッド処理やポーリングを含むコンシューマーのライフサイクルを管理します。
- 自動注入により、ほとんどの場合、手動でコンテキストを取得する必要がなくなります。

#### 手動Kafkaコンシューマー
Kafkaコンシューマーを手動で作成する必要がある場合（例：Kafkaクライアントライブラリを直接使用）、Spring管理のBean内で作成し、上記の明示的な受け渡しアプローチに示すように`ApplicationContext`を渡します。

### 推奨事項
- **Kafkaコンシューマーの場合**：可能な限り、Spring管理のBean内でSpring Kafkaの`@KafkaListener`を使用してください。これにより、SpringとKafkaの統合が活用され、`ApplicationContext`や他のBeanへのアクセスが簡素化されます。
- **一般的なプレーンJavaオブジェクトの場合**：静的`ApplicationContextProvider`アプローチを使用するか、Spring管理のBeanから`ApplicationContext`を明示的に渡します。可能な場合は、明示的な受け渡し方法が推奨されます。これは、静的状態を回避し、テスト容易性を向上させるためです。

これらの方法に従うことで、特定のセットアップに応じて、Kafkaコンシューマーを含むプレーンJavaオブジェクトでSpringコンテキストを利用可能にするために`ApplicationContextAware`を効果的に使用できます。