---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ganancia de Corriente del Transistor de Unión Bipolar
translated: true
type: note
---

### Fundamentos de los Transistores de Unión Bipolar (BJT)

Para entender la ganancia de corriente \\( \beta \\) en este problema de transistor, comencemos por los fundamentos. Un **Transistor de Unión Bipolar (BJT)** es un dispositivo semiconductor de tres terminales utilizado para amplificación y conmutación en circuitos electrónicos. Existen dos tipos principales: NPN (el más común) y PNP, pero los principios son similares. Los terminales son:

- **Emisor (E)**: Libera portadores de carga en el circuito.
- **Base (B)**: Una capa delgada que controla el flujo de portadores.
- **Colector (C)**: Recoge la mayoría de los portadores.

En un BJT NPN, la corriente fluye del colector al emisor cuando la unión base-emisor está polarizada en directa (voltaje positivo en la base respecto al emisor) y la unión base-colector está polarizada en inversa (voltaje negativo en la base respecto al colector). Esta configuración define la **región activa** de operación, donde el transistor actúa como un amplificador de corriente.

#### Regiones Clave de Operación
Los BJT tienen tres regiones principales de operación:
1. **Región de Corte**: Ambas uniones están polarizadas en inversa. No fluye una corriente significativa (\\( I_B \approx 0 \\), \\( I_C \approx 0 \\)). El transistor está "apagado".
2. **Región Activa** (o Activa-Directa): Base-emisor polarizada en directa, base-colector polarizada en inversa. Aquí, una pequeña corriente de base \\( I_B \\) controla una corriente de colector \\( I_C \\) mucho mayor. Este es el modo de amplificación.
3. **Región de Saturación**: Ambas uniones polarizadas en directa. Fluye la corriente máxima; el transistor está "encendido" como un interruptor cerrado, pero no hay amplificación.

El problema especifica que el transistor está en la **región activa**, por lo que estamos tratando con el comportamiento de amplificación.

#### Corrientes en un BJT
En la región activa:
- **Corriente de Base (\\( I_B \\))**: Pequeña corriente inyectada en la base, principalmente para proporcionar portadores minoritarios.
- **Corriente de Colector (\\( I_C \\))**: Corriente mucho mayor que fluye del colector al emisor, proporcional a \\( I_B \\).
- **Corriente de Emisor (\\( I_E \\))**: Corriente total que sale del emisor, donde \\( I_E = I_B + I_C \\) (por la Ley de Corrientes de Kirchhoff).

La relación es aproximadamente lineal: \\( I_C \approx \beta I_B \\), donde \\( \beta \\) (beta) es la **ganancia de corriente en CC** o **factor de amplificación de corriente**. Es una relación adimensional, típicamente de 50–300 para transistores discretos, dependiendo del dispositivo.

- \\( \beta \\) no es perfectamente constante—varía ligeramente con la temperatura, el voltaje y los niveles de corriente—pero en análisis básicos, asumimos que es constante en la región activa.
- La corriente de colector también tiene un pequeño componente de fuga (\\( I_{CBO} \\)), pero es despreciable: \\( I_C = \beta I_B + (1 + \beta) I_{CBO} \approx \beta I_B \\).

#### Ganancia de Corriente en CC vs. Ganancia de Pequeña Señal (Incremental)
- **\\( \beta \\) en CC**: Se calcula en un punto de operación específico usando corrientes instantáneas: \\( \beta = \frac{I_C}{I_B} \\).
- **\\( \beta \\) de Pequeña Señal (o \\( h_{fe} \\))**: Para cambios dinámicos (por ejemplo, señales de CA), es la relación de pequeños cambios: \\( \beta \approx \frac{\Delta I_C}{\Delta I_B} \\). Esto es útil cuando el transistor está polarizado en un punto y aplicamos una pequeña variación, ya que \\( \beta \\) se asume constante en ese rango pequeño.

En problemas como este, donde las corrientes "cambian de" un valor a otro, el enfoque incremental a menudo da el \\( \beta \\) "aproximado" si el cambio es pequeño en relación con el punto de operación.

### Aplicando Esto al Problema
El escenario: Transistor en región activa. La corriente de base aumenta de \\( I_{B1} = 12 \, \mu\text{A} \\) a \\( I_{B2} = 22 \, \mu\text{A} \\). La corriente de colector cambia de \\( I_{C1} = 1 \, \text{mA} \\) a \\( I_{C2} = 2 \, \text{mA} \\).

Primero, convertir las unidades para consistencia (1 mA = 1000 μA):
- \\( I_{B1} = 0.012 \, \text{mA} \\), \\( I_{B2} = 0.022 \, \text{mA} \\).
- \\( \Delta I_B = I_{B2} - I_{B1} = 0.022 - 0.012 = 0.010 \, \text{mA} \\) (o 10 μA).
- \\( \Delta I_C = I_{C2} - I_{C1} = 2 - 1 = 1 \, \text{mA} \\).

#### \\( \beta \\) en CC en Cada Punto
- En el punto inicial: \\( \beta_1 = \frac{I_{C1}}{I_{B1}} = \frac{1}{0.012} \approx 83.33 \\).
- En el punto final: \\( \beta_2 = \frac{I_{C2}}{I_{B2}} = \frac{2}{0.022} \approx 90.91 \\).

Estos valores coinciden estrechamente con las opciones A (83) y B (91), pero \\( \beta \\) no es constante aquí—aumentó ligeramente, lo que puede suceder en transistores reales debido a factores como el efecto Early (modulación del ancho de la base). Sin embargo, el problema pregunta por "su ganancia de corriente \\( \beta \\) es aproximadamente", lo que implica un valor único, y los cambios son significativos (83% de aumento en \\( I_B \\), 100% en \\( I_C \\)), por lo que los puntos de CC por sí solos no capturan un \\( \beta \\) "constante".

#### \\( \beta \\) Incremental (de Pequeña Señal)
Asumiendo que \\( \beta \\) es aproximadamente constante en el rango de operación, la mejor estimación es la pendiente de la línea de \\( I_C \\) vs. \\( I_B \\):
\\[
\beta \approx \frac{\Delta I_C}{\Delta I_B} = \frac{1 \, \text{mA}}{0.010 \, \text{mA}} = 100.
\\]

Esto coincide exactamente con la opción C. ¿Por qué usar esto?
- En el modelo de la región activa, \\( I_C = \beta I_B \\) es lineal, por lo que la relación de cambios refleja la ganancia directamente.
- El promedio de los puntos de CC es \\( \frac{83.33 + 90.91}{2} \approx 87 \\), pero esa no es una opción e ignora el supuesto de linealidad.
- La opción D (183) podría provenir de un cálculo erróneo como \\( \frac{2}{0.011} \\) o duplicar algo, pero es incorrecta.

Gráficamente, si se grafica \\( I_C \\) vs. \\( I_B \\):
- Puntos: (0.012, 1) y (0.022, 2).
- Pendiente = subida/corrida = \\( \frac{1}{0.01} = 100 \\).

Esta \\( \beta \\) incremental es la que los diseñadores de circuitos suelen usar para el análisis del punto de polarización o modelos de pequeña señal.

### Por Qué Esto es Importante en la Práctica
En amplificadores, se polariza el transistor en la región activa (por ejemplo, en corrientes de punto medio) para que las variaciones de pequeña señal se mantengan lineales alrededor de \\( \beta \\). Aquí, el cambio es grande, pero el problema prueba la comprensión de la relación proporcional.

Si \\( \beta \\) variara más drásticamente, necesitaríamos una simulación SPICE completa, pero para preguntas de opción múltiple, 100 es la respuesta prevista.

Para lectura más profunda:  
[All About Circuits: BJT Fundamentals](https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistor-bjt/)  
[Electronics Tutorials: Transistor as an Amplifier](https://www.electronics-tutorials.ws/amplifier/transistor-amplifier.html)