---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Rendimiento de LoRA frente al Ajuste Fino Completo
translated: true
type: note
---

### Resumen del Rendimiento de LoRA frente al Fine-Tuning Completo

Basándose en análisis empírico de Thinking Machines Lab, LoRA (Low-Rank Adaptation) ofrece un fine-tuning eficiente en parámetros que a menudo iguala al fine-tuning completo (FullFT) en escenarios con limitaciones de capacidad, como conjuntos de datos pequeños o aprendizaje por refuerzo (RL), pero se degrada en conjuntos de datos más grandes debido a limitaciones inherentes en la dinámica del entrenamiento.[1] Esta expansión profundiza en cada hallazgo, explicando los mecanismos, la evidencia y las implicaciones prácticas para los desarrolladores de modelos.

### Equivalencia en Conjuntos de Datos Pequeños a Medianos de Sintonización por Instrucción y Razonamiento

LoRA logra una paridad de rendimiento con FullFT al realizar fine-tuning en conjuntos de datos de tamaño moderado, como los utilizados para seguir instrucciones (por ejemplo, conjuntos de datos estilo Alpaca) o tareas de razonamiento (por ejemplo, problemas matemáticos GSM8K). Esta equivalencia surge porque estos conjuntos de datos típicamente contienen entre 10,000 y 100,000 ejemplos, lo que se alinea bien con la capacidad de parametrización de bajo rango de LoRA. LoRA aproxima las actualizaciones de pesos como una descomposición matricial de bajo rango (ΔW = B A, donde B y A son matrices de bajo rango), lo que es suficiente para capturar los cambios de comportamiento específicos necesarios para tales tareas sin necesidad de la expresividad completa de actualizar todos los parámetros.

En la práctica, esto significa que los desarrolladores pueden usar LoRA para afinar modelos grandes (por ejemplo, de 70B+ parámetros) en hardware de consumo o instancias en la nube con memoria limitada, logrando las mismas métricas posteriores, como precisión o perplejidad, que con FullFT. Por ejemplo, en conjuntos de datos como Dolly-15k para instrucciones, LoRA con un rango de 8–16 produce resultados indistinguibles, ahorrando hasta el 99% en parámetros entrenables y tiempo de entrenamiento.[1] Sin embargo, esto se mantiene solo si el conjunto de datos no exige una generalización amplia más allá de la distribución de entrenamiento; los riesgos de sobreajuste siguen siendo similares a los de FullFT.

### Bajo Rendimiento en Conjuntos de Datos Grandes que Exceden la Capacidad de LoRA

Cuando los conjuntos de datos crecen más allá de la capacidad efectiva de LoRA (por ejemplo, millones de ejemplos para adaptación específica de dominio como la generación de código en The Stack), LoRA se queda por detrás de FullFT. El problema clave no es un "límite de capacidad" duro donde la pérdida se estanca abruptamente; en cambio, LoRA exhibe una eficiencia de entrenamiento reducida, con una convergencia de pérdida más lenta vinculada al desajuste entre el cuello de botella de bajo rango y la escala del conjunto de datos.

Esto proviene del sesgo inductivo de LoRA: la forma producto-de-matrices (W' = W + γ B A) restringe las actualizaciones a un subespacio, lo que funciona para cambios dispersos y de baja dimensión, pero lucha con las señales de alta varianza en conjuntos de datos grandes. Empíricamente, las curvas de pérdida muestran que LoRA requiere de 2 a 5 veces más pasos para alcanzar niveles cercanos a FullFT, e incluso entonces, el rendimiento final puede ser entre un 5% y un 10% peor en benchmarks como HumanEval para codificación.[1] La relación es paramétrica: la eficiencia disminuye a medida que el tamaño del conjunto de datos escala más rápido que el rango de LoRA (r), lo que sugiere que aumentar r ayuda marginalmente pero no compensa completamente sin arriesgar el sobreajuste en regímenes de pocos datos.

Las implicaciones incluyen preferir FullFT (o híbridos como QLoRA) para corpus masivos, mientras que LoRA brilla en la creación de prototipos iterativos. Esto también subraya la necesidad de estimar el tamaño del conjunto de datos antes de elegir métodos; herramientas como los conteos de tokens pueden guiar esto.

### Sensibilidad a Tamaños de Lote Grandes y Efectos de Parametrización

LoRA muestra una mayor intolerancia a los tamaños de lote grandes en comparación con FullFT, con penalizaciones de pérdida que surgen abruptamente más allá de los puntos óptimos (por ejemplo, tamaño de lote > 512). Mientras que el ruido del gradiente de FullFT se escala de manera más gradual, la configuración producto-de-matrices de LoRA amplifica la varianza en las actualizaciones de bajo rango, lo que lleva a una optimización inestable. Esta penalización persiste incluso si se aumenta el rango, ya que está arraigada en las diferentes propiedades del Hessiano de la forma bilineal frente a la optimización directa de pesos.

Por ejemplo, en experimentos con conjuntos de datos de razonamiento, la pérdida de LoRA aumenta entre un 20% y un 30% más rápido con tamaños de lote superiores a 1k, mientras que FullFT se estabiliza mediante un promedio de parámetros más amplio.[1] Las estrategias de mitigación incluyen la acumulación de gradientes para simular lotes efectivos más pequeños o el uso de técnicas como AdamW con una programación cuidadosa de la tasa de aprendizaje. Esta dinámica resalta la compensación de LoRA: eficiencia en memoria pero fragilidad al escalar el paralelismo computacional, lo que lo hace menos ideal para clústeres de entrenamiento de alto rendimiento.

### Beneficios de Aplicar LoRA a Todas las Capas, Especialmente MLPs y MoEs

Incluso en conjuntos de datos pequeños, aplicar LoRA universalmente (a capas de atención, MLP y Mixture-of-Experts) supera a las variantes que solo aplican a la atención, particularmente cuando los recuentos de parámetros se igualan mediante rangos más altos. La variante de LoRA que solo aplica a la atención, común en las primeras implementaciones, tiene un rendimiento entre un 3% y un 7% inferior en tareas como el razonamiento de múltiples saltos porque descuida las capas feed-forward (MLPs/MoEs), que manejan la mayoría de las transformaciones no lineales y la integración de conocimiento específico del dominio.

LoRA de capa completa aprovecha la arquitectura del modelo de manera más holística: los MLPs contribuyen con aproximadamente el 70% de los parámetros y capturan cálculos específicos de la tarea, mientras que los MoEs (en modelos como Mixtral) se benefician de adaptaciones específicas de la ruta. Igualar los parámetros aumentando solo el rango de la atención falla debido a la redundancia en las cabezas de atención, lo que lleva a subespacios ineficientes. Mejores prácticas: Utilice un rango de 16 a 64 en todas las capas para datos pequeños, obteniendo ganancias en eficiencia y evaluaciones sin añadir cómputo.[1] Este hallazgo fomenta una adopción más amplia en bibliotecas como PEFT, reduciendo el "impuesto LoRA" en arquitecturas especializadas.

### Equivalencia en Aprendizaje por Refuerzo con Rangos Bajos

LoRA iguala a FullFT en el fine-tuning por RL (por ejemplo, RLHF o DPO en conjuntos de datos de preferencia), incluso con rangos muy bajos (r=4–8), debido a los requisitos inherentes de baja capacidad del RL. Teóricamente, desde la perspectiva de la información, las actualizaciones de RL se centran en el modelado de recompensas y los gradientes de política sobre trayectorias dispersas, rara vez excediendo el poder de representación de los deltas de bajo rango, a diferencia de las predicciones de tokens densas del aprendizaje supervisado.

Anticipado por la teoría, esto se cumple porque las pérdidas de RL (por ejemplo, los clips de PPO) enfatizan los cambios direccionales en el comportamiento, que el subespacio de LoRA codifica eficientemente sin necesidad de una parametrización completa. Los experimentos confirman la paridad en benchmarks como HH-RLHF de Anthropic, con LoRA convergiendo más rápido y usando 10 veces menos memoria.[1] Para los profesionales, esto convierte a LoRA en una opción por defecto para las canalizaciones de RL, permitiendo la alineación escalable de modelos de billones de parámetros en hardware modesto.

### Implicaciones Más Amplias y Recomendaciones

Estas ideas revelan a LoRA como una herramienta pragmática para la mayoría de las necesidades posteriores al entrenamiento, especialmente en entornos con recursos limitados, pero no como un reemplazo universal para FullFT en datos expansivos. Trabajos futuros podrían explorar rangos adaptativos o escalado específico por capa para cerrar las brechas. Los desarrolladores deben realizar benchmarks en la escala de su conjunto de datos y monitorear los efectos del tamaño de lote desde el principio.[1] En general, LoRA democratiza el fine-tuning sin arrepentimiento en escenarios específicos, alineándose con el cambio hacia el desarrollo eficiente de IA.

Citas:
[1] https://tinker-docs.thinkingmachines.ai/lora-primer