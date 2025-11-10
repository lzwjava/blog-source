---
audio: false
generated: true
image: false
lang: es
layout: post
title: Uso y Análisis del Archivo Destino de JaCoCo
translated: true
type: note
---

Buena pregunta — desglosemos cómo funciona `destfile` de JaCoCo cuando ejecutas una aplicación Java o Spring Boot.

### 1. Qué es `destfile`

`destfile` es un parámetro del agente Java de JaCoCo (`jacocoagent.jar`) que le indica al agente **dónde escribir sus datos de ejecución**.
Por defecto, es algo como `jacoco.exec`, pero puedes establecerlo explícitamente:

```bash
-javaagent:jacocoagent.jar=destfile=/path/to/jacoco.exec
```

### 2. Qué se escribe

Cuando tu aplicación Spring Boot se ejecuta con el agente JaCoCo adjunto, el agente instrumenta el bytecode de tus clases.
Durante la ejecución, JaCoCo registra información de cobertura como:

* Qué clases y métodos se cargaron
* Qué líneas se ejecutaron
* Cobertura de ramas (si se alcanzaron ambas rutas `if`/`else`, etc.)

Estos datos de cobertura en tiempo de ejecución se almacenan en memoria y se vuelcan periódicamente al archivo definido por `destfile`.

Así que sí — la JVM, a través del agente JaCoCo, escribe información de ejecución a nivel de función y línea en ese archivo.

### 3. Cómo funciona el análisis

El archivo `.exec` en sí **no es legible para humanos**. Son solo datos binarios de cobertura.
Después de que tu aplicación termina, normalmente ejecutas una tarea de informe (por ejemplo, Maven `jacoco:report` o Gradle `jacocoTestReport`) que:

* Lee los datos del `destfile`
* Lee tus archivos `.class` compilados y el código fuente
* Genera un informe de cobertura en HTML, XML o CSV

En este paso es donde ves porcentajes, líneas de código coloreadas, etc.

### 4. Tiempo de ejecución vs. tiempo de informe

* **Tiempo de ejecución:** El agente registra la ejecución en memoria y la vuelca al `destfile`.
* **Tiempo de informe:** Usas las herramientas de JaCoCo (Maven, Gradle, CLI o Ant) para interpretar ese archivo `.exec` y generar informes legibles.

Por lo tanto, el `destfile` en sí es **solo datos de ejecución en bruto** — no se analiza hasta que ejecutas el paso del informe.

---

👉 En resumen: Sí, cuando tu aplicación Spring Boot se ejecuta con el agente JaCoCo, la información de cobertura sobre métodos y líneas se guarda en el `destfile`. Posteriormente, las herramientas de informe de JaCoCo la usan (junto con los archivos de clase/fuente) para producir informes comprensibles para humanos.

¿Quieres que también te muestre cómo funciona esto paso a paso con Spring Boot (por ejemplo, configuración de Maven + ejecución + generación de informe)?