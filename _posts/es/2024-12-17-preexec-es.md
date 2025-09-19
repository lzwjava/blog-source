---
audio: false
generated: false
image: true
lang: es
layout: post
title: Mostrar Configuración del Proxy Antes de Ejecutar Comandos
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/preexec/pe1.png" alt="prexec" />  
</div>

Vivir en China o trabajar en empresas que utilizan VPNs y proxies puede complicar el desarrollo de software. Olvidar configurar estos ajustes a menudo provoca problemas de conectividad. Para agilizar tu flujo de trabajo, creé un sencillo script en Zsh con la ayuda de ChatGPT que muestra automáticamente tus configuraciones de proxy cuando ejecutas comandos específicos que dependen de la red.

## ¿Por qué mostrar la configuración del proxy?

Los proxies y las VPN son esenciales para acceder a recursos externos de manera segura. Mostrar la configuración de tu proxy antes de ejecutar comandos que dependen de la red te ayuda a identificar y solucionar rápidamente problemas de conectividad.

## El Script

Este script utiliza la función `preexec` de Zsh para verificar si el próximo comando depende de la red. Si lo es y las variables de entorno del proxy están configuradas, muestra la configuración actual del proxy.

```bash
# Función para verificar y mostrar la configuración del proxy antes de ciertos comandos
preexec() {
    # Definir comandos dependientes de la red
    local network_commands=(
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
        # Añadir más comandos según sea necesario
    )
```

    # Extraer la primera palabra (comando) de la línea de comandos
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Función para mostrar variables de proxy
    display_proxy() {
        echo -e "\n🚀 Configuración de Proxy Detectada:"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

```bash
        echo ""
    }
```

```bash
    # Verificar si el comando depende de la red
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                
                display_proxy
            fi
            break
        fi
    done
}
```

## Configurando el Script en Zsh

### 1. Abre tu archivo `.zshrc`

Usa tu editor de texto preferido para abrir el archivo de configuración `.zshrc`. Por ejemplo:

```bash
nano ~/.zshrc
```

### 2. Agrega la función `preexec`

Pega el script anterior al final del archivo.

### 3. Guardar y Cerrar

Presiona `CTRL + O` para guardar y `CTRL + X` para salir.

### 4. Aplicar los Cambios

Recarga tu `.zshrc` para aplicar la nueva configuración de inmediato:

```bash
source ~/.zshrc
```

## Probando la Configuración

### 1. Con Proxy Habilitado

Establece una variable de proxy temporalmente y ejecuta un comando dependiente de la red usando `pip`:

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
pip install selenium beautifulsoup4 urllib3
```

Salida Esperada:

```

🚀 Configuración de Proxy Detectada:
   - HTTP_PROXY: http://127.0.0.1:7890
   - http_proxy: 127.0.0.1:7890
   - HTTPS_PROXY: 127.0.0.1:7890
   - https_proxy: 127.0.0.1:7890
   - ALL_PROXY: 127.0.0.1:7890
   - all_proxy: 127.0.0.1:7890

Recopilando selenium
  Descargando selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
Recopilando beautifulsoup4
  Descargando beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
Recopilando urllib3
  Descargando urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

### 2. Sin Proxy Habilitado

Desactiva la variable de proxy y ejecuta el mismo comando `pip`:

```bash
unset HTTP_PROXY
pip install selenium beautifulsoup4 urllib3
```

*Nota: El código no necesita traducción, ya que es un comando en bash y los nombres de los paquetes de Python también se mantienen en inglés.*

Salida Esperada:

```
Recopilando selenium
  Descargando selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
Recopilando beautifulsoup4
  Descargando beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
Recopilando urllib3
  Descargando urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

*(No debería aparecer ninguna notificación de proxy.)*

### 3. Comando sin Red

Ejecuta un comando local como `ls`:

```bash
ls
```

Salida Esperada:

```
[Lista de archivos y directorios]
```

*(No debería aparecer ninguna notificación de proxy.)*

## Personalización

- Extender `network_commands`: Agrega cualquier comando adicional que dependa de la red al arreglo `network_commands`.

- Manejar alias: Asegúrate de que cualquier alias para comandos dependientes de la red esté incluido en la lista `network_commands`.

  ```bash
  alias gpa='git push all'
  ```

Agrega `"gpa"` al arreglo `network_commands` para activar notificaciones de proxy cuando uses este alias.

- Mejora la Visibilidad con Colores:

Para una mejor visibilidad, especialmente en terminales abarrotados, puedes agregar color a las notificaciones del proxy:

  ```bash
  # Agrega códigos de color al principio de tu .zshrc
  GREEN='\033[0;32m'
  NC='\033[0m' # Sin Color
```

  display_proxy() {
      echo -e "\n${GREEN}🚀 Configuración de Proxy Detectada:${NC}"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

      echo ""
  }
  ```

## Conclusión

La gestión de configuraciones de proxy es crucial para un desarrollo de software fluido en entornos de red restringidos. Este script de Zsh asegura que siempre estés informado sobre tus configuraciones de proxy al ejecutar comandos que requieren acceso a la red, mejorando tu flujo de trabajo y la eficiencia en la resolución de problemas.

¡Feliz Codificación! 🚀