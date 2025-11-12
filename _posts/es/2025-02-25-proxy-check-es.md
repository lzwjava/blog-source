---
audio: false
generated: true
lang: es
layout: post
title: Implementación de una Verificación de Proxy en Windows
translated: true
type: note
---

Para implementar una verificación de proxy en Windows usando Git-Bash y PowerShell, necesitas configurar mecanismos en cada shell para detectar cuando se ejecutan comandos relacionados con la red y mostrar la configuración del proxy si está configurada. A continuación se detallan los pasos y el código para Git-Bash y PowerShell. Es probable que la "terminal" mencionada se refiera a Windows Terminal que aloja estos shells, por lo que nos centraremos en las implementaciones para Git-Bash y PowerShell.

---

### **Para Git-Bash**

Git-Bash es una emulación de Bash en Windows, y podemos usar un `trap` de `DEBUG` para ejecutar una función antes de cada ejecución de comando. El objetivo es verificar si el comando está relacionado con la red y si la configuración del proxy está establecida, para luego mostrarla.

#### **Pasos:**

1.  **Definir la lista de comandos relacionados con la red.**
2.  **Crear una función para mostrar la configuración del proxy.**
3.  **Crear una función para verificar el comando y la configuración del proxy.**
4.  **Configurar el `trap` de `DEBUG` para ejecutar la verificación antes de cada comando.**
5.  **Definir una función manual `checkproxy` para mostrar la configuración del proxy bajo demanda.**
6.  **Agregar todas las configuraciones al archivo `.bashrc`.**

#### **Implementación:**

Agrega el siguiente código a tu archivo `~/.bashrc` (crea el archivo si no existe):

```bash
# Lista de comandos relacionados con la red
network_commands=(
    "gpa"
    "git"
    "ssh"
    "scp"
    "sftp"
    "rsync"
    "curl"
    "wget"
    "apt"
    "yum"
    "dnf"
    "npm"
    "yarn"
    "pip"
    "pip3"
    "gem"
    "cargo"
    "docker"
    "kubectl"
    "ping"
    "traceroute"
    "netstat"
    "ss"
    "ip"
    "ifconfig"
    "dig"
    "nslookup"
    "nmap"
    "telnet"
    "ftp"
    "nc"
    "tcpdump"
    "adb"
    "bundle"
    "brew"
    "cpanm"
    "bundle exec jekyll"
    "make"
    "python"
    "glcoud"
)

# Función para mostrar la configuración del proxy
display_proxy() {
    echo -e "🚀 **Configuración de Proxy Detectada:**"
    [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
    [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
    [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
    [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
    [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
    [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
    echo ""
}

# Función para verificar si el comando está relacionado con la red y los proxies están configurados
proxy_check() {
    local cmd
    # Extrae la primera palabra del comando
    cmd=$(echo "$BASH_COMMAND" | awk '{print $1}')
    
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$cmd" == "$network_cmd" ]]; then
            # Verifica si alguna variable de entorno de proxy está configurada
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                display_proxy
            fi
            break
        fi
    done
}

# Configura el trap DEBUG para ejecutar proxy_check antes de cada comando
trap 'proxy_check' DEBUG

# Función para verificar manualmente la configuración del proxy
checkproxy() {
    echo "HTTP_PROXY: $HTTP_PROXY"
    echo "HTTPS_PROXY: $HTTPS_PROXY"
    echo "Git HTTP Proxy:"
    git config --get http.proxy
    echo "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **Cómo Funciona:**

-   El array `network_commands` enumera comandos que están relacionados con la red.
-   `display_proxy` muestra todas las variables de entorno de proxy relevantes si están configuradas.
-   `proxy_check` usa `BASH_COMMAND` (disponible en el `trap` de `DEBUG`) para obtener el comando que se está ejecutando, extrae la primera palabra y verifica si coincide con algún comando de red. Si las variables de proxy están configuradas, las muestra.
-   La línea `trap 'proxy_check' DEBUG` asegura que `proxy_check` se ejecute antes de cada comando.
-   `checkproxy` te permite ver manualmente la configuración del proxy, incluidas las configuraciones de proxy específicas de Git.
-   Después de agregar esto a `.bashrc`, reinicia Git-Bash o ejecuta `source ~/.bashrc` para aplicar los cambios.

#### **Uso:**

-   Cuando ejecutes un comando de red (por ejemplo, `git clone`, `curl`), si la configuración del proxy está configurada, se mostrará antes de que se ejecute el comando.
-   Ejecuta `checkproxy` para ver manualmente la configuración del proxy.

---

### **Para PowerShell**

PowerShell no tiene un equivalente directo al `trap` de `DEBUG` de Bash, pero podemos usar el `CommandValidationHandler` del módulo `PSReadLine` para lograr una funcionalidad similar. Este controlador se ejecuta antes de cada comando, permitiéndonos verificar los comandos de red y la configuración del proxy.

#### **Pasos:**

1.  **Definir la lista de comandos relacionados con la red.**
2.  **Crear una función para mostrar la configuración del proxy.**
3.  **Configurar el `CommandValidationHandler` para verificar comandos y la configuración del proxy.**
4.  **Definir una función manual `checkproxy` para mostrar la configuración del proxy bajo demanda.**
5.  **Agregar todas las configuraciones a tu perfil de PowerShell.**

#### **Implementación:**

Primero, localiza tu archivo de perfil de PowerShell ejecutando `$PROFILE` en PowerShell. Si no existe, créalo:

```powershell
New-Item -Type File -Force $PROFILE
```

Agrega el siguiente código a tu perfil de PowerShell (por ejemplo, `Microsoft.PowerShell_profile.ps1`):

```powershell
# Lista de comandos relacionados con la red
$networkCommands = @(
    "gpa",
    "git",
    "ssh",
    "scp",
    "sftp",
    "rsync",
    "curl",
    "wget",
    "apt",
    "yum",
    "dnf",
    "npm",
    "yarn",
    "pip",
    "pip3",
    "gem",
    "cargo",
    "docker",
    "kubectl",
    "ping",
    "traceroute",
    "netstat",
    "ss",
    "ip",
    "ifconfig",
    "dig",
    "nslookup",
    "nmap",
    "telnet",
    "ftp",
    "nc",
    "tcpdump",
    "adb",
    "bundle",
    "brew",
    "cpanm",
    "bundle exec jekyll",
    "make",
    "python",
    "glcoud"
)

# Función para mostrar la configuración del proxy
function Display-Proxy {
    Write-Host "🚀 **Configuración de Proxy Detectada:**"
    if ($env:HTTP_PROXY) { Write-Host "   - HTTP_PROXY: $env:HTTP_PROXY" }
    if ($env:http_proxy) { Write-Host "   - http_proxy: $env:http_proxy" }
    if ($env:HTTPS_PROXY) { Write-Host "   - HTTPS_PROXY: $env:HTTPS_PROXY" }
    if ($env:https_proxy) { Write-Host "   - https_proxy: $env:https_proxy" }
    if ($env:ALL_PROXY) { Write-Host "   - ALL_PROXY: $env:ALL_PROXY" }
    if ($env:all_proxy) { Write-Host "   - all_proxy: $env:all_proxy" }
    Write-Host ""
}

# Configura CommandValidationHandler para verificar comandos antes de la ejecución
Set-PSReadLineOption -CommandValidationHandler {
    param($command)
    # Extrae la primera palabra del comando
    $cmd = ($command -split ' ')[0]
    
    if ($networkCommands -contains $cmd) {
        # Verifica si alguna variable de entorno de proxy está configurada
        if ($env:HTTP_PROXY -or $env:http_proxy -or $env:HTTPS_PROXY -or $env:https_proxy -or $env:ALL_PROXY -or $env:all_proxy) {
            Display-Proxy
        }
    }
    # Siempre retorna true para permitir la ejecución del comando
    return $true
}

# Función para verificar manualmente la configuración del proxy
function checkproxy {
    Write-Host "HTTP_PROXY: $env:HTTP_PROXY"
    Write-Host "HTTPS_PROXY: $env:HTTPS_PROXY"
    Write-Host "Git HTTP Proxy:"
    git config --get http.proxy
    Write-Host "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **Cómo Funciona:**

-   `$networkCommands` es un array de comandos relacionados con la red.
-   `Display-Proxy` muestra todas las variables de entorno de proxy relevantes si están configuradas.
-   `Set-PSReadLineOption -CommandValidationHandler` define un bloque de script que se ejecuta antes de cada comando:
    -   Extrae la primera palabra del comando.
    -   Verifica si está en `$networkCommands`.
    -   Si las variables de proxy están configuradas, llama a `Display-Proxy`.
    -   Retorna `$true` para asegurar que el comando se ejecute.
-   `checkproxy` permite la visualización manual de la configuración del proxy, incluidos los proxies específicos de Git.
-   Después de agregarlo a tu perfil, reinicia PowerShell o ejecuta `. $PROFILE` para aplicar los cambios.

#### **Requisitos:**

-   Se requiere el módulo `PSReadLine`, que está incluido por defecto en PowerShell 5.1 y versiones posteriores.
-   Si usas una versión anterior, es posible que necesites actualizar PowerShell o encontrar un método alternativo (no cubierto aquí, ya que la mayoría de los sistemas usan versiones más recientes).

#### **Uso:**

-   Cuando ejecutes un comando de red (por ejemplo, `git pull`, `curl`), si la configuración del proxy está configurada, se mostrará antes de que se ejecute el comando.
-   Ejecuta `checkproxy` para ver manualmente la configuración del proxy.

---

### **Notas sobre la "Terminal"**

-   Si "terminal" se refiere a Windows Terminal, es simplemente un host para shells como Git-Bash, PowerShell o Command Prompt (cmd.exe).
-   Las implementaciones anteriores funcionan dentro de sesiones de Git-Bash o PowerShell en Windows Terminal.
-   Implementar una funcionalidad similar en Command Prompt (cmd.exe) no es práctico debido a sus capacidades de scripting limitadas. Se recomienda usar Git-Bash o PowerShell en su lugar.

---

### **Consideraciones Adicionales**

-   **Análisis de Comandos:**
    -   Ambas implementaciones verifican solo la primera palabra del comando contra la lista de comandos de red. Por ejemplo, `git clone` se activa porque `git` está en la lista.
    -   Los comandos de varias palabras como `bundle exec jekyll` se activarán si `bundle` está en la lista, lo cual es suficiente para la mayoría de los casos.
    -   Si es necesario, podrías modificar el código para verificar todas las palabras del comando, pero esto podría generar falsos positivos y generalmente es innecesario.

-   **Variables de Proxy:**
    -   Ambas implementaciones verifican `HTTP_PROXY`, `http_proxy`, `HTTPS_PROXY`, `https_proxy`, `ALL_PROXY` y `all_proxy` para cubrir variaciones comunes.
    -   En Windows, las variables de entorno no distinguen entre mayúsculas y minúsculas, pero verificamos ambos casos para mantener la coherencia con el comportamiento tipo Unix (especialmente en Git-Bash).

-   **Configuración de Proxy en Git:**
    -   La función `checkproxy` en ambos shells muestra la configuración de proxy específica de Git usando `git config --get`.

---

### **Pruebas**

-   **Configurar Variables de Proxy:**
    -   En Git-Bash: `export HTTP_PROXY=http://proxy.example.com:8080`
    -   En PowerShell: `$env:HTTP_PROXY = "http://proxy.example.com:8080"`
-   **Ejecutar Comandos de Red:**
    -   Prueba comandos como `git --version`, `curl -V`, etc.
    -   La configuración del proxy debería mostrarse antes de la salida del comando.
-   **Usar `checkproxy`:**
    -   Ejecuta `checkproxy` en cualquier shell para ver manualmente la configuración del proxy.

---

Esta implementación proporciona una verificación de proxy robusta tanto en Git-Bash como en PowerShell, adecuada para su uso dentro de Windows Terminal o de forma independiente.