---
audio: false
generated: true
lang: es
layout: post
title: 'Primeros Pasos con JShell: Una Guía Rápida'
translated: true
type: note
---

JShell es una herramienta interactiva REPL (Read-Eval-Print Loop) incluida en el Java Development Kit (JDK) a partir de JDK 9. Te permite ejecutar fragmentos de código Java de forma interactiva sin necesidad de escribir un programa completo. A continuación, tienes una guía concisa sobre cómo usar JShell:

### 1. **Iniciar JShell**
- **Asegúrate de que JDK esté instalado**: Asegúrate de tener JDK 9 o posterior instalado. Puedes verificarlo ejecutando `java -version` en tu terminal o símbolo del sistema.
- **Lanzar JShell**:
  - Abre una terminal o símbolo del sistema.
  - Escribe `jshell` y presiona Enter.
  - Verás un prompt como `jshell>` que indica que JShell está listo.

### 2. **Uso Básico**
- **Ejecutar Código Java**:
  - Escribe expresiones, declaraciones o definiciones de Java directamente en el prompt.
  - Ejemplo:
    ```java
    jshell> System.out.println("¡Hola, JShell!")
    ¡Hola, JShell!
    ```
  - JShell evalúa la entrada y muestra el resultado inmediatamente.

- **Variables y Expresiones**:
  - Declara variables o evalúa expresiones:
    ```java
    jshell> int x = 10
    x ==> 10
    jshell> x * 2
    $2 ==> 20
    ```
  - JShell asigna automáticamente nombres temporales (por ejemplo, `$2`) a los resultados de las expresiones.

- **Definir Métodos y Clases**:
  - Puedes definir métodos o clases:
    ```java
    jshell> void sayHello() { System.out.println("¡Hola!"); }
    |  created method sayHello()
    jshell> sayHello()
    ¡Hola!
    ```
    ```java
    jshell> class Test { int x = 5; }
    |  created class Test
    jshell> Test t = new Test()
    t ==> Test@7c417213
    jshell> t.x
    $5 ==> 5
    ```

### 3. **Comandos Clave**
JShell proporciona comandos integrados que comienzan con `/`. Aquí hay algunos esenciales:
- **Listar todo el código**: `/list` – Muestra todos los fragmentos ingresados en la sesión.
  ```java
  jshell> /list
  ```
- **Editar código**: `/edit <id>` – Abre un editor GUI para el fragmento con el ID dado (de `/list`).
- **Guardar sesión**: `/save myfile.java` – Guarda todos los fragmentos en un archivo.
- **Cargar archivo**: `/open myfile.java` – Carga y ejecuta código desde un archivo.
- **Ver variables**: `/vars` – Lista todas las variables declaradas.
  ```java
  jshell> /vars
  |    int x = 10
  ```
- **Ver métodos**: `/methods` – Lista todos los métodos definidos.
- **Salir de JShell**: `/exit` – Cierra la sesión de JShell.
- **Ayuda**: `/help` – Muestra todos los comandos disponibles.

### 4. **Importar Paquetes**
- JShell importa automáticamente paquetes comunes (por ejemplo, `java.util`, `java.io`). Para usar otros, impórtalos manualmente:
  ```java
  jshell> import java.time.LocalDate
  jshell> LocalDate.now()
  $3 ==> 2025-06-27
  ```

### 5. **Editar y Corregir Código**
- **Modificar código existente**:
  - Usa `/list` para encontrar el ID de un fragmento.
  - Redefínelo escribiendo una nueva versión. JShell sobrescribe la definición anterior.
    ```java
    jshell> int x = 5
    x ==> 5
    jshell> int x = 10
    x ==> 10
    ```
- **Eliminar un fragmento**: `/drop <id>` – Elimina un fragmento específico por su ID.

### 6. **Autocompletado con Tab**
- Presiona `Tab` para autocompletar nombres de clases, métodos o comandos.
- Ejemplo:
  ```java
  jshell> System.out.pr<tab>
  ```
  Esto sugiere `println`, `print`, etc.

### 7. **Ejecutar Scripts Externos**
- Carga y ejecuta un archivo Java:
  ```java
  jshell> /open MyScript.java
  ```
- También puedes iniciar JShell con un script:
  ```bash
  jshell MyScript.java
  ```

### 8. **Personalizar JShell**
- **Scripts de inicio**: Crea un archivo (por ejemplo, `startup.jsh`) con importaciones o código común, luego cárgalo con `/open startup.jsh` o establécelo como script de inicio predeterminado:
  ```bash
  jshell --start startup.jsh
  ```
- **Modos de feedback**: Ajusta la verbosidad de la salida con `/set feedback <modo>` (por ejemplo, `normal`, `concise`, `verbose`).

### 9. **Consejos**
- **Prototipado rápido**: Usa JShell para probar pequeños fragmentos de código, experimentar con APIs o aprender sintaxis de Java.
- **Manejo de errores**: JShell proporciona mensajes de error claros y te permite corregir errores sobre la marcha.
- **Entrada multilínea**: Para código complejo, JShell admite edición multilínea. Termina una línea con una barra invertida (`\`) para continuar:
  ```java
  jshell> int sum(int a, int b) { \
      ...> return a + b; \
      ...> }
  ```

### 10. **Solución de Problemas**
- **JShell no encontrado**: Asegúrate de que el directorio `bin` del JDK esté en la variable PATH de tu sistema.
- **Inicio lento**: En algunos sistemas, JShell puede tardar un momento en inicializarse. Asegúrate de que tu JDK esté actualizado.
- **Reiniciar sesión**: Usa `/reset` para borrar todos los fragmentos y comenzar de nuevo.

Para más detalles, consulta la documentación oficial de JDK o ejecuta `/help` en JShell. Si tienes tareas específicas o código que quieres probar en JShell, ¡avísame y puedo guiarte más!