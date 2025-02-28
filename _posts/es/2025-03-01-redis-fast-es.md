---
audio: false
lang: es
layout: post
title: ¿Por qué es rápido Redis?
translated: true
---

### Puntos Clave
- Parece probable que el video de YouTube "System Design: Why is single-threaded Redis so fast?" de ByteByteGo explique la velocidad de Redis debido al almacenamiento en memoria, la multiplexación de E/S y las estructuras de datos eficientes.
- La investigación sugiere que estos factores permiten que Redis maneje hasta 100,000 consultas por segundo, a pesar de ser single-threaded para el procesamiento de solicitudes.
- La evidencia indica que las versiones recientes de Redis han añadido multihilo para tareas específicas, pero el núcleo sigue siendo single-threaded.

---

### Introducción
Este post de blog se basa en el video de YouTube "System Design: Why is single-threaded Redis so fast?" de ByteByteGo, parte de su serie de diseño de sistemas. Redis, conocido por su alto rendimiento, puede manejar hasta 100,000 consultas por segundo en una sola máquina, lo cual es impresionante para un sistema single-threaded. Exploremos por qué esto es posible y qué hace que Redis sea tan rápido.

### Razones de la Velocidad de Redis
La velocidad de Redis se puede atribuir a varios factores clave, probablemente cubiertos en el video:

- **Almacenamiento en Memoria**: Redis almacena datos en RAM, que es mucho más rápido que el almacenamiento en disco. Esto reduce la latencia y aumenta el rendimiento, ya que los tiempos de acceso a la memoria son en nanosegundos en comparación con los milisegundos para el acceso al disco.

- **Multiplexación de E/S y Ejecución Single-Threaded**: La multiplexación de E/S, utilizando mecanismos como epoll en Linux, permite que un solo hilo maneje múltiples conexiones de clientes de manera eficiente. Esto evita el sobrecoste del cambio de contexto, y el bucle single-threaded simplifica las operaciones eliminando problemas de sincronización.

- **Estructuras de Datos Eficientes**: Redis utiliza estructuras de datos optimizadas como tablas hash (búsquedas O(1)), listas enlazadas y listas de salto, que mejoran el rendimiento minimizando el uso de memoria y acelerando las operaciones.

### Escalabilidad y Evolución
Para alta concurrencia, Redis se puede escalar horizontalmente utilizando múltiples instancias o agrupación. Un detalle inesperado es que, aunque el procesamiento de solicitudes principal sigue siendo single-threaded, las versiones recientes (desde 4.0) han introducido multihilo para tareas como la eliminación de objetos en segundo plano, mejorando aún más el rendimiento sin cambiar el modelo principal.

---

### Nota de Encuesta: Análisis Detallado del Rendimiento Single-Threaded de Redis

Esta sección proporciona un análisis exhaustivo de por qué Redis single-threaded es tan rápido, basado en el video de YouTube "System Design: Why is single-threaded Redis so fast?" de ByteByteGo y la investigación relacionada. El video, publicado el 13 de agosto de 2022, es parte de una serie centrada en el diseño de sistemas, escrita por los creadores de los libros de entrevistas de diseño de sistemas más vendidos. Dado el enfoque del canal, el video probablemente proporciona información detallada adecuada para entrevistas técnicas y discusiones de diseño de sistemas.

#### Antecedentes y Contexto
Redis, un almacén de valores clave en memoria de código abierto, se utiliza ampliamente como caché, broker de mensajes y motor de transmisión. Soporta estructuras de datos como cadenas, listas, conjuntos, hashes, conjuntos ordenados y estructuras probabilísticas como Bloom Filter y HyperLogLog. El título del video sugiere una exploración de por qué Redis mantiene un alto rendimiento a pesar de su procesamiento de solicitudes single-threaded, que es central en su diseño.

De artículos relacionados, Redis puede manejar hasta 100,000 Consultas Por Segundo (QPS) en una sola máquina, una cifra a menudo citada en las pruebas de rendimiento. Esta velocidad es sorprendente dado el modelo single-threaded, pero la investigación indica que se debe a varias elecciones arquitectónicas.

#### Factores Clave que Contribuyen a la Velocidad de Redis

1. **Almacenamiento en Memoria**
   Redis almacena datos en RAM, que es al menos 1000 veces más rápido que el acceso aleatorio al disco. Esto elimina la latencia de la E/S del disco, con tiempos de acceso a la RAM de alrededor de 100-120 nanosegundos en comparación con 50-150 microsegundos para SSDs y 1-10 milisegundos para HDDs. El video probablemente enfatiza esto como una razón principal, ya que se alinea con el enfoque del canal en los fundamentos del diseño de sistemas.

   | Aspecto               | Detalles                                      |
   |----------------------|----------------------------------------------|
   | Medio de Almacenamiento| RAM (en memoria)                              |
   | Tiempo de Acceso      | ~100-120 nanosegundos                        |
   | Comparación con Disco | 1000 veces más rápido que el acceso aleatorio al disco        |
   | Impacto en el Rendimiento| Reduce la latencia, aumenta el rendimiento        |

2. **Multiplexación de E/S y Bucle de Ejecución Single-Threaded**
   La multiplexación de E/S permite que un solo hilo monitoree múltiples flujos de E/S simultáneamente utilizando llamadas del sistema como `select`, `poll`, `epoll` (Linux), `kqueue` (Mac OS) o `evport` (Solaris). Esto es crucial para manejar múltiples conexiones de clientes sin bloquear, un punto probablemente detallado en el video. El bucle de ejecución single-threaded evita el sobrecoste del cambio de contexto y la sincronización, simplificando el desarrollo y la depuración.

   | Mecanismo            | Descripción                                  |
   |----------------------|----------------------------------------------|
   | epoll/kqueue         | Eficiente para alta concurrencia, no bloqueante |
   | select/poll          | Más antiguo, menos escalable, complejidad O(n)        |
   | Impacto               | Reduce el sobrecoste de conexión, habilita el encolado |

   Sin embargo, comandos que bloquean al cliente como `BLPOP` o `BRPOP` pueden retrasar el tráfico, un posible inconveniente mencionado en artículos relacionados. El video puede discutir cómo esta elección de diseño equilibra la simplicidad con el rendimiento.

3. **Estructuras de Datos de Nivel Inferior Eficientes**
   Redis aprovecha estructuras de datos como tablas hash para búsquedas de clave O(1), listas enlazadas para listas y listas de salto para conjuntos ordenados. Estas están optimizadas para operaciones en memoria, minimizando el uso de memoria y maximizando la velocidad. El video probablemente incluye diagramas o ejemplos, como cómo las tablas hash permiten operaciones de clave-valor rápidas, un tema común en entrevistas de diseño de sistemas.

   | Estructura de Datos       | Caso de Uso                                     | Complejidad Temporal |
   |----------------------|----------------------------------------------|-----------------|
   | Tabla Hash           | Almacenamiento de clave-valor                           | O(1) promedio    |
   | Lista Enlazada          | Listas, eficiente en los extremos                    | O(1) para extremos   |
   | Lista de Salto            | Conjuntos ordenados, almacenamiento ordenado                | O(log n)        |

   Esta optimización es crítica, ya que la mayoría de las operaciones de Redis son basadas en memoria, con cuellos de botella típicamente en memoria o red, no en CPU.

#### Consideraciones Adicionales y Evolución
Aunque el procesamiento de solicitudes principal es single-threaded, las versiones recientes de Redis han introducido multihilo para tareas específicas. Desde Redis 4.0, se ha implementado la liberación asincrónica de memoria (lazy-free), y desde 6.0, se ha añadido multihilo para el análisis de protocolos bajo alta concurrencia. Estos cambios, probablemente mencionados en el video, mejoran el rendimiento sin alterar el modelo single-threaded para operaciones principales.

Para escalar más allá de una sola instancia, Redis soporta agrupación y ejecución de múltiples instancias, una estrategia que puede ser discutida para abordar necesidades de alta concurrencia. Este es un aspecto importante para el diseño de sistemas, alineándose con el enfoque del canal en sistemas de gran escala.

#### Posibles Desventajas y Comparaciones
El modelo single-threaded tiene ventajas como la ausencia de contención de bloqueos y una depuración más sencilla, pero puede enfrentar desafíos con operaciones bloqueantes y cuellos de botella de memoria/red bajo alta carga. Artículos relacionados sugieren que para tareas intensivas en CPU, bases de datos multihilo podrían desempeñarse mejor, pero para los casos de uso típicos de Redis, el diseño single-threaded es óptimo.

#### Conclusión
El video "System Design: Why is single-threaded Redis so fast?" de ByteByteGo probablemente cubre el almacenamiento en memoria, la multiplexación de E/S y las estructuras de datos eficientes como razones clave para la velocidad de Redis. Estos factores le permiten manejar un alto QPS, con versiones recientes añadiendo multihilo para optimizaciones específicas. Este análisis proporciona una comprensión exhaustiva, adecuada tanto para aprendices técnicos como para profesionales del diseño de sistemas.

---

### Citas Clave
- [Why is redis so fast blog post](https://blog.bytebytego.com/p/why-is-redis-so-fast)
- [Why is Redis So Fast Despite Being Single-Threaded article](https://medium.com/@aditimishra_541/why-is-redis-so-fast-despite-being-single-threaded-dc06ba33fc75)
- [Interview on Redis thread model article](https://medium.com/javarevisited/interview-why-is-redis-so-fast-even-though-it-is-single-threaded-bfe663dabe08)
- [Why is single threaded Redis so fast article](https://www.pixelstech.net/article/1677580861-Why-is-single-threaded-Redis-so-fast)