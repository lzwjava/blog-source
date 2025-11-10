---
audio: false
generated: true
lang: es
layout: post
title: Gestión del Enrutamiento de Tráfico con Doble SIM en iOS Considerando el Gran
  Cortafuegos
translated: true
type: note
---

iOS proporciona APIs que te permiten gestionar y separar el tráfico de red para diferentes planes de datos celulares cuando se utiliza la funcionalidad Dual SIM, pero existen limitaciones, y el control directo sobre el enrutamiento de tráfico específico a SIMs específicas basado en las restricciones del Gran Cortafuegos de China (GFW) no es compatible de forma nativa a un nivel granular. Sin embargo, con una combinación de APIs de iOS, configuración manual y potencialmente herramientas de terceros, puedes lograr cierto nivel de separación para manejar el tráfico de manera diferente para una SIM de Macao y una SIM de China Telecom. A continuación, describiré las APIs relevantes, configuraciones y consideraciones, incluyendo cómo abordar los desafíos relacionados con el GFW.

### APIs y Características Clave de iOS para Dual SIM y Gestión de Tráfico

1. **Framework CoreTelephony**:
   - **Propósito**: Proporciona acceso a información relacionada con la red celular y configuración para dispositivos Dual SIM.
   - **Clases Clave**:
     - `CTCellularPlanProvisioning`: Te permite añadir o gestionar planes celulares (por ejemplo, eSIM o SIM física).
     - `CTTelephonyNetworkInfo`: Proporciona información sobre los planes celulares disponibles y sus propiedades, como el nombre de la operadora, el código de país móvil (MCC) y el código de red móvil (MNC).
     - `CTCellularData`: Monitorea el uso de datos celulares y el estado de la red (por ejemplo, si los datos celulares están habilitados).
   - **Limitaciones**: CoreTelephony te permite consultar y gestionar planes celulares pero no proporciona control directo sobre el enrutamiento de tráfico específico de una app a una SIM particular. Puedes detectar qué SIM está activa para datos pero no puedes asignar programáticamente tráfico específico (por ejemplo, para una app o destino específico) a una SIM a nivel de API.

2. **Framework NetworkExtension**:
   - **Propósito**: Permite configuraciones de red avanzadas, como crear VPNs personalizadas o gestionar reglas de tráfico de red.
   - **Características Clave**:
     - **NEVPNManager**: Te permite configurar y gestionar conexiones VPN, que pueden usarse para enrutar tráfico a través de un servidor específico para evitar las restricciones del GFW.
     - **NEPacketTunnelProvider**: Para crear túneles VPN personalizados, que pueden configurarse para enrutar tráfico específico a través de una SIM de Macao para evitar las restricciones del GFW.
   - **Caso de Uso para GFW**: Al configurar una VPN en la SIM de Macao (que no está sujeta a la censura del GFW, ya que las redes de Macao son independientes), puedes enrutar el tráfico a través de un servidor fuera de China continental para acceder a servicios bloqueados como Google, WhatsApp o YouTube.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)
   - **Limitaciones**: Las configuraciones VPN normalmente se aplican a nivel del sistema, no por SIM. Necesitarías cambiar manualmente la SIM de datos activa o usar una solución VPN personalizada para enrutar el tráfico de forma selectiva.

3. **Configuración Dual SIM (Basada en Ajustes)**:
   - iOS es compatible con Dual SIM Dual Standby (DSDS) en iPhones compatibles (por ejemplo, iPhone XS, XR o posteriores comprados en regiones como Macao o Hong Kong, que admiten Dual SIM con dos nano-SIMs o eSIM). Esto te permite:[](https://support.apple.com/en-us/109317)[](https://support.apple.com/en-us/108898)
     - Asignar una SIM por defecto para datos celulares (Ajustes > Celular > Datos Celulares).
     - Activar "Permitir Cambio de Datos Celulares" para cambiar automáticamente entre SIMs según la cobertura o disponibilidad (Ajustes > Celular > Datos Celulares > Permitir Cambio de Datos Celulares).[](https://support.apple.com/en-us/108898)
     - Etiquetar las SIMs (por ejemplo, "SIM Macao" para acceso sin restricciones, "China Telecom" para servicios locales) y seleccionar manualmente qué SIM maneja los datos para tareas específicas.
   - **Separación Manual de Tráfico**: Puedes cambiar manualmente la SIM de datos activa en Ajustes para dirigir todo el tráfico celular a través de la SIM de Macao (para evitar el GFW) o de la SIM de China Telecom (para servicios locales sujetos al GFW). Sin embargo, iOS no proporciona una API para enrutar dinámicamente el tráfico a una SIM específica basándose en la aplicación o el destino sin la intervención del usuario.

4. **VPN por Aplicación (NetworkExtension)**:
   - iOS admite configuraciones de VPN por aplicación a través de las clases `NEAppProxyProvider` o `NEAppRule` en el framework NetworkExtension, típicamente utilizadas en entornos empresariales (por ejemplo, Configuraciones de Aplicaciones Gestionadas).
   - **Caso de Uso**: Podrías configurar una VPN por aplicación para enrutar el tráfico de aplicaciones específicas (por ejemplo, YouTube, Google) a través de un túnel VPN utilizando la conexión de datos de la SIM de Macao para evitar las restricciones del GFW, mientras que otras aplicaciones usan la SIM de China Telecom para servicios locales.
   - **Requisitos**: Esto requiere una aplicación VPN personalizada o una solución empresarial de Mobile Device Management (MDM), que es compleja de implementar para desarrolladores individuales. Adicionalmente, necesitarías asegurarte de que la SIM de Macao esté configurada como la SIM de datos activa cuando la VPN esté en uso.

5. **URLSession y Redes Personalizadas**:
   - La API `URLSession` te permite configurar solicitudes de red con interfaces celulares específicas usando `allowsCellularAccess` o vinculando a una interfaz de red específica.
   - **Caso de Uso**: Puedes deshabilitar programáticamente el acceso celular para ciertas solicitudes (forzando Wi-Fi u otra interfaz) o usar una VPN para enrutar el tráfico. Sin embargo, vincular solicitudes específicas a la interfaz celular de una SIM particular no es compatible directamente; necesitarías depender de la configuración de la SIM de datos activa del sistema.
   - **Solución Alternativa**: Combina `URLSession` con una VPN configurada para usar los datos de la SIM de Macao para enrutar el tráfico a servidores fuera de China.

### Manejo de las Restricciones del GFW con Dual SIMs

El Gran Cortafuegos de China (GFW) bloquea el acceso a muchos sitios web y servicios extranjeros (por ejemplo, Google, YouTube, WhatsApp) cuando se utilizan operadoras de China continental como China Telecom, ya que su tráfico se enruta a través de la infraestructura censurada de China. En contraste, una SIM de Macao (por ejemplo, de CTM o Three Macao) enruta el tráfico a través de las redes independientes de Macao, que no están sujetas a la censura del GFW (excepto China Telecom Macao, que aplica las restricciones del GFW). Así es como puedes aprovechar esto con una SIM de Macao y una SIM de China Telecom:[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)

1. **SIM de Macao para Acceso Sin Restricciones**:
   - Usa la SIM de Macao como el plan de datos celulares por defecto para aplicaciones o servicios bloqueados por el GFW (por ejemplo, Google, YouTube).
   - **Configuración**:
     - Ve a Ajustes > Celular > Datos Celulares y selecciona la SIM de Macao.
     - Asegúrate de que la itinerancia de datos esté habilitada para la SIM de Macao cuando estés en China continental, ya que enrutará el tráfico a través de la red de Macao, evitando el GFW.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
     - Opcionalmente, configura una VPN (por ejemplo, usando `NEVPNManager`) para asegurar aún más el tráfico, aunque una SIM de Macao típicamente no requiere una VPN para acceder a servicios bloqueados.
   - **Compatibilidad con API**: Usa `CTTelephonyNetworkInfo` para confirmar que la SIM de Macao está activa para datos (propiedad `dataServiceIdentifier`) y monitorear su estado.

2. **SIM de China Telecom para Servicios Locales**:
   - Usa la SIM de China Telecom para aplicaciones y servicios locales (por ejemplo, WeChat, Alipay) que requieran un número de teléfono chino o estén optimizados para las redes continentales.
   - **Configuración**:
     - Cambia manualmente a la SIM de China Telecom en Ajustes > Celular > Datos Celulares cuando accedas a servicios locales.
     - Ten en cuenta que el tráfico en esta SIM estará sujeto a las restricciones del GFW, bloqueando el acceso a muchos sitios extranjeros a menos que se use una VPN.
   - **Compatibilidad con API**: Usa `CTCellularData` para monitorear el uso de datos celulares y asegurarte de que la SIM correcta esté activa. También puedes usar `NEVPNManager` para configurar una VPN para aplicaciones específicas para evitar el GFW en la SIM de China Telecom, aunque la fiabilidad de las VPN en China es inconsistente debido al bloqueo activo.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

3. **Flujo de Trabajo Práctico para la Separación de Tráfico**:
   - **Cambio Manual**: Por simplicidad, cambia la SIM de datos activa en Ajustes según la tarea (por ejemplo, SIM de Macao para aplicaciones internacionales, SIM de China Telecom para aplicaciones locales). Este es el enfoque más directo pero requiere la intervención del usuario.
   - **VPN para la SIM de China Telecom**: Si necesitas acceder a servicios bloqueados mientras usas la SIM de China Telecom, configura una VPN usando `NEVPNManager`. Ten en cuenta que muchas VPNs (por ejemplo, ExpressVPN, NordVPN) pueden ser poco fiables en China debido al bloqueo del GFW, así que prueba proveedores como Astrill o soluciones personalizadas de antemano. Algunos proveedores de eSIM (por ejemplo, Holafly, ByteSIM) ofrecen VPNs integradas que pueden activarse para evitar las restricciones.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://www.reddit.com/r/chinalife/comments/1ebjcxi/can_you_use_esims_to_get_around_the_firewall/)[](https://esim.holafly.com/internet/mobile-internet-china/)
   - **VPN por Aplicación**: Para uso avanzado, desarrolla una aplicación personalizada usando `NEAppProxyProvider` para enrutar el tráfico de aplicaciones específicas a través de una VPN cuando la SIM de China Telecom esté activa, permitiendo que otras aplicaciones usen la SIM de Macao directamente.
   - **Limitaciones de Automatización**: iOS no proporciona una API para cambiar programáticamente la SIM de datos activa basándose en la aplicación o la URL de destino. Necesitarías depender del cambio de SIM iniciado por el usuario o de una VPN para gestionar el enrutamiento del tráfico.

### Pasos para Implementar la Separación de Tráfico

1. **Configurar Dual SIM**:
   - Asegúrate de que tu iPhone sea compatible con Dual SIM (por ejemplo, iPhone XS o posterior con iOS 12.1 o posterior).[](https://support.apple.com/en-us/109317)
   - Inserta la SIM de Macao y la SIM de China Telecom (o configura una eSIM para una de ellas).
   - Ve a Ajustes > Celular, etiqueta los planes (por ejemplo, "Macao" y "China Telecom") y establece la SIM de datos por defecto (por ejemplo, Macao para acceso sin restricciones).[](https://support.apple.com/en-us/108898)

2. **Configurar los Ajustes de Datos Celulares**:
   - Desactiva "Permitir Cambio de Datos Celulares" para prevenir el cambio automático de SIM, dándote control manual sobre qué SIM se usa para datos (Ajustes > Celular > Datos Celulares > Permitir Cambio de Datos Celulares).[](https://support.apple.com/en-us/108898)
   - Usa `CTTelephonyNetworkInfo` para verificar programáticamente qué SIM está activa para datos en tu aplicación.

3. **Implementar VPN para Evitar el GFW**:
   - Para la SIM de China Telecom, configura una VPN usando `NEVPNManager` o una aplicación VPN de terceros (por ejemplo, Astrill, VPN integrada de Holafly) para evitar las restricciones del GFW.
   - Para la SIM de Macao, una VPN puede no ser necesaria, ya que su tráfico se enruta fuera de la infraestructura censurada de China.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)

4. **Monitorear y Gestionar el Tráfico**:
   - Usa `CTCellularData` para monitorear el uso de datos celulares y asegurarte de que se esté usando la SIM correcta.
   - Para enrutamiento avanzado, explora `NEPacketTunnelProvider` para crear una VPN personalizada que enrute selectivamente el tráfico basándose en la aplicación o el destino, aunque esto requiere un esfuerzo de desarrollo significativo.

5. **Probar y Optimizar**:
   - Prueba la conectividad en China continental con ambas SIMs para asegurarte de que la SIM de Macao evita el GFW como se espera y que la SIM de China Telecom funciona para servicios locales.
   - Verifica el rendimiento de la VPN en la SIM de China Telecom, ya que el GFW bloquea activamente muchos protocolos VPN.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### Limitaciones y Desafíos

- **No Hay API Nativa para Enrutamiento Dinámico de SIM**: iOS no proporciona una API para enrutar dinámicamente el tráfico a una SIM específica basándose en la aplicación, URL o destino. Debes cambiar manualmente la SIM de datos activa o usar una VPN para gestionar el tráfico.
- **Bloqueo de VPN por el GFW**: El GFW bloquea activamente muchos protocolos VPN (por ejemplo, IPsec, PPTP), e incluso las VPNs basadas en SSL pueden ser limitadas en tasa si se detectan. Una SIM de Macao suele ser más fiable para evitar el GFW sin una VPN.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)
- **Restricciones de la SIM de China Telecom**: La red basada en CDMA de China Telecom puede tener problemas de compatibilidad con algunos teléfonos extranjeros, aunque su red LTE/5G es más ampliamente compatible. Adicionalmente, su tráfico está sujeto a la censura del GFW, requiriendo una VPN para servicios bloqueados.[](https://esim.holafly.com/sim-card/china-sim-card/)[](https://yesim.app/blog/mobile-internet-and-sim-card-in-china/)
- **Registro de Nombre Real**: Tanto las SIMs de Macao como de China Telecom pueden requerir registro de nombre real (por ejemplo, detalles del pasaporte), lo que puede complicar la configuración.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
- **Rendimiento**: La itinerancia en una SIM de Macao en China continental puede resultar en velocidades más lentas en comparación con una SIM local de China Telecom, especialmente en áreas rurales.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)

### Recomendaciones

- **Estrategia Principal**: Usa la SIM de Macao como el plan de datos celulares por defecto para acceder a servicios bloqueados, ya que naturalmente evita el GFW al enrutar el tráfico a través de las redes sin censura de Macao. Cambia a la SIM de China Telecom para aplicaciones locales como WeChat o Alipay que requieran un número chino o estén optimizadas para las redes continentales.[](https://prepaid-data-sim-card.fandom.com/wiki/Macau)[](https://www.reddit.com/r/shanghai/comments/10c9fqc/can_phone_data_roaming_from_overseas_bypass_the/)
- **VPN como Respaldo**: Para la SIM de China Telecom, usa un proveedor de VPN fiable (por ejemplo, Astrill, o eSIMs con VPNs integradas como Holafly o ByteSIM) para acceder a servicios bloqueados. Pre-instala y prueba la VPN antes de entrar a China, ya que descargar aplicaciones VPN en China puede estar restringido.[](https://esim.holafly.com/internet/mobile-internet-china/)[](https://bytesim.com/blogs/esim/mobile-internet-china)[](https://prepaid-data-sim-card.fandom.com/wiki/China)
- **Esfuerzo de Desarrollo**: Si estás construyendo una aplicación, usa `NetworkExtension` para implementar una VPN personalizada para el enrutamiento selectivo de tráfico, pero ten en cuenta que esto es complejo y puede requerir permisos de nivel empresarial. Para la mayoría de los usuarios, el cambio manual de SIM combinado con una VPN es suficiente.
- **Configuración Previa al Viaje**: Compra y activa ambas SIMs (o eSIMs) antes de llegar a China, ya que las políticas locales pueden restringir la compra de eSIMs en China continental. Por ejemplo, proveedores como Nomad o Holafly permiten la precompra y activación de eSIMs con bypass del GFW integrado.[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://www.getnomad.app/blog/do-esims-work-in-china)[](https://esim.holafly.com/internet/mobile-internet-china/)

### Ejemplo de Fragmento de Código

A continuación se muestra un ejemplo básico del uso de `CTTelephonyNetworkInfo` para verificar el plan celular activo y `NEVPNManager` para configurar una VPN para la SIM de China Telecom:

```swift
import CoreTelephony
import NetworkExtension

// Verificar el plan celular activo
func checkActiveCellularPlan() {
    let networkInfo = CTTelephonyNetworkInfo()
    if let dataService = networkInfo.serviceCurrentRadioAccessTechnology {
        for (serviceIdentifier, rat) in dataService {
            print("Servicio: \(serviceIdentifier), Tecnología de Acceso por Radio: \(rat)")
            // Identificar qué SIM está activa (por ejemplo, Macao o China Telecom)
        }
    }
}

// Configurar VPN para la SIM de China Telecom
func setupVPN() {
    let vpnManager = NEVPNManager.shared()
    vpnManager.loadFromPreferences { error in
        if let error = error {
            print("Error al cargar las preferencias de VPN: \(error)")
            return
        }
        
        let vpnProtocol = NEVPNProtocolIKEv2()
        vpnProtocol.serverAddress = "vpn.example.com" // Reemplaza con tu servidor VPN
        vpnProtocol.remoteIdentifier = "vpn.example.com"
        vpnProtocol.authenticationMethod = .certificate // Configurar según sea necesario
        
        vpnManager.protocolConfiguration = vpnProtocol
        vpnManager.isEnabled = true
        
        vpnManager.saveToPreferences { error in
            if let error = error {
                print("Error al guardar las preferencias de VPN: \(error)")
            } else {
                print("VPN configurada exitosamente")
            }
        }
    }
}
```

### Conclusión

Si bien iOS no ofrece una API nativa para enrutar dinámicamente el tráfico a SIMs específicas basándose en la aplicación o el destino, puedes lograr la separación del tráfico mediante:
1. El uso de la SIM de Macao para acceso sin restricciones y evitar el GFW sin una VPN.
2. El uso de la SIM de China Telecom para servicios locales, emparejada con una VPN (configurada vía `NEVPNManager` o una aplicación de terceros) para acceder a servicios bloqueados.
3. El cambio manual de la SIM de datos activa en Ajustes para diferentes tareas.
4. Opcionalmente, el desarrollo de una solución VPN personalizada con `NetworkExtension` para el enrutamiento de tráfico por aplicación, aunque esto es complejo.

Para el enfoque más simple, confía en la SIM de Macao para los servicios bloqueados por el GFW y cambia a la SIM de China Telecom para necesidades locales, pre-instalando una VPN fiable para esta última. Siempre prueba las configuraciones antes de viajar a China, ya que las políticas del GFW y la fiabilidad de las VPN pueden cambiar rápidamente.[](https://www.flyertalk.com/forum/china/2113715-sim-card-bypass-great-firewall.html)[](https://prepaid-data-sim-card.fandom.com/wiki/China)

¡Si necesitas más aclaraciones o asistencia con implementaciones específicas de API, házmelo saber!