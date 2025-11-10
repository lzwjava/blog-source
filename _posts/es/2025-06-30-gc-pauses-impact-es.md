---
audio: false
generated: true
lang: es
layout: post
title: 'Pausas del Recolector de Basura de Go: Cloudflare frente a TiDB'
translated: true
type: note
---

Sí, las pausas del recolector de basura (GC) de Go pueden afectar tanto a los servicios de Cloudflare como a la base de datos TiDB, ya que ambos aprovechan Go extensivamente en su arquitectura. Sin embargo, la naturaleza y el impacto de estas pausas, y cómo se mitigan, difieren.

Aquí hay un desglose:

**El GC de Go y sus Características:**

* **GC de Marcado y Barrido:** Go utiliza un recolector de basura concurrente de marcado y barrido de tres colores. Esto significa que la mayor parte del trabajo del GC (marcar objetos activos) ocurre de forma concurrente con la ejecución de la aplicación.
* **Pausas "Stop-the-World" (STW):** Aunque es concurrente, el GC de Go aún requiere breves pausas "stop-the-world" (STW). Estas pausas ocurren en fases específicas (como la configuración inicial del "marcado" y las fases finales de "terminación del marcado" y "terminación del barrido") donde las gorutinas de la aplicación se detienen para garantizar la consistencia de la memoria. El objetivo de los ingenieros del runtime de Go es minimizar estas duraciones STW, manteniéndolas típicamente en el rango de microsegundos.
* **Factores que influyen en el GC:** La frecuencia y duración de las pausas del GC están influenciadas por:
    * **Tasa de asignación:** La rapidez con la que la aplicación asigna nueva memoria.
    * **Tamaño del heap:** La cantidad total de memoria gestionada por el runtime de Go.
    * **`GOGC`:** Un parámetro que controla el porcentaje objetivo de recolección de basura (valor por defecto 100%). Un `GOGC` más bajo significa GCs más frecuentes.
    * **`GOMEMLIMIT`:** Un nuevo parámetro (Go 1.19+) que establece un límite superior para el tamaño objetivo del heap, ayudando a prevenir OOMs y gestionar la memoria de manera más predecible.

**Impacto en Cloudflare:**

Cloudflare utiliza Go extensivamente para muchos de sus servicios críticos, incluyendo la infraestructura DNS, el manejo de SSL, pruebas de carga y más. Para un sistema de alto rendimiento y baja latencia como Cloudflare, incluso las pausas de microsegundos pueden ser significativas.

* **Servicios sensibles a la latencia:** Los servicios que manejan altas tasas de solicitudes (como DNS o proxy) son muy sensibles a los picos de latencia. Las pausas del GC, aunque sean cortas, pueden contribuir a estos picos, afectando la experiencia del usuario.
* **Aplicaciones intensivas en memoria:** Algunos servicios de Cloudflare pueden ser intensivos en memoria, lo que lleva a ciclos de GC más frecuentes si no se ajustan adecuadamente.
* **Mitigación en Cloudflare:** Los ingenieros de Cloudflare trabajan activamente en:
    * **Ajustar `GOGC` y `GOMEMLIMIT`:** Experimentan con estos parámetros para equilibrar el uso de memoria y la frecuencia del GC.
    * **Perfilado y optimización de código:** Identifican y reducen las asignaciones de memoria innecesarias en su código Go.
    * **Optimizaciones Guiadas por Perfil (PGO):** Cloudflare ha visto ahorros significativos de CPU (y por lo tanto probablemente una reducción de la presión del GC) aprovechando la función PGO de Go.
    * **Consideraciones arquitectónicas:** Diseñan servicios para que sean resistentes a pausas cortas, potencialmente teniendo suficiente redundancia o procesando solicitudes de una manera que minimice el impacto de la pausa de una sola gorutina.

**Impacto en la Base de Datos TiDB:**

TiDB es una base de datos SQL distribuida construida por PingCAP, con su capa SQL (`tidb-server`) escrita principalmente en Go. Como base de datos, tiene características y requisitos de rendimiento diferentes en comparación con un servicio proxy.

* **GC específico de la base de datos:** TiDB tiene sus propios mecanismos de recolección de basura para datos MVCC (Control de Concurrencia Multi-Versión) (limpiando versiones antiguas de datos en TiKV, su motor de almacenamiento). Esto es distinto del GC del runtime de Go, aunque el "coordinador" de TiDB (escrito en Go) inicia y gestiona este proceso.
* **GC del Runtime de Go en TiDB:** El GC de Go *sí* impacta a TiDB porque `tidb-server` procesa solicitudes SQL, gestiona memoria para planes de consulta, resultados y otros datos del runtime.
    * **Variabilidad de la latencia:** Las pausas STW frecuentes pueden provocar picos de latencia en la ejecución de consultas, afectando la capacidad de respuesta de la base de datos.
    * **Sobrecarga de CPU:** La actividad del GC consume recursos de CPU, que de otro modo podrían usarse para procesar consultas.
    * **Activación adaptativa del GC:** TiDB activa proactivamente el GC de Go cuando el uso de memoria alcanza un cierto umbral (configurable mediante `tidb_server_memory_limit` y `tidb_server_memory_limit_gc_trigger`). También utiliza una estrategia adaptativa para `tidb_server_memory_limit_gc_trigger` para evitar GCs excesivamente frecuentes.
* **Monitoreo y Ajuste:** PingCAP proporciona herramientas extensivas de monitoreo (como el TiDB Runtime Dashboard) para observar el comportamiento del GC de Go (frecuencia del GC, duración, latencia STW, tiempo de CPU dedicado al GC) y permite a los usuarios configurar `GOGC` y `GOMEMLIMIT` para optimizar el rendimiento.
* **Esfuerzos continuos:** Los ingenieros de PingCAP trabajan continuamente en optimizar la gestión de memoria de Go en TiDB y el comportamiento del GC para minimizar su impacto en el rendimiento y la estabilidad.

**En resumen:**

Tanto Cloudflare como TiDB, al ser sistemas de alto rendimiento que dependen de Go, son susceptibles a los impactos de las pausas del GC de Go. Aunque el GC de Go está altamente optimizado para duraciones STW cortas, a escala, estas pausas pueden contribuir a picos de latencia y sobrecarga de CPU. Ambas empresas monitorean, ajustan y optimizan activamente sus aplicaciones e infraestructura en Go para mitigar estos efectos, aprovechando los parámetros del runtime de Go y sus propios diseños arquitectónicos específicos.