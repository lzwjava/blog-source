---
audio: false
lang: es
layout: post
title: Configurar el compilador de Java en Visual Studio Code
translated: true
---

¡Hola! Para configurar el compilador de Java en Visual Studio Code (VSCode) versión 1.96.4 en Windows, especialmente ya que has instalado el Java Extension Pack, necesitarás configurar la ruta del Java Development Kit (JDK). El compilador de Java es parte del JDK y VSCode necesita saber dónde encontrarlo para compilar tu código Java. Aquí tienes una guía paso a paso para configurarlo:

---

### Paso 1: Asegúrate de tener un JDK instalado
Antes de configurar nada en VSCode, asegúrate de tener un JDK (no solo un JRE) instalado en tu máquina Windows. El JDK incluye el compilador de Java (`javac`). Si aún no lo has instalado, puedes descargarlo de un proveedor como Oracle, OpenJDK o Adoptium (por ejemplo, JDK 17 o otra versión compatible con tu proyecto). Después de instalar, anota la ruta de instalación (por ejemplo, `C:\Program Files\Java\jdk-17.0.1`).

---

### Paso 2: Abre la configuración de VSCode
Para decirle a VSCode dónde está tu JDK, necesitarás ajustar su configuración:

- **A través de la interfaz de configuración:**
  - Presiona `Ctrl + ,` para abrir el panel de configuración.
  - Alternativamente, ve a `File > Preferences > Settings`.
- **A través de settings.json (opcional):**
  - Presiona `Ctrl + Shift + P` para abrir el Command Palette.
  - Escribe **"Open Settings (JSON)"** y selecciónalo para editar el archivo `settings.json` directamente.

---

### Paso 3: Configura la ruta del JDK con `java.home`
El Java Extension Pack depende de la configuración `java.home` para localizar tu JDK para la compilación y las características del lenguaje (como IntelliSense). Aquí te explico cómo configurarlo:

- **En la interfaz de configuración:**
  - En el panel de configuración, busca **"java.home"**.
  - En el campo "Java: Home", introduce la ruta completa a tu instalación del JDK. Por ejemplo:
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - Usa barras invertidas (`\`) ya que estás en Windows y asegúrate de que la ruta apunte al directorio raíz del JDK (debería contener una carpeta `bin` con `javac.exe`).

- **En settings.json:**
  - Si estás editando `settings.json`, agrega esta línea (reemplaza la ruta con la ubicación real de tu JDK):
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - Ejemplo completo de `settings.json`:
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - Guarda el archivo después de editarlo.

---

### Paso 4: Verifica la ruta
Asegúrate de que:
- La ruta apunte a un JDK (no a un JRE). La carpeta `bin` del JDK debería incluir `javac.exe`.
- No haya errores tipográficos en la ruta y coincida con la ubicación de tu instalación del JDK (por ejemplo, `C:\Program Files\Java\jdk-17.0.1`).

Si no estás seguro de dónde está instalado tu JDK, puedes encontrarlo en `C:\Program Files\Java` o donde lo hayas elegido durante la instalación.

---

### Paso 5: Opcional - Configura múltiples JDKs
Si tienes múltiples versiones de JDK instaladas y quieres cambiar entre ellas (por ejemplo, JDK 8 para un proyecto, JDK 17 para otro), puedes usar la configuración `java.configuration.runtimes`:

- Agrega esto a tu `settings.json`:
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-1.8",
          "path": "C:\\Program Files\\Java\\jdk1.8.0_291"
      },
      {
          "name": "JavaSE-17",
          "path": "C:\\Program Files\\Java\\jdk-17.0.1",
          "default": true
      }
  ]
  ```
- La opción `default: true` establece el entorno de ejecución predeterminado para ejecutar tu código. Sin embargo, para la compilación, la extensión de Java utiliza principalmente el JDK especificado en `java.home`.

---

### Paso 6: Recarga o reinicia VSCode
Después de configurar `java.home`, es posible que necesites:
- Recargar la ventana de VSCode (presiona `Ctrl + Shift + P`, escribe **"Reload Window"** y selecciónalo).
- O reiniciar completamente VSCode para que los cambios surtan efecto.

---

### Notas sobre la compilación
- **Archivos Java individuales:** Si estás trabajando con archivos `.java` individuales (sin herramientas de construcción), el Java Extension Pack "Language Support for Java(TM) by Red Hat" usa el JDK de `java.home` para compilar y ejecutar tu código. Puedes usar el botón "Run" o el comando **"Java: Run"**.
- **Proyectos con herramientas de construcción:** Si estás usando Maven, Gradle u otra herramienta de construcción, el compilador se gestiona por la configuración de la herramienta de construcción (por ejemplo, la variable de entorno `JAVA_HOME`, `pom.xml` para Maven o `build.gradle` para Gradle). Sin embargo, configurar `java.home` asegura que las características del lenguaje de VSCode funcionen correctamente.

---

### Solución de problemas
- **Problemas de ruta:** Si VSCode no puede encontrar el JDK, verifica la ruta en `java.home`. Evita espacios adicionales o comillas a menos que sea necesario.
- **JDK no instalado:** Si obtienes errores sobre `javac` faltante, asegúrate de que un JDK esté instalado.
- **Compatibilidad de versiones:** Asegúrate de que la versión de tu JDK coincida con los requisitos de tu proyecto (por ejemplo, JDK 8, 11, 17).

---

¡Listo! Ahora deberías tener el compilador de Java configurado en VSCode. Si encuentras algún problema o tienes más preguntas, como trabajar con una herramienta de construcción específica, no dudes en decírmelo y estaré encantado de ayudarte más. 😊

---

Configura `maven.terminal.userJavaHome` en true. Puedes verificar la versión de Java en la terminal.