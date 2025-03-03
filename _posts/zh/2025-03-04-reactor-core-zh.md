---
audio: false
generated: true
lang: zh
layout: post
title: 反应式编程与Java
translated: true
---

要使用 **reactor-core**，一个基于反应流规范的用于构建非阻塞、异步应用程序的Java库，请按照以下步骤进行：

---

### 1. 将 reactor-core 添加为依赖
首先，将 **reactor-core** 包含到您的项目中。根据您的构建工具：

- **Maven**：将以下内容添加到您的 `pom.xml`：
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**：将以下内容添加到您的 `build.gradle`：
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

这将确保库在您的项目中可用。如果需要，请在 [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) 查找最新版本。

---

### 2. 了解核心组件
Reactor-core 提供了两个主要类用于反应式编程：
- **`Flux`**：表示一个可以发出 **0 到 N 个项** 的异步流。
- **`Mono`**：表示一个可以发出 **0 个或 1 个项** 的异步流。

这些是您用来处理数据的基础构建块。

---

### 3. 创建 Flux 或 Mono
您可以创建 `Flux` 或 `Mono` 的实例来表示您的数据流。

- **使用 Flux 的示例**（多个项）：
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **使用 Mono 的示例**（单个项）：
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

`just` 方法是从静态值创建流的一种简单方法，但 Reactor 提供了许多其他创建方法（例如，从数组、范围或自定义源）。

---

### 4. 订阅以处理数据
要消费发出的项，您需要**订阅** `Flux` 或 `Mono`。订阅会触发流开始发出数据。

- **订阅 Flux**：
  ```java
  numbers.subscribe(System.out::println);  // 打印: 1, 2, 3, 4, 5
  ```

- **订阅 Mono**：
  ```java
  greeting.subscribe(System.out::println); // 打印: Hello, World!
  ```

`subscribe` 方法还可以接受额外的参数，例如错误处理程序或完成回调，以获得更多控制。

---

### 5. 使用操作符转换数据
Reactor 提供了一套丰富的操作符来操作流，例如 `map`、`filter` 等。

- **使用 Flux 和 map 的示例**：
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // 打印: 2, 4, 6, 8, 10
  ```

- **使用 Mono 和 map 的示例**：
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // 打印: HELLO, WORLD!
  ```

这些操作符允许您以声明性方式转换、过滤或组合数据。

---

### 6. 处理错误和反压
Reactor-core 支持错误处理和反压管理：
- **错误处理**：使用带有错误消费者的 `subscribe`：
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // 打印: Oops!
  ```
- **反压**：使用操作符（例如 `onBackpressureBuffer()` 或 `onBackpressureDrop()`）控制订阅者如何处理压倒性的数据流。

---

### 7. 进一步探索
对于更高级的用法：
- 查看 [官方 Reactor 文档](https://projectreactor.io/docs/core/release/reference/) 以获取详细示例和教程。
- 查看 [reactor-core GitHub 存储库](https://github.com/reactor/reactor-core) 以获取更多资源。

---

### 总结
要使用 **reactor-core**：
1. 将其作为项目的依赖项添加。
2. 使用 `Flux` 处理多个项或使用 `Mono` 处理单个项。
3. 使用方法（例如 `just`）创建流。
4. 订阅以处理数据。
5. 根据需要应用操作符来转换流。

这是使用 reactor-core 进行反应式编程的入门指南。通过小示例进行实验，以熟悉其反应式范式！