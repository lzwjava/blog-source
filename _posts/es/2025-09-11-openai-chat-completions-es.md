---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Trabajando con los Modelos de Chat Completions de OpenAI
translated: true
type: note
---

Has enlazado el artículo de Microsoft Learn **“Trabajar con modelos de finalización de chat”** (publicado el **1 de septiembre de 2025**). Aquí tienes un resumen claro y conciso de sus puntos principales:

---

### Aspectos Destacados Clave

* **Modelos orientados al chat**
  Los nuevos modelos de chat difieren de los modelos GPT-3 anteriores. En lugar de ser "texto-entrada, texto-salida", utilizan un formato **conversación-entrada, mensaje-salida**. Esencialmente, la entrada se estructura como una transcripción (con roles como *sistema*, *usuario*, *asistente*), y el modelo devuelve un mensaje para continuar la conversación ([Microsoft Learn][1]).

* **Diseñados para el diálogo**
  Esta estructura está optimizada para conversaciones de varios turnos. También funciona bien para escenarios de un solo mensaje, pero el formato conversacional permite interacciones más fluidas ([Microsoft Learn][1]).

* **No los trates como a los modelos antiguos**
  Estos modelos de chat son más verbosos y a menudo producen respuestas menos útiles si los abordas como si fueran GPT-3. Se recomienda utilizar la nueva interfaz de estilo chat para obtener los mejores resultados ([Microsoft Learn][1]).

* **Fragmento de código de ejemplo**
  El artículo incluye un ejemplo de código básico que utiliza una sintaxis estilo Python para llamar a la API de finalizaciones de chat de Azure:

  ```python
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.getenv("AZURE_OPENAI_API_KEY"),
      base_url="https://YOUR-RESOURCE-NAME.openai.azure.com/openai/v1/"
  )

  response = client.chat.completions.create(
      model="gpt-4o",  # o deployment_name
      messages=[
          {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
          {"role": "user", "content": "Who were the founders of Microsoft?"}
      ]
  )

  print(response.model_dump_json(indent=2))
  print(response.choices[0].message.content)
  ```

  Esto muestra cómo enviar correctamente los mensajes (con separación de roles) y recuperar la respuesta del modelo ([Microsoft Learn][1]).

---

### Por Qué Es Importante

1.  **Contexto conversacional mejorado** — Los modelos de chat mantienen mejor el flujo y el contexto a lo largo de interacciones de varios turnos.
2.  **Usabilidad mejorada** — El uso de roles (sistema, usuario, asistente) permite instrucciones más claras, establecer personalidad o aplicar restricciones.
3.  **Evita inconvenientes** — Tratar a los modelos de chat como a los de generaciones anteriores puede resultar en una baja calidad de respuesta; utiliza la interfaz de API de chat según lo previsto.

---

Avísame si necesitas ayuda para revisar el ejemplo de código, adaptarlo a tu configuración o explorar guías relacionadas—¡estaré encantado de ayudarte!

Y como prefieres, he mantenido esto en un formato simple y legible, sin tablas.

[1]: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt?utm_source=chatgpt.com "Work with chat completion models - Azure OpenAI in ..."