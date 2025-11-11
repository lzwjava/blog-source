---
audio: false
generated: true
lang: es
layout: post
title: Números de Latencia
translated: true
type: note
---

### Puntos Clave
- Es probable que el video analice los números de latencia estándar que los programadores deberían conocer, basándose en su título y contenido en línea relacionado.
- La investigación sugiere que estos números incluyen tiempos para operaciones como acceso a caché L1 (0.5 ns) y viajes de ida y vuelta en red (hasta 150 ms), variando según el hardware.
- La evidencia indica que estos números son aproximados, con actualizaciones que reflejan avances tecnológicos, especialmente en SSD y redes.

### Introducción
El video "Latency Numbers Programmer Should Know: Crash Course System Design #1" probablemente cubre cifras de latencia esenciales para operaciones informáticas, cruciales para el diseño de sistemas. Estos números ayudan a los programadores a comprender los impactos en el rendimiento y a optimizar sistemas.

### Números de Latencia y Su Importancia
La latencia es el retraso entre iniciar y completar una operación, como acceder a la memoria o enviar datos a través de una red. El video probablemente enumera latencias típicas, tales como:
- Referencia a caché L1 en 0.5 nanosegundos (ns), el acceso a memoria más rápido.
- Un viaje de ida y vuelta dentro del mismo centro de datos en 500 microsegundos (us) o 0.5 milisegundos (ms), afectando a los sistemas distribuidos.

Estas cifras, aunque aproximadas, guían las decisiones en el diseño de sistemas, como elegir entre almacenamiento en memoria o en disco.

### Contexto en el Diseño de Sistemas
Comprender estas latencias ayuda a optimizar el código, tomar decisiones de compensación y mejorar la experiencia del usuario. Por ejemplo, saber que una búsqueda en disco toma 10 ms puede influir en el diseño de bases de datos para minimizar tales operaciones.

### Detalle Inesperado
Un aspecto interesante es cómo estos números, como los tiempos de lectura de SSD, han mejorado con la tecnología, mientras que latencias centrales de la CPU como el acceso a la caché L1 se mantienen estables, mostrando el impacto desigual de la evolución del hardware.

---

### Nota de Estudio: Análisis Detallado de los Números de Latencia del Video

Esta nota proporciona una exploración exhaustiva de los números de latencia probablemente discutidos en el video "Latency Numbers Programmer Should Know: Crash Course System Design #1", basándose en contenido en línea disponible y recursos relacionados. El análisis tiene como objetivo sintetizar información para programadores y diseñadores de sistemas, ofreciendo tanto un resumen como detalles sobre la importancia de estos números.

#### Antecedentes y Contexto
El video, accesible en [YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0), es parte de una serie sobre diseño de sistemas, centrándose en números de latencia críticos para programadores. La latencia, definida como el retraso de tiempo entre el inicio y la finalización de una operación, es fundamental para comprender el rendimiento del sistema. Dado el título del video y las búsquedas relacionadas, parece cubrir cifras de latencia estándar popularizadas por figuras como Jeff Dean de Google, a menudo referenciadas en comunidades de programación.

Búsquedas en línea revelaron varios recursos que discuten estos números, incluyendo un Gist de GitHub titulado "Latency Numbers Every Programmer Should Know" ([GitHub Gist](https://gist.github.com/jboner/2841832)) y un artículo de Medium de 2023 ([Artículo de Medium](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)). Estas fuentes, junto con una publicación de High Scalability de 2013 ([High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)), proporcionaron una base para compilar el contenido probable del video.

#### Compilación de los Números de Latencia
Basándose en la información recopilada, la siguiente tabla resume los números de latencia estándar, probablemente discutidos en el video, con explicaciones para cada operación:

| Operación                                      | Latencia (ns) | Latencia (us) | Latencia (ms) | Explicación                                                          |
|------------------------------------------------|--------------|--------------|--------------|----------------------------------------------------------------------|
| Referencia a caché L1                          | 0.5          | -            | -            | Acceso a datos en la caché de Nivel 1, la memoria más rápida cerca de la CPU. |
| Predicción errónea de bifurcación              | 5            | -            | -            | Penalización cuando la CPU predice incorrectamente una bifurcación condicional. |
| Referencia a caché L2                          | 7            | -            | -            | Acceso a datos en la caché de Nivel 2, más grande que L1 pero más lenta. |
| Bloqueo/desbloqueo de mutex                    | 25           | -            | -            | Tiempo para adquirir y liberar un mutex en programas multihilo.        |
| Referencia a memoria principal                 | 100          | -            | -            | Acceso a datos desde la memoria principal de acceso aleatorio (RAM).  |
| Comprimir 1 KB con Zippy                       | 10,000       | 10           | -            | Tiempo para comprimir 1 kilobyte usando el algoritmo Zippy.           |
| Enviar 1 KB por red de 1 Gbps                  | 10,000       | 10           | -            | Tiempo para transmitir 1 kilobyte por una red de 1 Gigabit por segundo. |
| Lectura aleatoria de 4 KB desde SSD            | 150,000      | 150          | -            | Lectura aleatoria de 4 kilobytes desde una unidad de estado sólido.   |
| Lectura secuencial de 1 MB desde memoria       | 250,000      | 250          | -            | Lectura secuencial de 1 megabyte desde la memoria principal.          |
| Viaje de ida y vuelta dentro del mismo centro de datos | 500,000      | 500          | 0.5          | Tiempo de viaje de ida y vuelta en red dentro del mismo centro de datos. |
| Lectura secuencial de 1 MB desde SSD           | 1,000,000    | 1,000        | 1            | Lectura secuencial de 1 megabyte desde un SSD.                        |
| Búsqueda en HDD                                | 10,000,000   | 10,000       | 10           | Tiempo para que un disco duro busque una nueva posición.              |
| Lectura secuencial de 1 MB desde disco         | 20,000,000   | 20,000       | 20           | Lectura secuencial de 1 megabyte desde un HDD.                        |
| Envío de paquete CA->Países Bajos->CA          | 150,000,000  | 150,000      | 150          | Tiempo de viaje de ida y vuelta para un paquete de red desde California a Países Bajos. |

Estos números, principalmente de 2012 con algunas actualizaciones, reflejan el rendimiento típico del hardware, con variaciones notadas en discusiones recientes, especialmente para SSD y redes debido a avances tecnológicos.

#### Análisis e Implicaciones
Los números de latencia no son fijos y pueden variar según el hardware y configuraciones específicas. Por ejemplo, una publicación de blog de 2020 de Ivan Pesin ([Pesin Space](http://pesin.space/posts/2020-09-22-latencies/)) señaló que las latencias de disco y red han mejorado gracias a mejores SSD (NVMe) y redes más rápidas (10/100Gb), pero las latencias centrales de la CPU como el acceso a la caché L1 permanecen estables. Esta evolución desigual resalta la importancia del contexto en el diseño de sistemas.

En la práctica, estos números guían varios aspectos:
- **Optimización del Rendimiento**: Minimizar operaciones con alta latencia, como búsquedas en disco (10 ms), puede mejorar significativamente la velocidad de la aplicación. Por ejemplo, almacenar en caché datos accedidos frecuentemente en memoria (250 us para lectura de 1 MB) en lugar de en disco puede reducir los tiempos de espera.
- **Decisiones de Compensación**: Los diseñadores de sistemas a menudo enfrentan elecciones, como usar cachés en memoria versus bases de datos. Saber que una referencia a memoria principal (100 ns) es 200 veces más rápida que una referencia a caché L1 (0.5 ns) puede informar tales decisiones.
- **Experiencia del Usuario**: En aplicaciones web, las latencias de red, como un viaje de ida y vuelta en un centro de datos (500 us), pueden afectar los tiempos de carga de la página, impactando la satisfacción del usuario. Una publicación del blog de Vercel de 2024 ([Blog de Vercel](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)) enfatizó esto para el desarrollo frontend, notando cómo las cascadas de red pueden acumular latencia.

#### Contexto Histórico y Actualizaciones
Los números originales, atribuidos a Jeff Dean y popularizados por Peter Norvig, datan de alrededor de 2010, con actualizaciones por investigadores como Colin Scott ([Latencies Interactivas](https://colin-scott.github.io/personal_website/research/interactive_latency.html)). Una publicación de Medium de 2019 por Dan Hon ([Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)) añadió latencias humorísticas pero relevantes, como reiniciar un MacBook Pro (90 segundos), ilustrando retrasos más amplios relacionados con la tecnología. Sin embargo, los números de latencia central han experimentado cambios mínimos, con el Gist de GitHub sugiriendo que permanecen "bastante similares" a partir de 2023, basándose en limitaciones físicas.

#### Conclusión y Recomendaciones
Para programadores y diseñadores de sistemas, memorizar estos números de latencia proporciona un modelo mental para la optimización del rendimiento. Deben tratarse como pautas, realizando benchmarks reales para hardware específico. Mantenerse al día con las actualizaciones, especialmente en tecnologías emergentes como la computación cuántica o redes 5G, será crucial. Recursos como el Gist de GitHub y el artículo de Medium ofrecen puntos de partida para una mayor exploración.

Este análisis, basado en el contenido probable del video y complementado con una extensa investigación en línea, subraya la relevancia perdurable de los números de latencia en la informática, con un llamado a adaptarse a los cambios tecnológicos para un diseño de sistema óptimo.

#### Citas Clave
- [Latency Numbers Every Programmer Should Know GitHub Gist](https://gist.github.com/jboner/2841832)
- [Latency Numbers Programmer Should Know YouTube Video](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [Updated Latency Numbers Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [More Numbers Every Awesome Programmer Must Know High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [Latency Numbers Every Web Developer Should Know Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [Latency Numbers Every Engineer Should Know Pesin Space Blog](http://pesin.space/posts/2020-09-22-latencies/)
- [More Latency Numbers Every Programmer Should Know Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [Numbers Every Programmer Should Know By Year Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)