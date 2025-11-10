---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía Práctica de Estratificación de Pruebas
translated: true
type: note
---

Excelente pregunta. Una estrategia de pruebas sensata se trata principalmente de **riesgo y velocidad de feedback**. Aquí tienes una forma práctica de decidir **qué probar en qué capa**—sin tablas, solo reglas claras y ejemplos.

---

# Principios fundamentales

* **Prueba el comportamiento, no la implementación.** Favorece las APIs públicas sobre los detalles privados.
* **Lleva la mayoría de las verificaciones a la capa más rápida** que pueda detectar el bug.
* **Usa dependencias reales solo cuando el riesgo lo justifique** (BD, colas, navegador).
* **Cubre las rutas críticas de principio a fin, pero con moderación.** Las pruebas de UI son las más frágiles y lentas; resérvalas para lo que realmente importa.

---

# Qué va dónde (heurísticas rápidas)

## 1) Pruebas unitarias (rápidas, aisladas)

**Úsalas cuando:** La lógica pura/dominio se puede probar sin E/S (BD, HTTP, sistema de archivos).

* Reglas de negocio, cálculos de precios/tarifas, validadores, mappers, utilidades.
* Métodos de servicio con repositorios/clientes **simulados** (mocked).
* Objetivo: muchas pruebas pequeñas; que fallen en milisegundos.

**Ejemplo en Java/Spring**

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

## 2) Pruebas de integración / componentes (configuración real, mocks mínimos)

**Úsalas cuando:** Necesitas verificar la configuración de Spring, serialización, filtros, consultas a BD, transacciones.

* **Capa HTTP sin red**: `@WebMvcTest` (controladores + json), o `@SpringBootTest(webEnvironment=RANDOM_PORT)` para el stack completo.
* **Corrección de BD**: Usa **Testcontainers** para ejecutar una BD real; verifica SQL, índices, migraciones.
* **Mensajería**: Prueba consumidores/productores con un broker real en contenedor (Kafka/RabbitMQ).

**Ejemplo de segmento HTTP**

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

**BD con Testcontainers**

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

## 3) Pruebas de contrato API y end-to-end (E2E) de API

**Úsalas cuando:** Debes garantizar **contratos retrocompatibles** o flujos de trabajo completos del sistema.

* **Pruebas de contrato** (ej., validación de esquema OpenAPI o Pact) detectan cambios incompatibles sin la UI.
* **Flujos E2E de API**: Ejecuta la aplicación con BD real y haz peticiones HTTP (RestAssured). Enfócate en rutas felices + algunos casos extremos críticos.

**Ejemplo de E2E de API**

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

## 4) Pruebas end-to-end (E2E) de UI (navegador)

**Úsalas cuando:** Solo **unas pocas** rutas de usuario críticas deben probarse en un navegador real:

* Autenticación + checkout; movimientos de dinero; flujos de PII; carga de archivos.
* Mantén **3–10 escenarios clave**. Todo lo demás: cúbrelo en las capas unitaria/integración/API.

**¿Selenium vs. Playwright/Cypress?**

* **Prefiere Playwright** (o Cypress) para aplicaciones Angular modernas: espera automática, selectores más fáciles, paralelismo, visor de trazas integrado, ejecuciones headless estables en Chromium/Firefox/WebKit.
* **Usa Selenium** si necesitas controlar **navegadores de proveedor real en un grid personalizado**, interactuar con configuraciones **legacy/empresariales**, o ya tienes una infraestructura Selenium madura. Requiere más configuración; necesitarás esperas explícitas y un grid para velocidad.

**Ejemplo de Playwright (TypeScript)**

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

**Si debes usar Selenium (Java)**

```java
WebDriver d = new ChromeDriver();
d.get("http://localhost:4200");
new WebDriverWait(d, Duration.ofSeconds(10))
  .until(ExpectedConditions.elementToBeClickable(By.id("loginBtn"))).click();
```

---

# Decidiendo capa por capa (flujo rápido)

1. **¿Se puede probar sin E/S?**
   → Sí: **Prueba unitaria**.

2. **¿Depende de la configuración del framework/serialización o consultas a BD?**
   → Sí: Prueba de **integración/componente** (segmentos de Spring, Testcontainers).

3. **¿Es un contrato de API pública o entre servicios?**
   → Sí: **Pruebas de contrato** (esquema/Pact) + un par de flujos **E2E de API**.

4. **¿El valor solo es visible en la UI o es una UX crítica?**
   → Sí: **E2E de UI**, pero solo para los flujos principales.

---

# Proporciones y presupuestos sensatos

* Apunta aproximadamente a **70–80% unitarias**, **15–25% integración/API**, **5–10% E2E de UI**.
* Mantén el CI por commit rápido: unitarias en <2–3 min, integración en paralelo; ejecuta un **pequeño smoke test de UI** en los PRs, un **conjunto más amplio de UI cada noche**.

---

# Qué priorizar (lista de verificación basada en riesgo)

* Movimiento de dinero, autenticación, permisos, cumplimiento → **API y una ruta feliz de UI**.
* Cálculos complejos, reglas de precios → **Unitarias** (muchos casos) + un **par de integración** con redondeo de BD real/husos horarios.
* Lógica de persistencia, migraciones, joins complejos → **Pruebas de repositorio con Testcontainers**.
* Contratos entre equipos → **Pruebas de contrato** en CI para bloquear cambios incompatibles.
* Accesibilidad, i18n → **Pruebas de componente** para ARIA/locale + **escaneo periódico de UI** (axe) en páginas clave.

---

# Forma de la pipeline de CI (pragmática)

* **En cada push:** unitarias + pruebas de segmento; un puñado de E2E de API; smoke test mínimo de UI (1–3).
* **Cada noche:** E2E de API completo, conjunto más amplio de UI, smoke test de rendimiento (k6), escaneo básico de seguridad (ZAP).
* **Pon en cuarentena** las pruebas inestables rápidamente; arréglalas o elimínalas—no las ignores.

---

# Consejos sobre datos de prueba e inestabilidad

* Usa **métodos de fábrica/builders**; evita fixtures compartidos mutables.
* **Inicializa Testcontainers** con SQL/datos al inicio; mantén las pruebas **idempotentes**.
* En UI, prefiere **selectores por rol/etiqueta** sobre CSS/XPath; evita sleeps, usa waits vinculados a condiciones visibles para el usuario.
* **Graba trazas** (trazas de Playwright, logs de Selenium) para depurar fallos en CI.

---

# Reglas generales (TL;DR)

* Si un bug hubiera sido detectado por una capa **más rápida**, **mueve la prueba hacia abajo**.
* Mantén solo **pocos** flujos de UI **críticos**.
* Usa **Testcontainers** para darle significado a la integración.
* Prefiere **Playwright** a menos que Selenium sea un requisito indispensable.

Si quieres, dime tus **3–5 flujos críticos para el negocio principales** y esbozaré la lista exacta de pruebas por capa (con elección de herramientas y control en CI).