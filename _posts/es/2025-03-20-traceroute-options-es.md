---
audio: false
generated: true
lang: es
layout: post
title: Opciones de Traceroute
translated: true
type: note
---

Traceroute es una herramienta poderosa para diagnosticar rutas de red, y aunque su uso básico es sencillo, ofrece opciones avanzadas para personalizar su comportamiento. A continuación, describiré las opciones comunes y explicaré cómo usar traceroute de manera avanzada, centrándome en ejemplos prácticos. Las opciones exactas dependen de su sistema operativo (por ejemplo, Windows usa `tracert`, mientras que Linux/macOS usan `traceroute`), pero cubriré las más ampliamente aplicables.

### Uso Básico
- **Linux/macOS**: `traceroute [destino]`
  - Ejemplo: `traceroute google.com`
- **Windows**: `tracert [destino]`
  - Ejemplo: `tracert google.com`

Esto muestra los saltos (routers) entre usted y el objetivo, junto con los tiempos de ida y vuelta (RTT) para cada uno.

---

### Opciones Comunes de Traceroute
Aquí hay un resumen de las opciones clave, principalmente para el comando `traceroute` en sistemas tipo Unix (Linux/macOS). Windows `tracert` tiene menos opciones pero comparte algunos conceptos.

1. **`-n` (Sin Búsqueda DNS)**  
   - Omite la resolución de direcciones IP a nombres de host, acelerando el proceso y mostrando las IPs en crudo.
   - Uso: `traceroute -n google.com`
   - Por qué: Útil cuando la resolución DNS es lenta o solo le importan las IPs.

2. **`-m [max_saltos]` (Establecer Saltos Máximos)**  
   - Limita cuántos saltos verifica traceroute antes de rendirse (el valor predeterminado suele ser 30).
   - Uso: `traceroute -m 15 google.com`
   - Por qué: Evita ejecuciones interminables si el objetivo es inalcanzable o está muy lejano.

3. **`-q [nconsultas]` (Número de Consultas por Salto)**  
   - Establece cuántos paquetes se envían por salto (el valor predeterminado es 3). Cada consulta muestra un valor de latencia.
   - Uso: `traceroute -q 1 google.com`
   - Por qué: Reduce el desorden de la salida o acelera el trazado; auméntelo para obtener datos de latencia más confiables.

4. **`-w [tiempo_espera]` (Tiempo de Espera por Salto)**  
   - Establece cuánto tiempo (en segundos) esperar por una respuesta antes de marcar un salto como agotado el tiempo.
   - Uso: `traceroute -w 2 google.com`
   - Por qué: Se adapta a redes lentas o reduce retrasos en redes rápidas.

5. **`-p [puerto]` (Especificar Puerto, Modo UDP)**  
   - Establece el puerto de destino para traceroute basado en UDP (el valor predeterminado suele ser 33434+).
   - Uso: `traceroute -p 53 google.com`
   - Por qué: Apunta a servicios específicos (por ejemplo, DNS en el puerto 53) o evita filtros que bloquean ICMP.

6. **`-I` (Usar ICMP en lugar de UDP)**  
   - Cambia de UDP (predeterminado en muchos sistemas) a paquetes ICMP Echo Request.
   - Uso: `traceroute -I google.com`
   - Por qué: Algunas redes bloquean UDP pero permiten ICMP, mejorando la visibilidad.

7. **`-T` (Modo TCP)**  
   - Utiliza paquetes TCP en lugar de UDP o ICMP, a menudo con paquetes SYN.
   - Uso: `traceroute -T -p 80 google.com`
   - Por qué: Evita firewalls que bloquean ICMP/UDP; ideal para rastrear servidores web (puerto 80 = HTTP).

8. **`-f [ttl_inicial]` (Comenzar en un TTL Específico)**  
   - Establece el valor TTL inicial, omitiendo saltos anteriores.
   - Uso: `traceroute -f 5 google.com`
   - Por qué: Se centra en una parte específica de la ruta, por ejemplo, más allá de su red local.

9. **`-g [puerta_enlace]` (Enrutamiento de Fuente No Estricto)**  
   - Fuerza a los paquetes a pasar por una puerta de enlace especificada (si la red lo admite).
   - Uso: `traceroute -g 192.168.1.1 google.com`
   - Por qué: Prueba rutas específicas o evita el enrutamiento predeterminado.

10. **`-4` o `-6` (Forzar IPv4 o IPv6)**  
    - Restringe traceroute a IPv4 o IPv6.
    - Uso: `traceroute -6 google.com`
    - Por qué: Asegura que está probando un protocolo específico, útil para redes de doble pila.

---

### Opciones de Windows `tracert`
Windows tiene menos opciones, pero estas son las principales:
- **`-d`**: Sin búsquedas DNS (como `-n`).
- **`-h [max_saltos]`**: Saltos máximos (como `-m`).
- **`-w [tiempo_espera]`**: Tiempo de espera en milisegundos (como `-w`).
- Ejemplo: `tracert -d -h 20 google.com`

---

### Ejemplos de Uso Avanzado
Aquí se explica cómo combinar opciones para propósitos específicos:

1. **Diagnosticar una Conexión Lenta**  
   - Objetivo: Identificar dónde se producen picos de latencia.
   - Comando: `traceroute -I -q 5 -w 1 google.com`
   - Por qué: ICMP para confiabilidad, 5 consultas para mejores estadísticas de latencia, tiempo de espera de 1 segundo para avanzar rápidamente.

2. **Evitar Restricciones del Firewall**  
   - Objetivo: Rastrear un servidor web bloqueado por filtros ICMP.
   - Comando: `traceroute -T -p 443 google.com`
   - Por qué: TCP en el puerto 443 (HTTPS) imita tráfico legítimo, a menudo permitido a través de firewalls.

3. **Probar Más Allá de Su ISP**  
   - Objetivo: Omitir saltos locales para centrarse en el enrutamiento externo.
   - Comando: `traceroute -f 3 -m 10 google.com`
   - Por qué: Comienza en el salto 3 (pasando su router/ISP), limita a 10 saltos en total.

4. **Comparar Rutas IPv4 vs. IPv6**  
   - Objetivo: Ver si la elección del protocolo afecta el enrutamiento.
   - Comandos: 
     - `traceroute -4 google.com`
     - `traceroute -6 google.com`
   - Por qué: Identifica diferencias en las rutas de red o el rendimiento.

5. **Trazado Rápido y Silencioso para Scripting**  
   - Objetivo: Salida rápida para automatización.
   - Comando: `traceroute -n -q 1 -w 1 google.com > salida.txt`
   - Por qué: Sin DNS, una consulta, tiempo de espera corto, redirigido a un archivo.

---

### Consejos para Uso Avanzado
- **Combinar con Otras Herramientas**: Combine traceroute con `ping` (para latencia) o `mtr` (traceroute en tiempo real) para obtener información más profunda.
- **Comprender el Contexto de la Red**: Firewalls, NAT o VPNs pueden ocultar saltos (mostrando asteriscos `*`)—ajuste los protocolos (ICMP/TCP) para adaptarse.
- **Privilegios de Root**: En sistemas Unix, algunas opciones (por ejemplo, modo TCP) pueden requerir `sudo` para acceso a sockets raw: `sudo traceroute -T google.com`.

El poder de traceroute reside en su flexibilidad. Al ajustar las opciones, puede personalizarlo para solucionar problemas específicos de red, evitar restricciones o analizar el comportamiento del enrutamiento en detalle. ¡Avíseme si desea profundizar en un escenario particular!