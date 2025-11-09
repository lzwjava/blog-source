---
audio: false
date: 2025-09-14
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Deshabilitación de Soluciones Alternativas de Autenticación de LibreChat
translated: true
type: note
---

Respuesta corta: no puedes desactivar por completo la autenticación en LibreChat, pero puedes solucionar el problema de que "siga pidiéndome que inicie sesión" y hacer que se sienta casi como "sin inicio de sesión". Esto es lo que realmente funciona (y por qué):

### 1) No puedes desactivar la autenticación por completo

Esto está confirmado por el mantenedor: el registro se puede desactivar, pero el sistema de autenticación en sí no se puede apagar. ([GitHub][1])

### 2) Por qué sigues siendo desconectado

Si accedes a tu instancia a través de **HTTP** (por ejemplo, una IP LAN), las cookies se marcan como `secure` en producción, por lo que el navegador no las guarda; te devuelve al inicio de sesión. Usa **HTTPS** (incluso auto-firmado) o ejecuta la API en un modo de desarrollo que desactive las cookies seguras. ([GitHub][1])

### 3) Dos soluciones confiables

#### Opción A — Correcta/segura (recomendada)

* Pon LibreChat detrás de HTTPS (nginx/caddy/traefik; auto-firmado está bien en LAN).
* Luego aumenta las ventanas de sesión en tu `.env`:

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24h
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30d
  ```
* Reinicia los contenedores después de cambiar el entorno.
  Esto te mantiene conectado durante días/semanas y soluciona la pérdida de cookies. ([GitHub][2])

#### Opción B — "Estoy en una LAN privada y solo quiero que deje de desconectarme"

* Crea un `docker-compose.override.yml` y ejecuta la API en modo de desarrollo (desactiva las cookies seguras):

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* `docker compose up -d` para aplicar.
  Esto es menos seguro (las cookies no son `secure`), pero detiene el re-inicio de sesión forzado a través de HTTP plano. ([librechat.ai][3])

### 4) Ajustes opcionales para la calidad de vida

* **Desactiva los nuevos registros** para que sea efectivamente de un solo usuario:

  ```
  ALLOW_REGISTRATION=false
  ```

  (Aún puedes agregar usuarios via `npm run create-user` si es necesario.) ([librechat.ai][4])
* Mantén otros interruptores de autenticación en `.env` (banderas de inicio de sesión por correo electrónico/redes sociales) si quieres la ruta de inicio de sesión más simple. ([librechat.ai][5])

### 5) Lista de verificación rápida para tu caso (v0.8.0-rc3)

1. Decide: proxy HTTPS (mejor) **o** modo de desarrollo (solución rápida para LAN).
2. Establece `SESSION_EXPIRY` y `REFRESH_TOKEN_EXPIRY` más largos en `.env`.
3. Reinicia el stack para que los cambios en el entorno surtan efecto.
4. (Opcional) Desactiva el registro para una sensación de "usuario único".

Si quieres, pega tu `docker-compose.yml` y `.env` actuales (sin secretos). Marcaré exactamente qué agregar/cambiar para tu configuración.

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"