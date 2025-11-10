---
audio: false
generated: true
lang: es
layout: post
title: Ubicación de la instalación de OpenJDK 21.0.7 en Ubuntu 22.04
translated: true
type: note
---

El comando `java --version` que ejecutaste muestra que tienes OpenJDK 21.0.7 instalado en tu sistema, específicamente la versión empaquetada para Ubuntu 22.04. Esta salida confirma que el Java Development Kit (JDK) está instalado y es accesible desde tu línea de comandos.

La ubicación de la instalación de Java normalmente se puede encontrar verificando dónde está ubicado el binario `java`. Dado que estás en un sistema basado en Ubuntu, es probable que OpenJDK esté instalado en un directorio estándar del sistema, como `/usr/lib/jvm/`.

Para localizar la ruta exacta de la instalación de Java:

1. **Encuentra la ruta del binario `java`**:
   Ejecuta el siguiente comando en tu terminal:
   ```bash
   which java
   ```
   Esto probablemente mostrará algo como `/usr/bin/java`. Este es un enlace simbólico al binario real de Java.

2. **Sigue el enlace simbólico hasta la ubicación real**:
   Dado que `/usr/bin/java` suele ser un enlace simbólico, puedes encontrar el directorio de instalación real ejecutando:
   ```bash
   readlink -f $(which java)
   ```
   Esto podría mostrar algo como `/usr/lib/jvm/java-21-openjdk-amd64/bin/java`, lo que indica que el JDK está instalado en `/usr/lib/jvm/java-21-openjdk-amd64/`.

3. **Verifica el directorio de instalación**:
   Puedes listar el contenido del directorio JVM para confirmar:
   ```bash
   ls /usr/lib/jvm/
   ```
   Deberías ver un directorio como `java-21-openjdk-amd64` o similar, que contiene la instalación de OpenJDK.

### Resumen
Tu instalación de Java probablemente esté ubicada en `/usr/lib/jvm/java-21-openjdk-amd64/` (o un directorio similar bajo `/usr/lib/jvm/`). El comando `java` que ejecutaste es un enlace simbólico que apunta al binario `java` dentro de este directorio. Si deseas confirmar la ruta exacta, usa el comando `readlink -f $(which java)`.