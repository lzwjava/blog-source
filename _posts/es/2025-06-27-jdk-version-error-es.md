---
audio: false
generated: true
lang: es
layout: post
title: Cómo Solucionar el Error 'Unsupported OpenJDK' en VisualVM
translated: true
type: note
---

El error "Version of OpenJDK is not supported. Please use the default-jdk" al ejecutar VisualVM indica que la versión del Java Development Kit (JDK) que se está utilizando no es compatible con VisualVM. Este problema es común cuando VisualVM no puede encontrar un JDK compatible o cuando el JDK instalado no está configurado correctamente. A continuación se presentan pasos para resolver este problema, basados en el contexto de su configuración (YourKit Java Profiler 2025.3 y VisualVM en lo que parece ser un sistema Linux).

### Pasos para Solucionar el Problema

1.  **Verifique Su Versión Actual de Java**
    Ejecute el siguiente comando para verificar la versión de Java instalada:
    ```bash
    java -version
    ```
    Esto mostrará la versión de OpenJDK, por ejemplo:
    ```
    openjdk version "17.0.9" 2023-10-17
    OpenJDK Runtime Environment (build 17.0.9+9-Ubuntu-122.04)
    OpenJDK 64-Bit Server VM (build 17.0.9+9-Ubuntu-122.04, mixed mode, sharing)
    ```
    VisualVM normalmente requiere un JDK (no solo un JRE) y es compatible con Oracle JDK 8+ o versiones compatibles de OpenJDK. Asegúrese de tener un JDK compatible instalado.[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://visualvm.github.io/troubleshooting.html)

2.  **Instale el JDK Predeterminado**
    El error sugiere usar el `default-jdk`. En Ubuntu/Debian, puede instalarlo con:
    ```bash
    sudo apt update
    sudo apt install default-jdk
    ```
    Esto normalmente instala una versión estable y compatible de OpenJDK (por ejemplo, OpenJDK 11 o 17). Después de la instalación, verifique la versión nuevamente con `java -version`.[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

3.  **Configure la Variable de Entorno JAVA_HOME**
    VisualVM depende de la variable de entorno `JAVA_HOME` para localizar el JDK. Compruebe si está configurada:
    ```bash
    echo $JAVA_HOME
    ```
    Si no está configurada o apunta a un JDK no compatible, configúrela con la ruta correcta del JDK. Por ejemplo, si `default-jdk` instaló OpenJDK 17, la ruta podría ser `/usr/lib/jvm/java-17-openjdk-amd64`. Configúrela con:
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
    ```
    Para hacer esto permanente, agregue la línea a su `~/.bashrc` o `~/.zshrc`:
    ```bash
    echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
    source ~/.bashrc
    ```
    Reemplace la ruta con la ruta real del JDK en su sistema (use `update-alternatives --list java` para encontrarla).[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://github.com/oracle/visualvm/issues/558)

4.  **Especifique la Ruta del JDK para VisualVM**
    Si configurar `JAVA_HOME` no resuelve el problema, puede especificar explícitamente la ruta del JDK al iniciar VisualVM:
    ```bash
    ~/bin/YourKit-JavaProfiler-2025.3/bin/visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
    ```
    Reemplace `/usr/lib/jvm/java-17-openjdk-amd64` con la ruta a su JDK. Esto asegura que VisualVM use el JDK especificado.[](https://visualvm.github.io/download.html)[](https://notepad.onghu.com/2021/solve-visualvm-does-not-start-on-windows-openjdk/)

5.  **Instale un JDK Compatible**
    Si el `default-jdk` sigue siendo incompatible, considere instalar una versión específica de JDK conocida por funcionar con VisualVM, como OpenJDK 11 u Oracle JDK 8+:
    ```bash
    sudo apt install openjdk-11-jdk
    ```
    Luego, actualice `JAVA_HOME` o use la opción `--jdkhome` como se describió anteriormente.[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)

6.  **Verifique la Instalación de VisualVM**
    Asegúrese de que VisualVM esté instalado correctamente. El error sugiere que está ejecutando VisualVM desde el directorio de YourKit Java Profiler (`~/bin/YourKit-JavaProfiler-2025.3/bin`). Esto es inusual, ya que VisualVM es típicamente una herramienta independiente o incluida con un JDK. Verifique que VisualVM no esté corrupto:
    - Descargue la última versión de VisualVM desde `visualvm.github.io/download.html` (por ejemplo, VisualVM 2.2, lanzada el 22 de abril de 2025, es compatible con JDK 24).[](https://visualvm.github.io/relnotes.html)[](https://visualvm.github.io/)
    - Descomprímala en un nuevo directorio y ejecútela:
      ```bash
      unzip visualvm_22.zip
      cd visualvm_22/bin
      ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
      ```
    Evite descomprimir sobre una instalación existente de VisualVM, ya que esto puede causar problemas.[](https://visualvm.github.io/troubleshooting.html)

7.  **Compruebe Múltiples Instalaciones de Java**
    Múltiples versiones de Java pueden causar conflictos. Liste todas las versiones de Java instaladas:
    ```bash
    update-alternatives --list java
    ```
    Si se listan múltiples versiones, establezca la deseada como predeterminada:
    ```bash
    sudo update-alternatives --config java
    ```
    Seleccione el número correspondiente al JDK compatible (por ejemplo, OpenJDK 11 o 17).[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

8.  **Verifique las Dependencias de VisualVM**
    VisualVM requiere `libnb-platform18-java` y `libvisualvm-jni`. Asegúrese de que estén instalados:
    ```bash
    sudo apt install libnb-platform18-java libvisualvm-jni
    ```
    Esto es particularmente relevante si instaló VisualVM mediante `apt`.[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

9.  **Omita las Restricciones de OpenJDK (Opcional)**
    Si está utilizando una compilación de OpenJDK no compatible (por ejemplo, IcedTea o AdoptOpenJDK), las funciones de profiling pueden ser limitadas. Puede omitir algunas restricciones agregando un argumento de línea de comandos:
    ```bash
    ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64 -J-Dorg.graalvm.visualvm.profiler.SupportAllVMs=true
    ```
    Esto habilita el profiling para JVMs no compatibles, aunque no se garantiza que funcione perfectamente.[](https://github.com/oracle/visualvm/issues/143)

10. **Compruebe la Compatibilidad entre YourKit y VisualVM**
    Dado que está ejecutando VisualVM desde el directorio de YourKit Java Profiler, asegúrese de que el entorno de YourKit no esté interfiriendo. YourKit Java Profiler 2025.3 puede incluir una versión o configuración específica de VisualVM. Consulte la documentación de YourKit o contacte a `support@yourkit.com` para confirmar la compatibilidad con su JDK. Alternativamente, intente ejecutar VisualVM de forma independiente (descargado por separado) para aislar el problema.[](https://www.yourkit.com/changes/)

### Notas Adicionales
-   **Contexto de YourKit**: El error no se relaciona directamente con YourKit Java Profiler, pero ejecutar VisualVM desde el directorio de YourKit sugiere integración. YourKit es compatible con Java 7–15 y versiones posteriores con compilaciones EAP, así que asegúrese de que su JDK sea compatible con ambas herramientas si se usan juntas.[](https://www.yourkit.com/forum/viewtopic.php?t=41723)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
-   **Archivos de Log**: Revise los logs de VisualVM para obtener más detalles. Los logs suelen estar en `~/.visualvm/<version>/var/log`. Para YourKit, revise `~/.yjp/log/` para los logs del agente del profiler. Si los problemas persisten, envíe los logs a `support@yourkit.com`.[](https://stackoverflow.com/questions/70211315/java-17-and-yourkit-2021-11)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
-   **Alternativa**: Si VisualVM sigue fallando, considere usar las herramientas de profiling integradas de YourKit u otro profiler como JProfiler o Async Profiler, que pueden tener mejor compatibilidad con su configuración.[](https://digma.ai/9-best-java-profilers-to-use-in-2024/)[](https://bell-sw.com/blog/a-guide-to-java-profiling-tools-techniques-best-practices/)

### Si el Problema Persiste
Si ninguno de los pasos anteriores resuelve el problema, proporcione:
-   La salida de `java -version` y `echo $JAVA_HOME`.
-   La salida de `update-alternatives --list java`.
-   La versión exacta de VisualVM (verifique mediante `visualvm --help` o la página de descarga).
-   Si está utilizando VisualVM incluido con YourKit o una instalación independiente.

Esto ayudará a identificar el problema con mayor precisión. También puede reportar el problema en la página de GitHub de VisualVM (`https://github.com/oracle/visualvm`) o al soporte de YourKit para obtener orientación específica.[](https://github.com/oracle/visualvm/issues/558)