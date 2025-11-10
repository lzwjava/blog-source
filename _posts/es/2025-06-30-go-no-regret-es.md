---
audio: false
generated: true
lang: es
layout: post
title: PingCAP y Cloudflare elogian a Go
translated: true
type: note
---

Ni PingCAP ni Cloudflare han expresado "arrepentimiento" por usar Go. De hecho, ambas empresas han elogiado públicamente a Go por sus fortalezas y continúan usándolo extensamente en sus productos principales. Sin embargo, también son pragmáticas sobre las elecciones de lenguaje y usan otros lenguajes donde son más adecuados para problemas específicos.

Aquí hay un desglose:

### PingCAP (TiDB) y Go

*   **Sin Arrepentimiento:** PingCAP eligió Go para la capa SQL (`tidb-server`) de TiDB debido a su excelente modelo de concurrencia (goroutines y channels), facilidad de desarrollo y sólida biblioteca estándar. Estas características les permitieron construir una base de datos distribuida compleja relativamente rápido.
*   **Desafíos Reconocidos:** Si bien Go es central para TiDB, PingCAP es muy transparente sobre los desafíos, particularmente en lo que respecta al recolector de basura de Go. Su documentación y publicaciones de blog discuten frecuentemente:
    *   **Pausas del GC:** Reconocen que las pausas del GC, incluso si son cortas, pueden introducir variabilidad de latencia en una base de datos de alto rendimiento. Trabajan activamente para mitigar esto mediante el ajuste de `GOGC`, `GOMEMLIMIT` y la implementación de activación de GC adaptativa.
    *   **Gestión de Memoria:** Proporcionan guías detalladas sobre cómo monitorear el uso de memoria y solucionar problemas de OOM, reconociendo que los patrones de memoria ineficientes en Go pueden llevar a problemas.
*   **Uso Estratégico de Rust:** PingCAP eligió **Rust** para TiKV, su motor de almacenamiento distribuido clave-valor. Esto no fue un "arrepentimiento" de Go, sino más bien una **decisión estratégica** para la capa de almacenamiento donde el rendimiento extremadamente bajo de latencia, predecible y el control de memoria fino son primordiales.
    *   El modelo de propiedad y préstamo de Rust, junto con la ausencia de un recolector de basura, son ideales para la programación a nivel de sistemas donde cada microsegundo y cada byte importan.
    *   Reconocieron que la compensación de la curva de aprendizaje más pronunciada y los tiempos de compilación más lentos de Rust era aceptable para el motor de almacenamiento crítico, pero menos deseable para la capa SQL de evolución más rápida.
*   **Conclusión para PingCAP:** Claramente ven a Go y Rust como herramientas complementarias. Go para la lógica de alto nivel y la iteración rápida, Rust para los componentes críticos de bajo nivel y rendimiento.

### Cloudflare y Go

*   **Adopción Extensiva de Go:** Cloudflare fue un adoptante temprano y entusiasta de Go. Utilizan Go para una gran variedad de sus servicios, incluyendo infraestructura DNS, manejo de SSL, herramientas de prueba de carga y muchos sistemas internos. Han hablado consistentemente de forma positiva sobre la concurrencia de Go, la facilidad de implementación y la productividad del desarrollador.
*   **Evolución, No Arrepentimiento:** Cloudflare ciertamente ha diversificado su uso de lenguajes, con un cambio notable hacia **Rust** en ciertas áreas críticas. Esto está impulsado por necesidades de rendimiento, seguridad y eficiencia de recursos, no por un "arrepentimiento" de Go.
    *   **Pingora (Rust):** Un ejemplo principal es el desarrollo por parte de Cloudflare de **Pingora**, un nuevo proxy HTTP construido en Rust para reemplazar partes de su infraestructura NGINX (que estaba escrita en C). Este cambio a Rust se debió en gran parte a:
        *   **Seguridad de Memoria:** Las garantías de Rust contra errores comunes de memoria (desbordamientos de búfer, uso después de la liberación) que son frecuentes en C/C++ (como en NGINX). Esto mejora significativamente la seguridad y la estabilidad.
        *   **Rendimiento Extremo:** Para un componente central que maneja billones de solicitudes, las "abstracciones de costo cero" y el control fino de Rust permiten un rendimiento aún mayor y un menor consumo de recursos que lo que es fácilmente alcanzable en Go (debido a la sobrecarga del GC de Go).
        *   **Experiencia Mejorada del Desarrollador para Programación de Sistemas:** Si bien Rust tiene una curva de aprendizaje más pronunciada inicialmente, para los ingenieros de sistemas que trabajan en componentes de red extremadamente de bajo nivel, su rigor y sistema de tipos potente pueden conducir a código más robusto y fácil de razonar a largo plazo.
    *   **Go sigue siendo fuerte:** Incluso con Pingora, Cloudflare continúa desarrollando y manteniendo muchos servicios en Go. Ven a Go como "lo suficientemente rápido" para la mayoría de sus cargas de trabajo y aprecian su velocidad de desarrollo y simplicidad operativa.
*   **Conclusión para Cloudflare:** Cloudflare adopta una estrategia multilingüe, eligiendo la mejor herramienta para el trabajo. Go sigue siendo un lenguaje fundamental para ellos, particularmente para servicios que se benefician de su desarrollo rápido y concurrencia. Rust se usa cada vez más para componentes a nivel de sistemas donde el rendimiento máximo, la seguridad de la memoria y el control fino son primordiales.

En esencia, ambas empresas son organizaciones de ingeniería sofisticadas que comprenden las compensaciones de los diferentes lenguajes de programación. No expresan "arrepentimiento" por elegir Go, sino que demuestran un enfoque pragmático para usar otros lenguajes como Rust para dominios problemáticos específicos donde sus fortalezas (por ejemplo, falta de GC, seguridad de memoria) ofrecen ventajas significativas para la infraestructura crítica.