---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل كيوكومبر للتنمية القائمة على السلوك لمطوري جافا
translated: true
type: note
---

إليك دليلًا عمليًا وشاملًا للمقدمة حول **Cucumber**—ما هو، ولماذا تستخدمه الفرق، وكيفية تحقيق الإنتاجية باستخدامه في جافا (بالإضافة إلى ملاحظات سريعة لمستخدمي JS/Python).

---

# ما هو Cucumber (وما ليس هو)

* **Cucumber** هو إطار عمل اختبار **BDD (التطوير القائم على السلوك)**. يسمح لك بوصف السلوك بلغة عادية (Gherkin) وربط تلك الجمل بكود قابل للتنفيذ (تعريفات الخطوات).
* مثالي عندما تريد **فهمًا مشتركًا** عبر فرق المنتج وضمان الجودة والهندسة، و**توثيقًا حيًا** يعمل كاختبارات في نفس الوقت.
* **ليس** بديلاً عن أطر عمل اختبار الوحدات (JUnit/TestNG/Jest/PyTest). فهو يكملها من خلال التركيز على **اختبارات القبول على مستوى الأعمال**.

---

# القطع الأساسية

**1) Gherkin (مواصفات نصية عادية)**

* مكتوبة في ملفات `.feature`.
* الكلمات المفتاحية: `Feature`، `Scenario`، `Given/When/Then/And/But`، `Background`، `Scenario Outline` + `Examples`، `@tags`، (واختياريًا `Rule` في إصدارات Gherkin الأحدث).
* أسلوب لغة طبيعية؛ يدعم العديد من اللغات.

**2) تعريفات الخطوات (الكود)**

* تربط خطوات Gherkin بالكود عبر **Cucumber Expressions** (أو التعبيرات النمطية).
* يمكنها استدعاء كائنات الصفحة، عملاء واجهة برمجة التطبيقات، الخدمات، مساعدي قواعد البيانات، إلخ.

**3) المُشغّل (Runner)**

* يبدأ تشغيل Cucumber، ويكتشف الميزات والخطوات من خلال مسارات الغراء (glue paths)، والتكوين، والعلامات (tags).
* على JVM، تشغله عادةً عبر **JUnit** (الإصدار 4 أو 5) أو **TestNG**.

**4) التقارير**

* إنشاء تقارير HTML/JSON/JUnit XML؛ التكامل مع لوحات CI وأدوات مثل **Allure**.

---

# مثال بسيط (جافا، Maven)

**pom.xml (الأجزاء الرئيسية)**

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
        <!-- run by tag, parallel, etc., if needed -->
      </configuration>
    </plugin>
  </plugins>
</build>
```

**هيكل المشروع**

```
src
 └─ test
     ├─ java
     │   └─ com/example/steps/...
     └─ resources
         └─ features/...
```

**ملف ميزة (`src/test/resources/features/login.feature`)**

```gherkin
Feature: Login
  As a registered user
  I want to sign in
  So that I can access my account

  Background:
    Given the application is running

  @smoke
  Scenario: Successful login
    Given I am on the login page
    When I sign in with username "alice" and password "secret"
    Then I should see "Welcome, alice"

  Scenario Outline: Failed login
    Given I am on the login page
    When I sign in with username "<user>" and password "<pass>"
    Then I should see "Invalid credentials"
    Examples:
      | user  | pass     |
      | alice | wrong    |
      | bob   | invalid  |
```

**تعريفات الخطوات (جافا، Cucumber Expressions)**

```java
package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {
  private String page;
  private String message;

  @Given("the application is running")
  public void app_running() {
    // bootstrap test app / start server / reset state
  }

  @Given("I am on the login page")
  public void i_am_on_the_login_page() {
    page = "login";
  }

  @When("I sign in with username {string} and password {string}")
  public void i_sign_in(String user, String pass) {
    // call UI or API; here fake it:
    if ("alice".equals(user) && "secret".equals(pass)) {
      message = "Welcome, alice";
    } else {
      message = "Invalid credentials";
    }
  }

  @Then("I should see {string}")
  public void i_should_see(String expected) {
    assertEquals(expected, message);
  }
}
```

**مشغل JUnit 5 (الاكتشاف بواسطة المحرك)**

```java
// No explicit runner class needed with JUnit Platform.
// Create a test suite if you want tag filtering:
import org.junit.platform.suite.api.*;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = "cucumber.glue", value = "com.example.steps")
@ConfigurationParameter(key = "cucumber.plugin", value = "pretty, html:target/cucumber.html, json:target/cucumber.json")
@ExcludeTags("wip") // example
public class RunCucumberTest {}
```

التشغيل:

```bash
mvn -q -Dtest=RunCucumberTest test
```

---

# أساسيات Gherkin التي ستستخدمها يوميًا

* **الخلفية (Background)**: إعداد مشترك مرة واحدة لكل سيناريو (مثل "Given I'm logged in").
* **ملخص السيناريو + الأمثلة (Scenario Outline + Examples)**: اختبارات مدفوعة بالبيانات دون نسخ ولصق الخطوات.
* **سلاسل المستندات (Doc Strings)**: حمولات متعددة الأسطر (مثل أجسام JSON) في الخطوات.
* **جداول البيانات (Data Tables)**: تحويل جدول الخطوة إلى كائنات أو خرائط.
* **العلامات (Tags)**: تقسيم مجموعة الاختبارات (`@smoke`، `@api`، `@slow`) لأنابيب CI.
* **القاعدة (Rule)** (اختياري): تجميع السيناريوهات حسب قاعدة عمل لتحسين قابلية القراءة.

---

# تعبيرات Cucumber (أكثر سهولة من التعبيرات النمطية)

* العناصر النائبة مثل `{string}`، `{int}`، `{word}`، `{float}`.
* تسمح لك **أنواع المعاملات المخصصة** بتحليل كائنات المجال:

```java
import io.cucumber.java.ParameterType;

public class ParameterTypes {
  @ParameterType("USD|CNY|EUR")
  public Currency currency(String code) { return Currency.getInstance(code); }
}
```

ثم استخدم: `When I pay 100 {currency}`.

---

# الخطافات (Hooks) ودورة حياة الاختبار

* `@Before`، `@After`، `@BeforeStep`، `@AfterStep` في إصدارات JVM/JS/Ruby.
* استخدم الخطافات لـ **إعداد/تفكيك نظيف**، التقاط لقطات الشاشة عند الفشل، إعادة تعيين قواعد البيانات، إلخ.
* لحقن التبعيات (DI)، استخدم **Spring** (cucumber-spring) أو **PicoContainer** لمشاركة الحالة:

  * مع Spring Boot، ضع تعليقات توضيحية على فئات الخطوات على أنها beans؛ استخدم `@SpringBootTest` للتوصيل وشرائح الاختبار حسب الحاجة.

---

# التكاملات التي من المحتمل أنك تريدها

* **واجهة المستخدم الويب (Web UI)**: Selenium/WebDriver، Playwright. ضعها في **كائنات الصفحة (Page Objects)** واستدعها من الخطوات.
* **واجهة برمجة التطبيقات (API)**: REST Assured/عملاء HTTP؛ التحقق باستخدام تأكيدات JSON.
* **قاعدة البيانات (DB)**: Flyway/Liquibase للمخطط، محملي بيانات الاختبار، قواعد البيانات المضمنة.
* **المحاكاة (Mocking)**: WireMock/Testcontainers للأنظمة الخارجية.
* **التقارير (Reporting)**: HTML/JSON المدمج؛ **Allure** للجداول الزمنية الغنية والمرفقات.
* **التشغيل المتوازي (Parallel)**: JUnit Platform (أو `cucumber-jvm-parallel-plugin` مع TestNG في المكدسات الأقدم). حافظ على عزل السيناريوهات؛ تجنب الحالة المشتركة القابلة للتغيير.

---

# CI/CD والتوسع

* **أنابيب قائمة على العلامات**: شغّل `@smoke` على طلبات السحب (PRs)، و`@regression` يوميًا، و`@slow` حسب الجدولة (cron).
* **تقسيم حسب الملف أو العلامة** عبر الوكلاء (agents) للسرعة.
* **القطع الأثرية (Artifacts)**: انشر HTML/JSON/Allure ولقطات الشاشة/مقاطع الفيديو (لواجهة المستخدم).
* **الاختبارات غير المستقرة (Flaky tests)**: ابحث عن السبب الجذري—لا تحاول "إعادة التشغيل حتى النجاح" كحل.

---

# الممارسات الجيدة (مُجرّبة في المعارك)

* **صوت واحد** في Gherkin: حافظ على تناسق صياغة الخطوات؛ تجنب الثرثرة حول واجهة المستخدم ("انقر على الزر الأزرق")—ركز على **النية** ("إرسال بيانات الاعتماد").
* **خطوات رفيعة، مساعدون سميكون**: يجب أن يفوض كود الخطوات إلى كائنات الصفحة/الخدمات؛ أبقِ المنطق خارج الخطوات.
* **بيانات اختبار مستقرة**: أنشئها عبر واجهات برمجة التطبيقات/أجهزة قواعد البيانات؛ تجنب الاقتران بعشوائية تشبه الإنتاج.
* **سيناريوهات سريعة ومستقلة**: لا تفترض ترتيبًا معينًا؛ نظف الحالة لكل سيناريو.
* **حدّد حجم مجموعة الاختبارات**: احتفظ بـ Cucumber لـ **سلوك الأعمال**؛ احتفظ باختبارات الوحدات في JUnit/TestNG/Jest للتفاصيل منخفضة المستوى.

---

# الأنماط المضادة التي يجب تجنبها

* معاملة Cucumber كأداة تشغيل لاختبارات الوحدات بشكل أجمل فقط.
* الإفراط في استخدام `And` مع تسلسلات إجرائية طويلة (أمرية، هشة).
* الاقتران بمحددات CSS أو تفاصيل واجهة المستخدم المتقلبة في صياغة الخطوات.
* الخلفيات الضخمة التي تخفي ما يحتاجه كل سيناريو فعليًا.

---

# ملاحظات سريعة للغات الأخرى

**JavaScript/TypeScript**

* استخدم **`@cucumber/cucumber`**.
* النصوص النموذجية:

  ```bash
  npm i -D @cucumber/cucumber
  npx cucumber-js --require steps/**/*.ts --publish-quiet
  ```
* تعمل بشكل جيد مع **Playwright** و **Allure**.

**Python**

* استخدم **behave** (شبيه بـ Cucumber) أو **pytest-bdd**.
* الهيكل والمفاهيم هي نفسها: ميزات + خطوات + أجهزة (fixtures).

**Ruby**

* التطبيق الأصلي لـ Cucumber؛ المصطلحات تعكس إصدارات JVM و JS.

---

# متى تختار Cucumber

* عندما تريد **توثيقًا حيًا** يمكن لغير المهندسين قراءته.
* عندما تحتاج معايير القبول إلى أن تكون **قابلة للتنفيذ** و**قابلة للتتبع** حتى الإصدارات.
* عندما تتفق الفرق الوظيفية المتقاطعة على السلوك **قبل** التنفيذ (ثلاثيات BDD).

تخطاه (أو استخدمه باعتدال) إذا كان الفريق لن يحافظ على Gherkin، أو إذا كانت الاختبارات تقنية بحتة حيث توفر اختبارات الوحدة والتكامل الوضوح بالفعل.

---

إذا أخبرتني بمكدس التقنيات الذي تستخدمه (Spring/Quarkus؟ REST/UI؟ كيف تنشر/تستخدم CI؟)، يمكنني رسم هيكل Cucumber جاهز للتشغيل مع Maven/Gradle، والإضافات الموصى بها، وخط أنابيب نموذجي يناسب إعدادك.