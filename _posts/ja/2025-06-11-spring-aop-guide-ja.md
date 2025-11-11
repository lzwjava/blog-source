---
audio: false
generated: true
lang: ja
layout: post
title: Spring AOPガイド
translated: true
type: note
---

## 1. Spring AOPの概要

Spring AOP（Aspect-Oriented Programming）はSpring Frameworkの主要コンポーネントであり、ビジネスロジックとは別に横断的関心事（ロギング、セキュリティ、トランザクション管理など）を実装する方法を提供します。

### 主要コンセプト：
- **横断的関心事（Cross-cutting concerns）**: 複数のレイヤーにまたがる機能（ロギング、セキュリティなど）
- **アスペクト（Aspect）**: 複数のクラスにまたがる関心事のモジュール化
- **結合点（Join point）**: プログラム実行中のポイント（メソッド実行、例外処理など）
- **アドバイス（Advice）**: 特定の結合点でアスペクトによって実行されるアクション
- **ポイントカット（Pointcut）**: 結合点をマッチングする述語
- **ウィービング（Weaving）**: アスペクトを他のアプリケーションタイプとリンクしてアドバイスされたオブジェクトを作成する処理

## 2. Spring AOP vs AspectJ

| 機能               | Spring AOP | AspectJ |
|-----------------------|-----------|---------|
| 実装方式        | ランタイムプロキシ | コンパイル時/ロード時ウィービング |
| パフォーマンス           | 遅い | 速い |
| サポートされる結合点 | メソッド実行のみ | すべて（メソッド、コンストラクタ、フィールドアクセスなど） |
| 複雑さ            | シンプル | より複雑 |
| 依存関係            | 追加の依存関係なし | AspectJコンパイラ/ウィーバーが必要 |

## 3. コアAOPコンポーネント

### 3.1 アスペクト
`@Aspect`で注釈されたクラスで、アドバイスとポイントカットを含みます。

```java
@Aspect
@Component
public class LoggingAspect {
    // アドバイスとポイントカットをここに記述
}
```

### 3.2 アドバイスの種類

1. **Before**: 結合点の前に実行
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("メソッド実行前");
   }
   ```

2. **AfterReturning**: 結合点が正常に完了した後に実行
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("メソッド戻り値: " + result);
   }
   ```

3. **AfterThrowing**: メソッドが例外をスローして終了した場合に実行
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("スローされた例外: " + ex.getMessage());
   }
   ```

4. **After (Finally)**: 結果に関係なく結合点の後に実行
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("メソッド実行後（finally）");
   }
   ```

5. **Around**: 結合点をラップする、最も強力なアドバイス
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("処理前");
       Object result = joinPoint.proceed();
       System.out.println("処理後");
       return result;
   }
   ```

### 3.3 ポイントカット式

ポイントカットは、式を使用してアドバイスを適用する場所を定義します：

- **Execution**: メソッド実行にマッチ
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **Within**: 特定のタイプ内のすべての結合点にマッチ
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **this**: 指定されたタイプのインスタンスであるBeanにマッチ
- **target**: 指定されたタイプに代入可能なBeanにマッチ
- **args**: 特定の引数タイプを持つメソッドにマッチ
- **@annotation**: 特定の注釈を持つメソッドにマッチ

### 3.4 ポイントカットの結合

ポイントカットは論理演算子を使用して結合できます：
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. 実装手順

### 4.1 セットアップ

1. Spring AOP依存関係を追加（Spring Bootを使用しない場合）：
   ```xml
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-aop</artifactId>
       <version>${spring.version}</version>
   </dependency>
   <dependency>
       <groupId>org.aspectj</groupId>
       <artifactId>aspectjweaver</artifactId>
       <version>${aspectj.version}</version>
   </dependency>
   ```

2. Spring Bootの場合、`spring-boot-starter-aop`を含める：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. 設定でAOPを有効化：
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 アスペクトの作成

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("開始: {}.{}() 引数 = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("終了: {}.{}() 結果 = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} の実行時間: {} ms", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 カスタム注釈

特定のAOP動作のためにメソッドをマークするカスタム注釈を作成：

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

メソッドで使用：
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // 実装
    }
}
```

## 5. 高度なトピック

### 5.1 アスペクトの順序制御

`@Order`でアスペクトの実行順序を制御：
```java
@Aspect
@Component
@Order(1)
public class LoggingAspect {
    // ...
}

@Aspect
@Component
@Order(2)
public class ValidationAspect {
    // ...
}
```

### 5.2 メソッド情報へのアクセス

アドバイスメソッドで以下にアクセス可能：
- `JoinPoint`（Before、After、AfterReturning、AfterThrowing用）
- `ProceedingJoinPoint`（Around用）

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 例外処理

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // 例外のログ記録、アラート送信など
}
```

### 5.4 プロキシメカニズム

Spring AOPは2種類のプロキシを使用：
- **JDK動的プロキシ**: インターフェース用のデフォルト
- **CGLIBプロキシ**: インターフェースが利用できない場合に使用（`proxyTargetClass=true`で強制可能）

## 6. ベストプラクティス

1. **アスペクトは焦点を絞る**: 各アスペクトは1つの特定の横断的関心事を扱うべき
2. **意味のあるポイントカット名を使用**: コードの可読性を向上
3. **アスペクトでの高コスト操作を避ける**: マッチしたすべての結合点で実行される
4. **Aroundアドバイスには注意**: 意図的に実行を防ぐ場合を除き、常に`proceed()`を呼び出す
5. **アスペクトを十分にテスト**: アプリケーションの複数部分に影響する
6. **アスペクトを文書化**: 特に動作を大幅に変更する場合
7. **パフォーマンスを考慮**: 複雑なポイントカットや多数のアスペクトはパフォーマンスに影響する

## 7. 一般的なユースケース

1. **ロギング**: メソッドの開始/終了、パラメータ、戻り値
2. **パフォーマンス監視**: 実行時間の計測
3. **トランザクション管理**: （通常はSpringの`@Transactional`で処理）
4. **セキュリティ**: 認証チェック
5. **バリデーション**: パラメータ検証
6. **エラー処理**: 一貫した例外処理
7. **キャッシング**: メソッド結果のキャッシュ
8. **監査**: 誰がいつ何を呼び出したかを追跡

## 8. 制限事項

1. Spring管理Beanでのみ動作
2. メソッド実行結合点のみサポート
3. finalクラスやメソッドにはアドバイスできない
4. 自己呼び出し（クラス内のメソッドが同じクラスの別メソッドを呼び出す）はプロキシをバイパスする
5. AspectJと比較してポイントカット式が限定されている

## 9. トラブルシューティング

**問題**: アドバイスが実行されない
- BeanがSpring管理であることを確認
- ポイントカット式が意図したメソッドにマッチすることを確認
- `@EnableAspectJAutoProxy`が存在することを確認

**問題**: Aroundアドバイスが進行しない
- `ProceedingJoinPoint`で`proceed()`を呼び出すことを確認

**問題**: 不正なプロキシタイプ
- `@EnableAspectJAutoProxy(proxyTargetClass=true)`を使用してCGLIBを強制

## 10. 結論

Spring AOPは、アプリケーションで横断的関心事を実装するための強力でシンプルな方法を提供します。完全なAspectJと比較していくつかの制限はありますが、Springとシームレスに統合され、ほとんどの一般的なユースケースをカバーします。このガイドで概説されたパターンとベストプラクティスに従うことで、横断的関心事を効果的にモジュール化し、ビジネスロジックをクリーンで焦点の絞られた状態に保つことができます。

---

Spring AOPはAspectJのウィービング機能を使用しません（代わりにプロキシベースのAOPを使用します）が、いくつかの重要な理由で`aspectjweaver`依存関係が必要です：

### 1. **AspectJ注釈サポート**
Spring AOPは、アスペクトとアドバイスを定義するためにAspectJの**注釈**（`@Aspect`、`@Pointcut`、`@Before`、`@After`など）を使用します。これらの注釈は`aspectjweaver`ライブラリから提供されます。

- これがないと、`@Aspect`や他のAOP注釈を使用する際にコンパイルエラーが発生します。

### 2. **ポイントカット式言語**
Spring AOPは、アドバイスを適用する場所を定義するためにAspectJの**ポイントカット式言語**を借用しています（例：`execution(* com.example.service.*.*(..))`）。

- `aspectjweaver`はこれらの式のパーサーとマッチングロジックを提供します。

### 3. **追加の結合点サポート（限定）**
Spring AOPは**メソッド実行**結合点のみをサポートしますが（AspectJはコンストラクタ、フィールドアクセスなどをサポート）、依然としてAspectJの基盤となるポイントカットマッチングメカニズムに依存しています。

### 4. **ロード時ウィービング（オプション）**
Spring AOPで**ロード時ウィービング（LTW）**を使用する場合（稀ですが可能）、`aspectjweaver`が必要です。LTWはプロキシの代わりにクラスロード時にアスペクトを織り込むことを可能にします。

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **@EnableAspectJAutoProxyとの互換性**
`@EnableAspectJAutoProxy`を使用すると、Springは内部でAOP注釈を処理するためにAspectJのインフラストラクチャを使用します（完全なAspectJウィービングは行いませんが）。

---

### **常に必要ですか？**
- **Spring Boot（`spring-boot-starter-aop`）を使用する場合**: 不要、推移的に`aspectjweaver`を含むため
- **プレーンなSpring AOPを使用する場合**: はい、明示的に含める必要があります

### **代替手段？**
- **完全なAspectJ**（コンパイル時またはロード時ウィービング）を使用する場合、`aspectjrt`と`aspectjtools`も必要になります
- しかし**Spring AOP**の場合、`aspectjweaver`のみで十分です

### **結論**
Spring AOPは**プロキシベース**ですが、AspectJの注釈とポイントカット構文を**再利用する**ため、`aspectjweaver`が必要です。これはSpringのプロキシアプローチとAspectJのより強力なAOPモデルの間のギャップを埋める役割を果たします。