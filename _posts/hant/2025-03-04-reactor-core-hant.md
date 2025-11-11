---
audio: false
generated: true
lang: hant
layout: post
title: Java 響應式編程
translated: true
type: note
---

要使用 **reactor-core**（一個基於 Reactive Streams 規範、用於構建非阻塞異步應用程序的 Java 函式庫），請遵循以下步驟：

---

### 1. 添加 reactor-core 作為依賴項
首先，將 **reactor-core** 加入您的專案中。根據您的建置工具：

- **Maven**：將以下內容加入您的 `pom.xml`：
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**：將以下內容加入您的 `build.gradle`：
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

這確保函式庫在您的專案中可用。如有需要，請在 [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) 上查看最新版本。

---

### 2. 理解核心組件
Reactor-core 提供兩個主要類別用於響應式編程：
- **`Flux`**：代表一個能發出 **0 到 N 個項目**的異步流。
- **`Mono`**：代表一個能發出 **0 或 1 個項目**的異步流。

這些是您用於以響應式方式處理數據的基礎構建模塊。

---

### 3. 創建 Flux 或 Mono
您可以創建 `Flux` 或 `Mono` 的實例來代表您的數據流。

- **使用 Flux 的範例**（多個項目）：
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **使用 Mono 的範例**（單一項目）：
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

`just` 方法是從靜態值創建流的簡單方式，但 Reactor 還提供許多其他創建方法（例如從陣列、範圍或自訂來源創建）。

---

### 4. 訂閱以處理數據
要消費發出的項目，您需要**訂閱** `Flux` 或 `Mono`。訂閱會觸發流開始發送數據。

- **訂閱 Flux**：
  ```java
  numbers.subscribe(System.out::println);  // 輸出：1, 2, 3, 4, 5
  ```

- **訂閱 Mono**：
  ```java
  greeting.subscribe(System.out::println); // 輸出：Hello, World!
  ```

`subscribe` 方法也可以接受其他參數，例如錯誤處理程序或完成回調，以實現更精細的控制。

---

### 5. 使用運算子轉換數據
Reactor 提供豐富的運算子來操作流，例如 `map`、`filter` 等。

- **使用 Flux 和 map 的範例**：
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // 輸出：2, 4, 6, 8, 10
  ```

- **使用 Mono 和 map 的範例**：
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // 輸出：HELLO, WORLD!
  ```

這些運算子允許您以聲明式的方式轉換、過濾或合併數據。

---

### 6. 處理錯誤和背壓
Reactor-core 支援錯誤處理和背壓管理：
- **錯誤處理**：使用帶有錯誤消費者的 `subscribe`：
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // 輸出：Oops!
  ```
- **背壓**：使用如 `onBackpressureBuffer()` 或 `onBackpressureDrop()` 等運算子來控制訂閱者如何處理過載的數據流。

---

### 7. 進一步探索
如需更高階的用法：
- 查閱 [官方 Reactor 文檔](https://projectreactor.io/docs/core/release/reference/) 以獲取詳細範例和教程。
- 查看 [reactor-core GitHub 倉庫](https://github.com/reactor/reactor-core) 以獲取額外資源。

---

### 總結
要使用 **reactor-core**：
1. 將其作為依賴項加入您的專案。
2. 使用 `Flux` 處理多個項目，或使用 `Mono` 處理單一項目。
3. 使用如 `just` 等方法創建流。
4. 訂閱以處理數據。
5. 根據需要應用運算子來轉換流。

這是使用 reactor-core 進行響應式編程的初學者友好起點。通過小型範例進行實驗，以熟悉其響應式範式！