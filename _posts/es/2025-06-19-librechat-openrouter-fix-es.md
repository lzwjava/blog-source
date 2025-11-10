---
audio: false
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Corrección del Error de Modelo OpenRouter en LibreChat
translated: true
type: note
---

Este error ocurre al usar **LibreChat** con **OpenRouter** como backend, y el modelo seleccionado (`gpt-5-chat` o similar) no está disponible o no está enrutado correctamente. Aquí tienes un desglose del problema y cómo resolverlo:

---

## **Por qué ocurre este error**
- **OpenRouter** actúa como un proxy para varios modelos de IA, pero no todos los modelos están disponibles o habilitados por defecto.
- El error `404 No endpoints found that support tool use` significa que el modelo que seleccionaste (`gpt-5-chat`) es:
  - No compatible con OpenRouter.
  - No configurado en tu instalación de LibreChat.
  - Requiere un proveedor o clave API diferente.

---

## **Cómo solucionarlo**

### 1. **Verifica los modelos disponibles en OpenRouter**
- Visita la [lista de modelos de OpenRouter](https://openrouter.ai/models) para ver qué modelos están disponibles.
- Hasta ahora, `gpt-5-chat` no es un modelo oficial de OpenAI (el más reciente es GPT-4o). Si te referías a GPT-4, usa `openai/gpt-4` o similar.

### 2. **Actualiza la configuración de LibreChat**
- En LibreChat, ve a **Configuración** > **Selección de modelo**.
- Elige un modelo que sea **compatible con OpenRouter** (por ejemplo, `openai/gpt-4`, `mistralai/mistral-7b`, etc.).
- Si deseas usar OpenAI directamente, cambia el **Proveedor de API** a **OpenAI** en lugar de OpenRouter.

### 3. **Verifica las claves API**
- Asegúrate de tener una **clave API de OpenRouter** válida (si usas OpenRouter) o una **clave API de OpenAI** (si usas OpenAI).
- Añade la clave en **Configuración** > **Claves API** de LibreChat.

### 4. **Reinicia LibreChat**
- Después de cambiar la configuración, reinicia LibreChat para aplicar los cambios.

### 5. **Consulta la documentación de LibreChat**
- Consulta la [guía de configuración de OpenRouter para LibreChat](https://github.com/danny-avila/LibreChat#openrouter) para obtener instrucciones detalladas.

---

## **Soluciones alternativas**
- Si deseas usar los modelos de OpenAI, configura el proveedor a **OpenAI** y selecciona `gpt-4`, `gpt-4o` o `gpt-3.5-turbo`.
- Si deseas usar OpenRouter, elige un modelo de su [lista de modelos compatibles](https://openrouter.ai/models).

---