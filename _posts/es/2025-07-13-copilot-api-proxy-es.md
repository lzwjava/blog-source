---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Servidor Proxy de la API de Copilot
translated: true
type: note
---

El repositorio de GitHub `ericc-ch/copilot-api` es un proyecto de TypeScript de código abierto que ofrece un servidor proxy de ingeniería inversa para acceder a la funcionalidad de IA de GitHub Copilot como una API compatible con OpenAI y Anthropic. Permite la integración con herramientas como Claude Code, lo que permite a los usuarios aprovechar las funciones de generación y finalización de código de Copilot a través de un formato de API estandarizado. Según los datos más recientes, tiene más de 1,200 estrellas y 203 bifurcaciones en GitHub.[1][2][3]

### Cómo Funciona
Este proxy está diseñado para exponer la API subyacente de GitHub Copilot, que no está disponible públicamente por GitHub, pero utiliza ingeniería inversa para interceptar y redirigir las solicitudes. Aquí hay un desglose de su funcionalidad:

- **Mecanismo Proxy**: El servidor actúa como un middleware entre las aplicaciones cliente (por ejemplo, herramientas que esperan APIs al estilo de OpenAI o Anthropic) y el servicio Copilot de GitHub. Transforma las solicitudes entrantes al formato que Copilot espera y retransmite las respuestas en una salida compatible.[1][2]

- **Compatibilidad de API**: Específicamente, imita el comportamiento de los modelos GPT de OpenAI y los modelos Claude de Anthropic, permitiendo la integración con las herramientas de desarrollo existentes sin necesidad de los clientes nativos de Copilot. Las actualizaciones recientes (por ejemplo, la versión v0.5.14) han incluido correcciones para problemas como el manejo de URLs de imágenes y optimizaciones para herramientas como Claude Code.[1][4][2]

- **Configuración y Uso**:
  - Clonar o descargar el repositorio.
  - Instalar las dependencias (usando npm o similar para TypeScript).
  - Ejecutar el servidor, normalmente con autenticación a tu cuenta de GitHub Copilot (ya que requiere una suscripción válida a Copilot).
  - Configurar las aplicaciones cliente para que apunten al endpoint del proxy en lugar de a las APIs directas de OpenAI/Anthropic.[2][3]

- **Características y Mejoras Clave**: El proyecto incluye manejo de errores para problemas comunes (por ejemplo, errores HTTP 421 o 500 al usar con herramientas como Aider), soporte para registro (opción --log-file) y desarrollo continuo a través de pull requests que abordan correcciones de errores y mejoras.[5][6][4]

Para instrucciones detalladas, consulta el README del proyecto en GitHub. Ten en cuenta que esto no es oficial y depende de la API interna de GitHub, que podría cambiar inesperadamente.[1][2][3]

### Riesgos Potenciales
El uso de proxies de ingeniería inversa puede violar los términos de servicio de GitHub, y su fiabilidad podría verse afectada por actualizaciones de la API de Copilot.[7]

Citas:
[1] https://github.com/ericc-ch/copilot-api
[2] https://github.com/ericc-ch/copilot-api/activity
[3] https://github.com/ericc-ch
[4] https://github.com/ericc-ch/copilot-api/pulls
[5] https://github.com/ericc-ch/copilot-api/issues/7
[6] https://github.com/ericc-ch/copilot-api/issues/4
[7] https://github.com/open-webui/open-webui/discussions/14285