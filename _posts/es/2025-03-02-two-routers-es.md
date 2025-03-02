---
audio: false
lang: es
layout: post
title: Usando Dos Routers
translated: true
---

Para configurar sus dos routers TP-Link AX3000 (TL-XDR 3050) con su módem en la configuración **Módem → Cable → Router1 → Inalámbrico → Router2**, siga esta guía paso a paso. Su módem ya tiene funcionalidad WiFi y una dirección IP de `192.168.1.1`. Configuraremos Router1 como el router principal conectado al módem mediante un cable y Router2 para extender la red inalámbricamente.

Aquí está cómo lograrlo:

---

### **Paso 1: Entender la Configuración**
- **Módem**: Proporciona acceso a Internet y tiene su propio WiFi (IP: `192.168.1.1`).
- **Router1**: Se conectará al módem con un cable y actuará como el router principal para su red.
- **Router2**: Se conectará inalámbricamente a Router1 para extender la cobertura de la red.

Ha mencionado varios modos (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Usaremos **DHCP** para Router1 para obtener una conexión a Internet desde el módem y **Wireless AP Bridge** (o un modo similar como WDS/Repeater) para Router2 para conectarse inalámbricamente a Router1.

---

### **Paso 2: Configurar Router1**
1. **Conectar Router1 al Módem**:
   - Tome un cable Ethernet y conéctelo a un puerto **LAN** en su módem.
   - Conecte el otro extremo al puerto **WAN (Internet)** en Router1.

2. **Acceder a la Interfaz Web de Router1**:
   - Conecte una computadora o smartphone a la red WiFi predeterminada de Router1 (verifique la etiqueta en el router para el SSID y la contraseña predeterminados) o use un cable Ethernet.
   - Abra un navegador web y escriba `http://tplinkwifi.net` o `192.168.0.1` (la IP predeterminada para routers TP-Link).
   - Inicie sesión con las credenciales predeterminadas (generalmente `admin` para ambos nombre de usuario y contraseña) a menos que las haya cambiado.

3. **Configurar Router1**:
   - **Conexión a Internet**:
     - Vaya a **Configuración Rápida** o a la sección de **Configuración de Internet**.
     - Seleccione el modo **DHCP**. Esto permite que Router1 obtenga automáticamente una dirección IP del módem (probablemente en el rango `192.168.1.x`).
   - **Configuración de WiFi**:
     - Establezca un **SSID** único (nombre de la red) y una contraseña fuerte para el WiFi de Router1.
     - Guarde estos detalles, ya que Router2 los necesitará para conectarse inalámbricamente.
   - **Configuración de LAN**:
     - Asegúrese de que la IP de LAN de Router1 sea diferente de la IP del módem. Por defecto, probablemente sea `192.168.0.1`, lo cual está bien ya que el módem es `192.168.1.1`.
     - Confirme que **DHCP** esté habilitado en Router1. Esto permite que Router1 asigne direcciones IP (por ejemplo, `192.168.0.x`) a los dispositivos conectados a él, incluyendo Router2.
   - Guarde la configuración y reinicie Router1 si se le solicita.

---

### **Paso 3: Configurar Router2 como un Puente Inalámbrico**
1. **Acceder a la Interfaz Web de Router2**:
   - Conecte una computadora o smartphone a la red WiFi predeterminada de Router2 o mediante Ethernet.
   - Abra un navegador web y escriba `http://tplinkwifi.net` o `192.168.0.1`.
   - Inicie sesión con las credenciales predeterminadas (o las suyas personalizadas).

2. **Configurar Router2 en Modo Puente Inalámbrico**:
   - Busque un modo como **Wireless AP Bridge**, **WDS** o **Repeater** en la configuración (probablemente bajo **Modo de Operación** o **Configuración Inalámbrica**).
   - Seleccione **Wireless AP Bridge** (o WDS/Repeater si es lo que está disponible).
   - **Conectar a la WiFi de Router1**:
     - Escanee las redes disponibles y seleccione el SSID de Router1.
     - Ingrese la contraseña de WiFi de Router1.
     - Asegúrese de que Router2 use el mismo canal inalámbrico que Router1 para compatibilidad (por ejemplo, si Router1 está en el Canal 6, configure Router2 en el Canal 6).
   - **Configuración de IP de LAN**:
     - Cambie la IP de LAN de Router2 para evitar conflictos con Router1. Por ejemplo, configúrela en `192.168.0.2` (ya que Router1 probablemente sea `192.168.0.1`).
     - **Deshabilite DHCP** en Router2. Router1 manejará la asignación de IPs para todos los dispositivos.
   - Guarde la configuración y reinicie Router2. Ahora debería conectarse inalámbricamente a Router1.

---

### **Paso 4: Probar la Configuración**
1. **Verificar la Conexión de Router2**:
   - Después de reiniciar, verifique la interfaz de Router2 para confirmar que está conectado a la WiFi de Router1.
2. **Conectar un Dispositivo a Router2**:
   - Use un smartphone, laptop u otro dispositivo para conectarse a la WiFi de Router2 (puede usar el mismo SSID que Router1, dependiendo del modo).
   - Verifique que el dispositivo obtenga una dirección IP de Router1 (por ejemplo, `192.168.0.x`).
   - Pruebe el acceso a Internet navegando a un sitio web.

---

### **Resumen de la Configuración Final**
- **Módem**: IP `192.168.1.1`, proporciona internet y WiFi.
- **Router1**:
  - WAN: Conectado al módem mediante cable, configurado en **DHCP** (obtiene IP del módem, por ejemplo, `192.168.1.x`).
  - LAN: IP `192.168.0.1`, **DHCP habilitado** para asignar IPs a dispositivos.
  - WiFi: SSID y contraseña personalizados.
- **Router2**:
  - Modo: **Wireless AP Bridge** (o WDS/Repeater), conectado inalámbricamente a la WiFi de Router1.
  - IP de LAN: `192.168.0.2`, **DHCP deshabilitado**.

---

### **Consejos de Solución de Problemas**
- **Router2 No Se Conecta Inalámbricamente**:
  - Verifique nuevamente el SSID, la contraseña y la configuración del canal de Router1 en la configuración de Router2.
  - Si **Wireless AP Bridge** no está disponible, intente el modo **WDS** o **Repeater**. Consulte el manual de TP-Link AX3000 para los modos compatibles.
- **Sin Internet en Router2**:
  - Asegúrese de que el DHCP de Router1 esté funcionando y el DHCP de Router2 esté desactivado.
  - Verifique que Router2 esté conectado correctamente a Router1.
- **Preocupaciones de NAT Doble**:
  - Dado que su módem tiene WiFi y Router1 actúa como router, podría tener NAT doble (módem y Router1 ambos asignando IPs). Esto generalmente está bien para uso básico, pero podría afectar algunas aplicaciones (por ejemplo, juegos). Si es necesario, configure el módem en **modo puente** (consulte el manual de su módem), aunque esto podría deshabilitar su WiFi.

Con esta configuración, Router2 extenderá su red inalámbricamente desde Router1, y los dispositivos conectados a cualquiera de los routers deberían acceder a Internet a través del módem. ¡Hágame saber si necesita más asistencia!

---

Si decide usar una dirección IP fija (estática) para el primer router (Router1) en lugar de confiar en DHCP, deberá configurar manualmente sus configuraciones WAN para comunicarse con su módem. Aquí está lo que debe configurar para la dirección IP, DNS, máscara de subred y puerta de enlace:

---

### **Suposiciones**
- Su módem tiene una dirección IP de `192.168.1.1` y usa la subred `192.168.1.0/24` (máscara de subred `255.255.255.0`).
- El módem tiene un rango DHCP (por ejemplo, `192.168.1.2` a `192.168.1.100`) que asigna direcciones IP a dispositivos conectados.

Si su módem usa una IP o subred diferente, ajuste los valores en consecuencia.

---

### **Configuración WAN para Router1**
Estas configuraciones determinan cómo Router1 se conecta al módem:

1. **Dirección IP**
   - Elija una IP estática dentro de la subred del módem (`192.168.1.0/24`) pero **fuera del rango DHCP del módem** para evitar conflictos.
   - Ejemplo: Si el rango DHCP del módem es `192.168.1.2` a `192.168.1.100`, puede usar **`192.168.1.101`**.
   - Esto asegura que Router1 tenga una dirección única y fija en la red del módem.

2. **Máscara de Subred**
   - Establezca esto para que coincida con la máscara de subred del módem, que generalmente es **`255.255.255.0`**.
   - Esto define el rango de red como `192.168.1.0` a `192.168.1.255`.

3. **Puerta de Enlace Predeterminada**
   - Establezca esto en la dirección IP del módem, que es **`192.168.1.1`**.
   - La puerta de enlace es el dispositivo (su módem) que Router1 usa para acceder a Internet.

4. **Servidores DNS**
   - Tiene dos opciones:
     - Use la IP del módem: **`192.168.1.1`**. Esto permite que el módem maneje las solicitudes DNS.
     - Use servidores DNS públicos: **`8.8.8.8`** (Google) y **`8.8.4.4`** (Google secundario). Estos son confiables y a menudo más rápidos.
   - Recomendación: Comience con `192.168.1.1`. Si experimenta problemas de DNS, cambie a `8.8.8.8` y `8.8.4.4`.

---

### **Configuración de Ejemplo**
Aquí es cómo podrían verse las configuraciones WAN de Router1:

- **Dirección IP**: `192.168.1.101`
- **Máscara de Subred**: `255.255.255.0`
- **Puerta de Enlace Predeterminada**: `192.168.1.1`
- **Servidor DNS**: `192.168.1.1` (o `8.8.8.8` y `8.8.4.4`)

---

### **Notas Adicionales**
- **Verificar Configuración del Módem**: Inicie sesión en su módem (generalmente en `192.168.1.1`) para confirmar su IP, máscara de subred y rango DHCP. Ajuste la IP estática de Router1 si es necesario.
- **Configuración de LAN para Router1**: Para evitar conflictos, configure la red LAN de Router1 en una subred diferente, como `192.168.0.1` con una máscara de subred de `255.255.255.0`. Habilite DHCP en Router1 para asignar IPs (por ejemplo, `192.168.0.2` a `192.168.0.254`) a dispositivos conectados a él.
- **Pruebas**: Después de aplicar estas configuraciones, asegúrese de que Router1 pueda acceder a Internet. Si no es así, verifique la IP (sin conflictos), la puerta de enlace y los valores DNS.

Esta configuración da a Router1 una IP fija en la red del módem, asegurando una conectividad consistente. ¡Hágame saber si necesita ayuda con routers adicionales o detalles específicos del módem!