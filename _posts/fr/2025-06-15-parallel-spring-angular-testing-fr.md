---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Test angulaire parallèle dans le navigateur
translated: true
type: note
---

Compris — vous cherchez une méthode pratique pour tester votre site Spring (Java) + Angular **en parallèle sur Edge et Chrome**, principalement **manuellement** (avec un peu d'automatisation légère si cela peut aider). Voici un processus éprouvé qui évite les tableaux trop larges.

---

# 1) Configurer des navigateurs propres et comparables

* **Installez les dernières versions stables** de Chrome et Edge. Prenez note des versions.
* Créez **des profils propres distincts** pour les tests dans chacun :

  * Chrome : `chrome --user-data-dir=/tmp/chrome-qa --no-first-run`
  * Edge : `msedge --user-data-dir=/tmp/edge-qa --no-first-run`
* Alignez le **zoom (100%)**, le **DPR**, la **langue**, le **thème du système d'exploitation**, les **packs de polices**, et désactivez les extensions.
* Placez les deux navigateurs côte à côte (deux écrans si possible). Utilisez la même **taille de viewport** (par ex., 1440×900).

---

# 2) Préparer un backend stable + des données réalistes

* Démarrez votre backend Spring en **mode staging** avec des données de seed déterministes.
* Préférez des **comptes de test immuables** et un **jeu de données connu** (par ex., Testcontainers pour des instantanés de base de données ou des scripts de seed Flyway/Liquibase).
* Pour les dépendances instables, utilisez des stubs **WireMock** (HTTP) afin que le comportement de l'UI soit reproductible.

---

# 3) Miroiter les interactions entre les navigateurs (manuel, mais synchronisé)

Pour des tests manuels véritablement parallèles, miroitez les clics, défilements et saisies d'un navigateur à l'autre :

* Utilisez **Browsersync** comme proxy local pour **synchroniser les interactions** :

  ```bash
  npm i -g browser-sync
  browser-sync start --proxy "http://localhost:4200" --files "dist/**/*" --open "external"
  ```

  Ouvrez l'URL proxifiée dans **Chrome** et **Edge** ; les défilements, clics et saisies de formulaire seront miroités.
  (Idéal pour les différences de mise en page, les vérifications de hover/focus et les flux rapides.)

> Si vous ne pouvez pas utiliser de proxy (contraintes d'authentification, réseau d'entreprise), ouvrez deux fenêtres et suivez une **liste d'étapes** stricte (ci-dessous) avec un enregistrement d'écran en vue partagée.

---

# 4) Checklist cross-browser (exécutez les deux en même temps)

Parcourez cela **en parallèle** — même étape dans les deux navigateurs avant de passer à la suivante.

* **Bootstrap & polices :** FOUC (Flash of Unstyled Content), polices d'icônes, polices de fallback.
* **Mise en page :** Écarts Flex/Grid, en-têtes/pieds de page sticky, débordement/ellipsis, habillage du texte RTL/L10n.
* **Formulaires :** Remplissage automatique, placeholders, messages de validation, champs nombre/date, saisie IME/chinoise, copier/coller.
* **Focus/clavier :** Ordre de tabulation, visibilité de l'anneau de focus, `:focus-visible` vs `:focus`, comportements Entrée/Échap, raccourcis.
* **Survol/actif :** Menus, infobulles, effets de ripple, classes d'état Angular Material.
* **Fichiers & téléchargements :** Filtres d'acceptation des champs de fichier, glisser-déposer, invites de téléchargement.
* **Auth/session :** Cookies, SameSite, isolation du stockage entre les onglets, expiration de session et flux de rafraîchissement du token.
* **Routing :** Liens profonds, actualisation forcée sur une route imbriquée, fallback 404.
* **Cache :** Cycle de mise à jour du Service Worker, invalidation des assets obsolètes, comportement de la page hors-ligne.
* **Médias & APIs :** getUserMedia/presse-papiers, permissions de notifications.
* **Vérification rapide d'accessibilité :** Points de repère/rôles, contraste des couleurs (Outils de développement), navigation au clavier uniquement.
* **Vérification sommaire des performances :** Performance des Outils de développement, vérification des longues tâches, et Lighthouse dans **les deux** navigateurs.

Astuce : Gardez les **Outils de développement ouverts** (F12) dans les deux, ancrés en bas, et comparez les avertissements de la **Console** (framework, CSP, messages d'obsolescence).

---

# 5) Spécificités Angular qui diffèrent souvent

* **Détection de changement & asynchrone :** Le timing des micro-tâches peut révéler des conditions de course différemment ; surveillez les indicateurs de chargement et les boutons "Sauvegarder" pour les problèmes de double-clic.
* **Erreurs Zone.js :** Rejets de promesses non gérés dans un navigateur mais pas dans l'autre — vérifiez la console.
* **Thèmes Angular Material :** Vérifiez les tokens sombre/clair, le mode contraste élevé et les contours de focus (Edge les rend souvent légèrement différemment).
* **Pipes i18n & formats de date :** Différences de locale avec `DatePipe` et `Intl` dans les variantes Chromium.

---

# 6) Pièges courants du backend Spring

* **CORS & redirections :** Mêmes règles mais **Edge signale parfois les problèmes de pré-vol CORS** plus tôt en développement ; vérifiez les réponses `OPTIONS` et les en-têtes.
* **Content-Type & compression :** Vérifiez `application/json;charset=UTF-8` vs `application/json` ; vérifiez gzip/br — les incohérences peuvent se manifester par un "Échec du chargement" dans un navigateur en premier.
* **En-têtes de sécurité :** CSP, HSTS, X-Frame-Options — des politiques plus strictes peuvent bloquer les scripts/styles inline différemment.

---

# 7) Rendre le "manuel" reproductible avec une fine couche d'automatisation

Même si vous ne voulez pas de tests E2E complets, configurez un **harness de navigateur court et rapide** pour que l'IC exécute Chrome et Edge sur chaque PR. Vous détecterez les régressions plus tôt et allégerez votre passage manuel.

### Option A : Playwright (mon choix préféré pour les apps Angular)

* Un seul lanceur de tests, lance les canaux **Chrome Stable** et **Microsoft Edge**, s'exécute **en parallèle**.
* `npm i -D @playwright/test`
* `npx playwright install chromium`
* Exemple `playwright.config.ts` :

  ```ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    testDir: './e2e',
    workers: 4, // parallélisme
    use: {
      baseURL: 'http://localhost:4200',
      trace: 'retain-on-failure',
    },
    projects: [
      {
        name: 'Chrome Stable',
        use: { ...devices['Desktop Chrome'], channel: 'chrome' },
      },
      {
        name: 'Microsoft Edge',
        use: { ...devices['Desktop Edge'], channel: 'msedge' },
      },
    ],
  });
  ```

  Spécification de smoke minimale (`e2e/smoke.spec.ts`) :

  ```ts
  import { test, expect } from '@playwright/test';

  test('home loads and login works', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('Password123!');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page.getByText('Dashboard')).toBeVisible();
  });
  ```

  Exécutez : `npx playwright test`

### Option B : Cypress (famille Chromium, exécute Chrome & Edge)

* Parallélisation via une matrice d'IC (ou Cypress Dashboard).
* Dans l'IC, exécutez :

  * `cypress run --browser chrome`
  * `cypress run --browser edge`
* Gardez les specs minimales (smoke seulement) pour rester "manuel d'abord".

### Option C : Selenium Grid (si vous utilisez déjà Selenium)

* Grid dockerisé exécute **les nœuds chromium/edge** simultanément.

  ```yaml
  # docker-compose.yml
  services:
    selenium-hub:
      image: selenium/hub:4
      ports: ["4444:4444"]
    chrome:
      image: selenium/node-chrome:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
    edge:
      image: selenium/node-edge:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
  ```

  Pointez vos tests WebDriver vers `http://localhost:4444/wd/hub` et exécutez les suites en parallèle.

---

# 8) IC "parallèle par défaut"

* Utilisez un travail en **matrice** (Chrome/Edge) et exécutez votre smoke Playwright/Cypress en parallèle.
* Arrêt au premier échec pour gagner du temps ; joignez les **traces/vidéos** pour le navigateur en échec.
* Tous les soirs, exécutez un jeu de tests légèrement plus large et un passage **Lighthouse** sur les deux navigateurs.

---

# 9) Tri rapide en cas de différence

* Récupérez le **HAR** de chaque navigateur, différez les réponses (statut, en-têtes, cache).
* Comparez les **styles calculés** pour l'élément cassé (Outils de développement → Styles → Calculé).
* Activez/désactivez **réduction animation** et **couleurs forcées** pour révéler les problèmes CSS d'accessibilité.
* Effacez les **données du site** (Panneau Application) et retestez pour exclure les caches/SW obsolètes.

---

# 10) Artéfacts minimaux à conserver

* Une **checklist partagée** (markdown) de vos vérifications cross-browser.
* Un **registre des versions** : commit de l'app, versions Chrome/Edge, OS, drapeaux importants.
* Joignez des **captures d'écran** (même viewport) pour toute différence visuelle que vous acceptez comme "ne sera pas corrigé".

---

Si vous le souhaitez, je peux générer un **squelette Playwright** prêt à l'emploi pour votre app Angular (avec `npm scripts`, matrice d'IC et deux specs de smoke), ou un **script Browsersync** adapté à la configuration de votre serveur de développement.