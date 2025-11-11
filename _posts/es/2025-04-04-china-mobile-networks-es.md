---
audio: false
generated: true
lang: es
layout: post
title: Por qué fallan las operaciones de Git en las redes móviles chinas
translated: true
type: note
---

Este es un problema común al usar ciertas redes móviles en China, especialmente con servicios como Git que dependen de puertos y protocolos específicos. A continuación, se explica por qué sucede y cómo solucionarlo:

**Por qué fallan las operaciones de Git en las redes móviles chinas:**

* **Bloqueo/Limitación de Puertos:**
    * Los operadores de redes móviles en China a veces implementan modelado de tráfico o bloqueo de puertos, particularmente para puertos no estándar utilizados por Git (como el puerto SSH 22). Esto se hace a menudo para gestionar el ancho de banda de la red o por razones de seguridad.
    * Incluso si el puerto 22 no está completamente bloqueado, podría estar muy limitado, lo que lleva a conexiones extremadamente lentas o tiempos de espera agotados, que aparecen como operaciones de Git "atascadas".
* **Problemas de DNS:**
    * Aunque puedes acceder a sitios web como GitHub y Google, las operaciones de Git dependen de la resolución de nombres de host específicos (por ejemplo, `github.com`) a través del DNS. Si la resolución DNS es lenta o poco confiable, puede hacer que Git se cuelgue.
* **Pérdida de Paquetes/Latencia:**
    * Las redes móviles, especialmente cuando se usan como hotspots, pueden tener una mayor latencia y pérdida de paquetes en comparación con las conexiones cableadas. Esto puede interrumpir la conexión SSH utilizada por Git, provocando fallos.
* **Interferencia del Firewall:**
    * El "Gran Firewall" de China puede interferir con las conexiones SSH, incluso si no están explícitamente bloqueadas. La inspección profunda de paquetes del firewall a veces puede causar inestabilidad en la conexión.
* **Problemas de MTU:**
    * Los problemas de Unidad Máxima de Transmisión (MTU) pueden causar problemas con la transferencia de datos, y las redes móviles a veces tienen valores de MTU más pequeños que las redes cableadas.

**Cómo solucionar los problemas de Git Push/Pull en las redes móviles chinas:**

1.  **Usar HTTPS en lugar de SSH:**
    * Git sobre HTTPS utiliza el puerto 443, que normalmente está abierto para el tráfico web. Esta es la solución más confiable.
    * Para cambiar tu repositorio remoto de Git a HTTPS:
        * Abre tu terminal.
        * Navega a tu repositorio de Git.
        * Ejecuta el siguiente comando, reemplazando `tu_nombre_de_usuario` y `tu_repositorio` con tus datos de GitHub:
            ```bash
            git remote set-url origin https://github.com/tu_nombre_de_usuario/tu_repositorio.git
            ```
    * Si necesitas proporcionar nombre de usuario y contraseña, puedes usar el ayudante de credenciales de git, o usar un token de acceso personal.
2.  **Usar una VPN:**
    * Una VPN confiable puede eludir las restricciones de la red y proporcionar una conexión más estable.
    * Conéctate a un servidor VPN fuera de China antes de intentar operaciones con Git.
    * Ten en cuenta que las VPN también pueden experimentar inestabilidad y problemas de velocidad.
3.  **Configurar el Puerto SSH (si es necesario usar SSH):**
    * Si debes usar SSH, intenta configurar Git para usar un puerto diferente (por ejemplo, 443) que podría tener menos probabilidades de estar bloqueado.
    * Edita tu archivo `~/.ssh/config`:
        ```
        Host github.com
            Hostname ssh.github.com
            Port 443
            User git
        ```
    * Luego, cambia la URL de tu repositorio remoto para usar ssh.github.com:
        ```bash
        git remote set-url origin git@ssh.github.com:tu_nombre_de_usuario/tu_repositorio.git
        ```
4.  **Verificar la Configuración de MTU:**
    * Si sospechas problemas de MTU, intenta reducir el tamaño de tu MTU.
    * En macOS, puedes usar el comando `networksetup` para ajustar la MTU.
    * Sin embargo, cambiar la MTU es generalmente un paso de solución de problemas más avanzado y debe hacerse con precaución.
5.  **Verificar la Configuración de DNS:**
    * Intenta usar un servidor DNS público, como Google DNS (8.8.8.8 y 8.8.4.4) o Cloudflare DNS (1.1.1.1 y 1.0.0.1).
    * Puedes configurar los ajustes de DNS en las preferencias de red de tu macOS.
6.  **Usar un Proxy para Git:**
    * Si tienes acceso a un servidor proxy, puedes configurar Git para usarlo.
    * Establece las variables de configuración de Git `http.proxy` y `https.proxy`:
        ```bash
        git config --global http.proxy http://direccion_proxy:puerto_proxy
        git config --global https.proxy https://direccion_proxy:puerto_proxy
        ```
    * Si el proxy necesita autenticación, puedes incluir el nombre de usuario y la contraseña en la URL del proxy.
7.  **Intentar usar SSH sobre Websockets:**
    * Algunas herramientas y servicios te permiten tunelizar tráfico SSH sobre websockets, lo que puede ser útil si los puertos SSH estándar están bloqueados.
    * Esta es una técnica más avanzada y requiere configurar un servidor que admita SSH sobre websockets.

**Consideraciones Importantes:**

* Las condiciones de la red móvil pueden variar significativamente, por lo que lo que funciona en una ubicación o en un momento dado podría no funcionar en otro.
* Ten en cuenta los términos de servicio de tu proveedor de red móvil y cualquier restricción potencial sobre el uso de VPNs u otras soluciones.
* HTTPS es generalmente la mejor solución para la mayoría de los usuarios.