---
audio: false
generated: true
image: false
lang: es
layout: post
title: Capas de Validación de API de LLM Segura
translated: true
type: note
---

Al construir o utilizar una **API de LLM**, generalmente querrás salvaguardas para garantizar que las respuestas sean seguras, válidas y útiles. Estas son las principales formas de agregar verificaciones:

---

### 1. **Validación de Entrada**

* **Comprobaciones de esquema**: Asegúrate de que el JSON de la solicitud siga el esquema esperado antes de enviarlo al LLM.
* **Saneamiento del prompt**: Elimina o escapa caracteres no deseados, instrucciones maliciosas o intentos de inyección.
* **Comprobaciones de longitud**: Aplica límites máximos de tokens/caracteres para las entradas para evitar costos innecesarios o truncamiento.

---

### 2. **Validación de Salida**

* **Validación de esquema JSON**: Si se supone que el LLM devuelve JSON, pásalo por `json.loads()` y valídalo contra un esquema (por ejemplo, con `pydantic`, `jsonschema`).
* **Comprobaciones de Regex/formato**: Para correos electrónicos, URLs o números, aplica patrones.
* **Comprobación de tipos**: Verifica que los campos sean del tipo correcto (string, integer, list, etc.).
* **Comprobaciones de rango**: Asegúrate de que los valores numéricos o de fecha estén dentro de los límites esperados.

---

### 3. **Comprobaciones de Seguridad y Contenido**

* **Filtros de toxicidad o blasfemias**: Pasa la salida por un clasificador (por ejemplo, Perspective API, OpenAI moderation API).
* **Filtros de políticas**: Define reglas para bloquear respuestas que contengan ciertas palabras clave o categorías.
* **Detección de alucinaciones**: Añade pasos de verificación de hechos (mediante comprobaciones aumentadas por recuperación, validación cruzada con múltiples modelos o comprobaciones de coherencia basadas en reglas).

---

### 4. **Restricciones de Lógica de Negocio**

* **Reglas de consistencia**: Si la respuesta debe coincidir con datos del sistema (por ejemplo, saldo de cuenta disponible, valores de configuración), verifica cruzadamente antes de devolverla al usuario.
* **Barreras de protección**: Usa bibliotecas como **Guardrails AI**, **LMQL** o **Instructor** para aplicar salidas estructuradas y restricciones de forma declarativa.
* **Hooks de post-procesamiento**: Envuelve las respuestas del LLM con lógica personalizada (normalizar mayúsculas y minúsculas, aplicar valores predeterminados, rechazar respuestas inesperadas).

---

### 5. **Redundancia y Verificación Cruzada**

* **Prompts de auto-comprobación**: Pide al LLM que vuelva a validar o explique su propia respuesta.
* **Comprobación con doble modelo**: Usa un LLM más pequeño/rápido para verificar la salida del modelo principal (por ejemplo, "¿esta respuesta se ajusta al esquema X?").
* **Votación/consenso**: Ejecuta múltiples llamadas y compara las respuestas para verificar estabilidad.

---

### 6. **Salvaguardas Operativas**

* **Límites de tasa**: Previene el abuso de la API.
* **Tiempos de espera**: Aborta las solicitudes que se cuelgan.
* **Registro y auditoría de trazas**: Mantén un registro de las solicitudes y respuestas filtradas.
* **Alternativas de respaldo**: Si la validación falla, reintenta con un prompt ajustado o devuelve un valor predeterminado/error seguro.

---

👉 En la práctica, una buena pila de API de LLM aplica estos en capas:

1. Valida la entrada.
2. Llama al LLM.
3. Valida la salida contra el esquema + reglas de negocio.
4. Ejecuta filtros de seguridad/contenido.
5. Devuelve la respuesta solo si las comprobaciones son exitosas (de lo contrario, reintenta/usar alternativa).

---

¿Te gustaría que te muestre un **ejemplo en Python** donde envolvemos una llamada a la API de un LLM con validación de esquema JSON y comprobaciones de moderación?