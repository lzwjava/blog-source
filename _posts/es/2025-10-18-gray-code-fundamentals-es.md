---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Fundamentos y Aplicaciones del Código Gray
translated: true
type: note
---

### ¿Qué es el Código Gray?

El código Gray (también conocido como código binario reflejado) es un sistema numérico binario diseñado de modo que **dos valores consecutivos (o adyacentes) difieren en exactamente un bit**. Esta propiedad minimiza los errores durante las transiciones, ya que solo un único bit necesita cambiar al pasar de un número al siguiente. Es particularmente útil en aplicaciones como:
- **Codificadores rotativos** (por ejemplo, en dispositivos mecánicos como perillas o ruedas, donde la posición cambia gradualmente).
- **Detección/corrección de errores** en comunicaciones digitales.
- **Mapas de Karnaugh** en el diseño de lógica digital para simplificar el álgebra booleana.

A diferencia del código binario estándar, donde los números adyacentes pueden diferir en múltiples bits (lo que puede causar "glitches" o errores potenciales), el código Gray garantiza transiciones suaves de un solo bit.

### Cómo funciona el Código Gray
La regla clave es: **Cualesquiera dos códigos sucesivos difieren en solo una posición de bit**.

#### Ejemplo Sencillo: Secuencia de Código Gray de 2 Bits (para números del 0 al 3)
Aquí hay una comparación entre el binario estándar y el código Gray:

| Decimal | Binario Estándar | Código Gray | Diferencia de Bits con el Anterior |
|---------|------------------|-------------|------------------------------------|
| 0       | 00               | 00          | (Punto de inicio)                 |
| 1       | 01               | 01          | 1 bit (bit menos significativo)   |
| 2       | 10               | 11          | 1 bit (bit menos significativo)   |
| 3       | 11               | 10          | 1 bit (bit más significativo)     |

- En el **binario estándar**, la transición del 1 (01) al 2 (10) cambia *dos* bits, lo que podría causar errores.
- En el **código Gray**, cada paso cambia *exactamente un* bit, lo que coincide con tu descripción de "dos códigos continuos solo uno es diferente".

#### Generando el Código Gray
Puedes convertir binario a código Gray usando una simple operación XOR:
- Gray(n) = n XOR (n >> 1) (donde >> es desplazamiento a la derecha por 1 bit).

Por ejemplo:
- Binario 2 (10 en decimal): 10 XOR 01 = 11 (código Gray para 2).
- Para volver atrás: Binario(n) = Gray(n) XOR (Gray(n) >> 1).

Este patrón puede extenderse a cualquier número de bits (por ejemplo, 3-bit, 4-bit, etc.), manteniendo siempre la propiedad de diferencia de un solo bit.

Si tienes un caso de uso específico o quieres ejemplos para más bits, ¡avísame!