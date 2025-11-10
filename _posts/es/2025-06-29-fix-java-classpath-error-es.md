---
audio: false
generated: true
lang: es
layout: post
title: Corregir Error de Classpath en Java
translated: true
type: note
---

El error que encontraste (`Could not find or load main class scripts.benchmark.MultiMark`) ocurre porque intentaste ejecutar el programa Java desde el directorio raíz del proyecto (`~/projects/lzwjava.github.io`) usando el nombre completo de la clase (`scripts.benchmark.MultiMark`), pero el runtime de Java espera que la clase se ejecute desde el directorio donde comienza la estructura del paquete, o necesitas especificar el classpath correctamente. Cuando cambiaste al directorio `scripts/benchmark` y ejecutaste `java MultiMark`, funcionó porque la clase estaba en el directorio correcto relativo al comando.

Para ejecutar `MultiMark.java` o `MultiMark.class` desde el directorio raíz del proyecto (`~/projects/lzwjava.github.io`) sin cambiar de directorio, puedes usar la opción `-cp` (classpath) con el comando `java` para indicarle a Java dónde encontrar el archivo de clase compilado. Aquí hay dos formas de lograrlo, manteniéndote en el directorio raíz:

---

### **Opción 1: Ejecutar la Clase Compilada con Classpath**
Si `MultiMark.class` ya existe en `scripts/benchmark/` (como se muestra en la salida de tu `ls`), puedes ejecutarlo desde el directorio raíz especificando el classpath.

1. **Permanece en el Directorio Raíz**
   Asegúrate de estar en `~/projects/lzwjava.github.io`.

2. **Ejecuta el Programa**
   Usa la opción `-cp` para apuntar al directorio que contiene el archivo de clase:
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` le dice a Java que busque clases en el directorio `scripts/benchmark`.
   - `MultiMark` es el nombre de la clase (sin el prefijo `.class` o del paquete, ya que `MultiMark.java` no tiene una declaración `package`).

   Esto debería producir una salida como:
   ```
   CPU cores: 32
   ...
   ```

3. **Nota**: Si `MultiMark.class` está desactualizado o falta, compila primero el archivo fuente desde el directorio raíz:
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   Luego ejecuta el comando anterior.

---

### **Opción 2: Ejecutar el Archivo Fuente Directamente con Classpath (Java 11+)**
Si prefieres ejecutar el archivo fuente directamente (como `python script.py`), puedes usar el comando `java` con la ruta del archivo fuente, especificando el classpath.

1. **Permanece en el Directorio Raíz**
   Asegúrate de estar en `~/projects/lzwjava.github.io`.

2. **Ejecuta el Archivo Fuente**
   Usa:
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` establece el classpath al directorio que contiene el fuente.
   - `scripts/benchmark/MultiMark.java` especifica el archivo fuente a compilar y ejecutar.

   Esto compila y ejecuta `MultiMark.java` en un solo paso, produciendo la misma salida que antes.

---

### **Opción 3: Crear un Shell Script en el Directorio Raíz**
Para hacerlo aún más conveniente (como ejecutar `./multimark` desde el directorio raíz), puedes crear un shell script en el directorio raíz (`~/projects/lzwjava.github.io`).

1. **Crea un Shell Script**
   Crea un archivo llamado `multimark` en el directorio raíz:
   ```bash
   nano multimark
   ```
   Añade:
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   Guarda y sal.

2. **Hazlo Ejecutable**
   ```bash
   chmod +x multimark
   ```

3. **Ejecuta el Script**
   Desde el directorio raíz:
   ```bash
   ./multimark
   ```
   Esto ejecuta el programa Java sin necesidad de cambiar de directorios.

4. **Opcional: Compilar en el Script**
   Si quieres que el script maneje la compilación (por ejemplo, si el archivo fuente cambia), modifica el script:
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **Notas Clave**
- **Classpath (`-cp`)**: La opción `-cp` le dice a Java dónde encontrar clases o archivos fuente. Dado que `MultiMark.java` no tiene una declaración `package`, el nombre de la clase es simplemente `MultiMark`, no `scripts.benchmark.MultiMark`. Si tuviera una línea `package scripts.benchmark;`, necesitarías usar `java -cp . scripts.benchmark.MultiMark` desde la raíz.
- **Versión de Java**: La ejecución de archivo fuente (`java scripts/benchmark/MultiMark.java`) requiere Java 11 o superior. Tu sistema parece tener Java instalado, ya que funcionó desde el directorio `scripts/benchmark`.
- **Directorio**: Estas soluciones te mantienen en el directorio raíz (`~/projects/lzwjava.github.io`), coincidiendo con tu preferencia.
- **Automatización**: El shell script (Opción 3) es lo más cercano a una experiencia tipo Python, ya que puedes ejecutar `./multimark` como un script de Python. También podrías añadirlo a tu `PATH` para acceso global, pero eso es opcional.
- **Manejo de Errores**: Si obtienes errores como `NoClassDefFoundError`, asegúrate de que `MultiMark.class` exista en `scripts/benchmark/` o recompila. Si no se encuentra Java, verifica la instalación (`java --version`).

Si quieres integrar esto con tus scripts de Python o necesitas un flujo de trabajo específico (por ejemplo, ejecutar `multimark.py` y `MultiMark.java` juntos), ¡avísame!