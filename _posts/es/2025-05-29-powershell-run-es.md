---
audio: false
generated: true
lang: es
layout: post
title: 'PowerShell: Ejecutar Comandos en la Terminal Actual'
translated: true
type: note
---

Para ejecutar comandos como `mvn` o comandos del servidor WebSphere directamente en la terminal actual de PowerShell sin abrir un nuevo símbolo del sistema, puedes usar el operador de llamada (`&`) o invocar el comando directamente. Este enfoque garantiza que el comando se ejecute dentro de la sesión existente de PowerShell, manteniendo la salida y los errores en la misma terminal.

Así es como hacerlo:

1.  **Ejecutar el Comando Directamente**:
    Si el comando (por ejemplo, `mvn`) está en el PATH de tu sistema o es accesible en el directorio actual, simplemente escribe el comando como lo harías en una terminal:

    ```powershell
    mvn clean install
    ```

    Esto ejecuta `mvn` directamente en la sesión de PowerShell, y la salida permanece en la terminal actual.

2.  **Usar el Operador de Llamada (`&`)**:
    Si necesitas especificar la ruta al ejecutable o el comando está almacenado en una variable, usa el operador de llamada:

    ```powershell
    & "C:\ruta\a\maven\bin\mvn.cmd" clean install
    ```

    Para comandos del servidor WebSphere, si estás ejecutando algo como `wsadmin` o `startServer`, puedes hacer:

    ```powershell
    & "C:\ruta\a\WebSphere\AppServer\bin\startServer.bat" server1
    ```

    El operador `&` garantiza que el comando se ejecute en la sesión actual de PowerShell.

3.  **Manejar Comandos con Espacios o Variables**:
    Si la ruta del comando contiene espacios o está almacenada en una variable, usa `&` con la ruta entre comillas:

    ```powershell
    $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
    & $mvnPath clean install
    ```

4.  **Establecer Variables de Entorno (si es necesario)**:
    Algunos comandos como `mvn` o scripts de WebSphere pueden requerir variables de entorno (por ejemplo, `JAVA_HOME` o `WAS_HOME`). Establécelas en el script antes de ejecutar el comando:

    ```powershell
    $env:JAVA_HOME = "C:\ruta\a\jdk"
    $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
    mvn --version
    ```

    Para WebSphere:

    ```powershell
    $env:WAS_HOME = "C:\ruta\a\WebSphere\AppServer"
    & "$env:WAS_HOME\bin\startServer.bat" server1
    ```

5.  **Capturar la Salida o Manejar Errores**:
    Para capturar la salida del comando o manejar errores, usa los mecanismos estándar de PowerShell:

    ```powershell
    try {
        $output = & mvn clean install 2>&1
        Write-Output $output
    } catch {
        Write-Error "Error al ejecutar Maven: $_"
    }
    ```

6.  **Evitar `Start-Process`**:
    A diferencia de `Start-Process`, que inicia un nuevo proceso (a menudo en una ventana separada), los métodos anteriores mantienen la ejecución en la sesión actual. Evita usar `Start-Process` de esta manera:

    ```powershell
    # Esto abrirá una nueva ventana de símbolo del sistema
    Start-Process -FilePath "mvn" -ArgumentList "clean install"
    ```

    En su lugar, usa la ejecución directa o `&`.

### Script de Ejemplo
Aquí tienes un script de PowerShell de ejemplo para ejecutar `mvn` y un comando de WebSphere en la terminal actual:

```powershell
# Establecer variables de entorno si es necesario
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# Ejecutar comando de Maven
Write-Output "Ejecutando Maven..."
& mvn clean install

# Ejecutar comando del servidor WebSphere
Write-Output "Iniciando servidor WebSphere..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### Notas
-   Asegúrate de que las herramientas de línea de comandos (`mvn`, `startServer.bat`, etc.) estén en tu PATH o proporciona la ruta completa al ejecutable.
-   Si el comando requiere un directorio de trabajo específico, usa `Set-Location` (o `cd`) antes de ejecutarlo:

    ```powershell
    Set-Location "C:\ruta\al\proyecto"
    & mvn clean install
    ```

-   Para comandos que dependen de archivos `.bat` o `.cmd` (común con WebSphere), el operador `&` funciona bien, pero asegúrate de que el script se ejecute en PowerShell, no en `cmd.exe`.
-   Si encuentras problemas con las variables de entorno o el PATH, verifícalos con `Get-ChildItem Env:`.

Este enfoque mantiene todo en la terminal actual de PowerShell, evitando nuevas ventanas y manteniendo un flujo de trabajo limpio. Si tienes un comando o configuración específica que está causando problemas, comparte más detalles y puedo adaptar la solución aún más.