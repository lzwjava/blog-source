---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Control de la Temperatura en la Generación de Texto con RNN
translated: true
type: note
---

### Comprender la temperatura en el muestreo de RNN

En las redes neuronales recurrentes (RNN) para generación de texto—como las que Andrej Karpathy explora en su famosa publicación sobre modelos de lenguaje a nivel de carácter—la temperatura es un hiperparámetro que ajusta cuán "aleatorio" o "predecible" se siente el texto generado. Se aplica durante el paso de muestreo, donde la RNN predice el siguiente carácter (o token) basándose en los anteriores. Sin control de temperatura, la generación puede ser demasiado rígida (eligiendo siempre el siguiente carácter más probable, lo que lleva a bucles aburridos) o demasiado salvaje (pura aleatoriedad). La temperatura logra un equilibrio al suavizar la distribución de probabilidad del modelo sobre los posibles caracteres siguientes.

#### Matemática Rápida Detrás de Esto
La RNN genera *logits* (puntuaciones brutas, no normalizadas) para cada posible carácter siguiente. Estos se convierten en probabilidades usando la función softmax:

\\[
p_i = \frac{\exp(\text{logit}_i / T)}{\sum_j \exp(\text{logit}_j / T)}
\\]

- \\(T\\) es la temperatura (típicamente entre 0.1 y 2.0).
- Cuando \\(T = 1\\), es el softmax estándar: las probabilidades reflejan la confianza "natural" del modelo.
- Luego, *muestreas* el siguiente carácter de esta distribución (por ejemplo, mediante muestreo multinomial) en lugar de elegir siempre el de mayor probabilidad (decodificación codiciosa).

Este muestreo ocurre de forma iterativa: introduce el carácter elegido nuevamente como entrada, predice el siguiente y repite para generar una secuencia.

#### Temperatura Baja: Repetitiva pero Segura
- **Efecto**: \\(T < 1\\) (por ejemplo, 0.5 o cerca de 0) *acentúa* la distribución. Las predicciones de alta confianza obtienen probabilidades aún más altas, mientras que las bajas se reducen hacia cero.
- **Salida**: El texto se mantiene "seguro" y coherente, pero rápidamente se vuelve repetitivo. El modelo se apega a las rutas más probables, como quedar atrapado en un bucle.
- **Ejemplo de la publicación de Karpathy** (generando ensayos al estilo de Paul Graham): A temperatura muy baja, escupe algo como:
  > “is that they were all the same thing that was a startup is that they were all the same thing that was a startup is that they were all the same thing that was a startup is that they were all the same”

  Es confiado y gramaticalmente sólido, pero carece de creatividad—piensa en ecos infinitos de los datos de entrenamiento.

#### Temperatura Alta: Creativa pero Errática
- **Efecto**: \\(T > 1\\) (por ejemplo, 1.5 o 2.0) *aplanea* la distribución. Las probabilidades se vuelven más uniformes, dando a los menos probables (caracteres menos probables) una mejor oportunidad.
- **Salida**: Texto más diverso e inventivo, pero se desvía hacia sinsentidos, errores ortográficos o tangentes salvajes. El modelo explora caminos raros, lo que puede generar originalidad pero a costa de coherencia.
- **Ejemplo de Karpathy**: Temperaturas más altas producen ensayos variados con frases frescas, pero "a costa de más errores (por ejemplo, errores ortográficos, etc.)". Es como si la RNN estuviera haciendo una lluvia de ideas libremente—divertido para poesía o ciencia ficción, arriesgado para escritura factual.

#### Por Qué Importa en las RNN
Las RNN (o LSTMs en la configuración de Karpathy) son autorregresivas: cada predicción se construye sobre la última, por lo que los pequeños sesgos en el muestreo se acumulan en secuencias largas. La temperatura te permite ajustar la exploración vs. la explotación:
- Usa \\(T\\) baja para texto confiable y acorde a la marca (por ejemplo, descripciones de productos).
- Auméntala para lluvia de ideas o generación artística (por ejemplo, historias surrealistas).
- Experimenta en código: el repositorio de RNN vanilla de Karpathy incluye un control deslizante de temperatura—pruébalo en muestras de Shakespeare para ver el cambio de sonetos sosos a versos caóticos.

En esencia, la temperatura no "aprende" nada nuevo; solo está ajustando el dial de creatividad de la RNN durante la inferencia. Baja la mantiene tranquila y predecible; alta libera el caos.

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)