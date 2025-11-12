---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおけるリアクティブプログラミング
translated: true
type: note
---

**reactor-core** を使用するには、Reactive Streams 仕様に基づいたノンブロッキングな非同期アプリケーションを構築するための Java ライブラリです。以下の手順に従ってください。

---

### 1. reactor-core を依存関係に追加する
まず、プロジェクトに **reactor-core** を含めます。使用するビルドツールに応じて:

- **Maven**: `pom.xml` に以下を追加:
  ```xml
  <dependency>
    <groupId>io.projectreactor</groupId>
    <artifactId>reactor-core</artifactId>
    <version>3.7.3</version>
  </dependency>
  ```

- **Gradle**: `build.gradle` に以下を追加:
  ```groovy
  implementation 'io.projectreactor:reactor-core:3.7.3'
  ```

これにより、ライブラリがプロジェクトで利用可能になります。必要に応じて [Maven Central](https://central.sonatype.com/artifact/io.projectreactor/reactor-core) で最新バージョンを確認してください。

---

### 2. コアコンポーネントを理解する
Reactor-core はリアクティブプログラミングのために、主に2つのクラスを提供します:
- **`Flux`**: **0 から N 個のアイテム**を発行できる非同期ストリームを表します。
- **`Mono`**: **0 または 1 個のアイテム**を発行する非同期ストリームを表します。

これらは、データをリアクティブに扱うために使用する構成要素です。

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

`just` メソッドは静的な値からストリームを作成する簡単な方法ですが、Reactor は他にも多くの作成メソッド (例: 配列、範囲、カスタムソースから) を提供しています。

---

### 4. データを処理するために Subscribe する
発行されたアイテムを消費するには、`Flux` または `Mono` を **subscribe** する必要があります。Subscribe することで、ストリームがデータの発行を開始します。

- **Flux を Subscribe**:
  ```java
  numbers.subscribe(System.out::println);  // 出力: 1, 2, 3, 4, 5
  ```

- **Mono を Subscribe**:
  ```java
  greeting.subscribe(System.out::println); // 出力: Hello, World!
  ```

`subscribe` メソッドは、より制御するためのエラーハンドラーや完了コールバックなどの追加引数を取ることもできます。

---

### 5. オペレーターでデータを変換する
Reactor は、`map`、`filter` などのストリームを操作するための豊富なオペレーターセットを提供します。

- **Flux と map の例**:
  ```java
  numbers.map(n -> n * 2).subscribe(System.out::println);  // 出力: 2, 4, 6, 8, 10
  ```

- **Mono と map の例**:
  ```java
  greeting.map(s -> s.toUpperCase()).subscribe(System.out::println); // 出力: HELLO, WORLD!
  ```

これらのオペレーターを使用して、データを宣言的に変換、フィルタリング、結合できます。

---

### 6. エラーとバックプレッシャーを処理する
Reactor-core はエラーハンドリングとバックプレッシャー管理をサポートしています:
- **エラーハンドリング**: エラーコンシューマーを指定して `subscribe` を使用:
  ```java
  Flux.error(new RuntimeException("Oops!"))
      .subscribe(System.out::println, error -> System.err.println(error.getMessage()));
  // 出力: Oops!
  ```
- **バックプレッシャー**: `onBackpressureBuffer()` や `onBackpressureDrop()` などのオペレーターを使用して、サブスクライバーが圧倒的なデータストリームをどのように処理するかを制御します。

---

### 7. さらに探求する
より高度な使用方法については:
- 詳細な例とチュートリアルは [公式 Reactor ドキュメント](https://projectreactor.io/docs/core/release/reference/) を確認してください。
- 追加のリソースについては [reactor-core GitHub リポジトリ](https://github.com/reactor/reactor-core) を参照してください。

---

### まとめ
**reactor-core** を使用するには:
1. プロジェクトの依存関係として追加します。
2. 複数のアイテムには `Flux` を、単一のアイテムには `Mono` を使用します。
3. `just` のようなメソッドでストリームを作成します。
4. データを処理するために Subscribe します。
5. 必要に応じてストリームを変換するためにオペレーターを適用します。

これは、reactor-core を使ったリアクティブプログラミングの初心者向けの出発点です。そのリアクティブなパラダイムに慣れるために、小さな例で実験してみてください！