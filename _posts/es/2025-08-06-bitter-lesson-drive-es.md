---
audio: false
generated: true
image: false
lang: es
layout: post
title: La Amarga Lección Impulsa la Evolución del Transformador
translated: true
type: note
---

En su charla en el evento Stanford CS25, Hyung Won Chung ofrece un análisis histórico y predictivo detallado de las arquitecturas **Transformer**, argumentando que comprender las fuerzas impulsoras detrás de su evolución es clave para anticipar el futuro de la IA. El núcleo de su argumento se centra en "La Lección Amarga" del desarrollo de la IA, que ilustra a través de la evolución de los modelos Transformer.

***

### La Fuerza Impulsora del Progreso de la IA

Chung postula que el factor más significativo que impulsa la investigación en IA es el **coste exponencialmente decreciente del cómputo**, que ha permitido un aumento correspondiente en la escala de los modelos y los datos. Argumenta que para entender el ritmo acelerado de cambio en el campo, uno debe centrarse en esta fuerza impulsora dominante en lugar de perderse en los detalles de las innovaciones arquitectónicas individuales.

Introduce **"La Lección Amarga"**, un concepto que sugiere que el progreso de la IA a largo plazo favorece métodos más simples y generales con menos suposiciones incorporadas (sesgos inductivos). Mientras que los modelos altamente estructurados y específicos de un dominio pueden ofrecer ganancias a corto plazo, finalmente se convierten en cuellos de botella a medida que escalan el cómputo y los datos. Alienta a los investigadores a cuestionar y simplificar constantemente las estructuras subyacentes de sus modelos.

***

### La Evolución de las Arquitecturas Transformer

Chung utiliza tres arquitecturas Transformer principales para ejemplificar sus puntos:

1.  **Codificador-Decodificador (Transformer Original):** Esta arquitectura, utilizada originalmente para tareas como la traducción automática, tiene una estructura más inherente. Utiliza parámetros separados para el codificador y el decodificador y patrones específicos de atención cruzada. Si bien es efectiva para tareas de entrada/salida distintas, esta estructura está volviéndose menos relevante en la era de los modelos grandes de propósito general.

2.  **Solo Codificador (ej., BERT):** Una arquitectura más simple que renuncia a la generación, centrándose en tareas como la clasificación. Si bien es potente para benchmarks específicos, su enfoque estrecho la hace menos generalizable para una amplia gama de aplicaciones modernas.

3.  **Solo Decodificador (ej., GPT-3):** Esta es la más general y menos estructurada de las tres. Utiliza una única pila de capas y parámetros compartidos, lo que la hace muy adecuada para los modernos modelos de lenguaje grandes que manejan diversas tareas, aprenden conocimiento general y realizan generación de texto extenso.

***

### Conclusiones Clave y Predicciones

Según Chung, la tendencia es clara: la IA se está moviendo hacia **arquitecturas más simples y generales con menos estructura impuesta**. Esto permite a los modelos la libertad de aprender patrones y relaciones complejas a partir de vastas cantidades de datos sin estar limitados por suposiciones fijas.

Sugiere que el próximo cuello de botella en la IA podría no ser la arquitectura en sí, sino el **objetivo de aprendizaje**. Considera métodos como el Aprendizaje por Refuerzo a partir de la Retroalimentación Humana (RLHF) como un paso hacia funciones de objetivo menos estructuradas y aprendidas que son más adecuadas para tareas de generación abiertas y complejas. Alienta a la audiencia a pensar críticamente sobre estos principios para ayudar a dar forma al futuro de la IA.

Puedes ver la charla completa en [https://www.youtube.com/watch?v=3gb-ZkVRemQ&pp=0gcJCfwAo7VqN5tD](https://www.youtube.com/watch?v=3gb-ZkVRemQ&pp=0gcJCfwAo7VqN5tD).