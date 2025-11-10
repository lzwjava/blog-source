---
audio: false
generated: true
image: false
lang: es
layout: post
title: Puente API de GitHub Copilot
translated: true
type: note
---

Has aterrizado en **ericc-ch/copilot-api**, un proyecto de GitHub que transforma **GitHub Copilot** en un servidor API local compatible con las APIs de **OpenAI** y **Anthropic** (por ejemplo, Claude).

Aquí tienes un desglose más claro—sin tablas, solo información directa:

---

### ¿Qué es esto?

* Es un **proxy de ingeniería inversa** que te permite interactuar con GitHub Copilot utilizando endpoints familiares al estilo de OpenAI, como `/v1/chat/completions`, `/v1/models` y `/v1/embeddings`. También puedes usar endpoints compatibles con Anthropic, como `/v1/messages` ([GitHub][1]).

* Básicamente, esto permite que herramientas que admiten las APIs de OpenAI o Anthropic—como Claude Code—utilicen GitHub Copilot como su backend ([GitHub][1]).

---

### Características Principales

* **Compatibilidad con OpenAI & Anthropic**: Funciona como la API real de OpenAI o Anthropic ([GitHub][1]).
* **Integración con Claude Code**: Listo para conectarse a Claude Code con un flag `--claude-code` ([GitHub][1]).
* **Panel de Uso**: Monitorea tu uso y cuotas de la API de Copilot a través de una interfaz web integrada ([GitHub][1]).
* **Límites de Tasa y Controles de Aprobación**: Incluye opciones para limitar la tasa de solicitudes (`--rate-limit`), espera automática (`--wait`), aprobación manual (`--manual`) y depuración (mostrando tokens)—ideal para evitar los sistemas de abuso de GitHub ([GitHub][1]).
* **Admite Varios Planes de Copilot**: Funciona con cuentas individuales, empresariales o enterprise ([GitHub][1]).

---

### Configuración y Uso

* **Prerrequisitos**: Necesitarás Bun (≥ 1.2.x) y una suscripción a GitHub Copilot ([GitHub][1]).
* **Opciones de Instalación**:

  * **Docker**:

    ```bash
    docker build -t copilot-api .
    docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
    ```

    O pasa tu token de GitHub directamente mediante `GH_TOKEN` ([GitHub][1]).
  * **npx**:

    ```bash
    npx copilot-api@latest start --port 8080
    ```

    O `npx copilot-api@latest auth` solo para autenticar ([GitHub][1]).
* **Estructura de Comandos**:

  * `start`: Inicia el servidor API (maneja la autenticación si es necesario).
  * `auth**: Activa el inicio de sesión de GitHub sin ejecutar el servidor.
  * `check-usage`: Muestra el uso actual de Copilot en tu terminal.
  * `debug`: Muestra información de diagnóstico (versiones, estado de autenticación, etc.), con salida opcional `--json` ([GitHub][1]).

---

### Opiniones Reales

Usuarios de Reddit han comentado:

> “Este proyecto te permite convertir copilot en un endpoint compatible con openai.” ([Reddit][2])
> “Es un proyecto increíble para hacer tu …” ([Reddit][3])

---

### Advertencias Importantes

* **No Oficial y Sin Soporte**: Esto **no** es un producto oficial de GitHub y podría dejar de funcionar en cualquier momento ([GitHub][1]).
* **Riesgo de Detección de Abuso**: Un uso intensivo o automatizado podría activar la protección contra abuso de GitHub y podría suspender tu acceso a Copilot ([GitHub][1]).
* **Posibles Problemas de Límite de Tasa**: Algunos usuarios han reportado errores como `421 Misdirected Request`, y el mantenedor pausó el desarrollo mientras investiga ([GitHub][4]).

---

### Resumen (Sin Tablas Necesarias)

* **Qué Hace**: Expone GitHub Copilot como si fuera una API de OpenAI/Anthropic.
* **Por Qué es Importante**: Hace que Copilot sea utilizable en herramientas que esperan esas APIs—como Claude Code.
* **Cómo Usarlo**: Instala vía Docker o npx; ejecuta comandos para iniciar, autenticar o monitorear el uso.
* **Procede con Precaución**: Es útil, pero no oficial, y los límites de tasa o salvaguardas de seguridad de GitHub pueden afectar un uso intensivo.

---

¡Avísame si necesitas ayuda para configurarlo, o si tienes curiosidad sobre cómo integrarlo en un proyecto o herramienta específica!

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"