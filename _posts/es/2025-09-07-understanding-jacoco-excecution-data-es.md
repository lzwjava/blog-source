---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Comprensión de los Archivos de Datos de Ejecución de JaCoCo
translated: true
type: note
---

Aquí tienes una guía práctica con todo lo que necesitas saber.

# ¿Qué es `jacoco-it.exec`?

* Es un **archivo de datos de ejecución de JaCoCo** generado durante las **pruebas de integración**.
* El "`-it`" es solo una **convención** (del objetivo *report-integration* de `jacoco-maven-plugin` y la fase Failsafe). Las pruebas unitarias suelen generar `jacoco.exec`, mientras que las pruebas de integración generan `jacoco-it.exec`.
* Puedes tener muchos archivos `.exec` (por módulo, por fase, por ejecución) y **combinarlos** después para producir un único informe de cobertura.

Configuración típica en Maven:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <!-- para pruebas unitarias -->
    <execution>
      <id>prepare-agent</id>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <!-- para pruebas de integración -->
    <execution>
      <id>prepare-agent-integration</id>
      <goals><goal>prepare-agent-integration</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-integration</goal></goals>
    </execution>
  </executions>
</plugin>
```

Esto normalmente escribe `target/jacoco.exec` (unitarias) y `target/jacoco-it.exec` (integración).

# ¿Qué hay dentro de un archivo `.exec`?

* **Solo registros de ejecución de sondas**, indexados por clase.
* Concretamente: para cada clase cargada, JaCoCo calcula un **ID** (basado en el bytecode) y almacena un **array booleano de sondas** (qué instrucciones/ramas fueron ejecutadas).
* También almacena un **id de sesión** y marcas de tiempo.
* **No contiene el bytecode de la clase, nombres de métodos, números de línea, o código fuente**. Esa información estructural viene después de tus **archivos de clase** y **fuentes** cuando ejecutas `jacoco:report` para generar el HTML/XML.

Implicaciones:

* Si tus clases cambian después de producir el `.exec`, el archivo puede dejar de coincidir (los IDs no cuadrarán). Siempre genera el informe contra **exactamente la misma compilación** de archivos de clase que produjo el exec.

# ¿Contiene información de la estructura de las clases?

* **No.** No contiene métodos, ni números de línea, ni código fuente.
* Es un **mapa de ejecución** binario y compacto por clase. El paso de generación de informes lee tus **clases compiladas** (y opcionalmente las fuentes) para mapear esas ejecuciones a paquetes, clases, métodos, líneas y ramas.

# ¿Se actualizará cuando se adjunte via `-javaagent`?

Respuesta corta: **Sí**, con detalles:

* Cuando inicias tu JVM con el agente, este instrumenta las clases **sobre la marcha** y registra las ejecuciones de las sondas **en memoria**.
* El agente **escribe** en `destfile`:

  * **Al salir de la JVM** (para `output=file`, el valor por defecto), o
  * Cuando **vacíes** explícitamente (TCP/JMX/API), o
  * Cuando `append=true` está establecido, **añadirá/combinará** con un archivo existente en lugar de sobrescribirlo.

Opciones comunes del agente:

```bash
-javaagent:/ruta/a/org.jacoco.agent.jar=\
destfile=/ruta/a/jacoco-it.exec,\
append=true,\
output=file
```

Otros modos útiles:

* `output=tcpserver` (escucha en un puerto; puedes conectarte y activar un vaciado)
* `output=tcpclient` (envía a un servidor)
* `jmx=true` (expone un MBean JMX para vaciar/reiniciar)
* Programáticamente: `org.jacoco.agent.rt.RT.getAgent().dump(/*reset*/ true|false)`

Notas sobre "actualizado":

* Con `output=file` **y** `append=true`, **cada vaciado** combina los arrays de sondas en el archivo existente (OR lógico de las ejecuciones).
* Sin `append=true`, la siguiente escritura **sobrescribe** el archivo al vaciar/salir.
* Si tienes **múltiples JVMs** (microservicios, tests bifurcados), apunta cada una a **archivos diferentes**, o usa TCP/JMX para recogerlos de forma centralizada y luego combinarlos.

# Flujos de trabajo típicos

**Fase de pruebas de integración (Failsafe):**

* Maven adjunta el agente a la(s) JVM(s) de integration-test con `destfile=target/jacoco-it.exec`.
* Al final, ejecuta `jacoco:report-integration` que lee:

  * `target/jacoco-it.exec` (ejecuciones)
  * `target/classes` (estructura)
  * `src/main/java` (opcional para las líneas de código fuente)
* Salida: Cobertura HTML/XML/CSV *solo para las pruebas de integración*.

**Combinando múltiples ejecuciones:**

```bash
# vía Maven
mvn jacoco:merge -Djacoco.destFile=target/merged.exec \
  -Djacoco.dataFileList="target/jacoco.exec,target/jacoco-it.exec,other.exec"
# luego
mvn jacoco:report -Djacoco.dataFile=target/merged.exec
```

# Problemas comunes y consejos prácticos

* **Coincidencia de compilaciones**: genera informes contra **las mismas clases compiladas** que produjeron el `.exec`.
* **Procesos paralelos**: al ejecutar tests en paralelo o en múltiples JVMs, evita muchos escritores en el mismo archivo a menos que `append=true` y estés de acuerdo con añadidos concurrentes (es más seguro usar un archivo por JVM y luego combinarlos).
* **Servicios de larga duración**: habilita **TCP/JMX** o llama a la API en tiempo de ejecución para **vaciar periódicamente**; no esperes a que termine el proceso.
* **Aislamiento de Classloader**: algunos servidores de aplicaciones cargan la misma clase dos veces; JaCoCo elimina duplicados por id de clase, pero tenlo en cuenta en contenedores complejos.
* Existe la **instrumentación offline**, pero el enfoque con **javaagent** suele ser más simple y robusto.

---

## Respuestas directas a tus preguntas

* **"¿Qué es `jacoco-it.exec`?"**
  El archivo de datos de ejecución (ejecuciones de sondas) capturado durante las **pruebas de integración**. Es solo una convención de nomenclatura; funcionalmente tiene el mismo formato que `jacoco.exec`.

* **"¿Contiene información de la estructura de las clases?"**
  **No.** Solo almacena **arrays de ejecuciones de sondas** por clase y metadatos de sesión. La información de clase/método/línea viene de tus clases compiladas/fuentes durante el paso de generación de informes.

* **"¿Se actualizará cuando se adjunte via `-javaagent`?"**
  **Sí.** Con `output=file`, el agente escribe al **salir de la JVM** o **bajo demanda** (TCP/JMX/API). Con `append=true`, **combina** con cualquier archivo existente; sin ello, lo **sobrescribe**. Para ejecuciones multi-JVM, usa archivos separados o un vaciado remoto y **combínalos** después.