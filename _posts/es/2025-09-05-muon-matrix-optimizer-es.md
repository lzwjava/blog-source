---
audio: false
generated: true
image: false
lang: es
layout: post
title: 'Muon: Optimizador de Matrices Consciente de la Estructura'
translated: true
type: note
---

“Muon” en Kimi se refiere a un optimizador avanzado—específicamente un **optimizador consciente de la estructura y ortogonalizador de matrices** utilizado en el entrenamiento del modelo de lenguaje Kimi K2.

---

### ¿Qué es el Optimizador Muon?

1. **Optimización Consciente de la Matriz**
   A diferencia de AdamW o SGD, Muon trata las matrices de pesos como entidades geométricas en lugar de parámetros escalares independientes. Aplica **iteraciones de Newton–Schulz** para ortogonalizar el gradiente promediado por momento, produciendo actualizaciones bien condicionadas y equilibradas que respetan tanto la estructura de filas como de columnas de la matriz ([Medium][1], [kellerjordan.github.io][2]).

2. **Ortogonalización vía Newton–Schulz**
   En lugar de realizar una costosa Descomposición en Valores Singulares (SVD), Muon utiliza un método iterativo rápido (Newton–Schulz) para aproximar la matriz ortogonal más cercana al gradiente. Esto mantiene la actualización bajo **restricciones de norma espectral**, preservando la energía y distribuyendo el aprendizaje por todas las direcciones por igual ([Medium][1], [kellerjordan.github.io][2]).

3. **Ajuste del Pipeline**
   El flujo de actualización estándar—**Gradiente → Momento → Actualización de Parámetros**—se reemplaza por:
   **Gradiente → Momento → Ortogonalización de Newton–Schulz → Actualización de Parámetros**.
   Esta modificación mejora la eficiencia y estabilidad del entrenamiento para matrices de parámetros 2D ([Medium][3], [kellerjordan.github.io][2]).

4. **Eficiente en la Práctica**
   A pesar de añadir una pequeña sobrecarga computacional, Muon ofrece aceleraciones significativas:

   * Récords en NanoGPT speedrunning, mejorando el tiempo de entrenamiento en ~35% ([kellerjordan.github.io][2]).
   * Escala bien en el entrenamiento de modelos de lenguaje grandes cuando se combina con weight decay y ajustes RMS por parámetro ([arXiv][4]).

5. **Bases Teóricas Sólidas**
   Investigaciones recientes respaldan las propiedades de convergencia de Muon, los beneficios del weight decay y el tamaño de lote óptimo. Los estudios confinan límites teóricos más estrictos y eficiencia en diversos escenarios prácticos ([arXiv][5]).

---

### Rol de Muon en **Kimi K2**

Kimi K2 es el **modelo Mixture-of-Experts (MoE)** de Moonshot AI, con **1 billón de parámetros totales** (32B activados) optimizado para capacidades agenticas. Logró un rendimiento excepcional en benchmarks de conocimiento, razonamiento y codificación, gracias en parte al entrenamiento con Muon (y una variante denominada **MuonClip**) ([Hugging Face][6], [Poe][7]).

* El **optimizador MuonClip** se refiere a la aplicación de Muon a gran escala masiva mientras se abordan los desafíos de estabilidad intrínsecos a modelos tan grandes ([Hugging Face][6], [Poe][7]).
* El optimizador fue clave para permitir **cero inestabilidad en el entrenamiento** sobre un gran conjunto de datos de tokens (~15.5 billones de tokens) y ofrecer resultados de vanguardia ([Hugging Face][6]).

---

### En Resumen (Sin Tabla, como se Solicitó)

* **Muon** = “MomentUm Orthogonalized by Newton–Schulz” (Momento Ortogonalizado por Newton–Schulz)—un optimizador que reemplaza las actualizaciones de gradiente crudo con actualizaciones ortogonalizadas, mejorando la dinámica de aprendizaje para parámetros matriciales.
* Preserva la estructura, asegura actualizaciones equilibradas y se mantiene eficiente mediante la ortogonalización iterativa en lugar de descomposiciones costosas.
* **Kimi K2** aprovecha Muon (y MuonClip) para llevar al límite el entrenamiento de MoE a gran escala, logrando un rendimiento superior con estabilidad y eficiencia computacional.

---

¡Házme saber si te gustaría una inmersión más profunda—quizás cómo se compara Muon con AdamW en las trayectorias de entrenamiento, cómo MuonClip ajusta el algoritmo para MoEs, o cómo funciona el método Newton–Schulz en código!

[1]: https://medium.com/%40gauritr01/the-truth-about-kimi-k2-pretraining-muon-optimizer-moe-unpacked-43554527d94a?utm_source=chatgpt.com "The Truth About KIMI K2 Pretraining: Muon Optimizer ..."
[2]: https://kellerjordan.github.io/posts/muon/?utm_source=chatgpt.com "Muon: An optimizer for hidden layers in neural networks"
[3]: https://medium.com/%40jenwei0312/going-beyond-adamw-a-practical-guide-to-the-muon-optimizer-93d90e91dbd3?utm_source=chatgpt.com "Going Beyond AdamW: A Practical Guide to the Muon ..."
[4]: https://arxiv.org/html/2502.16982v1?utm_source=chatgpt.com "Muon is Scalable for LLM Training"
[5]: https://arxiv.org/abs/2507.01598?utm_source=chatgpt.com "Convergence Bound and Critical Batch Size of Muon Optimizer"
[6]: https://huggingface.co/moonshotai/Kimi-K2-Base?utm_source=chatgpt.com "moonshotai/Kimi-K2-Base"
[7]: https://poe.com/Kimi-K2?utm_source=chatgpt.com "Kimi-K2"