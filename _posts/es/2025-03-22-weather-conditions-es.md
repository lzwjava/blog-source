---
audio: false
generated: true
lang: es
layout: post
title: Condiciones Climáticas Completas en Accesos Directos de iOS
translated: true
type: note
---

Aquí tienes un desglose completo de todos los rangos de valores de condiciones meteorológicas disponibles en Accesos Directos de iOS:

## Índice UV
- **Rango**: 0-11+
- **Escala**:
  - 0-2: Bajo
  - 3-5: Moderado
  - 6-7: Alto
  - 8-10: Muy alto
  - 11+: Extremo

## Temperatura
- **Rango**: Varía según la ubicación
- **Unidades**: Celsius (°C) o Fahrenheit (°F)
- **Rango típico**: -50°C a 50°C (-58°F a 122°F)

## Sensación Térmica
- **Rango**: Similar a la temperatura real
- **Unidades**: Celsius (°C) o Fahrenheit (°F)
- **Factores**: Combina temperatura, humedad, sensación térmica del viento

## Humedad
- **Rango**: 0-100%

## Visibilidad
- **Rango**: 0-10+ millas o 0-16+ kilómetros

## Velocidad del Viento
- **Rango**: 0-100+ mph o 0-160+ kph
- **Unidades**: mph, kph, m/s o nudos

## Dirección del Viento
- **Rango**: 0-359 grados
- **Direcciones cardinales**: N (0°), E (90°), S (180°), O (270°)

## Índice de Calidad del Aire (AQI)
- **Rango**: 0-500+
- **Escala**: Buena (0-50) a Peligrosa (301+)

## Probabilidad de Precipitación
- **Rango**: 0-100%
- **Interpretación**: Probabilidad de precipitación en el período de pronóstico

## Cantidad de Precipitación
- **Rango**: 0 a 100+ mm o pulgadas
- **Unidades**: mm o pulgadas
- **Período de tiempo**: Generalmente medido por hora o por día

## Intensidad de Precipitación
- **Rango**:
  - Nula: 0 mm/h
  - Ligera: 0.1-2.5 mm/h
  - Moderada: 2.5-10 mm/h
  - Fuerte: 10-50 mm/h
  - Violenta: 50+ mm/h

## Presión
- **Rango**: Típicamente 950-1050 hPa/mb
- **Unidades**: hPa, mb o inHg
- **Presión estándar**: 1013.25 hPa al nivel del mar

## Punto de Rocío
- **Rango**: Similar al rango de temperatura
- **Unidades**: Celsius (°C) o Fahrenheit (°F)
- **Niveles de confort**:
  - <55°F (<13°C): Seco y cómodo
  - 55-65°F (13-18°C): Cómodo
  - >65°F (>18°C): Cada vez más húmedo e incómodo

## Cobertura de Nubes
- **Rango**: 0-100%

## Condición Meteorológica
- **Valores**: Descripciones de texto (Despejado, Parcialmente Nublado, Lluvia, Nieve, etc.)

## Horarios de Amanecer/Atardecer
- **Rango**: Valores de hora en la zona horaria local

## Fase Lunar
- **Rango**: 0-1 (0 = Luna Nueva, 0.5 = Luna Llena, 1 = Luna Nueva)
- **Valores de texto**: Luna Nueva, Creciente, Cuarto Creciente, etc.

## Conteo de Polen
- **Rango**: Generalmente 0-12
- **Escala**: Bajo, Moderado, Alto, Muy Alto

## Índice de Calor
- **Rango**: Rango de temperatura, pero solo se calcula cuando la temperatura está por encima de 80°F (27°C)
- **Unidades**: Igual que la temperatura

## Cantidad de Nieve
- **Rango**: 0 a 100+ cm o pulgadas
- **Unidades**: cm o pulgadas
- **Período de tiempo**: Generalmente por hora o por día

Estos valores de condiciones meteorológicas se pueden usar en declaraciones condicionales dentro de Accesos Directos para crear automatizaciones sofisticadas basadas en el clima y adaptadas a condiciones específicas.