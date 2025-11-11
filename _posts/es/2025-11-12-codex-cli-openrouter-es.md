---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de Codex CLI para OpenRouter
translated: true
type: note
---

### Configuración de Codex CLI para OpenRouter

Codex CLI (de OpenAI) es un agente de codificación basado en terminal que admite proveedores de modelos personalizados como OpenRouter a través de su archivo de configuración. OpenRouter proporciona una API compatible con OpenAI, por lo que puedes enrutar solicitudes a través de él definiendo un proveedor con la URL base adecuada. Esto permite acceder a una gama más amplia de modelos (por ejemplo, de Anthropic, Google o proveedores de código abierto) mientras se utiliza Codex.

La configuración se almacena en un archivo TOML en `~/.codex/config.toml` (crea el archivo si no existe). Definirás una sección de **proveedor de modelos** para OpenRouter y luego la referenciarás en un **perfil** para modelos específicos.

#### Paso 1: Obtén tu Clave API de OpenRouter
- Regístrate en [openrouter.ai](https://openrouter.ai) si aún no lo has hecho.
- Genera una clave API desde el panel de tu cuenta.
- Establécelo como una variable de entorno:  
  ```
  export OPENROUTER_API_KEY=tu_clave_api_aqui
  ```
  Añade esto a tu perfil de shell (por ejemplo, `~/.bashrc` o `~/.zshrc`) para que sea persistente.

#### Paso 2: Edita el Archivo de Configuración
Abre `~/.codex/config.toml` en tu editor y añade las siguientes secciones. Esto establece la URL base al endpoint de OpenRouter (`https://openrouter.ai/api/v1`), que es compatible con OpenAI (Codex añade `/chat/completions` automáticamente).

```toml
# Define el proveedor OpenRouter
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # Lee desde tu variable de entorno para la autenticación

# Define un perfil usando este proveedor (ejemplo: usando un modelo tipo GPT)
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # Reemplaza con cualquier ID de modelo de OpenRouter, ej. "anthropic/claude-3.5-sonnet"
```

- **Campos clave explicados**:
  - `base_url`: Apunta al endpoint de la API de OpenRouter. Esto anula la URL base predeterminada de OpenAI.
  - `env_key`: Especifica la variable de entorno para el encabezado de autenticación Bearer token.
  - `model`: Usa los IDs de modelo exactos de la [lista de modelos de OpenRouter](https://openrouter.ai/models). Para tareas de codificación, prueba con "openai/codex-mini-latest" o "meta-llama/llama-3.1-405b-instruct".
  - Puedes añadir múltiples perfiles para diferentes modelos (por ejemplo, `[profiles.openrouter-claude]` con `model = "anthropic/claude-3.5-sonnet"`).

#### Paso 3: Usa la Configuración
- Instala Codex CLI si es necesario: `npm install -g @openai/codex` (o vía Homebrew: `brew install codex`).
- Ejecuta Codex con tu perfil:  
  ```
  codex --profile openrouter-gpt
  ```
  O establece un perfil predeterminado en la configuración:  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- Pruébalo: Ejecuta `codex` y dale un prompt de codificación simple. Revisa el panel de OpenRouter para ver el uso.

#### Resolución de Problemas
- **Errores de autenticación**: Asegúrate de que `OPENROUTER_API_KEY` esté establecida y exportada.
- **Modelo no encontrado**: Verifica el ID del modelo en OpenRouter—es sensible a mayúsculas y tiene prefijo (por ejemplo, "proveedor/nombre-del-modelo").
- **Verificación de versión**: Usa Codex CLI v0.13+ para soporte completo de proveedores. Actualiza con `npm update -g @openai/codex`.
- **Enrutamiento avanzado**: Para características específicas de OpenRouter como el enrutamiento optimizado por costos, añade parámetros opcionales como `provider = { sort = "price" }` bajo el perfil (compatible en versiones más recientes).

Esta configuración mantiene tus solicitudes compatibles con la API de estilo OpenAI de Codex mientras aprovechas el ecosistema de OpenRouter. Para más detalles, consulta la [documentación de Codex CLI en npm](https://www.npmjs.com/package/@openai/codex) o la [guía de API de OpenRouter](https://openrouter.ai/docs). Si estás usando un fork como Open Codex, la configuración es similar pero puede tener soporte adicional para Gemini.