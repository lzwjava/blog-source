---
audio: false
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Corrección del Error de Búsqueda Web de LibreChat en OpenRouter
translated: true
type: note
---

El error **"404 No endpoints found that support tool use"** al usar la función de búsqueda web en LibreChat con OpenRouter es un problema conocido. Esto es lo que sucede y cómo solucionarlo:

---

## **Por qué sucede esto**
- **No todos los modelos en OpenRouter admiten el "tool use"** (como búsqueda web, function calling, etc.)—solo un subconjunto lo hace. Si seleccionas un modelo que no admite herramientas, obtendrás este error 404.
- OpenRouter requiere que **elijas explícitamente un modelo que admita tool/function calling** para que funciones como la búsqueda web funcionen.
- La configuración de LibreChat también puede anular los endpoints si no está configurada correctamente, lo que genera problemas de enrutamiento.

---

## **Cómo solucionarlo**

### 1. **Selecciona un modelo que admita herramientas**
- Ve a la [lista de modelos de OpenRouter](https://openrouter.ai/models) y **filtra por "tools"** en la barra lateral. Solo los modelos con soporte para herramientas funcionarán con la función de búsqueda web de LibreChat.
- Modelos recomendados: Busca aquellos etiquetados como que admiten "function calling" o "tools" (por ejemplo, algunas versiones de GPT-4, Claude u otros modelos avanzados).

### 2. **Actualiza la configuración de LibreChat**
- **No uses `OPENROUTER_API_KEY`** en tu configuración de LibreChat, ya que podría anular el endpoint de OpenAI y causar conflictos.
- En `librechat.yaml`, asegúrate de que tu endpoint de OpenRouter esté configurado correctamente y no esté bloqueado por "Ignored Providers" o restringido por "Allowed Providers".

### 3. **Elimina las restricciones del proveedor**
- En la configuración de OpenRouter, **desbloquea todos los "Ignored Providers"** y **limpia los "Allowed Providers"** para garantizar que LibreChat pueda acceder a todos los endpoints disponibles.

### 4. **Reinicia LibreChat**
- Después de realizar estos cambios, reinicia LibreChat para aplicar la nueva configuración.

---

## **¿Aún no funciona?**
- Consulta la [documentación de LibreChat sobre endpoints personalizados](https://www.librechat.ai/docs/quick_start/custom_endpoints) para una configuración avanzada.
- Si el problema persiste, intenta cambiar a la API oficial de OpenAI (si tienes acceso) u otro proveedor que admita tool use.