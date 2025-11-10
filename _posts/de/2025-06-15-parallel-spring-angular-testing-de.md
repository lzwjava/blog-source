---
audio: false
generated: true
image: false
lang: de
layout: post
title: Parallele Federung Angular Browser-Tests
translated: true
type: note
---

Verstanden – Sie suchen eine praktische Methode, um Ihre Spring (Java) + Angular-Website **parallel in Edge und Chrome** zu testen, hauptsächlich **manuell** (mit etwas leichter Automatisierung, wo es hilft). Hier ist ein erprobtes Vorgehen, das breite Tabellen vermeidet.

---

# 1) Saubere, vergleichbare Browser einrichten

* **Installieren Sie die neueste stabile Version** von Chrome und Edge. Notieren Sie sich die Versionen.
* Erstellen Sie **separate, saubere Profile** für das Testen in jedem Browser:

  * Chrome: `chrome --user-data-dir=/tmp/chrome-qa --no-first-run`
  * Edge: `msedge --user-data-dir=/tmp/edge-qa --no-first-run`
* Gleichen Sie **Zoom (100%)**, **DPR**, **Sprache**, **OS-Theme**, **Font-Pakete** ab und schalten Sie Erweiterungen aus.
* Platzieren Sie beide Browser nebeneinander (bei zwei Monitoren ideal). Verwenden Sie das gleiche **Viewport** (z.B. 1440×900).

---

# 2) Stabiles Backend + realistische Daten vorbereiten

* Starten Sie Ihr Spring-Backend im **Staging-Modus** mit deterministischen Seed-Daten.
* Bevorzugen Sie **unveränderliche Test-Accounts** und einen **bekannten Datensatz** (z.B. Testcontainers für DB-Snapshots oder Flyway/Liquibase Seed-Skripte).
* Für flatterhafte Abhängigkeiten verwenden Sie **WireMock** Stubs (HTTP), damit das UI-Verhalten wiederholbar ist.

---

# 3) Interaktionen über Browser hinweg spiegeln (manuell, aber synchronisiert)

Für echtes paralleles manuelles Testen: Spiegeln Sie Klicks, Scrollen und Tippen von einem Browser zum anderen:

* Verwenden Sie **Browsersync** als lokalen Proxy, um **Interaktionen zu synchronisieren**:

  ```bash
  npm i -g browser-sync
  browser-sync start --proxy "http://localhost:4200" --files "dist/**/*" --open "external"
  ```

  Öffnen Sie die geproxyte URL in **Chrome** und **Edge**; Scrollen, Klicks und Formulareingaben werden gespiegelt.
  (Ideal für Layout-Unterschiede, Hover/Focus-Checks und schnelle Abläufe.)

> Falls ein Proxy nicht möglich ist (Auth-Beschränkungen, Firmennetzwerk), führen Sie zwei Fenster und halten Sie eine strenge **Schrittliste** (unten) plus eine Split-View Bildschirmaufnahme bereit.

---

# 4) Cross-Browser-Checkliste (gleichzeitig in beiden ausführen)

Arbeiten Sie diese **parallel** ab – gleicher Schritt in beiden Browsern, bevor Sie weitergehen.

* **Bootstrap & Fonts:** Flash of unstyled content (FOUC), Icon-Fonts, Fallback-Fonts.
* **Layout:** Flex/Grid-Lücken, sticky Header/Footer, Overflow/Ellipsis, RTL/L10n Textumbruch.
* **Formulare:** Autofill, Platzhalter, Validierungsmeldungen, Number/Date-Inputs, IME/Chinesische Eingabe, Copy/Paste.
* **Fokus/Tastatur:** Tab-Reihenfolge, Sichtbarkeit des Fokusrings, `:focus-visible` vs `:focus`, Enter/Esc-Verhalten, Shortcuts.
* **Hover/Active:** Menüs, Tooltips, Ripple-Effekte, Angular Material State Classes.
* **Dateien & Downloads:** File-Input Accept-Filter, Drag-and-Drop, Download-Aufforderungen.
* **Auth/Session:** Cookies, SameSite, Storage-Isolation über Tabs hinweg, Session-Timeout und Refresh-Token-Abläufe.
* **Routing:** Deep Links, Hard Refresh auf einer verschachtelten Route, 404-Fallback.
* **Caching:** Service Worker Update-Zyklus, Entfernen veralteter Assets, Offline-Seitenverhalten.
* **Media & APIs:** getUserMedia/clipboard, Benachrichtigungsberechtigungen.
* **Accessibility Quick Check:** Landmarks/Rollen, Farbkontrast (DevTools), Navigation nur mit Tastatur.
* **Performance-Sanity-Check:** DevTools Performance, Prüfung auf Long Tasks und Lighthouse in **beiden** Browsern.

Tipp: Halten Sie **DevTools geöffnet** (F12) in beiden, angedockt unten, und vergleichen Sie **Console**-Warnungen (Framework + CSP + Deprecation Messages).

---

# 5) Angular-Spezifika, die oft abweichen

* **Change Detection & Async:** Microtask-Timing kann Race Conditions unterschiedlich aufdecken; achten Sie auf Spinner und "Save"-Buttons bei Doppelklick-Problemen.
* **Zone.js-Fehler:** Unbehandelte Promise-Rejections in einem Browser, aber nicht im anderen – Console prüfen.
* **Angular Material Themes:** Überprüfen Sie Dark/Light-Tokens, High-Contrast-Modus und Fokus-Umrisslinien (Edge rendert Fokus oft leicht anders).
* **i18n Pipes & Datumsformate:** Locale-Unterschiede bei `DatePipe` und `Intl` in Chromium-Varianten.

---

# 6) Spring-Backend-Fallstricke

* **CORS & Redirects:** Gleiche Regeln, aber **Edge zeigt CORS Preflight-Probleme** manchmal früher im Dev-Modus an; überprüfen Sie `OPTIONS`-Antworten und Header.
* **Content-Type & Komprimierung:** Prüfen Sie `application/json;charset=UTF-8` vs `application/json`; verifizieren Sie gzip/br – Fehlanpassungen können sich in einem Browser zuerst als "Failed to load" zeigen.
* **Security-Header:** CSP, HSTS, X-Frame-Options – strengere Richtlinien können Inline-Skripte/Stile unterschiedlich blockieren.

---

# 7) „Manuell“ mit einer dünnen Automatisierungsschicht wiederholbar machen

Selbst wenn Sie keine vollständige E2E wollen, richten Sie eine **kurze, schnelle** Browser-Harness ein, damit CI bei jedem PR sowohl Chrome als auch Edge ausführen kann. So fangen Sie Regressionen früher und entlasten Ihren manuellen Durchgang.

### Option A: Playwright (meine erste Wahl für Angular-Apps)

* Ein Test-Runner, startet **Chrome Stable** und **Microsoft Edge** Kanäle, läuft **parallel**.
* `npm i -D @playwright/test`
* `npx playwright install chromium`
* `playwright.config.ts` Beispiel:

  ```ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    testDir: './e2e',
    workers: 4, // Parallelität
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

  Minimaler Smoke-Test (`e2e/smoke.spec.ts`):

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

  Ausführung: `npx playwright test`

### Option B: Cypress (Chromium-Familie, läuft in Chrome & Edge)

* Parallelisierung über CI-Matrix (oder Cypress Dashboard).
* In CI ausführen:

  * `cypress run --browser chrome`
  * `cypress run --browser edge`
* Halten Sie Specs klein (nur Smoke), um "manual-first" zu bleiben.

### Option C: Selenium Grid (falls Sie bereits Selenium verwenden)

* Dockerisierte Grid läuft **chromium/edge nodes** gleichzeitig.

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

  Richten Sie Ihre WebDriver-Tests auf `http://localhost:4444/wd/hub` aus und führen Sie Testsuites parallel aus.

---

# 8) CI "standardmäßig parallel"

* Verwenden Sie einen **Matrix**-Job (Chrome/Edge) und führen Sie Ihre Playwright/Cypress-Smoke-Tests parallel aus.
* Fail-Fast, um Zeit zu sparen; hängen Sie **Traces/Videos** für den fehlerhaften Browser an.
* Führen Sie nächtlich einen etwas breiteren Test und einen **Lighthouse**-Durchlauf in beiden Browsern aus.

---

# 9) Schnelle Fehleranalyse bei Unterschieden

* Erstellen Sie einen **HAR** von jedem Browser, diffen Sie die Antworten (Status, Header, Caching).
* Vergleichen Sie **berechnete Styles** für das fehlerhafte Element (DevTools → Styles → Computed).
* Schalten Sie **reduced motion** und **forced colors** um, um Accessibility-CSS-Probleme aufzudecken.
* Löschen Sie **Site-Daten** (Application Panel) und testen Sie erneut, um veraltete SW/Caches auszuschließen.

---

# 10) Minimale Artefakte zum Beibehalten

* Eine **gemeinsame Checkliste** (Markdown) Ihrer Cross-Browser-Checks.
* Ein **Versions-Ledger**: App-Commit, Chrome/Edge-Versionen, OS, wichtige Flags.
* Hängen Sie **Screenshots** (gleiches Viewport) für jeden visuellen Unterschied an, den Sie als "Won't Fix" akzeptieren.

---

Falls gewünscht, kann ich ein lauffähiges **Playwright-Skelett** für Ihre Angular-App generieren (mit `npm scripts`, CI-Matrix und zwei Smoke-Specs) oder ein **Browsersync-Skript**, das auf Ihre Dev-Server-Konfiguration zugeschnitten ist.