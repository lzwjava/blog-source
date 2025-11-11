---
audio: false
generated: true
lang: es
layout: post
title: Función Softmax en Aprendizaje Profundo
translated: true
type: note
---

### ¿Qué es Softmax?

La **función Softmax** es una función matemática utilizada en el aprendizaje automático, particularmente en el aprendizaje profundo, para convertir un vector de puntuaciones brutas (a menudo llamadas logits) en una distribución de probabilidad. Garantiza que los valores de salida sean positivos y sumen 1, lo que los hace interpretables como probabilidades.

La función Softmax se define de la siguiente manera para un vector \\( z = [z_1, z_2, \dots, z_n] \\):

\\[
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}}
\\]

Donde:
- \\( z_i \\): La puntuación de entrada (logit) para la clase \\( i \\)-ésima.
- \\( e^{z_i} \\): La exponencial de la puntuación de entrada, que garantiza positividad.
- \\( \sum_{j=1}^n e^{z_j} \\): La suma de exponenciales de todas las puntuaciones de entrada, utilizada para la normalización.
- La salida \\( \text{Softmax}(z_i) \\) representa la probabilidad de la clase \\( i \\)-ésima.

Propiedades clave:
- **Rango de salida**: Cada valor de salida está entre 0 y 1.
- **Suma a 1**: La suma de todos los valores de salida es igual a 1, lo que la convierte en una distribución de probabilidad válida.
- **Amplifica diferencias**: La función exponencial en Softmax enfatiza los valores de entrada más grandes, haciendo que las probabilidades de salida sean más decisivas para logits más grandes.

### Cómo se aplica Softmax en el Aprendizaje Profundo

La función Softmax se utiliza comúnmente en la **capa de salida** de las redes neuronales para tareas de **clasificación multi-clase**. Así es como se aplica:

1. **Contexto en Redes Neuronales**:
   - En una red neuronal, la capa final a menudo produce puntuaciones brutas (logits) para cada clase. Por ejemplo, en un problema de clasificación con 3 clases (p. ej., gato, perro, pájaro), la red podría generar logits como \\([2.0, 1.0, 0.5]\\).
   - Estos logits no son directamente interpretables como probabilidades porque pueden ser negativos, no estar acotados y no sumar 1.

2. **Función de Softmax**:
   - La función Softmax transforma estos logits en probabilidades. Para el ejemplo anterior:
     \\[
     \text{Softmax}([2.0, 1.0, 0.5]) = \left[ \frac{e^{2.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{1.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{0.5}}{e^{2.0} + e^{1.0} + e^{0.5}} \right]
     \\]
     Esto podría resultar en probabilidades como \\([0.665, 0.245, 0.090]\\), indicando un 66.5% de probabilidad para la clase 1 (gato), 24.5% para la clase 2 (perro) y 9.0% para la clase 3 (pájaro).

3. **Aplicaciones**:
   - **Clasificación multi-clase**: Softmax se utiliza en tareas como clasificación de imágenes (p. ej., identificar objetos en imágenes), procesamiento del lenguaje natural (p. ej., análisis de sentimientos con múltiples categorías) o cualquier problema donde una entrada deba asignarse a una de varias clases.
   - **Cálculo de pérdida**: Softmax se suele emparejar con la función de **pérdida de entropía cruzada**, que mide la diferencia entre la distribución de probabilidad predicha y la distribución verdadera (etiquetas codificadas en one-hot). Esta pérdida guía el entrenamiento de la red neuronal.
   - **Toma de decisiones**: Las probabilidades de salida pueden usarse para seleccionar la clase más probable (p. ej., tomando la clase con la probabilidad más alta).

4. **Ejemplos en Aprendizaje Profundo**:
   - **Clasificación de Imágenes**: En una red neuronal convolucional (CNN) como ResNet, la capa totalmente conectada final produce logits para cada clase (p. ej., 1000 clases en ImageNet). Softmax los convierte en probabilidades para predecir el objeto en una imagen.
   - **Procesamiento del Lenguaje Natural**: En modelos como los transformers (p. ej., BERT), Softmax se utiliza en la capa de salida para tareas como clasificación de texto o predicción de la siguiente palabra, donde se necesitan probabilidades sobre un vocabulario o un conjunto de clases.
   - **Aprendizaje por Refuerzo**: Softmax puede usarse para convertir puntuaciones de acciones en probabilidades para seleccionar acciones en un método basado en políticas.

5. **Implementación en Frameworks**:
   - En frameworks como **PyTorch** o **TensorFlow**, Softmax a menudo se implementa como una función integrada:
     - PyTorch: `torch.nn.Softmax(dim=1)` o `torch.nn.functional.softmax()`
     - TensorFlow: `tf.nn.softmax()`
   - Muchos frameworks combinan Softmax con la pérdida de entropía cruzada en una sola operación (p. ej., `torch.nn.CrossEntropyLoss` en PyTorch) para lograr estabilidad numérica, ya que calcular Softmax por separado puede provocar problemas como desbordamiento con logits grandes.

### Consideraciones Prácticas
- **Estabilidad Numérica**: El cálculo directo de Softmax puede provocar desbordamiento debido a la función exponencial. Un truco común es restar el valor del logit máximo a todos los logits (\\( z_i - \max(z) \\)) antes de aplicar Softmax, lo que no cambia la salida pero evita exponenciales grandes.
- **Softmax vs. Sigmoide**: Para la **clasificación binaria**, la función sigmoide se usa a menudo en lugar de Softmax, ya que maneja dos clases de manera más eficiente. Softmax generaliza la sigmoide a múltiples clases.
- **Limitaciones**:
  - Softmax asume exclusividad mutua (una clase correcta). Para la clasificación multi-etiqueta (donde múltiples clases pueden ser verdaderas), se prefiere la sigmoide.
  - Softmax puede ser excesivamente confiado en las predicciones debido a la función exponencial, que puede amplificar pequeñas diferencias en los logits.

### Ejemplo de Cálculo
Supongamos que una red neuronal genera logits \\([1.5, 0.8, -0.2]\\) para un problema de 3 clases:
1. Calcular exponenciales: \\( e^{1.5} \approx 4.482, e^{0.8} \approx 2.225, e^{-0.2} \approx 0.819 \\).
2. Sumar las exponenciales: \\( 4.482 + 2.225 + 0.819 = 7.526 \\).
3. Calcular probabilidades:
   - Clase 1: \\( \frac{4.482}{7.526} \approx 0.596 \\)
   - Clase 2: \\( \frac{2.225}{7.526} \approx 0.296 \\)
   - Clase 3: \\( \frac{0.819}{7.526} \approx 0.109 \\)
4. Salida: \\([0.596, 0.296, 0.109]\\), una distribución de probabilidad válida.

### Visualización de Softmax
Para ilustrar cómo Softmax transforma los logits en probabilidades, considere el siguiente gráfico que muestra los logits y sus correspondientes probabilidades de Softmax:

```chartjs
{
  "type": "bar",
  "data": {
    "labels": ["Class 1", "Class 2", "Class 3"],
    "datasets": [
      {
        "label": "Logits",
        "data": [1.5, 0.8, -0.2],
        "backgroundColor": "rgba(75, 192, 192, 0.6)",
        "borderColor": "rgba(75, 192, 192, 1)",
        "borderWidth": 1
      },
      {
        "label": "Softmax Probabilities",
        "data": [0.596, 0.296, 0.109],
        "backgroundColor": "rgba(255, 99, 132, 0.6)",
        "borderColor": "rgba(255, 99, 132, 1)",
        "borderWidth": 1
      }
    ]
  },
  "options": {
    "scales": {
      "y": {
        "beginAtZero": true,
        "title": {
          "display": true,
          "text": "Valor"
        }
      },
      "x": {
        "title": {
          "display": true,
          "text": "Clases"
        }
      }
    },
    "plugins": {
      "legend": {
        "display": true
      },
      "title": {
        "display": true,
        "text": "Logits vs. Probabilidades de Softmax"
      }
    }
  }
}
```

Este gráfico compara los logits brutos con las probabilidades después de aplicar Softmax, destacando cómo Softmax normaliza los valores en una distribución de probabilidad.

### Resumen
La función Softmax es una piedra angular de la clasificación multi-clase en el aprendizaje profundo, transformando puntuaciones brutas en una distribución de probabilidad. Se utiliza ampliamente en las capas de salida de las redes neuronales para tareas como clasificación de imágenes y texto, permitiendo que los modelos asignen probabilidades a múltiples clases y facilitando el entrenamiento con funciones de pérdida como la entropía cruzada. Su naturaleza exponencial la hace sensible a las diferencias en los logits, y una implementación cuidadosa garantiza la estabilidad numérica.