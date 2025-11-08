---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Principio de Posicionamiento GPS Explicado Sencillamente
translated: true
type: note
---

### Tarea de Divulgación Científica de Hoy Número Dos: Un Video Explicando el Principio del Sistema de Posicionamiento GPS

Les recomiendo a todos ver este video que explica los principios del sistema de posicionamiento GPS. Sin embargo, había un pequeño error en una de las imágenes, así que hice una corrección rápida.

El principio es en realidad bastante sencillo—solo requiere conocimientos básicos de geometría sólida para entenderlo. Se puede resumir en una frase: "La intersección de cuatro esferas es un único punto". Ahora, voy a desglosar exactamente cómo se aplica esto:

1.  Los satélites GPS (o las estaciones base terrestres) transmiten información que incluye sus "coordenadas" en el momento de la transmisión y una "marca de tiempo". (Figura 1)

    *   Cuando el receptor GPS capta esta señal, puede calcular la distancia \\( r_1 \\) desde ese satélite hasta sí mismo usando la marca de tiempo: \\( r_1 = \\) velocidad de la luz × tiempo de transmisión.

    *   Todas las posiciones a una distancia \\( r_1 \\) de este satélite se encuentran en una esfera con radio \\( r_1 \\). Para simplificar, la llamaré la "esfera equidistante". La geometría nos dice que la intersección de dos esferas es un círculo, por lo que la intersección de esta "esfera equidistante" con la Tierra es un círculo (Figura 2a—requiere un poco de visualización 3D). Claramente, con solo la señal de un satélite, no podemos determinar nuestra ubicación exacta; solo sabemos que estamos en algún lugar de ese círculo.

2.  Si recibimos señales de un segundo satélite con su posición y distancia, podemos dibujar otra esfera. La intersección de estas dos esferas equidistantes con la Tierra—tres esferas en total—da las posibles posiciones donde podríamos estar. Esta intersección muy probablemente sean solo dos puntos, pero no sabemos cuál es el correcto. (Figura 2b)

3.  Con la posición y distancia de un tercer satélite, su esfera equidistante muy probablemente pasará por uno de esos dos puntos pero no por el otro. Esto determina las coordenadas del receptor en el suelo. (Figura 2c)

4.  Si obtenemos una señal de un cuarto satélite, su esfera equidistante también pasará por ese mismo punto. Entonces, si solo necesitamos coordenadas en tierra, el cuarto satélite no es estrictamente necesario. (Figura 2d)

Todo esto realmente se puede reducir a una idea clave: la intersección de cuatro esferas es un único punto. Las tres esferas equidistantes de los satélites, más la Tierra misma (como la cuarta esfera), se intersecan en un punto único—solo una ubicación.

Nótese que estas señales no tienen que venir de satélites. Las estaciones base terrestres con coordenadas conocidas pueden transmitir el mismo tipo de señal (coordenadas + marca de tiempo), y el receptor puede calcular su posición exactamente de la misma manera—es simplemente un cálculo de intersección geométrica.

**Ejercicio 1:** En el segundo paso, debido a que normalmente hay una diferencia de tiempo entre el reloj del receptor y el reloj del satélite GPS, no se puede obtener el "tiempo de transmisión" con solo una señal. Pero si el mismo satélite envía dos señales, se puede eliminar este desfase y calcular el tiempo de transmisión. Intenta descubrir por qué por tu cuenta.

**Ejercicio 2a:** En el cuarto paso, dije que la intersección de las dos esferas equidistantes y la Tierra "muy probablemente" son solo dos puntos. ¿En qué casos especiales esta intersección sería más de dos puntos? ¿Qué otra forma podría tomar?

**Ejercicio 2b:** En el quinto paso, dije que la esfera equidistante del tercer satélite "muy probablemente" pasa por uno de los dos puntos pero no por el otro. ¿En qué casos especiales su esfera equidistante pasaría por ambos puntos a la vez?

**Ejercicio 3:** Con señales de cuatro satélites, no solo se pueden calcular las coordenadas, sino también la altitud (elevación). Entonces, ¿por qué el cuarto satélite sigue siendo útil?

**Ejercicio 4:** Si dependemos completamente de estaciones base terrestres, podemos calcular coordenadas usando señales de tres estaciones. Con la señal de una cuarta estación base, ¿podemos calcular la altitud? Si es así, ¿qué condición deben satisfacer las posiciones de estas cuatro estaciones base?

**Ejercicio 5:** Si la configuración del Ejercicio 4 es factible, diseña un "sistema GPS basado en tierra" que no use satélites en absoluto pero replique completamente la funcionalidad de un sistema GPS satelital. Debe satisfacer las necesidades de la navegación diaria para vehículos y peatones, aviación, viajes marítimos, senderismo, off-roading y más. El sistema debe ser rentable, con gastos no superiores a los de un sistema basado en satélites.

[Publicación Original: Principios del GPS](https://yinwang1.substack.com/p/gps)