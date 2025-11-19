---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Progreso del Entrenamiento y Estimación de Tiempo
translated: true
type: note
---

### Progreso actual
- Acabas de pasar la iteración 2800 (de tu objetivo de 20,000)
- Velocidad estable actual: **≈ 3.91 segundos por iteración**  
  (los registros ocasionales de 19 segundos en los pasos de evaluación son solo cada 500 iteraciones y no afectan mucho el promedio)

### Iteraciones restantes
20,000 − 2,800 = **17,200 iteraciones restantes**

### Tiempo estimado para finalizar

| Tiempo promedio por iter | Tiempo restante | Cuándo finalizará (desde ahora, 19 de Nov 2025) |
|-------------------|----------------|---------------------------------------------|
| 3.91 s (actual)  | **18 horas 35 minutos** | ~ **mañana (20 de Nov) alrededor de 14:30–15:30** (dependiendo de tu zona horaria y la hora exacta de inicio de este registro) |
| Un poco más rápido (3.8 s, común a medida que el MFU aumenta un poco más) | ~ 18 horas         | mañana temprano–media tarde              |
| Un poco más lento (4.0 s) | ~ 19 horas 5 min   | mañana ~16:00                            |

Expectativa realista en una RTX 4070 con esta configuración exacta: **18–19 horas desde ahora**.

### Referencia rápida
- Si comenzaste a registrar esto alrededor del mediodía–primera hora de la tarde hoy → terminará mañana por la mañana–primera hora de la tarde.
- Si lo dejas ejecutándose durante la noche → te despertarás con un modelo muy fuerte de 40M terminado (o casi terminado) mañana.

Tu pérdida está disminuyendo muy bien (la pérdida de validación ya es 3.94 con solo ~1.5B tokens vistos) y sigue cayendo constantemente. ¡Definitivamente vale la pena dejarlo ejecutar las 20k completas — simplemente déjalo funcionando durante la noche y tendrás un modelo excelente para mañana por la tarde