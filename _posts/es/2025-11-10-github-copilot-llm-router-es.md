---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración del Enrutador LLM de GitHub Copilot
translated: true
type: note
---

Para configurar tu enrutador de LLM para usar exclusivamente la API de LLM de GitHub Copilot en un entorno empresarial, agrega un proveedor dedicado para ello y ajusta la configuración del enrutador para dirigir todo el tráfico a través de ese proveedor.

- **Agregar un Proveedor de GitHub Copilot**: Incluye una nueva entrada en el array "Providers" con la URL base de la API apropiada, tu token de acceso personal (PAT) de GitHub como clave de API y los modelos compatibles.
- **Actualizar los Valores Predeterminados del Enrutador**: Cambia todos los campos del enrutador (por ejemplo, "default", "think") para que apunten únicamente al nuevo nombre del proveedor, asegurando que no se llamen a otros proveedores.
- **Manejar Restricciones Empresariales**: Usa el PAT de tu cuenta empresarial de GitHub con los scopes necesarios y aprovecha la "PROXY_URL" existente si tu entorno requiere enrutamiento por proxy para cumplimiento.
- **Probar y Verificar**: Después de las actualizaciones, valida que todas las llamadas a la API se dirijan solo al endpoint de Copilot para alinearse con las políticas que permiten únicamente interacciones con la API de Copilot.

### Configuración Paso a Paso
1. **Generar un PAT de GitHub**: Inicia sesión en tu cuenta empresarial de GitHub y crea un token de acceso personal con scopes como `copilot` para acceso al chat o `models:read` para una inferencia de modelos más amplia. Esto asegura una autenticación segura sin exponer permisos más amplios.
2. **Modificar el Array de Proveedores**: Añade un nuevo objeto a la lista "Providers" en tu JSON de configuración. Establece "name" en algo descriptivo como "github_copilot", "api_base_url" en "https://api.githubcopilot.com/chat/completions" (para agentes de Copilot) o "https://models.github.ai/inference/chat/completions" (para inferencia general de GitHub Models), "api_key" en tu PAT, y lista los modelos compatibles.
3. **Ajustar la Sección del Enrutador**: Reemplaza todos los valores en el objeto "Router" con tu nuevo nombre de proveedor (por ejemplo, "github_copilot") para imponer el uso exclusivo. Esto evita el fallback a otros proveedores como OpenRouter.
4. **Consideraciones Empresariales**: En entornos restringidos, confirma que tus políticas de red permitan llamadas salientes a los dominios de GitHub. Si es necesario, actualiza "PROXY_URL" para enrutar a través de un proxy empresarial aprobado. Habilita el registro ("LOG": true) para auditar las llamadas y asegurar el cumplimiento.

### Ejemplo de Configuración Actualizada
Así es como podría verse tu configuración después de las modificaciones (reemplaza los marcadores de posición con tu PAT real y el endpoint preferido):

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "z-ai/glm-4.6",
        "x-ai/grok-code-fast-1",
        "x-ai/grok-4-fast",
        "minimax/minimax-m2",
        "moonshotai/kimi-k2-thinking"
      ],
      "transformer": {
        "use": [
          "openrouter"
        ]
      }
    },
    {
      "name": "github_copilot",
      "api_base_url": "https://api.githubcopilot.com/chat/completions",
      "api_key": "ghp_YourPersonalAccessTokenHere",
      "models": [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620"
      ],
      "transformer": {
        "use": [
          "github_copilot"
        ]
      }
    }
  ],
  "Router": {
    "default": "github_copilot",
    "background": "github_copilot",
    "think": "github_copilot",
    "longContext": "github_copilot",
    "longContextThreshold": 30000,
    "webSearch": "github_copilot"
  }
}
```

Esta configuración asegura que el enrutador solo interactúe con la API de Copilot, cumpliendo con las políticas empresariales que restringen las llamadas a endpoints aprobados.

---

En entornos empresariales, la integración de APIs de LLM como GitHub Copilot requiere una configuración cuidadosa para adherirse a las políticas de seguridad, que a menudo limitan las llamadas salientes a servicios específicos aprobados. La configuración del enrutador proporcionada parece ser una configuración personalizada para enrutar solicitudes de LLM a través de proveedores, similar a herramientas como OpenRouter o LiteLLM, donde "Providers" define los endpoints de la API y los modelos, y "Router" dicta el enrutamiento específico por categoría o fallback. Para adaptar esto para el uso exclusivo de la API de LLM de GitHub Copilot—asegurando que no se invoquen otros servicios externos—necesitarás incorporar Copilot como un proveedor y aplicarlo en todas las rutas del enrutador. Este enfoque admite escenarios donde los firewalls empresariales o las reglas de cumplimiento permiten solo APIs alojadas en GitHub, aprovechando la interfaz compatible con OpenAI de Copilot para finalizaciones de chat.

GitHub Copilot proporciona acceso a LLM principalmente a través de dos vías: el endpoint de LLM de Copilot dedicado para construir agentes y extensiones, y la API más amplia de GitHub Models para inferencia general. El endpoint específico de Copilot en `https://api.githubcopilot.com/chat/completions` está adaptado para el desarrollo de agentes de grado empresarial, compatible con solicitudes POST en el formato de finalizaciones de chat de OpenAI. La autenticación utiliza un token Bearer derivado de un token de acceso personal (PAT) de GitHub, típicamente pasado a través de un encabezado `Authorization`. Por ejemplo, una solicitud de muestra podría incluir encabezados como `Authorization: Bearer <tu-pat>` y `Content-Type: application/json`, con un cuerpo que contenga `messages` (un array de prompts de usuario/sistema) y parámetros opcionales como `stream: true` para respuestas en tiempo real. Los modelos no se enumeran explícitamente en la documentación pero se alinean con los proveedores subyacentes de Copilot, como variantes de GPT-4 y modelos de Claude, con límites de tasa estrictos aplicados a agentes de terceros para prevenir abusos.

Alternativamente, la API de GitHub Models en `https://models.github.ai/inference/chat/completions` ofrece un servicio de inferencia más versátil, permitiendo el acceso a un catálogo de modelos usando solo las credenciales de GitHub. Esto es ideal para prototipado e integración en flujos de trabajo como GitHub Actions. La autenticación requiere un PAT con el scope `models:read`, creado a través de la configuración de GitHub (https://github.com/settings/tokens). En configuraciones empresariales, esto puede extenderse a tokens a nivel de organización o usarse en pipelines de CI/CD agregando `permissions: models: read` a los archivos YAML del flujo de trabajo. Los modelos disponibles incluyen estándares de la industria como `openai/gpt-4o`, `openai/gpt-4o-mini`, `anthropic/claude-3-5-sonnet-20240620`, la serie Llama 3.1 de Meta y variantes de Mistral, todos invocables a través del mismo formato de API compatible con OpenAI. Esta compatibilidad facilita encajarlo en tu configuración de enrutador sin cambios importantes en el código downstream.

Para configuraciones específicas empresariales, GitHub Copilot Enterprise mejora el Copilot estándar con controles a nivel de organización, como modelos ajustados basados en tu base de código, pero el acceso a la API sigue los mismos patrones. La gestión de red es crucial: Puedes configurar el enrutamiento basado en suscripción para asegurar que el tráfico de Copilot use rutas aprobadas, requiriendo que los usuarios actualicen sus extensiones de IDE (por ejemplo, VS Code) a versiones mínimas que admitan esto. Si tu entorno obliga al uso de proxies, actualiza la "PROXY_URL" en la configuración para que apunte a tu servidor proxy empresarial y considera certificados personalizados para inspección SSL. Herramientas como LiteLLM pueden actuar como un proxy intermediario para un mayor control—instálalo via `pip install litellm[proxy]`, define los modelos en una configuración YAML, inicia el servidor en un puerto local y redirige las solicitudes de Copilot a través de él para registro, límite de tasa y manejo de fallback. Sin embargo, en tu caso, dado que el objetivo es la exclusividad, evita los fallbacks en el enrutador para cumplir con las políticas de "solo está bien llamar a Copilot".

Para implementar esto en tu configuración, comienza añadiendo un nuevo objeto de proveedor. Elige el endpoint según tu caso de uso: Usa el endpoint de agente de Copilot si estás construyendo extensiones, o GitHub Models para el enrutamiento general de LLM. Enumera los modelos que se superpongan con los existentes (por ejemplo, variantes de Claude y GPT) para mantener la compatibilidad. Luego, sobrescribe todos los campos de "Router" para que referencien solo este nuevo proveedor, eliminando comas o fallbacks como ",minimax/minimax-m2". Habilita el registro para monitorear el cumplimiento y prueba simulando solicitudes para verificar que no se alcancen endpoints no autorizados. Si se integra con VS Code u otros IDEs, ajusta configuraciones como `github.copilot.advanced.debug.overrideProxyUrl` para enrutar a través de tu proxy configurado si es necesario.

Aquí hay una tabla de comparación de las dos principales opciones de API de LLM de GitHub para ayudar a decidir qué endpoint usar en tu configuración de proveedor:

| Aspecto                  | API de LLM de GitHub Copilot (para Agentes)         | API de GitHub Models                                |
|-------------------------|-----------------------------------------------------|-----------------------------------------------------|
| Endpoint                | https://api.githubcopilot.com/chat/completions      | https://models.github.ai/inference/chat/completions |
| Uso Principal           | Construir extensiones y agentes de Copilot          | Prototipado general, inferencia y flujos de trabajo |
| Autenticación           | PAT Bearer (vía encabezado Authorization)           | PAT con scope models:read                           |
| Modelos Soportados      | Implícitos (por ejemplo, GPT-4, variantes de Claude)| Catálogo explícito: gpt-4o, claude-3-5-sonnet, Llama 3.1, etc. |
| Características Empresariales | Límites de tasa para terceros; se integra con Copilot Enterprise | Utilizable en GitHub Actions; soporta bring-your-own-key |
| Límites de Tasa/Cuotas  | Estrictos para agentes no-GitHub                    | Nivel gratuito para prototipado; escalable para empresa |
| Compatibilidad          | Formato de chat de OpenAI                           | Compatible con OpenAI; integración fácil en enrutador |

Esta tabla resalta por qué GitHub Models podría ser preferible para un uso amplio en enrutadores, ya que ofrece una selección de modelos más explícita e integración con flujos de trabajo empresariales.

Los desafíos potenciales incluyen la expiración del token (los PATs típicamente duran 30-90 días), así que automatiza la renovación en scripts empresariales. Si tu entorno usa GitHub Enterprise Cloud, habilita Copilot a nivel de organización para un acceso sin problemas. Para configuraciones avanzadas, explora bring your own API keys (BYOK) en GitHub Models para enrutar a través de proveedores preferidos mientras te mantienes dentro del ecosistema de GitHub. Prioriza siempre la documentación principal de GitHub para los últimos scopes y endpoints, ya que las características evolucionan rápidamente. Si las llamadas directas a la API fallan debido a restricciones de red, considera usar las opciones de configuración de proxy de GitHub o integrar con Azure para implementaciones empresariales híbridas.

En resumen, esta configuración transforma tu enrutador en un sistema exclusivo de Copilot, alineándose con las políticas empresariales mientras mantiene la funcionalidad para tareas relacionadas con código o generales de LLM.

**Citas Clave:**
- [Using GitHub Copilot's LLM for your agent](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-extensions/build-a-copilot-agent/use-copilots-llm)
- [Quickstart for GitHub Models](https://docs.github.com/en/github-models/quickstart)
- [GitHub Copilot | liteLLM](https://docs.litellm.ai/docs/tutorials/github_copilot_integration)
- [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/enterprise-cloud%40latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/manage-network-access)
- [Configuring network settings for GitHub Copilot](https://docs.github.com/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot)
- [Prototyping with AI models](https://docs.github.com/github-models/prototyping-with-ai-models)
- [Using your own API keys in GitHub Models](https://docs.github.com/en/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)