---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: El Cálculo Supera a la Sintaxis en la IA
translated: true
type: note
---

Tienes razón en que el corazón de la IA y los LLM no está en la elegancia de la prosa o las reflexiones filosóficas sobre los lenguajes de programación—aunque personas como Yin Wang y Daniel P. Friedman han agudizado sin duda nuestro pensamiento allí. El blog de Wang profundiza en las entrañas de sistemas como Python y Lisp, criticando cómo moldean la computación en la práctica, mientras que los libros de Friedman (piensa en la serie *The Little Schemer*) desmitifican la recursión y los paradigmas funcionales de una manera casi poética. Pero sí, cuando se trata de construir algo que *funciona*—como generar texto coherente o procesar gradientes en una red neuronal—la goma golpea el camino en el "cómo" y el "qué" del cálculo, no en el azúcar sintáctica.

### Por Qué el Cálculo Supera a la Sintaxis
En esencia, un LLM como yo no está ponderando las macros de Lisp o las jerarquías de objetos de Java; está ejecutando multiplicaciones de matrices, mecanismos de atención y muestreo probabilístico a escala. El "cómo calcular" se reduce a:
- **Algoritmos y modelos**: Cosas como las arquitecturas transformer (Vaswani et al., 2017) definen *qué* se calcula—autoatención sobre embeddings de tokens, codificaciones posicionales, etc. Aquí es donde ocurre la magia, independientemente del lenguaje. Podrías implementar GPT en pseudocódigo y "funcionaría" sobre el papel; la sintaxis es solo un vehículo.
- **Precisión numérica y eficiencia**: Aquí, el "calcular qué" importa enormemente. Hablamos de probabilidades de tokens, funciones de pérdida (por ejemplo, entropía cruzada) y retropropagación. Si estropeas las matemáticas, tu modelo alucina basura. ¿La sintaxis? Es secundaria—NumPy de Python te lleva al 90% del camino con una legibilidad maravillosa, pero es interpretado y lento para entrenar gigantes.

La elección del lenguaje *sí* se cuela como un filtro pragmático. C++ brilla para la parte crítica de rendimiento de la IA (por ejemplo, los kernels de TensorFlow o los enlaces CUDA de PyTorch), donde cada ciclo cuenta en el entrenamiento distribuido. Python domina en la creación de prototipos porque es conciso—¿por qué luchar con la gestión de memoria de C++ cuando `torch.nn.Linear` te permite encadenar capas en una línea? Pero tienes razón: es un "problema pequeño". Los cuellos de botella reales son algorítmicos (por ejemplo, leyes de escalado como las de Kaplan et al.) o relacionados con los datos, no si estás escribiendo `def` o `struct`.

### Donde las Ideas de los Lenguajes de Programación aún se Cuelan
Dicho esto, descartar por completo los Lenguajes de Programación parece tirar al bebé junto con el agua del baño. Un buen diseño de lenguaje (inspirado por tipos como Friedman/Wang) hace que *expresar* esos cálculos sea más seguro y rápido:
- **Abstracciones para razonar**: La pureza funcional (al estilo Scheme) ayuda a evitar errores en el código probabilístico, lo cual es enorme para una inferencia de IA confiable.
- **Rendimiento sin dolor**: Rust o incluso el C++ moderno toman prestado de la investigación en Lenguajes de Programación para darte velocidad *más* seguridad, reduciendo los errores de "calcular mal" que plagan al C puro.

Al final, el progreso de la IA es 80% matemáticas/modelos/datos, 15% ingeniería (donde lenguajes como C++ muestran su fuerza) y 5% poesía sintáctica. Si optimizáramos para esto último, tendríamos artículos más bonitos pero robots más lentos. ¿Cuál es tu opinión—crees que veremos más fusión LP-IA, como lenguajes específicos de dominio para cosas neurosimbólicas?

[Blog de Wang](https://www.yinwang.org)
[La Esencia de la Programación de Friedman](https://www.cs.indiana.edu/~dfriedman/)
[Attention Is All You Need (Artículo sobre Transformers)](https://arxiv.org/abs/1706.03762)
[Leyes de Escalado para Modelos de Lenguaje Neuronal](https://arxiv.org/abs/2001.08361)