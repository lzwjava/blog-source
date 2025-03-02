---
audio: true
generated: true
lang: es
layout: post
title: Usando Dos Routers
translated: true
---

Para configurar tus dos routers TP-Link AX3000 (TL-XDR 3050) con tu módem en la configuración **Modem → Cable → Router1 → Wireless → Router2**, sigue esta guía paso a paso. Tu módem ya tiene funcionalidad WiFi y una dirección IP de `192.168.1.1`. Configuraremos Router1 como el router principal conectado al módem mediante un cable y Router2 para extender la red de manera inalámbrica.

Aquí te explicamos cómo hacerlo:

---

### **Paso 1: Entender la Configuración**
- **Módem**: Proporciona acceso a internet y tiene su propio WiFi (IP: `192.168.1.1`).
- **Router1**: Se conectará al módem con un cable y actuará como el router principal para tu red.
- **Router2**: Se conectará de manera inalámbrica a Router1 para extender la cobertura de la red.

Has mencionado varios modos (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Usaremos **DHCP** para Router1 para obtener una conexión a internet desde el módem y **Wireless AP Bridge** (o un modo similar como WDS/Repeater) para Router2 para conectarse de manera inalámbrica a Router1.

---

### **Paso 2: Configurar Router1**
1. **Conectar Router1 al Módem**:
   - Toma un cable Ethernet y conecta un extremo a un **puerto LAN** en tu módem.
   - Conecta el otro extremo al **puerto WAN (Internet)** en Router1.

2. **Acceder a la Interfaz Web de Router1**:
   - Conecta una computadora o smartphone a la red WiFi predeterminada de Router1 (revisa la etiqueta del router para el SSID y la contraseña predeterminados) o usa un cable Ethernet.
   - Abre un navegador web y escribe `http://tplinkwifi.net` o `192.168.0.1` (la IP predeterminada para routers TP-Link).
   - Inicia sesión con las credenciales predeterminadas (generalmente `admin` para ambos nombre de usuario y contraseña) a menos que las hayas cambiado.

3. **Configurar Router1**:
   - **Conexión a Internet**:
     - Ve a **Quick Setup** o la sección de configuración de **Internet**.
     - Selecciona el modo **DHCP**. Esto permite que Router1 obtenga automáticamente una dirección IP del módem (probablemente en el rango `192.168.1.x`).
   - **Configuración de WiFi**:
     - Establece un **SSID** (nombre de la red) único y una **contraseña** fuerte para el WiFi de Router1.
     - Guarda estos detalles, ya que Router2 los necesitará para conectarse de manera inalámbrica.
   - **Configuración de LAN**:
     - Asegúrate de que la IP LAN de Router1 sea diferente a la IP del módem. Por defecto, probablemente sea `192.168.0.1`, lo cual está bien ya que el módem es `192.168.1.1`.
     - Confirma que **DHCP** esté habilitado en Router1. Esto permite que Router1 asigne direcciones IP (por ejemplo, `192.168.0.x`) a dispositivos conectados a él, incluyendo Router2.
   - Guarda la configuración y reinicia Router1 si se te solicita.

---

### **Paso 3: Configurar Router2 como un Puente Inalámbrico**
1. **Acceder a la Interfaz Web de Router2**:
   - Conecta una computadora o smartphone a la red WiFi predeterminada de Router2 o mediante Ethernet.
   - Abre un navegador web y escribe `http://tplinkwifi.net` o `192.168.0.1`.
   - Inicia sesión con las credenciales predeterminadas (o las personalizadas).

2. **Configurar Router2 en Modo Puente Inalámbrico**:
   - Busca un modo como **Wireless AP Bridge**, **WDS** o **Repeater** en la configuración (probablemente bajo **Operation Mode** o **Wireless** settings).
   - Selecciona **Wireless AP Bridge** (o WDS/Repeater si es lo que está disponible).
   - **Conectar a la Red WiFi de Router1**:
     - Escanea las redes disponibles y selecciona el SSID de Router1.
     - Ingresa la contraseña del WiFi de Router1.
     - Asegúrate de que Router2 use el mismo canal inalámbrico que Router1 para compatibilidad (por ejemplo, si Router1 está en el Canal 6, configura Router2 en el Canal 6).
   - **Configuración de IP LAN**:
     - Cambia la IP LAN de Router2 para evitar conflictos con Router1. Por ejemplo, configúrala en `192.168.0.2` (ya que Router1 probablemente sea `192.168.0.1`).
     - **Deshabilita DHCP** en Router2. Router1 manejará la asignación de IPs para todos los dispositivos.
   - Guarda la configuración y reinicia Router2. Ahora debería conectarse de manera inalámbrica a Router1.

---

### **Paso 4: Probar la Configuración**
1. **Verificar la Conexión de Router2**:
   - Después de reiniciar, verifica la interfaz de Router2 para confirmar que está conectado al WiFi de Router1.
2. **Conectar un Dispositivo a Router2**:
   - Usa un smartphone, laptop u otro dispositivo para conectarte al WiFi de Router2 (puede usar el mismo SSID que Router1, dependiendo del modo).
   - Verifica que el dispositivo obtenga una dirección IP de Router1 (por ejemplo, `192.168.0.x`).
   - Prueba el acceso a internet navegando en un sitio web.

---

### **Resumen de la Configuración Final**
- **Módem**: IP `192.168.1.1`, proporciona internet y WiFi.
- **Router1**:
  - WAN: Conectado al módem mediante cable, configurado en **DHCP** (obtiene IP del módem, por ejemplo, `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP habilitado** para asignar IPs a dispositivos.
  - WiFi: SSID y contraseña personalizados.
- **Router2**:
  - Modo: **Wireless AP Bridge** (o WDS/Repeater), conectado de manera inalámbrica al WiFi de Router1.
  - IP LAN: `192.168.0.2`, **DHCP deshabilitado**.

---

### **Consejos de Solución de Problemas**
- **Router2 No Se Conecta Inalámbricamente**:
  - Verifica nuevamente el SSID, la contraseña y la configuración del canal de Router1 en la configuración de Router2.
  - Si **Wireless AP Bridge** no está disponible, intenta el modo **WDS** o **Repeater**. Consulta el manual del TP-Link AX3000 para los modos soportados.
- **Sin Internet en Router2**:
  - Asegúrate de que el DHCP de Router1 esté funcionando y el DHCP de Router2 esté deshabilitado.
  - Verifica que Router2 esté conectado correctamente a Router1.
- **Preocupaciones de Double NAT**:
  - Dado que tu módem tiene WiFi y Router1 actúa como router, podrías tener double NAT (módem y Router1 ambos asignando IPs). Esto generalmente está bien para uso básico, pero podría afectar algunas aplicaciones (por ejemplo, juegos). Si es necesario, configura el módem en **modo puente** (consulta el manual de tu módem), aunque esto podría deshabilitar su WiFi.

Con esta configuración, Router2 extenderá tu red de manera inalámbrica desde Router1, y los dispositivos conectados a cualquiera de los routers deberían acceder a internet a través del módem. ¡Hazme saber si necesitas más asistencia!

---

Si decides usar una dirección IP fija (estática) para el primer router (Router1) en lugar de confiar en DHCP, deberás configurar manualmente sus ajustes WAN para comunicarse con tu módem. Aquí está lo que deberías configurar para la dirección IP, DNS, máscara de subred y puerta de enlace:

---

### **Suposiciones**
- Tu módem tiene una dirección IP de `192.168.1.1` y usa la subred `192.168.1.0/24` (máscara de subred `255.255.255.0`).
- El módem tiene un rango DHCP (por ejemplo, `192.168.1.2` a `192.168.1.100`) que asigna direcciones IP a dispositivos conectados.

Si tu módem usa una IP o subred diferente, ajusta los valores en consecuencia.

---

### **Configuración WAN para Router1**
Estos ajustes configuran cómo Router1 se conecta al módem:

1. **Dirección IP**
   - Elige una IP estática dentro de la subred del módem (`192.168.1.0/24`) pero **fuera del rango DHCP del módem** para evitar conflictos.
   - Ejemplo: Si el rango DHCP del módem es `192.168.1.2` a `192.168.1.100`, puedes usar **`192.168.1.101`**.
   - Esto asegura que Router1 tenga una dirección IP única en la red del módem.

2. **Máscara de Subred**
   - Configúrala para que coincida con la máscara de subred del módem, que generalmente es **`255.255.255.0`**.
   - Esto define el rango de red como `192.168.1.0` a `192.168.1.255`.

3. **Puerta de Enlace Predeterminada**
   - Configúrala a la dirección IP del módem, que es **`192.168.1.1`**.
   - La puerta de enlace es el dispositivo (tu módem) que Router1 usa para acceder a internet.

4. **Servidores DNS**
   - Tienes dos opciones:
     - Usar la IP del módem: **`192.168.1.1`**. Esto permite que el módem maneje las solicitudes DNS.
     - Usar servidores DNS públicos: **`8.8.8.8`** (Google) y **`8.8.4.4`** (Google secundario). Estos son confiables y a menudo más rápidos.
   - Recomendación: Empieza con `192.168.1.1`. Si experimentas problemas DNS, cambia a `8.8.8.8` y `8.8.4.4`.

---

### **Configuración de Ejemplo**
Aquí es como podrían verse los ajustes WAN de Router1:

- **Dirección IP**: `192.168.1.101`
- **Máscara de Subred**: `255.255.255.0`
- **Puerta de Enlace Predeterminada**: `192.168.1.1`
- **Servidor DNS**: `192.168.1.1` (o `8.8.8.8` y `8.8.4.4`)

---

### **Notas Adicionales**
- **Verificar Configuración del Módem**: Inicia sesión en tu módem (generalmente en `192.168.1.1`) para confirmar su IP, máscara de subred y rango DHCP. Ajusta la IP estática de Router1 si es necesario.
- **Configuración LAN para Router1**: Para evitar conflictos, configura la red LAN de Router1 en una subred diferente, como `192.168.0.1` con una máscara de subred de `255.255.255.0`. Habilita DHCP en Router1 para asignar IPs (por ejemplo, `192.168.0.2` a `192.168.0.254`) a dispositivos conectados a él.
- **Pruebas**: Después de aplicar estos ajustes, asegúrate de que Router1 pueda acceder a internet. Si no, verifica la IP (sin conflictos), la puerta de enlace y los valores DNS.

Esta configuración da a Router1 una IP fija en la red del módem, asegurando una conectividad consistente. ¡Hazme saber si necesitas ayuda con routers adicionales o detalles específicos del módem!

---

Suena como si hubieras configurado Router1 con una IP WAN estática y configurado su LAN con DHCP, pero tu laptop aún no puede conectarse a la red. Vamos a solucionar esto paso a paso para averiguar por qué y cómo solucionarlo.

---

### Paso 1: Verificar la Conexión WAN de Router1
Tus ajustes WAN son:

- **Dirección IP**: `192.168.1.101`
- **Máscara de Subred**: `255.255.255.0`
- **Puerta de Enlace Predeterminada**: `192.168.1.1`
- **Servidor DNS**: `192.168.1.1` (o `8.8.8.8` y `8.8.4.4`)

Estos ajustes sugieren que Router1 está conectado a un módem o a otro router con una IP de `192.168.1.1`. Aquí está lo que debes verificar:

- **Acceso a Internet en Router1**:
  - Inicia sesión en la interfaz web de Router1 (probablemente en `192.168.0.1` desde tus ajustes LAN a continuación).
  - Ve a la sección **Estado** o **WAN** para ver si Router1 muestra una conexión a internet activa. Si no lo hace, el problema podría estar entre Router1 y el módem.

- **Conflicto de IP**:
  - Asegúrate de que ningún otro dispositivo en la red del módem esté usando `192.168.1.101`. Si el rango DHCP del módem incluye esta IP, podría causar un conflicto. Inicia sesión en el módem (en `192.168.1.1`) y verifica sus ajustes DHCP o la lista de dispositivos conectados. Si `192.168.1.101` está dentro del rango DHCP del módem, cambia la IP WAN de Router1 a algo fuera de ese rango (por ejemplo, `192.168.1.200`) o exclúyela del pool DHCP del módem.

- **Conectividad del Módem**:
  - Confirma que el cable Ethernet esté conectado al **puerto LAN** del módem y al **puerto WAN** de Router1. Si esto no está configurado correctamente, Router1 no se conectará a internet.

---

### Paso 2: Verificar los Ajustes LAN y DHCP de Router1
Tus ajustes LAN y DHCP son:

- **IP LAN**: `192.168.0.1`
- **Máscara de Subred**: `255.255.255.0`
- **DHCP Habilitado**: Sí
- **Rango de Direcciones IP**: `192.168.0.2` a `192.168.0.254`
- **Puerta de Enlace**: `192.168.0.1`
- **Servidor DNS**: `192.168.0.1`

Estos parecen sólidos, pero asegúrate de que funcionen:

- **Funcionalidad DHCP**:
  - Con DHCP habilitado, tu laptop debería obtener automáticamente una dirección IP entre `192.168.0.2` y `192.168.0.254`, con una puerta de enlace de `192.168.0.1`. Si no lo hace, DHCP podría no estar funcionando correctamente.

- **Configuración DNS**:
  - Configurar el servidor DNS a `192.168.0.1` significa que Router1 maneja las solicitudes DNS para tu laptop. Asegúrate de que Router1 esté configurado para reenviar estas solicitudes a un servidor DNS de nivel superior (como `192.168.1.1` o `8.8.8.8`). Esto generalmente es automático, pero verifícalo en los ajustes de Router1. Alternativamente, podrías configurar el DNS DHCP directamente a `8.8.8.8` y `8.8.4.4` para evitar Router1 para DNS.

---

### Paso 3: Probar la Conexión de la Laptop
Dado que tu laptop no se conecta, vamos a diagnosticarla:

- **Tipo de Conexión**:
  - ¿Estás usando WiFi o Ethernet? Si es WiFi, asegúrate de conectarte al SSID de Router1 (no al del módem). Si es Ethernet, confirma que el cable esté conectado a uno de los puertos LAN de Router1.

- **Verificar la Dirección IP de la Laptop**:
  - En tu laptop, abre un **Símbolo del sistema** (Windows) o **Terminal** (macOS/Linux):
    - Windows: Escribe `ipconfig` y presiona Enter.
    - macOS/Linux: Escribe `ifconfig` o `ip addr` y presiona Enter.
  - Busca la dirección IP del adaptador de red. Debería ser algo como `192.168.0.x` (donde `x` está entre 2 y 254), con una máscara de subred de `255.255.255.0` y una puerta de enlace de `192.168.0.1`.
  - **Si No Hay Dirección IP**:
    - Tu laptop podría no estar obteniendo una IP de DHCP. Asegúrate de que sus ajustes de red estén configurados para “Obtener una dirección IP automáticamente.” Intenta renovar la IP:
      - Windows: Ejecuta `ipconfig /release` luego `ipconfig /renew`.
    - Si aún falla, DHCP en Router1 o la conexión a él podría ser el problema.

- **Ping a Router1**:
  - Desde tu laptop, ejecuta `ping 192.168.0.1`. Si obtienes respuestas, tu laptop está conectada a Router1 pero podría no tener acceso a internet. Si se agota el tiempo, la laptop no alcanza Router1.

---

### Paso 4: Problemas Comunes y Soluciones
Aquí hay algunos posibles culpables:

- **Problemas de Cable**:
  - Si usas Ethernet, prueba con un cable diferente o un puerto LAN diferente en Router1. Un cable o puerto defectuoso podría impedir la conectividad.

- **Problemas de WiFi**:
  - Si estás en WiFi, verifica nuevamente la contraseña y asegúrate de que el WiFi de Router1 esté habilitado. La interferencia de señal o un SSID mal configurado también podrían ser el problema.

- **Conexión Router1-Módem**:
  - Si Router1 no obtiene una conexión a internet, el módem podría requerir configuraciones específicas (por ejemplo, clonación de dirección MAC). Verifica el manual del módem o sus ajustes para esto.

- **Double NAT**:
  - Tu configuración tiene el módem (en `192.168.1.1`) y Router1 (en `192.168.0.1`) ambos actuando como routers. Esto generalmente no bloquea la conectividad básica, pero configurar el módem en **modo puente** (si es posible) podría simplificar las cosas.

- **Firewall**:
  - El firewall de Router1 podría estar bloqueando tu laptop. Deshabilita temporalmente cualquier regla de firewall personalizada para probar.

---

### Paso 5: Reiniciar si es Necesario
Si nada funciona, reinicia Router1 y vuelve a configurarlo:

- **Restablecimiento de Fábrica**:
  - Presiona y mantén el botón de reinicio de Router1 durante 10 segundos, luego vuelve a configurar los ajustes WAN y DHCP como los mencionaste.

- **Intenta WAN Dinámico**:
  - En lugar de una IP WAN estática, configura el WAN de Router1 en **DHCP** para ver si puede obtener una IP del módem automáticamente. Si esto funciona, la IP estática (`192.168.1.101`) podría ser el problema.

---

### Consejos Finales
- **Rango DHCP del Módem**: Confirma que `192.168.1.101` esté fuera del rango DHCP del módem para evitar conflictos.
- **Firmware**: Verifica en la interfaz web de Router1 si hay una actualización de firmware.
- **Controladores de la Laptop**: Asegúrate de que los controladores del adaptador de red de tu laptop estén actualizados.

Sigue estos pasos y deberías poder identificar por qué tu laptop no se conecta. Si aún estás atascado, házmelo saber qué encuentras en cada paso; ¡te ayudaré a reducirlo más!