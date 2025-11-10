---
audio: false
generated: true
lang: es
layout: post
title: Ejecutar Java Como Scripts De Python
translated: true
type: note
---

Para ejecutar el archivo `MultiMark.java` directamente, de manera similar a como ejecutas un script de Python, tienes algunas opciones. Como estás en un sistema tipo Unix (indicado por la ruta `~/projects` y el comando `ls`), proporcionaré los pasos para hacer que ejecutar el programa Java sea lo más sencillo posible. Aquí hay dos enfoques principales:

---

### **Opción 1: Ejecutar `MultiMark.java` Directamente con el Comando `java` (Java 11+)**
Desde Java 11, puedes ejecutar un único archivo fuente de Java directamente sin compilarlo explícitamente primero, lo que se siente más similar a ejecutar un script de Python.

1. **Asegúrate de que Java esté Instalado**
   Verifica si tienes Java 11 o una versión posterior instalada:
   ```bash
   java --version
   ```
   Si Java no está instalado o es una versión anterior, instala una versión compatible (por ejemplo, OpenJDK):
   ```bash
   sudo apt update
   sudo apt install openjdk-17-jdk
   ```

2. **Ejecuta el Archivo Java Directamente**
   Navega al directorio que contiene `MultiMark.java`:
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Ejecuta el archivo Java directamente usando:
   ```bash
   java MultiMark.java
   ```
   Este comando compila y ejecuta el archivo `MultiMark.java` en un solo paso. La salida (por ejemplo, núcleos de CPU, recuentos de hilos y tiempos) aparecerá en la terminal.

---

### **Opción 2: Crear un Script de Shell para Mayor Comodidad**
Para hacer que ejecutar `MultiMark.java` sea aún más similar a ejecutar un script de Python (por ejemplo, `./multimark`), puedes crear un script de shell contenedor.

1. **Crea un Script de Shell**
   Crea un archivo llamado `multimark` (sin extensión) en el directorio `scripts/benchmark`:
   ```bash
   nano ~/projects/lzwjava.github.io/scripts/benchmark/multimark
   ```
   Añade el siguiente contenido:
   ```bash
   #!/bin/bash
   java MultiMark.java
   ```
   Guarda y sal (`Ctrl+O`, `Enter`, `Ctrl+X` en nano).

2. **Haz que el Script sea Ejecutable**
   Establece los permisos de ejecución:
   ```bash
   chmod +x multimark
   ```

3. **Ejecuta el Script**
   Ahora puedes ejecutar el programa como un script de Python:
   ```bash
   ./multimark
   ```
   Esto ejecutará `java MultiMark.java` internamente.

---

### **Opción 3: Compilar y Ejecutar por Separado (Enfoque Tradicional)**
Si prefieres o necesitas compilar el archivo Java explícitamente (por ejemplo, para versiones antiguas de Java o para verificar errores de compilación), sigue estos pasos:

1. **Compila el Archivo Java**
   Navega al directorio:
   ```bash
   cd ~/projects/lzwjava.github.io/scripts/benchmark
   ```
   Compila el archivo fuente de Java:
   ```bash
   javac MultiMark.java
   ```
   Esto genera un archivo `MultiMark.class`.

2. **Ejecuta el Programa Compilado**
   Ejecuta la clase compilada:
   ```bash
   java MultiMark
   ```
   Nota: Usa `MultiMark` (sin `.java`) porque estás ejecutando el archivo de clase compilado.

---

### **Hacerlo Similar a Python**
Para que la experiencia sea lo más parecida posible a ejecutar un script de Python, la **Opción 1** (`java MultiMark.java` directo) es la más simple, ya que omita la compilación manual. La **Opción 2** (script de shell) es ideal si quieres un único comando como `./multimark` que se sienta como ejecutar `./script.py`.

### **Notas**
- **Versión de Java**: El código usa bibliotecas estándar de Java (`java.util.*` y `System.nanoTime`), por lo que debería funcionar con Java 8 o posterior. La función de ejecución directa (`java MultiMark.java`) requiere Java 11+.
- **Rendimiento**: El programa `MultiMark.java` evalúa el rendimiento de la ordenación con múltiples hilos. Ejecutarlo directamente o mediante un script no afectará su rendimiento, pero asegúrate de que tu sistema tenga suficientes recursos (CPU/memoria) para los recuentos de hilos probados (hasta 64 hilos).
- **Contexto del Directorio**: Dado que mostraste `ls scripts/benchmark/`, asumí que `MultiMark.java` está en ese directorio. Ajusta las rutas si está en otro lugar.
- **Manejo de Errores**: Si encuentras errores (por ejemplo, `java: command not found`), asegúrate de que Java esté instalado y añadido a tu `PATH`. Si el programa falla (por ejemplo, debido a límites de memoria o hilos), revisa el seguimiento de la pila (stack trace) para obtener detalles.

Si deseas integrar esto en un flujo de trabajo con tus scripts de Python (`executormark.py`, `multimark.py`, `threadmark.py`), házmelo saber y puedo sugerir formas de combinarlos (por ejemplo, llamando al programa Java desde Python).