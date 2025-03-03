---
audio: false
generated: true
lang: ja
layout: post
title: リアクティブプログラミングのJava
translated: true
---

**reactor-core** を使用するための Java ライブラリは、Reactive Streams 仕様に基づいた非同期、非ブロッキングアプリケーションを構築するためのものです。以下の手順に従ってください。

---

### 1. reactor-core を依存関係として追加
まず、プロジェクトに **reactor-core** を含めます。ビルドツールによっては異なります。

- **Maven**: `pom.xml` にこれを追加します:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: `build.gradle` にこれを追加します:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

これにより、ライブラリがプロジェクトで利用可能になります。最新バージョンは必要に応じて [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) で確認してください。

---

### 2. 主要なコンポーネントを理解する
Reactor-core は、反応型プログラミングのための 2 つの主要なクラスを提供します:
- **`Flux`**: 0 から N 個のアイテムを発信する非同期ストリームを表します。
- **`Mono`**: 0 または 1 個のアイテムを発信する非同期ストリームを表します。

これらが、データを反応的に処理するための基本的な構成要素です。

---

### 3. Flux または Mono を作成する
データストリームを表す `Flux` または `Mono` のインスタンスを作成できます。

- **Flux の例** (複数のアイテム):
  ```java
  Flux<Integer> numbers = Flux.just(1, 2, 3, 4, 5);
  ```

- **Mono の例** (単一のアイテム):
  ```java
  Mono<String> greeting = Mono.just("Hello, World!");
  ```

`just` メソッドは、静的な値からストリームを作成する簡単な方法ですが、Reactor は他にも多くの作成方法（例：配列、範囲、またはカスタムソースから）を提供しています。

---

### 4. データを処理するためにサブスクライブ
発信されたアイテムを消費するには、`Flux` または `Mono` に **サブスクライブ** する必要があります。サブスクライブすることで、ストリームがデータの発信を開始します。

- **Flux にサブスクライブ**:
  ```java
  numbers.subscribe(System.out::println);  // 出力: 1, 2, 3, 4, 5
  ```

- **Mono にサブスクライブ**:
  ```java
  greeting.subscribe(System.out::println); // 出力: Hello, World!
  ```

`subscribe` メソッドには、エラーハンドラーや完了コールバックなど、より多くの制御を提供する追加の引数を取ることができます。

---

### 5. オペレータを使用してデータを変換する
Reactor は、`map`、`filter` など、ストリームを操作するための豊富なオペレータセットを提供しています。

- **Flux と map の例**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // 出力: 2, 4, 6, 8, 10
  ```

- **Mono と map の例**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // 出力: HELLO, WORLD!
  ```

これらのオペレータは、宣言的な方法でデータを変換、フィルタリング、または結合することができます。

---

### 6. エラーとバックプレッシャーを処理する
Reactor-core は、エラー処理とバックプレッシャー管理をサポートしています:
- **エラー処理**: エラーコンシューマを使用して `subscribe` します:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // 出力: Oops!
  ```
- **バックプレッシャー**: `onBackpressureBuffer()` または `onBackpressureDrop()` などのオペレータを使用して、サブスクライバーが圧倒的なデータストリームを処理する方法を制御します。

---

### 7. さらに探求する
より高度な使用方法については:
- [公式 Reactor ドキュメント](https://projectreactor.io/docs/core/release/reference/) を確認して、詳細な例やチュートリアルを確認してください。
- [reactor-core GitHub リポジトリ](https://github.com/reactor/reactor-core) を確認して、追加のリソースを確認してください。

---

### 要約
**reactor-core** を使用するには:
1. プロジェクトに依存関係として追加します。
2. 複数のアイテムには `Flux` を、単一のアイテムには `Mono` を使用します。
3. `just` などのメソッドを使用してストリームを作成します。
4. データを処理するためにサブスクライブします。
5. 必要に応じてオペレータを適用してストリームを変換します。

これは、reactor-core を使用した反応型プログラミングの初心者向けのスターティングポイントです。小さな例で実験して、その反応型パラダイムに慣れてください!