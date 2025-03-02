---
audio: true
generated: false
lang: es
layout: post
title: Configurando OpenWRT como un Puente Inalámbrico
translated: true
---

Con la ayuda de Grok, sigo tratando de trabajar en lo siguiente.

---

Para abordar su consulta, "¿es correcto?" con respecto a los pasos para configurar OpenWRT como un puente inalámbrico, y para proporcionar las formas correctas de lograr esto, evaluaré los pasos que proporcionó y los refinaré según las mejores prácticas para OpenWRT. Su objetivo es configurar su router OpenWRT (por ejemplo, Xiaomi Mi Router 4C con OpenWRT 24.10.0) como un puente inalámbrico, conectándose inalámbricamente a una red Wi-Fi existente como cliente y compartiendo esa conexión a través de su propio punto de acceso Wi-Fi (AP) o puertos Ethernet, manteniendo todos los dispositivos en la misma subred que el router principal.

Sus pasos proporcionados son en su mayoría precisos, pero faltan un ajuste crítico para garantizar un puente adecuado y evitar conflictos de IP. A continuación, primero evaluaré su configuración y luego presentaré los pasos correctos y completos para lograr un puente inalámbrico en OpenWRT utilizando el método de puente simple (cliente + AP en el mismo puente), que se alinea con su intención. También mencionaré brevemente una alternativa utilizando `relayd` para casos en los que el método simple falle, aunque su configuración probablemente soporte el enfoque más sencillo.

---

### **Evaluación de sus pasos proporcionados**

Sus pasos tienen como objetivo:
1. Conectar el router OpenWRT como cliente a una red Wi-Fi existente.
2. Configurar un AP para transmitir una nueva red Wi-Fi.
3. Puentear las interfaces cliente y AP para compartir internet.

Aquí hay una revisión rápida:
- **Paso 1: Iniciar sesión en LuCI** - Correcto, acceder a la interfaz web es el punto de partida.
- **Paso 2: Configurar el cliente inalámbrico** - Unirse a la Wi-Fi objetivo y asignarla a la red `lan` es un buen comienzo, pero la configuración predeterminada de `lan` en OpenWRT (IP estática, generalmente 192.168.1.1) podría entrar en conflicto con el router principal si usa la misma IP. Esto necesita ajuste.
- **Paso 3: Configurar el AP inalámbrico** - Configurar un AP y asignarlo a `lan` es correcto para el puente, pero depende de que la interfaz `lan` esté configurada correctamente.
- **Paso 4: Puentear las redes** - Asignar ambas interfaces a `lan` teóricamente las puentea, pero sin deshabilitar el servidor DHCP o ajustar la configuración de IP, puede que no funcione sin problemas.
- **Paso 5: Probar la configuración** - Probar es esencial, pero el éxito depende de que los pasos anteriores estén completamente correctos.

**¿Qué falta o está mal?**
- Por defecto, la interfaz `lan` de OpenWRT tiene una IP estática (por ejemplo, 192.168.1.1) y ejecuta un servidor DHCP. Si el router principal también es 192.168.1.1, esto causa un conflicto de IP. Necesita configurar la interfaz `lan` en modo cliente DHCP para obtener una IP del router principal y deshabilitar el servidor DHCP local para que el router principal asigne IPs a todos los dispositivos.
- La asignación de la zona de firewall a `lan` está bien para la simplicidad, pero la configuración de IP es crítica.

Con esto en mente, sus pasos son "en su mayoría correctos" pero incompletos sin ajustar la configuración de la interfaz `lan`. A continuación se presentan los pasos corregidos.

---

### **Pasos correctos para configurar OpenWRT como un puente inalámbrico (Método de puente simple)**

Este método configura su router OpenWRT para conectarse a una red Wi-Fi existente como cliente y compartir esa conexión a través de su propio AP o puertos Ethernet, todo en la misma subred que el router principal (por ejemplo, 192.168.1.x). Aquí está cómo hacerlo a través de la interfaz web LuCI:

#### **Requisitos previos**
- OpenWRT está instalado (por ejemplo, versión 24.10.0 en Xiaomi Mi Router 4C).
- Tiene el SSID, la contraseña y el tipo de cifrado (por ejemplo, WPA2-PSK) de la red Wi-Fi principal.
- Acceso a LuCI en `http://192.168.1.1` (o la IP actual) y sus credenciales de administrador.

#### **Paso 1: Iniciar sesión en LuCI**
- Abra un navegador y vaya a `http://192.168.1.1`.
- Inicie sesión con su nombre de usuario de OpenWRT (predeterminado: `root`) y su contraseña (establecida durante la instalación).

#### **Paso 2: Configurar el cliente inalámbrico**
- **Navegar a la configuración inalámbrica:**
  - Vaya a **Red > Inalámbrico**.
- **Escanear redes:**
  - Localice su radio (por ejemplo, `radio0` para 2.4 GHz en el Mi Router 4C).
  - Haga clic en **Escanear** para listar las redes Wi-Fi disponibles.
- **Unirse a la red Wi-Fi principal:**
  - Encuentre el SSID de la Wi-Fi de su router principal.
  - Haga clic en **Unirse a la red**.
- **Configurar la configuración del cliente:**
  - **Clave Wi-Fi:** Ingrese la contraseña de la Wi-Fi principal.
  - **Red:** Seleccione o establezca en `lan` (esto agrega la interfaz cliente al puente `br-lan`).
  - **Zona de firewall:** Asignar a `lan` (esto simplifica las reglas de tráfico para el puente).
  - **Nombre de la interfaz:** LuCI puede sugerir `wwan`; puede dejarlo o renombrarlo a `cliente` para mayor claridad, pero asegúrese de que esté vinculado a `lan`.
- **Guardar y aplicar:**
  - Haga clic en **Guardar y aplicar** para conectarse a la Wi-Fi principal.

#### **Paso 3: Ajustar la interfaz LAN a cliente DHCP**
- **Ir a Interfaces:**
  - Navegue a **Red > Interfaces**.
- **Editar la interfaz LAN:**
  - Haga clic en **Editar** junto a la interfaz `lan`.
- **Establecer el protocolo en cliente DHCP:**
  - En el menú desplegable **Protocolo**, seleccione **cliente DHCP**.
  - Esto permite que el puente `br-lan` (que ahora incluye el cliente inalámbrico) obtenga una dirección IP del servidor DHCP del router principal (por ejemplo, 192.168.1.x).
- **Deshabilitar el servidor DHCP:**
  - Dado que `lan` ahora es un cliente DHCP, el servidor DHCP local se deshabilita automáticamente. Verifique esto bajo **Configuración avanzada** o **DHCP y DNS**—asegúrese de que "Ignorar interfaz" esté marcada si aparece la opción.
- **Guardar y aplicar:**
  - Haga clic en **Guardar y aplicar**. El router ahora solicitará una IP del router principal.

#### **Paso 4: Configurar el punto de acceso inalámbrico**
- **Agregar una nueva red inalámbrica:**
  - Vuelva a **Red > Inalámbrico**.
  - Haga clic en **Agregar** bajo el mismo radio (por ejemplo, `radio0`) para crear una nueva interfaz inalámbrica.
- **Configurar el AP:**
  - **ESSID:** Elija un nombre para su Wi-Fi (por ejemplo, `OpenWRT_AP`).
  - **Modo:** Establecer en **Punto de acceso (AP)**.
  - **Red:** Asignar a `lan` (esto lo puentea con la interfaz cliente y los puertos Ethernet).
- **Configurar la seguridad:**
  - Vaya a la pestaña **Seguridad inalámbrica**.
  - **Cifrado:** Seleccione **WPA2-PSK** (recomendado).
  - **Clave:** Establezca una contraseña fuerte para su AP.
- **Guardar y aplicar:**
  - Haga clic en **Guardar y aplicar**. Su router ahora transmitirá su propia Wi-Fi.

#### **Paso 5: Verificar el puente**
- **Verificar interfaces:**
  - Vaya a **Red > Interfaces**.
  - Asegúrese de que la interfaz `lan` liste tanto el cliente inalámbrico (por ejemplo, `wlan0`) como el AP (por ejemplo, `wlan0-1`) bajo el puente `br-lan`.
- **Verificar la asignación de IP:**
  - Vaya a **Estado > Descripción general**.
  - Tome nota de la dirección IP asignada a la interfaz `lan` por el router principal (por ejemplo, `192.168.1.100`).

#### **Paso 6: Probar la configuración**
- **Probar Wi-Fi:**
  - Conecte un dispositivo a la Wi-Fi `OpenWRT_AP`.
  - Verifique que reciba una IP del router principal (por ejemplo, `192.168.1.x`) y tenga acceso a internet.
- **Probar Ethernet (si corresponde):**
  - Conecte un dispositivo a uno de los puertos LAN del router.
  - Confirme que obtenga una IP del router principal y se conecte a internet.
- **Acceder a LuCI:**
  - Use la nueva dirección IP (por ejemplo, `http://192.168.1.100`) para acceder a la interfaz de OpenWRT.

---

### **Por qué esto funciona**
- Asignar tanto la interfaz cliente como la AP a la red `lan` las agrega al puente `br-lan`, permitiendo que el tráfico de capa 2 fluya entre ellas y el router principal.
- Configurar `lan` como cliente DHCP asegura que el router OpenWRT obtenga una IP única del router principal, evitando conflictos (por ejemplo, con `192.168.1.1`), y deshabilita el servidor DHCP local para que el router principal administre todas las asignaciones de IP.
- Los dispositivos conectados al AP o puertos Ethernet aparecen en la misma subred que la red principal (por ejemplo, `192.168.1.x`), cumpliendo con el requisito del puente inalámbrico.

---

### **Método alternativo: Usando relayd (Pseudo-bridge)**
Si el método de puente simple falla (por ejemplo, debido a limitaciones del controlador inalámbrico), puede usar el paquete `relayd` para un pseudo-bridge. Esto crea una configuración enrutada donde los clientes del router OpenWRT están en una subred diferente, pero es más confiable en algunos hardware. Aquí hay un breve resumen:

1. **Instalar relayd:**
   - Vaya a **Sistema > Software**, busque `relayd` e instálelo.
2. **Configurar cliente inalámbrico:**
   - Únase a la Wi-Fi principal, pero asigne a una nueva interfaz (por ejemplo, `wwan`) establecida en cliente DHCP.
3. **Configurar LAN:**
   - Establezca `lan` en una IP estática (por ejemplo, `192.168.2.1`) con su propio servidor DHCP.
4. **Configurar relayd:**
   - Configure `relayd` a través de SSH o LuCI (en **Red > Hostnames**) para relayar entre `wwan` y `lan`.
5. **Configurar AP:**
   - Establezca el AP en la red `lan`.
6. **Probar:**
   - Los dispositivos en `OpenWRT_AP` estarán en `192.168.2.x`, con internet relayado desde el router principal.

**Nota:** Esto no es un puente real (subredes diferentes), así que úselo solo si el método simple no funciona. Para su Xiaomi Mi Router 4C con OpenWRT 24.10.0, el puente simple debería ser suficiente.

---

### **Conclusión**
Sus pasos originales son **en su mayoría correctos** pero incompletos sin configurar la interfaz `lan` en modo cliente DHCP para evitar conflictos de IP y asegurar un puente adecuado. Los pasos corregidos anteriormente proporcionan una manera confiable de configurar OpenWRT como un puente inalámbrico. Si los sigue, su router se conectará a la Wi-Fi principal y compartirá esa conexión sin problemas a través de su AP o puertos Ethernet, todo en la misma subred. Pruebe la configuración, y si surgen problemas (raro con OpenWRT moderno), considere la alternativa `relayd`.