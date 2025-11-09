---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Apache DataFusion Comet Acelera Spark
translated: true
type: note
---

### Apache DataFusion Comet

Apache DataFusion Comet es un proyecto de código abierto bajo la Apache Software Foundation que funciona como un acelerador de alto rendimiento para Apache Spark. Está construido sobre el motor de consultas Apache DataFusion y tiene como objetivo mejorar el rendimiento de las cargas de trabajo de Spark—como un procesamiento de datos más rápido y una obtención de insights más rápida—mientras se ejecuta en hardware estándar. No se requieren cambios en el código para la integración, y también acelera las operaciones de Apache Iceberg que implican escaneos de Parquet desde Spark.

#### Características Principales
- **Mejoras de Rendimiento**: Ofrece aceleraciones significativas para las consultas. Por ejemplo, los benchmarks en 22 consultas TPC-H con 100 GB de datos Parquet muestran una mejora general de 2.2x (de 687 segundos a 302 segundos en un único ejecutor de 8 núcleos). También hay benchmarks TPC-DS disponibles, con resultados reproducibles a través de las guías del proyecto.
- **Eficiencia de Hardware**: Funciona con hardware estándar, evitando la necesidad de GPUs o FPGAs costosas.
- **Compatibilidad Transparente**: Totalmente compatible con las versiones soportadas de Apache Spark, garantizando una integración directa en configuraciones existentes.
- **Integración Estrecha con DataFusion**: Aprovecha el motor de ejecución de DataFusion para una eficiencia optimizada.
- **Impulsado por la Comunidad**: Bajo la licencia Apache License 2.0, con una comunidad activa para contribuciones, incluyendo corrección de errores, nuevas funcionalidades y documentación.

El proyecto se mantiene activamente, con recursos para comenzar, guías para contribuyentes y canales comunitarios como Slack y Discord.

Para más detalles, incluyendo la instalación (a través de la documentación en datafusion.apache.org) y benchmarking, consulta el repositorio.

[Repositorio GitHub de Apache DataFusion Comet](https://github.com/apache/datafusion-comet)