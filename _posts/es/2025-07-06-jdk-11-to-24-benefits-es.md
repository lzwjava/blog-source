---
audio: false
generated: true
lang: es
layout: post
title: Beneficios de la actualización a JDK 24 explicados
translated: true
type: note
---

Actualizar de JDK 11 a JDK 24 ofrece beneficios significativos en varios aspectos, incluyendo rendimiento, nuevas características y seguridad. Aquí hay un desglose:

**1. Mejoras de Rendimiento:**

*   **Hilos Virtuales (Project Loom):** Aunque se introdujeron en JDK 21, JDK 24 refina aún más los hilos virtuales (JEP 491: Synchronize Virtual Threads Without Pinning). Esto es un cambio radical para aplicaciones de alta concurrencia, permitiendo millones de hilos ligeros sin la sobrecarga de los hilos de plataforma tradicionales. Esto puede mejorar drásticamente la escalabilidad y la capacidad de respuesta, especialmente para aplicaciones del lado del servidor.
*   **Arranque Más Rápido:** JDK 24 incluye "Carga y Enlace de Clases Anticipado (Ahead-of-Time)" (JEP 483), que hace que las clases de la aplicación estén disponibles instantáneamente cuando se inicia la JVM, reduciendo los tiempos de arranque. Esto es especialmente beneficioso para microservicios y aplicaciones nativas de la nube donde un arranque rápido es crucial.
*   **Cabeceras de Objetos Compactas (Experimental):** JEP 450 tiene como objetivo reducir el tamaño de las cabeceras de los objetos en arquitecturas de 64 bits, lo que puede generar ahorros significativos de memoria (10-20%) y una mejor localidad de caché, especialmente para aplicaciones con muchos objetos pequeños.
*   **Modo Generacional de ZGC (Por Defecto):** El Recolector de Basura Z (ZGC) ahora tiene por defecto un modo generacional (JEP 490), optimizando la recolección de basura para objetos de corta duración. Esto puede conducir a tiempos de pausa reducidos y a una mejor eficiencia de memoria para montones (heaps) grandes.
*   **Stream Gatherers (JEP 485):** Esta nueva API permite operaciones intermedias personalizadas en las canalizaciones de Stream, proporcionando más flexibilidad y transformaciones de datos potencialmente más eficientes.
*   **Operaciones Masivas Optimizadas en la API de Función y Memoria Externa:** Las operaciones de memoria masivas ahora utilizan código Java en lugar de métodos nativos, lo que conduce a un rendimiento más rápido en ciertas arquitecturas (por ejemplo, Linux x64/AArch64), especialmente para tamaños de datos más pequeños.
*   **Impulso en el Arranque de la Concatenación de Cadenas:** Las optimizaciones internas en la concatenación de cadenas conducen a un arranque más rápido y menos sobrecarga en la generación de código.

**2. Nuevas Características del Lenguaje y APIs:**

*   **Mejoras en la Coincidencia de Patrones (Pattern Matching) (JEP 488):** Mejoras adicionales en la coincidencia de patrones, permitiendo tipos primitivos en los patrones y extendiendo `instanceof` y `switch` para trabajar con todos los tipos primitivos, haciendo el código más conciso y legible.
*   **Valores de Alcance (Scoped Values) (JEP 487):** Una API en vista previa que proporciona una forma más segura y eficiente de compartir datos inmutables dentro de un hilo y con hilos hijos, especialmente beneficioso con hilos virtuales.
*   **Concurrencia Estructurada (Structured Concurrency) (JEP 499):** Una API en vista previa que simplifica la programación concurrente al tratar grupos de tareas relacionadas como una sola unidad, mejorando el manejo de errores, la cancelación y la observabilidad.
*   **API de Archivos de Clase (Class-File API) (JEP 484):** Una API estándar para analizar, generar y transformar archivos de clase de Java.
*   **API Vectorial (Vector API) (JEP 489):** (Todavía en incubadora) Esta API permite expresar cálculos vectoriales que se compilan en instrucciones vectoriales óptimas en las CPU compatibles, lo que conduce a un rendimiento superior para ciertas operaciones numéricas.
*   **API de Función de Derivación de Claves (Key Derivation Function API) (JEP 478):** Una API en vista previa para algoritmos criptográficos utilizados para derivar claves adicionales a partir de una clave secreta.

**3. Mejoras de Seguridad:**

*   **Criptografía Resistente a la Computación Cuántica:** JDK 24 introduce implementaciones del Mecanismo de Encapsulación de Claves Basado en Módulo-Retículo (ML-KEM) (JEP 496) y del Algoritmo de Firma Digital Basado en Módulo-Retículo (ML-DSA) (JEP 497), resistentes a la computación cuántica, preparando a Java para los futuros desafíos criptográficos.
*   **Mejoras en TLS:** Mejoras como el recuento configurable de nuevos tickets de sesión para TLSv1.3 y un mecanismo para deshabilitar suites de cifrado TLS mediante coincidencia de patrones. Las suites de cifrado TLS_RSA ahora están deshabilitadas por defecto para una mejor secreto forward (forward secrecy).
*   **Eliminación del Security Manager (JEP 486):** El Security Manager, una característica heredada, está permanentemente deshabilitado. Esto simplifica el modelo de seguridad de la JVM y fomenta el uso de prácticas de seguridad modernas como la contención basada en contenedores.
*   **Advertencias para `sun.misc.Unsafe`:** JDK 24 emite advertencias en tiempo de ejecución cuando se utilizan los métodos de acceso a memoria en `sun.misc.Unsafe`, fomentando la migración a alternativas más seguras como la API VarHandle y la API de Función y Memoria Externa.

**4. Desaprobaciones y Eliminaciones:**

*   Si bien estos podrían requerir cambios en el código, contribuyen a una plataforma más limpia, segura y mantenible. La deshabilitación permanente del Security Manager y las advertencias para `sun.misc.Unsafe` son ejemplos de esto.

**5. Consideraciones de Soporte a Largo Plazo (LTS):**

*   JDK 11 es una versión LTS, con soporte extendido de Oracle disponible hasta enero de 2032.
*   JDK 24 *no* es una versión LTS. La próxima versión LTS después de JDK 21 está planificada para ser JDK 25 en septiembre de 2025.
*   Esto significa que si actualiza a JDK 24, necesitará planificar otra actualización a JDK 25 (o una LTS posterior) relativamente pronto para garantizar soporte a largo plazo continuo y actualizaciones de seguridad.

**En resumen:**

Actualizar a JDK 24 desde JDK 11 ofrece una gran cantidad de características nuevas, ganancias significativas de rendimiento (especialmente con hilos virtuales y un arranque más rápido) y mejoras de seguridad cruciales. Sin embargo, es importante considerar el ciclo de vida del soporte, ya que JDK 24 es una versión no LTS, lo que significa que será necesaria una actualización posterior a JDK 25 (la próxima LTS) para la estabilidad y el soporte a largo plazo.