---
audio: false
generated: true
lang: es
layout: post
title: La Amarga Lección de Rich Sutton
translated: true
type: note
---

La "lección amarga" de Rich Sutton es una observación que invita a la reflexión sobre la historia de la investigación en Inteligencia Artificial. En esencia, afirma que **los investigadores de IA que intentan incorporar conocimiento similar al humano y características diseñadas a mano en sus sistemas eventualmente llegan a un punto muerto y son superados por enfoques que dependen más de algoritmos de aprendizaje de propósito general, siempre que tengan suficiente capacidad de cálculo.**

La parte "amarga" proviene del hecho de que los investigadores a menudo tienen intuiciones sólidas sobre cómo funciona la inteligencia y qué tipo de conocimiento o arquitectura debería ser beneficiosa. Sin embargo, la historia ha demostrado repetidamente que estas intuiciones a menudo conducen a callejones sin salida en comparación con permitir que los algoritmos aprendan directamente de los datos a través de métodos como la búsqueda y el aprendizaje.

Aquí hay un desglose de los aspectos clave de la lección amarga:

* **El Conocimiento Humano es a menudo un Apoyo a Corto Plazo:** Si bien incorporar conocimiento humano puede conducir a un progreso inicial o a un mejor rendimiento en conjuntos de datos pequeños, a menudo limita la capacidad del sistema para escalar y adaptarse a problemas más complejos o a mayores cantidades de datos. Las características diseñadas a mano se vuelven frágiles y no logran generalizar.
* **Los Métodos de Propósito General Triunfan con la Escala:** Sutton argumenta que los avances más significativos en IA han provenido de métodos de propósito general como la búsqueda (por ejemplo, en juegos) y el aprendizaje (por ejemplo, en el machine learning y el deep learning). Estos métodos, cuando se les proporciona suficiente datos y poder computacional, pueden descubrir sus propias representaciones y estrategias, a menudo superando a las soluciones diseñadas por humanos.
* **La Importancia del Cómputo:** Un tema central es la creciente disponibilidad e importancia del cómputo. A medida que crece el poder de cálculo, la ventaja se desplaza hacia los métodos que pueden aprovechar eficazmente este poder para aprender de vastas cantidades de datos.
* **Ejemplos que Sutton Cita Frecuentemente:**
    * **Juegos (Ajedrez, Go):** Los primeros intentos de construir programas para jugar al ajedrez dependían en gran medida de reglas codificadas manualmente y funciones de evaluación basadas en el conocimiento experto humano. Estos fueron eventualmente superados por sistemas como Deep Blue (que utilizó búsqueda masiva) y AlphaGo (que utilizó deep reinforcement learning), que aprendieron sus estrategias a través del cómputo y los datos.
    * **Reconocimiento de Voz:** Los primeros sistemas de reconocimiento de voz incorporaban mucho conocimiento lingüístico y características diseñadas a mano. Los sistemas modernos basados en deep learning, entrenados con cantidades masivas de datos de audio, han logrado un rendimiento mucho mejor sin codificar explícitamente dicho conocimiento.
    * **Visión por Computadora:** Similar al reconocimiento de voz, la visión por computadora inicial dependía de características diseñadas manualmente como detectores de bordes y descriptores de textura. Los modelos de deep learning, entrenados de extremo a extremo en grandes conjuntos de datos de imágenes, han revolucionado el campo.

**Implicaciones para la Investigación en IA:**

La lección amarga de Sutton sugiere que la investigación en IA debería centrarse más en desarrollar algoritmos de aprendizaje escalables y de propósito general y proporcionarles la mayor cantidad de datos y capacidad de cálculo posible, en lugar de intentar codificar de forma rígida una inteligencia similar a la humana o depender en gran medida de características diseñadas a mano. Es una llamada a confiar en el poder del aprendizaje y en el aumento implacable de los recursos computacionales.

Si bien la lección amarga no descarta por completo el valor de la perspicacia humana en el diseño de los propios algoritmos de aprendizaje, enfatiza que el conocimiento sobre el *dominio del problema* a menudo se aprende mejor directamente de los datos, en lugar de ser programado explícitamente.

En resumen, la lección amarga es un recordatorio de que, si bien la intuición humana puede ser un punto de partida, el éxito a largo plazo de la IA a menudo reside en la capacidad de los métodos de aprendizaje de propósito general para descubrir soluciones a través del cómputo y los datos, incluso si esas soluciones no son inmediatamente intuitivas para los humanos.