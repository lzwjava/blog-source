---
audio: false
generated: true
lang: es
layout: post
title: Construcción y Prueba de un Biestable JK
translated: true
type: note
---

En un video anterior, exploramos el flip-flop JK y su funcionamiento, observando su similitud con el flip-flop SR pero con el mecanismo de retroalimentación añadido. Esta retroalimentación permite que la salida conmute cuando ambas entradas están en alto en un flanco de subida del reloj, en lugar de entrar en un estado indefinido. En este video, mi objetivo es construirlo y observar su funcionalidad práctica.

He construido un flip-flop JK siguiendo el diagrama del circuito proporcionado. Durante la construcción, me di cuenta de un error de etiquetado en el diagrama: esta es en realidad la entrada K, y esta es la entrada J. J corresponde al "set", lo que significa que cuando se pone en alto, la salida Q también debería ponerse en alto. Por el contrario, K corresponde al "reset", por lo que cuando se pone en alto, la salida Q debería ponerse en bajo. Aparte de esta pequeña corrección de etiquetado, el resto del circuito es correcto.

Para las puertas NOR, estoy utilizando el chip 74LS02, específicamente las dos puertas NOR en su parte superior. El otro chip, el 74LS11, es una puerta AND triple de 3 entradas. Estoy empleando dos de estas puertas AND de tres entradas para el circuito.

Al conectar la alimentación, el circuito se estabiliza en un estado, con la salida Q aparentemente "encendida". Luego conecté mi circuito de reloj. Los dos interruptores que ves están conectados a tierra a través de resistencias pull-down; presionar un botón hace que la entrada se ponga en alto. Estos interruptores están conectados con cables verdes a las dos puertas AND, sirviendo como las entradas K y J.

La señal de reloj también se alimenta a las puertas AND. Pasa a través de un circuito RC, que consiste en un condensador de 0.0001 microfaradios y una resistencia de 1000 ohmios. La salida de este circuito RC, transportada por dos cables blancos, va a otra entrada en ambas puertas AND. Las salidas de estas puertas AND están representadas por cables azules, que se conectan a dos de las entradas en las puertas NOR. Las otras entradas de las puertas NOR reciben retroalimentación de sus propias salidas a través de cables amarillos. Estos cables amarillos también vuelven a las puertas AND. Finalmente, las salidas de las puertas NOR accionan dos LEDs: uno para Q y otro para el complemento de Q.

Cuando la entrada K se pone en alto, el latch debería resetearse, y la salida Q debería apagarse, lo cual hace. De manera similar, poner la entrada J en alto debería establecer el latch, encendiendo la salida Q, lo cual también hace. Es importante observar que el cambio no es instantáneo al presionar el botón; ocurre con la siguiente señal de reloj, ya que esta operación está controlada por el flanco de subida del reloj.

Ahora, como esto es un flip-flop JK, si ambas entradas J y K se establecen en alto, esperamos que la salida conmute con cada pulso de reloj. Sin embargo, no está conmutando consistentemente. A veces lo hace, especialmente si manipulo el circuito ligeramente, pero es muy inconsistente. Para asegurarme de que estoy presionando ambos botones, insertaré puentes sobre ellos, proporcionando efectivamente una entrada continua en alto tanto a J como a K. Esto *debería* hacer que conmute con cada flanco de subida del reloj. Aunque ahora funciona mejor, sigue siendo inconsistente.

Este comportamiento inconsistente tiene una explicación clara, y la mejor manera de entenderlo es usando un osciloscopio para examinar las señales.

Primero, veamos la entrada de reloj como referencia. El osciloscopio muestra la señal de reloj encendiéndose y apagándose, aproximadamente dos veces por segundo. Cada división en el osciloscopio representa 100 milisegundos, así que en 10 divisiones, pulsa dos veces por segundo.

A continuación, quiero observar la salida, ya que esto es lo que esperamos que conmute con cada pulso de reloj. El reloj está pulsando efectivamente a unas dos pulsaciones por segundo. Actualmente, la salida no está conmutando, pero con un pequeño ajuste, sí conmuta, aunque de manera inconsistente. Cuando *sí* conmuta, lo hace en los flancos de subida del reloj, como se desea.

La parte interesante surge cuando hacemos zoom en el flanco de subida del reloj. Vemos algo de actividad allí. Al acercarnos más, se vuelve bastante claro: cuando el reloj se pone en alto, la salida *sí* conmuta, pero lo hace de un lado a otro varias veces antes de finalmente estabilizarse en un estado estable. Esta es precisamente la razón por la cual el comportamiento es tan inconsistente. La salida conmuta como se desea en el flanco de subida del reloj, pero luego vuelve a conmutar rápidamente poco después. El período de estas conmutaciones rápidas es de unos 82 nanosegundos.

Este fenómeno, conocido como "carrera" o "racing", tiene sentido cuando reexaminamos el diagrama del circuito. El pulso de reloj, aunque pretendemos usar solo su flanco de subida, permanece en alto durante un tiempo considerable (250 milisegundos en este caso). Si la salida cambia *antes* de que este pulso vuelva a cero, el bucle de retroalimentación hace que cambie otra vez, y otra vez, lo que lleva a múltiples conmutaciones. Así que, cuando el pulso de reloj se pone en alto, la salida se enciende, pero inmediatamente se apaga y se enciende repetidamente. Es pura casualidad que a veces se estabilice en el estado deseado.

La causa principal de esta condición de carrera reside en el circuito RC utilizado para detectar el flanco de subida. Mencioné que el condensador es de 0.0001 microfaradios y la resistencia es de 1000 ohmios. Multiplicar estos valores da la constante de tiempo del circuito RC, que indica la duración del pulso. Esta constante de tiempo es de aproximadamente 100 nanosegundos.

Midamos la entrada de pulso para el circuito. Inicialmente, se ve muy bien cuando se aleja la imagen – un pulso rápido en el flanco de subida del reloj, como se desea. El problema es que este pulso no es lo suficientemente rápido. Es un pulso de 1 microsegundo, y durante ese 1 microsegundo, la salida conmuta de un lado a otro repetidamente antes de finalmente estabilizarse cuando el pulso cae a un cero lógico.

¿Qué se puede hacer al respecto? Una opción es hacer el pulso más corto. Dado que el período de conmutación es de alrededor de 80 nanosegundos, necesitamos un pulso significativamente más corto que 1 microsegundo. Podemos intentar cambiar la resistencia de 1000 ohmios por una de 100 ohmios, lo que debería reducir la constante de tiempo a 100 nanosegundos.

Después de cambiar la resistencia, observamos un pulso mucho más pequeño. Sin embargo, todavía no funciona de manera consistente. En este punto, nos estamos topando con las limitaciones de las protoboards. Las señales de alta velocidad en el rango de decenas de nanosegundos son un desafío en las protoboards debido a las capacitancias parásitas, inductancias y otros efectos parasitarios. Esto explica por qué simplemente mover mi mano cerca del circuito puede alterar su comportamiento, ya que mi mano cambia la capacitancia al actuar como un objeto conectado a tierra.

Puedes ver que la salida ahora se pone en alto, luego en bajo, y se mantiene en bajo. Pero de nuevo, si ajusto la posición de mi mano, podría empezar a conmutar. No estoy cambiando ninguna conexión, solo moviendo mi mano, lo que afecta a la capacitancia.

Incluso el flanco de subida de nuestro reloj no es perfectamente nítido en esta escala de tiempo, nuevamente debido a las limitaciones de la protoboard. El pulso que estamos generando no es tan limpio como lo era con la resistencia más grande. En última instancia, todo esto apunta al hecho de que estamos presionando los límites de lo que es factible en una protoboard. Este método particular de detectar un flanco de subida usando un circuito RC es inherentemente problemático en un flip-flop JK debido a la condición de carrera. Si el pulso no es lo suficientemente estrecho (idealmente solo unos pocos nanosegundos), la salida se retroalimentará y conmutará más de una vez por flanco de subida del reloj.

Entonces, ¿cuál es la solución? En el próximo video, demostraré un método muy superior para construir un flip-flop JK que elimina por completo este problema de carrera: el flip-flop JK maestro-esclavo. Es un diseño mucho más robusto y debería funcionar sin problemas en una protoboard.