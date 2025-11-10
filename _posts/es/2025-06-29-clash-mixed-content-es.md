---
audio: false
generated: true
lang: es
layout: post
title: Corrección de Errores de Contenido Mixto en Clash VPN
translated: true
type: note
---

Los mensajes de error que estás viendo indican un problema de **contenido mixto** con la aplicación Clash VPN, específicamente cuando la página en `https://clash.razord.top/` intenta cargar recursos desde un endpoint inseguro `http://127.0.0.1:9090/` (por ejemplo, `http://127.0.0.1:9090/version`). Los navegadores modernos bloquean estas solicitudes porque violan las políticas de seguridad al intentar cargar contenido HTTP inseguro en una página HTTPS segura. Además, hay errores de CORS (Cross-Origin Resource Sharing) debido a restricciones de control de acceso. A continuación, se presenta una guía paso a paso para resolver este problema.

---

### Por qué sucede esto
- **Error de Contenido Mixto**: La página web se sirve a través de HTTPS, pero intenta obtener recursos (como la verificación de versión) desde `http://127.0.0.1:9090`, que es inseguro. Los navegadores bloquean estas solicitudes para prevenir posibles vulnerabilidades de seguridad, como ataques de intermediario.
- **Error de CORS**: El navegador está bloqueando la solicitud a `http://127.0.0.1:9090` debido a la política CORS, que restringe las solicitudes de origen cruzado a menos que el servidor las permita explícitamente.
- **Contexto de Clash**: Clash (o Clash for Windows) es una aplicación proxy que probablemente utiliza un servidor local (`127.0.0.1:9090`) para su panel de control o API. Si este servidor local no admite HTTPS o no está configurado correctamente, desencadena estos errores cuando se accede a través de una página web HTTPS.

---

### Pasos para solucionar el problema

#### 1. **Verificar la configuración del Clash Core**
   - **Comprobar si Clash Core se está ejecutando**: Asegúrate de que el núcleo de Clash (el servicio backend) se esté ejecutando en tu máquina y escuchando en `127.0.0.1:9090`. Puedes verificarlo:
     - Abriendo una terminal o símbolo del sistema.
     - Ejecutando `curl http://127.0.0.1:9090/version` para comprobar si el endpoint responde con la versión de Clash.
     - Si no responde, asegúrate de que el servicio Clash esté activo. Reinicia Clash for Windows o el proceso del núcleo de Clash.
   - **Habilitar HTTPS para Clash Core** (si es posible):
     - Algunas versiones de Clash (por ejemplo, Clash Premium o Clash Meta) admiten HTTPS para la API local. Consulta la documentación de Clash o el archivo de configuración (generalmente `config.yaml`) para encontrar una opción que habilite HTTPS para el controlador externo (el endpoint de la API).
     - Busca una configuración como `external-controller` o `external-ui` en el archivo de configuración. Por ejemplo:
       ```yaml
       external-controller: 127.0.0.1:9090
       external-ui: <ruta-a-la-ui>
       ```
       Si HTTPS es compatible, es posible que necesites configurar un certificado para el servidor local. Esto es avanzado y puede requerir generar un certificado autofirmado (consulta el paso 4 a continuación).

#### 2. **Acceder al panel de control a través de HTTP (Solución temporal)**
   - Si se puede acceder al panel de control de Clash a través de HTTP (por ejemplo, `http://clash.razord.top/` en lugar de HTTPS), intenta cargarlo sin HTTPS para evitar problemas de contenido mixto:
     - Abre tu navegador y navega a `http://clash.razord.top/`.
     - Nota: Esto no se recomienda para uso en producción, ya que HTTP es inseguro. Úsalo solo para pruebas o si el panel de control solo se accede localmente.
   - Si el panel de control requiere HTTPS, procede con los siguientes pasos para abordar la causa principal.

#### 3. **Actualizar las URL a HTTPS**
   - El error sugiere que el panel de control de Clash está intentando obtener recursos desde `http://127.0.0.1:9090`. Si tienes acceso al código fuente o la configuración del panel de control de Clash:
     - Revisa el código frontend (por ejemplo, `index-5e90ca00.js` o `vendor-827b5617.js`) en busca de referencias codificadas a `http://127.0.0.1:9090`.
     - Actualízalas a `https://127.0.0.1:9090` si el núcleo de Clash admite HTTPS, o usa una URL relativa (por ejemplo, `/version`) para permitir que el navegador use el mismo protocolo que la página.
     - Si no tienes acceso al código fuente, es posible que necesites configurar un proxy inverso (consulta el paso 4).

#### 4. **Configurar un proxy inverso con HTTPS**
   - Para resolver el problema de contenido mixto, puedes configurar un proxy inverso (por ejemplo, usando Nginx o Caddy) para servir la API del núcleo de Clash (`http://127.0.0.1:9090`) a través de HTTPS. Esto permite que el panel de control se comunique con el núcleo de forma segura.
   - **Pasos para Nginx**:
     1. Instala Nginx en tu sistema (si aún no está instalado).
     2. Genera un certificado SSL autofirmado para `127.0.0.1`:
        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -subj "/CN=localhost"
        ```
     3. Configura Nginx para redirigir las solicitudes a `http://127.0.0.1:9090` a través de HTTPS. Crea un archivo de configuración (por ejemplo, `/etc/nginx/sites-available/clash`):
        ```nginx
        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate /ruta/a/localhost.crt;
            ssl_certificate_key /ruta/a/localhost.key;

            location / {
                proxy_pass http://127.0.0.1:9090;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        ```
     4. Habilita la configuración y reinicia Nginx:
        ```bash
        sudo ln -s /etc/nginx/sites-available/clash /etc/nginx/sites-enabled/
        sudo nginx -t
        sudo systemctl restart nginx
        ```
     5. Actualiza el panel de control de Clash para usar `https://localhost:443` en lugar de `http://127.0.0.1:9090` para las solicitudes de la API.
     6. En tu navegador, acepta el certificado autofirmado cuando se te solicite.

   - **Alternativa con Caddy**: Caddy es más simple de configurar y maneja HTTPS automáticamente:
     1. Instala Caddy.
     2. Crea un `Caddyfile`:
        ```caddy
        localhost:443 {
            reverse_proxy http://127.0.0.1:9090
        }
        ```
     3. Ejecuta Caddy: `caddy run`.
     4. Actualiza el panel de control de Clash para usar `https://localhost:443`.

#### 5. **Evitar las restricciones de CORS (Avanzado)**
   - El error de CORS (`XMLHttpRequest cannot load http://127.0.0.1:9090/version due to access control checks`) indica que el servidor del núcleo de Clash no está enviando los encabezados CORS apropiados. Si controlas el núcleo de Clash:
     - Modifica la configuración del núcleo de Clash para incluir encabezados CORS, como:
       ```yaml
       external-controller: 127.0.0.1:9090
       allow-cors: true
       ```
       (Consulta la documentación de Clash para la sintaxis exacta, ya que esto depende de la versión de Clash).
     - Alternativamente, la configuración del proxy inverso en el paso 4 puede manejar CORS agregando encabezados como:
       ```nginx
       add_header Access-Control-Allow-Origin "https://clash.razord.top";
       add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
       add_header Access-Control-Allow-Headers "*";
       ```
   - Si no controlas el núcleo, puedes usar una extensión del navegador para evitar temporalmente CORS (por ejemplo, "CORS Unblock" para Chrome), pero esto no se recomienda por razones de seguridad.

#### 6. **Actualizar Clash o cambiar a una versión compatible**
   - Asegúrate de estar usando la última versión de Clash for Windows o Clash Verge, ya que las versiones anteriores pueden tener errores o carecer de soporte HTTPS para el controlador externo.
   - Consulta el repositorio de GitHub de Clash (`github.com/Dreamacro/clash` o `github.com/Fndroid/clash_for_windows_pkg`) en busca de actualizaciones o problemas reportados relacionados con contenido mixto o CORS.
   - Considera cambiar a **Clash Verge** o **Clash Meta**, que pueden tener un mejor soporte para HTTPS y las políticas de seguridad modernas de los navegadores.

#### 7. **Permitir contenido inseguro en el navegador (No recomendado)**
   - Como último recurso, puedes permitir contenido inseguro en tu navegador para `https://clash.razord.top/`:
     - **Chrome**:
       1. Haz clic en el icono del candado en la barra de direcciones.
       2. Ve a "Configuración del sitio" > "Contenido no seguro" > Establecer en "Permitir".
     - **Firefox**:
       1. Haz clic en el icono del candado y ve a "Configuración de conexión".
       2. Desactiva "Bloquear contenido peligroso y engañoso" temporalmente.
     - **Advertencia**: Esto evita las protecciones de seguridad y solo debe usarse para pruebas locales en redes confiables.
   - Alternativamente, inicia Chrome con el indicador `--disable-web-security` (solo para desarrollo):
     ```bash
     google-chrome --disable-web-security --user-data-dir="/tmp/chrome_dev"
     ```

#### 8. **Verificar extensiones conflictivas o firewall**
   - Las extensiones del navegador (por ejemplo, bloqueadores de anuncios, herramientas de privacidad) o la configuración del firewall pueden interferir con el servidor local de Clash. Desactiva las extensiones temporalmente o verifica tu firewall para asegurarte de que `127.0.0.1:9090` sea accesible.
   - En Windows, asegúrate de que la aplicación Clash tenga permisos de firewall:
     - Ve a Configuración > Red e Internet > Firewall de Windows > Permitir una aplicación a través del firewall.
     - Agrega o habilita Clash for Windows.

#### 9. **Contactar al soporte o la comunidad de Clash**
   - Si los pasos anteriores no resuelven el problema, informa del problema en la página de issues de GitHub de Clash for Windows (`github.com/Fndroid/clash_for_windows_pkg/issues`) o en los foros de la comunidad de Clash. Proporciona detalles sobre tu configuración, incluyendo:
     - Versión de Clash.
     - Sistema operativo.
     - Archivo de configuración (omite información sensible).
     - Navegador y versión.
   - Busca problemas similares en la comunidad, ya que este error puede ser específico de ciertas versiones o configuraciones de Clash.

---

### Enfoque recomendado
La solución más segura y robusta es **configurar un proxy inverso con HTTPS** (paso 4) para garantizar que todas las solicitudes se sirvan a través de HTTPS, resolviendo tanto los problemas de contenido mixto como los de CORS. Si no puedes modificar el núcleo o el panel de control de Clash, usar una versión más nueva de Clash (por ejemplo, Clash Verge) o acceder al panel de control a través de HTTP temporalmente (paso 2) pueden ser soluciones más rápidas.

---

### Notas adicionales
- Si estás usando un panel de control personalizado de Clash o un servicio de terceros como `clash.razord.top`, verifica que sea compatible con tu versión del núcleo de Clash.
- Siempre haz una copia de seguridad de tu configuración de Clash (`config.yaml`) antes de realizar cambios.
- Si el problema persiste, puedes intentar cambiar a clientes proxy alternativos como v2rayN u OpenVPN, que pueden tener un mejor soporte HTTPS para las API locales.

¡Avísame si necesitas ayuda con pasos específicos, como configurar Nginx o depurar la configuración de Clash!