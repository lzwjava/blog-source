---
audio: false
generated: true
lang: es
layout: post
title: Los Modelos de 128.000 Tokens de DeepSeek en 2025
translated: true
type: note
---

A junio de 2025, DeepSeek cuenta con una gama de modelos con longitudes de contexto impresionantes, que a menudo aprovechan su arquitectura Mixture-of-Experts (MoE) para lograr eficiencia. Aquí hay un desglose:

*   **DeepSeek-R1:** Este modelo, lanzado en enero de 2025, destaca por admitir una longitud de contexto de **128,000 tokens** (o 131,072 tokens en algunos benchmarks). Es particularmente fuerte en matemáticas, codificación y pensamiento estructurado debido a su post-entrenamiento con Reinforcement Learning (RL).
*   **DeepSeek-V3:** Lanzado en diciembre de 2024, DeepSeek-V3, incluido su modelo base, también admite una longitud de contexto de **128,000 tokens**. Es un potente modelo MoE con 671 mil millones de parámetros totales (37 mil millones activos por consulta).
*   **DeepSeek-Coder-V2:** Este modelo MoE centrado en código, lanzado en julio de 2024, tiene una ventana de contexto significativa de **128,000 tokens**. Admite una amplia gama de lenguajes de programación (338).
*   **DeepSeek-V2:** Lanzado en mayo de 2024, DeepSeek-V2 cuenta con una longitud de contexto de **128,000 tokens**. Este modelo MoE apunta a un entrenamiento económico y una inferencia eficiente.
*   **DeepSeek-V2.5:** Lanzado en septiembre de 2024, este modelo combina capacidades generales y de codificación y también admite una ventana de contexto de **128,000 tokens**.

**Consideraciones importantes:**

*   **Longitud de Contexto Nativa vs. Límites de la API:** Si bien algunos modelos de DeepSeek tienen una longitud de contexto nativa de hasta 163,840 tokens, la API de DeepSeek puede limitar la ventana de contexto disponible para modelos específicos (por ejemplo, "deepseek-chat" y "deepseek-reasoner" actualmente tienen un límite de contexto de 64K a través de su API). Si necesita el contexto completo, podría ser necesario ejecutar los modelos localmente o utilizar proveedores de API que permitan contextos más largos.
*   **Degradación del Rendimiento:** Al igual que otros modelos de lenguaje grandes, aunque los modelos pueden anunciar ventanas de contexto muy largas, el rendimiento (precisión, razonamiento) a veces puede degradarse cuando se lleva al límite máximo absoluto. Se espera que DeepSeek R2, por ejemplo, aborde la caída del 15% en el rendimiento observada en R1 en su ventana de contexto máxima de 128,000 tokens.

En resumen, DeepSeek es un actor fuerte en el espacio de los LLM de contexto largo, con varios modelos en junio de 2025 que ofrecen una ventana de contexto de 128K tokens, lo que los hace adecuados para manejar entradas extensas y tareas complejas.