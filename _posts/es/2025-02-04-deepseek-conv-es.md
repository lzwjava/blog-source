---
audio: false
generated: false
lang: es
layout: post
title: Deepseek - Conversación
translated: true
type: note
---

A: He estado revisando el informe técnico de DeepSeek-V3 y estoy realmente impresionado por la escala de este modelo. ¿671 mil millones de parámetros, pero solo 37 mil millones activados por token? Esa es una arquitectura MoE masiva. ¿Cómo funciona siquiera?

B: ¡Sí, es toda una hazaña! DeepSeek-V3 está construido sobre el framework Mixture-of-Experts (MoE), que le permite activar solo un subconjunto de parámetros para cada token. Específicamente, utiliza 256 expertos enrutados, pero solo 8 se activan por token. Esto lo hace increíblemente eficiente en comparación con los modelos densos, donde todos los parámetros están activos para cada token.

A: Eso tiene sentido. Pero, ¿cómo decide qué expertos activar? ¿Es simplemente aleatorio o hay algún tipo de mecanismo de enrutamiento?

B: ¡Buena pregunta! El enrutamiento se basa en puntuaciones de afinidad token-a-experto. A cada token se le asigna una puntuación para cada experto, y los K expertos principales con las puntuaciones más altas se activan. DeepSeek-V3 utiliza una función sigmoide para calcular estas puntuaciones, lo que ayuda a equilibrar la carga entre los expertos.

A: Ah, entonces no es aleatorio, se aprende durante el entrenamiento. Pero, ¿eso no lleva a un uso desequilibrado de los expertos? He oído que ese es un problema común con los modelos MoE.

B: ¡Exactamente! El uso desequilibrado de expertos puede ser un problema, pero DeepSeek-V3 introduce una estrategia libre de pérdidas auxiliares para manejar esto. En lugar de agregar un término de pérdida separado para fomentar el equilibrio de carga, ajusta dinámicamente un término de sesgo para cada experto. Si un experto está sobrecargado, su sesgo disminuye, y si está infrautilizado, el sesgo aumenta. Esto mantiene la carga equilibrada sin degradar el rendimiento del modelo.

A: Eso es inteligente. Entonces, sin pérdidas auxiliares significa menos interferencia con el objetivo principal de entrenamiento. Pero, ¿cómo se compara esto con los modelos MoE tradicionales que utilizan pérdidas auxiliares?

B: Correcto. Los modelos MoE tradicionales a menudo usan pérdidas auxiliares para fomentar el equilibrio de carga, pero estas pérdidas a veces pueden perjudicar el rendimiento. El enfoque libre de pérdidas auxiliares de DeepSeek-V3 evita esta compensación. De hecho, los estudios de ablación muestran que supera consistentemente a los modelos que dependen de pérdidas auxiliares, especialmente en tareas como programación y matemáticas.

A: Interesante. Hablando de programación y matemáticas, noté que DeepSeek-V3 tiene un rendimiento excepcional en benchmarks como HumanEval y MATH. ¿Cuál es el ingrediente secreto allí?

B: Una gran parte es el objetivo de predicción multi-token (MTP). En lugar de solo predecir el siguiente token, DeepSeek-V3 predice múltiples tokens futuros en cada posición. Esto densifica la señal de entrenamiento y ayuda al modelo a planificar con anticipación, lo que es especialmente útil para tareas que requieren razonamiento secuencial, como programación y matemáticas.

A: Espera, ¿entonces está prediciendo múltiples tokens a la vez? ¿Cómo funciona eso durante la inferencia? ¿Todavía usa MTP o es solo para entrenamiento?

B: Durante la inferencia, los módulos MTP pueden descartarse y el modelo se comporta como un modelo autorregresivo estándar. Pero aquí está la parte genial: los módulos MTP también pueden reutilizarse para decodificación especulativa, lo que acelera la generación prediciendo múltiples tokens en paralelo y luego verificándolos.

A: Ese es un truco ingenioso. Entonces, es como obtener los beneficios de MTP durante el entrenamiento y luego usarlo para acelerar la inferencia. Pero, ¿qué pasa con el mecanismo de atención? Vi algo sobre Multi-head Latent Attention (MLA). ¿Cómo encaja eso?

B: MLA es otra innovación clave. Reduce la huella de memoria comprimiendo la caché Key-Value (KV). En lugar de almacenar claves y valores de atención completos, utiliza compresión conjunta de bajo rango para representarlos. Esto reduce significativamente el tamaño de la caché KV durante la inferencia mientras mantiene un rendimiento comparable a la Multi-Head Attention estándar.

A: Esa es una gran ventaja para la eficiencia. Pero, ¿la compresión no introduce cierta pérdida de información? ¿Cómo mantiene el rendimiento?

B: Buen punto. La compresión está diseñada para preservar la información más importante al centrarse en los vectores latentes que capturan las características esenciales de las claves y valores. El modelo también utiliza Rotary Positional Embedding (RoPE) para mantener la información posicional, lo que ayuda a mitigar cualquier pérdida por compresión.

A: Entendido. Entonces, MLA trata sobre eficiencia sin sacrificar demasiado rendimiento. Pero, ¿qué pasa con el entrenamiento? Entrenar un modelo de este tamaño debe ser increíblemente costoso. ¿Cómo logra DeepSeek-V3 mantener los costos bajos?

B: La eficiencia del entrenamiento es un enfoque principal. DeepSeek-V3 utiliza un framework de precisión mixta FP8, que reduce el uso de memoria y acelera la computación. También emplea un algoritmo DualPipe para el paralelismo de pipeline, que minimiza las burbujas de pipeline y superpone la computación con la comunicación. Estas optimizaciones permiten que el modelo sea entrenado en 14.8 billones de tokens con solo 2.788 millones de horas de GPU H800.

A: Eso es impresionante. Pero el entrenamiento FP8 puede ser complicado, ¿cómo manejan los problemas de precisión? He oído que el entrenamiento de baja precisión puede llevar a inestabilidad.

B: Tienes razón. El entrenamiento FP8 es desafiante debido al rango dinámico limitado. DeepSeek-V3 aborda esto con cuantización de grano fino, donde las activaciones y los pesos se agrupan en mosaicos o bloques más pequeños y se escalan de forma independiente. Esto reduce el impacto de los valores atípicos y mantiene estable el entrenamiento. También utilizan acumulación de alta precisión para operaciones críticas para mantener la precisión.

A: Eso tiene sentido. Entonces, es un equilibrio entre eficiencia y precisión. Pero, ¿qué pasa con los datos? 14.8 billones de tokens es un conjunto de datos masivo. ¿En qué tipo de datos está entrenado?

B: El conjunto de datos es diverso y de alta calidad, con un enfoque en texto en inglés y chino. También incluye una cantidad significativa de datos matemáticos y de programación, lo que ayuda al modelo a sobresalir en esos dominios. La pipeline de datos está optimizada para minimizar la redundancia mientras mantiene la diversidad, y utilizan técnicas como el empaquetado de documentos para garantizar la integridad de los datos.

A: Eso explica el fuerte rendimiento en tareas de programación y matemáticas. Pero, ¿qué pasa con el rendimiento multilingüe? ¿Maneja bien otros idiomas?

B: Sí, DeepSeek-V3 está entrenado en un corpus multilingüe y tiene un buen rendimiento en benchmarks como MMMLU, que incluye tareas en idiomas no ingleses. Es particularmente fuerte en chino, superando a modelos como Qwen2.5 en benchmarks chinos como C-Eval y CMMLU.

A: Eso es impresionante. Pero, ¿qué pasa con las tareas de contexto largo? Vi que admite hasta 128K tokens. ¿Cómo maneja entradas tan largas?

B: DeepSeek-V3 extiende su longitud de contexto en dos etapas: primero a 32K tokens y luego a 128K tokens utilizando la técnica YaRN. Esto le permite manejar tareas de contexto largo como resumen de documentos y recuperación de manera efectiva. También tiene un buen rendimiento en la prueba 'Needle In A Haystack', que evalúa la comprensión de contexto largo.

A: Esa es una gran mejora sobre los modelos anteriores. Pero, ¿qué pasa con la implementación? ¿Cómo manejan la inferencia para un modelo tan grande?

B: La inferencia se maneja en un clúster H800, con GPUs interconectadas usando NVLink e InfiniBand. La estrategia de implementación separa las etapas de prellenado y decodificación para garantizar tanto alto rendimiento como baja latencia. También utilizan expertos redundantes para equilibrar la carga durante la inferencia, lo que ayuda a mantener la eficiencia.

A: Esas son muchas optimizaciones. Pero, ¿cuáles son las limitaciones? Seguramente, un modelo de este tamaño tiene algunas compensaciones.

B: Una limitación es el tamaño de la unidad de implementación. DeepSeek-V3 requiere un clúster relativamente grande para una inferencia eficiente, lo que podría ser un desafío para equipos más pequeños. También hay margen de mejora en la velocidad de generación, aunque la decodificación especulativa con MTP ayuda.

A: Me parece justo. Pero en general, parece un gran paso adelante. ¿Qué sigue para DeepSeek-V3? ¿Hay alguna dirección futura que estén explorando?

B: Están considerando varias áreas, como refinar la arquitectura para admitir longitud de contexto infinita, explorar fuentes adicionales de señales de entrenamiento y mejorar las capacidades de razonamiento del modelo. También están trabajando en métodos de evaluación más completos para evaluar mejor el rendimiento del modelo.

A: Suena que no van a reducir la velocidad en ningún momento pronto. Gracias por guiarme a través de todo esto, DeepSeek-V3 es definitivamente un cambio de juego en el espacio de LLM de código abierto.

B: ¡Absolutamente! Es emocionante ver hasta dónde han llegado los modelos de código abierto. DeepSeek-V3 está empujando los límites, y no puedo esperar a ver qué harán después.

A: Mencionaste que DeepSeek-V3 usa entrenamiento de precisión mixta FP8. Tengo curiosidad, ¿cómo se compara eso con BF16 o FP16? ¿Es FP8 realmente lo suficientemente estable para entrenar un modelo tan grande?

B: Esa es una gran pregunta. FP8 es ciertamente más desafiante debido a su rango dinámico limitado, pero DeepSeek-V3 utiliza una estrategia de cuantización de grano fino para mitigar esto. Por ejemplo, las activaciones se agrupan en mosaicos de 1x128 y los pesos se agrupan en bloques de 128x128. Cada grupo se escala de forma independiente, lo que ayuda a manejar los valores atípicos y mantiene estable el entrenamiento.

A: Interesante. Entonces, no es solo una cuantización FP8 general, es más matizada. Pero, ¿eso no introduce sobrecarga adicional para gestionar todos estos grupos y factores de escala?

B: Lo hace, pero la sobrecarga es mínima en comparación con los beneficios. La clave es que FP8 reduce el uso de memoria y acelera la computación, lo que es crítico para entrenar un modelo tan grande. También utilizan acumulación de alta precisión para operaciones críticas, como multiplicaciones de matrices, para garantizar la estabilidad numérica.

A: Entendido. Entonces, es una compensación entre precisión y eficiencia, pero han logrado un buen equilibrio. ¿Qué pasa con el algoritmo DualPipe? ¿Cómo funciona?

B: DualPipe está diseñado para minimizar las burbujas de pipeline en el paralelismo de pipeline. Superpone la computación y la comunicación dividiendo cada fragmento de trabajo en cuatro componentes: atención, despacho all-to-all, MLP y combinación all-to-all. Durante las pasadas hacia atrás, divide aún más la computación en 'backward for input' y 'backward for weights', lo que permite una superposición más eficiente.

A: Eso suena complejo, pero tiene sentido. Entonces, esencialmente está ocultando la sobrecarga de comunicación superponiéndola con la computación. ¿Cómo se compara esto con otros métodos de paralelismo de pipeline como 1F1B o Zero Bubble?

B: DualPipe tiene menos burbujas de pipeline en comparación con 1F1B y Zero Bubble. También permite programación bidireccional, donde los micro-lotes se alimentan desde ambos extremos del pipeline. Esto reduce aún más el tiempo de inactividad y mejora la eficiencia general. De hecho, DualPipe logra una sobrecarga de comunicación all-to-all casi nula, lo que es crucial para escalar modelos MoE.

A: Eso es impresionante. Pero, ¿qué pasa con el uso de memoria? ¿Requiere DualPipe más memoria que otros métodos?

B: Requiere un poco más de memoria porque mantiene dos copias de los parámetros del modelo, pero el aumento es manejable. La huella de memoria se optimiza mediante técnicas como el recomputación de RMSNorm y las proyecciones ascendentes de MLA, lo que elimina la necesidad de almacenar activaciones intermedias.

A: Ah, entonces están intercambiando un poco de memoria por mejor eficiencia. Eso parece una compensación justa. Hablando de memoria, ¿cómo manejan la caché KV para una longitud de contexto tan grande? 128K tokens deben requerir una caché enorme.

B: Ahí es donde MLA realmente brilla. Al comprimir la caché KV, reducen significativamente su tamaño. En lugar de almacenar claves y valores de atención completos, almacenan vectores latentes comprimidos, que son mucho más pequeños. Esto permite que DeepSeek-V3 maneje contextos largos sin encontrarse con cuellos de botella de memoria.

A: Esa es una solución inteligente. Pero, ¿qué pasa con la calidad de la atención? ¿La compresión afecta la capacidad del modelo para atender a los tokens correctos?

B: La compresión está diseñada para preservar la información más importante, por lo que el impacto en la calidad de la atención es mínimo. También utilizan RoPE (Rotary Positional Embedding) para mantener la información posicional, lo que ayuda al modelo a entender las posiciones relativas de los tokens incluso con claves y valores comprimidos.

A: Tiene sentido. Entonces, MLA es una situación en la que todos ganan: reduce el uso de memoria sin sacrificar demasiado rendimiento. Pero, ¿qué pasa con los datos de entrenamiento? Mencionaste que son 14.8 billones de tokens. ¿Cómo aseguran la calidad y diversidad de un conjunto de datos tan masivo?

B: El conjunto de datos está cuidadosamente curado para incluir tokens diversos y de alta calidad. Optimizan la pipeline de datos para minimizar la redundancia mientras mantienen la diversidad, y utilizan técnicas como el empaquetado de documentos para garantizar la integridad de los datos. El corpus incluye una mezcla de texto en inglés y chino, con énfasis en muestras matemáticas y de programación.

A: Eso explica el fuerte rendimiento en tareas de programación y matemáticas. Pero, ¿qué pasa con las tareas multilingües? ¿Maneja bien otros idiomas?

B: Sí, DeepSeek-V3 está entrenado en un corpus multilingüe y tiene un buen rendimiento en benchmarks como MMMLU, que incluye tareas en idiomas no ingleses. Es particularmente fuerte en chino, superando a modelos como Qwen2.5 en benchmarks chinos como C-Eval y CMMLU.

A: Eso es impresionante. Pero, ¿qué pasa con las tareas de contexto largo? Vi que admite hasta 128K tokens. ¿Cómo maneja entradas tan largas?

B: DeepSeek-V3 extiende su longitud de contexto en dos etapas: primero a 32K tokens y luego a 128K tokens utilizando la técnica YaRN. Esto le permite manejar tareas de contexto largo como resumen de documentos y recuperación de manera efectiva. También tiene un buen rendimiento en la prueba 'Needle In A Haystack', que evalúa la comprensión de contexto largo.

A: Esa es una gran mejora sobre los modelos anteriores. Pero, ¿qué pasa con la implementación? ¿Cómo manejan la inferencia para un modelo tan grande?

B: La inferencia se maneja en un clúster H800, con GPUs interconectadas usando NVLink e InfiniBand. La estrategia de implementación separa las etapas de prellenado y decodificación para garantizar tanto alto rendimiento como baja latencia. También utilizan expertos redundantes para equilibrar la carga durante la inferencia, lo que ayuda a mantener la eficiencia.

A: Esas son muchas optimizaciones. Pero, ¿cuáles son las limitaciones? Seguramente, un modelo de este tamaño tiene algunas compensaciones.

B: Una limitación es el tamaño de la unidad de implementación. DeepSeek-V3 requiere un clúster relativamente grande para una inferencia eficiente, lo que podría ser un desafío para equipos más pequeños. También hay margen de mejora en la velocidad de generación, aunque la decodificación especulativa con MTP ayuda.

A: Me parece justo. Pero en general, parece un gran paso adelante. ¿Qué sigue para DeepSeek-V3? ¿Hay alguna dirección futura que estén explorando?

B: Están considerando varias áreas, como refinar la arquitectura para admitir longitud de contexto infinita, explorar fuentes adicionales de señales de entrenamiento y mejorar las capacidades de razonamiento del modelo. También están trabajando en métodos de evaluación más completos para evaluar mejor el rendimiento del modelo.

A: Suena que no van a reducir la velocidad en ningún momento pronto. Gracias por guiarme a través de todo esto, DeepSeek-V3 es definitivamente un cambio de juego en el espacio de LLM de código abierto.

B: ¡Absolutamente! Es emocionante ver hasta dónde han llegado los modelos de código abierto. DeepSeek-V3 está empujando los límites, y no puedo esperar a ver qué harán después.