---
audio: false
generated: true
image: false
lang: es
layout: post
title: Sincronizar Ramas y Código de UAT de Primavera
translated: true
type: note
---

Aquí tienes una colección de mejores prácticas y patrones que puedes combinar para mantener tus tres ramas UAT sincronizadas, mantener tu historial limpio y manejar código específico por país en una aplicación Spring—más un poco sobre dónde la IA puede ayudar.

---

## 1. Ramificación y sincronización

1.  **Basado en troncal (Trunk-based) con ramas de características de corta duración**

    * Mantén una única rama **main** (o **develop**).
    * Para cada ticket de Jira (ej. FT-103) y país, crea ramas de características nombradas:

      ```
      feature/FT-103-cn
      feature/FT-103-sg
      feature/FT-103-tw
      ```
    * Cuando el trabajo esté listo, fusiona de vuelta en **main**, luego haz cherry-pick o fusiona en cada `uat_cn`, `uat_sg`, `uat_tw`.
    * Beneficio: las fusiones a main ocurren una vez; las ramas de país solo toman lo que necesitan.

2.  **Sincronización regular de las ramas UAT**

    * Programa un trabajo diario (o por compilación) para rebasar cada `uat_*` sobre `main` para que no se separen demasiado.
    * Automatízalo en CI (ej. una GitHub Action que rebase `uat_cn` cada noche).

3.  **Usa pull-requests + aplicación de revisión**

    * Requiere un PR para cada fusión de rama-de-característica → main.
    * Asegúrate de que el ticket “FT-xxx” esté en el nombre de la rama y en el título/descripción del PR.

---

## 2. Convenciones de mensajes de commit y squashing

1.  **Estilo convencional con clave JIRA**

    ```
    FT-103: fix null-pointer in customer lookup
    ```

2.  **Micro-commit → squash al momento de la fusión**

    * Durante el trabajo en la característica, los desarrolladores confirman cambios (commit) sobre la marcha:

      ```
      FT-103 #1: initial wiring of service beans
      FT-103 #2: add validation logic
      FT-103 #3: update error handling
      ```
    * Al fusionar el PR, usa “Squash and merge” para colapsar todos los commits de FT-103 en un commit conciso:

      ```
      FT-103: customer-service validation and error handling
      ```

3.  **Numeración dentro de un ticket**

    * Si se rastrean múltiples pasos distintos en el mismo ticket, la numeración (`#1`, `#2`) está bien durante el desarrollo.
    * Una vez fusionado, compacta (squash) todo en un *único* commit FT-103; el historial permanece ordenado y cada ticket es un cambio lógico.

4.  **Automatiza commit-lint**

    * Usa un hook de Git o un plugin de CI (ej. [commitlint](https://commitlint.js.org)) para exigir `FT-\d+` al inicio de cada mensaje.
    * Opcionalmente, exige un alcance (scope): `FT-103(sg): …`.

---

## 3. Manejo de código específico por país en Spring

1.  **Perfiles y beans condicionales**

    * Define un perfil de Spring por país: `@Profile("cn")`, `@Profile("sg")`, `@Profile("tw")`.
    * En `application-cn.yml`, `application-sg.yml`, etc., establece propiedades específicas por país.
    * Al inicio, pasa `--spring.profiles.active=cn` (o sg, tw) para seleccionar los beans correctos.

2.  **Patrón estrategia / módulos plugin**

    * Crea una interfaz `PaymentProcessor` con tres implementaciones (`CnPaymentProcessor`, etc.).
    * Usa `@Component` + `@Profile` o una fábrica que elija el bean basándose en una bandera (flag) de tiempo de ejecución.

3.  **Paquetes de recursos / feature flags**

    * Si las diferencias son pequeñas (ej. formatos de fecha, URLs de endpoints), mantén una única ruta de código y externaliza las diferencias en archivos de propiedades o un servicio de feature flags.

4.  **Módulos separados (si son grandes)**

    * Para lógica muy divergente, divídela en submódulos:

      ```
      /core
      /country-cn
      /country-sg
      /country-tw
      ```
    * La aplicación principal incluye solo el módulo de país activo en el momento de la compilación/despliegue.

---

## 4. Separación de tareas por autor vs por ticket

*   **Por ticket, no por autor.** Las tareas deben estar unitizadas alrededor de *características* (IDs de Jira), no de la persona.
*   Si múltiples desarrolladores trabajan en FT-103, colaboran en la misma rama o usan ramas temáticas derivadas de ella—pero en última instancia fusionan de vuelta en la única rama FT-103.
*   Los metadatos del autor permanecen en el campo de autor del commit; no necesitas compactar (squash) por autor.

---

## 5. Poniendo a trabajar a la IA

1.  **Generación de mensajes de commit**

    * Herramientas como GitHub Copilot u OpenAI pueden sugerir mensajes de commit limpios y convencionales a partir de tu diff.
    * Integra un pre-commit hook que ejecute `ai-commit --preview` para redactar el mensaje para su revisión.

2.  **Descripción de PR y changelog**

    * Usa un asistente de IA para resumir todos los commits bajo un ticket en una descripción de PR coherente o una nota de versión:

      > “Resume los cambios en feature/FT-103 en puntos de viñeta.”

3.  **Asistencia en revisión de código**

    * Linters con IA (SonarQube con plugins de IA, DeepCode) pueden señalar problemas en rutas de código específicas por país.

4.  **Automatización de cherry-picks/rebases**

    * Escribe un pequeño script (o usa una plataforma low-code) que, cuando FT-103 aterrice en `main`, automáticamente haga cherry-pick en cada `uat_*` y abra PRs para cualquier conflicto de fusión.

---

### Integrando todo

1.  **Desarrolla en** `feature/FT-XXX-<cn/sg/tw>`.
2.  **Confirma cambios (commit) libremente** (pasos numerados OK), referenciando la clave JIRA.
3.  **Abre un PR** → main; elige **Squash-and-merge** para que cada FT-XXX sea un commit limpio.
4.  **El trabajo de CI** automáticamente rebasa/fusiona ese commit en cada `uat_cn`, `uat_sg`, `uat_tw`.
5.  **Los perfiles de Spring** en tiempo de ejecución eligen la lógica correcta del país—sin duplicación de código en tres ramas.
6.  **Las herramientas de IA** ayudan a hacer cumplir el estilo de commits, resumir PRs y gestionar fusiones.

Este flujo de trabajo mantiene tu historial ordenado, asegura que cada ticket sea rastreable hasta un único commit en todos los entornos, separa la lógica de país en tiempo de ejecución en lugar de en el historial de Git, y aprovecha la IA donde agrega más valor.