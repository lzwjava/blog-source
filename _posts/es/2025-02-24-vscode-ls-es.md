---
audio: false
generated: true
lang: es
layout: post
title: Servidor de Lenguaje Java en Visual Studio Code
translated: true
type: note
---

¡Hola! La configuración `java.jdt.ls.java.home` en Visual Studio Code (VSCode) es una opción específica utilizada por el Java Language Server (parte de la extensión "Language Support for Java(TM) by Red Hat", incluida en el Java Extension Pack). Vamos a desglosarlo:

---

### Qué Significa
- **JDT**: Significa "Java Development Tools", originalmente parte del IDE Eclipse. El Java Language Server en VSCode está basado en JDT de Eclipse, que proporciona funciones como autocompletado, depuración y compilación.
- **LS**: Significa "Language Server", un proceso en segundo plano que impulsa el soporte de Java en VSCode (por ejemplo, IntelliSense, comprobación de errores).
- **`java.jdt.ls.java.home`**: Esta configuración le indica al Java Language Server exactamente qué Java Development Kit (JDK) usar para sus operaciones. Es distinta de la configuración más general `java.home`, aunque están relacionadas.

En resumen, `java.jdt.ls.java.home` especifica la ruta del JDK que el Java Language Server utiliza para:
- Analizar tu código Java.
- Proporcionar funciones de lenguaje (por ejemplo, autocompletado, ir a la definición).
- Compilar y ejecutar código en algunos casos (aunque la compilación a menudo depende de otras configuraciones o herramientas de build).

---

### Diferencias con `java.home`
- **`java.home`**: Una configuración general de VSCode que apunta al JDK para todas las extensiones y tareas relacionadas con Java en VSCode. Se usa a menos que sea anulada por configuraciones más específicas.
- **`java.jdt.ls.java.home`**: Una configuración más específica que anula `java.home` solo para el Java Language Server. Si no se establece, el Language Server recurre a `java.home`.

Por lo tanto, si configuras `java.jdt.ls.java.home`, esta tiene prioridad para las operaciones del Language Server, permitiéndote usar un JDK diferente para las funciones de lenguaje que, por ejemplo, para las tareas de ejecución o depuración.

---

### Cómo Configurarlo
Como estás en Windows y usas VSCode 1.96.4 con el Java Extension Pack, aquí te explicamos cómo establecerlo:

1. **Abrir Configuración:**
   - Presiona `Ctrl + ,` para la Interfaz de Usuario de Configuración, o usa `Ctrl + Mayús + P` y escribe **"Open Settings (JSON)"** para editar `settings.json`.

2. **Establecer la Ruta:**
   - **En la Interfaz de Usuario de Configuración:**
     - Busca **"java.jdt.ls.java.home"**.
     - Ingresa la ruta completa a tu JDK (por ejemplo, `C:\Program Files\Java\jdk-17.0.1`).
   - **En settings.json:**
     - Añade esta línea (reemplaza con la ruta de tu JDK):
       ```json
       "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       ```
     - Ejemplo de `settings.json`:
       ```json
       {
           "java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
       }
       ```

3. **Verificar la Ruta del JDK:**
   - Asegúrate de que la ruta apunte a una carpeta JDK que contenga un directorio `bin` con `javac.exe` y `java.exe`.

4. **Recargar VSCode:**
   - Recarga la ventana (`Ctrl + Shift + P` > "Reload Window") o reinicia VSCode para aplicar el cambio.

---

### Cuándo Usarlo
Normalmente configurarías `java.jdt.ls.java.home` si:
- Tienes múltiples JDK instalados y quieres que el Language Server use uno específico (por ejemplo, JDK 17) mientras que otras tareas de Java (como ejecutar código) podrían usar un JDK diferente a través de `java.home`.
- Estás solucionando problemas del Language Server (por ejemplo, no está detectando automáticamente el JDK correcto).
- Tu proyecto tiene requisitos específicos de versión de JDK para las funciones de lenguaje.

Si no lo configuras, el Language Server usará el JDK de `java.home` (o la variable de entorno `JAVA_HOME` del sistema como último recurso).

---

### Ejemplo Práctico
Supongamos que tienes JDK 8 y JDK 17 instalados:
- Configura `"java.home": "C:\\Program Files\\Java\\jdk1.8.0_291"` para uso general.
- Configura `"java.jdt.ls.java.home": "C:\\Program Files\\Java\\jdk-17.0.1"` para asegurar que el Language Server use JDK 17 para soportar la sintaxis moderna de Java.

De esta manera, puedes depurar/ejecutar con JDK 8 pero obtener soporte de lenguaje para las funciones de JDK 17.

---

¿Queda claro? Si te preguntas cómo se ajusta esto a tu configuración o necesitas ayuda para ajustarlo más, ¡avísame! 😊