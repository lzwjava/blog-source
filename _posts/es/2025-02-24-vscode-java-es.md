---
audio: false
generated: true
lang: es
layout: post
title: Configurar el compilador de Java en Visual Studio Code
translated: true
type: note
---

¡Hola! Para configurar el compilador de Java en Visual Studio Code (VSCode) versión 1.96.4 en Windows, especialmente dado que ya tienes instalado el Java Extension Pack, necesitarás configurar la ruta del Java Development Kit (JDK). El compilador de Java es parte del JDK, y VSCode necesita saber dónde encontrarlo para compilar tu código Java. Aquí tienes una guía paso a paso para configurarlo:

---

### Paso 1: Asegúrate de tener un JDK instalado
Antes de configurar cualquier cosa en VSCode, asegúrate de tener un JDK (no solo un JRE) instalado en tu máquina Windows. El JDK incluye el compilador de Java (`javac`). Si aún no lo has instalado, puedes descargarlo de un proveedor como Oracle, OpenJDK o Adoptium (por ejemplo, JDK 17 u otra versión compatible con tu proyecto). Después de la instalación, toma nota de la ruta de instalación (por ejemplo, `C:\Program Files\Java\jdk-17.0.1`).

---

### Paso 2: Abre la Configuración de VSCode
Para indicarle a VSCode dónde está ubicado tu JDK, necesitarás ajustar su configuración:

- **A través de la Interfaz de Usuario (UI) de Configuración:**
  - Presiona `Ctrl + ,` para abrir el panel de Configuración.
  - Alternativamente, ve a `Archivo > Preferencias > Configuración`.
- **A través de settings.json (opcional):**
  - Presiona `Ctrl + Shift + P` para abrir la Paleta de Comandos.
  - Escribe **"Open Settings (JSON)"** y selecciónalo para editar el archivo `settings.json` directamente.

---

### Paso 3: Establece la Ruta del JDK con `java.home`
El Java Extension Pack depende de la configuración `java.home` para localizar tu JDK para la compilación y las características del lenguaje (como IntelliSense). Así es como configurarlo:

- **En la Interfaz de Usuario de Configuración:**
  - En el panel de Configuración, busca **"java.home"**.
  - En el campo "Java: Home", ingresa la ruta completa a tu instalación del JDK. Por ejemplo:
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - Usa barras invertidas (`\`) ya que estás en Windows, y asegúrate de que la ruta apunte al directorio raíz del JDK (debería contener una carpeta `bin` con `javac.exe`).

- **En settings.json:**
  - Si estás editando `settings.json`, agrega esta línea (reemplaza la ruta con la ubicación real de tu JDK):
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - Ejemplo de `settings.json` completo:
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - Guarda el archivo después de editarlo.

---

### Paso 4: Verifica la Ruta
Verifica nuevamente que:
- La ruta apunte a un JDK (no a un JRE). La carpeta `bin` del JDK debe incluir `javac.exe`.
- No haya errores tipográficos en la ruta, y que coincida con la ubicación de instalación de tu JDK (por ejemplo, `C:\Program Files\Java\jdk-17.0.1`).

Si no estás seguro de dónde está instalado tu JDK, puedes buscarlo en `C:\Program Files\Java` o donde lo hayas elegido durante la instalación.

---

### Paso 5: Opcional - Configurar Múltiples JDKs
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
- La opción `default: true` establece el runtime predeterminado para ejecutar tu código. Sin embargo, para la compilación, la extensión de Java utiliza principalmente el JDK especificado en `java.home`.

---

### Paso 6: Recarga o Reinicia VSCode
Después de configurar `java.home`, es posible que necesites:
- Recargar la ventana de VSCode (presiona `Ctrl + Shift + P`, escribe **"Reload Window"** y selecciónalo).
- O reiniciar VSCode completamente para que los cambios surtan efecto.

---

### Notas sobre la Compilación
- **Archivos Java Individuales:** Si estás trabajando con archivos `.java` individuales (sin herramientas de construcción), la función "Language Support for Java(TM) by Red Hat" del Java Extension Pack utiliza el JDK de `java.home` para compilar y ejecutar tu código. Puedes usar el botón "Run" o el comando **"Java: Run"**.
- **Proyectos con Herramientas de Construcción:** Si estás usando Maven, Gradle u otra herramienta de construcción, el compilador es gestionado por la configuración de la herramienta (por ejemplo, la variable de entorno `JAVA_HOME`, `pom.xml` para Maven, o `build.gradle` para Gradle). Sin embargo, configurar `java.home` aún asegura que las características de lenguaje de VSCode funcionen correctamente.

---

### Resolución de Problemas
- **Problemas con la Ruta:** Si VSCode no puede encontrar el JDK, verifica nuevamente la ruta en `java.home`. Evita espacios adicionales o comillas a menos que sean necesarios.
- **JDK No Instalado:** Si recibes errores sobre `javac` faltante, asegúrate de que un JDK esté instalado.
- **Compatibilidad de Versión:** Asegúrate de que tu versión de JDK coincida con los requisitos de tu proyecto (por ejemplo, JDK 8, 11, 17).

---

¡Eso es todo! Ahora deberías tener el compilador de Java configurado en VSCode. Si encuentras algún problema o tienes más preguntas—como trabajar con una herramienta de construcción específica—no dudes en hacérmelo saber, ¡y estaré encantado de ayudarte más! 😊

---

Establece `maven.terminal.userJavaHome` en true. Puedes verificar la versión de Java en la terminal.