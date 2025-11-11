---
audio: false
generated: true
lang: ja
layout: post
title: アスペクトJによる循環依存の解決
translated: true
type: note
---

あなたのシナリオにおける循環依存は、`BlogConfig`、`BlogCore`、`BlogWeb` が互いに参照し合うことで発生し、依存関係のループを形成しています。さらに、`BlogCore`（または`BlogWeb`）内の AspectJ `LoggingAspect` が、`BlogCore` に依存する `BlogConfig` を含むモジュール全体のメソッドに適用される場合、この問題を悪化させる可能性があります。これを分解し、AspectJ の機能を維持しながら循環依存を解決する方法を説明します。

### 問題分析
1. **モジュール依存関係**:
   - `BlogCore` は `BlogConfig` に依存
   - `BlogWeb` は `BlogCore` と `BlogConfig` の両方に依存
   - `BlogConfig` は `BlogCore` に依存（これが循環依存を生み出す: `BlogCore` ↔ `BlogConfig`）
   - `BlogWeb` の両モジュールへの依存が、循環依存を取り込む可能性がある

2. **AspectJ LoggingAspect**:
   - `BlogCore`（または `BlogWeb`）内の `LoggingAspect` は広範なポイントカット（`execution(* *(..))`）を使用し、`BlogConfig`、`BlogCore`、`BlogWeb` を含むアプリケーションコンテキスト内のすべてのメソッド実行に適用される
   - `LoggingAspect` が `BlogCore` に存在し、`BlogConfig` に織り込まれ、かつ `BlogConfig` が `BlogCore` に依存する場合、AspectJ のウィービングプロセスが初期化時の循環依存を複雑にする可能性がある

3. **循環依存の影響**:
   - Maven や Gradle などのビルドシステムでは、モジュール間の循環依存がコンパイルまたはランタイムの問題（Spring 使用時の `BeanCurrentlyInCreationException` やクラスローディング問題など）を引き起こす可能性がある
   - AspectJ のコンパイル時またはロード時ウィービングが、`BlogConfig` と `BlogCore` のクラスが相互依存して完全に初期化されていない場合、失敗または予期しない動作を引き起こす可能性がある

### 解決策
循環依存を解決し、AspectJ `LoggingAspect` が正しく機能することを確保するには、以下の手順に従ってください。

#### 1. 循環依存の解消
主な問題は `BlogCore` ↔ `BlogConfig` の依存関係です。これを修正するには、`BlogConfig` が `BlogCore` に依存する原因となる共有機能または設定を新しいモジュールに抽出するか、依存関係をリファクタリングします。

**オプションA: 新しいモジュール（`BlogCommon`）の導入**
- `BlogCore` と `BlogConfig` の両方が必要とする共有インターフェース、設定、またはユーティリティを保持する新しいモジュール `BlogCommon` を作成
- `BlogConfig` が依存する `BlogCore` の部分（インターフェース、定数、共有サービスなど）を `BlogCommon` に移動
- 依存関係を更新:
  - `BlogConfig` は `BlogCommon` に依存
  - `BlogCore` は `BlogCommon` と `BlogConfig` に依存
  - `BlogWeb` は `BlogCore` と `BlogConfig` に依存

**依存関係構造の例**:
```
BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
```

**実装**:
- `BlogCommon` でインターフェースまたは共有コンポーネントを定義:
  ```java
  // BlogCommon モジュール
  public interface BlogService {
      void performAction();
  }
  ```
- `BlogCore` でインターフェースを実装:
  ```java
  // BlogCore モジュール
  public class BlogCoreService implements BlogService {
      public void performAction() { /* ロジック */ }
  }
  ```
- `BlogConfig` で `BlogCommon` のインターフェースを使用:
  ```java
  // BlogConfig モジュール
  import com.example.blogcommon.BlogService;
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- `BlogWeb` では必要に応じて両モジュールを使用

これにより、`BlogConfig` が `BlogCore` に直接依存しなくなり、循環依存が解消されます。

**オプションB: 依存性注入による制御の反転（IoC）**
- Spring のようなフレームワークを使用している場合、`BlogConfig` が具象クラスではなく `BlogCore` で定義された抽象（インターフェース）に依存するようにリファクタリング
- 依存性注入を使用して、`BlogCore` の実装を実行時に `BlogConfig` に提供し、コンパイル時の循環依存を回避
- 例:
  ```java
  // BlogCore モジュール
  public interface BlogService {
      void performAction();
  }
  @Component
  public class BlogCoreService implements BlogService {
      public void performAction() { /* ロジック */ }
  }

  // BlogConfig モジュール
  @Configuration
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- Spring の IoC コンテナが実行時に依存関係を解決し、コンパイル時の循環性を解消

#### 2. AspectJ 設定の調整
`LoggingAspect` の広範なポイントカット（`execution(* *(..))`）は、`BlogConfig` を含むすべてのモジュールに適用される可能性があり、初期化を複雑にする可能性があります。アスペクトをより管理しやすくし、ウィービングの問題を回避するには:

- **ポイントカットの絞り込み**: アスペクトを特定のパッケージやモジュールに制限し、`BlogConfig` や他のインフラストラクチャコードへの適用を回避
  ```java
  import org.aspectj.lang.JoinPoint;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import java.util.Arrays;

  @Aspect
  public class LoggingAspect {
      @After("execution(* com.example.blogcore..*(..)) || execution(* com.example.blogweb..*(..))")
      public void logAfter(JoinPoint joinPoint) {
          System.out.println("実行されたメソッド: " + joinPoint.getSignature());
          System.out.println("引数: " + Arrays.toString(joinPoint.getArgs()));
      }
  }
  ```
  このポイントカットは `BlogCore`（`com.example.blogcore`）と `BlogWeb`（`com.example.blogweb`）のメソッドにのみ適用され、`BlogConfig` は除外されます

- **アスペクトの別モジュールへの移動**: モジュール初期化時のウィービング問題を回避するため、`LoggingAspect` を新しいモジュール（例: `BlogAspects`）に配置し、`BlogConfig` には依存しないようにする
  - 依存関係構造:
    ```
    BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
                       ↑          ↑
                       └─ BlogAspects ─┘
    ```
  - ビルド設定を更新し、`BlogAspects` が `BlogCore` と `BlogWeb` の後に織り込まれることを確保

- **ロード時ウィービング（LTW）の使用**: コンパイル時ウィービングが循環依存により問題を引き起こす場合、AspectJ のロード時ウィービングに切り替え。アプリケーションで LTW を設定（Spring の `@EnableLoadTimeWeaving` や `aop.xml` ファイル経由）し、クラスがロードされた後の実行時までアスペクト適用を延期

#### 3. ビルド設定の更新
ビルドツール（Maven、Gradle など）が新しいモジュール構造を反映し、依存関係を正しく解決することを確保

**Maven の例**:
```xml
<!-- BlogCommon/pom.xml -->
<dependencies>
    <!-- 依存関係なし -->
</dependencies>

<!-- BlogConfig/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogCore/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogWeb/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogAspects/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogWeb</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>org.aspectj</groupId>
        <artifactId>aspectjrt</artifactId>
        <version>1.9.7</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>aspectj-maven-plugin</artifactId>
            <version>1.14.0</version>
            <configuration>
                <complianceLevel>11</complianceLevel>
                <source>11</source>
                <target>11</target>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>compile</goal>
                        <goal>test-compile</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

**Gradle の例**:
```groovy
// BlogCommon/build.gradle
dependencies {
    // 依存関係なし
}

// BlogConfig/build.gradle
dependencies {
    implementation project(':BlogCommon')
}

// BlogCore/build.gradle
dependencies {
    implementation project(':BlogCommon')
    implementation project(':BlogConfig')
}

// BlogWeb/build.gradle
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogConfig')
}

// BlogAspects/build.gradle
plugins {
    id 'java'
    id 'io.freefair.aspectj.post-compile-weaving' version '6.5.1'
}
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogWeb')
    implementation 'org.aspectj:aspectjrt:1.9.7'
}
```

#### 4. アプリケーションのテスト
- アプリケーションをビルドして実行し、循環依存が解決されたことを確認
- `LoggingAspect` が `BlogCore` と `BlogWeb` のメソッド実行をログに記録するが、`BlogConfig` では記録しないことを確認（明示的に望まない限り）
- Spring を使用している場合、コンテキスト初期化時の `BeanCurrentlyInCreationException` や類似のエラーをチェック
- AspectJ ウィービングをテストし、正しいメソッドに対してログが表示されることを確認

#### 5. 追加のヒント
- **依存関係分析ツールの使用**: Maven の `mvn dependency:tree` や Gradle の `dependencies` タスクなどのツールを使用して、残存する循環依存を検出
- **アスペクトの粒度を考慮**: ロギングが特定のサービスのみに必要な場合、ポイントカットをさらに絞り込み、特定のクラスやメソッドを対象にする（例: `execution(* com.example.blogcore.service.*.*(..))`）
- **設定モジュールへの AspectJ 使用回避**: 一般に、設定やインフラストラクチャコード（`BlogConfig` など）へのアスペクト適用は避け、複雑さを軽減

### 最終的な依存関係構造
リファクタリング後:
```
BlogCommon → BlogConfig → BlogCore → BlogWeb
   ↑                        ↑
   └────── BlogAspects ─────┘
```

### この解決策が有効な理由
- **循環の解消**: 共有依存関係を `BlogCommon` に移動するか、IoC を使用することで、`BlogConfig` が `BlogCore` に依存しなくなり、循環依存が解消
- **アスペクトの分離**: `LoggingAspect` を別モジュール（`BlogAspects`）に配置するか、ポイントカットを絞り込むことで、ウィービングの問題を防止し、アスペクトロジックを依存関係チェーンから独立させることができる
- **ビルド設定**: 適切なビルドツールの設定により、モジュールが正しい順序でコンパイルおよび織り込まれることを確保

このアプローチにより、AspectJ ロギング機能を維持しながら、クリーンで保守可能なモジュール構造を実現できます。設定（Spring の使用状況、循環を引き起こす特定のクラスなど）に関する追加の詳細があれば、さらに解決策を洗練できます！