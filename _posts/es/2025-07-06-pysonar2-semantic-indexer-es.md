---
audio: false
generated: true
lang: es
layout: post
title: 'PySonar2: Indexador Semántico de Python'
translated: true
type: note
---

PySonar2 es un indexador semántico para Python, desarrollado por yinwang0, que utiliza inferencia de tipos interprocedural para analizar grandes bases de código Python. Está diseñado para procesamiento por lotes, lo que lo hace adecuado para crear índices para navegadores de código y motores de búsqueda, en lugar de para Entornos de Desarrollo Integrado (IDEs) en tiempo real. Su enfoque principal es la precisión a través de la inferencia de tipos, que pretende describir cómo se usa realmente el código.

**Características y Funcionalidades Clave:**

*   **Indexación Semántica:** La función principal de PySonar2 es construir un índice semántico del código Python, permitiendo capacidades avanzadas de navegación y búsqueda de código.
*   **Inferencia de Tipos Interprocedural:** Emplea una inferencia de tipos interprocedural sofisticada para comprender el flujo y el uso de los tipos en toda una base de código, lo que contribuye a su precisión.
*   **Procesamiento por Lotes:** Optimizado para procesar grandes proyectos de manera por lotes, en contraste con las herramientas de análisis en tiempo real.
*   **Librería para Herramientas de Desarrollo:** PySonar2 está concebido como una librería fundamental para otras herramientas de desarrollo, no como una aplicación de usuario final independiente.
*   **Licencia Apache-2.0:** El proyecto es de código abierto bajo la licencia Apache-2.0, lo que permite su uso, modificación y distribución gratuitos.

**Adopción y Uso:**

PySonar2 ha tenido una adopción significativa en la industria, destacándose como motor de indexación para:

*   La Búsqueda de Código interna de Google
*   sourcegraph.com
*   insight.io

**Detalles Técnicos:**

*   **Lenguajes:** El repositorio está escrito predominantemente en Java (94.4%), usando Python (5.1%) para el objetivo de análisis.
*   **Sistema de Construcción:** Utiliza Maven para la construcción. Para compilar el proyecto, ejecuta `mvn package -DskipTests`.
*   **Demo:** Hay una demo disponible para construir un navegador de código simple para la librería estándar de Python 2.7 usando un comando de Java.
*   **Requisitos del Sistema:** Requiere Python 2.7.x o 3.x, Java 8+ y Maven. La configuración correcta de las variables de entorno `PATH` y `PYTHONPATH` es crucial.
*   **Pruebas:** Las pruebas unitarias se pueden ejecutar con `mvn test`. Las nuevas pruebas implican crear código Python en directorios que terminen con ".test" dentro del directorio `tests`.

**Estado del Repositorio:**

El repositorio ha ganado una atención considerable, evidenciada por:

*   **1.4k estrellas**
*   **506 forks**

Los commits recientes indican mantenimiento continuo, incluyendo actualizaciones del README y la versión, y correcciones de code smells.

**Contribuciones:**

Las contribuciones son bienvenidas, aunque se recomienda discutir cambios significativos con el mantenedor debido a la compleja teoría subyacente del proyecto.

Para más detalles, puedes visitar el [Repositorio de GitHub de PySonar2](https://github.com/yinwang0/pysonar2).