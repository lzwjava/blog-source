---
audio: false
generated: true
lang: ja
layout: post
title: ポイントカット式の理解
translated: true
type: note
---

AspectJ のポイントカット式、特に `execution` の使用方法、ワイルドカードの使い方、クラス名のマッチング（プレフィックス/サフィックス）、そして `@AfterReturning` のような他のアドバイスタイプについて包括的なガイドを求めているようですね。順を追って説明していきましょう。

### Spring AOP (AspectJ 構文) におけるポイントカット式の理解

Spring AOP は、アドバイス (`@Before`, `@AfterReturning` など) を *どこに* 適用すべきかを決定するために AspectJ のポイントカット式を使用します。ご質問の核心は、最も一般的に使用されるポイントカット指定子である `execution` を中心に展開されています。

#### `execution` ポイントカット指定子

`execution` ポイントカット指定子は、メソッドの実行をマッチングします。その一般的な構文は以下の通りです：

`execution(修飾子パターン? 戻り値型パターン 宣言型パターン?名前パターン(パラメータパターン) 例外パターン?)`

各構成要素を分解してみましょう：

*   **`修飾子パターン?`**: オプション。メソッドの修飾子をマッチングします (例: `public`, `private`, `protected`)。
*   **`戻り値型パターン`**: 必須。メソッドの戻り値の型をマッチングします。
*   **`宣言型パターン?`**: オプション。メソッドが宣言されている完全修飾クラス名をマッチングします。
*   **`名前パターン`**: 必須。メソッドの名前をマッチングします。
*   **`パラメータパターン`**: 必須。メソッドのパラメータをマッチングします。
*   **`例外パターン?`**: オプション。メソッドがスローする例外をマッチングします。

#### あなたの例: `@Before("execution(* com.example.service.*.*(..))")`

与えられた例を分析してみましょう：

*   `@Before`: これはアドバイスアノテーションであり、アノテーションが付けられたメソッドがマッチした結合ポイントの*前に*実行されることを意味します。
*   `execution()`: ポイントカット指定子。
*   `*`: 任意の戻り値の型にマッチします。
*   `com.example.service.*.*`:
    *   `com.example.service`: パッケージ `com.example.service` にマッチします。
    *   `.*`: `service` の後の最初の `*` は、`com.example.service` パッケージ内の任意のクラスにマッチします。
    *   `.`: パッケージ/クラスとメソッドの間の区切り文字。
    *   `*`: 2番目の `*` は、それらのクラス内の任意のメソッド名にマッチします。
*   `(..)`: 任意の数のパラメータ（0個以上、任意の型）にマッチします。

**平易な言葉で説明すると:** このポイントカットは、`com.example.service` パッケージ内の*任意のクラス*の*任意のメソッド*の実行にマッチします（およびその直接のサブパッケージ、もし `com.example.service` に直接クラスがある場合）。

---

### ポイントカット式におけるワイルドカード

ワイルドカードは、柔軟なポイントカット式を作成するために不可欠です。

*   **`*` (単一のアスタリスク)**:
    *   名前パターン内の任意の単一の要素にマッチします（例：任意の戻り値型、任意のクラス名、任意のメソッド名）。
    *   パッケージ名内の任意の単一のセグメントにマッチします（例：`com.example.*.service` は `com.example.foo.service` にマッチします）。
*   **`..` (二重ドット)**:
    *   **パッケージパターン内**: パッケージ名内の0個以上のセグメントにマッチします。
        *   `com.example..service`: `com.example.service`, `com.example.foo.service`, `com.example.foo.bar.service` などにマッチします。
    *   **パラメータパターン内**: 任意の型の0個以上の引数にマッチします。
        *   `(..)`: 任意の数の引数にマッチします。
        *   `(java.lang.String, ..)`: 最初の引数が `String` で、その後に任意の数の他の引数が続くメソッドにマッチします。
        *   `(.., java.lang.Long)`: 任意の数の初期引数があり、最後が `Long` で終わるメソッドにマッチします。

---

### クラス名のマッチング

#### 1. サフィックスによるクラス名のマッチング

特定のサフィックスで終わるクラスにマッチさせるには、サフィックスの前にワイルドカードを配置します。

**例: `ServiceImpl` で終わるすべてのクラスにマッチ**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

*   `*ServiceImpl`: `ServiceImpl` で終わる任意のクラス名にマッチします。

**例: `com.example.web` の任意のサブパッケージ内で `Controller` で終わるすべてのクラスにマッチ**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

*   `com.example.web..`: `com.example.web` およびその任意のサブパッケージにマッチします。
*   `*Controller`: `Controller` で終わる任意のクラス名にマッチします。

#### 2. プレフィックスによるクラス名のマッチング

特定のプレフィックスで始まるクラスにマッチさせるには、プレフィックスの後にワイルドカードを配置します。

**例: `User` で始まるすべてのクラスにマッチ**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

*   `User*`: `User` で始まる任意のクラス名にマッチします。

**例: `com.example.admin` パッケージ内で `Admin` で始まるすべてのクラスにマッチ**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. 特定のクラス名とのマッチング (完全一致)

完全一致の場合はワイルドカードは必要ありません。

**例: `com.example.service.UserServiceImpl` 内のメソッドのみにマッチ**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### 様々な種類のポイントカット指定子

`execution` が最も一般的ですが、AspectJ は結合ポイントを指定するためにいくつかの他のポイントカット指定子を提供しています。これらは論理演算子 (`and`, `or`, `not` または `&&`, `||`, `!`) を使用して組み合わせることができます。

以下に最も重要なものを示します：

1.  **`execution()`**: 前述の通り、メソッドの実行にマッチします。
    *   例: `@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`**: コードが特定の型（クラス）内にある結合ポイントにマッチします。これは、他のポイントカットのスコープを制限するためによく使用されます。
    *   例: `@Before("within(com.example.service.*) && execution(* *(..))")`
        *   これは `within` と `execution` を組み合わせています。「`com.example.service` パッケージ内の任意のクラス内での任意のメソッド実行」を意味します。`execution` の部分は、`within` がクラスのマッチングを処理するため、任意のメソッドに対するワイルドカードとなります。

3.  **`this()`**: プロキシ*自体*が指定された型のインスタンスである結合ポイントにマッチします。これは、単純なアドバイスにはあまり使用されず、導入 (Introduction) や自己呼び出しの問題により使用されます。
    *   例: `@Around("this(com.example.service.UserService)")`
        *   AOP プロキシが `UserService` を実装している場合にマッチします。

4.  **`target()`**: *ターゲットオブジェクト*（アドバイスされている実際のオブジェクト、プロキシではない）が指定された型のインスタンスである結合ポイントにマッチします。これは、基盤となる実装を気にする場合、`this()` よりも直感的であることが多いです。
    *   例: `@Around("target(com.example.service.UserServiceImpl)")`
        *   ターゲットオブジェクトが `UserServiceImpl` のインスタンスである場合にマッチします。

5.  **`args()`**: 引数が特定の型であるか、特定のパターンにマッチする結合ポイントにマッチします。
    *   例: `@Before("execution(* com.example.service.*.*(String, ..))")`
        *   最初の引数が `String` であるメソッドにマッチします。
    *   例: `@Before("args(java.lang.String, int)")`
        *   正確に `String` の後に `int` が続くメソッドにマッチします。
    *   例: `@Before("args(name, age)")` ここで `name` と `age` は、その後アドバイスメソッドのパラメータにバインドできます。

6.  **`bean()`**: (Spring 固有) 特定の名前または名前パターンを持つ Spring Bean 上で実行されるメソッドにマッチします。
    *   例: `@Before("bean(userService) && execution(* *(..))")`
        *   "userService" という名前の Spring Bean 上の任意のメソッド実行にマッチします。
    *   例: `@Before("bean(*Service) && execution(* *(..))")`
        *   名前が "Service" で終わる Spring Bean 上の任意のメソッド実行にマッチします。

7.  **`@annotation()`**: ターゲットメソッド（または `within` の場合はクラス）が特定のアノテーションで注釈されている結合ポイントにマッチします。
    *   例: `@Before("@annotation(com.example.annotation.Loggable)")`
        *   `@Loggable` で注釈されている任意のメソッドにマッチします。
    *   例: `@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        *   `@Transactional` で注釈されている任意のメソッド実行にマッチします。

8.  **`@within()`**: 宣言型（クラス）が特定のアノテーションで注釈されている結合ポイントにマッチします。
    *   例: `@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        *   `@Service` で注釈されているクラス内の任意のメソッド実行にマッチします。

9.  **`@target()`**: ターゲットオブジェクトのクラスが指定されたアノテーションを持っている結合ポイントにマッチします。
    *   例: `@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`**: メソッドに渡された実際の引数の実行時型が、指定された型のアノテーションを持っている結合ポイントにマッチします。
    *   例: `@Before("@args(com.example.annotation.ValidInput)")`

---

### アドバイスの種類 (アノテーション)

`@AfterReturning` と「アノテーションで使用できる他のもの」について言及されています。Spring AOP は、結合ポイントのライフサイクルの異なる時点で実行されるいくつかのアドバイスタイプを提供します：

1.  **`@Before`**:
    *   マッチしたメソッド実行の*前に*実行されます。
    *   例: サービスメソッドが実行される前にリクエストの詳細をログに記録する。
    *   メソッドの実行を防いだり、その戻り値を変更したりすることはできません。

2.  **`@AfterReturning`**:
    *   マッチしたメソッドが*正常に*戻った後（例外をスローせずに）実行されます。
    *   メソッドの戻り値にアクセスできます。
    *   構文: `@AfterReturning(pointcut="yourPointcut()", returning="result")`
    *   例:
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("User retrieved: " + user);
        }
        ```
        *注: `returning` 属性名（この場合は `user`）は、アドバイスメソッドのパラメータ名と一致しなければなりません。*

3.  **`@AfterThrowing`**:
    *   マッチしたメソッドが例外をスローした*後に*実行されます。
    *   スローされた例外にアクセスできます。
    *   構文: `@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    *   例:
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Exception occurred: " + ex.getMessage());
        }
        ```
        *注: `throwing` 属性名（この場合は `ex`）は、アドバイスメソッドのパラメータ名と一致しなければなりません。*

4.  **`@After` (finally アドバイス)**:
    *   マッチしたメソッドが完了した*後に*、正常に戻ったか例外をスローしたかに関わらず実行されます。
    *   `finally` ブロックに似ています。
    *   例: メソッドの結果に関係なくリソースを解放する。
    *   ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Order process completed (cleanup)");
        }
        ```

5.  **`@Around`**:
    *   最も強力で柔軟なアドバイスタイプです。
    *   マッチしたメソッド実行を*囲むように*実行されます。
    *   `ProceedingJoinPoint.proceed()` を使用して実際のメソッドを呼び出す責任があります。
    *   メソッドの引数と戻り値を検査、変更、または抑制することさえできます。
    *   アドバイスされたメソッドによってスローされた例外をキャッチして処理できます。
    *   例: パフォーマンス監視、トランザクション管理、キャッシング。
    *   ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // 元のメソッドを実行
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " executed in " + (end - start) + "ms");
                return result;
            }
        }
        ```

### 再利用可能なポイントカットの定義

可読性と再利用性を高めるために、`@Pointcut` を使用して名前付きポイントカットを定義できます。

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // com.example.service パッケージ内のすべてのメソッドに対するポイントカットを定義
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // User オブジェクトを返すメソッドに対するポイントカットを定義
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // 定義されたポイントカットを使用
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Before service method execution.");
    }

    // 論理 AND でポイントカットを結合
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("Service method returned user: " + user);
    }

    // 引数付きでポイントカットを定義することも可能
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Saving entity: " + entity);
    }
}
```

この包括的なガイドは、ポイントカット式、ワイルドカードの使用法、クラス名のマッチング、および Spring AOP における様々なアドバイスタイプの基本をカバーしています。これらの概念をマスターすることで、横断的関心事を適用する場所とタイミングを正確に制御できるようになります。