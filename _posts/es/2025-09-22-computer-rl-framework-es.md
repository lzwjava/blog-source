---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Marco ComputerRL para Agentes de Automatización de Escritorio
translated: true
type: note
---

El artículo “ComputerRL” es un trabajo de investigación reciente titulado *“ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents”*. ([arXiv][1])

Aquí están las ideas clave y contribuciones en resumen:

---

### ¿Qué es ComputerRL?

* Es un framework destinado a permitir que los agentes autónomos interactúen con entornos de escritorio (aplicaciones, GUI, API) como lo haría un humano —haciendo clic, escribiendo, usando menús, etc.— pero también a través de API cuando sea posible. ([arXiv][1])
* La idea es combinar tanto las **interacciones basadas en GUI** (para cuando la API no está disponible o es más natural para un humano) como las **llamadas programáticas a la API** (más precisas, robustas y eficientes) en lo que ellos denominan el **paradigma API-GUI**. ([arXiv][1])

---

### Por qué es diferente / qué problemas resuelve

* Uno de los grandes desafíos en entrenar agentes de RL para tareas de escritorio / GUI es la ineficiencia e inestabilidad al iniciar muchas máquinas virtuales / simular entornos durante largos períodos. ComputerRL aborda la escalabilidad ejecutando muchos entornos de escritorio en paralelo. ([arXiv][1])
* Además, las ejecuciones largas de RL tienden a sufrir **colapso de entropía** (donde la política se estanca volviéndose demasiado determinista demasiado pronto, reduciendo la exploración). Proponen una estrategia de entrenamiento llamada **Entropulse**, que alterna entre fases de aprendizaje por refuerzo y ajuste fino supervisado para mantener viva la exploración de la política. ([arXiv][1])

---

### Experimentos y Resultados

* Lo aplicaron a modelos abiertos como **GLM-4-9B-0414** y **Qwen2.5-14B**. ([arXiv][1])
* El benchmark de evaluación es **OSWorld**, que prueba a los agentes en entornos similares al escritorio de Ubuntu. ([arXiv][1])
* Su agente “AutoGLM-OS-9B” (basado en GLM-4-9B-0414) logra una nueva precisión state-of-the-art (\~48.1%) en esas tareas de automatización de escritorio. ([arXiv][1])

---

Si quieres, puedo enviarte un resumen de cómo esto podría compararse con, por ejemplo, AgentBench o los agentes de Anthropic (en términos de estabilidad, TPS, etc.), si tienes curiosidad.

[1]: https://arxiv.org/abs/2508.14040?utm_source=chatgpt.com "ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents"