---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Probando la Generalización con Elementos No Vistos
translated: true
type: note
---

En la charla de Ilya Sutskever por el Premio Test of Time en NeurIPS 2024 sobre su artículo de 2014 "Sequence to Sequence Learning with Neural Networks" (y trabajos relacionados como su tesis doctoral sobre modelado del lenguaje con RNN), reflexionó sobre los primeros esfuerzos para construir modelos de lenguaje neuronal generalizadores. Un desafío clave era asegurar que los modelos no solo memorizaran los datos de entrenamiento, sino que pudieran manejar entradas novedosas, es decir, evitar el sobreajuste.

La "forma ingenua" específica a la que se refirió para detectar esto implica probar el modelo con **palabras o n-gramas (secuencias de varias palabras) no vistos que no estén presentes en el corpus de entrenamiento (a menudo llamado "base de datos")**.

### ¿Por qué este enfoque?
- **Riesgo de sobreajuste en los primeros modelos de lenguaje**: Líneas de base simples como los modelos de n-gramas (por ejemplo, bigramas o trigramas) a menudo se "sobreajustan" al predecir con fluidez solo si la secuencia exacta apareció múltiples veces en el entrenamiento. Asignan una probabilidad cercana a cero a cualquier cosa novedosa, fallando en generalizar.
- **Prueba de detección ingenua**: Para comprobar una verdadera generalización (no sobreajuste), se entrena con un conjunto de validación/prueba retenido, diseñado con elementos "no vistos" deliberados:
  - Reemplazar frases comunes con otras inventadas pero plausibles (por ejemplo, en su tesis, probar la completación de oraciones con una cita falsa como "(ABC et al., 2003)"—una cadena que el modelo nunca había encontrado debido a su capitalización no natural y nombre de autor).
  - Medir si el modelo asigna probabilidades razonables, genera completaciones coherentes o mantiene bajas puntuaciones de perplejidad/BLEU a pesar de la novedad.
- Si el modelo falla (por ejemplo, alta perplejidad o salida incoherente) en estos elementos no vistos, pero se desempeña excelentemente en los datos de entrenamiento vistos, está sobreajustando (memorizando especificidades en lugar de aprender patrones). Si tiene éxito, está generalizando a través de representaciones aprendidas (por ejemplo, estados LSTM que capturan sintaxis/semántica).

### Ejemplos de su trabajo
- **En el artículo de seq2seq (2014)**: Usaron un vocabulario fijo (80k palabras en francés, 160k en inglés), reemplazando las palabras fuera de vocabulario (OOV) con "UNK". Para detectar problemas de generalización, penalizaron las puntuaciones BLEU por las ocurrencias OOV y graficaron el rendimiento frente al "rango de frecuencia de palabra promedio" (más raro = más parecido a no visto). El LSTM manejó bien las palabras raras/no vistas sin degradación, a diferencia de las líneas de base.
- **En su tesis doctoral (2013, sobre modelado del lenguaje con RNN)**: Para la completación estructurada de oraciones, probaron con cadenas completamente novedosas como "(ABC et al., 2003)" (no vista en el entrenamiento debido a su rareza). La RNN multiplicativa (MRNN) generalizó de manera robusta (por ejemplo, prediciendo correctamente el año/contexto), mientras que los modelos base de n-gramas no podían hacerlo a menos que existieran coincidencias exactas, lo que destaca su sobreajuste.

Esta prueba de "verificar palabras/n-gramas no vistos" fue una heurística temprana y sencilla, anterior a técnicas avanzadas como dropout o curvas de validación. Sutskever señaló en la charla cómo estas ideas impulsaron el escalamiento hacia los LLM modernos, donde la generalización sobre vastos datos no vistos sigue siendo fundamental.

[Sequence to Sequence Learning with Neural Networks (PDF de arXiv)](https://arxiv.org/pdf/1409.3215.pdf)
[Tesis Doctoral de Ilya Sutskever (PDF)](https://www.cs.utoronto.ca/~ilya/pubs/ilya_sutskever_phd_thesis.pdf)
[Video de la Charla de Ilya Sutskever en NeurIPS 2024](https://www.youtube.com/watch?v=YD-9NG1Ke5Y)