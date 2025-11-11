---
audio: false
generated: true
lang: ja
layout: post
title: Springにおける循環依存関係
translated: true
type: note
---

SpringまたはSpring Bootにおける循環依存は、2つ以上のBeanが初期化中に直接的または間接的にお互いに依存している状態で発生します。これにより、各Beanが互いに完全に初期化されることを要求するため、Springの依存性注入メカニズムが依存関係を解決できなくなる循環が生じます。この問題は通常、SpringアプリケーションコンテキストでのBean作成中に発生し、`BeanCurrentlyInCreationException`を引き起こします。

### 循環依存が発生する理由
Springは依存性注入コンテナ内でBeanを管理し、Beanは通常、依存関係に基づいて特定の順序で作成されます。Beanが循環的に互いを参照する場合（例：Bean AがBean Bに依存し、Bean BがBean Aに依存する）、Springは初期化中に無限ループに陥るため、それらをインスタンス化できません。これは、密結合されたコンポーネントを持つ複雑なアプリケーションで特に一般的です。

この問題は以下のシナリオで発生しやすくなります：
1. **コンストラクタインジェクション**: Beanがコンストラクタ経由で配線される場合、Springはインスタンス化時に依存関係を解決する必要があり、Beanが互いを参照すると循環性の問題が発生する可能性があります。
2. **フィールドまたはセッターインジェクションと即時初期化**: Beanが即時初期化される場合（シングルトンBeanのデフォルト動作）、Springは直ちに依存関係を解決しようとし、循環依存を露呈させます。
3. **設定ミスまたは過度に複雑なBean関係**: 不適切な設計や関心の分離の欠如は、意図しない循環を引き起こす可能性があります。
4. **`@Autowired`や`@Component`などのアノテーション**: 密結合されたコンポーネントでの自動依存性注入は、不注意で循環を作成する可能性があります。

### 循環依存の一般的な例

#### 例1: コンストラクタインジェクションの循環
```java
@Component
public class BeanA {
    private final BeanB beanB;

    @Autowired
    public BeanA(BeanB beanB) {
        this.beanB = beanB;
    }
}

@Component
public class BeanB {
    private final BeanA beanA;

    @Autowired
    public BeanB(BeanA beanA) {
        this.beanA = beanA;
    }
}
```
**問題**: `BeanA`はコンストラクタで`BeanB`を必要とし、`BeanB`はコンストラクタで`BeanA`を必要とします。Springは、各Beanが互いに最初に完全に初期化されることに依存するため、いずれのBeanも作成できません。

**エラー**: `BeanCurrentlyInCreationException: Error creating bean with name 'beanA': Requested bean is currently in creation: Is there an unresolvable circular reference?`

#### 例2: フィールドインジェクションの循環
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanA beanA;
}
```
**問題**: `BeanA`と`BeanB`の両方が`@Autowired`を使用してフィールド経由で互いを注入します。フィールドインジェクションはコンストラクタインジェクションよりも柔軟ですが、両方がシングルトンBean（デフォルトスコープ）の場合、Springは依然としてBean初期化中に循環を検出します。

#### 例3: 間接的な循環依存
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanC beanC;
}

@Component
public class BeanC {
    @Autowired
    private BeanA beanA;
}
```
**問題**: `BeanA`は`BeanB`に依存し、`BeanB`は`BeanC`に依存し、`BeanC`は`BeanA`に依存し、循環を形成します。この間接的な依存関係は発見しにくいですが、同じ問題を引き起こします。

#### 例4: 循環参照を持つ`@Configuration`クラス
```java
@Configuration
public class ConfigA {
    @Autowired
    private ConfigB configB;

    @Bean
    public ServiceA serviceA() {
        return new ServiceA(configB);
    }
}

@Configuration
public class ConfigB {
    @Autowired
    private ConfigA configA;

    @Bean
    public ServiceB serviceB() {
        return new ServiceB(configA);
    }
}
```
**問題**: `@Configuration`クラスである`ConfigA`と`ConfigB`が互いに依存し、Springがこれらのクラスで定義されたBeanを初期化しようとするときに循環が発生します。

### Spring Bootでの一般的な原因
- **自動設定**: Spring Bootの自動設定は、カスタムBeanが自動設定されたものと相互作用する場合に、循環につながる依存関係を導入することがあります。
- **コンポーネントスキャン**: `@ComponentScan`の過剰使用または設定ミスによるパッケージは、意図しないBeanを取得し、循環依存を引き起こす可能性があります。
- **密結合設計**: サービス、リポジトリ、またはコントローラーを密結合するビジネスロジックは、不注意で循環を作成する可能性があります。
- **プロトタイプスコープの誤用**: プロトタイプスコープのBeanは循環依存を回避できることがありますが、循環的な方法でシングルトンBeanと組み合わせると依然として問題を引き起こす可能性があります。

### 循環依存の解決方法
1. **`@Lazy`アノテーションの使用**:
   - 依存関係の1つに`@Lazy`を付けて、実際に必要になるまでその初期化を遅延させます。
   ```java
   @Component
   public class BeanA {
       @Autowired
       @Lazy
       private BeanB beanB;
   }
   ```
   これにより、`BeanB`が解決される前に`BeanA`を部分的に初期化できるようにして循環を断ち切ります。

2. **セッターまたはフィールドインジェクションへの切り替え**:
   - コンストラクタインジェクションの代わりに、Beanの1つにセッターまたはフィールドインジェクションを使用して、Springが最初にBeanを初期化し、後で依存関係を注入できるようにします。
   ```java
   @Component
   public class BeanA {
       private BeanB beanB;

       @Autowired
       public void setBeanB(BeanB beanB) {
           this.beanB = beanB;
       }
   }
   ```

3. **循環を断ち切るためのコードリファクタリング**:
   - インターフェースまたは中間コンポーネントを導入してBeanを分離します。
   - 例：共通の依存関係を第三のBeanに抽出するか、サービス層を使用して相互作用を仲介します。
   ```java
   public interface Service {
       void performAction();
   }

   @Component
   public class BeanA implements Service {
       @Autowired
       private BeanB beanB;

       public void performAction() {
           // ロジック
       }
   }

   @Component
   public class BeanB {
       @Autowired
       private Service service; // BeanAに直接依存せず、インターフェースに依存
   }
   ```

4. **`@DependsOn`アノテーションの使用**:
   - 特定の場合に循環を回避するために、Beanの初期化順序を明示的に制御します。
   ```java
   @Component
   @DependsOn("beanB")
   public class BeanA {
       @Autowired
       private BeanB beanB;
   }
   ```

5. **`@EnableAspectJAutoProxy`によるプロキシの有効化**:
   - Springが依存関係を処理するためにプロキシ（CGLIBまたはJDK動的プロキシ）を使用するようにして、実際のBeanの代わりにプロキシを注入することで、一部の循環性の問題を解決できるようにします。

6. **設計の再評価**:
   - 循環依存は多くの場合、設計上の欠陥を示しています。単一責任の原則または依存性逆転の原則に従うようにリファクタリングを検討してください。

### 循環依存のデバッグ方法
- **スタックトレースの確認**: `BeanCurrentlyInCreationException`のスタックトレースは、循環に関与しているBeanを示します。
- **デバッグログの有効化**: `spring.main.lazy-initialization=true`を設定するか、`org.springframework`のデバッグログを有効にしてBean作成の詳細を確認します。
- **ツールの使用**: Spring Boot ActuatorやIDEプラグイン（例：Spring Tools Suite）などのツールは、Beanの依存関係を可視化できます。

### 循環依存の防止
- **ベストプラクティスの遵守**: インターフェースや抽象化などの依存性注入パターンを使用して、密結合を減らします。
- **コードのモジュール化**: 大規模なアプリケーションをより小さく、疎結合なモジュールに分解します。
- **早期テスト**: 統合テストを実行して、開発中に循環依存を検出します。
- **コンポーネントスキャンの制限**: 不必要なBeanを取得しないように、`@ComponentScan`で具体的に指定します。

### 循環依存が発生しにくい場合
- **プロトタイプスコープ**: プロトタイプスコープのBeanはオンデマンドで作成されるため、循環性の可能性を減らします（ただし完全には排除しません）。
- **遅延初期化**: グローバルな遅延初期化（`spring.main.lazy-initialization=true`）を有効にするとBean作成を延期できますが、問題を隠蔽するだけの場合があります。

### 結論
Spring/Spring Bootにおける循環依存は、Bean間の密結合から生じ、コンストラクタインジェクションや複雑な設定によって悪化することがよくあります。一般的な解決策には、`@Lazy`の使用、セッター/フィールドインジェクションへの切り替え、循環を断ち切るためのリファクタリングが含まれます。根本原因を理解し、ベストプラクティスを適用することで、これらの問題を効果的に防止または解決できます。特定の循環依存に遭遇した場合は、関連するコードやエラーの詳細を共有していただければ、さらに分析をお手伝いします！