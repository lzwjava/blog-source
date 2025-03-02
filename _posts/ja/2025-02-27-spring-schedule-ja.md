---
audio: true
generated: true
lang: ja
layout: post
title: スプリングでのタスクスケジューリング
translated: true
---

スプリングでのタスクのスケジューリングは、メールの送信、レポートの生成、システムのメンテナンスなど、繰り返しのあるジョブを自動化するための一般的な要件です。スプリングは、@Scheduledアノテーションとスプリングタスクスケジューラを通じて、強力で使いやすいタスクスケジューリング機能を提供しています。以下に、設定方法と主要な概念を説明します。

### 1. **スプリングアプリケーションでスケジューリングを有効にする**
スケジューリングを使用するには、スプリングアプリケーションでそれを有効にする必要があります。これは、@EnableSchedulingアノテーションを設定クラスに追加することで行います。

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // カスタムスケジューラ設定が必要でない限り、設定クラスは空で構いません
}
```

これにより、スプリングは@Scheduledでアノテートされたメソッドを検索し、定義されたスケジュールに従って実行します。

---

### 2. **スケジュールするタスクを作成する**
任意のスプリング管理ビーン（@Componentまたは@Serviceなど）でメソッドを定義し、@Scheduledでアノテートすることで、スケジュールを定義できます。以下に例を示します。

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // 5秒ごとに実行
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("タスクは実行されました: " + System.currentTimeMillis());
    }
}
```

この例では：
- @Componentはクラスをスプリングビーンにします。
- @Scheduled(fixedRate = 5000)はメソッドを5秒ごと（5000ミリ秒）に実行します。

---

### 3. **スケジューリングの種類**
スプリングは、タスクが実行されるタイミングを定義するためのいくつかの方法を提供しています。

#### a) **固定レート**
- タスクを固定間隔で実行し、タスクの実行時間に関係なく実行します。
- 例: @Scheduled(fixedRate = 5000)（5秒ごと）。

#### b) **固定遅延**
- 1つの実行の終了から次の実行の開始までの固定遅延でタスクを実行します。
- 例: @Scheduled(fixedDelay = 5000)（前のタスクが終了した後、5秒後に実行）。

#### c) **Cron式**
- より複雑なスケジュール（例：毎週の平日に9時）に対して、cronのような構文を使用します。
- 例: @Scheduled(cron = "0 0 9 * * MON-FRI")。

#### d) **初期遅延**
- タスクの最初の実行を遅延させます。fixedRateまたはfixedDelayと組み合わせることができます。
- 例: @Scheduled(fixedRate = 5000, initialDelay = 10000)（10秒後に開始し、その後5秒ごとに実行）。

---

### 4. **Cron構文の基本**
cronを使用する場合、以下のクイックリファレンスを参照してください：
- 形式: second minute hour day-of-month month day-of-week
- 例: @Scheduled(cron = "0 15 10 * * ?")（毎日10:15に実行）。

| フィールド         | 許可される値       |
|---------------|----------------------|
| 秒         | 0-59                |
| 分         | 0-59                |
| 時         | 0-23                |
| 月の日       | 1-31                |
| 月         | 1-12またはJAN-DEC     |
| 週の日       | 0-7またはSUN-SAT（0または7は日曜日） |

`*`（すべて）、`,`（リスト）、`-`（範囲）、`/`（インクリメント）などの特殊文字を使用できます。

---

### 5. **依存関係**
Spring Bootを使用している場合、スケジューリング機能は`spring-boot-starter`依存関係にデフォルトで含まれています。Spring Bootを使用しないSpringプロジェクトの場合は、以下を確認してください。

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- 最新バージョンを使用 -->
</dependency>
```

---

### 6. **Spring Bootの完全な例**
以下に、完全なSpring Bootの例を示します。

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
        System.out.println("5秒ごとに実行: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("毎分実行: " + System.currentTimeMillis());
    }
}
```

---

### 7. **スケジューラのカスタマイズ（オプション）**
デフォルトでは、スプリングはシングルスレッドスケジューラを使用します。並行タスク実行が必要な場合は、カスタム`TaskScheduler`を設定できます。

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
- アプリケーションを実行し、コンソールログを確認して、タスクが期待通りに実行されていることを確認します。
- テスト中は、結果を迅速に確認するために、短い間隔（例：2秒ごと）を使用します。