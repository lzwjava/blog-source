---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'Transformadores: Orígenes, Diseño y Futuro'
translated: true
type: note
---

### Resumen de "Cómo aprendí a dejar de preocuparme y amar el Transformer" por Ashish Vaswani

Esta charla de 45 minutos, impartida el 7 de noviembre de 2023 como parte de la serie CS25 Transformers United de Stanford, es una inmersión reflexiva en los orígenes, diseño, evolución y futuro de la arquitectura Transformer. Como coautor del innovador artículo de 2017 "Attention Is All You Need", Vaswani comparte anécdotas personales de su tiempo en Google Brain, desmitifica decisiones clave y ofrece visiones optimistas pero fundamentadas para la próxima fase de la IA. Está estructurada en torno al contexto histórico, las innovaciones centrales, los avances posteriores al Transformer y las ideas de futuro, perfecta para entender por qué los Transformers se convirtieron en la columna vertebral de la IA moderna.

#### Antecedentes históricos y la chispa de los Transformers
Vaswani comienza con un guiño a la Conferencia de Dartmouth de 1956, donde los pioneros de la IA soñaban con una máquina unificada que imitara la inteligencia humana a través de la visión, el lenguaje y más, utilizando sistemas basados en reglas y asumiendo victorias rápidas. Avance rápido 70 años: a pesar de los inviernos de la IA, estamos volviendo con los Transformers impulsando modelos multimodales. Contrasta esto con la PNL de los años 2000, que era un desordenado mosaico de pipelines para tareas como la traducción automática (por ejemplo, alineamientos de palabras, extracción de frases, revaloración neuronal). Para 2013, el campo estaba fragmentado en silos como el análisis de sentimientos o el diálogo, con el progreso impulsado por la financiación más que por una teoría unificada.

¿El punto de inflexión? Las representaciones distribuidas (por ejemplo, "rey - hombre + mujer ≈ reina" de word2vec) y los modelos seq2seq (2014-2015), que colapsaron diversas tareas en frameworks de codificador-decodificador. Pero las redes recurrentes como las LSTM eran un problema: el procesamiento secuencial mataba el paralelismo, los estados ocultos creaban cuellos de botella de información y las dependencias de largo alcance eran débiles. Las convoluciones (por ejemplo, ByteNet, ConvS2S) ayudaron con la velocidad pero luchaban con las conexiones distantes.

**Anécdota interna:** Trabajando en Google Neural Machine Translation (GNMT) en 2016, el equipo de Vaswani abandonó los pipelines por LSTMs puras, alcanzando el estado del arte con datos masivos. Sin embargo, las LSTMs se sentían "frustrantes": lentas en GPUs, difíciles de escalar. El "aja" fue anhelar el paralelismo total: codificar entradas y decodificar salidas sin la monotonía paso a paso. Los primeros sueños no autorregresivos (generar todo de una vez, luego refinar) fracasaron porque los modelos no podían aprender el orden sin la guía de izquierda a derecha, que naturalmente poda las rutas improbables.

#### Decisiones de diseño centrales: Construyendo el Transformer original
Los Transformers abandonaron la recurrencia y las convoluciones por atención pura, permitiendo chats directos de token a token a través de la similitud de contenido, como extraer parches de imagen similares en tareas de visión (por ejemplo, eliminación de ruido por medias no locales). La auto-atención es invariante a la permutación pero amigable con el paralelismo, con una complejidad O(n² d) que es oro para GPUs cuando las secuencias no son interminables.

Bloques de construcción clave:
- **Atención de Producto Punto Escalado:** Proyecciones Q, K, V de las entradas; puntuaciones como softmax(QK^T / √d_k) ponderadas sobre V. Escalado para evitar gradientes que se desvanecen (asumiendo varianza unitaria). Enmascaramiento causal para los decodificadores evita mirar hacia adelante. Elegido sobre la atención aditiva por la velocidad de la multiplicación de matrices.
- **Atención Multi-Cabeza:** Una sola cabeza promedia demasiado (por ejemplo, difuminando los roles de "el gato se lamió la mano"). Las cabezas dividen las dimensiones en subespacios, como máquinas de Turing multi-cinta, para subespacios enfocados (por ejemplo, una cabeza se bloquea con probabilidad 1 en detalles específicos). Sin cómputo extra, selectividad similar a la convolución.
- **Codificación Posicional:** Los sinusoides inyectan orden, apuntando a posiciones relativas (descomponibles por distancia). No aprendió del todo las relativas inicialmente, pero funcionó.
- **Apilar y Estabilizar:** Pilas de codificador-decodificador con residuales y normalización de capa (pre-norma después para redes más profundas). Las redes feed-forward se expanden/contraen como ResNets. Codificador: auto-atención; Decodificador: auto-atención enmascarada + atención cruzada.

Aplastó los benchmarks de WMT con 8 veces menos flops que los ensembles de LSTM, se generalizó al análisis sintáctico y sugirió potencial multimodal. ¿Interpretabilidad? Las cabezas se especializaron (algunas de largo alcance, otras locales como conv), pero Vaswani bromea diciendo que es "leer hojas de té": prometedor pero difuso.

#### Evolución: Correcciones y Victorias de Escalado
Los Transformers "prendieron" porque son simples, pero los ajustes los amplificaron:
- **Posiciones 2.0:** Los sinusoides se quedaron cortos en relativas; los embeddings relativos (sesgos por par) impulsaron la traducción/música. ALiBi (sesgos de distancia aprendidos) extrapola longitudes; RoPE (rotaciones que mezclan absoluto/relativo) es ahora el rey: ahorra memoria, clava las relativas.
- **Contextos Largos:** ¿Maldición cuadrática? Ventanas locales, patrones dispersos (escalonados/globales), hashing (Reformer), recuperación (Memorizing Transformer), trucos de bajo rango. Flash Attention omite escrituras en memoria para velocidad; Multi-Query reduce cabezas KV para inferencia. Los modelos grandes diluyen el coste de la atención de todos modos.
- **Otros Ajustes:** La pre-norma estabiliza; la decodificación especulativa (borrador rápido, verificación lenta) imita la velocidad no autorregresiva en producción.

**Perla interna:** Hackear la atención relativa eficiente fue "calistenia matricial", pero la física del hardware (por ejemplo, productos punto para aceleradores) guió las decisiones.

#### Direcciones Futuras: Más allá del Escalado
Vaswani es optimista: Los gigantes auto-supervisados permiten agentes en contexto, haciendo eco a la máquina unificada de Dartmouth. Las leyes de escalado mandan, pero hay que vigilar los renacimientos de RNN o mejores arquitecturas. Prioridades:
- **Agentes Multimodales:** Programa mediante prompts a miles; las herramientas como puentes (internalizar las simples, colaborar en las complejas).
- **Datos e Infraestructura:** Mejoras de 2x con mejores datos; FP8/INT8 para ancho de banda, entrenamiento a escala InfiniBand.
- **Inteligencia Adaptativa:** Modelos pequeños + planificadores/representaciones de datos igualan a los grandes; few-shot en inferencia; señalización de incertidumbre; construcción de habilidades (por ejemplo, bots de Minecraft).
- **Magia Full-Stack:** Bucles de retroalimentación para flujos de trabajo (por ejemplo, análisis de datos como minería de "conocimiento oscuro").
- **Emergentes:** Desde el "grokking" en juguetes hasta los misterios de GPT-4: estudiar lo pequeño para entender lo grande.
- **Sistemas:** El ancho de banda de memoria es el cuello de botella; recuperación para todo.

Insínua su startup con el coautor Noam Shazeer: Automatizando flujos de trabajo desde el procesamiento de datos, full-stack para la magia de la retroalimentación. Herramientas hasta que sean "Transformers hasta el fondo", aprovechando la inteligencia del software.

#### Puntos Destacados de la Sesión de Preguntas y Respuestas
En la charla posterior:
- Obstáculos no autorregresivos: Necesita un "ordenamiento oráculo" para la independencia; los espacios latentes ayudan pero la multimodalidad pica.
- Mundo desde el Texto: Los LLMs + RLHF extraen planificadores robóticos; mezclar datos de entrenamiento despierta creatividad "nueva".
- Modularidad: MoE induce expertos; la coordinación multi-agente (objetivos, actualizaciones, verificaciones) es clave.
- Consejo: Perseguir el bucle cerrado humano-IA; el campo está abierto de par en par para sorpresas.

Cosas atemporales: vibraciones históricas, profundidad técnica, inspiración sin exageraciones. Si estás en IA, es una visita obligada para entender el contexto de por qué los Transformers ganaron.

[Cómo aprendí a dejar de preocuparme y amar el Transformer (YouTube)](https://www.youtube.com/watch?v=1GbDTTK3aR4)