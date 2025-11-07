---
audio: false
generated: false
image: false
lang: es
layout: post
title: Netplan, Systemd, SSH, Limpieza de Conda
translated: true
type: post
---

### Tabla de Contenidos

1. [Probando Netplan](#probando-netplan)
   - La configuración de IP estática causó la pérdida de SSH
   - Se requirió acceso físico para revertir
   - Se modificó el archivo de resolución DNS del sistema

2. [Servicio Systemd](#systemd-service)
   - Configurar servicio para inferencia LLM local
   - Configurar interfaz web para modelos LLM
   - Establecer servicio de herramienta de proxy basada en reglas
   - Usar comandos systemctl para la gestión de servicios

3. [Configuración SSH](#ssh-configuration)
   - Conexiones externas de proxy a través de corkscrew
   - Excluir la red local del proxy
   - Gestionar claves SSH a través de llavero y agente
   - Especificar la ubicación predeterminada de la clave privada

4. [Eliminar Conda en Linux](#eliminar-conda-en-linux)
   - Eliminar el directorio completo de instalación de conda
   - Eliminar el código de inicialización de conda de bashrc
   - Actualizar la variable de entorno PATH
   - Eliminar los archivos binarios de conda de la ruta del sistema


## Probando Netplan

Intenté la siguiente configuración para asignar una dirección IP estática a una máquina Ubuntu. Ejecuto OpenWebUI y llama.cpp en ese servidor.

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

Después de ejecutar `sudo netplan apply`, ya no se podía acceder a la máquina a través de `ssh lzw@192.168.1.128`.

Se utilizó el teclado y el ratón para iniciar sesión en la máquina, eliminar los archivos y revertir la configuración.

`/etc/resolv.conf` fue cambiado.

---

## Servicio Systemd

*13.02.2025*

## Configuración del servicio del servidor LLaMA

Esta sección explica cómo configurar un servicio systemd para ejecutar el servidor LLaMA, que proporciona capacidades de inferencia LLM local.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Configuración del servicio Open WebUI

Esta sección explica cómo configurar un servicio systemd para ejecutar Open WebUI, que proporciona una interfaz web para interactuar con modelos LLM.

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## Configuración del servicio Clash

Esta sección explica cómo configurar un servicio systemd para ejecutar Clash, una herramienta de proxy basada en reglas.

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# Crear el archivo de servicio
sudo emacs /etc/systemd/system/clash.service 

# Recargar el demonio systemd
sudo systemctl daemon-reload

# Habilitar e iniciar el servicio
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# Comprobar estado
sudo systemctl status clash.service
```

---

## Configuración SSH

*09.02.2025*

Este archivo `ssh-config` configura el comportamiento del cliente SSH. Desglosamos cada parte:

-   `Host * !192.*.*.*`: Esta sección se aplica a todos los hosts *excepto* a aquellos que coinciden con el patrón `192.*.*.*` (típicamente, direcciones de red local).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: Esta es la parte clave. Le dice a SSH que use el programa `corkscrew` para conectarse al host de destino.
        -   `corkscrew`: Una herramienta que permite tunelizar conexiones SSH a través de proxies HTTP o HTTPS.
        -   `localhost 7890`: Especifica la dirección (`localhost`) y el puerto (`7890`) del servidor proxy. Esto asume que tienes un servidor proxy ejecutándose en tu máquina local, escuchando en el puerto 7890 (por ejemplo, Shadowsocks, un proxy SOCKS, u otra solución de tunelización).
        -   `%h`: Una variable especial de SSH que se expande al nombre de host de destino al que intentas conectarte.
        -   `%p`: Otra variable de SSH que se expande al puerto de destino (normalmente 22 para SSH).
    - En resumen, este bloque `Host` configura SSH para usar el proxy `corkscrew` para todas las conexiones *excepto* las de la red local.

-   `Host *`: Esta sección se aplica a *todos* los hosts.
    -   `UseKeychain yes`: En macOS, esto le dice a SSH que almacene y recupere las claves SSH de tu Llavero, para que no tengas que introducir tu contraseña cada vez.
    -   `AddKeysToAgent yes`: Esto añade automáticamente tus claves SSH al agente SSH, para que no tengas que añadirlas manualmente después de cada reinicio.
    -   `IdentityFile ~/.ssh/id_rsa`: Especifica la ruta a tu archivo de clave privada SSH. `~/.ssh/id_rsa` es la ubicación predeterminada para la clave privada RSA.

**En esencia, esta configuración establece un proxy para todas las conexiones SSH excepto las de la red local, y configura la gestión de claves para mayor comodidad.**


```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa 
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa    
```

---

## Eliminar Conda en Linux

*07.02.2025*

```bash
rm -rf ~/anaconda3
```

Elimina el siguiente código en `.bashrc`:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Actualizar la ruta de:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

A:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```