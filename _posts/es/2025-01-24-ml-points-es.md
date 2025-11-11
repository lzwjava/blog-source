---
audio: false
generated: false
lang: es
layout: post
title: Aprendizaje Automático, Aprendizaje Profundo y GPT
translated: true
type: note
---

1. Machine Learning (ML) es un campo de la informática que permite a los sistemas aprender de los datos y mejorar su rendimiento sin una programación explícita.

2. Deep Learning (DL) es un subcampo del ML que utiliza redes neuronales multicapa para modelar patrones complejos en los datos.

3. Las Neural Networks son modelos computacionales inspirados en el cerebro humano, compuestos por nodos interconectados (neuronas) que procesan información en capas.

4. Training Data es el conjunto de datos etiquetados o no etiquetados utilizado para enseñar a un modelo de machine learning cómo realizar una tarea.

5. Supervised Learning implica entrenar un modelo con datos etiquetados, donde cada ejemplo tiene una entrada y una salida correcta asociada.

6. Unsupervised Learning utiliza datos no etiquetados, permitiendo al modelo descubrir patrones ocultos o agrupaciones sin instrucción explícita.

7. Reinforcement Learning (RL) entrena agentes para tomar decisiones recompensando los comportamientos deseados y penalizando los indeseables.

8. Los Generative Models aprenden a producir nuevos datos similares a sus ejemplos de entrenamiento (por ejemplo, texto, imágenes).

9. Los Discriminative Models se centran en clasificar entradas en categorías o predecir resultados específicos.

10. Transfer Learning permite que un modelo entrenado en una tarea se reutilice o ajuste para una tarea relacionada.

11. GPT (Generative Pre-trained Transformer) es una familia de grandes modelos de lenguaje desarrollados por OpenAI que pueden generar texto similar al humano.

12. ChatGPT es una variante interactiva de GPT, ajustada para conversaciones y tareas de seguimiento de instrucciones.

13. Transformer Architecture se introdujo en el artículo "Attention Is All You Need", revolucionando el procesamiento del lenguaje natural al basarse en mecanismos de atención.

14. Los mecanismos de Self-Attention permiten al modelo ponderar diferentes partes de la secuencia de entrada al construir una representación de salida.

15. Positional Encoding en los Transformers ayuda al modelo a identificar el orden de los tokens en una secuencia.

16. Pre-training es la fase inicial donde un modelo aprende características generales a partir de datos a gran escala antes de ser ajustado para tareas específicas.

17. Fine-tuning es el proceso de tomar un modelo preentrenado y adaptarlo a una tarea más específica utilizando un conjunto de datos más pequeño y específico de la tarea.

18. Language Modeling es la tarea de predecir el siguiente token (palabra o subpalabra) en una secuencia, fundamental para modelos tipo GPT.

19. Zero-shot Learning permite a un modelo manejar tareas sin ejemplos de entrenamiento explícitos, confiando en el conocimiento general aprendido.

20. Few-shot Learning aprovecha un número limitado de ejemplos específicos de la tarea para guiar las predicciones o comportamientos del modelo.

21. RLHF (Reinforcement Learning from Human Feedback) se utiliza para alinear las salidas del modelo con las preferencias y valores humanos.

22. Human Feedback puede incluir clasificaciones o etiquetas que guían la generación del modelo hacia respuestas más deseables.

23. Prompt Engineering es el arte de elaborar consultas o instrucciones de entrada para guiar eficazmente a los grandes modelos de lenguaje.

24. Context Window se refiere a la cantidad máxima de texto que el modelo puede procesar a la vez; los modelos GPT tienen una longitud de contexto limitada.

25. Inference es la etapa donde un modelo entrenado hace predicciones o genera salidas dadas nuevas entradas.

26. Parameter Count es un factor clave en la capacidad del modelo; los modelos más grandes pueden capturar patrones más complejos pero requieren más computación.

27. Las técnicas de Model Compression (por ejemplo, pruning, quantization) reducen el tamaño de un modelo y aceleran la inferencia con una pérdida mínima de precisión.

28. Attention Heads en los Transformers procesan diferentes aspectos de la entrada en paralelo, mejorando el poder de representación.

29. Masked Language Modeling (por ejemplo, en BERT) implica predecir tokens faltantes en una oración, ayudando al modelo a aprender contexto.

30. Causal Language Modeling (por ejemplo, en GPT) implica predecir el siguiente token basándose en todos los tokens anteriores.

31. Encoder-Decoder Architecture (por ejemplo, T5) utiliza una red para codificar la entrada y otra para decodificarla en una secuencia objetivo.

32. Las Convolutional Neural Networks (CNNs) sobresalen en el procesamiento de datos en forma de cuadrícula (por ejemplo, imágenes) a través de capas convolucionales.

33. Las Recurrent Neural Networks (RNNs) procesan datos secuenciales pasando estados ocultos a lo largo de pasos de tiempo, aunque pueden tener problemas con dependencias a largo plazo.

34. Long Short-Term Memory (LSTM) y GRU son variantes de RNN diseñadas para capturar mejor dependencias de largo alcance.

35. Batch Normalization ayuda a estabilizar el entrenamiento normalizando las salidas de las capas intermedias.

36. Dropout es una técnica de regularización que "desactiva" neuronas aleatoriamente durante el entrenamiento para prevenir el sobreajuste.

37. Los Optimizer Algorithms como Stochastic Gradient Descent (SGD), Adam y RMSProp actualizan los parámetros del modelo basándose en gradientes.

38. Learning Rate es un hiperparámetro que determina cuán drásticamente se actualizan los pesos durante el entrenamiento.

39. Los Hyperparameters (por ejemplo, tamaño del lote, número de capas) son configuraciones elegidas antes del entrenamiento para controlar cómo se desarrolla el aprendizaje.

40. Model Overfitting ocurre cuando un modelo aprende los datos de entrenamiento demasiado bien, fallando en generalizar a nuevos datos.

41. Las Regularization Techniques (por ejemplo, L2 weight decay, dropout) ayudan a reducir el sobreajuste y mejorar la generalización.

42. Validation Set se utiliza para ajustar los hiperparámetros, mientras que el Test Set evalúa el rendimiento final del modelo.

43. Cross-validation divide los datos en múltiples subconjuntos, entrenando y validando sistemáticamente para obtener una estimación de rendimiento más robusta.

44. Los problemas de Gradient Exploding y Vanishing ocurren en redes profundas, haciendo el entrenamiento inestable o ineficaz.

45. Residual Connections (conexiones de salto) en redes como ResNet ayudan a mitigar los gradientes que se desvanecen al crear caminos directos para los datos.

46. Scaling Laws sugieren que aumentar el tamaño del modelo y los datos generalmente conduce a un mejor rendimiento.

47. Compute Efficiency es crítica; entrenar modelos grandes requiere hardware (GPUs, TPUs) y algoritmos optimizados.

48. Ethical Considerations incluyen sesgo, equidad y daño potencial—los modelos de ML deben ser probados y monitoreados cuidadosamente.

49. Data Augmentation expande artificialmente los conjuntos de datos de entrenamiento para mejorar la robustez del modelo (especialmente en tareas de imagen y voz).

50. Data Preprocessing (por ejemplo, tokenization, normalization) es esencial para un entrenamiento efectivo del modelo.

51. Tokenization divide el texto en tokens (palabras o subpalabras), las unidades fundamentales procesadas por los modelos de lenguaje.

52. Vector Embeddings representan tokens o conceptos como vectores numéricos, preservando relaciones semánticas.

53. Positional Embeddings añaden información sobre la posición de cada token para ayudar a un Transformer a entender el orden de la secuencia.

54. Attention Weights revelan cómo un modelo distribuye el enfoque a través de diferentes partes de la entrada.

55. Beam Search es una estrategia de decodificación en modelos de lenguaje que mantiene múltiples candidatos de salida en cada paso para encontrar la mejor secuencia general.

56. Greedy Search elige el token más probable en cada paso, pero puede conducir a salidas finales subóptimas.

57. Temperature en el sampling ajusta la creatividad de la generación de lenguaje: temperatura más alta = más aleatoriedad.

58. Los métodos de sampling Top-k y Top-p (Nucleus) restringen los tokens candidatos a los k más probables o a una probabilidad acumulativa p, equilibrando diversidad y coherencia.

59. Perplexity mide qué tan bien un modelo de probabilidad predice una muestra; una perplexity más baja indica un mejor rendimiento predictivo.

60. Precision y Recall son métricas para tareas de clasificación, centrándose en la corrección y la exhaustividad, respectivamente.

61. F1 Score es la media armónica de la precisión y la exhaustividad, equilibrando ambas métricas en un solo valor.

62. Accuracy es la fracción de predicciones correctas, pero puede ser engañosa en conjuntos de datos desequilibrados.

63. Area Under the ROC Curve (AUC) mide el rendimiento de un clasificador a través de varios umbrales.

64. Confusion Matrix muestra los recuentos de verdaderos positivos, falsos positivos, falsos negativos y verdaderos negativos.

65. Los métodos de Uncertainty Estimation (por ejemplo, Monte Carlo Dropout) evalúan cuán seguro está un modelo en sus predicciones.

66. Active Learning implica consultar nuevos ejemplos de datos sobre los cuales el modelo está menos seguro, mejorando la eficiencia de los datos.

67. Online Learning actualiza el modelo incrementalmente a medida que llegan nuevos datos, en lugar de reentrenar desde cero.

68. Evolutionary Algorithms y Genetic Algorithms optimizan modelos o hiperparámetros utilizando mutación y selección de inspiración biológica.

69. Bayesian Methods incorporan conocimiento previo y actualizan creencias con los datos entrantes, útiles para la cuantificación de la incertidumbre.

70. Ensemble Methods (por ejemplo, Random Forest, Gradient Boosting) combinan múltiples modelos para mejorar el rendimiento y la estabilidad.

71. Bagging (Bootstrap Aggregating) entrena múltiples modelos en diferentes subconjuntos de los datos, luego promedia sus predicciones.

72. Boosting entrena iterativamente nuevos modelos para corregir errores cometidos por modelos previamente entrenados.

73. Gradient Boosted Decision Trees (GBDTs) son potentes para datos estructurados, a menudo superando a las redes neuronales simples.

74. Autoregressive Models predicen el siguiente valor (o token) basándose en salidas anteriores en una secuencia.

75. Autoencoder es una red neuronal diseñada para codificar datos en una representación latente y luego decodificarla de nuevo, aprendiendo representaciones comprimidas de los datos.

76. Variational Autoencoder (VAE) introduce un giro probabilístico para generar nuevos datos que se asemejen al conjunto de entrenamiento.

77. Generative Adversarial Network (GAN) enfrenta a un generador contra un discriminador, produciendo imágenes, texto u otros datos realistas.

78. Self-Supervised Learning aprovecha grandes cantidades de datos no etiquetados creando tareas de entrenamiento artificiales (por ejemplo, predecir partes faltantes).

79. Foundation Models son grandes modelos preentrenados que pueden adaptarse a una amplia gama de tareas posteriores.

80. Multimodal Learning integra datos de múltiples fuentes (por ejemplo, texto, imágenes, audio) para crear representaciones más ricas.

81. Data Labeling es a menudo la parte que más tiempo consume en ML, requiriendo una anotación cuidadosa para garantizar la precisión.

82. Edge Computing lleva la inferencia de ML más cerca de la fuente de datos, reduciendo la latencia y el uso de ancho de banda.

83. Federated Learning entrena modelos a través de dispositivos o servidores descentralizados que mantienen muestras de datos locales, sin intercambiarlas.

84. Privacy-Preserving ML incluye técnicas como differential privacy y homomorphic encryption para proteger datos sensibles.

85. Explainable AI (XAI) tiene como objetivo hacer que las decisiones de modelos complejos sean más interpretables para los humanos.

86. Bias and Fairness en ML necesitan una supervisión cuidadosa, ya que los modelos pueden aprender e amplificar inadvertidamente sesgos sociales.

87. Concept Drift ocurre cuando las propiedades estadísticas de la variable objetivo cambian con el tiempo, impactando el rendimiento del modelo.

88. AB Testing compara dos o más versiones de un modelo para ver cuál funciona mejor en un entorno del mundo real.

89. GPU Acceleration explota la computación paralela en tarjetas gráficas para acelerar drásticamente el entrenamiento de ML.

90. TPUs (Tensor Processing Units) son aceleradores de hardware especializados por Google para cargas de trabajo eficientes de deep learning.

91. Open-Source Frameworks (por ejemplo, TensorFlow, PyTorch) proporcionan bloques de construcción y herramientas para el desarrollo de modelos de ML.

92. Model Serving es la práctica de desplegar modelos entrenados para que puedan manejar predicciones en tiempo real o por lotes.

93. Scalability es crucial para manejar grandes conjuntos de datos o tráfico pesado, requiriendo estrategias de entrenamiento e inferencia distribuidos.

94. MLOps combina el desarrollo de ML con las prácticas de operaciones, centrándose en la reproducibilidad, las pruebas y la integración continua.

95. Version Control para datos y modelos garantiza un seguimiento consistente de experimentos y colaboración.

96. Deployment Strategies (por ejemplo, contenedores, microservicios) organizan cómo se empaquetan y sirven los modelos a escala.

97. Monitoring rastrea el rendimiento del modelo después del despliegue, vigilando degradaciones o anomalías.

98. Retraining y Model Updates mantienen los modelos actualizados a medida que surgen nuevos datos y condiciones cambiantes.

99. Time Complexity (O-notation) mide cómo escala el tiempo de ejecución de un algoritmo con el tamaño de la entrada; O(1) denota tiempo constante.

100. Future of ML promete modelos cada vez más sofisticados y generales, pero debe abordar consideraciones éticas, sociales y ambientales.