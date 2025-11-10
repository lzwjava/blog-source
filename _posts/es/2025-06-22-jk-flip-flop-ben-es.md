---
audio: false
generated: true
lang: es
layout: post
title: Latch SR y Modificaciones de Flip-Flop por Ben Eater
translated: true
type: note
---

En un video anterior, hablé sobre el *SR Latch*, y te animo a que revises ese video si no estás familiarizado con él. Para resumir, el *SR Latch* tiene dos entradas: **R** (*Reset*) y **S** (*Set*). Cuando la entrada *Reset* se pone en alto, la salida **Q** se pone en bajo (apagado), restableciendo el *latch*. Cuando la entrada *Set* se pone en alto, la salida **Q** se pone en alto (encendido), configurando el *latch*. También hay una salida complementaria, **Q̅** (Q-barra), que siempre es lo opuesto a **Q**, excepto en un caso: cuando ambas entradas **R** y **S** están en alto simultáneamente. En este escenario, tanto **Q** como **Q̅** se ponen en bajo, lo que se considera un estado inválido, ya que no se debe configurar y restablecer el *latch* al mismo tiempo. Si ambas entradas se liberan, el estado del *latch* se vuelve impredecible, ya que depende de qué entrada se libere primero. Generalmente, el *SR Latch* permanecerá enclavado en uno de sus dos estados estables.

En este video, hablaré sobre modificaciones al circuito básico del *SR Latch*. La primera modificación es el **SR Latch con Enable**. Esta versión añade **compuertas AND** a ambas entradas **R** y **S**, controladas por una señal **Enable**. Cuando la señal *Enable* está en alto (1), las compuertas AND dejan pasar las entradas **R** y **S** sin cambios. Por ejemplo, si **Enable** es 1 y **Reset** es 1, la compuerta AND emite un 1; si **Reset** es 0, emite un 0. Sin embargo, si la señal **Enable** está en bajo (0), las salidas de las compuertas AND son siempre 0, independientemente de las entradas **R** y **S**. Esto hace que el *latch* permanezca en su último estado, ignorando efectivamente las entradas. Por lo tanto, la señal *Enable* permite habilitar el *latch* para que responda a sus entradas **R** y **S** o deshabilitarlo para mantener su estado actual.

A continuación, podemos extender este concepto para crear un **SR Flip-Flop**. La diferencia clave entre un *latch* y un *flip-flop* es que las salidas de un *latch* cambian cada vez que sus entradas cambian, mientras que las salidas de un *flip-flop* solo cambian con un disparador específico, típicamente un pulso de reloj. En un *SR Flip-Flop*, una entrada **Clock** (indicada por un símbolo de triángulo en los diagramas) controla cuándo se actualizan las salidas. Específicamente, las salidas **Q** y **Q̅** cambian solo cuando el reloj transiciona de bajo a alto (un flanco de subida). En todos los demás momentos, las entradas **R** y **S** son ignoradas, y el *flip-flop* retiene su estado anterior.

El *SR Flip-Flop* logra esto usando un capacitor en el circuito del reloj. Cuando el reloj transiciona de bajo a alto, una corriente breve fluye a través del capacitor mientras se carga, creando un pulso de voltaje corto en las entradas de las compuertas AND. Este pulso habilita efectivamente el *SR Latch con Enable* solo en ese momento, permitiendo que las entradas **R** y **S** afecten a las salidas **Q** y **Q̅**. Una vez que el capacitor está completamente cargado, el pulso se detiene, y el *flip-flop* ignora los cambios posteriores de entrada hasta el siguiente flanco de subida.

Así es como se comporta el *SR Flip-Flop* durante un flanco de subida del reloj:
- Si **R** está en alto y **S** en bajo, **Q** se pone en bajo (*reset*), y **Q̅** se pone en alto.
- Si **S** está en alto y **R** en bajo, **Q** se pone en alto (*set*), y **Q̅** se pone en bajo.
- Si tanto **R** como **S** están en bajo, el *flip-flop* permanece en su estado anterior.
- Si tanto **R** como **S** están en alto (el estado inválido del *SR Latch*), el comportamiento es impredecible. Similar al *SR Latch*, tanto **Q** como **Q̅** pueden ponerse en bajo durante el pulso, pero cuando las entradas se liberan, el *flip-flop* se establece en un estado u otro según qué entrada caiga primero. Esto hace que la salida sea incierta, ya que depende de diferencias de temporización (por ejemplo, unos nanosegundos), lo que convierte a este en un estado inválido e impredecible.

Para abordar esta impredecibilidad, podemos usar un **JK Flip-Flop**, que es similar al *SR Flip-Flop* pero incluye retroalimentación de las salidas **Q** y **Q̅** a las entradas. El *JK Flip-Flop* utiliza compuertas AND de tres entradas que incorporan **J** (análogo a **S**), **K** (análogo a **R**), y las señales de retroalimentación **Q** y **Q̅**. Las letras **J** y **K** son arbitrarias y no representan términos específicos, pero distinguen este circuito del *SR Flip-Flop*.

El *JK Flip-Flop* opera de la siguiente manera:
- Si **J** y **K** son ambos 0, las salidas de las compuertas AND son 0, por lo que el *flip-flop* permanece en su estado anterior, incluso durante un pulso de reloj.
- Si el *latch* está actualmente configurado (**Q** = 1, **Q̅** = 0) y quieres restablecerlo (**K** = 1, **J** = 0), la compuerta AND conectada a **K** emite un 1 durante el pulso de reloj (dado que **Q** = 1), restableciendo el *flip-flop* (**Q** = 0, **Q̅** = 1).
- Si el *latch* ya está restablecido (**Q** = 0, **Q̅** = 1) y **K** = 1, **J** = 0, las salidas de las compuertas AND permanecen en 0, por lo que el *flip-flop* se mantiene restablecido, que es el comportamiento deseado.
- De manera similar, si el *latch* está restablecido (**Q** = 0, **Q̅** = 1) y quieres configurarlo (**J** = 1, **K** = 0), la compuerta AND conectada a **J** emite un 1 durante el pulso de reloj (dado que **Q̅** = 1), configurando el *flip-flop* (**Q** = 1, **Q̅** = 0).
- Si el *latch* ya está configurado y **J** = 1, **K** = 0, permanece configurado, como se esperaba.

La característica única del *JK Flip-Flop* surge cuando tanto **J** como **K** son 1. Debido a la retroalimentación, solo una compuerta AND puede estar activa a la vez (ya que **Q** y **Q̅** no pueden ser ambos 1). Si **Q** es 1, la compuerta AND para **K** está activa, y el *flip-flop* se restablece en el siguiente pulso de reloj (**Q** = 0, **Q̅** = 1). Si **Q** es 0, la compuerta AND para **J** está activa, y el *flip-flop* se configura en el siguiente pulso de reloj (**Q** = 1, **Q̅** = 0). Esto crea un comportamiento de **toggle** (conmutación): si **J** = **K** = 1, el *flip-flop* cambia su estado en cada pulso de reloj (**Q** cambia de 0 a 1 o de 1 a 0). Esta conmutación predecible elimina el estado inválido e impredecible del *SR Flip-Flop*, haciendo que el *JK Flip-Flop* sea más robusto y versátil.