---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corrección de Configuración de Enrutamiento de Código Claude DeepSeek
translated: true
type: note
---

Entendido. Tu configuración está enviando **tráfico de estilo Anthropic de Claude Code** al **endpoint de estilo OpenAI de OpenRouter** para DeepSeek V3.1. Cuando Claude Code (el agente del IDE) intenta usar herramientas/plan/flujo continuo, el esquema del mensaje no coincide → errores.

A continuación, una forma limpia de configurarlo para que **los modelos Anthropic** sigan usando una pasarela de estilo Anthropic, mientras que **DeepSeek V3.1** (estilo OpenAI) permanezca en `/chat/completions`. Te mostraré las ediciones exactas que puedes pegar.

---

### 1) Verifica el slug de DeepSeek V3.1

El slug del modelo de chat en OpenRouter es:

```
deepseek/deepseek-chat-v3.1
```

(Ese es el modelo instruct/chat—distinto del modelo "base"). ([OpenRouter][1])

---

### 2) Añade un proxy con formato Anthropic para Claude Code

Claude Code espera **Mensajes Anthropic** (`/messages`, bloques `tool_use`). La solución más simple es ejecutar un pequeño proxy que convierta Anthropic→OpenAI (OpenRouter) y viceversa. Hay uno listo para usar: **maxnowack/anthropic-proxy**. Inícialo así (la variable de entorno es tu clave de OpenRouter):

```bash
OPENROUTER_API_KEY=TU_CLAVE npx anthropic-proxy
```

Escucha localmente y traduce los esquemas por ti. ([GitHub][2])

Ahora, añade un **segundo proveedor** que dirija el tráfico de Claude Code a ese proxy.

#### 🔧 Reemplaza tu JSON con estos cambios específicos

**Añade este proveedor (mantén tu proveedor `openrouter` actual tal cual):**

```json
{
  "name": "anthropic-proxy",
  "api_base_url": "http://127.0.0.1:3000/v1/messages",
  "api_key": "", 
  "models": [
    "anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4"
  ]
}
```

**Mantén tu proveedor OpenRouter existente (es correcto usar `/chat/completions` para DeepSeek y otros modelos con esquema OpenAI).** OpenRouter normaliza a un esquema compatible con OpenAI y soporta extras como tokens de razonamiento, herramientas, etc. ([OpenRouter][3])

---

### 3) Dirige los modelos al proveedor correcto

Dirige los modelos Anthropic al **anthropic-proxy**; dirige DeepSeek/GPT/Gemini/Qwen a **openrouter**.

Ejemplo de bloque Router que puedes incluir:

```json
"Router": {
  "default": "openrouter,openai/gpt-5-mini",

  "background": "openrouter,google/gemini-2.5-flash",
  "think": "openrouter,qwen/qwen3-coder",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "longContextThreshold": 2000,
  "webSearch": "openrouter,mistralai/mistral-medium-3.1",

  "overrides": {
    "anthropic/claude-sonnet-4": "anthropic-proxy,anthropic/claude-sonnet-4",
    "anthropic/claude-3.5-sonnet": "anthropic-proxy,anthropic/claude-3.5-sonnet",
    "anthropic/claude-3.7-sonnet:thinking": "anthropic-proxy,anthropic/claude-3.7-sonnet:thinking",
    "anthropic/claude-opus-4": "anthropic-proxy,anthropic/claude-opus-4",

    "deepseek/deepseek-chat-v3.1": "openrouter,deepseek/deepseek-chat-v3.1"
  }
}
```

> Si tu router no soporta un mapa `overrides`, el equivalente es: crea "perfiles" separados en tu aplicación (ej., "Claude Code via anthropic-proxy" vs "Chat general via openrouter") y elige el perfil por acción.

---

### 4) Evita colisiones de flujo de razonamiento en DeepSeek (opcional pero más seguro)

DeepSeek V3.1 soporta **tokens de "pensamiento"**. Muchos wrappers fallan si estos aparecen a mitad del flujo. En OpenRouter puedes **excluir el razonamiento** con un flag en la petición. Si tu router te permite establecer parámetros por modelo, adjunta:

```json
"params": {
  "reasoning": { "exclude": true }
}
```

(o `include_reasoning: false` dependiendo de la nomenclatura de parámetros de tu router). Esto evita que el contenido `