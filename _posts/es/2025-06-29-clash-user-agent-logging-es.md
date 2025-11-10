---
audio: false
generated: true
lang: es
layout: post
title: Registro de User-Agent en Clash Proxy
translated: true
type: note
---

Parece que te refieres a **Clash**, una utilidad de proxy basada en reglas, y deseas configurarla para imprimir o registrar el **User-Agent** de sus peticiones HTTP. Según la información disponible, Clash (o su núcleo, a menudo referido como `clash-core`) no tiene una función integrada para imprimir directamente el User-Agent de las peticiones salientes de forma sencilla. Sin embargo, puedes lograr esto aprovechando las opciones de configuración de Clash, herramientas externas o métodos de depuración. A continuación, se presenta una guía paso a paso para ayudarte a registrar o inspeccionar el User-Agent de las peticiones realizadas a través de Clash.

---

### Comprendiendo el Contexto
- **Clash** es una utilidad de proxy que enruta el tráfico basándose en reglas y soporta protocolos como HTTP, SOCKS5, Shadowsocks, V2Ray y más. Opera en las capas de red y aplicación.
- El **User-Agent** es una cabecera HTTP típicamente establecida por la aplicación cliente (por ejemplo, un navegador o una herramienta como `curl`) que realiza la petición, no por el propio Clash. Clash, como proxy, reenvía estas peticiones y puede no registrar o modificar el User-Agent de forma inherente a menos que se configure explícitamente para hacerlo.
- Para imprimir el User-Agent, necesitas:
  1. Configurar Clash para registrar las cabeceras HTTP (incluyendo User-Agent) para depuración.
  2. Usar una herramienta externa (por ejemplo, un depurador de proxy o un sniffer de red) para inspeccionar las peticiones.
  3. Modificar la configuración de Clash para añadir cabeceras personalizadas o usar un script para registrarlas.

Dado que Clash en sí mismo no tiene una configuración directa para registrar las cabeceras User-Agent, puede que necesites combinar Clash con otras herramientas o usar configuraciones específicas. A continuación se presentan los métodos para lograr esto.

---

### Método 1: Habilitar el Registro Detallado en Clash e Inspeccionar los Logs
Clash puede registrar peticiones en varios niveles, pero no registra de forma nativa las cabeceras HTTP como el User-Agent a menos que se configure explícitamente o se use con una herramienta que pueda inspeccionar el tráfico. Puedes habilitar el registro detallado y usar una herramienta para capturar el User-Agent.

#### Pasos:
1. **Establecer el Nivel de Log de Clash a Debug**:
   - Edita tu archivo de configuración de Clash (`config.yaml`, típicamente ubicado en `~/.config/clash/config.yaml` o un directorio personalizado especificado con la bandera `-d`).
   - Establece `log-level` a `debug` para capturar información detallada sobre las peticiones:
     ```yaml
     log-level: debug
     ```
   - Guarda la configuración y reinicia Clash:
     ```bash
     clash -d ~/.config/clash
     ```
   - Clash ahora registrará información más detallada en `STDOUT` o en un archivo de log especificado. Sin embargo, esto puede no incluir la cabecera User-Agent directamente, ya que Clash se centra en los detalles de enrutamiento y conexión.

2. **Inspeccionar los Logs**:
   - Revisa la salida de los logs en la terminal o en el archivo de log (si está configurado). Busca detalles de las peticiones HTTP, pero ten en cuenta que el registro por defecto de Clash puede no incluir las cabeceras HTTP completas como User-Agent.
   - Si no ves información del User-Agent, procede a usar un proxy de depuración (ver Método 2) o un sniffer de red (Método 3).

3. **Opcional: Usar el Dashboard de Clash**:
   - Clash proporciona un dashboard basado en web (por ejemplo, YACD en `https://yacd.haishan.me/` o el dashboard oficial en `https://clash.razord.top/`) para monitorizar conexiones y logs.
   - Configura `external-controller` y `external-ui` en tu `config.yaml` para habilitar el dashboard:
     ```yaml
     external-controller: 127.0.0.1:9090
     external-ui: folder
     ```
   - Accede al dashboard via `http://127.0.0.1:9090/ui` y revisa la pestaña "Logs" o "Connections". Esto puede mostrar detalles de conexión pero es poco probable que muestre el User-Agent directamente.

#### Limitaciones:
- Los logs de depuración de Clash se centran en las decisiones de enrutamiento y proxy, no en las cabeceras HTTP completas. Para capturar el User-Agent, necesitas interceptar el tráfico HTTP, lo que requiere herramientas adicionales.

---

### Método 2: Usar un Proxy de Depuración para Capturar el User-Agent
Dado que Clash en sí mismo no registra directamente las cabeceras HTTP como User-Agent, puedes enrutar el tráfico de Clash a través de un proxy de depuración como **mitmproxy**, **Charles Proxy** o **Fiddler**. Estas herramientas pueden interceptar y mostrar la petición HTTP completa, incluyendo el User-Agent.

#### Pasos:
1. **Instalar mitmproxy**:
   - Instala `mitmproxy`, una herramienta de código abierto popular para interceptar tráfico HTTP/HTTPS:
     ```bash
     sudo apt install mitmproxy  # En Debian/Ubuntu
     brew install mitmproxy      # En macOS
     ```
   - Alternativamente, usa otra herramienta de proxy como Charles o Fiddler.

2. **Configurar Clash para Enrutar Tráfico a través de mitmproxy**:
   - Por defecto, Clash actúa como un proxy HTTP/SOCKS5. Puedes encadenarlo a `mitmproxy` estableciendo `mitmproxy` como el proxy ascendente.
   - Edita tu `config.yaml` de Clash para incluir un proxy HTTP que apunte a `mitmproxy`:
     ```yaml
     proxies:
       - name: mitmproxy
         type: http
         server: 127.0.0.1
         port: 8080  # Puerto por defecto de mitmproxy
     proxy-groups:
       - name: Proxy
         type: select
         proxies:
           - mitmproxy
     ```
   - Guarda la configuración y reinicia Clash.

3. **Iniciar mitmproxy**:
   - Ejecuta `mitmproxy` para que escuche en el puerto 8080:
     ```bash
     mitmproxy
     ```
   - `mitmproxy` mostrará todas las peticiones HTTP que pasen a través de él, incluyendo la cabecera User-Agent.

4. **Enviar una Petición de Prueba**:
   - Usa un cliente (por ejemplo, `curl`, un navegador u otra herramienta) configurado para usar Clash como proxy.
   - Ejemplo con `curl`:
     ```bash
     curl --proxy http://127.0.0.1:7890 http://example.com
     ```
   - En `mitmproxy`, verás la petición HTTP completa, incluyendo el User-Agent (por ejemplo, `curl/8.0.1` o el User-Agent del navegador).

5. **Inspeccionar el User-Agent**:
   - En la interfaz de `mitmproxy`, navega a través de las peticiones capturadas. La cabecera User-Agent será visible en los detalles de la petición.
   - También puedes guardar los logs en un archivo para un análisis posterior:
     ```bash
     mitmproxy -w mitmproxy.log
     ```

#### Notas:
- Si estás usando HTTPS, necesitas instalar y confiar en el certificado CA de `mitmproxy` en tu dispositivo cliente para descifrar el tráfico HTTPS. Sigue las instrucciones en `http://mitm.clash/cert.crt` o en la documentación de `mitmproxy`.
- Este método requiere encadenar proxies (Cliente → Clash → mitmproxy → Destino), lo que puede aumentar ligeramente la latencia pero permite la inspección completa de las cabeceras.

---

### Método 3: Usar un Sniffer de Red para Capturar el User-Agent
Si prefieres no encadenar proxies, puedes usar un sniffer de red como **Wireshark** para capturar e inspeccionar el tráfico HTTP que pasa a través de Clash.

#### Pasos:
1. **Instalar Wireshark**:
   - Descarga e instala Wireshark desde [wireshark.org](https://www.wireshark.org/).
   - En Linux:
     ```bash
     sudo apt install wireshark
     ```
   - En macOS:
     ```bash
     brew install wireshark
     ```

2. **Iniciar Clash**:
   - Asegúrate de que Clash esté ejecutándose con tu configuración deseada (por ejemplo, proxy HTTP en el puerto 7890):
     ```bash
     clash -d ~/.config/clash
     ```

3. **Capturar Tráfico en Wireshark**:
   - Abre Wireshark y selecciona la interfaz de red que Clash esté usando (por ejemplo, `eth0`, `wlan0` o `lo` para tráfico localhost).
   - Aplica un filtro para capturar tráfico HTTP:
     ```
     http
     ```
   - Alternativamente, filtra por el puerto del proxy HTTP de Clash (por ejemplo, 7890):
     ```
     tcp.port == 7890
     ```

4. **Enviar una Petición de Prueba**:
   - Usa un cliente configurado para usar Clash como proxy:
     ```bash
     curl --proxy http://127.0.0.1:7890 http://example.com
     ```

5. **Inspeccionar el User-Agent**:
   - En Wireshark, busca peticiones HTTP (por ejemplo, `GET / HTTP/1.1`). Haz doble clic en un paquete para ver sus detalles.
   - Expande la sección "Hypertext Transfer Protocol" para encontrar la cabecera `User-Agent` (por ejemplo, `User-Agent: curl/8.0.1`).

#### Notas:
- Para tráfico HTTPS, Wireshark no puede descifrar el User-Agent a menos que tengas la clave privada del servidor o uses una herramienta como `mitmproxy` para descifrar el tráfico.
- Este método es más complejo y requiere familiaridad con el análisis de paquetes de red.

---

### Método 4: Modificar la Configuración de Clash para Inyectar o Registrar Cabeceras Personalizadas
Clash soporta cabeceras HTTP personalizadas en su configuración para ciertos tipos de proxy (por ejemplo, HTTP o VMess). Puedes configurar Clash para inyectar un User-Agent específico o usar un script para registrar las cabeceras. Sin embargo, esto es menos directo para registrar el User-Agent de todas las peticiones.

#### Pasos:
1. **Añadir Cabecera User-Agent Personalizada**:
   - Si quieres forzar un User-Agent específico para pruebas, modifica la sección `proxies` en `config.yaml` para incluir una cabecera personalizada:
     ```yaml
     proxies:
       - name: my-http-proxy
         type: http
         server: proxy.example.com
         port: 8080
         header:
           User-Agent:
             - "MyCustomUserAgent/1.0"
     ```
   - Esto establece un User-Agent personalizado para las peticiones enviadas a través de este proxy. Sin embargo, sobrescribe el User-Agent original del cliente, lo que puede no ser lo que deseas si estás intentando registrar el User-Agent del cliente.

2. **Usar Reglas de Script para Registrar Cabeceras**:
   - Clash soporta reglas basadas en script usando motores como `expr` o `starlark` (). Puedes escribir un script para registrar o procesar cabeceras, incluyendo User-Agent.[](https://pkg.go.dev/github.com/yaling888/clash)
   - Ejemplo de configuración:
     ```yaml
     script:
       engine: starlark
       code: |
         def match(req):
           print("User-Agent:", req.headers["User-Agent"])
           return "Proxy"  # Enrutar a un grupo de proxy
     ```
   - Esto requiere escribir un script personalizado, lo cual es avanzado y puede no estar totalmente soportado en todas las versiones de Clash. Consulta la documentación de Clash para el soporte de scripts.

3. **Verificar con mitmproxy o Wireshark**:
   - Después de inyectar un User-Agent personalizado, usa el Método 2 o el Método 3 para confirmar que el User-Agent se está enviando como se espera.

#### Limitaciones:
- Inyectar un User-Agent personalizado sobrescribe el User-Agent del cliente, por lo que esto sólo es útil para probar User-Agents específicos.
- El registro basado en scripts es experimental y puede no estar disponible en todas las versiones de Clash.

---

### Método 5: Usar el Proxy MITM de Clash para Registrar Cabeceras
Clash soporta un modo de proxy **Man-in-the-Middle (MITM)** que puede interceptar y registrar tráfico HTTPS, incluyendo cabeceras como User-Agent.

#### Pasos:
1. **Habilitar MITM en Clash**:
   - Edita `config.yaml` para habilitar el proxy MITM:
     ```yaml
     mitm-port: 7894
     mitm:
       hosts:
         - "*.example.com"
     ```
   - Esto configura Clash para interceptar tráfico HTTPS para los dominios especificados.

2. **Instalar el Certificado CA de Clash**:
   - Clash genera un certificado CA para MITM. Accede a `http://mitm.clash/cert.crt` en un navegador para descargarlo e instalarlo.
   - Confía en el certificado en tu dispositivo cliente para permitir que Clash descifre el tráfico HTTPS.

3. **Inspeccionar los Logs**:
   - Con MITM habilitado, Clash puede registrar información de petición más detallada, incluyendo cabeceras. Revisa los logs en la terminal o en el dashboard.
   - Si las cabeceras no se registran, usa `mitmproxy` (Método 2) para capturar el tráfico descifrado.

#### Notas:
- El modo MITM requiere confiar en el certificado CA en todos los dispositivos cliente, lo que puede no ser práctico para todos los casos de uso.
- Este método es mejor para tráfico HTTPS pero requiere configuración adicional.

---

### Recomendaciones
- **Método Preferido**: Usa el **Método 2 (mitmproxy)** para la forma más fácil y fiable de capturar y registrar el User-Agent de las peticiones. Es de código abierto, ampliamente soportado y está diseñado para la depuración HTTP.
- **Alternativa**: Usa el **Método 3 (Wireshark)** si te sientes cómodo con el análisis de paquetes de red y no quieres encadenar proxies.
- **Para Usuarios Avanzados**: Experimenta con el **Método 4 (Cabeceras Personalizadas o Scripts)** si necesitas manipular o registrar cabeceras programáticamente dentro de Clash.

---

### Notas Adicionales
- **Documentación de Clash**: Consulta la documentación oficial de Clash (,) para detalles de configuración. El repositorio de GitHub (`https://github.com/Dreamacro/clash`) y la wiki (`https://en.clash.wiki`) proporcionan guías detalladas.[](https://en.clash.wiki/)[](https://en.clash.wiki/configuration/getting-started.html)
- **User-Agent del Lado del Cliente**: El User-Agent es establecido por el cliente (por ejemplo, navegador, `curl` o aplicación), no por Clash. Asegúrate de que tu cliente está enviando el User-Agent esperado. Por ejemplo:
  - `curl` usa `curl/<versión>` por defecto.
  - Los navegadores usan sus propias cadenas de User-Agent (por ejemplo, `Mozilla/5.0 ...`).
- **Pruebas**: Siempre prueba con una petición HTTP simple (por ejemplo, `curl --proxy http://127.0.0.1:7890 http://example.com`) para verificar la configuración.
- **Seguridad**: Cuando uses MITM o proxies de depuración, asegúrate de confiar en los certificados CA y las herramientas para evitar riesgos de seguridad.

Si necesitas más aclaraciones o asistencia con configuraciones específicas, ¡por favor proporciona más detalles sobre tu configuración (por ejemplo, versión de Clash, sistema operativo o tipo de proxy específico) y puedo adaptar las instrucciones aún más!