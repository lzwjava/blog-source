---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración del Proxy del Demonio de Docker
translated: true
type: note
---

### Configuración del Daemon de Docker para Ajustes de Proxy

El daemon de Docker puede configurarse para usar un proxy HTTP/HTTPS para operaciones como extraer imágenes o construir contenedores desde detrás de un firewall corporativo. Esto se hace editando (o creando) el archivo `/etc/docker/daemon.json`. Ten en cuenta que esta configuración se aplica al propio daemon (por ejemplo, para `docker pull` o `docker build`), no a contenedores individuales (que usarían variables de entorno o argumentos de construcción de Docker).

#### Prerrequisitos
- Necesitas acceso root o sudo en un sistema Linux (este es el sistema operativo principal para la configuración del daemon de Docker; en Windows/Mac con Docker Desktop, usa la configuración de la GUI en su lugar).
- Docker instalado y en ejecución.
- Conocer los detalles de tu servidor proxy (por ejemplo, `http://proxy.company.com:8080` para proxy HTTP/HTTPS, y cualquier excepción de no-proxy).

#### Configuración Paso a Paso

1.  **Localiza o Crea el Archivo de Configuración del Daemon**:
    - Abre una terminal y navega a `/etc/docker/` (crea el directorio si no existe: `sudo mkdir -p /etc/docker`).
    - Edita el archivo `daemon.json` usando un editor de texto (por ejemplo, `sudo nano /etc/docker/daemon.json` o `sudo vim /etc/docker/daemon.json`).
    - Si el archivo no existe, créalo. Comienza con un objeto JSON vacío `{}` si es nuevo.

2.  **Añade la Configuración del Proxy**:
    - Añade una sección `"proxies"` al archivo JSON. Aquí tienes un ejemplo básico:

      ```json
      {
        "proxies": {
          "http-proxy": "http://proxy.company.com:8080",
          "https-proxy": "http://proxy.company.com:8080",
          "no-proxy": "localhost,127.0.0.1,*.company.com,10.0.0.0/8"
        }
      }
      ```

      - **Explicaciones**:
        - `"http-proxy"`: La URL para el proxy HTTP (requerida para peticiones no-HTTPS).
        - `"https-proxy"`: La URL para el proxy HTTPS (a menudo la misma que el proxy HTTP).
        - `"no-proxy"`: Una lista separada por comas de hosts/dominios/rangos IP que deben evitar el proxy (por ejemplo, direcciones locales o dominios internos). Esto evita bucles infinitos.
        - Si se necesita autenticación, usa el formato `http://usuario:contraseña@proxy.company.com:8080`.
        - Para proxies SOCKS, usa `"http-proxy": "socks5://proxy.company.com:1080"`.

      - Si `daemon.json` ya tiene contenido existente (por ejemplo, otros ajustes como `"log-driver": "json-file"`), fusiona la sección `"proxies"` en él sin duplicar claves. Asegura una sintaxis JSON válida (usa una herramienta como `jsonlint` para validar si es necesario).

3.  **Guarda y Reinicia el Daemon de Docker**:
    - Guarda el archivo.
    - Reinicia el servicio Docker para aplicar los cambios:
      ```
      sudo systemctl restart docker
      ```
      - En sistemas antiguos o configuraciones sin systemd, usa `sudo service docker restart`.
    - Verifica que el daemon esté en ejecución:
      ```
      sudo systemctl status docker
      ```
      - Comprueba los registros si hay problemas: `sudo journalctl -u docker.service`.

4.  **Verifica la Configuración**:
    - Prueba extrayendo una imagen (que ahora debería enrutarse a través de tu proxy):
      ```
      docker pull hello-world
      ```
    - Comprueba si los ajustes del proxy están aplicados inspeccionando la configuración del daemon:
      ```
      docker info | grep -i proxy
      ```
      - Deberías ver una salida como:
        ```
        HTTP Proxy: http://proxy.company.com:8080
        HTTPS Proxy: http://proxy.company.com:8080
        No Proxy: localhost,127.0.0.1,*.company.com,10.0.0.0/8
        ```
    - Si estás usando Docker en un contexto de construcción, prueba con:
      ```
      docker build -t test-proxy .
      ```
      (Asumiendo un Dockerfile simple que extrae una imagen base).

#### Notas Adicionales
- **Seguridad**: Evita codificar credenciales en `daemon.json` en sistemas compartidos. Usa variables de entorno si es posible, o herramientas como `docker config` para configuraciones más avanzadas.
- **Problemas Comunes**:
  - **Errores de Sintaxis**: Un JSON inválido impedirá que el daemon se inicie. Verifica dos veces con `cat /etc/docker/daemon.json` y un validador JSON.
  - **Firewall/SELinux**: Asegúrate de que tu proxy sea accesible y que ningún módulo de seguridad lo bloquee.
  - **Versión de Docker**: Esto funciona en Docker 20.10+ (versiones anteriores usaban diferentes variables de entorno como `HTTP_PROXY`). Comprueba tu versión con `docker --version` y actualiza si es necesario.
  - **Proxies Específicos del Registro**: Para registros privados, podrías necesitar configuración adicional bajo `"registry-mirrors"` o registros inseguros en `daemon.json`.
- **Para Contenedores**: Si necesitas ajustes de proxy *dentro* de contenedores en ejecución (no el daemon), establece variables de entorno en el Dockerfile (por ejemplo, `ENV http_proxy=http://proxy.company.com:8080`) o mediante `docker run -e http_proxy=...`.
- **Docker Desktop (Windows/Mac)**: Ve a Settings > Resources > Proxies, y habilita/configura allí—no es necesario editar JSON.

Para más detalles, consulta la documentación oficial de Docker: [Configure the Docker daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file). Si encuentras errores, ¡comparte la salida exacta para poder ayudarte!