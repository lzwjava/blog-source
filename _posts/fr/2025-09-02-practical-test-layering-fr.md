---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide Pratique de la Stratification des Tests
translated: true
type: note
---

Excellente question. Une stratégie de test rationnelle repose principalement sur **le risque et la vitesse de feedback**. Voici une méthode pratique pour décider **quoi tester à quelle couche**—pas de tableaux, juste des règles claires et des exemples.

---

# Principes fondamentaux

* **Testez le comportement, pas l'implémentation.** Privilégiez les APIs publiques aux détails privés.
* **Poussez la plupart des vérifications vers la couche la plus rapide** capable de détecter le bug.
* **N'utilisez des dépendances réelles que lorsque le risque le justifie** (BDD, files d'attente, navigateur).
* **Couvrez les chemins critiques de bout en bout, mais avec parcimonie.** Les tests UI sont les plus fragiles et les plus lents ; réservez-les pour ce qui compte vraiment.

---

# Où placer les tests (heuristiques rapides)

## 1) Tests unitaires (rapides, isolés)

**À utiliser quand :** La logique métier/domaine peut être testée sans E/S (BDD, HTTP, système de fichiers).

* Règles métier, calculs de prix/frais, validateurs, mappers, utilitaires.
* Méthodes de service avec les repos/clients **mockés**.
* Objectif : beaucoup de petits tests ; échec en millisecondes.

**Exemple Java/Spring**

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

## 2) Tests d'intégration / composants (câblage réel, mocks minimaux)

**À utiliser quand :** Vous devez vérifier le câblage Spring, la sérialisation, les filtres, les requêtes BDD, les transactions.

* **Couche HTTP sans réseau** : `@WebMvcTest` (contrôleurs + json), ou `@SpringBootTest(webEnvironment=RANDOM_PORT)` pour la stack complète.
* **Exactitude BDD** : Utilisez **Testcontainers** pour exécuter une vraie BDD ; vérifiez le SQL, les index, les migrations.
* **Messagerie** : Testez les consommateurs/producteurs avec un vrai conteneur de broker (Kafka/RabbitMQ).

**Exemple de slice HTTP**

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

**BDD avec Testcontainers**

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

## 3) Tests de contrat API & tests bout-en-bout API

**À utiliser quand :** Vous devez garantir des **contrats rétrocompatibles** ou des workflows système complets.

* **Tests de contrat** (par ex., validation de schéma OpenAPI ou Pact) détectent les changements cassants sans UI.
* **Flux API bout-en-bout** : Lancez l'app avec une vraie BDD et interagissez via HTTP (RestAssured). Concentrez-vous sur les chemins heureux + quelques cas limites critiques.

**Exemple API E2E**

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

## 4) Tests UI bout-en-bout (navigateur)

**À utiliser quand :** Seuls **quelques** parcours utilisateur critiques doivent être validés dans un vrai navigateur :

* Auth + checkout ; mouvements d'argent ; flux PII ; upload de fichier.
* Limitez à **3–10 scénarios clés**. Tout le reste : couvrez-le aux couches unitaire/intégration/API.

**Selenium vs. Playwright/Cypress ?**

* **Préférez Playwright** (ou Cypress) pour les apps Angular modernes : attente automatique, sélecteurs plus faciles, parallélisme, visionneuse de traces intégrée, exécutions headless stables sur Chromium/Firefox/WebKit.
* **Utilisez Selenium** si vous devez piloter de **vrais navigateurs vendors dans un grid personnalisé**, interagir avec des setups **legacy/enterprise**, ou si vous avez déjà une infrastructure Selenium mature. C'est plus complexe ; vous aurez besoin de waits explicites et d'un grid pour la vitesse.

**Exemple Playwright (TypeScript)**

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

**Si vous devez utiliser Selenium (Java)**

```java
WebDriver d = new ChromeDriver();
d.get("http://localhost:4200");
new WebDriverWait(d, Duration.ofSeconds(10))
  .until(ExpectedConditions.elementToBeClickable(By.id("loginBtn"))).click();
```

---

# Décision couche par couche (flux rapide)

1. **Peut-on le tester sans E/S ?**
   → Oui : **Test unitaire**.

2. **Dépend-il du câblage/sérialisation du framework ou de requêtes BDD ?**
   → Oui : Test **intégration/composant** (slices Spring, Testcontainers).

3. **S'agit-il d'un contrat cross-service/API publique ?**
   → Oui : **Tests de contrat** (schéma/Pact) + quelques flux **API E2E**.

4. **La valeur n'est-elle visible que dans l'UI ou s'agit-il d'une UX critique ?**
   → Oui : **UI E2E**, mais seulement pour les parcours principaux.

---

# Proportions sensées & budgets

* Visez environ **70–80% unitaire**, **15–25% intégration/API**, **5–10% UI E2E**.
* Gardez le CI par commit rapide : unitaire en <2–3 min, intégration parallélisée ; exécutez un **petit smoke test UI** sur les PRs, un **pack UI plus large chaque nuit**.

---

# Prioriser quoi (checklist basée sur le risque)

* Mouvement d'argent, auth, permissions, conformité → **API & un parcours heureux UI**.
* Calculs complexes, règles de tarification → **Unitaire** (beaucoup de cas) + **quelques intégrations** avec les arrondis BDD réels/fuseaux horaires.
* Logique de persistance, migrations, jointures complexes → **Tests de repo avec Testcontainers**.
* Contrats inter-équipes → **Tests de contrat** dans le CI pour bloquer les changements cassants.
* Accessibilité, i18n → **Tests composant** pour ARIA/locale + **scan UI périodique** (axe) sur les pages clés.

---

# Forme du pipeline CI (pragmatique)

* **À chaque push :** unitaire + tests slice ; une poignée d'API E2E ; petit smoke UI (1–3).
* **Chaque nuit :** API E2E complet, pack UI plus large, smoke test de performance (k6), scan de sécurité basique (ZAP).
* **Mettez en quarantaine les tests instables** rapidement ; corrigez ou supprimez—ne ignorez pas.

---

# Conseils sur les données de test et l'instabilité

* Utilisez des **méthodes factory/builders** ; évitez les fixtures mutables partagées.
* **Amorcez Testcontainers** avec SQL/des données au démarrage ; gardez les tests **idempotents**.
* Dans l'UI, préférez les **sélecteurs de rôle/libellé** au CSS/XPath ; évitez les sleeps, utilisez des waits liés aux conditions visibles par l'utilisateur.
* **Enregistrez les traces** (trace Playwright, logs Selenium) pour déboguer les échecs CI.

---

# Règles générales (TL;DR)

* Si un bug aurait pu être détecté par une couche **plus rapide**, **descendez le test**.
* Gardez seulement **quelques** parcours UI **critiques**.
* Utilisez **Testcontainers** pour donner du sens à l'intégration.
* Préférez **Playwright** sauf si Selenium est une exigence stricte.

Si vous voulez, donnez-moi vos **3–5 flux critiques pour le business** et je vous esquisserai la liste exacte des tests par couche (avec les choix d'outils et la gestion CI).