---
audio: false
generated: true
lang: es
layout: post
title: Recolección de Basura en Java
translated: true
type: note
---

¡Vale, aprendamos sobre Garbage Collection (GC) en Java! Es un aspecto crucial de la gestión de memoria de Java que ayuda a los desarrolladores a evitar la asignación y liberación manual de memoria.

**¿Qué es Garbage Collection en Java?**

Garbage Collection es el proceso automático de recuperar la memoria ocupada por objetos que ya no están en uso por una aplicación Java. En esencia, es la forma que tiene Java de limpiar la "basura" (objetos no utilizados) para hacer espacio para nuevos objetos.

**¿Por qué se necesita Garbage Collection?**

En muchos otros lenguajes de programación (como C o C++), los desarrolladores son responsables de asignar y desasignar memoria explícitamente usando funciones como `malloc` y `free`. Esta gestión manual de la memoria puede llevar a varios problemas:

*   **Fugas de Memoria:** Si se asigna memoria pero nunca se libera, la aplicación puede eventualmente quedarse sin memoria y fallar.
*   **Punteros Colgantes:** Si se libera memoria pero un puntero todavía hace referencia a esa ubicación de memoria, usar ese puntero puede llevar a comportamientos impredecibles o fallos.
*   **Mayor Complejidad de Desarrollo:** Gestionar la memoria manualmente añade una capa significativa de complejidad al desarrollo de software.

El Garbage Collection de Java automatiza este proceso, liberando a los desarrolladores de la carga de la gestión manual de la memoria y facilitando la escritura de código más seguro y confiable.

**¿Cómo funciona Garbage Collection?**

La idea central detrás del garbage collection es identificar qué objetos en la memoria todavía están siendo utilizados por la aplicación y cuáles no. El recolector de basura luego recupera la memoria ocupada por los objetos no utilizados.

Aquí hay una descripción general simplificada del proceso:

1.  **Identificación de Objetos Activos (Marcado):** El recolector de basura comienza identificando el conjunto de objetos que todavía son alcanzables desde los objetos "raíz". Los objetos raíz son típicamente objetos directamente accesibles por la aplicación, tales como:
    * Variables locales en métodos en ejecución.
    * Variables estáticas.
    * Objetos referenciados por código nativo.
    * Los hilos activos de la Java Virtual Machine (JVM).

    El recolector de basura recorre el grafo de objetos comenzando desde estas raíces, marcando todos los objetos que son alcanzables.

2.  **Recuperación de Memoria (Barrido y Compactación):** Una vez que los objetos activos están marcados, el recolector de basura necesita recuperar la memoria ocupada por los objetos no marcados (inalcanzables). Diferentes algoritmos de recolección de basura emplean diferentes estrategias para esto:

    *   **Marcar y Barrer:** Este algoritmo identifica y marca los objetos activos, luego barre la memoria, liberando el espacio ocupado por los objetos no marcados. Esto puede llevar a fragmentación de memoria (pequeños bloques dispersos de memoria libre que no son lo suficientemente grandes para asignar nuevos objetos).
    *   **Marcar y Compactar:** Este algoritmo también marca los objetos activos. Después del marcado, mueve (comprime) los objetos activos juntos en la memoria, eliminando la fragmentación y facilitando la asignación de bloques contiguos de memoria para nuevos objetos.
    *   **Copia:** Este algoritmo divide la memoria en dos o más regiones. Los objetos activos se copian de una región a otra, recuperando efectivamente el espacio en la región original.

**Conceptos Clave en Java Garbage Collection:**

*   **Heap:** El área de memoria donde se asignan los objetos en Java. El recolector de basura opera principalmente en el heap.
*   **Generación Joven (Nursery):** Esta es una porción del heap donde los objetos recién creados se asignan inicialmente. Se divide además en:
    *   **Espacio Eden:** Donde se crean la mayoría de los nuevos objetos.
    *   **Espacios Survivor (S0 y S1):** Se utilizan para contener objetos que han sobrevivido a algunos ciclos de garbage collection menor.
*   **Generación Vieja (Tenured Generation):** Los objetos que han sobrevivido múltiples ciclos de garbage collection en la generación joven eventualmente se mueven a la generación vieja. Los objetos en la generación vieja son generalmente de larga duración.
*   **Generación Permanente (PermGen) / Metaspace:** En versiones antiguas de Java (anteriores a Java 8), la Generación Permanente almacenaba metadatos sobre clases y métodos. En Java 8 y posteriores, esto ha sido reemplazado por Metaspace, que es parte de la memoria nativa (no del heap de Java).
*   **Algoritmos de Garbage Collection:** Se utilizan diferentes algoritmos para la recolección de basura, cada uno con sus propias ventajas y desventajas en términos de rendimiento y eficiencia.

**Garbage Collection Generacional:**

Java HotSpot JVM (la JVM más común) utiliza un enfoque generacional para la recolección de basura. Esto se basa en la observación de que la mayoría de los objetos en una aplicación tienen vidas útiles cortas.

1.  **GC Menor (GC de la Generación Joven):** Cuando el espacio Eden se llena, se activa un GC menor. Los objetos activos de Eden y uno de los espacios Survivor (digamos, S0) se copian al otro espacio Survivor (S1). Los objetos que han sobrevivido un cierto número de ciclos de GC menor se mueven a la generación vieja. Los objetos inalcanzables se descartan.

2.  **GC Mayor (GC de la Generación Vieja) / GC Completo:** Cuando la generación vieja se llena, se realiza un GC mayor (o a veces un GC completo, que puede involucrar tanto a las generaciones jóvenes como a las viejas). Este proceso generalmente consume más tiempo que un GC menor y puede causar pausas más largas en la ejecución de la aplicación.

**Recolectores de Basura Comunes en Java HotSpot JVM:**

La JVM Java HotSpot ofrece varios algoritmos de recolección de basura que se pueden elegir según los requisitos de la aplicación (por ejemplo, baja latencia, alto rendimiento). Algunos comunes incluyen:

*   **Recolector Serial:** Utiliza un solo hilo para la recolección de basura. Adecuado para aplicaciones pequeñas con recursos limitados.
*   **Recolector Paralelo:** Utiliza múltiples hilos para la recolección de basura, mejorando el rendimiento. Adecuado para aplicaciones con conjuntos de datos de moderados a grandes que se ejecutan en procesadores multi-núcleo.
*   **Recolector CMS (Concurrent Mark Sweep):** Intenta minimizar los tiempos de pausa realizando la mayor parte del trabajo de recolección de basura concurrentemente con los hilos de la aplicación. Sin embargo, puede llevar a fragmentación y podría requerir un GC completo eventualmente.
*   **Recolector G1 (Garbage-First):** Pretende proporcionar un buen equilibrio entre rendimiento y baja latencia. Divide el heap en regiones y prioriza recolectar basura de las regiones con más basura. Es el recolector por defecto en Java 9 y posteriores.
*   **Recolector ZGC (Z Garbage Collector):** Un recolector de basura de baja latencia diseñado para heaps grandes. Su objetivo son tiempos de pausa de menos de 10ms.
*   **Shenandoah:** Otro recolector de basura de baja latencia con objetivos similares a ZGC.

Puede especificar qué recolector de basura usar mediante opciones de línea de comandos de la JVM.

**¿Cuándo se ejecuta Garbage Collection?**

La recolección de basura es principalmente un proceso automático impulsado por la JVM. Típicamente se ejecuta cuando:

*   La generación joven (espacio Eden) se llena.
*   La generación vieja se llena.
*   El sistema tiene poca memoria.

Si bien no puede controlar directamente *cuándo* se ejecutará la recolección de basura, puede sugerir a la JVM que podría ser un buen momento para realizar la recolección de basura usando `System.gc()`. Sin embargo, no hay garantía de que la JVM ejecute realmente el recolector de basura inmediatamente o en absoluto cuando llama a este método. Generalmente es mejor confiar en el mecanismo automático de recolección de basura de la JVM.

**`System.gc()` y Finalización:**

*   **`System.gc()`:** Como se mencionó, esto es una petición a la JVM para que ejecute el recolector de basura. A menudo se recomienda evitar depender de este método para una gestión crítica de la memoria, ya que la JVM suele ser mejor decidiendo cuándo realizar el GC.
*   **Método `finalize()`:** Antes de que un objeto sea recolectado por el garbage collector, la JVM le da la oportunidad de realizar cualquier operación de limpieza llamando a su método `finalize()` (si está implementado). Sin embargo, `finalize()` tiene varios inconvenientes y generalmente se desaconseja en el desarrollo moderno de Java. Puede introducir problemas de rendimiento y hacer que la recolección de basura sea menos predecible. Considere usar otros mecanismos como try-with-resources para la gestión de recursos.

**Impacto de Garbage Collection en el Rendimiento de la Aplicación:**

Si bien la recolección de basura es esencial para la gestión de la memoria, también puede impactar el rendimiento de una aplicación debido a las pausas "stop-the-world". Durante estas pausas, todos los hilos de la aplicación se detienen mientras el recolector de basura realiza su trabajo. La duración y frecuencia de estas pausas dependen del algoritmo de recolección de basura que se esté utilizando y del tamaño y las características del heap.

Los recolectores de basura de baja latencia como G1, ZGC y Shenandoah tienen como objetivo minimizar estos tiempos de pausa para hacer que las aplicaciones sean más receptivas.

**Ajuste de Garbage Collection:**

Para aplicaciones con requisitos de rendimiento específicos, la recolección de basura se puede ajustar modificando parámetros de la JVM como:

*   Tamaño del heap (`-Xms`, `-Xmx`)
*   Tamaño de la generación joven (`-Xmn`)
*   Ratios de los espacios Survivor (`-XX:SurvivorRatio`)
*   Elección de un recolector de basura específico (`-XX:+UseG1GC`, `-XX:+UseZGC`, etc.)
*   Establecer flags de recolección de basura para un control más detallado.

El ajuste del GC es un tema avanzado y generalmente requiere un análisis cuidadoso del comportamiento y rendimiento de la aplicación.

**Mejores Prácticas para Escribir Código Amigable con el Recolector de Basura:**

Si bien Java maneja la memoria automáticamente, escribir código teniendo en cuenta al recolector de basura puede conducir a un mejor rendimiento:

*   **Minimice la Creación de Objetos:** Crear una gran cantidad de objetos de corta duración puede ejercer presión sobre el recolector de basura. Intente reutilizar objetos cuando sea apropiado.
*   **Libere Referencias a Objetos:** Si tiene una referencia a un objeto que ya no necesita, establezca la referencia a `null`. Esto hace que el objeto sea elegible para la recolección de basura antes.
*   **Use Estructuras de Datos con Cuidado:** Elija estructuras de datos que sean apropiadas para sus necesidades. Por ejemplo, usar un `ArrayList` grande y luego descartar la mayoría de sus elementos puede ser ineficiente.
*   **Evite los Finalizadores:** Como se mencionó anteriormente, evite depender del método `finalize()` para la limpieza de recursos. Use try-with-resources para recursos como archivos y conexiones de red.
*   **Tenga Cuidado con las Variables Estáticas:** Los objetos referenciados por variables estáticas vivirán durante toda la duración de la aplicación, así que tenga precaución al almacenar objetos grandes o innecesarios en campos estáticos.

**En Resumen:**

Garbage Collection en Java es un proceso automático de gestión de memoria que recupera la memoria ocupada por objetos no utilizados. Simplifica el desarrollo liberando a los desarrolladores de la gestión manual de memoria. Comprender cómo funciona, las diferentes generaciones del heap y los algoritmos de recolección de basura disponibles puede ayudarle a escribir aplicaciones Java más eficientes y de mejor rendimiento.