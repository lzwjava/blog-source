---
audio: false
generated: true
image: false
lang: es
layout: post
title: Desactivar caché en Claude Code
translated: true
type: note
---

En **Claude Code**, ese fragmento

```json
"cache_control": {
  "type": "ephemeral"
}
```

significa que la respuesta (o artefacto) producida por el modelo **no se almacena en caché para reutilización**.

### Por qué existe

Normalmente, Claude Code (y otros SDKs de Anthropic) pueden almacenar respuestas en caché para acelerar los procesos si envías el mismo prompt nuevamente. Pero cuando configuras `"cache_control": { "type": "ephemeral" }`, le estás diciendo a la API:

* **No guardes este resultado en la caché**.
* **No lo reutilices** si llega otra solicitud idéntica más tarde.
* Trata la respuesta como **de corta duración**—solo para esta llamada.

### Cuándo usarlo

Esto es útil si:

* Tu solicitud incluye **datos sensibles o personales** que no quieres que se almacenen en caché.
* Estás enviando **consultas únicas** que no se beneficiarían de la reutilización.
* Quieres **salida fresca** cada vez, incluso si el texto de la solicitud es idéntico.

En resumen, `"ephemeral"` hace que la salida de Claude sea *transitoria*—privada para esta interacción, sin almacenamiento en caché entre llamadas.

¿Te gustaría que también explique cómo se diferencia esto del comportamiento predeterminado de `cache_control` en Claude Code (por ejemplo, `type: "default"` vs `"none"` vs `"ephemeral"`)?