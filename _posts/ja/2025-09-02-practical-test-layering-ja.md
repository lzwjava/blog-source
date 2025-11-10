---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 実践的テストレイヤリングガイド
translated: true
type: note
---

素晴らしい質問です。健全なテスト戦略は、主に**リスクとフィードバックの速度**に関わります。ここでは、**どのレイヤーで何をテストすべきか**を決める実践的な方法を説明します。表は使わず、明確なルールと例を示します。

---

# 基本原則

* **実装ではなく振る舞いをテストする。** 非公開の詳細よりも公開APIを優先する。
* **バグを検知できる最速のレイヤーに検査を押し下げる。**
* **リスクが正当化される場合にのみ、実際の依存関係（DB、キュー、ブラウザ）を使用する。**
* **クリティカルなパスはエンドツーエンドでカバーするが、控えめに。** UIテストは最も壊れやすく遅いため、真に重要なものに限定する。

---

# 何をどこでテストするか（実践的なヒューリスティック）

## 1) 単体テスト (高速、分離)

**使用場面:** I/O（DB、HTTP、ファイルシステム）なしでテストできる純粋な/ドメインロジック。

* ビジネスルール、価格/手数料計算、バリデータ、マッパー、ユーティリティ。
* リポジトリ/クライアントを**モック化**したサービスメソッド。
* 目標: 多数の小さなテストをミリ秒単位で失敗させる。

**Java/Spring の例**

```java
@ExtendWith(MockitoExtension.class)
class FeeServiceTest {
  @Mock AccountRepo repo;
  @InjectMocks FeeService svc;

  @Test void vipGetsDiscount() {
    when(repo.tier("u1")).thenReturn("VIP");
    assertEquals(Money.of(90), svc.charge("u1", Money.of(100)));
    verify(repo).tier("u1");
  }
}
```

## 2) 結合 / コンポーネントテスト (実際の連携、最小限のモック)

**使用場面:** Springの連携、シリアライゼーション、フィルター、DBクエリ、トランザクションを検証する必要がある場合。

* **ネットワークなしのHTTPレイヤー**: `@WebMvcTest` (コントローラー + JSON)、またはフルスタックの場合は `@SpringBootTest(webEnvironment=RANDOM_PORT)`。
* **DBの正確性**: **Testcontainers**を使用して実際のDBを実行し、SQL、インデックス、マイグレーションをチェック。
* **メッセージング**: 実際のブローカーコンテナ (Kafka/RabbitMQ) を使用してコンシューマー/プロデューサーをテスト。

**HTTPスライスの例**

```java
@WebMvcTest(controllers = OrderController.class)
class OrderControllerTest {
  @Autowired MockMvc mvc;
  @MockBean OrderService svc;

  @Test void createsOrder() throws Exception {
    when(svc.create(any())).thenReturn(new Order("id1", 100));
    mvc.perform(post("/orders").contentType("application/json")
        .content("{\"amount\":100}"))
      .andExpect(status().isCreated())
      .andExpect(jsonPath("$.id").value("id1"));
  }
}
```

**Testcontainersを使用したDBの例**

```java
@Testcontainers
@SpringBootTest
class RepoIT {
  @Container static PostgreSQLContainer<?> db = new PostgreSQLContainer<>("postgres:16");
  @Autowired OrderRepo repo;

  @Test void persistsAndQueries() {
    var saved = repo.save(new OrderEntity(null, 100));
    assertTrue(repo.findById(saved.getId()).isPresent());
  }
}
```

## 3) API契約 & エンドツーエンドAPIテスト

**使用場面:** **下位互換性のある契約**または完全なシステムワークフローを保証する必要がある場合。

* **契約テスト** (例: OpenAPIスキーマ検証やPact) は、UIなしで破壊的変更を検出。
* **エンドツーエンドAPIフロー**: 実際のDBでアプリを起動し、HTTP経由でアクセス (RestAssured)。正常系パスと少数の重要なエッジケースに焦点。

**API E2Eの例**

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class ApiFlowIT {
  @LocalServerPort int port;
  @Test void happyPath() {
    given().port(port).contentType("application/json")
      .body("{\"amount\":100}")
      .when().post("/orders")
      .then().statusCode(201)
      .body("amount", equalTo(100));
  }
}
```

## 4) UIエンドツーエンドテスト (ブラウザ)

**使用場面:** 実際のブラウザで証明する必要がある、**少数の**重要なユーザージャーニーのみ:

* 認証 + チェックアウト; 金銭移動; PIIフロー; ファイルアップロード。
* **3〜10の重要なシナリオ**に抑える。それ以外はすべて、単体/結合/APIレイヤーでカバー。

**Selenium vs. Playwright/Cypress?**

* **Playwright** (またはCypress) を推奨: 自動待機、より簡単なセレクター、並列処理、組み込みのトレースビューアー、Chromium/Firefox/WebKitにわたる安定したヘッドレス実行。
* **Selenium** は、**カスタムグリッドで実際のベンダーブラウザ**を駆動する必要がある場合、**レガシー/エンタープライズ**設定と連携する場合、または成熟したSeleniumインフラが既にある場合に使用する。より多くの手作業が必要で、速度向上のためにグリッドが必要。

**Playwright (TypeScript) の例**

```ts
import { test, expect } from '@playwright/test';

test('checkout happy path', async ({ page }) => {
  await page.goto('http://localhost:4200');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.getByLabel('Email').fill('u@example.com');
  await page.getByLabel('Password').fill('secret');
  await page.getByRole('button', { name: 'Login' }).click();

  await page.getByText('Add to cart', { exact: true }).first().click();
  await page.getByRole('button', { name: 'Checkout' }).click();
  await expect(page.getByText('Order confirmed')).toBeVisible();
});
```

**Selenium (Java) を使用する必要がある場合**

```java
WebDriver d = new ChromeDriver();
d.get("http://localhost:4200");
new WebDriverWait(d, Duration.ofSeconds(10))
  .until(ExpectedConditions.elementToBeClickable(By.id("loginBtn"))).click();
```

---

# レイヤーごとの決定 (クイックフロー)

1. **I/Oなしでテストできるか？**
   → はい: **単体テスト**。

2. **フレームワークの連携/シリアライゼーションやDBクエリに依存するか？**
   → はい: **結合/コンポーネント**テスト (Springスライス、Testcontainers)。

3. **サービス間/公開API契約か？**
   → はい: **契約テスト** (スキーマ/Pact) + いくつかの **API E2E** フロー。

4. **価値がUIでのみ確認される、または重要なUXか？**
   → はい: **UI E2E**、ただしコアなジャーニーのみ。

---

# 賢明な割合と予算

* おおよそ **70–80% 単体**、**15–25% 結合/API**、**5–10% UI E2E** を目指す。
* コミットごとのCIを高速に保つ: 単体テストは <2–3分、結合テストは並列化。PRでは**小さなUIスモーク**テストを実行し、**より広範なUIパック**は毎晩実行。

---

# 優先すべきもの (リスクベースのチェックリスト)

* 金銭移動、認証、権限、コンプライアンス → **API & UIの正常系パス**。
* 複雑な計算、価格設定ルール → **単体テスト** (多くのケース) + 実際のDBの丸め/タイムゾーンを使った**いくつかの結合テスト**。
* 永続化ロジック、マイグレーション、複雑な結合 → **Testcontainersを使用したリポジトリテスト**。
* チーム間の契約 → **契約テスト**をCIで実行し、破壊的変更をブロック。
* アクセシビリティ、国際化 → ARIA/ロケールのための**コンポーネントテスト** + 主要ページでの**定期的なUIスキャン** (axe)。

---

# CIパイプラインの形状 (実用的)

* **すべてのプッシュ時:** 単体テスト + スライステスト; 少数のAPI E2E; ごく少数のUIスモーク (1–3)。
* **毎晩:** 全API E2E、より広範なUIパック、パフォーマンススモーク (k6)、基本的なセキュリティスキャン (ZAP)。
* 不安定なテストは迅速に**隔離**。修正または削除—無視しない。

---

# テストデータと不安定さへのヒント

* **ファクトリメソッド/ビルダー**を使用。共有される可変フィクスチャーは避ける。
* **Testcontainersの起動時にSQL/データをシード**し、テストを**冪等**に保つ。
* UIでは、CSS/XPathよりも**ロール/ラベルセレクター**を優先。スリープは避け、ユーザーが確認できる条件に結びついた待機を使用。
* CIでの失敗をデバッグするために**トレースを記録** (Playwright trace, Selenium logs)。

---

# 要するに経験則

* バグが**より高速な**レイヤーで検出できたはずなら、**テストを下のレイヤーに移動**する。
* **少数の重要な**UIジャーニーのみを維持する。
* **Testcontainers**を使用して結合テストを意味のあるものにする。
* Seleniumが必須でない限り、**Playwright**を優先する。

もしよろしければ、あなたの**上位3〜5のビジネスクリティカルなフロー**を教えてください。それらに対して、レイヤーごとの正確なテストリスト（ツールの選択とCIでのゲートを含む）を概説します。