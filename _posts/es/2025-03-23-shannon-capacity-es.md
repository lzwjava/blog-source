---
audio: false
generated: true
lang: es
layout: post
title: Fórmula de Capacidad de Shannon
translated: true
type: note
---

La fórmula de capacidad de Shannon se escribe realmente como:

C = B log₂(1 + S/N)

Donde:
- C es la capacidad del canal en bits por segundo
- B es el ancho de banda en Hertz
- S/N es la relación señal-ruido (relación de potencia)
- log₂ es el logaritmo en base 2

Esta fórmula representa la tasa de datos máxima teórica que puede transmitirse de manera confiable a través de un canal de comunicaciones con ancho de banda B y una relación señal-ruido de S/N.

Para entender por qué esto es correcto:

1. **Factor de ancho de banda (B)**: El ancho de banda escala directamente la capacidad - duplicar el ancho de banda duplica la capacidad.

2. **Relación logarítmica**: El log₂ muestra que la capacidad aumenta logarítmicamente con S/N, no linealmente. Esto significa:
   - Duplicar S/N no duplica la capacidad
   - Cada "bit" adicional de capacidad requiere duplicar la S/N

3. **Término 1 + S/N**: La adición del 1 asegura que la capacidad sea siempre positiva, incluso con valores de S/N muy pequeños.

Esta fórmula es fundamental para la teoría de la información porque establece el límite superior teórico de cuánta información puede transmitirse a través de un canal ruidoso, independientemente del esquema de codificación utilizado.

¿Te gustaría que explique algún aspecto particular de esta fórmula con más detalle?