---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Los UUID Garantizan la Singularidad Global Sin Coordinación
translated: true
type: note
---

Los UUID pueden cumplir el propósito de identificación globalmente única sin una autoridad central porque están diseñados con un espacio de direcciones enorme: 128 bits, lo que proporciona aproximadamente 3.4 × 10^38 valores posibles. Esto es enormemente mayor que la cantidad de UUIDs que se generarán en escenarios prácticos en todos los sistemas del mundo. Para los UUIDs de versión 4 (los aleatorios, como el que compartiste), 122 de esos bits se llenan con datos aleatorios de alta calidad, lo que hace que los duplicados sean extremadamente improbables.

En cuanto a las colisiones: Sí, en teoría es posible que dos UUIDs sean idénticos, pero la probabilidad es tan baja que es efectivamente cero para el uso en el mundo real. Esto sigue la "paradoja del cumpleaños" en probabilidad: las colisiones se vuelven más probables a medida que crece el número de elementos, pero incluso así:

- La probabilidad de que dos UUIDs de versión 4 aleatorios colisionen es de aproximadamente 1 en 2.71 × 10^18.
- Necesitarías generar aproximadamente 4.8 × 10^18 UUIDs (eso es que cada persona en la Tierra posea unos 600 millones cada una) para tener un 50% de probabilidad de que haya *solo un* duplicado.
- Para ponerlo en contexto, incluso generando 1 billón (10^12) de UUIDs da un riesgo de colisión de alrededor de 1 en mil millones o menos.

Las diferentes versiones de UUID agregan salvaguardas: la versión 1 usa marcas de tiempo y direcciones MAC, la versión 5 aplica hash a nombres con namespaces, etc. Pero la aleatoriedad de la versión 4 por sí sola garantiza la unicidad en sistemas distribuidos, bases de datos o aplicaciones sin coordinación.

[¿Cuáles son las probabilidades?](https://jhall.io/archive/2021/05/19/what-are-the-odds/)  
[Identificador único universal - Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)  
[¿Qué tan grande es la probabilidad de una colisión con Java UUID.randomUUID?](https://stackoverflow.com/questions/24876188/how-big-is-the-chance-to-get-a-java-uuid-randomuuid-collision)