---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Evitando Bucles de Proxy del Demonio de Docker
translated: true
type: note
---

### Por qué `"no-proxy": "localhost,127.0.0.1,.local"` es crucial en `daemon.json` de Docker

Cuando configuras el daemon de Docker con ajustes de proxy como `"http-proxy": "http://localhost:7890"` (común para herramientas como Clash ejecutándose localmente), el daemon aplica estas reglas a **todo** el tráfico de red saliente por defecto. Esto incluye conexiones a registros externos (por ejemplo, `registry-1.docker.io` para descargar imágenes como `hello-world`).

Sin embargo, sin la directiva `no-proxy`, el daemon de Docker también intenta enrutar **las conexiones locales**—como el protocolo de enlace TCP inicial a tu propio servidor proxy en `localhost:7890`—a través del mismo proxy. Esto crea un clásico **bucle de proxy**:

1.  Docker necesita obtener una imagen de `registry-1.docker.io`.
2.  Intenta conectarse a través del proxy en `localhost:7890`.
3.  Pero para alcanzar `localhost:7890`, los ajustes del proxy se activan de nuevo, forzando a Docker a... conectarse a través del proxy en `localhost:7890`.
4.  Esta recursión infinita falla a nivel de TCP porque el proxy no puede proxyizar una conexión a sí mismo (conduce a un bucle autorreferencial sin resolución).
5.  La conexión se aborta inesperadamente, resultando en el error `proxyconnect tcp: EOF` (EOF significa "end of file", señalando un cierre prematuro durante la negociación/protocolo de enlace del proxy).

Agregar `"no-proxy": "localhost,127.0.0.1,.local"` le dice explícitamente al daemon que **omita el proxy** para el tráfico destinado a:
-   `localhost` (el nombre de host de loopback de tu máquina),
-   `127.0.0.1` (dirección de loopback IPv4),
-   dominios `.local` (común para resolución mDNS/red local).

Esto permite a Docker conectarse **directamente** al servidor proxy en localhost sin pasar por sí mismo en un bucle. Una vez conectado, el proxy puede entonces manejar correctamente la solicitud externa al registro de Docker (por ejemplo, via HTTP CONNECT para tráfico HTTPS).

En resumen: Evita que el daemon "proxyice al proxy", garantizando que el acceso al proxy local funcione mientras sigue enrutando el tráfico dirigido a internet (como las descargas de imágenes) a través de él.

Si tu configuración involucra otros servicios locales (por ejemplo, registros internos o contenedores que se comunican localmente), extender `no-proxy` con esos dominios/IPs puede prevenir problemas similares.

[Configuración de Proxy del Daemon de Docker](https://docs.docker.com/engine/daemon/proxy/)  
[Discusión en el Foro sobre Ajustes de Proxy de Docker](https://forums.docker.com/t/proxy-settings-for-the-docker-daemon/132089)  
[Guía de Proxy de Docker para Firewalls Corporativos](https://www.datacamp.com/tutorial/docker-proxy)