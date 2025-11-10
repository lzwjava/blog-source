---
audio: false
generated: true
lang: es
layout: post
title: 'JDK 24: Características Principales y Actualizaciones'
translated: true
type: note
---

### Introducción a JDK 24

Java Development Kit (JDK) 24 es una versión de funciones de la plataforma Java SE (Standard Edition), lanzada oficialmente el 18 de marzo de 2025 como la Implementación de Referencia de la versión 24, especificada por JSR 399 en el Java Community Process. Continúa el ciclo de lanzamientos de seis meses de Oracle, ofreciendo un sólido conjunto de mejoras para aumentar la productividad de los desarrolladores, el rendimiento y la seguridad. JDK 24 incluye 24 JDK Enhancement Proposals (JEPs), la mayor cantidad de funciones desde que comenzó el programa de lanzamientos basado en el tiempo en 2018, lo que la convierte en un hito significativo en la evolución de Java. Sirve como un peldaño hacia JDK 25, la próxima versión de Soporte a Largo Plazo (LTS) programada para septiembre de 2025.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://openjdk.org/projects/jdk/24/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Estado de Soporte a Largo Plazo (LTS)

JDK 24 **no** es una versión de Soporte a Largo Plazo (LTS). Es una versión de soporte a corto plazo, que recibe solo seis meses de soporte de nivel Premier por parte de Oracle, hasta septiembre de 2025, cuando será reemplazada por JDK 25. En contraste, las versiones LTS como JDK 21 (septiembre de 2023) y la próxima JDK 25 (septiembre de 2025) reciben al menos cinco años de soporte Premier, lo que las hace preferibles para la estabilidad empresarial. La cadencia LTS de Oracle ocurre cada dos años, siendo JDK 21 la LTS más reciente y JDK 25 la siguiente.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)

### Lanzamiento y Estabilidad

JDK 24 es un **lanzamiento estable y listo para producción**, que alcanzó la Disponibilidad General (GA) el 18 de marzo de 2025. Los binarios listos para producción están disponibles desde Oracle bajo los Términos y Condiciones Sin Costo (NFTC) de Oracle y la Licencia Pública General de GNU (GPLv2) para OpenJDK, y los binarios de otros proveedores siguen shortly. El lanzamiento incluye más de 3000 correcciones de errores y mejoras más pequeñas más allá de los 24 JEPs, lo que garantiza la estabilidad para uso general. Sin embargo, al no ser una versión LTS, está dirigida principalmente a desarrolladores ansiosos por probar nuevas funciones más que a empresas que requieren estabilidad a largo plazo.[](https://openjdk.org/projects/jdk/24/)[](https://www.theregister.com/2025/03/18/oracle_jdk_24/)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)

### Nuevas Funciones en JDK 24

JDK 24 introduce 24 JEPs, categorizados en mejoras de bibliotecas principales, mejoras del lenguaje, funciones de seguridad, optimizaciones de HotSpot JVM y herramientas de Java. De estos, 14 son funciones permanentes, siete son funciones de vista previa, dos son experimentales y uno es un módulo incubador. A continuación, se presentan algunas de las funciones más notables, centrándose en las relevantes para desarrolladores y despliegues:

1.  **Stream Gatherers (JEP 485)** - Permanente
    - Mejora la Stream API introduciendo la interfaz `Gatherer`, permitiendo a los desarrolladores definir operaciones intermedias personalizadas para las canalizaciones de flujos. Esto permite transformaciones de datos más flexibles, complementando la interfaz `Collector` existente para operaciones terminales.
    - Ejemplo: Agrupar palabras por longitud usando `StreamGatherers.groupBy`.
    - Beneficio: Simplifica el procesamiento complejo de flujos para los desarrolladores.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

2.  **Ahead-of-Time Class Loading & Linking (JEP 483)** - Experimental
    - Parte de Project Leyden, esta función reduce los tiempos de inicio de las aplicaciones Java mediante la precarga y vinculación de clases en una caché durante una fase preparatoria. La caché se reutiliza en tiempo de ejecución, evitando los costosos pasos de carga de clases.
    - Beneficio: Mejora el rendimiento para aplicaciones en la nube y microservicios.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

3.  **Compact Object Headers (JEP 450)** - Experimental
    - Parte de Project Lilliput, esto reduce el tamaño de las cabeceras de los objetos Java de 96–128 bits a 64 bits en arquitecturas de 64 bits, disminuyendo el uso del montón y mejorando la eficiencia de la memoria.
    - Beneficio: Reduce la huella de memoria y mejora la localidad de los datos para un mejor rendimiento.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)[](https://www.happycoders.eu/java/java-24-features/)

4.  **Generational Shenandoah Garbage Collector (JEP 404)** - Permanente
    - Transiciona el modo generacional del GC Shenandoah de experimental a una función de producto, mejorando el rendimiento, la resistencia a picos de carga y la utilización de la memoria al dividir los objetos en generaciones jóvenes y antiguas.
    - Beneficio: Mejora el rendimiento para cargas de trabajo exigentes.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)[](https://www.infoworld.com/article/3846172/jdk-25-the-new-features-in-java-25.html)

5.  **Module Import Declarations (JEP 494)** - Segunda Vista Previa
    - Simplifica la programación modular al permitir la importación directa de todos los paquetes exportados por un módulo sin requerir un archivo `module-info.java` (ej., `import module java.sql;`).
    - Beneficio: Reduce la sobrecarga para aplicaciones ligeras y scripting, ayudando a principiantes y a la creación rápida de prototipos.[](https://codefarm0.medium.com/java-24-features-a-deep-dive-into-whats-coming-81e77382b39c)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

6.  **Flexible Constructor Bodies (JEP 492)** - Tercera Vista Previa
    - Permite declaraciones en constructores antes de las llamadas `super()` o `this()`, permitiendo que la lógica de inicialización de campos se coloque de forma más natural sin métodos auxiliares.
    - Beneficio: Mejora la confiabilidad y legibilidad del código, especialmente para la creación de subclases.[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

7.  **Key Derivation Function (KDF) API (JEP 487)** - Vista Previa
    - Introduce una API para funciones de derivación de claves criptográficas como HMAC-based Extract-and-Expand y Argon2, dando soporte al hashing seguro de contraseñas y a la interacción con hardware criptográfico.
    - Beneficio: Mejora la seguridad para aplicaciones que requieren criptografía avanzada.[](https://www.jrebel.com/blog/whats-new-java-24)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

8.  **Permanently Disable the Security Manager (JEP 486)** - Permanente
    - Elimina el Security Manager, obsoleto en JDK 17, ya que ya no es el medio principal para asegurar aplicaciones Java (reemplazado por el sandboxing basado en contenedores).
    - Nota: Las aplicaciones que dependen del Security Manager pueden requerir cambios arquitectónicos.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

9.  **Late Barrier Expansion for G1 Garbage Collector (JEP 464)** - Permanente
    - Simplifica la implementación de barreras del GC G1 al mover la expansión más tarde en la canalización de compilación, reduciendo el tiempo de compilación y mejorando la mantenibilidad.
    - Beneficio: Mejora el rendimiento para aplicaciones que usan el GC G1.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

10. **Quantum-Resistant Cryptography (JEP 452, 453)** - Vista Previa
    - Introduce Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) y Digital Signature Algorithm (ML-DSA) para proteger contra ataques de computación cuántica.
    - Beneficio: Prepara las aplicaciones Java para la seguridad post-cuántica.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)

11. **Scoped Values (JEP 480)** - Cuarta Vista Previa
    - Permite compartir datos inmutables dentro y entre hilos de forma más segura que las variables de hilo locales, mejorando el manejo de la concurrencia.
    - Beneficio: Simplifica el razonamiento sobre el código concurrente.[](https://www.jrebel.com/blog/whats-new-java-24)

12. **Deprecate 32-bit x86 Port (JEP 501)** - Permanente
    - Declara obsoleto el puerto x86 de 32 bits para su eliminación en JDK 25, siendo el puerto Zero, independiente de la arquitectura, la alternativa para sistemas de 32 bits.
    - Beneficio: Reduce la sobrecarga de mantenimiento, centrándose en arquitecturas modernas.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

13. **Vector API (JEP 489)** - Noveno Incubador
    - Continúa refinando la Vector API para la programación SIMD, con mejoras en las operaciones aritméticas y entre carriles.
    - Beneficio: Mejora el rendimiento para aplicaciones de computación intensiva.[](https://www.infoq.com/news/2025/02/java-24-so-far/)

14. **Linking Run-Time Images without JMODs (JEP 493)** - Permanente
    - Permite a la herramienta `jlink` crear imágenes de tiempo de ejecución personalizadas sin archivos JMOD, reduciendo el tamaño del JDK en ~25%.
    - Beneficio: Mejora la eficiencia del despliegue para entornos de ejecución Java personalizados.[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Notas Adicionales

-   **Funciones de Vista Previa y Experimentales**: Muchas funciones (ej., Scoped Values, KDF API) están en etapas de vista previa o experimentales, permitiendo a los desarrolladores probarlas y proporcionar comentarios antes de que se vuelvan permanentes en JDK 25 o versiones posteriores. Estas pueden cambiar antes de su finalización.[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoq.com/news/2025/02/java-24-so-far/)
-   **Integración de Proyectos**: JDK 24 introduce elementos de los Proyectos OpenJDK como Leyden (optimización de inicio), Lilliput (eficiencia de memoria) y Panama (interoperabilidad nativa), sentando las bases para futuras mejoras.[](https://bell-sw.com/blog/an-overview-of-jdk-24-features/)
-   **Seguridad y Obsolescencia**: Funciones como la eliminación del Security Manager y la obsolescencia del puerto x86 de 32 bits reflejan el enfoque de Oracle en modernizar Java mediante la eliminación progresiva de componentes obsoletos.[](https://www.azul.com/blog/six-jdk-24-features-you-should-know-about/)[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)

### Conclusión

JDK 24 es un lanzamiento estable y rico en funciones que avanza en el rendimiento, la productividad del desarrollador y la seguridad de Java. Aunque no es un lanzamiento LTS, sus 24 JEPs ofrecen mejoras significativas, muchas de las cuales se finalizarán en el próximo lanzamiento LTS, JDK 25. Los desarrolladores pueden aprovechar funciones como Stream Gatherers y Module Import Declarations para obtener ganancias inmediatas de productividad, mientras que funciones experimentales como Compact Object Headers y Ahead-of-Time Class Loading señalan la optimización continua de Java para las cargas de trabajo modernas. Para uso empresarial, se recomienda seguir con versiones LTS como JDK 21 o esperar a JDK 25 debido a su soporte extendido.[](https://www.infoworld.com/article/3491404/jdk-24-the-new-features-in-java-24.html)[](https://www.jrebel.com/blog/whats-new-java-24)[](https://www.infoworld.com/article/3830643/the-most-relevant-new-features-in-jdk-24.html)

Para más detalles, visite:
- [Notas de la versión de Oracle JDK 24](https://www.oracle.com)[](https://www.oracle.com/java/technologies/javase/24-relnote-issues.html)
- [OpenJDK JDK 24](https://openjdk.org)[](https://openjdk.org/projects/jdk/24/)
- [Conferencia JavaOne 2025](https://www.oracle.com/javaone) para resaltados de funciones[](https://www.oracle.com/news/announcement/oracle-releases-java-24-2025-03-18/)