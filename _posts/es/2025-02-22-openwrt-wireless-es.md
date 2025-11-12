---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración de OpenWRT como puente inalámbrico
translated: true
type: note
---

Con la ayuda de Grok, todavía estoy intentando trabajar en lo siguiente.

---

Para abordar tu consulta, "¿es correcto?" sobre los pasos para configurar OpenWRT como un puente inalámbrico, y para proporcionar las formas correctas de lograrlo, evaluaré los pasos que proporcionaste y los refinaré basándome en las mejores prácticas para OpenWRT. Tu objetivo es configurar tu router OpenWRT (por ejemplo, un Xiaomi Mi Router 4C con OpenWRT 24.10.0) como un puente inalámbrico—conectándose de forma inalámbrica a una red Wi-Fi existente como cliente y compartiendo esa conexión a través de su propio punto de acceso (AP) Wi-Fi o puertos Ethernet, manteniendo todos los dispositivos en la misma subred que el router principal.

Los pasos que proporcionaste son mayormente precisos, pero omiten un ajuste crítico para garantizar un puente correcto y evitar conflictos de IP. A continuación, primero evaluaré tu configuración y luego presentaré los pasos correctos y completos para lograr un puente inalámbrico en OpenWRT usando el método de puente simple (cliente + AP en el mismo puente), que se alinea con tu intención. También mencionaré brevemente una alternativa usando `relayd` para casos donde el método simple falle, aunque es probable que tu configuración soporte el enfoque más simple.

---

### **Evaluación de los Pasos que Proporcionaste**

Tus pasos tienen como objetivo:
1. Conectar el router OpenWRT como cliente a una red Wi-Fi existente.
2. Configurar un AP para transmitir una nueva red Wi-Fi.
3. Puentear las interfaces cliente y AP para compartir la conexión a internet.

Aquí hay una revisión rápida:
- **Paso 1: Iniciar Sesión en LuCI** - Correcto, acceder a la interfaz web es el punto de partida.
- **Paso 2: Configurar el Cliente Inalámbrico** - Unirse a la red Wi-Fi objetivo y asignarla a la red `lan` es un buen comienzo, pero la configuración predeterminada de `lan` en OpenWRT (IP estática, típicamente 192.168.1.1) podría entrar en conflicto con el router principal si usa la misma IP. Esto necesita un ajuste.
- **Paso 3: Configurar el Punto de Acceso Inalámbrico** - Configurar un AP y asignarlo a `lan` es correcto para el puente, pero depende de que la interfaz `lan` esté configurada correctamente.
- **Paso 4: Puentear las Redes** - Asignar ambas interfaces a `lan` teóricamente las puentea, pero sin deshabilitar el servidor DHCP o ajustar la configuración de IP, puede que no funcione sin problemas.
- **Paso 5: Probar la Configuración** - Probar es esencial, pero el éxito depende de que los pasos anteriores sean completamente correctos.

**¿Qué Faltó o Estuvo Mal?**
- Por defecto, la interfaz `lan` de OpenWRT tiene una IP estática (ej. 192.168.1.1) y ejecuta un servidor DHCP. Si el router principal también es 192.168.1.1, esto causa un conflicto de IP. Necesitas configurar la interfaz `lan` en modo cliente DHCP para obtener una IP del router principal y deshabilitar el servidor DHCP local para permitir que el router principal asigne IPs a todos los dispositivos.
- La asignación de la zona del firewall a `lan` está bien para simplificar, pero la configuración de IP es crítica.

Con esto en mente, tus pasos son "mayormente correctos" pero incompletos sin ajustar la configuración de la interfaz `lan`. A continuación se presentan los pasos corregidos.

---

### **Pasos Correctos para Configurar OpenWRT como un Puente Inalámbrico (Método de Puente Simple)**

Este método configura tu router OpenWRT para conectarse a una red Wi-Fi existente como cliente y compartir esa conexión a través de su propio AP o puertos Ethernet, todo en la misma subred que el router principal (ej. 192.168.1.x). Así es cómo hacerlo a través de la interfaz web de LuCI:

#### **Prerrequisitos**
- OpenWRT está instalado (ej. versión 24.10.0 en Xiaomi Mi Router 4C).
- Tienes el SSID, la contraseña y el tipo de cifrado (ej. WPA2-PSK) de la red Wi-Fi principal.
- Acceso a LuCI en `http://192.168.1.1` (o la IP actual) y tus credenciales de administrador.

#### **Paso 1: Iniciar Sesión en LuCI**
- Abre un navegador y ve a `http://192.168.1.1`.
- Inicia sesión con tu nombre de usuario de OpenWRT (por defecto: `root`) y contraseña (establecida durante la instalación).

#### **Paso 2: Configurar el Cliente Inalámbrico**
- **Navegar a la Configuración Inalámbrica:**
  - Ve a **Network > Wireless**.
- **Escanear Redes:**
  - Localiza tu radio (ej. `radio0` para 2.4 GHz en el Mi Router 4C).
  - Haz clic en **Scan** para listar las redes Wi-Fi disponibles.
- **Unirse a la Red Wi-Fi Principal:**
  - Encuentra el SSID de la red Wi-Fi de tu router principal.
  - Haz clic en **Join Network**.
- **Configurar los Ajustes del Cliente:**
  - **Wi-Fi Key:** Introduce la contraseña de la red Wi-Fi principal.
  - **Network:** Selecciona o establece `lan` (esto añade la interfaz cliente al puente `br-lan`).
  - **Firewall Zone:** Asígnala a `lan` (esto simplifica las reglas de tráfico para el puente).
  - **Interface Name:** LuCI puede sugerir `wwan`; puedes dejarlo o renombrarlo a `client` para mayor claridad, pero asegúrate de que esté vinculado a `lan`.
- **Guardar y Aplicar:**
  - Haz clic en **Save & Apply** para conectarte a la red Wi-Fi principal.

#### **Paso 3: Ajustar la Interfaz LAN a Cliente DHCP**
- **Ir a Interfaces:**
  - Navega a **Network > Interfaces**.
- **Editar la Interfaz LAN:**
  - Haz clic en **Edit** al lado de la interfaz `lan`.
- **Establecer el Protocolo a Cliente DHCP:**
  - En el menú desplegable **Protocol**, selecciona **DHCP client**.
  - Esto permite que el puente `br-lan` (que ahora incluye el cliente inalámbrico) obtenga una dirección IP del servidor DHCP del router principal (ej. 192.168.1.x).
- **Deshabilitar el Servidor DHCP:**
  - Dado que `lan` es ahora un cliente DHCP, el servidor DHCP local se deshabilita automáticamente. Verifica esto bajo **Advanced Settings** o **DHCP and DNS**—asegúrate de que "Ignore interface" esté marcada si la opción aparece.
- **Guardar y Aplicar:**
  - Haz clic en **Save & Apply**. El router ahora solicitará una IP al router principal.

#### **Paso 4: Configurar el Punto de Acceso Inalámbrico**
- **Añadir una Nueva Red Inalámbrica:**
  - Regresa a **Network > Wireless**.
  - Haz clic en **Add** bajo la misma radio (ej. `radio0`) para crear una nueva interfaz inalámbrica.
- **Configurar el AP:**
  - **ESSID:** Elige un nombre para tu Wi-Fi (ej. `OpenWRT_AP`).
  - **Mode:** Establece en **Access Point (AP)**.
  - **Network:** Asígnalo a `lan` (esto lo puentea con la interfaz cliente y los puertos Ethernet).
- **Configurar la Seguridad:**
  - Ve a la pestaña **Wireless Security**.
  - **Encryption:** Selecciona **WPA2-PSK** (recomendado).
  - **Key:** Establece una contraseña fuerte para tu AP.
- **Guardar y Aplicar:**
  - Haz clic en **Save & Apply**. Tu router ahora transmitirá su propia red Wi-Fi.

#### **Paso 5: Verificar el Puente**
- **Comprobar Interfaces:**
  - Ve a **Network > Interfaces**.
  - Asegúrate de que la interfaz `lan` liste tanto el cliente inalámbrico (ej. `wlan0`) como el AP (ej. `wlan0-1`) bajo el puente `br-lan`.
- **Comprobar la Asignación de IP:**
  - Ve a **Status > Overview**.
  - Anota la dirección IP asignada a la interfaz `lan` por el router principal (ej. `192.168.1.100`).

#### **Paso 6: Probar la Configuración**
- **Probar el Wi-Fi:**
  - Conecta un dispositivo a la red Wi-Fi `OpenWRT_AP`.
  - Verifica que reciba una IP del router principal (ej. `192.168.1.x`) y que tenga acceso a internet.
- **Probar Ethernet (si es aplicable):**
  - Conecta un dispositivo a uno de los puertos LAN del router.
  - Confirma que obtenga una IP del router principal y se conecte a internet.
- **Acceder a LuCI:**
  - Usa la nueva dirección IP (ej. `http://192.168.1.100`) para acceder a la interfaz de OpenWRT.

---

### **Por Qué Esto Funciona**
- Asignar tanto las interfaces cliente como AP a la red `lan` las añade al puente `br-lan`, permitiendo que el tráfico de capa 2 fluya entre ellas y el router principal.
- Configurar `lan` como cliente DHCP asegura que el router OpenWRT obtenga una IP única del router principal, evitando conflictos (ej. con `192.168.1.1`), y deshabilita el servidor DHCP local para que el router principal gestione todas las asignaciones de IP.
- Los dispositivos conectados al AP o a los puertos Ethernet aparecen en la misma subred que la red principal (ej. `192.168.1.x`), cumpliendo con el requisito del puente inalámbrico.

---

### **Método Alternativo: Usando relayd (Pseudo-Puente)**
Si el método de puente simple falla (ej. debido a limitaciones del controlador inalámbrico), puedes usar el paquete `relayd` para un pseudo-puente. Esto crea una configuración enrutada donde los clientes del router OpenWRT están en una subred diferente, pero es más confiable en algún hardware. Aquí hay un resumen breve:

1. **Instalar relayd:**
   - Ve a **System > Software**, busca `relayd`, e instálalo.
2. **Configurar el Cliente Inalámbrico:**
   - Únete a la red Wi-Fi principal, pero asígnala a una nueva interfaz (ej. `wwan`) configurada como cliente DHCP.
3. **Configurar LAN:**
   - Establece `lan` a una IP estática (ej. `192.168.2.1`) con su propio servidor DHCP.
4. **Configurar relayd:**
   - Configura `relayd` vía SSH o LuCI (bajo **Network > Hostnames**) para hacer de relay entre `wwan` y `lan`.
5. **Configurar AP:**
   - Configura el AP en la red `lan`.
6. **Probar:**
   - Los dispositivos en `OpenWRT_AP` estarán en `192.168.2.x`, con internet relayada desde el router principal.

**Nota:** Esto no es un puente verdadero (subredes diferentes), así que úsalo solo si el método simple no funciona. Para tu Xiaomi Mi Router 4C con OpenWRT 24.10.0, el puente simple debería ser suficiente.

---

### **Conclusión**
Tus pasos originales son **mayormente correctos** pero incompletos sin establecer la interfaz `lan` en modo cliente DHCP para evitar conflictos de IP y garantizar un puente correcto. Los pasos corregidos anteriores proporcionan una forma confiable de configurar OpenWRT como un puente inalámbrico. Si los sigues, tu router se conectará a la red Wi-Fi principal y compartirá esa conexión sin problemas a través de su AP o puertos Ethernet, todo en la misma subred. Prueba la configuración, y si surgen problemas (poco común con OpenWRT moderno), considera la alternativa de `relayd`.