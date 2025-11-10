---
audio: false
generated: true
image: false
lang: es
layout: post
title: Uso de Herramientas frente a Llamadas a Funciones Explicado
translated: true
type: note
---

Desglosemos la diferencia entre **tool use** (uso de herramientas) y **function calling** (llamada a funciones) en el contexto de las APIs de LLM:

---

## 1. Tool Use (Uso de Herramientas)

* **Concepto**: El uso de herramientas es una idea amplia donde el LLM se potencia con capacidades externas. En lugar de solo generar texto, puede "usar una herramienta" para obtener información, ejecutar código, consultar una base de datos o generar una imagen.
* **Implementación**: En la práctica, las "herramientas" son APIs o sistemas externos registrados en el runtime del LLM (por ejemplo, una API de búsqueda, un entorno de ejecución de Python o una API de calendario).
* **Rol del LLM**: El modelo decide cuándo llamar a la herramienta, con qué argumentos e integra los resultados nuevamente en la conversación.
* **Ejemplo**:

  * Usuario: "¿Qué tiempo hace en Guangzhou?"
  * LLM: Llama a la herramienta `weather` con `{city: "Guangzhou"}` → obtiene `28°C, soleado`.
  * LLM: Responde: "Hace 28°C y está soleado."

Piensa en el **tool use** como un marco de orquestación general donde el LLM no solo responde con palabras, sino que coordina acciones con sistemas externos.

---

## 2. Function Calling (Llamada a Funciones)

* **Concepto**: La llamada a funciones es un mecanismo *estructurado* proporcionado por algunas APIs de LLM (como OpenAI, Anthropic, etc.), donde defines funciones (con nombres, parámetros, esquemas) y el LLM puede devolver argumentos JSON para llamarlas.
* **Implementación**: Proporcionas al modelo esquemas JSON que describen las funciones. La salida del modelo es entonces texto o un objeto estructurado de llamada a función.
* **Rol del LLM**: En lugar de "alucinar" el uso de la API, el modelo genera argumentos estructurados válidos para funciones predefinidas.
* **Ejemplo**:

  * Defines una función:

    ```json
    {
      "name": "getWeather",
      "description": "Obtener el clima actual",
      "parameters": {
        "type": "object",
        "properties": {
          "city": {"type": "string"}
        },
        "required": ["city"]
      }
    }
    ```
  * Usuario: "¿Qué tiempo hace en Guangzhou?"
  * LLM: Devuelve → `{ "name": "getWeather", "arguments": {"city": "Guangzhou"} }`
  * Tu sistema ejecuta la función y pasa los resultados de vuelta.

Esto hace que **function calling** sea una forma específica, segura y basada en esquemas de realizar **tool use**.

---

## 3. Diferencias Clave

* **Alcance**:

  * Tool use = concepto general (LLM potenciado con sistemas externos).
  * Function calling = un diseño de API estandarizado para llamadas estructuradas.
* **Control**:

  * El tool use puede ser más libre (el LLM decide y formatea).
  * La function calling impone esquemas estrictos, reduciendo la ambigüedad y las alucinaciones.
* **Interoperabilidad**:

  * El tool use puede involucrar muchos sistemas externos (búsqueda, ejecución de código, generación de imágenes).
  * La function calling es mejor cuando quieres argumentos precisos y estructurados (como en APIs o consultas a bases de datos).

---

## 4. Modelo Mental

* La function calling es un **subconjunto** del tool use.
* Si el tool use es la *estrategia general*, la function calling es el *método seguro y estructurado* que la mayoría de las APIs exponen.

---

¿Te gustaría que también muestre un **ejemplo de flujo de trabajo comparativo** (como prompt del usuario → salida del LLM → ejecución) para ilustrar la diferencia de manera más concreta?