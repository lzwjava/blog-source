---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Deriva de Punto Cero en Electrónica
translated: true
type: note
---

### Deriva del Punto Cero: Definición y Explicación

La deriva del punto cero (también llamada deriva de offset o deriva de DC offset) es un error en circuitos electrónicos, sensores o sistemas de medición donde la salida produce un voltaje de offset o un nivel de señal no deseado, incluso cuando la entrada es exactamente cero. Esto resulta en un "offset de salida no deseado con entrada cero", desplazando la línea base desde el punto cero ideal. Es como una báscula que lentamente marca "1 kg" cuando no hay nada sobre ella; la lectura se desvía con el tiempo o debido a las condiciones.

#### Características Principales
- **Manifestación**: La salida no regresa al cero real sin una entrada, causando errores acumulativos en sistemas multi-etapa (ej. amplificadores) donde pequeños offsets se amplifican.
- **Común en**: Amplificadores operacionales (op-amps), amplificadores de instrumentación, termopares, galgas extensométricas y circuitos directamente acoplados (sin condensadores para bloquear la CC).
- **Medición**: A menudo cuantificada en μV/°C (voltios por grado Celsius) para la deriva térmica o ppm/°C para cambios relativos.

#### Causas Primarias
- **Variaciones de Temperatura**: La más común; los parámetros de transistores o resistencias (ej. voltaje base-emisor) cambian con el calor, conduciendo a desplazamientos del punto de polarización.
- **Envejeccimiento de Componentes**: Degradación gradual en semiconductores o componentes pasivos con el tiempo.
- **Fluctuaciones de la Fuente de Alimentación**: Ripple de voltaje inestable que afecta los puntos de polarización.
- **Desajustes de Parámetros**: En amplificadores multi-etapa, ligeras diferencias en las ganancias de los transistores o resistencias amplifican los offsets.

#### Efectos y Mitigación
- **Impacto**: Distorsiona señales de bajo nivel, reduce la precisión en aplicaciones críticas como dispositivos médicos o audio (ej. zumbido o ruido en el "silencio").
- **Soluciones**:
  - Circuitos de auto-zero o de estabilización por chopper para resetear offsets periódicamente.
  - Componentes emparejados o trimpots para calibración.
  - Compensación de temperatura (ej. termistores).
  - Acoplamiento AC para bloquear la CC en aplicaciones que no la requieren.

En amplificadores multi-etapa directamente acoplados (como se discutió previamente), es especialmente problemático porque las señales de CC pasan a través de todas las etapas, magnificando pequeñas derivas.

[Zero Drift Amplifiers Explained](https://www.analog.com/en/resources/analog-dialogue/articles/zero-drift-amplifiers.html)  
[Offset Drift in Op-Amps](https://www.ti.com/lit/an/sboa275/sboa275.pdf)  
[Wikipedia: Offset (electronics)](https://en.wikipedia.org/wiki/Offset_(electronics))