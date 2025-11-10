---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Java開発者のためのCucumber BDDガイド
translated: true
type: note
---

以下は、**Cucumber** の実践的でエンドツーエンドの紹介です。Cucumber とは何か、チームがなぜそれを使うのか、そして Java でそれを使って生産的になる方法を説明します（JS/Python ユーザー向けの簡単なメモも含みます）。

---

# Cucumber とは何か（そして何ではないか）

* **Cucumber** は **BDD (Behavior-Driven Development)** テストフレームワークです。これは、プレーンテキスト (Gherkin) で振る舞いを記述し、それらの文を実行可能なコード (ステップ定義) に結びつけることができます。
* プロダクト、QA、エンジニアリングの間で**共通理解**を得たい場合、およびテストとしても機能する** Living Documentation **が必要な場合に理想的です。
* 単体テストフレームワーク (JUnit/TestNG/Jest/PyTest) の**代替品ではありません**。**ビジネスレベルの受け入れテスト**に焦点を当てることで、それらを補完します。

---

# コア構成要素

**1) Gherkin (プレーンテキスト仕様)**

* `.feature` ファイルで記述されます。
* キーワード: `Feature`, `Scenario`, `Given/When/Then/And/But`, `Background`, `Scenario Outline` + `Examples`, `@tags`, (およびオプションで新しい Gherkin の `Rule`)。
* 自然言語スタイル。多くのロケールをサポートします。

**2) ステップ定義 (コード)**

* **Cucumber Expressions** (または正規表現) を介して Gherkin ステップをコードにバインドします。
* ページオブジェクト、API クライアント、サービス、DB ヘルパーなどを呼び出すことができます。

**3) ランナー**

* Cucumber を起動し、グルーパス、設定、タグによってフィーチャー/ステップを検出します。
* JVM では、通常 **JUnit** (4 または 5) または **TestNG** を介して実行します。

**4) レポート**

* HTML/JSON/JUnit XML を生成します。CI ダッシュボードや **Allure** のようなツールと統合します。

---

# 最小限の例 (Java, Maven)

**pom.xml (主要部分)**

```xml
<dependencies>
  <!-- JUnit 5 -->
  <dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
  </dependency>

  <!-- Cucumber JVM + JUnit Platform -->
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-junit-platform-engine</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
</dependencies>

<build>
  <plugins>
    <plugin>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version>
      <configuration>
        <!-- 必要に応じてタグ、並列実行などで実行 -->
      </configuration>
    </plugin>
  </plugins>
</build>
```

**プロジェクトレイアウト**

```
src
 └─ test
     ├─ java
     │   └─ com/example/steps/...
     └─ resources
         └─ features/...
```

**フィーチャーファイル (`src/test/resources/features/login.feature`)**

```gherkin
Feature: ログイン
  登録ユーザーとして
  サインインしたい
  自分のアカウントにアクセスできるように

  Background:
    Given アプリケーションが起動している

  @smoke
  Scenario: ログイン成功
    Given ログインページにいる
    When ユーザー名 "alice" とパスワード "secret" でサインインする
    Then "Welcome, alice" と表示されるべき

  Scenario Outline: ログイン失敗
    Given ログインページにいる
    When ユーザー名 "<user>" とパスワード "<pass>" でサインインする
    Then "Invalid credentials" と表示されるべき
    Examples:
      | user  | pass     |
      | alice | wrong    |
      | bob   | invalid  |
```

**ステップ定義 (Java, Cucumber Expressions)**

```java
package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {
  private String page;
  private String message;

  @Given("アプリケーションが起動している")
  public void app_running() {
    // テストアプリのブートストラップ / サーバー起動 / 状態リセット
  }

  @Given("ログインページにいる")
  public void i_am_on_the_login_page() {
    page = "login";
  }

  @When("ユーザー名 {string} とパスワード {string} でサインインする")
  public void i_sign_in(String user, String pass) {
    // UI または API を呼び出す。ここでは仮の実装:
    if ("alice".equals(user) && "secret".equals(pass)) {
      message = "Welcome, alice";
    } else {
      message = "Invalid credentials";
    }
  }

  @Then("{string} と表示されるべき")
  public void i_should_see(String expected) {
    assertEquals(expected, message);
  }
}
```

**JUnit 5 ランナー (エンジンによる検出)**

```java
// JUnit Platform では明示的なランナークラスは不要。
// タグフィルタリングが必要な場合はテストスイートを作成:
import org.junit.platform.suite.api.*;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = "cucumber.glue", value = "com.example.steps")
@ConfigurationParameter(key = "cucumber.plugin", value = "pretty, html:target/cucumber.html, json:target/cucumber.json")
@ExcludeTags("wip") // 例
public class RunCucumberTest {}
```

実行:

```bash
mvn -q -Dtest=RunCucumberTest test
```

---

# 日常的に使用する Gherkin の基本

* **Background**: シナリオごとの共通セットアップ (例: "Given ログインしている")。
* **Scenario Outline + Examples**: ステップのコピー＆ペーストなしでデータ駆動テストを実現。
* **Doc Strings**: ステップ内の複数行のペイロード (例: JSON ボディ)。
* **Data Tables**: ステップのテーブルをオブジェクトやマップに変換。
* **Tags**: CI パイプライン用にスイートを分割 (`@smoke`, `@api`, `@slow`)。
* **Rule** (オプション): 可読性のためにシナリオをビジネスルールでグループ化。

---

# Cucumber Expressions (正規表現より扱いやすい)

* `{string}`, `{int}`, `{word}`, `{float}` などのプレースホルダー。
* **カスタムパラメータタイプ**を使用してドメインオブジェクトをパースできます:

```java
import io.cucumber.java.ParameterType;

public class ParameterTypes {
  @ParameterType("USD|CNY|EUR")
  public Currency currency(String code) { return Currency.getInstance(code); }
}
```

そして使用: `When I pay 100 {currency}`.

---

# フック & テストライフサイクル

* JVM/JS/Ruby バリアントでは `@Before`, `@After`, `@BeforeStep`, `@AfterStep`。
* フックは **クリーンなセットアップ/ティアダウン**、失敗時のスクリーンショット、DB リセットなどに使用します。
* DI には、**Spring** (cucumber-spring) または **PicoContainer** を使用して状態を共有:

  * Spring Boot では、ステップクラスを Bean としてアノテートし、必要に応じてワイヤリングとテストスライスに `@SpringBootTest` を使用します。

---

# おそらく必要になる統合

* **Web UI**: Selenium/WebDriver, Playwright。**ページオブジェクト**でラップし、ステップから呼び出します。
* **API**: REST Assured/HTTP クライアント。JSON アサーションで検証します。
* **DB**: Flyway/Liquibase (スキーマ用)、テストデータローダー、組み込み DB。
* **モッキング**: WireMock/Testcontainers (外部システム用)。
* **レポート**: 組み込みの HTML/JSON。**Allure** (リッチなタイムラインと添付ファイル用)。
* **並列実行**: JUnit Platform (または古いスタックでは TestNG を使用した `cucumber-jvm-parallel-plugin`)。シナリオを分離し、共有された可変状態を避けます。

---

# CI/CD & スケーリング

* **タグベースのパイプライン**: PR で `@smoke` を実行、日次で `@regression`、cron で `@slow`。
* **ファイルまたはタグによるシャーディング**をエージェント間で行い、速度を向上。
* **成果物**: HTML/JSON/Allure およびスクリーンショット/ビデオ (UI) を公開。
* **不安定なテスト**: 根本原因を追究します。「成功するまで再試行」でごまかさないでください。

---

# 実戦で検証された良いプラクティス

* Gherkin では**一貫した表現**を: ステップの言い回しを一貫させます。UI の詳細 ("青いボタンをクリック") を避け、**意図** ("資格情報を送信") に焦点を当てます。
* **ステップは薄く、ヘルパーは厚く**: ステップコードはページオブジェクト/サービスに委任します。ロジックをステップ内に置かないようにします。
* **安定したテストデータ**: API/DB フィクスチャを介してシードします。本番環境に似たランダム性への結合を避けます。
* **高速で独立したシナリオ**: 順序付けの仮定を置かず、シナリオごとに状態をクリーンにします。
* **スイートサイズを制限**: Cucumber は**ビジネス振る舞い**用に確保します。低レベルの詳細には JUnit/TestNG/Jest での単体テストを維持します。

---

# 避けるべきアンチパターン

* Cucumber を単なる見栄えの良い単体テストランナーとして扱うこと。
* 長い手続き型のシーケンスで `And` を過度に使用すること (命令的で脆い)。
* ステップの表現で CSS セレクタや変わりやすい UI の詳細に結合すること。
* 各シナリオが実際に必要とするものを隠してしまう巨大な Background。

---

# 他の言語向けの簡単なメモ

**JavaScript/TypeScript**

* **`@cucumber/cucumber`** を使用します。
* 典型的なスクリプト:

  ```bash
  npm i -D @cucumber/cucumber
  npx cucumber-js --require steps/**/*.ts --publish-quiet
  ```
* **Playwright** および **Allure** と相性が良いです。

**Python**

* **behave** (Cucumber 類似) または **pytest-bdd** を使用します。
* 構造と概念は同じです: フィーチャー + ステップ + フィクスチャ。

**Ruby**

* オリジナルの Cucumber 実装。慣習は JVM および JS バージョンと同様です。

---

# Cucumber を選択する場合

* エンジニア以外にも読める **Living Documentation** が欲しい場合。
* 受け入れ基準が**実行可能**で、リリースに**トレーサブル**である必要がある場合。
* クロスファンクショナルチームが実装**前に**振る舞いについて合意する (BDD トライアド) 場合。

チームが Gherkin をメンテナンスしない場合、またはテストが純粋に技術的であり単体/結合テストですでに明確さが提供されている場合は、それを使用しないか、控えめに使用してください。

---

あなたのスタック (Spring/Quarkus? REST/UI? デプロイ/CI 方法?) を教えていただければ、Maven/Gradle、推奨プラグイン、およびあなたのセットアップに合ったサンプルパイプラインを備えた、すぐに実行できる Cucumber スケルトンを概説できます。