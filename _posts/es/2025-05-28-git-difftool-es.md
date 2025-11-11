---
audio: false
generated: true
lang: es
layout: post
title: Configuración de BeyondCompare con Git Difftool
translated: true
type: note
---

Para configurar Beyond Compare como `git difftool`, sigue estos pasos. Estas instrucciones asumen que tienes Beyond Compare instalado y Git configurado en tu sistema.

### Pasos para configurar Beyond Compare como `git difftool`

1.  **Verificar la instalación de Beyond Compare**
    Asegúrate de que Beyond Compare esté instalado y sea accesible desde la línea de comandos. Puedes verificarlo ejecutando:
    ```
    bcomp
    ```
    Si no es reconocido, asegúrate de que el ejecutable de Beyond Compare (por ejemplo, `BCompare.exe` en Windows o `bcomp` en macOS/Linux) esté en el PATH de tu sistema.

2.  **Configurar Git para usar Beyond Compare**
    Ejecuta los siguientes comandos de configuración de Git en tu terminal o símbolo del sistema:

    ```bash
    git config --global diff.tool bc
    git config --global difftool.bc.path "ruta/hacia/bcomp"
    git config --global difftool.prompt false
    ```

    -   Reemplaza `"ruta/hacia/bcomp"` con la ruta real al ejecutable de Beyond Compare:
        -   **Windows**: Típicamente `"C:\Program Files\Beyond Compare 4\BCompare.exe"`. Usa barras invertidas dobles (`\\`) o barras normales (`/`) en la ruta.
        -   **macOS**: Usualmente `/Applications/Beyond Compare.app/Contents/MacOS/bcomp`.
        -   **Linux**: A menudo `/usr/bin/bcomp` o donde sea que `bcomp` esté instalado.
    -   El ajuste `difftool.prompt false` evita que Git te pida permiso para lanzar la herramienta de diferencias para cada archivo.

3.  **(Opcional) Configurar como herramienta de fusión (Merge Tool)**
    Si también quieres usar Beyond Compare como tu `mergetool`, añade estos comandos:

    ```bash
    git config --global merge.tool bc
    git config --global mergetool.bc.path "ruta/hacia/bcomp"
    git config --global mergetool.prompt false
    ```

4.  **Probar la configuración**
    Para verificar la configuración, crea o navega a un repositorio Git con cambios y ejecuta:

    ```bash
    git difftool
    ```

    Esto debería lanzar Beyond Compare para mostrar las diferencias entre tus archivos modificados y el último commit. Si lo estás usando como herramienta de fusión, prueba con:

    ```bash
    git mergetool
    ```

    (Esto aplica solo si tienes conflictos de fusión).

5.  **Notas específicas para plataformas**
    -   **Windows**: Asegúrate de usar la ruta correcta a `BCompare.exe`. Si la ruta contiene espacios, envuélvela entre comillas.
    -   **macOS/Linux**: El comando `bcomp` a menudo necesita esperar a que Beyond Compare se cierre antes de devolver el control a la terminal. La documentación de Beyond Compare sugiere que lo maneja automáticamente, pero si Git termina prematuramente, puede que necesites ajustar scripts o usar un wrapper (consulta el soporte de Beyond Compare para más detalles).
    -   Si encuentras problemas, verifica la ruta y asegúrate de que Beyond Compare tenga licencia y funcione correctamente.

6.  **Ejemplo de configuración para Windows**
    Para Beyond Compare 4 en Windows, los comandos podrían verse así:

    ```bash
    git config --global diff.tool bc
    git config --global difftool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
    git config --global difftool.prompt false
    git config --global merge.tool bc
    git config --global mergetool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
    git config --global mergetool.prompt false
    ```

7.  **Verificar la configuración**
    Revisa tu configuración de Git para asegurarte de que los ajustes se han aplicado:

    ```bash
    git config --global --list
    ```

    Busca entradas como `diff.tool=bc` y `difftool.bc.path`.

### Consejos adicionales

-   **Comparar archivos específicos**: Usa `git difftool <archivo>` para comparar un archivo específico.
-   **Comparar ramas**: Usa `git difftool rama1 rama2` para comparar diferencias entre dos ramas.
-   **Ajustes de Beyond Compare**: En Beyond Compare, puedes personalizar las reglas de comparación (por ejemplo, ignorar espacios en blanco) a través de su interfaz para una mejor visualización de diferencias.
-   **Resolución de problemas**: Si Beyond Compare no se inicia, verifica la ruta en el ajuste `difftool.bc.path`. Usa `which bcomp` (macOS/Linux) o `where BCompare.exe` (Windows) para localizar el ejecutable.

Esta configuración debería permitirte usar Beyond Compare sin problemas con `git difftool` y, opcionalmente, con `git mergetool`. Si encuentras problemas específicos, ¡házmelo saber con tu sistema operativo y cualquier mensaje de error para un consejo más específico!