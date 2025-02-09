---
audio: false
lang: es
layout: post
title: Configuración SSH
translated: true
---

Este archivo `ssh-config` configura el comportamiento del cliente SSH. Desglosemos cada parte:

-   `Host * !192.*.*.*`: Esta sección se aplica a todos los hosts *excepto* aquellos que coinciden con el patrón `192.*.*.*` (típicamente, direcciones de red local).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: Esta es la parte clave. Le indica a SSH que use el programa `corkscrew` para conectarse al host de destino.
        -   `corkscrew`: Una herramienta que le permite tunelizar conexiones SSH a través de proxies HTTP o HTTPS.
        -   `localhost 7890`: Especifica la dirección del servidor proxy (`localhost`) y el puerto (`7890`). Esto asume que tiene un servidor proxy ejecutándose en su máquina local, escuchando en el puerto 7890 (por ejemplo, Shadowsocks, un proxy SOCKS u otra solución de tunelización).
        -   `%h`: Una variable SSH especial que se expande al nombre de host de destino al que intenta conectarse.
        -   `%p`: Otra variable SSH que se expande al puerto de destino (generalmente 22 para SSH).
    - En resumen, este bloque `Host` configura SSH para usar el proxy `corkscrew` para todas las conexiones *excepto* aquellas a la red local.

-   `Host *`: Esta sección se aplica a *todos* los hosts.
    -   `UseKeychain yes`: En macOS, esto le indica a SSH que almacene y recupere las claves SSH de su Keychain, para que no tenga que ingresar su contraseña cada vez.
    -   `AddKeysToAgent yes`: Esto agrega automáticamente sus claves SSH al agente SSH, para que no tenga que agregarlas manualmente después de cada reinicio.
    -   `IdentityFile ~/.ssh/id_rsa`: Especifica la ruta a su archivo de clave SSH privada. `~/.ssh/id_rsa` es la ubicación predeterminada para la clave privada RSA.

**En esencia, esta configuración configura un proxy para todas las conexiones SSH excepto las de la red local, y configura la administración de claves para mayor comodidad.**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
