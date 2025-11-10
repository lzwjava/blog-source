---
audio: false
generated: true
lang: es
layout: post
title: La visión artificial no iguala a la humana
translated: true
type: note
---

La publicación de blog de Yin Wang argumenta que los sistemas de visión por computadora, incluso los avanzados en 2019, estaban lejos de alcanzar un rendimiento a nivel humano. Afirma que estos sistemas tienen dificultades con el reconocimiento básico de objetos (por ejemplo, identificar un coche) y son fácilmente engañados por ejemplos adversariales o alteraciones menores en la imagen, a diferencia de los humanos que reconocen objetos sin esfuerzo. Wang sugiere que el campo exagera su progreso y que la verdadera visión por computadora a nivel humano sigue siendo esquiva debido a limitaciones fundamentales en cómo estos sistemas procesan y comprenden las imágenes.

### ¿Es cierto?
En el momento de la publicación en octubre de 2019, el argumento de Wang tenía mérito basándose en el estado de la visión por computadora en ese momento:

- **Generalización Limitada**: Los modelos de visión por computadora, como las redes neuronales convolucionales (CNNs), dependían en gran medida de la coincidencia de patrones dentro de los datos de entrenamiento. A menudo no lograban generalizar a nuevos contextos o manejar bien casos extremos, como describe Wang. Por ejemplo, los modelos podían clasificar erróneamente objetos cuando la iluminación, los ángulos o los fondos cambiaban significativamente.

- **Vulnerabilidad Adversarial**: El punto de Wang sobre los ejemplos adversariales—imágenes sutilmente alteradas para engañar a los modelos—era preciso. Investigaciones, como la de Goodfellow et al. (2014), mostraron que pequeñas perturbaciones imperceptibles podían hacer que los modelos clasificaran erróneamente imágenes con alta confianza, destacando una brecha entre la visión humana y la máquina.

- **Afirmaciones Exageradas**: La publicación critica el bombo publicitario en torno a la visión por computadora. En 2019, aunque modelos como ResNet, YOLO y los primeros transformers mostraban resultados impresionantes en benchmarks (por ejemplo, ImageNet), estos eran conjuntos de datos controlados. Las aplicaciones del mundo real a menudo revelaban debilidades, como identificaciones erróneas en sistemas de conducción autónoma o de reconocimiento facial.

Sin embargo, el tono de la publicación es absoluto, afirmando "no existe una visión por computadora a nivel humano". Esto pasa por alto el progreso en tareas específicas. Por ejemplo:
- **Éxito en Tareas Específicas**: Para 2019, los sistemas de visión por computadora superaban a los humanos en tareas específicas como clasificar ciertas imágenes médicas (por ejemplo, detectar retinopatía diabética) o reconocer objetos específicos en entornos controlados.
- **Progreso Desde 2019**: Para 2025, avances como los vision transformers (por ejemplo, ViT, CLIP) y modelos multimodales a gran escala (por ejemplo, GPT-4o, DALL·E 3) han reducido la brecha. Estos modelos manejan entradas más diversas, generalizan mejor entre contextos e integran lenguaje y visión para un razonamiento mejorado. Aún así, no replican completamente la robustez, la conciencia contextual o la comprensión intuitiva de la visión humana.

### Evaluación Crítica
La afirmación central de Wang—que la visión por computadora en 2019 no era a nivel humano—es en gran parte cierta. Los modelos carecían de la generalización, robustez y comprensión intuitiva de la visión humana. Sin embargo, su desestimación del progreso puede ser demasiado pesimista, ya que se han logrado avances significativos desde entonces. Incluso en 2025, aunque la visión por computadora sobresale en dominios específicos, todavía no alcanza la percepción a nivel humano en escenarios de mundo abierto debido a problemas como:
- **Razonamiento Contextual**: Los humanos integran datos sensoriales con conocimiento del mundo sin esfuerzo; las máquinas luchan con esto.
- **Casos Extremos**: Los modelos pueden fallar en situaciones raras o novedosas donde los humanos se adaptan rápidamente.
- **Eficiencia Energética**: La visión humana es mucho más eficiente energéticamente que los modelos computacionales.

La publicación sigue siendo relevante como una crítica a la exageración de las capacidades de la IA, pero no tiene en cuenta el rápido progreso en el campo. Ninguna fuente única confirma que se haya logrado una visión "a nivel humano" para 2025, pero la brecha se ha reducido significativamente.[](https://yinwang0.wordpress.com/2019/10/20/human-level-computer-vision/)