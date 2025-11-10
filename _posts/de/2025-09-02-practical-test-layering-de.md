---
audio: false
generated: true
image: false
lang: de
layout: post
title: Praktischer Leitfaden zum Testen in Schichten
translated: true
type: note
---

Gute Frage. Eine sinnvolle Teststrategie dreht sich hauptsächlich um **Risiko und Feedback-Geschwindigkeit**. Hier ist eine praktische Methode, um zu entscheiden, **was auf welcher Ebene getestet werden soll**—keine Tabellen, nur klare Regeln und Beispiele.

---

# Grundprinzipien

* **Teste Verhalten, nicht Implementierung.** Bevorzuge öffentliche APIs gegenüber privaten Details.
* **Schiebe die meisten Prüfungen auf die schnellste Ebene**, die den Fehler finden kann.
* **Verwende echte Abhängigkeiten nur, wenn das Risiko es rechtfertigt** (DB, Queues, Browser).
* **Decke kritische Pfade End-to-End ab, aber sparsam.** UI-Tests sind die fragilsten und langsamsten; bewahre sie für das auf, was wirklich wichtig ist.

---

# Was gehört wohin (schnelle Faustregeln)

## 1) Unit-Tests (schnell, isoliert)

**Verwende, wenn:** Reine/Domain-Logik ohne I/O (DB, HTTP, Dateisystem) getestet werden kann.

* Geschäftsregeln, Preis-/Gebührenberechnungen, Validatoren, Mapper, Utilities.
* Service-Methoden mit **gemockten** Repos/Clients.
* Ziel: viele kleine Tests; Fehler in Millisekunden.

**Java/Spring Beispiel**

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

## 2) Integrations- / Komponententests (echte Verkabelung, minimale Mocks)

**Verwende, wenn:** Du die Spring-Verkabelung, Serialisierung, Filter, DB-Queries, Transaktionen überprüfen musst.

* **HTTP-Schicht ohne Netzwerk**: `@WebMvcTest` (Controller + JSON), oder `@SpringBootTest(webEnvironment=RANDOM_PORT)` für den gesamten Stack.
* **DB-Korrektheit**: Verwende **Testcontainers**, um eine echte DB laufen zu lassen; prüfe SQL, Indizes, Migrationen.
* **Messaging**: Teste Consumer/Producer mit einem echten Broker-Container (Kafka/RabbitMQ).

**HTTP-Slice-Beispiel**

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

**DB mit Testcontainers**

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

## 3) API-Contract- & End-to-End-API-Tests

**Verwende, wenn:** Du **abwärtskompatible Contracts** oder komplette System-Workflows garantieren musst.

* **Contract-Tests** (z.B. OpenAPI-Schema-Validierung oder Pact) fangen Breaking Changes ohne UI auf.
* **End-to-End-API-Abläufe**: Starte die App mit echter DB und rufe sie via HTTP auf (RestAssured). Konzentriere dich auf Happy Paths + ein paar kritische Edge Cases.

**API-E2E-Beispiel**

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

## 4) UI-End-to-End-Tests (Browser)

**Verwende, wenn:** Nur **wenige** kritische User Journeys in einem echten Browser nachgewiesen werden müssen:

* Auth + Checkout; Geldbewegungen; PII-Flows; File-Upload.
* Beschränke dich auf **3–10 Schlüsselszenarien**. Alles andere: decke auf Unit-/Integrations-/API-Ebenen ab.

**Selenium vs. Playwright/Cypress?**

* **Bevorzuge Playwright** (oder Cypress) für moderne Angular-Apps: Auto-Waiting, einfachere Selektoren, Parallelismus, integrierter Trace-Viewer, stabile Headless-Läufe über Chromium/Firefox/WebKit.
* **Verwende Selenium**, wenn du **echte Vendor-Browser in einem Custom Grid** steuern musst, mit **Legacy-/Enterprise**-Setups interagierst oder bereits eine ausgereifte Selenium-Infrastruktur hast. Es ist mehr Aufbauarbeit; du brauchst explizite Waits und ein Grid für Geschwindigkeit.

**Playwright (TypeScript) Beispiel**

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

**Falls du Selenium verwenden musst (Java)**

```java
WebDriver d = new ChromeDriver();
d.get("http://localhost:4200");
new WebDriverWait(d, Duration.ofSeconds(10))
  .until(ExpectedConditions.elementToBeClickable(By.id("loginBtn"))).click();
```

---

# Entscheidung Ebene für Ebene (schneller Flow)

1.  **Kann es ohne I/O getestet werden?**
    → Ja: **Unit-Test**.

2.  **Hängt es von Framework-Verkabelung/Serialisierung oder DB-Queries ab?**
    → Ja: **Integrations-/Komponententest** (Spring Slices, Testcontainers).

3.  **Handelt es sich um einen Cross-Service/öffentlichen API-Contract?**
    → Ja: **Contract-Tests** (Schema/Pact) + ein paar **API-E2E**-Abläufe.

4.  **Ist der Wert nur in der UI sichtbar oder handelt es sich um eine kritische UX?**
    → Ja: **UI-E2E**, aber nur für Kern-Journeys.

---

# Sinnvolle Anteile & Budgets

*  Strebe grob nach **70–80% Unit**, **15–25% Integration/API**, **5–10% UI E2E**.
*  Halte den CI-Durchlauf pro Commit schnell: Unit in <2–3 Min, Integration parallelisiert; führe einen **kleinen UI-Smoke** bei PRs aus, ein **größeres UI-Paket nächtlich**.

---

# Was priorisieren (risikobasierte Checkliste)

*  Geldbewegungen, Auth, Berechtigungen, Compliance → **API & ein UI-Happy-Path**.
*  Komplexe Berechnungen, Preisregeln → **Unit** (viele Fälle) + ein **paar Integrationstests** mit echter DB-Rundung/Zeitzonen.
*  Persistenzlogik, Migrationen, knifflige Joins → **Repo-Tests mit Testcontainers**.
*  Cross-Team-Contracts → **Contract-Tests** in der CI, um Breaking Changes zu blockieren.
*  Barrierefreiheit, i18n → **Komponententests** für ARIA/Locale + **periodischer UI-Scan** (axe) auf Schlüsselseiten.

---

# CI-Pipeline-Form (pragmatisch)

*  **Bei jedem Push:** Unit + Slice-Tests; eine Handvoll API-E2E; winziger UI-Smoke (1–3).
*  **Nächtlich:** Vollständige API-E2E, breiteres UI-Paket, Performance-Smoke (k6), Basic-Security-Scan (ZAP).
*  **Quarantäne für flaky Tests** schnell; repariere oder lösche—ignoriere sie nicht.

---

# Testdaten & Flakiness-Tipps

*  Verwende **Factory-Methoden/Builder**; vermeide gemeinsam genutzte, veränderbare Fixtures.
*  **Seede Testcontainers** mit SQL/Daten beim Start; halte Tests **idempotent**.
*  In der UI, bevorzuge **Role/Label-Selektoren** gegenüber CSS/XPath; vermeide Sleeps, verwende Waits, die an benutzersichtbare Bedingungen geknüpft sind.
*  **Zeichne Traces auf** (Playwright Trace, Selenium Logs) zum Debuggen von CI-Fehlern.

---

# TL;DR Faustregeln

*  Wenn ein Fehler von einer **schnelleren** Ebene hätte gefunden werden können, **schiebe den Test nach unten**.
*  Behalte nur **wenige, kritische** UI-Journeys.
*  Verwende **Testcontainers**, um Integrationstests aussagekräftig zu machen.
*  Bevorzuge **Playwright**, es sei denn, Selenium ist eine harte Anforderung.

Wenn du möchtest, nenne mir deine **Top 3–5 geschäftskritischen Abläufe** und ich skizziere die genaue Testliste pro Ebene (mit Tool-Auswahl und CI-Gating).