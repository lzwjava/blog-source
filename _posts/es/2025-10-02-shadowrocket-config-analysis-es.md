---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Análisis del Archivo de Configuración de Shadowrocket
translated: true
type: note
---

Esto parece ser un archivo de configuración para Shadowrocket, una aplicación proxy basada en reglas para iOS (similar a herramientas como Surge o Quantumult). Está estructurado como un archivo de configuración basado en texto que define cómo la aplicación enruta el tráfico, maneja el DNS, aplica reglas y realiza reescrituras o intercepción MITM (man-in-the-middle). El archivo tiene la fecha "2025-10-02 20:25:43", que podría ser una marca de tiempo o un marcador de posición.

Lo explicaré sección por sección, desglosando cada parte, qué hace y por qué podría estar configurado de esta manera. Esta configuración parece estar optimizada para usuarios en regiones con restricciones de internet (por ejemplo, China), enrutando ciertos servicios globales/bloqueados a través de un servidor proxy mientras mantiene el tráfico local/doméstico directo para una mejor velocidad y para evitar redirecciones innecesarias. No es una configuración completa— aún necesitarías configurar un servidor proxy (por ejemplo, vía Shadowsocks, V2Ray, etc.) por separado en la aplicación, y esta configuración hace referencia a conjuntos de reglas externos que se actualizan automáticamente desde GitHub.

### Suposiciones y Notas Clave
- **Configuración del Proxy**: Esta configuración asume que tienes un servidor proxy funcionando configurado en Shadowrocket (por ejemplo, SOCKS5, HTTP o protocolos cifrados). Sin eso, las reglas "PROXY" no funcionarán.
- **Propósito**: Parece ser para eludir la censura (por ejemplo, el Gran Firewall en China). Los servicios de IA (como OpenAI/ChatGPT) se proxyfican, mientras que los dominios/IPs chinos van directos para evitar throttling.
- **Modo TUN**: Hace referencia a "tun" (modo túnel) para enrutar todo el tráfico a través del dispositivo.
- **Dependencias Externas**: Algunas reglas se cargan desde URLs de GitHub (por ejemplo, listas de reglas). Asegúrate de confiar en estas fuentes, ya que pueden actualizarse automáticamente.
- Si algo no está claro o necesitas ayuda para aplicarlo, házmelo saber con detalles sobre tu configuración.

### Desglose por Secciones

#### **[General]**
Esto establece los comportamientos globales de la aplicación, la resolución DNS y el enrutamiento de red. Es como las "preferencias" o "configuraciones del sistema" para Shadowrocket.

- `bypass-system = true`: Ignora la configuración del proxy del sistema de iOS. Shadowrocket maneja todo el proxyficado por sí mismo en lugar de depender de configuraciones globales del sistema.

- `skip-proxy = 192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com`: Una lista separada por comas de dominios/rangos de IP para **enrutar siempre directamente** (sin proxy). Esto incluye:
  - Redes privadas (por ejemplo, IPs de Wi-Fi doméstico como 192.168.x.x).
  - Dominios locales (*.local) y localhost.
  - La comprobación de portal cautivo de Apple.
  - Dominios de bancos chinos (*.ccb.com para China Construction Bank, *.abchina.com.cn para Agricultural Bank of China, *.psbc.com para Postal Savings Bank).
  - Baidu (www.baidu.com), un motor de búsqueda chino importante.
  - *¿Por qué?* Los sitios chinos domésticos (especialmente bancos y búsquedas) son accesibles sin proxy y podrían sufrir throttling o ser marcados si se enrutan a través de uno.

- `tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32, 239.255.255.250/32`: En el modo túnel (TUN), estos rangos de IP están **excluidos** del túnel proxy. Esto evita interferencias con el tráfico local/de enrutamiento como IPs de loopback, multidifusión y rangos de prueba.

- `dns-server = https://doh.pub/dns-query,https://dns.alidns.com/dns-query,223.5.5.5,119.29.29.29`: Lista priorizada de resolvers DNS para el tráfico proxy. Estos son servidores DoH (DNS sobre HTTPS) y DNS plano (Tencent's 119.29.29.29 y Aliyun's 223.5.5.5). Comienza con los cifrados/públicos (doh.pub y alidns.com) para privacidad/seguridad.

- `fallback-dns-server = system`: Si el DNS primario falla, recurre al DNS del sistema de iOS.

- `ipv6 = true`: Habilita el soporte para IPv6. `prefer-ipv6 = false`: Prefiere IPv4 sobre IPv6 para las conexiones (por ejemplo, por estabilidad o compatibilidad).

- `dns-direct-system = false`: No usar el DNS del sistema para conexiones directas—usar el DNS configurado en su lugar.

- `icmp-auto-reply = true`: Responde automáticamente a las solicitudes ICMP (ping). Útil para comprobaciones de conectividad.

- `always-reject-url-rewrite = false`: Permitir que se activen las reescrituras de URL (usadas más adelante en la configuración).

- `private-ip-answer = true`: Permitir respuestas DNS con IPs privadas (por ejemplo, tu router).

- `dns-direct-fallback-proxy = true`: Si una consulta DNS directa falla, reintentar a través del proxy.

- `tun-included-routes = `: (Vacío) No hay rutas personalizadas incluidas en el modo TUN—usa los valores por defecto.

- `always-real-ip = `: (Vacío) No hay exposición forzada de IP real—comportamiento estándar.

- `hijack-dns = 8.8.8.8:53,8.8.4.4:53`: Intercepta el tráfico DNS del DNS público de Google (8.8.8.8/8.8.4.4 en el puerto 53) y lo enruta a través del proxy. Esto usa forzosamente tu DNS configurado en lugar de los públicos, que podrían estar bloqueados o monitorizados.

- `udp-policy-not-supported-behaviour = REJECT`: Si el tráfico UDP no es compatible con una política, rechazarlo en lugar de permitirlo.

- `include = `: (Vacío) No se incluyen archivos de configuración adicionales.

- `update-url = `: (Vacío) No hay actualizaciones automáticas de configuración desde una URL.

#### **[Rule]**
Esto define las reglas de enrutamiento de tráfico, procesadas en orden. Es como una ACL (lista de control de acceso) que le dice a Shadowrocket qué proxyficar, qué enviar directo, basándose en dominios, palabras clave, GEOIP, etc. Si ninguna regla coincide, cae en `FINAL,DIRECT`.

- `DOMAIN-SUFFIX,anthropic.com,PROXY`: Enruta todos los subdominios de anthropic.com a través del proxy (por ejemplo, api.anthropic.com). Anthropic es una compañía de IA—probablemente para eludir bloques.

- `DOMAIN-SUFFIX,chatgpt.com,PROXY`: Enruta los dominios de ChatGPT a través del proxy. ChatGPT a menudo está restringido en ciertas regiones.

- `DOMAIN-SUFFIX,openai.com,PROXY`: Enruta los dominios de OpenAI a través del proxy (razón similar).

- `DOMAIN-SUFFIX,googleapis.com,PROXY`: Enruta los servicios API de Google a través del proxy (podría ser para acceder a servicios de Google indirectamente).

- `DOMAIN-SUFFIX,zhs.futbol,DIRECT`: Enruta este dominio específico (probablemente un sitio deportivo en español/chino) directamente.

- `RULE-SET,https://github.com/lzwjava/lzwjava.github.io/raw/refs/heads/main/scripts/auto-ss-config/AI.list,PROXY`: Carga un conjunto de reglas externo desde GitHub (una lista de dominios relacionados con IA) y los proxyfica. Esto se actualiza automáticamente y expande las reglas de proxy para IA.

- `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Lan/Lan.list,DIRECT`: Carga un conjunto de reglas para la red de área local (LAN) y los enruta directamente. Evita proxyficar el tráfico doméstico/interno.

- `DOMAIN-KEYWORD,cn,DIRECT`: Cualquier dominio que contenga la palabra clave "cn" (por ejemplo, cualquiercosa.cn) va directo. Útil para sitios chinos.

- `GEOIP,CN,DIRECT`: Cualquier IP geolocalizada en China (CN) va directo. Evita proxyficar el tráfico doméstico, que es rápido y sin restricciones.

- `FINAL,DIRECT`: Acción por defecto—si no coincide ninguna regla, enrutar directamente. Mantiene la mayor parte del tráfico sin proxyficar para eficiencia.

*Efecto General*: Esta es una configuración de "proxy para globales bloqueados". El tráfico de IA/ChatGPT/OpenAI se fuerza a través de VPN/proxy para eludir las restricciones regionales, mientras que lo chino/local permanece directo.

#### **[Host]**
Mapeos manuales de host (como un archivo de hosts local).

- `localhost = 127.0.0.1`: Mapea "localhost" a la IP de loopback. Estándar—asegura que la aplicación pueda conectarse a servicios locales.

#### **[URL Rewrite]**
Reescribe las URLs entrantes antes de que se realicen las solicitudes. Usa coincidencia de regex.

- `^https?://(www.)?g.cn https://www.google.com 302`: Reescribe cualquier URL HTTP/HTTPS para g.cn (o www.g.cn) para redirigir a google.com con un estado 302 (redirección temporal). g.cn es el dominio de Google en China— esto lo evita.

- `^https?://(www.)?google.cn https://www.google.com 302`: Lo mismo para google.cn a google.com. China a menudo bloquea o redirige google.com, así que esto fuerza una redirección limpia.

*¿Por qué?* En regiones censuradas, google.cn podría servir resultados alterados/prohibidos. Esto asegura que accedas al sitio global de Google directamente.

#### **[MITM]**
Configuraciones de man-in-the-middle para interceptar y modificar el tráfico HTTPS (requiere un certificado de CA raíz en Shadowrocket).

- `hostname = *.google.cn`: Intercepta el tráfico para cualquier subdominio de google.cn. Combinado con la reescritura de URL, esto podría descifrar/redirigir el tráfico para los dominios de Google CN.

*¿Por qué?* Esto podría ser para hacer cumplir las reescrituras o manejar problemas de certificate pinning en China, donde google.cn usa certificados diferentes.

### Cómo Usar Esta Configuración
1.  **Importar**: En Shadowrocket, importa esto como un archivo de configuración.
2.  **Servidor Proxy**: Añade tu proxy real (por ejemplo, servidor Shadowsocks) en la sección "Servers"—las reglas como "PROXY" dependen de ello.
3.  **Habilitar**: Cambia a esta configuración y habilita el modo túnel (VPN) si es necesario.
4.  **Certificado CA**: Para MITM, instala y confía en la CA de Shadowrocket si aún no lo has hecho.
5.  **Probar**: Comprueba sitios como whatismyipaddress.com para ver si las IPs/el enrutamiento funcionan como se espera. Monitoriza si los sitios chinos van lentos.
6.  **Solución de Problemas**: Si los conjuntos de reglas no se cargan, podrían estar limitados por tasa o haber cambiado. Las preferencias de IPv6 podrían necesitar activarse/desactivarse para la conectividad.

### Posibles Problemas/Notas de Seguridad
-   **Privacidad**: Los conjuntos de reglas expuestos (enlaces de GitHub) podrían filtrar lo que estás enrutando. MITM puede interceptar tráfico sensible—usa solo CAs de confianza.
-   **Actualizaciones**: Los conjuntos de reglas se cargan automáticamente; si GitHub está bloqueado, usa un proxy para ellos.
-   **Fecha Futura**: La configuración está etiquetada como Oct 2025—podría ser un error tipográfico o una futura prueba, pero ninguna característica depende de ello.
-   **Legalidad**: El uso de proxy para evadir la censura está bien en algunos lugares pero restringido en otros—úsalo bajo tu propio riesgo.
-   Si compartes registros de error o lo que estás intentando lograr, ¡puedo refinar los consejos!