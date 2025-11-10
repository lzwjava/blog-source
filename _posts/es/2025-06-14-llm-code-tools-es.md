---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Modelos de Lenguaje Grandes, Razonamiento de Código y Uso de Herramientas
translated: true
type: note
---

¡Excelente pregunta! Básicamente estás preguntando cómo algo como **Claude de Anthropic (y otros LLMs similares)** maneja internamente:

1.  **La ejecución de código o el razonamiento relacionado con código**
2.  **La validación de esquemas JSON/verificación de salidas estructuradas**
3.  **El uso de herramientas y el enrutamiento entre ellas**

Permíteme desglosarlo en detalle.

---

### 1. Razonamiento y ejecución de código
Claude (y otros LLMs de vanguardia) en realidad no *ejecutan* código directamente dentro del modelo; **simulan el razonamiento de código** prediciendo tokens de código o pasos lógicos.

- En el **modo de texto normal**, Claude puede "escribir" código continuando un patrón, pero no lo ejecuta internamente.
- Cuando se usa con un **backend (como Anthropic's Workbench, o el Code Interpreter de OpenAI)**, el sistema puede capturar esos fragmentos de código y luego *ejecutarlos* realmente en un entorno aislado (sandbox).
- Los resultados pueden luego ser alimentados de vuelta al modelo como contexto, para que pueda encadenar razonamientos como:
  → Generar código → Ejecutar externamente → Recibir salida → Decidir el siguiente paso.

Así que la inteligencia está en el bucle: el LLM genera → un ejecutor externo ejecuta → el LLM interpreta los resultados.

---

### 2. Verificación de esquemas JSON
Muchas APIs (Claude, OpenAI, etc.) ahora admiten un **modo de salida estructurada**, donde puedes adjuntar un esquema JSON. Así es como funciona internamente:

- Pasas una **definición de esquema JSON** con tu solicitud.
- Se guía al LLM para que genere **solo JSON válido** que se ajuste al esquema.
- Si intenta generar JSON inválido, el sistema lo detecta (usando un validador como [jsonschema](https://pypi.org/project/jsonschema/)) y le pide al modelo que "repare" la salida.
- Internamente, esto a menudo es un mecanismo de **decodificación restringida** o **decodificación basada en gramática**: básicamente, restringe la generación de tokens para que solo se permitan los `"siguientes tokens válidos en el esquema"`.

Esto garantiza que la salida sea JSON sintáctica y semánticamente correcto, lo cual es crítico para la automatización del uso de herramientas.

---

### 3. Uso de herramientas y enrutamiento
El uso de herramientas se maneja mediante algo como una **capa de enrutador** entre el LLM y un entorno de ejecución de herramientas:

- **Lógica de enrutamiento**: Se le pide al modelo que *decida qué herramienta llamar* (o que responda directamente).
- **Aplicación de esquemas**: Cada herramienta tiene un esquema de entrada. Se requiere que el LLM produzca JSON válido para esa herramienta.
- **Adaptadores de ejecución**: La capa de orquestación (fuera del modelo) toma el JSON del LLM, lo valida contra el esquema, ejecuta la herramienta y luego alimenta los resultados de vuelta como contexto.
- **Razonamiento encadenado (estilo ReAct)**: El LLM "piensa en voz alta" (puede producir pasos de razonamiento ocultos para el usuario), luego emite llamadas a herramientas cuando es necesario, llegando progresivamente a una respuesta final.

Por ejemplo:
```json
{
  "tool": "web_search",
  "query": "latest research on quantum error correction"
}
```
→ El enrutador ve `"tool": "web_search"`, valida el esquema, ejecuta la búsqueda web, coloca los resultados de vuelta en el contexto del modelo, y el modelo continúa razonando.

Claude de Anthropic, los GPTs de OpenAI, LangChain y otros, todos admiten este patrón.

---

### 🔑 Resumen
- **Código en Claude**: No ejecuta código internamente; genera código → un sandbox lo ejecuta → se devuelven los resultados → razonamiento iterativo.
- **Verificación de esquemas JSON**: Utiliza decodificación restringida / validación de esquemas para garantizar una salida estructurada válida.
- **Enrutamiento de uso de herramientas**: El LLM selecciona llamadas a herramientas en JSON, el motor de orquestación las valida y ejecuta, y alimenta los resultados de vuelta en un bucle.

---

👉 ¿Te gustaría que **dibuje un diagrama** que muestre el flujo (LLM ↔ enrutador de herramientas ↔ validador de esquemas ↔ motor de ejecución) para que sea más claro visualmente?