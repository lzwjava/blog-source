---
audio: false
generated: true
lang: ja
layout: post
title: 動的リージョン固有ビーンズ
translated: true
type: note
---

### 要件の理解

Spring Boot/Java Spring アプリケーションを構築しており、シンガポール（SG）、香港（HK）、台湾（TW）などの複数の地域（または「国籍」）をサポートする必要があるようです。`@Autowired` や Bean 管理などの機能を使用して、特に `CoreController` クラスに対して異なる Bean を動的にロードまたはインジェクションしたいと考えています。

これは、**マルチテナンシー**や**地域固有の設定**において、動作（サービス、設定、コントローラーなど）が地域によって異なる一般的なシナリオです。Spring では、実行時にコントローラークラス全体を簡単に切り替えることはできませんが、以下の方法があります：

1.  **Spring プロファイル**を使用して環境固有の Bean をロードする（例：各地域向けの個別のデプロイメントや有効化）。これはコンパイル時または起動時に行われます。
2.  **実行時選択**をストラテジーパターンと共に使用し、複数の Bean（例：Map 経由）をインジェクションして、リクエストパラメータ、ヘッダー、コンテキスト（例：ユーザーの地域）に基づいて適切なものを選択します。

「複数国籍開発」や SG/HK/TW などの例に言及されていることから、単一のアプリケーションインスタンスで複数の地域を処理する（実行時切り替え）必要があると想定します。地域ごとに個別のデプロイメントを行う場合は、プロファイルの方が簡単です。

両方のアプローチをコード例と共に説明します。`CoreController` が地域固有のサービス（例：`CoreService` インターフェースと各地域の実装）に依存していると仮定します。これにより、コントローラーは同じままで、インジェクションされる Bean を通じてその動作が変わります。

### アプローチ 1: Spring プロファイルを使用した地域固有 Bean のロード（起動時）

これは、地域ごとに個別のインスタンスをデプロイする場合（例：環境変数やアプリケーションプロパティ経由）に理想的です。Bean はアクティブなプロファイルに基づいて条件付きでロードされます。

#### ステップ 1: インターフェースと実装を定義する
地域固有のロジックのインターフェースを作成します：

```java
public interface CoreService {
    String getRegionMessage();
}
```

各地域の実装：

```java
// SgCoreService.java
@Service
@Profile("sg")  // 'sg' プロファイルがアクティブな場合のみこの Bean をロード
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service
@Profile("hk")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service
@Profile("tw")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### ステップ 2: CoreController でオートワイヤリングする
```java
@RestController
public class CoreController {
    private final CoreService coreService;

    @Autowired
    public CoreController(CoreService coreService) {
        this.coreService = coreService;
    }

    @GetMapping("/message")
    public String getMessage() {
        return coreService.getRegionMessage();
    }
}
```

#### ステップ 3: プロファイルを有効化する
- `application.properties` またはコマンドライン経由：
  - シンガポール Bean には `--spring.profiles.active=sg` を指定して実行。
  - これにより、`SgCoreService` Bean のみが作成され、オートワイヤリングされます。
- プロファイルを超えたカスタム条件には、`@ConditionalOnProperty` を使用します（例：`@ConditionalOnProperty(name = "app.region", havingValue = "sg")`）。

このアプローチはシンプルですが、再起動または地域ごとの個別アプリが必要です。単一のランタイムインスタンスですべての地域を処理するのには適していません。

### アプローチ 2: @Autowired Map を使用した実行時 Bean 選択（ストラテジーパターン）

単一のアプリケーションが複数の地域を動的に処理する場合（例：HTTP リクエストヘッダー `X-Region: sg` に基づく）、Bean の Map を使用します。Spring はすべての実装を Map<String, CoreService> にオートワイヤリングできます。キーは Bean 名です。

#### ステップ 1: インターフェースと実装を定義する
上記と同じですが、`@Profile` はなし：

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // Map キー用の明示的な Bean 名
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service("hkCoreService")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service("twCoreService")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### ステップ 2: CoreController で Map をオートワイヤリングする
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // Spring がすべての CoreService Bean を Bean 名をキーとして Map に自動投入
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // またはクエリパラメータの場合は @RequestParam を使用
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Unsupported region: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- ここで、Map に対する `@Autowired` は、すべての `CoreService` 実装を自動的にインジェクションします。
- Bean 名はキーのロジックに一致する必要があります（例："sgCoreService"）。
- 選択には：リクエストヘッダー/パラメータを使用して地域を決定します。これにより、リクエストごとに動的になります。

#### オプション: 特定のインジェクションに @Qualifier を使用する
特定の Bean を手動でインジェクションしたい場合：

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // SG Bean のみをインジェクション
    private CoreService sgCoreService;

    // ... 他も同様に
}
```
ただし、これは動的ではありません。実行時切り替えには Map を使用してください。

#### ステップ 3: 設定とベストプラクティス
- Spring Boot メインクラス：`@SpringBootApplication` で十分です。Spring が `@Service` Bean をスキャンします。
- デフォルトの処理：地域が一致しない場合のフォールバックサービスを追加します。
- より複雑な条件には、Bean に `@ConditionalOnExpression` またはカスタム `@Conditional` アノテーションを使用します。
- スレッド安全性：コントローラーはデフォルトでシングルトンであるため、サービスがステートレスであれば Map は安全です。
- テスト：モックリクエストを使用した `@SpringBootTest` で異なる地域をテストします。

### どちらのアプローチを選ぶべきか？
- **プロファイル**は、地域がデプロイメント/環境によって分離されている場合（例：SG/HK/TW で異なるサーバー）に使用します。
- **Map/ストラテジー**は、単一のアプリケーションが実行時にすべての地域を処理する場合（マイクロサービスにより柔軟）に使用します。

もしこれが正確な設定に合わない場合（例：`CoreController` 自体が地域ごとに異なる必要がある）、`@RequestMapping` 条件付きで複数のコントローラーを使用するか、コントローラーを動的に作成するファクトリーを使用できますが、それはより稀で複雑です。

詳細（例：地域の決定方法）を提供していただければ、さらに絞り込むことができます！