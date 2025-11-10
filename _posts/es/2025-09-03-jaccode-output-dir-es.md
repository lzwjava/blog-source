---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración del Directorio de Salida del Agente JaCoCo
translated: true
type: note
---

Sí — exactamente 👍.

Por defecto, si escribes

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

entonces `jacoco.exec` se crea en el **directorio de trabajo actual** del proceso de la JVM (a menudo la raíz del servidor o desde donde hayas lanzado Liberty).

Si quieres controlar dónde se guarda, debes proporcionar una **ruta absoluta o relativa**, por ejemplo:

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=/opt/coverage-data/jacoco.exec,output=file
```

o

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=target/jacoco.exec,output=file
```

(donde `target/` es relativo al directorio de inicio).

Así que sí, si quieres garantizar dónde termina el archivo `.exec`, usa la ruta completa.

👉 Consejo: Es común en proyectos de Maven/Gradle apuntarlo a `target/` (Maven) o `build/` (Gradle), para que luego los plugins de informes puedan recogerlo automáticamente.

¿Quieres que te muestre un ejemplo de `jvm.options` de Liberty con la ruta completa configurada?