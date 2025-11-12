---
audio: false
generated: true
lang: ja
layout: post
title: Springでのタスクスケジューリング
translated: true
type: note
---

Springでのタスクスケジューリングは、メール送信、レポート生成、システムメンテナンスなどの繰り返しジョブを自動化するための一般的な要件です。Springは`@Scheduled`アノテーションとSpring Task Schedulerを通じて、強力で使いやすいタスクスケジューリング機能を提供します。以下では、セットアップの手順と主要な概念について説明します。

### 1. **Springアプリケーションでスケジューリングを有効化**
スケジューリングを使用するには、Springアプリケーションで有効化する必要があります。これは、設定クラスに`@EnableScheduling`アノテーションを追加することで行います。

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // カスタムスケジューラ設定が必要ない限り、設定クラスは空で構いません
}
```

これにより、Springは`@Scheduled`でアノテーションされたメソッドを探し、定義されたスケジュールに従って実行します。

---

### 2. **スケジュールするタスクの作成**
Spring管理Bean（`@Component`や`@Service`など）内でメソッドを定義し、`@Scheduled`でアノテーションを付けることができます。以下は例です：

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // 5秒ごとに実行
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Task executed at: " + System.currentTimeMillis());
    }
}
```

この例では：
- `@Component`はクラスをSpring Beanにします。
- `@Scheduled(fixedRate = 5000)`はメソッドを5秒（5000ミリ秒）ごとに実行します。

---

### 3. **スケジューリングのオプションタイプ**
Springはタスクの実行タイミングを定義するいくつかの方法を提供します：

#### a) **Fixed Rate**
- タスクの実行時間に関係なく、固定間隔でタスクを実行します。
- 例：`@Scheduled(fixedRate = 5000)`（5秒ごと）。

#### b) **Fixed Delay**
- 前の実行の終了と次の実行の開始の間に固定の遅延を設けてタスクを実行します。
- 例：`@Scheduled(fixedDelay = 5000)`（前のタスク終了後5秒）。

#### c) **Cron Expression**
- より複雑なスケジュール（例：「平日の午前9時毎日」）にcronライクな構文を使用します。
- 例：`@Scheduled(cron = "0 0 9 * * MON-FRI")`。

#### d) **Initial Delay**
- タスクの最初の実行を遅延させます。`fixedRate`または`fixedDelay`と組み合わせて使用します。
- 例：`@Scheduled(fixedRate = 5000, initialDelay = 10000)`（10秒後に開始し、その後5秒ごとに実行）。

---

### 4. **Cron構文の基本**
cronを使用する場合のクイックリファレンス：
- 形式：`秒 分 時 日 月 曜日`
- 例：`@Scheduled(cron = "0 15 10 * * ?")`（毎日10時15分に実行）。

| フィールド      | 許可される値          |
|-----------------|-----------------------|
| 秒              | 0-59                 |
| 分              | 0-59                 |
| 時              | 0-23                 |
| 日              | 1-31                 |
| 月              | 1-12 または JAN-DEC  |
| 曜日            | 0-7 または SUN-SAT（0または7は日曜日） |

`*`（すべて）、`,`（リスト）、`-`（範囲）、`/`（増分）などの特殊文字を使用できます。

---

### 5. **依存関係**
Spring Bootを使用している場合、スケジューリング機能は`spring-boot-starter`依存関係にデフォルトで含まれています。非BootのSpringプロジェクトでは、以下があることを確認してください：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- 最新バージョンを使用 -->
</dependency>
```

---

### 6. **Spring Bootでの完全な例**
完全なSpring Bootの例を以下に示します：

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Component
class ScheduledTasks {

    @Scheduled(fixedRate = 5000)
    public void runEveryFiveSeconds() {
        System.out.println("Running every 5 seconds: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("Running every minute: " + System.currentTimeMillis());
    }
}
```

---

### 7. **スケジューラのカスタマイズ（オプション）**
デフォルトでは、Springはシングルスレッドのスケジューラを使用します。並行タスク実行が必要な場合は、カスタムの`TaskScheduler`を設定できます：

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // スレッド数
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

これにより、複数のタスクを並行して実行できます。

---

### 8. **スケジュールされたタスクのテスト**
- アプリケーションを実行し、コンソールログを確認してタスクが期待通りに実行されていることを検証します。
- テスト中は結果を素早く確認するために、より短い間隔（例：2秒ごと）を使用します。