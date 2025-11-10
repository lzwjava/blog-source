---
audio: false
generated: true
image: false
lang: es
layout: post
title: Pruebas Angulares Paralelas de Spring en el Navegador
translated: true
type: note
---

Entendido—quieres una forma práctica de probar tu sitio Spring (Java) + Angular en **Edge y Chrome en paralelo**, principalmente de forma **manual** (con algo de automatización ligera donde ayude). Aquí tienes un flujo de trabajo probado en campo que evita tablas anchas.

---

# 1) Configurar navegadores limpios y comparables

* **Instala las últimas versiones estables** de Chrome y Edge. Toma nota de las versiones.
* Crea **perfiles separados y limpios** para las pruebas en cada uno:

  * Chrome: `chrome --user-data-dir=/tmp/chrome-qa --no-first-run`
  * Edge: `msedge --user-data-dir=/tmp/edge-qa --no-first-run`
* Iguala el **zoom (100%)**, **DPR**, **idioma**, **tema del SO**, **paquetes de fuentes** y desactiva las extensiones.
* Coloca ambos navegadores uno al lado del otro (dos monitores si es posible). Usa el mismo **viewport** (ej., 1440×900).

---

# 2) Preparar un backend estable + datos realistas

* Levanta tu backend Spring en **modo staging** con datos de seed deterministas.
* Prefiere **cuentas de prueba inmutables** y un **conjunto de datos conocido** (ej., Testcontainers para snapshots de BD o scripts de seed de Flyway/Liquibase).
* Para dependencias inestables, usa stubs **WireMock** (HTTP) para que el comportamiento de la UI sea repetible.

---

# 3) Reflejar interacciones entre navegadores (manual, pero sincronizado)

Para pruebas manuales genuinamente paralelas, refleja clics, desplazamientos y escritura de un navegador al otro:

* Usa **Browsersync** como proxy local para **sincronizar interacciones**:

  ```bash
  npm i -g browser-sync
  browser-sync start --proxy "http://localhost:4200" --files "dist/**/*" --open "external"
  ```

  Abre la URL proxyficada en **Chrome** y **Edge**; los desplazamientos, clics y entradas de formulario se reflejarán.
  (Ideal para diferencias de diseño, comprobaciones de hover/focus y flujos rápidos).

> Si no puedes usar el proxy (restricciones de autenticación, red corporativa), ejecuta dos ventanas y mantén una **lista de pasos** estricta (abajo) más una vista dividida de grabadora de pantalla.

---

# 4) Lista de verificación cross-browser (ejecutar ambos a la vez)

Trabaja esto **en paralelo**—mismo paso en ambos navegadores antes de continuar.

* **Bootstrap y fuentes:** Flash de contenido sin estilo (FOUC), fuentes de iconos, fuentes de respaldo.
* **Layout:** Espacios de Flex/Grid, encabezados/pies de página fijos, desbordamiento/puntos suspensivos, ajuste de texto RTL/L10n.
* **Formularios:** Autocompletado, placeholders, mensajes de validación, entradas de número/fecha, entrada IME/Chino, copiar/pegar.
* **Focus/teclado:** Orden de tabulación, visibilidad del anillo de enfoque, `:focus-visible` vs `:focus`, comportamientos de Enter/Esc, atajos.
* **Hover/active:** Menús, tooltips, efectos de onda, clases de estado de Angular Material.
* **Archivos y descargas:** Filtros de aceptación de entrada de archivos, arrastrar y soltar, avisos de descarga.
* **Auth/sesión:** Cookies, SameSite, aislamiento de almacenamiento entre pestañas, tiempo de espera de sesión y flujos de actualización de token.
* **Enrutamiento:** Enlaces profundos, actualización forzada en una ruta anidada, respaldo 404.
* **Caché:** Ciclo de actualización del Service Worker, invalidación de activos obsoletos, comportamiento de la página sin conexión.
* **Medios y APIs:** getUserMedia/portapapeles, permisos de notificaciones.
* **Revisión rápida de accesibilidad:** Puntos de referencia/roles, contraste de color (DevTools), navegación solo con teclado.
* **Comprobación de rendimiento:** DevTools Performance, revisar tareas largas y Lighthouse en **ambos** navegadores.

Consejo: Mantén **DevTools abierto** (F12) en ambos, acoplado abajo, y compara las advertencias de la **Consola** (mensajes del framework, CSP y de desaprobación).

---

# 5) Aspectos específicos de Angular que suelen diferir

* **Detección de cambios y async:** La temporización de las microtareas puede sacar a la luz condiciones de carrera de forma diferente; observa los spinners y los botones "Guardar" por problemas de doble clic.
* **Errores de Zone.js:** Rechazos de promesas no manejados en un navegador pero no en el otro—revisa la consola.
* **Temas de Angular Material:** Verifica los tokens oscuro/claro, el modo de alto contraste y los contornos de enfoque (Edge a menudo renderiza el enfoque ligeramente diferente).
* **Pipes i18n y formatos de fecha:** Diferencias de configuración regional con `DatePipe` e `Intl` en las variantes de Chromium.

---

# 6) Problemas comunes del backend Spring

* **CORS y redirecciones:** Mismas reglas, pero **Edge a veces muestra problemas de preflight CORS** antes en desarrollo; verifica las respuestas `OPTIONS` y los headers.
* **Content-Type y compresión:** Comprueba `application/json;charset=UTF-8` vs `application/json`; verifica gzip/br—las discrepancias pueden mostrarse como "Error al cargar" primero en un navegador.
* **Headers de seguridad:** CSP, HSTS, X-Frame-Options—políticas más estrictas pueden bloquear scripts/estilos en línea de forma diferente.

---

# 7) Hacer que lo "manual" sea repetible con una capa fina de automatización

Incluso si no quieres E2E completo, configura un **harness de navegador corto y rápido** para que el CI ejecute tanto Chrome como Edge en cada PR. Detendrás regresiones antes y aliviarás tu pasada manual.

### Opción A: Playwright (mi elección principal para apps Angular)

* Un solo ejecutor de pruebas, lanza los canales **Chrome Stable** y **Microsoft Edge**, se ejecuta **en paralelo**.
* `npm i -D @playwright/test`
* `npx playwright install chromium`
* Ejemplo de `playwright.config.ts`:

  ```ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    testDir: './e2e',
    workers: 4, // paralelismo
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

  Spec de humo mínimo (`e2e/smoke.spec.ts`):

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

  Ejecutar: `npx playwright test`

### Opción B: Cypress (familia Chromium, ejecuta Chrome & Edge)

* Paralelización mediante matriz de CI (o Cypress Dashboard).
* En CI, ejecuta:

  * `cypress run --browser chrome`
  * `cypress run --browser edge`
* Mantén las especificaciones mínimas (solo humo) para mantener un enfoque "manual-first".

### Opción C: Selenium Grid (si ya usas Selenium)

* Grid en Docker ejecuta **nodos chromium/edge** concurrentemente.

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

  Apunta tus pruebas de WebDriver a `http://localhost:4444/wd/hub` y ejecuta las suites en paralelo.

---

# 8) CI "paralelo por defecto"

* Usa un trabajo de **matriz** (Chrome/Edge) y ejecuta tu prueba de humo de Playwright/Cypress en paralelo.
* Falla-rápido para ahorrar tiempo; adjunta **traces/videos** para el navegador que falla.
* Cada noche, ejecuta un conjunto ligeramente más amplio y una pasada de **Lighthouse** en ambos navegadores.

---

# 9) Triaje rápido cuando difieren

* Obtén un **HAR** de cada navegador, compara las respuestas (estado, headers, caché).
* Compara los **estilos calculados** para el elemento roto (DevTools → Styles → Computed).
* Alterna **movimiento reducido** y **colores forzados** para revelar problemas de CSS de accesibilidad.
* Borra **datos del sitio** (panel Application) y vuelve a probar para descartar SW/cachés obsoletos.

---

# 10) Artefactos mínimos para guardar

* Una **lista de verificación compartida** (markdown) de tus comprobaciones cross-browser.
* Un **registro de versiones**: commit de la app, versiones de Chrome/Edge, SO, flags importantes.
* Adjunta **capturas de pantalla** (mismo viewport) para cualquier diferencia visual que aceptes como "no se corrige".

---

Si quieres, puedo generar un **esqueleto de Playwright** listo para ejecutar para tu app Angular (con `npm scripts`, matriz de CI y dos specs de humo), o un **script de Browsersync** adaptado a la configuración de tu servidor de desarrollo.