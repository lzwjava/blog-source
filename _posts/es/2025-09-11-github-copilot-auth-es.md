---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Flujo de Autenticación de GitHub Copilot
translated: true
type: note
---

Buena pregunta — el flujo de autenticación de GitHub Copilot es básicamente una **concesión de código de dispositivo OAuth2 estándar**, pero con algunos tokens específicos de GitHub añadidos para el servicio Copilot en sí. Permíteme desglosarlo paso a paso:

---

### 1. **Flujo de Dispositivo (`/login/device/code`)**

* Cuando inicias sesión por primera vez, el cliente de Copilot (por ejemplo, la extensión de VS Code, el plugin de JetBrains o la CLI) llama al endpoint OAuth de GitHub:

  ```
  POST https://github.com/login/device/code
  ```
* Envía el **client\_id** (específico para GitHub Copilot).
* GitHub responde con:

  * `device_code` (código interno usado para el sondeo),
  * `user_code` (el que ves e ingresas en tu navegador),
  * `verification_uri` (la URL que visitas para ingresar el código),
  * `interval` (con qué frecuencia debe sondear el cliente).

---

### 2. **Sondeo para el Token de Acceso**

* El cliente de Copilot luego sondea:

  ```
  POST https://github.com/login/oauth/access_token
  ```
* Incluye el `device_code` y el `client_id`.
* Una vez que has aprobado en tu navegador, GitHub devuelve:

  * `access_token` (un **token OAuth de GitHub** con alcance para el uso de Copilot),
  * `token_type=bearer`,
  * `expires_in` (tiempo de vida).

Este `access_token` es un **token OAuth2 normal de GitHub**.

---

### 3. **Intercambio por el Token `copilot_internal`**

* El cliente de Copilot no puede llamar a las APIs de Copilot directamente con el token OAuth de GitHub.
* En su lugar, lo intercambia con el servicio Copilot:

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* La respuesta es:

  ```json
  {
    "token": "<copilot_internal token>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* Este **token `copilot_internal` v2** es lo que el cliente de Copilot usa para comunicarse con el **servicio de inferencia de Copilot** (por ejemplo, `https://copilot-proxy.githubusercontent.com`).

---

### 4. **Uso del Token `copilot_internal`**

* Todas las solicitudes posteriores de finalizaciones o chat se autentican con:

  ```
  Authorization: Bearer <copilot_internal token>
  ```
* Este token tiene un tiempo de vida corto (generalmente \~1 hora) y está vinculado a tu cuenta de GitHub y el estado de suscripción a Copilot.
* El cliente lo actualiza periódicamente volviendo a intercambiar el token de acceso OAuth de GitHub.

---

✅ **En resumen:**

* `/login/device/code` → te da un código para autenticarte en el navegador.
* `/login/oauth/access_token` → te da un token OAuth de GitHub.
* `/copilot_internal/v2/token` → intercambia eso por un token de Copilot de corta duración, que es la *verdadera* credencial utilizada para las finalizaciones.

---

¿Te gustaría que también dibuje los **ejemplos exactos de solicitud/respuesta** (con encabezados y JSON de ejemplo) para que puedas ver cómo son los payloads en la práctica?