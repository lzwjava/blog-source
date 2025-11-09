---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Explicación Estructurada de PEFT y LoRA
translated: true
type: note
---

A continuación, proporcionaré una explicación profunda y estructurada del texto proporcionado. Lo desglosaré paso a paso, comenzando con los conceptos fundamentales y avanzando hasta los detalles específicos del Ajuste Fino Eficiente en Parámetros (PEFT) y la Adaptación de Bajo Rango (LoRA). Usaré analogías, intuición matemática y contexto del mundo real para hacerlo accesible pero exhaustivo. Esta explicación se basa directamente en el texto mientras amplía las ideas subyacentes, motivaciones e implicaciones en el aprendizaje automático (ML) para modelos de lenguaje grandes (LLMs).

### 1. La Escala de los Modelos de Lenguaje Modernos: Pretraining y por qué Importa
El texto comienza destacando la inmensa escala de los principales LLMs actuales: "Los principales modelos de lenguaje de hoy contienen más de un billón de parámetros, preentrenados en decenas de billones de tokens. El rendimiento del modelo base sigue mejorando con la escala, ya que estos billones son necesarios para aprender y representar todos los patrones del conocimiento humano escrito".

#### ¿Qué son los Parámetros y los Tokens?
-   **Parámetros** son los "pesos" en una red neuronal: valores numéricos que el modelo aprende durante el entrenamiento. Piensa en ellos como la "memoria" o "perillas de conocimiento" del modelo. Un modelo de un billón de parámetros (por ejemplo, GPT-4 o PaLM) tiene alrededor de 1,000 billones de tales valores, aproximadamente equivalente al almacenamiento de datos de millones de imágenes de alta resolución.
-   **Tokens** son las unidades básicas de texto que el modelo procesa (por ejemplo, palabras o subpalabras). El preentrenamiento implica alimentar al modelo con **decenas de billones** de estos (por ejemplo, de libros, sitios web y repositorios de código) para que aprenda patrones generales como gramática, hechos y razonamiento.

#### ¿Por qué la Escala Mejora el Rendimiento?
-   Los LLMs son arquitecturas basadas en transformadores (introducidas en el artículo de 2017 "Attention is All You Need"), que sobresalen en capturar patrones complejos a través de capas de mecanismos de atención y redes feed-forward.
-   Las leyes de escala empíricas (por ejemplo, de Kaplan et al. de OpenAI, 2020) muestran que el rendimiento (por ejemplo, la precisión en tareas como responder preguntas) mejora de manera predecible con más parámetros, datos y capacidad de cómputo. Duplicar los parámetros a menudo produce ganancias logarítmicas en "habilidades emergentes" (por ejemplo, el modelo de repente se vuelve bueno en matemáticas o traducción).
-   **Intuición**: El conocimiento humano es vasto e interconectado. Para representarlo todo (por ejemplo, la sintaxis de cada idioma, los hechos históricos, los principios científicos), el modelo necesita un enorme "espacio de parámetros" para codificar esto como correlaciones de bajo nivel. Los modelos más pequeños (por ejemplo, 1 billón de parámetros) se sobreajustan a patrones superficiales y fallan en tareas matizadas, mientras que los modelos a escala de billones generalizan mejor.
-   **Compromisos**: Esta escala requiere una capacidad de cómputo masiva (por ejemplo, miles de GPUs durante semanas) y energía, pero es la base para "modelos base" como las series Llama o GPT.

En resumen, el preentrenamiento construye un "cerebro" de propósito general forzando patrones del corpus escrito de la humanidad. El texto enfatiza esto como la base antes de cualquier especialización.

### 2. Post-Entrenamiento (Ajuste Fino): Enfoque más Estrecho y Desafíos de Eficiencia
El texto contrasta el preentrenamiento con el "post-entrenamiento", que "implica conjuntos de datos más pequeños y generalmente se centra en dominios de conocimiento más estrechos y rangos de comportamiento. Parece un desperdicio usar un terabit de pesos para representar actualizaciones de un gigabit o megabit de datos de entrenamiento".

#### ¿Qué es el Post-Entrenamiento/Ajuste Fino?
-   Después del preentrenamiento, el modelo base se "afina" en conjuntos de datos más pequeños y específicos de la tarea (por ejemplo, 1-10 millones de ejemplos frente a billones de tokens). Esto lo adapta para aplicaciones como chatbots (por ejemplo, que sigan instrucciones), análisis de sentimientos o preguntas y respuestas médicas.
-   Ejemplos: Ajustar GPT-3 en registros de soporte al cliente para crear un asistente útil, o en textos legales para revisar contratos.
-   **¿Por qué conjuntos de datos más pequeños?** El ajuste fino apunta a "actualizaciones" o "sobreescrituras" del conocimiento base, por ejemplo, enseñando cortesía o jerga específica del dominio, sin reinventar la comprensión general del lenguaje.

#### La Intuición del Desperdicio
-   **Desajuste entre Datos y Tamaño del Modelo**: Si el modelo base tiene ~1 billón de parámetros (escala de terabit, ya que aproximadamente 1 bit por parámetro), pero los datos de ajuste fino son pequeños (escala de gigabit o megabit), actualizar *todos* los parámetros es como reescribir una enciclopedia completa para una sola nota al pie. La mayoría de los pesos del modelo siguen siendo irrelevantes para la nueva tarea.
-   **Problemas del Ajuste Fino Completo (FullFT)**:
    -   **Sobrecarga de Cómputo**: Actualizar todos los parámetros requiere recalcular los gradientes (señales de error) para todo el modelo durante cada paso de entrenamiento. Esto multiplica los costes de memoria y tiempo por 10-100x.
    -   **Olvido Catastrófico**: FullFT puede degradar las habilidades generales del modelo (por ejemplo, un modelo ajustado para matemáticas olvida poesía).
    -   **Hinchamiento de Almacenamiento**: Los modelos ajustados son tan grandes como la base (billones de parámetros), lo que hace que la implementación sea costosa (por ejemplo, los costes en la nube escalan con el tamaño).
-   **Analogía**: Imagina afinar una orquesta masiva para una sola actuación en solitario reentrenando a cada músico. Es excesivo cuando podrías simplemente entrenar al solista.

Esta ineficiencia motivó el **Ajuste Fino Eficiente en Parámetros (PEFT)**: Métodos para actualizar solo una pequeña fracción (por ejemplo, 0.1-1%) de los parámetros logrando el 90-100% de las ganancias de rendimiento de FullFT.

### 3. Ajuste Fino Eficiente en Parámetros (PEFT): La Gran Idea
"PEFT... ajusta una red grande actualizando un conjunto de parámetros mucho más pequeño".

-   **Motivación Central**: Preservar las fortalezas del modelo base mientras se inyectan actualizaciones específicas de la tarea con cambios mínimos. Esto reduce el cómputo, la memoria y el almacenamiento, algo crucial para democratizar la IA (por ejemplo, permitiendo que equipos más pequeños ajusten modelos como Llama 2 sin supercomputadoras).
-   **Técnicas Comunes de PEFT** (más allá de LoRA, mencionado más adelante):
    -   **Adaptadores**: Insertan pequeños módulos "conectables" (por ejemplo, capas de cuello de botella) entre las capas del transformador, entrenando solo esos.
    -   **Ajuste de Prompt**: Aprende prompts suaves (por ejemplo, tokens virtuales) antepuestos a las entradas, actualizando solo ~0.01% de los parámetros.
    -   **Ajuste de Prefijo**: Similar, pero ajusta prefijos para las capas de atención.
-   **Por qué Funciona**: Las actualizaciones del ajuste fino suelen ser de "baja dimensión": se encuentran en un subespacio del espacio completo de parámetros. No es necesario retocar todo; unos pocos cambios dirigidos se propagan a través de la red.
-   **Éxito Empírico**: Los métodos PEFT igualan o superan a FullFT en puntos de referencia como GLUE (comprensión del lenguaje natural) con 10-100x menos cómputo. Bibliotecas como PEFT de Hugging Face hacen que esto sea plug-and-play.

PEFT cambia el paradigma de "entrenar todo" a "editar quirúrgicamente", alineándose con el tema de eficiencia del texto.

### 4. Adaptación de Bajo Rango (LoRA): El Método PEFT Líder
"El método PEFT líder es la adaptación de bajo rango, o LoRA. LoRA reemplaza cada matriz de peso W del modelo original con una versión modificada W′ = W + γ B A, donde B y A son matrices que juntas tienen muchos menos parámetros que W, y γ es un factor de escalado constante. En efecto, LoRA crea una representación de baja dimensión de las actualizaciones impartidas por el ajuste fino".

#### Desglose Matemático
LoRA apunta a las matrices de peso **W** en el transformador (por ejemplo, en las proyecciones de consulta/clave/valor para la atención o las capas feed-forward). Estas son típicamente matrices d × k (por ejemplo, 4096 × 4096, millones de parámetros cada una).

-   **La Fórmula**: Durante el ajuste fino, en lugar de actualizar W directamente, LoRA calcula las salidas como:
    ```
    h = W x + γ (B A) x  (donde x es la entrada)
    ```
    -   **W**: Pesos originales congelados (sin cambios).
    -   **A**: Una matriz de bajo rango, inicializada aleatoriamente (por ejemplo, r × k, donde r << d, como r=8-64).
    -   **B**: Otra matriz de bajo rango (d × r), inicializada a cero (para que la actualización inicial sea cero, evitando interrupciones).
    -   **γ (gamma)**: Factor de escalado (por ejemplo, γ = α / r, donde α es un hiperparámetro como 16) para controlar la magnitud de la actualización y estabilizar el entrenamiento.
    -   Peso actualizado completo: **W' = W + γ B A**.

-   **¿Por qué "Bajo Rango"?**
    -   Las matrices se pueden descomponer mediante descomposición en valores singulares (SVD): Cualquier matriz ≈ U Σ V^T, donde el "rango" es el número de valores singulares significativos.
    -   Las actualizaciones del ajuste fino ΔW = W' - W son a menudo de **bajo rango** (r << min(d,k)), lo que significa que capturan cambios en un subespacio comprimido (por ejemplo, algunas direcciones como "enfatizar la seguridad" o "centrarse en el código").
    -   **B A** aproxima ΔW con rango-r (parámetros: d*r + r*k vs. d*k para W completa). Para r=8 en una W de 4096×4096, LoRA usa ~65k parámetros vs. 16M: ¡una reducción del 99.6%!
    -   **Intuición**: Las actualizaciones son como vectores en un espacio de alta dimensión; LoRA los proyecta en una "autopista" de baja dimensión (rango r), ignorando el ruido en el vasto espacio de parámetros.

-   **Cómo Funciona el Entrenamiento**:
    1.  Paso hacia adelante: Calcula h usando W + γ B A, pero solo entrena A y B (W congelado).
    2.  Retropropagación: Los gradientes fluyen solo hacia A/B, manteniendo la memoria baja.
    3.  Inferencia: O bien se fusiona (W' = W + B A) para un solo modelo o se mantiene separado para modularidad.
-   **Del Artículo (Hu et al., 2021)**: LoRA se introdujo para modelos de visión/lenguaje pero explotó en PLN. Supera a los adaptadores en tareas como resumen mientras usa menos memoria. Variantes como QLoRA cuantifican aún más el modelo base para huellas aún más pequeñas.

En esencia, LoRA "hackea" el modelo añadiendo un "delta" ligero (B A) que representa el ajuste fino como una transformación lineal compacta.

### 5. Ventajas de LoRA sobre el Ajuste Fino Completo (FullFT)
El texto enumera beneficios operativos, enfatizando la practicidad más allá de la eficiencia bruta. Ampliaré cada uno.

#### a. Costo y Velocidad del Post-Entrenamiento
-   LoRA entrena 100-1000x más rápido/más barato ya que actualiza ~0.1% de los parámetros. Por ejemplo, ajustar Llama-7B en una sola GPU A100 (FullFT necesita 8+ GPUs) toma horas frente a días.
-   Baja precisión (por ejemplo, bfloat16) es suficiente, reduciendo el uso de energía.

#### b. Servicio Multi-Inquilino
"Dado que LoRA entrena un adaptador (es decir, las matrices A y B) mientras mantiene los pesos originales sin cambios, un único servidor de inferencia puede mantener muchos adaptadores (diferentes versiones del modelo) en memoria y muestrear de ellos simultáneamente de forma agrupada. Punica: Multi-Tenant LoRA Serving (Chen, Ye, et al, 2023) Los motores de inferencia modernos como vLLM y SGLang implementan esta característica".

-   **Qué Significa**: La base W es compartida; los adaptadores son pequeños (MBs vs. GBs para modelos completos). Un servidor carga una W + N adaptadores (por ejemplo, para codificación, escritura, traducción).
-   **Multi-Inquilino**: Sirve múltiples usuarios/modelos en paralelo sin recargar la base. Agrupa solicitudes entre adaptadores para mayor eficiencia.
-   **Impacto en el Mundo Real**: En producción (por ejemplo, Hugging Face Spaces o Azure ML), esto permite "sopas de modelos" o cambiar de personalidad sobre la marcha. Punica (2023) optimiza la memoria mediante paginación; vLLM/SGLang usan atención paginada para un rendimiento 10x mayor.
-   **Analogía**: Como un solo motor (W) con kits turbo intercambiables (adaptadores) frente a comprar un coche nuevo por cada ajuste.

#### c. Tamaño del Diseño para el Entrenamiento
"Al ajustar todo el modelo, el estado del optimizador debe almacenarse junto con los pesos originales, a menudo con mayor precisión. Como resultado, FullFT generalmente requiere un orden de magnitud más de aceleradores que muestrear del mismo modelo... Para el entrenamiento, además de almacenar los pesos, normalmente necesitamos almacenar gradientes y momentos del optimizador para todos los pesos; además, estas variables a menudo se almacenan con mayor precisión (float32) que la utilizada para almacenar los pesos para inferencia (bfloat16 o inferior). Dado que LoRA entrena muchos menos pesos y usa mucha menos memoria, puede entrenarse en un diseño solo ligeramente más grande que el utilizado para el muestreo".

-   **Desglose de la Memoria de Entrenamiento**:
    -   FullFT: Pesos (1T parámetros @ bfloat16 = ~2TB) + Gradientes (igual) + Estados del optimizador (por ejemplo, Adam: 2 momentos por parámetro @ float32 = ~8TB total). Necesita 100s de GPUs en un "diseño" distribuido (por ejemplo, paralelismo de datos/modelo).
    -   LoRA: Solo A/B (~0.1% de parámetros) obtienen gradientes/estados (~2-10GB extra). Entrena en 1-2 GPUs, igual que el diseño de inferencia.
-   **Detalles de Precisión**: La inferencia usa baja precisión (bfloat16/float16) para velocidad; el entrenamiento necesita float32 para la estabilidad del gradiente. LoRA minimiza esta sobrecarga.
-   **Accesibilidad**: Los aficionados/startups pueden ajustar en hardware de consumo (por ejemplo, RTX 4090), frente a FullFT que requiere clusters empresariales. Eficiencia: LoRA a menudo converge más rápido debido a menos variables.

#### d. Facilidad de Carga y Transferencia
"Con menos pesos que almacenar, los adaptadores LoRA son rápidos y fáciles de configurar o transferir entre máquinas".

-   Los adaptadores son archivos de <100MB (frente a 100s de GB para modelos completos), comprimibles y compartibles (por ejemplo, a través de GitHub o torrents).
-   Implementación: Carga la base una vez, intercambia adaptadores en segundos. La fusión es opcional para permanencia.
-   **Casos Extremos**: Control de versiones (por ejemplo, Git para adaptadores), aprendizaje federado (entrena adaptadores en el dispositivo, envía solo deltas) o ajuste iterativo (apila múltiples LoRAs).

### Implicaciones y Limitaciones más Amplias
-   **Por qué LoRA Domina**: Es simple, efectivo y se integra perfectamente (por ejemplo, en la biblioteca PEFT). Se usa en modelos como los ajustes de Stable Diffusion o Alpaca (Llama ajustado por instrucciones).
-   **Limitaciones**: No siempre es tan performante como FullFT en tareas muy específicas; la elección del rango r importa (demasiado bajo se subajusta, demasiado alto desperdicia eficiencia). No maneja todos los tipos de actualización (por ejemplo, cambios arquitectónicos).
-   **Tendencias Futuras**: Extensiones como DoRA (descompone pesos aún más) o VeRA (basado en vectores, aún más disperso). A medida que los modelos escalan a 10T+ parámetros, PEFT/LoRA se vuelve esencial para la sostenibilidad.

Este texto encapsula un cambio pivotal en la IA: desde el reentrenamiento completo que consume muchos recursos hasta actualizaciones modulares y elegantes. Si deseas derivaciones matemáticas, ejemplos de código (por ejemplo, en PyTorch) o inmersiones en artículos relacionados, ¡avísame!