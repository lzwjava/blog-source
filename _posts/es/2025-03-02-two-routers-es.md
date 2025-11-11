---
audio: false
generated: true
lang: es
layout: post
title: Uso de dos enrutadores
translated: true
type: note
---

Para configurar tus dos routers TP-Link AX3000 (TL-XDR 3050) con tu módem en la configuración **Módem → Cable → Router1 → Inalámbrico → Router2**, sigue esta guía paso a paso. Tu módem ya tiene funcionalidad WiFi y una dirección IP de `192.168.1.1`. Configuraremos el Router1 como el router principal conectado al módem mediante un cable y el Router2 para extender la red de forma inalámbrica.

Así es como lograrlo:

---

### **Paso 1: Comprender la Configuración**
- **Módem**: Proporciona acceso a Internet y tiene su propia WiFi (IP: `192.168.1.1`).
- **Router1**: Se conectará al módem con un cable y actuará como el router principal de tu red.
- **Router2**: Se conectará de forma inalámbrica al Router1 para extender la cobertura de la red.

Has mencionado varios modos (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Usaremos **DHCP** para que el Router1 obtenga una conexión a Internet desde el módem y **Wireless AP Bridge** (o un modo similar como WDS/Repetidor) para que el Router2 se conecte de forma inalámbrica al Router1.

---

### **Paso 2: Configurar el Router1**
1. **Conectar el Router1 al Módem**:
   - Toma un cable Ethernet y conecta un extremo a un **puerto LAN** de tu módem.
   - Conecta el otro extremo al **puerto WAN (Internet)** del Router1.

2. **Acceder a la Interfaz Web del Router1**:
   - Conecta una computadora o smartphone a la red WiFi predeterminada del Router1 (revisa la etiqueta del router para ver el SSID y contraseña predeterminados) o usa un cable Ethernet.
   - Abre un navegador web y escribe `http://tplinkwifi.net` o `192.168.0.1` (la IP predeterminada para routers TP-Link).
   - Inicia sesión con las credenciales predeterminadas (generalmente `admin` para usuario y contraseña) a menos que las hayas cambiado.

3. **Configurar el Router1**:
   - **Conexión a Internet**:
     - Ve a **Configuración Rápida** o a la sección de configuración de **Internet**.
     - Selecciona el modo **DHCP**. Esto permite que el Router1 obtenga automáticamente una dirección IP del módem (probablemente en el rango `192.168.1.x`).
   - **Configuración WiFi**:
     - Establece un **SSID** (nombre de red) único y una **contraseña** segura para el WiFi del Router1.
     - Guarda estos detalles, ya que el Router2 los necesitará para conectarse de forma inalámbrica.
   - **Configuración LAN**:
     - Asegúrate de que la IP LAN del Router1 sea diferente a la IP del módem. Por defecto, es probablemente `192.168.0.1`, lo cual está bien ya que el módem es `192.168.1.1`.
     - Confirma que el **DHCP** esté habilitado en el Router1. Esto permite que el Router1 asigne direcciones IP (ej. `192.168.0.x`) a los dispositivos conectados a él, incluido el Router2.
   - Guarda la configuración y reinicia el Router1 si se solicita.

---

### **Paso 3: Configurar el Router2 como Puente Inalámbrico**
1. **Acceder a la Interfaz Web del Router2**:
   - Conecta una computadora o smartphone a la red WiFi predeterminada del Router2 o mediante Ethernet.
   - Abre un navegador web y escribe `http://tplinkwifi.net` o `192.168.0.1`.
   - Inicia sesión con las credenciales predeterminadas (o las personalizadas).

2. **Configurar el Router2 en Modo Puente Inalámbrico**:
   - Busca un modo como **Wireless AP Bridge**, **WDS** o **Repetidor** en la configuración (probablemente en **Modo de Operación** o configuración **Wireless**).
   - Selecciona **Wireless AP Bridge** (o WDS/Repetidor si es lo que está disponible).
   - **Conectarse al WiFi del Router1**:
     - Escanea las redes disponibles y selecciona el SSID del Router1.
     - Ingresa la contraseña WiFi del Router1.
     - Asegúrate de que el Router2 use el mismo canal inalámbrico que el Router1 para compatibilidad (ej. si el Router1 está en el Canal 6, configura el Router2 al Canal 6).
   - **Configuración de IP LAN**:
     - Cambia la IP LAN del Router2 para evitar conflictos con el Router1. Por ejemplo, configúrala a `192.168.0.2` (ya que el Router1 es probablemente `192.168.0.1`).
     - **Deshabilita el DHCP** en el Router2. El Router1 manejará las asignaciones de IP para todos los dispositivos.
   - Guarda la configuración y reinicia el Router2. Ahora debería conectarse de forma inalámbrica al Router1.

---

### **Paso 4: Probar la Configuración**
1. **Verificar la Conexión del Router2**:
   - Después del reinicio, revisa la interfaz del Router2 para confirmar que está conectado al WiFi del Router1.
2. **Conectar un Dispositivo al Router2**:
   - Usa un smartphone, laptop u otro dispositivo para conectarte al WiFi del Router2 (puede usar el mismo SSID que el Router1, dependiendo del modo).
   - Verifica que el dispositivo obtenga una dirección IP del Router1 (ej. `192.168.0.x`).
   - Prueba el acceso a Internet navegando a un sitio web.

---

### **Resumen de la Configuración Final**
- **Módem**: IP `192.168.1.1`, proporciona Internet y WiFi.
- **Router1**:
  - WAN: Conectado al módem por cable, configurado en **DHCP** (obtiene IP del módem, ej. `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP habilitado** para asignar IPs a los dispositivos.
  - WiFi: SSID y contraseña personalizados.
- **Router2**:
  - Modo: **Wireless AP Bridge** (o WDS/Repetidor), conectado de forma inalámbrica al WiFi del Router1.
  - IP LAN: `192.168.0.2`, **DHCP deshabilitado**.

---

### **Consejos para Solucionar Problemas**
- **Router2 No Se Conecta de Forma Inalámbrica**:
  - Verifica nuevamente el SSID, la contraseña y la configuración del canal del Router1 en la configuración del Router2.
  - Si **Wireless AP Bridge** no está disponible, prueba el modo **WDS** o **Repetidor**. Consulta el manual del TP-Link AX3000 para los modos soportados.
- **Sin Internet en el Router2**:
  - Asegúrate de que el DHCP del Router1 esté funcionando y el DHCP del Router2 esté desactivado.
  - Verifica que el Router2 se esté puenteando exitosamente al Router1.
- **Preocupaciones de Doble NAT**:
  - Dado que tu módem tiene WiFi y el Router1 actúa como un router, podrías tener doble NAT (el módem y el Router1 asignando IPs). Esto generalmente está bien para uso básico, pero podría afectar algunas aplicaciones (ej. juegos). Si es necesario, configura el módem en **modo bridge** (consulta el manual de tu módem), aunque esto puede deshabilitar su WiFi.

Con esta configuración, el Router2 extenderá tu red de forma inalámbrica desde el Router1, y los dispositivos conectados a cualquier router deberían acceder a Internet a través del módem. ¡Avísame si necesitas más ayuda!

---

Si decides usar una dirección IP fija (estática) para el primer router (Router1) en lugar de depender de DHCP, necesitarás configurar manualmente sus ajustes WAN para comunicarse con tu módem. Esto es lo que deberías configurar para la dirección IP, DNS, máscara de subred y puerta de enlace:

---

### **Suposiciones**
- Tu módem tiene una dirección IP de `192.168.1.1` y usa la subred `192.168.1.0/24` (máscara de subred `255.255.255.0`).
- El módem tiene un rango DHCP (ej. `192.168.1.2` a `192.168.1.100`) que asigna direcciones IP a los dispositivos conectados.

Si tu módem usa una IP o subred diferente, ajusta los valores en consecuencia.

---

### **Configuración WAN para el Router1**
Estos ajustes configuran cómo el Router1 se conecta al módem:

1. **Dirección IP**
   - Elige una IP estática dentro de la subred del módem (`192.168.1.0/24`) pero **fuera del rango DHCP del módem** para evitar conflictos.
   - Ejemplo: Si el rango DHCP del módem es `192.168.1.2` a `192.168.1.100`, puedes usar **`192.168.1.101`**.
   - Esto asegura que el Router1 tenga una dirección única y fija en la red del módem.

2. **Máscara de Subred**
   - Configúrala para que coincida con la máscara de subred del módem, que típicamente es **`255.255.255.0`**.
   - Esto define el rango de red como `192.168.1.0` a `192.168.1.255`.

3. **Puerta de Enlace Predeterminada**
   - Configúrala con la dirección IP del módem, que es **`192.168.1.1`**.
   - La puerta de enlace es el dispositivo (tu módem) que el Router1 usa para acceder a Internet.

4. **Servidores DNS**
   - Tienes dos opciones:
     - Usar la IP del módem: **`192.168.1.1`**. Esto permite que el módem maneje las solicitudes DNS.
     - Usar servidores DNS públicos: **`8.8.8.8`** (Google) y **`8.8.4.4`** (Google secundario). Estos son confiables y a menudo más rápidos.
   - Recomendación: Comienza con `192.168.1.1`. Si experimentas problemas de DNS, cambia a `8.8.8.8` y `8.8.4.4`.

---

### **Ejemplo de Configuración**
Así podrían verse tus ajustes WAN del Router1:

- **Dirección IP**: `192.168.1.101`
- **Máscara de Subred**: `255.255.255.0`
- **Puerta de Enlace Predeterminada**: `192.168.1.1`
- **Servidor DNS**: `192.168.1.1` (o `8.8.8.8` y `8.8.4.4`)

---

### **Notas Adicionales**
- **Verificar Configuración del Módem**: Inicia sesión en tu módem (generalmente en `192.168.1.1`) para confirmar su IP, máscara de subred y rango DHCP. Ajusta la IP estática del Router1 si es necesario.
- **Configuración LAN para el Router1**: Para evitar conflictos, configura la red LAN del Router1 en una subred diferente, como `192.168.0.1` con una máscara de subred de `255.255.255.0`. Habilita DHCP en el Router1 para asignar IPs (ej. `192.168.0.2` a `192.168.0.254`) a los dispositivos conectados a él.
- **Pruebas**: Después de aplicar estos ajustes, asegúrate de que el Router1 pueda acceder a Internet. Si no, verifica la IP (sin conflictos), la puerta de enlace y los valores DNS.

Esta configuración le da al Router1 una IP fija en la red del módem, asegurando una conectividad consistente. ¡Avísame si necesitas ayuda con routers adicionales o detalles específicos del módem!

---

Parece que has configurado el Router1 con una IP WAN estática y configurado su LAN con DHCP, pero tu laptop aún no puede conectarse a la red. Solucionemos esto paso a paso para averiguar por qué y cómo solucionarlo.

---

### Paso 1: Verificar la Conexión WAN del Router1
Tus ajustes WAN son:

- **Dirección IP**: `192.168.1.101`
- **Máscara de Subred**: `255.255.255.0`
- **Puerta de Enlace Predeterminada**: `192.168.1.1`
- **Servidor DNS**: `192.168.1.1` (o `8.8.8.8` y `8.8.4.4`)

Estos ajustes sugieren que el Router1 está conectado a un módem u otro router con una IP de `192.168.1.1`. Esto es lo que debes verificar:

- **Acceso a Internet en el Router1**:
  - Inicia sesión en la interfaz web del Router1 (probablemente en `192.168.0.1` según tu configuración LAN a continuación).
  - Ve a la sección **Estado** o **WAN** para ver si el Router1 muestra una conexión a Internet activa. Si no es así, el problema podría estar entre el Router1 y el módem.

- **Conflicto de IP**:
  - Asegúrate de que ningún otro dispositivo en la red del módem esté usando `192.168.1.101`. Si el rango DHCP del módem incluye esta IP, podría causar un conflicto. Inicia sesión en el módem (en `192.168.1.1`) y revisa su configuración DHCP o la lista de dispositivos conectados. Si `192.168.1.101` está dentro del rango DHCP del módem, cambia la IP WAN del Router1 a algo fuera de ese rango (ej. `192.168.1.200`) o exclúyela del grupo DHCP del módem.

- **Conectividad del Módem**:
  - Confirma que el cable Ethernet esté conectado al **puerto LAN** del módem y al **puerto WAN** del Router1. Si esto no está configurado correctamente, el Router1 no se conectará a Internet.

---

### Paso 2: Verificar la Configuración LAN y DHCP del Router1
Tu configuración LAN y DHCP es:

- **IP LAN**: `192.168.0.1`
- **Máscara de Subred**: `255.255.255.0`
- **DHCP Habilitado**: Sí
- **Rango de Direcciones IP**: `192.168.0.2` a `192.168.0.254`
- **Puerta de Enlace**: `192.168.0.1`
- **Servidor DNS**: `192.168.0.1`

Esto parece sólido, pero asegurémonos de que esté funcionando:

- **Funcionalidad DHCP**:
  - Con DHCP habilitado, tu laptop debería obtener automáticamente una dirección IP entre `192.168.0.2` y `192.168.0.254`, con una puerta de enlace de `192.168.0.1`. Si no es así, es posible que el DHCP no esté funcionando correctamente.

- **Configuración DNS**:
  - Configurar el servidor DNS a `192.168.0.1` significa que el Router1 maneja las solicitudes DNS para tu laptop. Asegúrate de que el Router1 esté configurado para reenviar estas solicitudes a un servidor DNS ascendente (como `192.168.1.1` o `8.8.8.8`). Esto suele ser automático, pero verifica nuevamente en la configuración del Router1. Alternativamente, podrías configurar el DNS del DHCP a `8.8.8.8` y `8.8.4.4` directamente para omitir el Router1 para DNS.

---

### Paso 3: Probar la Conexión de tu Laptop
Dado que tu laptop no se conecta, diagnostiquemos:

- **Tipo de Conexión**:
  - ¿Estás usando WiFi o Ethernet? Si es WiFi, asegúrate de estar conectándote al SSID del Router1 (no al del módem). Si es Ethernet, confirma que el cable esté conectado a uno de los puertos LAN del Router1.

- **Verificar la Dirección IP de la Laptop**:
  - En tu laptop, abre un **Símbolo del sistema** (Windows) o **Terminal** (macOS/Linux):
    - Windows: Escribe `ipconfig` y presiona Enter.
    - macOS/Linux: Escribe `ifconfig` o `ip addr` y presiona Enter.
  - Busca la dirección IP de tu adaptador de red. Debería ser algo como `192.168.0.x` (donde `x` está entre 2 y 254), con una máscara de subred de `255.255.255.0` y puerta de enlace `192.168.0.1`.
  - **Si No Hay Dirección IP**:
    - Es posible que tu laptop no esté obteniendo una IP del DHCP. Asegúrate de que su configuración de red esté establecida en "Obtener una dirección IP automáticamente". Intenta renovar la IP:
      - Windows: Ejecuta `ipconfig /release` luego `ipconfig /renew`.
    - Si aún falla, el DHCP en el Router1 o la conexión a él podría ser el problema.

- **Hacer Ping al Router1**:
  - Desde tu laptop, ejecuta `ping 192.168.0.1`. Si obtienes respuestas, tu laptop está conectada al Router1 pero podría no tener acceso a Internet. Si se agota el tiempo de espera, la laptop no está llegando al Router1.

---

### Paso 4: Problemas Comunes y Soluciones
Estos son algunos culpables probables:

- **Problemas con el Cable**:
  - Si usas Ethernet, prueba con un cable o puerto LAN diferente en el Router1. Un cable o puerto defectuoso podría impedir la conectividad.

- **Problemas de WiFi**:
  - Si estás en WiFi, verifica nuevamente la contraseña y asegúrate de que el WiFi del Router1 esté habilitado. La interferencia de señal o un SSID mal configurado también podrían ser el problema.

- **Enlace Router1-Módem**:
  - Si el Router1 no está obteniendo una conexión a Internet, el módem podría requerir configuraciones específicas (ej. clonación de dirección MAC). Consulta el manual o la configuración del módem para esto.

- **Doble NAT**:
  - Tu configuración tiene el módem (en `192.168.1.1`) y el Router1 (en `192.168.0.1`) actuando ambos como routers. Esto no debería bloquear la conectividad básica, pero configurar el módem en **modo bridge** (si es posible) podría simplificar las cosas.

- **Firewall**:
  - El firewall del Router1 podría estar bloqueando tu laptop. Deshabilita temporalmente cualquier regla de firewall personalizada para probar.

---

### Paso 5: Restablecer si es Necesario
Si nada funciona, restablece el Router1 y reconfigura:

- **Restablecimiento de Fábrica**:
  - Presiona y mantén presionado el botón de restablecimiento del Router1 durante 10 segundos, luego configura los ajustes WAN y DHCP nuevamente como los listaste.

- **Probar WAN Dinámica**:
  - En lugar de una IP WAN estática, configura la WAN del Router1 a **DHCP** para ver si puede obtener una IP del módem automáticamente. Si esto funciona, la IP estática (`192.168.1.101`) podría ser el problema.

---

### Consejos Finales
- **Rango DHCP del Módem**: Confirma que `192.168.1.101` esté fuera del rango DHCP del módem para evitar conflictos.
- **Firmware**: Revisa la interfaz web del Router1 para ver si hay una actualización de firmware.
- **Controladores de la Laptop**: Asegúrate de que los controladores del adaptador de red de tu laptop estén actualizados.

Sigue estos pasos y deberás identificar por qué tu laptop no se conecta. Si aún tienes problemas, ¡avísame lo que encuentres en cada paso y te ayudaré a reducirlo aún más!