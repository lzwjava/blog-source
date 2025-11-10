---
audio: false
generated: true
lang: es
layout: post
title: Actualización a OpenJDK 21 en macOS
translated: true
type: note
---

Dado que actualmente tienes OpenJDK 17 instalado a través de Homebrew en tu sistema macOS, aquí tienes una guía concisa para instalar OpenJDK 21, que es la última versión de Soporte a Largo Plazo (LTS) según tu fecha actual, 1 de julio de 2025. Puedes instalar OpenJDK 21 junto con OpenJDK 17 y cambiar entre ellos según sea necesario. El método más simple es usar Homebrew, pero también proporcionaré una opción de instalación manual.

### Método 1: Instalar OpenJDK 21 usando Homebrew (Recomendado)
Homebrew ya está instalado en tu sistema, como lo indica tu versión actual de Java. Este es el enfoque más fácil y mantenible.

1.  **Actualizar Homebrew**:
    Asegúrate de que Homebrew esté actualizado para obtener los últimos paquetes:
    ```bash
    brew update
    ```

2.  **Instalar OpenJDK 21**:
    Homebrew proporciona una fórmula específica para OpenJDK 21. Ejecuta el siguiente comando:
    ```bash
    brew install openjdk@21
    ```
    Esto instala OpenJDK 21 de manera "keg-only", lo que significa que no se creará un enlace simbólico en `/usr/local/bin` para evitar conflictos con otras versiones de Java.

3.  **Agregar OpenJDK 21 a tu PATH**:
    Para usar OpenJDK 21, necesitas agregarlo al PATH de tu sistema. Homebrew proporcionará instrucciones después de la instalación, pero típicamente, puedes enlazarlo temporal o permanentemente:
    -   **Temporal (para la sesión actual)**:
        ```bash
        export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
        ```
    -   **Permanente (agregar a la configuración del shell)**:
        Abre tu archivo de configuración del shell (probablemente `~/.zshrc` ya que macOS usa Zsh por defecto):
        ```bash
        nano ~/.zshrc
        ```
        Agrega la siguiente línea:
        ```bash
        export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
        ```
        Guarda y cierra el archivo, luego aplica los cambios:
        ```bash
        source ~/.zshrc
        ```

4.  **Establecer JAVA_HOME**:
    Para asegurar que las aplicaciones Java puedan localizar OpenJDK 21, establece la variable de entorno `JAVA_HOME`:
    ```bash
    export JAVA_HOME=$(/usr/libexec/java_home -v 21)
    ```
    Agrega esto a tu `~/.zshrc` para que sea permanente:
    ```bash
    echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
    source ~/.zshrc
    ```

5.  **Verificar la Instalación**:
    Verifica que OpenJDK 21 esté instalado y activo:
    ```bash
    java -version
    ```
    Deberías ver una salida similar a:
    ```
    openjdk 21.0.1 2023-10-17
    OpenJDK Runtime Environment (build 21.0.1+12)
    OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
    ```

6.  **Cambiar entre Versiones de Java**:
    Dado que tienes OpenJDK 17 instalado, puedes cambiar entre versiones usando `/usr/libexec/java_home`. Por ejemplo:
    -   Para usar OpenJDK 17:
        ```bash
        export JAVA_HOME=$(/usr/libexec/java_home -v 17)
        ```
    -   Para usar OpenJDK 21:
        ```bash
        export JAVA_HOME=$(/usr/libexec/java_home -v 21)
        ```
    Alternativamente, considera usar un gestor de versiones como `jenv` (instalar via `brew install jenv`) para cambiar más fácilmente:
    ```bash
    jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
    jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
    jenv enable-plugin export
    jenv global 21
    ```

### Método 2: Instalación Manual
Si prefieres no usar Homebrew, puedes instalar OpenJDK 21 manualmente.

1.  **Descargar OpenJDK 21**:
    -   Visita el sitio web oficial de OpenJDK (jdk.java.net/21) o un proveedor confiable como Oracle, Azul, o Adoptium.
    -   Para Apple Silicon (M1/M2), descarga el archivo `macOS/AArch64` tar.gz. Para Macs basados en Intel, elige `macOS/x64`.
    -   Ejemplo: Desde la página de descarga de JDK 21 de Oracle, selecciona el archivo tar.gz ARM64 o x64.

2.  **Verificar la Descarga**:
    Verifica la integridad del archivo descargado usando su suma de comprobación SHA256:
    ```bash
    shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
    ```
    Compara la salida con la suma de comprobación proporcionada en la página de descarga.

3.  **Extraer el Archivo**:
    Extrae el archivo tar.gz a un directorio deseado, como tu directorio de usuario:
    ```bash
    tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
    ```
    El JDK se extraerá en `~/OpenJDK/jdk-21.0.1.jdk/Contents/Home`.

4.  **Mover al Directorio del Sistema** (Opcional):
    Para mayor consistencia, puedes mover el JDK al directorio estándar de Java en macOS:
    ```bash
    sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
    ```

5.  **Establecer JAVA_HOME y PATH**:
    Actualiza tu `~/.zshrc` para incluir:
    ```bash
    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
    export PATH=$JAVA_HOME/bin:$PATH
    ```
    Aplica los cambios:
    ```bash
    source ~/.zshrc
    ```

6.  **Verificar la Instalación**:
    Confirma la instalación:
    ```bash
    java -version
    ```
    Asegúrate de que muestre OpenJDK 21.

### Notas
-   **Compatibilidad con Apple Silicon**: Asegúrate de descargar la compilación AArch64 para Macs M1/M2 para evitar problemas de rendimiento. Homebrew selecciona automáticamente la arquitectura correcta.
-   **Múltiples JDKs**: macOS admite múltiples JDKs en `/Library/Java/JavaVirtualMachines/`. Usa `/usr/libexec/java_home -v <version>` para cambiar entre ellos.
-   **Ventaja de Homebrew**: Homebrew simplifica las actualizaciones (`brew upgrade openjdk@21`) y asegura la compatibilidad con tu sistema.
-   **Proveedores Alternativos**: También puedes usar las compilaciones Azul Zulu o Eclipse Temurin de OpenJDK 21, disponibles en sus respectivos sitios web (por ejemplo, azul.com o adoptium.net).

Si encuentras algún problema, házmelo saber y puedo ayudar a solucionarlo.