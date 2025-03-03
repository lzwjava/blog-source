---
audio: false
generated: true
lang: hant
layout: post
title: 反應式編程與Java
translated: true
---

要使用 **reactor-core**，一個基於反應式流規範的 Java 庫，用於構建非阻塞、非同步應用程式，請按照以下步驟進行：

---

### 1. 將 reactor-core 作為依賴項添加
首先，將 **reactor-core** 添加到您的項目中。根據您的構建工具：

- **Maven**：將以下內容添加到您的 `pom.xml`：
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**：將以下內容添加到您的 `build.gradle`：
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

這樣可以確保庫在您的項目中可用。如果需要，請在 [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) 查找最新版本。

---

### 2. 了解核心組件
Reactor-core 提供了兩個主要類用於反應式編程：
- **`Flux`**：表示一個可以發出 **0 到 N 項** 的非同步流。
- **`Mono`**：表示一個可以發出 **0 或 1 項** 的非同步流。

這些是您用來反應式處理數據的基本構建塊。

---

### 3. 創建 Flux 或 Mono
您可以創建 `Flux` 或 `Mono` 的實例來表示您的數據流。

- **使用 Flux 的範例**（多項目）：
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **使用 Mono 的範例**（單項目）：
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

`just` 方法是從靜態值創建流的簡單方法，但 Reactor 提供了許多其他創建方法（例如，從數組、範圍或自定義來源）。

---

### 4. 訂閱以處理數據
要消費發出的項目，您需要訂閱 `Flux` 或 `Mono`。訂閱會觸發流開始發出數據。

- **訂閱 Flux**：
  ```java
  numbers.subscribe(System.out::println);  // 打印: 1, 2, 3, 4, 5
  ```

- **訂閱 Mono**：
  ```java
  greeting.subscribe(System.out::println); // 打印: Hello, World!
  ```

`subscribe` 方法還可以接受其他參數，例如錯誤處理程序或完成回調，以獲得更多控制。

---

### 5. 使用操作符轉換數據
Reactor 提供了一組豐富的操作符來操作流，例如 `map`、`filter` 等。

- **使用 Flux 和 map 的範例**：
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // 打印: 2, 4, 6, 8, 10
  ```

- **使用 Mono 和 map 的範例**：
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // 打印: HELLO, WORLD!
  ```

這些操作符允許您以聲明方式轉換、篩選或組合數據。

---

### 6. 處理錯誤和反壓
Reactor-core 支持錯誤處理和反壓管理：
- **錯誤處理**：使用帶有錯誤消費者的 `subscribe`：
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // 打印: Oops!
  ```
- **反壓**：使用操作符如 `onBackpressureBuffer()` 或 `onBackpressureDrop()` 來控制訂閱者如何處理過多的數據流。

---

### 7. 進一步探索
要進行更高級的使用：
- 查看 [官方 Reactor 文檔](https://projectreactor.io/docs/core/release/reference/) 以獲取詳細範例和教程。
- 查看 [reactor-core GitHub 存儲庫](https://github.com/reactor/reactor-core) 以獲取其他資源。

---

### 摘要
要使用 **reactor-core**：
1. 將其作為項目的依賴項添加。
2. 使用 `Flux` 來處理多項目或 `Mono` 來處理單項目。
3. 使用方法如 `just` 創建流。
4. 訂閱以處理數據。
5. 根據需要應用操作符來轉換流。

這是使用 reactor-core 進行反應式編程的初學者友好入門。通過小範例進行實驗，以熟悉其反應式範式！