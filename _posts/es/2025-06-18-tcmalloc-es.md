---
audio: false
generated: true
lang: es
layout: post
title: Solucione el Error de TCMalloc
translated: true
type: note
---

El error "Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)" indica que la biblioteca TCMalloc, parte de las gperftools de Google, no está instalada o no está configurada correctamente en tu sistema Linux. TCMalloc es un asignador de memoria que puede mejorar el rendimiento y reducir el uso de memoria, particularmente en aplicaciones como Stable Diffusion. Aquí se explica cómo solucionar este problema:

### Pasos para Corregir el Error de TCMalloc

1.  **Instalar TCMalloc y Google Perftools**
    Dependiendo de tu distribución de Linux, usa el gestor de paquetes apropiado para instalar las bibliotecas requeridas.

    -   **Para sistemas basados en Ubuntu/Debian**:
        ```bash
        sudo apt-get update
        sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
        ```
        Esto instala tanto `libgoogle-perftools-dev` (incluye TCMalloc) como `libtcmalloc-minimal4` (una versión ligera).

    -   **Para sistemas basados en Fedora**:
        ```bash
        sudo dnf install gperftools-libs -y
        ```
        Esto instala las bibliotecas necesarias de TCMalloc.

    -   **Para sistemas basados en CentOS/RHEL**:
        ```bash
        sudo yum install gperftools-libs -y
        ```
        Si el paquete no está disponible en los repositorios por defecto, puede que necesites habilitar primero el repositorio EPEL:
        ```bash
        sudo yum install epel-release
        sudo yum install gperftools-libs -y
        ```

2.  **Verificar la Instalación**
    Después de la instalación, comprueba si TCMalloc está instalado:
    ```bash
    dpkg -l | grep tcmalloc
    ```
    Deberías ver `libtcmalloc-minimal4` o paquetes similares listados. Alternativamente, comprueba la ruta de la biblioteca:
    ```bash
    dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
    ```
    Esto mostrará la ruta a la biblioteca TCMalloc (por ejemplo, `/usr/lib/libtcmalloc.so.4`).

3.  **Configurar la Variable de Entorno LD_PRELOAD**
    Para asegurar que tu aplicación use TCMalloc, establece la variable de entorno `LD_PRELOAD` para que apunte a la biblioteca TCMalloc. Esto se puede hacer temporal o permanentemente.

    -   **Temporalmente (para la sesión actual)**:
        Ejecuta tu aplicación con `LD_PRELOAD` configurado:
        ```bash
        export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
        ./launch.py
        ```
        Reemplaza `/usr/lib/libtcmalloc.so.4` con la ruta real encontrada en el paso 2 si es diferente.

    -   **Permanentemente (para Stable Diffusion o similar)**:
        Si estás usando un script como `webui.sh` (común con Stable Diffusion), edita el script (por ejemplo, `webui-user.sh`) para incluir:
        ```bash
        export LD_PRELOAD=libtcmalloc.so.4
        ```
        Guarda el archivo y vuelve a ejecutar el script:
        ```bash
        ./webui.sh
        ```
        Alternativamente, agrégalo a tu configuración de shell (por ejemplo, `~/.bashrc` o `~/.zshrc`):
        ```bash
        echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
        source ~/.bashrc
        ```

4.  **Volver a ejecutar la Aplicación**
    Después de instalar TCMalloc y configurar `LD_PRELOAD`, reinicia tu aplicación:
    ```bash
    ./launch.py
    ```
    El error ya no debería aparecer, y puedes notar un uso de memoria o rendimiento mejorado.

5.  **Solución de Problemas**
    -   **Si la ruta de la biblioteca es incorrecta**: Si `LD_PRELOAD` falla (por ejemplo, "cannot open shared object file"), verifica el nombre y la ruta exactos de la biblioteca:
        ```bash
        find /usr/lib -name "libtcmalloc*.so*"
        ```
        Actualiza `LD_PRELOAD` con la ruta correcta (por ejemplo, `libtcmalloc_minimal.so.4` si usas la versión mínima).
    -   **Si el error persiste**: Asegúrate de que la versión instalada de TCMalloc sea compatible con tu sistema (glibc 2.35 y GCC 11.4.0 en tu caso). Si los problemas continúan, intenta instalar desde el código fuente:
        ```bash
        git clone https://github.com/google/tcmalloc.git
        cd tcmalloc
        bazel build //tcmalloc:hello_main
        bazel run //tcmalloc:hello_main
        ```
        Sigue la guía de inicio rápido de TCMalloc para instrucciones detalladas.
    -   **Problemas de memoria**: Si encuentras fallos de asignación o cierres inesperados, asegúrate de que tu sistema tiene memoria suficiente y que TCMalloc no está en conflicto con otros asignadores.

6.  **Opcional: Verificar el Uso de TCMalloc**
    Para confirmar que TCMalloc está funcionando, puedes ejecutar un programa de prueba simple o comprobar el uso de memoria con herramientas como `top` o `htop` mientras tu aplicación se ejecuta. TCMalloc típicamente reduce la fragmentación de memoria y puede proporcionar una ligera mejora de rendimiento.

### Notas Adicionales
-   **¿Por qué TCMalloc?** TCMalloc es un asignador de memoria de alto rendimiento que reduce el uso de memoria de la CPU y la fragmentación, especialmente en aplicaciones multi-hilo como Stable Diffusion. No es estrictamente requerido pero puede mejorar el rendimiento.
-   **Compatibilidad**: Tu sistema (glibc 2.35, Python 3.10.12, GCC 11.4.0) es compatible con las últimas versiones de TCMalloc, por lo que los pasos anteriores deberían funcionar. Si estás usando una aplicación compilada personalmente, asegúrate de que está compilada con soporte para TCMalloc.
-   **Contexto de Stable Diffusion**: Este error aparece a menudo con el WebUI de Stable Diffusion de AUTOMATIC1111. Los pasos anteriores, particularmente instalar `libgoogle-perftools-dev` y configurar `LD_PRELOAD`, son conocidos por resolverlo.

Si encuentras errores específicos o necesitas ayuda con una distribución particular de Linux, ¡házmelo saber y puedo adaptar las instrucciones!