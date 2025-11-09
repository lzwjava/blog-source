---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Archivo de Cobertura JaCoCo y Modo de Anexar
translated: true
type: note
---

Ese es un detalle sutil pero importante sobre cómo funciona JaCoCo.

### Comportamiento de `jacoco:prepare-agent`

* Cuando Maven ejecuta el objetivo **`prepare-agent`**, en realidad no genera el archivo de cobertura inmediatamente.
* En su lugar, **configura la JVM** (normalmente mediante un argumento `-javaagent:jacocoagent.jar`) para que los datos de cobertura se recopilen mientras se ejecutan tus pruebas o aplicación.
* La ubicación del archivo `.exec` la controla la propiedad `jacoco.destFile` (el valor predeterminado es `target/jacoco.exec`, pero a menudo se personaliza, por ejemplo, `target/jacoco-it.exec`).

### ¿Qué sucede si el archivo ya existe?

* Por defecto, **JaCoCo sobrescribirá el archivo** cuando la JVM se inicie con el agente.
* Esto significa que cada ejecución de `prepare-agent` → ejecución de pruebas producirá un archivo `.exec` *nuevo*.
* No anexa automáticamente: los datos antiguos se pierden a menos que lo configures de otra manera.

### Cómo anexar en su lugar

Si deseas que múltiples ejecuciones se acumulen en el mismo archivo exec, debes habilitar explícitamente el modo de anexar:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <configuration>
    <destFile>${project.build.directory}/jacoco-it.exec</destFile>
    <append>true</append>   <!-- ✅ anexar datos de cobertura -->
  </configuration>
</plugin>
```

Con `<append>true>`, si el archivo existe, los nuevos datos de cobertura se fusionarán en él.

### En resumen

* **Por defecto:** Cada ejecución reemplaza el `.exec` antiguo.
* **Con `append=true`:** La cobertura de múltiples ejecuciones de JVM (o de múltiples módulos/pruebas) se fusiona en el mismo archivo.

---

¿Quieres que también explique cómo interactúa esto con **construcciones de Maven multi-módulo** (donde cada módulo puede intentar escribir su propio exec de JaCoCo), ya que esa es a menudo la razón por la que la gente se encuentra con problemas de sobrescritura vs anexado?