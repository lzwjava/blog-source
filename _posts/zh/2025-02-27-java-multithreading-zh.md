---
audio: false
generated: true
lang: zh
layout: post
title: Java 多线程
translated: true
---

让我们深入了解Java多线程以及如何有效使用`Executor`框架。多线程允许您的程序同时运行多个任务，从而提高I/O密集型或CPU密集型操作的性能。`Executor`框架通过抽象低级线程创建和处理来简化线程管理。我将带您了解基础知识，然后展示如何使用`Executor`及其相关工具。

---

### 1. Java多线程基础
Java提供了两种主要方法来创建线程：
- **扩展`Thread`类**：
```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // 启动线程
    }
}
```
- **实现`Runnable`接口**：
```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```
- 调用`start()`（而不是`run()`）来启动线程——`run()`只是在当前线程中执行代码。

---

### 2. 为什么使用`Executor`？
手动创建线程适用于简单情况，但对于管理大量任务（例如线程开销、资源耗尽）效率低下。`Executor`框架（在Java 5中引入，位于`java.util.concurrent`）提供了线程池和任务管理系统，使多线程更清晰且可扩展。

---

### 3. 使用`ExecutorService`
`ExecutorService`接口（`Executor`的子接口）是首选工具。以下是如何使用它：

#### 步骤1：创建一个`ExecutorService`
使用`Executors`实用程序类创建线程池：
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // 固定线程池，4个线程
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // 提交任务
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // 模拟工作
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // 关闭执行器
        executor.shutdown(); // 阻止新任务，等待现有任务完成
    }
}
```
- `newFixedThreadPool(4)`创建一个包含4个线程的池。多余的任务在队列中等待。
- `submit()`接受`Runnable`或`Callable`任务（`Callable`返回结果）。

#### 常见的`Executor`类型
- `Executors.newSingleThreadExecutor()`：一个线程，按顺序处理任务。
- `Executors.newCachedThreadPool()`：根据需要创建线程，重用空闲线程（适用于短期任务）。
- `Executors.newScheduledThreadPool(n)`：用于带有延迟或周期性的任务调度。

---

### 4. 使用`Callable`和`Future`处理结果
如果需要任务结果，使用`Callable`而不是`Runnable`：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // 提交一个`Callable`任务
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // 在任务运行时执行其他工作
        System.out.println("Task submitted...");

        // 获取结果（如果任务未完成则阻塞）
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()`检索结果，如果任务未完成则阻塞。
- 使用`future.isDone()`在不阻塞的情况下检查完成情况。

---

### 5. 高级：线程池调优
对于实际应用程序，您可能需要自定义`ThreadPoolExecutor`：
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // 自定义线程池：2-4个线程，队列容量为10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // 核心池大小
            4, // 最大池大小
            60L, // 空闲线程超时
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // 任务队列
        );

        for (int i = 0; i < 15; i++) {
            executor.execute(() -> {
                System.out.println("Task by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        executor.shutdown();
    }
}
```
- 核心大小（2）：保持活动的最小线程数。
- 最大大小（4）：如果队列满则最大线程数。
- 队列：在所有线程都忙时保存任务。

---

### 6. 最佳实践
- **正确关闭**：始终调用`shutdown()`或`shutdownNow()`以避免资源泄漏。
- **处理中断**：在循环中检查`Thread.currentThread().isInterrupted()`。
- **避免过载**：过多的线程会降低性能——根据CPU核心数调整池大小（例如，`Runtime.getRuntime().availableProcessors()`）。
- **使用`try-finally`与`ExecutorService`**：
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // 提交任务
} finally {
    executor.shutdown();
}
```

---

### 结合Log4j的示例（综合使用）
将多线程与之前的Log4j问题结合：
```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.util.concurrent.*;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                logger.info("Task {} started by {}", taskId, Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    logger.error("Task {} interrupted", taskId, e);
                    Thread.currentThread().interrupt();
                }
                logger.info("Task {} completed", taskId);
            });
        }

        executor.shutdown();
    }
}
```
使用之前的`log4j2.xml`，这将任务进度记录到控制台和文件中。