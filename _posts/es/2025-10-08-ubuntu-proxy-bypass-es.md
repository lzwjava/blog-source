---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de Hosts para Omitir Proxy en Ubuntu
translated: true
type: note
---

### Configurar múltiples hosts en los ajustes manuales del proxy de Ubuntu

En la configuración manual del proxy de Ubuntu (en **Ajustes > Red > Proxy de red > Manual**), el campo "Ignorar hosts" permite especificar una lista separada por puntos y comas de hosts, dominios o rangos de IP para omitir el proxy. Esto se usa comúnmente para tráfico local como localhost o redes internas. No puedes configurar estos como la dirección del *servidor proxy* (que espera un único host:puerto), pero encajan perfectamente en "Ignorar hosts".

#### Pasos para configurar mediante la interfaz gráfica:
1. Abre **Ajustes** (búscalo en la visión general de Actividades).
2. Ve a **Red** > **Proxy de red**.
3. Establece el método en **Manual**.
4. En el campo **Ignorar hosts**, ingresa tu lista separada por puntos y comas (sin espacios alrededor):
   ```
   localhost;127.0.0.1;192.168.1.1;192.168.2.1;::1
   ```
   - `localhost`: Se resuelve a direcciones de loopback.
   - `127.0.0.1`: Loopback IPv4.
   - `192.168.1.1` y `192.168.2.1`: IPs locales específicas (agrega tantas como necesites).
   - `::1`: Loopback IPv6.

5. Haz clic en **Aplicar** para guardar. Esto se aplica a todo el sistema (afecta a aplicaciones como navegadores, apt, etc.).

#### Uso de comodines como `192.168.1.*`:
- Los comodines directos (ej. `192.168.1.*`) **no son compatibles** en el campo "Ignorar hosts"—está diseñado para hosts exactos, sufijos de dominio (ej. `*.local`) o notación CIDR para rangos de IP.
- En su lugar, usa **notación CIDR** para rangos:
  - Para `192.168.1.*` (todas las IPs en la subred 192.168.1.0/24), usa `192.168.1.0/24`.
  - Lista de ejemplo actualizada:
    ```
    localhost;127.0.0.1;::1;192.168.1.0/24;192.168.2.1
    ```
  - Para redes locales más amplias, agrega `10.0.0.0/8;172.16.0.0/12;192.168.0.0/16` (rangos privados comunes).

#### Alternativa desde la línea de comandos (para scripting o precisión):
Si prefieres el terminal (o necesitas automatizar), usa `gsettings` (Ubuntu moderno) o edita `/etc/environment` para todo el sistema:
- Ver la lista actual de ignorados:
  ```
  gsettings get org.gnome.system.proxy ignore-hosts
  ```
- Establecer la lista (reemplaza con tus valores):
  ```
  gsettings set org.gnome.system.proxy ignore-hosts "['localhost', '127.0.0.1', '::1', '192.168.1.0/24', '192.168.2.1']"
  ```
- Para variable de entorno permanente (afecta algunas aplicaciones): Agrega en `/etc/environment`:
  ```
  no_proxy="localhost,127.0.0.1,::1,192.168.1.0/24,192.168.2.1"
  ```
  Luego reinicia o ejecuta `source /etc/environment`.

Prueba haciendo ping a un host listado o verificando el comportamiento del proxy en un navegador. Si surgen problemas (ej. con aplicaciones específicas), el método de la variable de entorno suele cubrir más terreno.

[Configurar proxy para ignorar todas las direcciones locales](https://askubuntu.com/questions/11274/setting-up-proxy-to-ignore-all-local-addresses)  
[Cómo configurar los ajustes de proxy en Ubuntu](https://phoenixnap.com/kb/ubuntu-proxy-settings)  
[Establecer un rango de red en la variable de entorno no_proxy](https://unix.stackexchange.com/questions/23452/set-a-network-range-in-the-no-proxy-environment-variable)