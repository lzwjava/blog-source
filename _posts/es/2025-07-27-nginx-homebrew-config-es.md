---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración de Nginx en macOS Homebrew
translated: true
type: note
---

Para Nginx instalado mediante Homebrew en macOS (como lo indica la ruta del binario `/opt/homebrew/bin/nginx`), el archivo de configuración principal se encuentra típicamente en:

```
/opt/homebrew/etc/nginx/nginx.conf
```

Este directorio también contiene otros archivos relacionados, como los bloques de servidor en un subdirectorio `servers/` (por ejemplo, `/opt/homebrew/etc/nginx/servers/`).

Para confirmar la ruta exacta del archivo de configuración que utiliza tu instancia de Nginx, ejecuta el siguiente comando en tu terminal:

```
nginx -t
```

Esto probará la configuración y mostrará la ruta al archivo `nginx.conf` que está utilizando. Alternativamente, usa `nginx -V` para ver los detalles de compilación, incluyendo el prefijo de la ruta de configuración.

Si estás en un Mac Intel más antiguo donde Homebrew se instala en `/usr/local` en su lugar, la ruta sería `/usr/local/etc/nginx/nginx.conf`, pero la ruta del binario que proporcionaste confirma la ubicación `/opt/homebrew`.

**Referencias**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)