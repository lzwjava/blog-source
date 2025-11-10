---
audio: false
generated: true
image: false
lang: es
layout: post
title: Opciones de la JVM Guía Rápida por Categorías
translated: true
type: note
---

En el mundo de la JVM, existen **muchas opciones** que puedes configurar, y el conjunto exacto depende de la implementación de la JVM (HotSpot, OpenJ9, GraalVM, etc.) y de la versión. En términos generales, las opciones de la JVM se clasifican en estas categorías:

---

## 1. Opciones Estándar

Son opciones estables, compatibles entre versiones, documentadas oficialmente y garantizadas para funcionar. Ejemplos:

* `-classpath` / `-cp` → especificar el classpath.
* `-Dproperty=valor` → establecer propiedades del sistema.
* `-version` → imprimir la versión de la JVM.
* `-Xms` / `-Xmx` → tamaño inicial y máximo del heap.
* `-ea` → habilitar aserciones.

---

## 2. Opciones No Estándar (`-X`)

Son específicas de la JVM y no se garantiza que permanezcan estables. Ejemplos (HotSpot):

* `-Xint` → solo interpretar (sin JIT).
* `-Xcomp` → compilar todos los métodos en su primer uso.
* `-Xbatch` → deshabilitar la compilación en segundo plano.
* `-Xss512k` → establecer el tamaño de la pila del hilo.

---

## 3. Opciones Avanzadas (`-XX`)

Proporcionan ajustes de grano fino para el GC, JIT y el comportamiento en tiempo de ejecución. Ejemplos:

* `-XX:+UseG1GC` → habilitar el recolector de basura G1.
* `-XX:+PrintGCDetails` → registrar la actividad del GC.
* `-XX:MaxMetaspaceSize=256m` → limitar el metaspace.
* `-XX:+HeapDumpOnOutOfMemoryError` → volcar el heap cuando ocurre un OOM.
* `-XX:+UnlockExperimentalVMOptions` → permitir flags experimentales.
* `-XX:+UseStringDeduplication` → reducir el uso de memoria mediante la deduplicación de strings.

---

## 4. Diagnóstico y Experimentales

Algunos flags están ocultos y requieren ser desbloqueados:

* `-XX:+UnlockDiagnosticVMOptions` → habilitar flags de diagnóstico.
* `-XX:+UnlockExperimentalVMOptions` → permitir ajustes experimentales.

Luego puedes usar opciones como:

* `-XX:+PrintFlagsFinal` → listar todas las opciones de la JVM y sus valores.
* `-XX:+LogCompilation` → registrar la actividad del compilador JIT.

---

## 5. Herramientas para Trabajar con Opciones de la JVM

* **`java -X`** → lista las opciones no estándar para tu compilación de la JVM.
* **`java -XX:+PrintFlagsFinal`** → imprime todas las opciones reconocidas con sus valores por defecto y actuales.
* **`jcmd <pid> VM.flags`** → muestra los flags de la JVM para un proceso en ejecución.
* **`jcmd <pid> VM.uptime`**, `jcmd <pid> VM.system_properties` → inspección en tiempo de ejecución.
* **`jps` + `jinfo`** → listar procesos Java e imprimir opciones de la JVM.
* **VisualVM / JConsole** → monitorear heap, GC y parámetros de tiempo de ejecución.

---

👉 Una forma práctica de explorar tu entorno es ejecutar:

```bash
java -XX:+PrintFlagsFinal | grep GC
```

para ver todas las opciones relacionadas con GC, o simplemente:

```bash
java -X
```

para consultar los flags no estándar disponibles.

---

¿Te gustaría que te proporcione una **hoja de referencia categorizada de las opciones de la JVM más útiles** (GC, memoria, depuración, ajuste de rendimiento) para que no tengas que analizar la enorme lista de `PrintFlagsFinal`?