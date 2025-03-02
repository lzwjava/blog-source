---
audio: false
lang: es
layout: post
title: Usando Dos Routers
translated: true
---

Para configurar tus dos routers TP-Link AX3000 (TL-XDR 3050) con tu módem en la configuración **Módem → Cable → Router1 → Inalámbrico → Router2**, sigue esta guía paso a paso. Tu módem ya tiene funcionalidad WiFi y una dirección IP de `192.168.1.1`. Configuraremos Router1 como el router principal conectado al módem mediante un cable y Router2 para extender la red inalámbricamente.

Aquí tienes cómo lograrlo:

---

### **Paso 1: Entender la Configuración**
- **Módem**: Proporciona acceso a internet y tiene su propio WiFi (IP: `192.168.1.1`).
- **Router1**: Se conectará al módem con un cable y actuará como el router principal para tu red.
- **Router2**: Se conectará inalámbricamente a Router1 para extender la cobertura de la red.

Has mencionado varios modos (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Usaremos **DHCP** para Router1 para obtener una conexión a internet desde el módem y **Wireless AP Bridge** (o un modo similar como WDS/Repeater) para Router2 para conectarse inalámbricamente a Router1.

---

### **Paso 2: Configurar Router1**
1. **Conectar Router1 al Módem**:
   - Toma un cable Ethernet y conecta un extremo a un **puerto LAN** en tu módem.
   - Conecta el otro extremo al **puerto WAN (Internet)** en Router1.

2. **Acceder a la Interfaz Web de Router1**:
   - Conecta una computadora o smartphone a la red WiFi predeterminada de Router1 (verifica la etiqueta en el router para el SSID y la contraseña predeterminados) o usa un cable Ethernet.
   - Abre un navegador web y escribe `http://tplinkwifi.net` o `192.168.0.1` (la IP predeterminada para routers TP-Link).
   - Inicia sesión con las credenciales predeterminadas (generalmente `admin` para ambos nombre de usuario y contraseña) a menos que las hayas cambiado.

3. **Configurar Router1**:
   - **Conexión a Internet**:
     - Ve a **Quick Setup** o la sección de configuración de **Internet**.
     - Selecciona el modo **DHCP**. Esto permite que Router1 obtenga automáticamente una dirección IP del módem (probablemente en el rango `192.168.1.x`).
   - **Configuración de WiFi**:
     - Establece un **SSID** único (nombre de la red) y una **contraseña** fuerte para el WiFi de Router1.
     - Guarda estos detalles, ya que Router2 los necesitará para conectarse inalámbricamente.
   - **Configuración de LAN**:
     - Asegúrate de que la IP LAN de Router1 sea diferente a la IP del módem. Por defecto, probablemente sea `192.168.0.1`, lo cual está bien ya que el módem es `192.168.1.1`.
     - Confirma que **DHCP** esté habilitado en Router1. Esto permite que Router1 asigne direcciones IP (por ejemplo, `192.168.0.x`) a los dispositivos conectados a él, incluyendo Router2.
   - Guarda la configuración y reinicia Router1 si se te indica.

---

### **Paso 3: Configurar Router2 como un Puente Inalámbrico**
1. **Acceder a la Interfaz Web de Router2**:
   - Conecta una computadora o smartphone a la red WiFi predeterminada de Router2 o mediante Ethernet.
   - Abre un navegador web y escribe `http://tplinkwifi.net` o `192.168.0.1`.
   - Inicia sesión con las credenciales predeterminadas (o las tuyas personalizadas).

2. **Configurar Router2 en Modo Puente Inalámbrico**:
   - Busca un modo como **Wireless AP Bridge**, **WDS** o **Repeater** en la configuración (probablemente bajo **Operation Mode** o **Wireless** settings).
   - Selecciona **Wireless AP Bridge** (o WDS/Repeater si es lo que está disponible).
   - **Conectar al WiFi de Router1**:
     - Escanea las redes disponibles y selecciona el SSID de Router1.
     - Introduce la contraseña del WiFi de Router1.
     - Asegúrate de que Router2 use el mismo canal inalámbrico que Router1 para compatibilidad (por ejemplo, si Router1 está en el Canal 6, configura Router2 en el Canal 6).
   - **Configuración de IP LAN**:
     - Cambia la IP LAN de Router2 para evitar conflictos con Router1. Por ejemplo, configúrala a `192.168.0.2` (ya que Router1 probablemente sea `192.168.0.1`).
     - **Deshabilita DHCP** en Router2. Router1 manejará la asignación de IPs para todos los dispositivos.
   - Guarda la configuración y reinicia Router2. Ahora debería conectarse inalámbricamente a Router1.

---

### **Paso 4: Probar la Configuración**
1. **Verificar la Conexión de Router2**:
   - Después de reiniciar, verifica la interfaz de Router2 para confirmar que está conectado al WiFi de Router1.
2. **Conectar un Dispositivo a Router2**:
   - Usa un smartphone, laptop u otro dispositivo para conectarte al WiFi de Router2 (puede usar el mismo SSID que Router1, dependiendo del modo).
   - Verifica que el dispositivo obtenga una dirección IP de Router1 (por ejemplo, `192.168.0.x`).
   - Prueba el acceso a internet navegando a un sitio web.

---

### **Resumen de la Configuración Final**
- **Módem**: IP `192.168.1.1`, proporciona internet y WiFi.
- **Router1**:
  - WAN: Conectado al módem mediante cable, configurado en **DHCP** (obtiene IP del módem, por ejemplo, `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP habilitado** para asignar IPs a dispositivos.
  - WiFi: SSID y contraseña personalizados.
- **Router2**:
  - Modo: **Wireless AP Bridge** (o WDS/Repeater), conectado inalámbricamente al WiFi de Router1.
  - IP LAN: `192.168.0.2`, **DHCP deshabilitado**.

---

### **Consejos de Solución de Problemas**
- **Router2 No Se Conecta Inalámbricamente**:
  - Verifica nuevamente el SSID, la contraseña y la configuración del canal de Router1 en la configuración de Router2.
  - Si **Wireless AP Bridge** no está disponible, intenta **WDS** o **Repeater** mode. Consulta el manual de TP-Link AX3000 para los modos soportados.
- **Sin Internet en Router2**:
  - Asegúrate de que el DHCP de Router1 esté funcionando y el DHCP de Router2 esté desactivado.
  - Verifica que Router2 esté conectado correctamente a Router1.
- **Preocupaciones sobre NAT Doble**:
  - Dado que tu módem tiene WiFi y Router1 actúa como router, podrías tener NAT doble (módem y Router1 ambos asignando IPs). Esto generalmente está bien para uso básico, pero podría afectar algunas aplicaciones (por ejemplo, juegos). Si es necesario, configura el módem en **modo puente** (consulta el manual de tu módem), aunque esto podría deshabilitar su WiFi.

Con esta configuración, Router2 extenderá tu red inalámbricamente desde Router1, y los dispositivos conectados a cualquiera de los routers deberían acceder a internet a través del módem. ¡Hazme saber si necesitas más asistencia!