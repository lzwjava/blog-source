---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Examen de Fundamentos de Tecnología Electrónica
translated: true
type: note
---

### Preguntas de Examen Muestra: Fundamentos de Tecnología Electrónica (III)
*(Basado en la edición de Wen Xidong, Examen Nacional de Autoeducación Superior)*

Este conjunto está extraído de exámenes pasados de 自考 para el curso 电子技术基础（三）. Los temas incluyen análisis de circuitos de CA, semiconductores, transistores y amplificadores operacionales. Las preguntas están en inglés (traducidas de los originales en chino) para mayor claridad. Cada pregunta de opción única vale 1 punto; la pregunta de análisis vale 5 puntos.

#### Sección I: Preguntas de Opción Única
Selecciona la opción correcta (A, B, C o D) para cada una.

1. **Entre las siguientes descripciones de las características de una fuente de voltaje ideal, la correcta es:**
   A. La resistencia interna de la fuente de señal de voltaje ideal tiende a infinito.
   B. Las fuentes de voltaje ideales se pueden conectar en paralelo en cualquier momento.
   C. El voltaje de salida de la fuente de voltaje ideal está relacionado con la carga.
   D. La corriente que fluye a través de la fuente de voltaje ideal está relacionada con la carga.

2. **Dada la corriente fasorial que fluye a través de la reactancia inductiva \\( \omega L = 2 \, \Omega \\) es \\( I = 10 \angle 30^\circ \\) mA, entonces el voltaje fasorial a través de ella es:**
   A. \\( U = 20 \angle 0^\circ \\) mV
   B. \\( U = 20 \angle 120^\circ \\) mV
   C. \\( U = 20 \angle 30^\circ \\) mV
   D. \\( U = 20 \angle -60^\circ \\) mV

3. **Suponiendo que el capacitor \\( C = 1 \, \mu \mathrm{F} \\), el voltaje a través del capacitor es \\( \cos(100 \pi t) \\) mV, entonces la corriente que fluye a través del capacitor es:**
   A. \\( i_c(t) = -0.1 \times 10^{-6} \pi \sin(100 \pi t) \\) A
   B. \\( i_c(t) = 0.1 \times 10^{-6} \pi \sin(100 \pi t) \\) A
   C. \\( i_c(t) = -0.1 \times 10^{-6} \sin(100 \pi t) \\) A
   D. \\( i_c(t) = 0.1 \times 10^{-6} \sin(100 \pi t) \\) A

4. **El portador mayoritario en un semiconductor tipo P es:**
   A. Electrones libres
   B. Huecos
   C. Átomos de impureza trivalente
   D. Iones de impureza trivalente

5. **Dados los potenciales de los tres electrodos de un cierto triodo de cristal como se muestra en la figura (voltajes emisor-base-colector que indican características de un transistor de silicio NPN), el tipo de este transistor es:**
   *(Descripción de la figura: Emisor a 0V, base a 0.7V, colector a 5V – típica unión de silicio NPN en polarización directa.)*
   A. Tubo de germanio tipo PNP
   B. Tubo de germanio tipo NPN
   C. Tubo de silicio tipo PNP
   D. Tubo de silicio tipo NPN

#### Sección II: Pregunta de Análisis
**Pregunta 31 (5 puntos):** En el circuito mostrado en la Figura 31 (una configuración básica de amplificador operacional inversor con resistencia de entrada \\( R_i = 10 \, \mathrm{k} \Omega \\), resistencia de retroalimentación \\( R_f = 20 \, \mathrm{k} \Omega \\), voltaje de entrada \\( U_i = 10 \\) V), calcula el voltaje de salida \\( U_o \\).

*(Descripción de la figura: Amplificador operacional inversor estándar; entrada no inversora conectada a tierra. Usa la fórmula de ganancia: \\( U_o = - \frac{R_f}{R_i} \times U_i \\).)*

**Sugerencia de solución:** Aplica el principio de tierra virtual (la entrada inversora está a un potencial de 0V). La caída de voltaje a través de \\( R_i \\) es igual a \\( U_i \\), por lo tanto la corriente \\( I = \frac{U_i}{R_i} \\). Entonces \\( U_o = -I \times R_f \\). Resultado esperado: \\( U_o = -20 \\) V.

Estas se alinean con capítulos como fasores de CA (Cap. 2), semiconductores (Cap. 3–4) y amplificadores operacionales (Cap. 5). Consejo de práctica: Repasa aritmética fasorial, transporte de portadores y reglas de amplificadores operacionales ideales.

**Referencias:**
- [04730 电子技术基础(三) 2010.07 自考 历年真题 试题](https://wenku.baidu.com/view/a2a96333b90d6c85ec3ac6bf.html)
- [自考电子技术基础（三）04730真题及答案免费分享](http://www.s9w.cn/zkzt408/)