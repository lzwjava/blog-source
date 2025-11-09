---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Conceptos Básicos y Comparaciones del Biestable D
translated: true
type: note
---

Respuesta: Flip-flop D

Por qué es la elección correcta
- Función: Un flip-flop D (data o delay) almacena exactamente un bit. En el flanco activo del reloj (creciente o decreciente, según el diseño), toma una muestra de la entrada D y actualiza Q a ese valor. Entre los flancos del reloj, Q mantiene su valor anterior.
- Regla de comportamiento: Q_siguiente = D en el flanco del reloj; de lo contrario, Q permanece sin cambios. Este comportamiento de "muestreo y retención" es exactamente lo que se desea para registros y pipelines.

En qué se diferencia de los otros
- Flip-flop RS: Tiene entradas separadas de Set y Reset y una condición no válida (S=R=1). No es ideal para el almacenamiento general de datos en diseños síncronos.
- Flip-flop JK: Generaliza el RS; J=K=1 provoca un toggle. Es más flexible pero más complejo y raramente se usa para registros de datos estándar.
- Flip-flop T: Hace toggle cuando T=1 en el flanco del reloj, mantiene el valor cuando T=0. Excelente para contadores divide-por-2, no para el almacenamiento de datos arbitrarios.

Detalles clave sobre los flip-flops D
- Disparado por flanco vs. latch: Un flip-flop D es disparado por flanco (se actualiza solo en el flanco del reloj). Un latch D es sensible al nivel (transparente mientras la habilitación está activa). Cuando la gente dice "transfiere directamente la entrada a la salida cuando se registra el reloj", normalmente se refiere a que el flip-flop D captura D en el flanco del reloj.
- Requisitos de temporización: El funcionamiento correcto requiere cumplir con el tiempo de setup (D estable antes del flanco) y el tiempo de hold (D estable después del flanco). Violar estos requisitos puede causar metastabilidad.
- Variantes: A menudo incluyen pines de preset (set) asíncrono y clear (reset) asíncrono para inicializar Q.
- Usos comunes: Construcción de registros de n bits (n flip-flops D en paralelo), etapas de pipeline, registros de estado, registros de desplazamiento (a menudo con un MUX para carga serie/paralelo), sincronizadores (en pares) para cruce de dominios de reloj.

Regla general
- Si necesitas un elemento de almacenamiento que "simplemente almacene el bit que presentas en el reloj", usa un flip-flop D.