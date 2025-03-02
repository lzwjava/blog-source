---
audio: false
generated: true
lang: es
layout: post
title: Perfil de Zsh
translated: true
---

Este perfil zsh tiene como objetivo mejorar la experiencia en la línea de comandos, con un enfoque en configuraciones de proxy, integración con Git y útiles alias. Las siguientes secciones detallan sus características:

**1. Configuración de PATH:**

   - `export PATH=...`: Esta línea establece la variable de entorno `PATH`, que le indica a la shell dónde buscar archivos ejecutables. Incluye varios directorios como los de Java, Ruby, Homebrew, Python, Flutter y el SDK de Google Cloud. Esto asegura que los comandos de estas herramientas se puedan ejecutar directamente desde la terminal.

**2. Gestión de Proxy:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: Esto define una variable `GLOBAL_PROXY` que contiene la dirección del servidor proxy.
   - `function start_proxy { ... }`: Esta función establece las variables de entorno `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy` y `ALL_PROXY` para usar el proxy especificado. También desactiva las solicitudes de URI completas para los proxies.
   - `function start_proxy_without_prefix { ... }`: Similar a `start_proxy`, pero establece las variables de proxy sin el prefijo `http://`.
   - `function stop_proxy { ... }`: Esta función desactiva las variables de proxy, desactivando efectivamente el proxy. También habilita las solicitudes de URI completas para los proxies.
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: Esto especifica una lista de hosts que deben omitir el proxy.

**3. Proxy de Git:**

   - `function start_git_proxy { ... }`: Esta función configura git para usar el proxy global para conexiones HTTP y HTTPS.
   - `function stop_git_proxy { ... }`: Esta función desactiva las configuraciones de proxy de git.

**4. Integración con Homebrew:**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`: Esta línea integra Homebrew en el entorno de la shell, permitiéndote usar comandos de Homebrew.

**5. Alias de Conveniencia:**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`: Esto crea un alias `gpa` para ejecutar un script de python `gitmessageai.py` con la API mistral.
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`: Esto crea un alias `gca` para ejecutar el mismo script sin enviar cambios.
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`: Esto crea un alias `gm` para ejecutar el mismo script y solo imprimir el mensaje de confirmación.
   - `alias gpam=/usr/local/bin/git-auto-commit`: Esto crea un alias `gpam` para ejecutar el script `git-auto-commit`.
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`: Esto crea un alias `rougify` para ejecutar el script `rougify`.

**6. Certificado SSL:**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`: Esto establece la ruta a un archivo de certificado SSL personalizado.

**7. Auto-Actualización de Homebrew:**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`: Esto desactiva las actualizaciones automáticas de Homebrew.

**8. Verificación de Proxy Pre-Ejecución:**

   - `preexec() { ... }`: Esta función se ejecuta antes de cada comando. Verifica si el comando está en una lista de comandos dependientes de la red. Si es así, y si alguna de las variables de proxy está configurada, muestra las configuraciones de proxy.
   - `local network_commands=( ... )`: Este array lista los comandos que se consideran dependientes de la red.
   - `display_proxy() { ... }`: Esta función muestra las configuraciones de proxy actuales.

**9. Completado de SDK de Google Cloud:**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`: Esta línea habilita el completado de comandos de shell para gcloud.

**10. Claves y Credenciales de API:**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`: Establece la ruta a las credenciales de la cuenta de servicio de Google Cloud.
    - `export DEEPSEEK_API_KEY="xxx"`: Establece la clave de API de DeepSeek.
    - `export MISTRAL_API_KEY="xxx"`: Establece la clave de API de Mistral.
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`: Establece la ruta de la biblioteca dinámica para curl.
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`: Establece el punto final de voz de Azure.
    - `export DO_API_KEY="xxx"`: Establece la clave de API de Digital Ocean.
    - `export GEMINI_API_KEY="xxx"`: Establece la clave de API de Gemini.

**11. Entorno Conda:**

    - `conda activate base`: Activa el entorno base de conda.

**En resumen, este perfil zsh proporciona una configuración completa para un desarrollador, incluyendo:**

- Fácil gestión de proxy con funciones para iniciar y detener proxies.
- Configuración de proxy de Git.
- Integración con Homebrew.
- Alias convenientes para tareas comunes.
- Verificaciones de proxy pre-ejecución para comandos dependientes de la red.
- Claves y credenciales de API para varios servicios.
- Activación del entorno conda.

Este perfil está diseñado para optimizar el flujo de trabajo del usuario y facilitar la gestión de diversas herramientas y servicios de desarrollo.

```bash
export PATH=/opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin:/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin:/Users/lzwjava/bin/flutter/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:/opt/homebrew/Cellar/llama.cpp/4539/bin:/Users/lzwjava/bin/google-cloud-sdk/bin

# /opt/homebrew/opt/openjdk/bin

# /opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin

export GLOBAL_PROXY='127.0.0.1:7890'
# export GLOBAL_PROXY='http://192.168.1.1:7890'

function start_proxy {
    export HTTP_PROXY="http://$GLOBAL_PROXY"
    export HTTPS_PROXY="http://$GLOBAL_PROXY"
    export http_proxy="http://$GLOBAL_PROXY"
    export https_proxy="http://$GLOBAL_PROXY"
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
    export ALL_PROXY=$http_proxy
}

function start_proxy_without_prefix {
    export http_proxy=$GLOBAL_PROXY
    export HTTP_PROXY=$GLOBAL_PROXY
    export https_proxy=$GLOBAL_PROXY
    export HTTPS_PROXY=$GLOBAL_PROXY
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
    export ALL_PROXY=$http_proxy
}

function stop_proxy {
    export http_proxy=
    export HTTP_PROXY=
    export https_proxy=
    export HTTPS_PROXY=
    export HTTP_PROXY_REQUEST_FULLURI=true
    export HTTPS_PROXY_REQUEST_FULLURI=true
    export ALL_PROXY=
}

export NO_PROXY="localhost,127.0.0.1,.example.com,::1"

function start_git_proxy {
  git config --global http.proxy $GLOBAL_PROXY
  git config --global https.proxy $GLOBAL_PROXY
}

function stop_git_proxy {
  git config --global --unset http.proxy
  git config --global --unset https.proxy
}

eval "$(/opt/homebrew/bin/brew shellenv)"

start_proxy
# start_git_proxy

# alias python3=/opt/homebrew/bin/python3
# alias pip3=/opt/homebrew/bin/pip3
# alias pip=pip3

alias gpa='python ~/bin/gitmessageai.py --api mistral'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'

alias gpam=/usr/local/bin/git-auto-commit

# bundle exec jekyll serve
export SSL_CERT_FILE=~/bin/cacert.pem

alias rougify=/Users/lzwjava/projects/rouge/bin/rougify

# git config --global core.editor "code --wait"
# git config --global -e

export HOMEBREW_NO_AUTO_UPDATE=1

# Función para verificar y mostrar las configuraciones de proxy antes de ciertos comandos
# Función para verificar y mostrar las configuraciones de proxy antes de ciertos comandos
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
        "python"
        "glcoud"
        # Añadir más comandos según sea necesario
    )

    # Extraer la primera palabra (comando) de la línea de comandos
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Función para mostrar variables de proxy
    display_proxy() {
        echo -e "🚀 **Configuraciones de Proxy Detectadas:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    # Verificar si el comando es dependiente de la red
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

# La siguiente línea habilita el completado de comandos de shell para gcloud.
if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi

export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"

export DEEPSEEK_API_KEY="xxx"

export MISTRAL_API_KEY="xxx"

export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib

export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"

export DO_API_KEY="xxx"

export GEMINI_API_KEY="xxx"

conda activate base
```