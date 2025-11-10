---
audio: false
generated: true
image: false
lang: es
layout: post
title: Modos Híbridos de DeepSeek V3.1 Explicados
translated: true
type: note
---

Así es como la **API de DeepSeek V3.1** maneja su nueva arquitectura de inferencia híbrida (modos "Think" vs "Non‑Think"):

---

### Resumen de los Cambios en la API

#### 1. **Dos Endpoints Distintos (Modos)**

* **`deepseek-chat`** corresponde al **modo Sin Pensar**—optimizado para respuestas rápidas.
* **`deepseek-reasoner`** corresponde al **modo Pensar**—diseñado para tareas de razonamiento más deliberadas y de múltiples pasos.
  Ambos endpoints ahora operan en el mismo modelo V3.1 con una ventana de contexto de 128K tokens. ([DeepSeek API Docs][1], [Data Science Dojo][2])

#### 2. **Soporte de Contexto Expandido**

* Ambos modos soportan el contexto extendido de 128K tokens, lo que es una mejora importante que permite manejar entradas muy largas. ([DeepSeek API Docs][1], [Hugging Face][3])

#### 3. **Formato y Capacidades Mejoradas**

* Ahora se admite la **compatibilidad con la API de Anthropic**, lo que facilita la integración de DeepSeek con bibliotecas cliente de estilo Anthropic. ([DeepSeek API Docs][1])
* Se admite **Strict Function Calling** (en beta), permitiendo una invocación de herramientas más robusta y validada a través de la API. ([DeepSeek API Docs][1])

#### 4. **Interruptor en la UI vs Invocación por API**

* En su web UI (botón "DeepThink"), los usuarios pueden cambiar entre modos de forma interactiva.
* En la **API**, debes elegir explícitamente el modo estableciendo el parámetro `model` como `"deepseek-chat"` (para no pensar) o `"deepseek-reasoner"` (para pensar). ([DeepSeek API Docs][1])

#### 5. **Otras Mejoras**

* Se han introducido **más recursos para la API** y una experiencia general más fluida para el desarrollador. ([DeepSeek API Docs][1])
* El tokenizador subyacente y las plantillas de chat se han actualizado para soportar el comportamiento basado en modos (por ejemplo, insertando tokens `` apropiadamente). ([Hugging Face][3])

---

### Resumen: Qué ha Cambiado — Sin una Tabla

* **Nueva nomenclatura**:

  * `deepseek-chat` → Modo Sin Pensar
  * `deepseek-reasoner` → Modo Pensar

* **Arquitectura compartida**: Ambos están construidos sobre el mismo modelo de 671B parámetros con una larga ventana de contexto de 128K tokens.

* **Opciones de integración mejoradas**:

  * Soporta APIs de estilo Anthropic.
  * Ofrece Strict Function Calling (beta), permitiendo interacciones con herramientas más seguras y basadas en esquemas.

* **Actualizaciones de plantillas**: La API ahora usa tokens especiales (``) en los prompts para diferenciar modos, y ha renovado la lógica de las plantillas de chat.

* **Experiencia del desarrollador**: La plataforma incluye más recursos, documentación actualizada y un proceso de integración más fluido en general.

---

### Ejemplo de Uso (Python/HTTP)

**Sin Pensar (respuestas rápidas):**

```python
import openai  # o un SDK compatible con DeepSeek
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"Cuéntame un chiste."}],
)
```

**Pensar (razonamiento profundo):**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"Explica por qué el cielo es azul."}],
)
```

**Function Calling (modo estricto, beta):**
Puedes definir funciones (herramientas) con esquemas JSON y permitir que el modelo las invoque, recibiendo llamadas estructuradas que puedes ejecutar y reintroducir—ideal para construir agentes autónomos. ([DeepSeek API Docs][1], [Reddit][4], [apidog][5])

---

¡Avísame si necesitas ayuda para crear prompts para el uso de herramientas, optimizar costes o velocidad, o explorar la interfaz compatible con Anthropic con más detalle!

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"