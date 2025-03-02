---
audio: false
generated: false
lang: es
layout: post
title: El flujo de trabajo es BFS, el agente es DFS
translated: true
---

Según Anthropic [^1]:

- **Workflows** son sistemas en los que los LLM (Modelos de Lenguaje de Gran Escala) y las herramientas se orquestan a través de rutas de código predefinidas.
- **Agents**, por otro lado, son sistemas en los que los LLM controlan dinámicamente sus propios procesos y el uso de herramientas, manteniendo la flexibilidad en cómo se realizan las tareas.

Lo que entiendo de esto es:

- Usar **workflows** para mejorar una aplicación o plataforma es similar a **BFS (Búsqueda en Anchura)**, donde las tareas se completan de manera sistemática, nivel por nivel.
- Usar **agentes** es más parecido a **DFS (Búsqueda en Profundidad)**, donde las tareas se abordan de manera más exploratoria, paso a paso.

A veces, **BFS** y **DFS** pueden combinarse. DFS puede anidarse dentro de otro DFS, y lo mismo ocurre con BFS.

Por ejemplo, **o1 (cadena de pensamiento)** es como BFS (búsqueda en amplitud). Inicialmente, las tareas principales se dividen en pasos separados, y cada paso se expande en explicaciones más detalladas. Luego, basándose en todo el razonamiento, se proporciona el resultado final.

Para tareas muy complejas, como pedirle a una IA que construya una aplicación de YouTube o cree un sistema operativo, podría utilizar BFS (Búsqueda en Anchura), DFS (Búsqueda en Profundidad) o una combinación de ambos. Realmente depende de cómo utilicemos BFS y DFS: a veces la IA necesita profundizar (DFS), y otras veces necesita expandir su enfoque (BFS).

Otra consideración es que, en cada paso, la IA debe evaluar qué hacer a continuación para alcanzar sus objetivos.

**Objetivos** son un aspecto interesante. Puede haber muchos objetivos, como crear una aplicación de YouTube, donde la IA necesita asegurarse de que todo el código funcione correctamente, todas las características estén implementadas y todas las pruebas se aprueben. La forma de alcanzar estos objetivos es fascinante. ¿Debería la IA abordar un objetivo a la vez, o debería avanzar en todos los objetivos simultáneamente y luego iterar en cada uno?

---

[^1]: Construyendo agentes efectivos, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

