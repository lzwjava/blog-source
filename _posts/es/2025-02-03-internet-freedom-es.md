---
audio: false
generated: false
image: true
lang: es
layout: post
title: El viaje para buscar la libertad en internet
translated: true
type: post
---

### Tabla de Contenidos

1. [Soluciones de Proxy en China](#proxy-solutions-in-china)
   - Usar tarjeta SIM de Macao para acceso directo
   - Recomendar proveedores de servidores proxy económicos
   - Configurar aplicaciones con reglas de enrutamiento global
   - Evitar configuraciones de servidor proxy autoalojadas
   - Cambiar la región de la App Store con proxy

2. [El Viaje para Perseguir la Libertad en Internet](#the-journey-to-pursue-internet-freedom)
   - Cronología de la evolución del método proxy
   - Comparar la lucha contra el GFW con la reversión de la miopía
   - La configuración actual utiliza múltiples servidores proxy
   - Selección automática de proxy basada en la velocidad
   - Lamentar no haber aprendido antes las técnicas de los proveedores

3. [Tarjetas SIM de Macao](#macau-sim-cards)
   - Detalles de la tarjeta SIM China Telecom Easy+
   - Tarjeta SIM Azul de Macao de pago por uso
   - Varios planes diarios de tarifas y datos
   - Requiere un dispositivo compatible con 4G
   - Sin contrato ni tarifas de cancelación

4. [Problemas con el Proxy Shadowsocks](#shadowsocks-proxy-issues)
   - Ocurren problemas de conectividad específicos de la red
   - Diferencias de rendimiento entre 5G y 4G
   - Las políticas del operador pueden bloquear el tráfico del proxy
   - La ubicación del servidor afecta la latencia
   - Solucionar problemas con diferentes servidores

5. [Registrarse en Cualquier Plataforma Independientemente de la Identidad](#registering-on-any-platform-regardless-of-identity)
   - Usar múltiples cuentas de correo electrónico para el registro
   - Alquilar números de teléfono a través de servicios en línea
   - Cambiar la región de la Apple Store con proxy
   - Restricciones de pago con tarjetas Visa chinas
   - Los documentos de identidad chinos a veces ayudan


## Soluciones de Proxy en China

*2024.12.29*

* La mejor manera es conseguir una tarjeta SIM de Macao (China) para usar los datos móviles directamente cuando sea necesario. Visita [https://www.1888.com.mo](https://www.1888.com.mo). Cuesta alrededor de 80 CNY por 10 GB de datos móviles, ofreciendo una experiencia rápida y sin problemas.

* Las tarjetas SIM de China Telecom Macao están disponibles en dos tipos: rojas y azules. Las tarjetas rojas ofrecen planes diarios, que suelen costar 2, 3 o 5 dólares de Macao por día. Las tarjetas azules proporcionan planes de datos, como 10 GB por 98 dólares de Macao o 20 GB por 198 dólares de Macao, sin cargos mensuales.

* Si necesitas más datos de red o usas una laptop con frecuencia, considera usar [zhs.cloud](https://zhs.cloud). Proporciona acceso a aproximadamente 15 servidores proxy globales por solo 30 CNY al mes.

* En iOS, usa Shadowrocket con reglas Shadowsocks: [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever). Configura el enrutamiento global para separar el tráfico de China del tráfico internacional.

* En Android, usa V2Ray. En Fire TV, usa la aplicación V2Ray. En Apple TV, usa la aplicación Shadowrocket. En Mac, usa la aplicación ShadowsocksX-NG o ClashX.

* No se recomienda configurar un servidor proxy por tu cuenta. Protocolos como Shadowsocks, VMess o Trojan se prohíben fácilmente, independientemente del servidor utilizado.

* Para cambiar la App Store a la región de EE. UU., activa un proxy global (EE. UU.) y mostrará la opción de pago "Ninguno", lo que te permitirá cambiar libremente.

* Usa una tarjeta Visa para comprar tarjetas de regalo en Amazon o usa el portal de tarjetas de regalo de Apple para cargar tu cuenta de App Store.

---

## El Viaje para Perseguir la Libertad en Internet

*2025.02.03, Esta publicación fue actualizada por última vez en agosto de 2025.*

#### El Viaje

De 2010 a 2013, utilicé Goagent y la herramienta proxy SwitchyOmega para eludir el GFW.

Entre 2014 y 2015, utilicé Qujing (曲径) para el proxy y seguí a su autor en Twitter, quien ahora vive en Japón.

Desde junio de 2016 hasta julio de 2018, utilicé Digital Ocean para alojar mi servidor proxy shadowsocks.

A partir de 2019, comencé a usar https://zhs.cloud.

En marzo de 2023, comencé a usar una tarjeta SIM de Macao en mi teléfono móvil para acceder a internet sin proxy ni VPN. Esto costaba alrededor de 150 CNY al mes por 20 GB de datos móviles, y utilicé este método durante aproximadamente un año.

En 2024, comencé a usar Outline Manager nuevamente con mi servidor proxy shadowsocks, experimentando con varios proveedores de la nube.

En febrero de 2025, mi configuración preferida es Outline Manager con un servidor Aliyun Hong Kong para uso diario y un servidor que no sea de Hong Kong (como Singapur o Japón) para herramientas de IA. Mantengo la misma configuración de reglas de proxy utilizada en Shadowrocket o Clash.

A partir de junio de 2025, comencé a usar un script de Python en mi laptop para seleccionar automáticamente un servidor proxy cada 10 minutos basándose en los resultados de las pruebas de velocidad. El script prioriza los servidores de Singapur sobre los de Hong Kong para usar herramientas de IA. Para más detalles, consulta [Automatización de la Gestión de Proxy de Clash](/clash-en). Para el proveedor de la nube VPN, seguí usando https://zhs.cloud.

Además, en iOS, volví a usar una tarjeta SIM de Macao, que cuesta 150 CNY al mes por 20 GB de datos. También compré 5 GB de datos adicionales tres veces por 20 MOP cada una, sumando un total de alrededor de 200 CNY por 35 GB de datos en mi teléfono móvil.

A partir de mediados de octubre de 2025, dejé de usar mi plan de tarjeta SIM de Macao porque he estado usando alrededor de 35 GB al mes en los últimos meses. El uso de aplicaciones chinas, que representan aproximadamente un tercio de mi uso de datos, principalmente en WeChat, consumiría datos móviles.

Comencé a usar la aplicación iOS Shadowsocks nuevamente con servidores proxy de https://zhs.cloud. Y comencé a aprender algunos conocimientos sobre los cables CN2.


#### La Diferencia Comparada con Revertir la Miopía

Un desafío es luchar contra el GFW, que es una creación humana. El otro es abordar los principios de la función de los músculos oculares.

Es fácil medir la efectividad de una solución de proxy. Sin embargo, revertir la miopía requiere tiempo para determinar si el globo ocular está cambiando.

#### Similitudes con la Reversión de la Miopía

Una similitud es que tanto una solución de proxy como unas gafas con una reducción de 200 grados a menudo funcionan bien. Una implica el acceso a internet y la otra la mejora de la vista. Ambas abordan problemas muy importantes.

El principio subyacente es que si entendemos cómo funciona el GFW y encontramos una manera de eludirlo, la solución debería ser sencilla.

#### Razonamiento y Matices

Todavía no entiendo completamente cómo funciona el GFW. Cuando la IP de mi servidor proxy es bloqueada, ahora tengo más formas de investigar la causa.

Puedo verificar si el bloqueo ocurre en la red celular o en la banda ancha doméstica. Si es la red celular, puedo verificar si es en 4G o 5G.

De manera similar, si mi miopía no mejora después de seis meses o un año, necesito investigar si hay diferencias entre mis ojos. También debo considerar si he estado viendo las cosas apenas con claridad sin forzar la vista durante la mayor parte del año.

#### Estado Actual

Mi servidor proxy actualmente funciona muy bien. Las velocidades de descarga en mi teléfono alcanzan los 80 Mbps y las velocidades de carga alcanzan los 50 Mbps al conectarse al servidor proxy de Hong Kong. Lo mismo ocurre en mi laptop.

Uso las mismas configuraciones de proxy en mi laptop y teléfonos, y funcionan perfectamente. Normalmente, uso un servidor proxy para visitar sitios fuera de China, y uso un servidor que no sea de Hong Kong para herramientas de IA.

#### Recuperación

Si las cosas están rotas, mi método de recuperación es simple. Solo necesito cambiar la IP elástica de mi servidor proxy Aliyun Hong Kong y cargar la nueva URL del proxy en el almacenamiento en la nube. Esto significa que necesito ejecutar dos scripts, lo que toma aproximadamente 1 minuto, y mi laptop y teléfonos pueden actualizar la dirección del servidor proxy.

#### Arrepentimiento

Luché demasiadas veces y durante demasiado tiempo contra el GFW. Probé muchos protocolos de proxy, sabiendo que serían detectados por el GFW y serían prohibidos. Sin un servidor proxy confiable, es difícil configurar un proxy en un enrutador OpenWrt.

Una cosa de la que me arrepiento es no haber aprendido antes las técnicas de los proveedores de proxy, como [zhs.cloud](https://zhs.cloud). Ahora conozco la mayoría de sus secretos.

Lo otro es que cada vez que mi servidor proxy era prohibido, no pensaba demasiado. Parecía que solo necesitabas configurar un nuevo servidor proxy para obtener una nueva dirección IP que no hubiera sido prohibida. Pero eso era un pensamiento superficial.

#### Métricas

Lamento no haber usado Speedtest antes. Conocía el nombre de la herramienta hace mucho tiempo, pero no aprendí a usarla cuidadosamente.

Es bueno usar Speedtest a menudo cuando se conecta a estaciones de señal móvil 5G o 4G o a una red de banda ancha doméstica.

Para revertir la miopía, es lo mismo. Compré una tabla optométrica en forma de C y una tabla optométrica estándar.

Sin medir, no hay mejora. Medir las cosas te ayuda a aprender. Usar Speedtest a menudo me ayuda a descubrir que en una red 5G, es fácil superar los 100 Mbps, mientras que en una red de banda ancha doméstica, es difícil superar los 100 Mbps.

#### Aún Es Temprano

¿Caerá el muro del GFW en los próximos años? Es difícil decirlo.

Cuando, después de revertir mi miopía durante dos años, le dije a mi amigo que mi método de reversión necesitaba ser mejorado y que necesitaba usar gafas con 200 grados menos de mi prescripción real en lugar de 150 grados menos.

Él dijo que no había problema, que estaba bien, que no era una pérdida de tiempo, y que todavía era temprano. Sí. Estas cosas son fundamentales. Como la miopía, la gente debería descubrirlo antes. Todd Becker compartió este descubrimiento en YouTube en 2014, y los videos obtuvieron más de 1 millón de visitas. Y ahora es 2025, ¿cuántas personas realmente lo saben en el mundo? Supongo que serán menos de 10 mil.


---

## Tarjetas SIM de Macao

*2023.04.20*

#### Mi Experiencia con las Tarjetas SIM de Macao

Durante mi visita de fin de semana a Macao en 2023, compré una tarjeta SIM Easy+ de China Telecom Macao. Al llegar a Guangzhou, descubrí que seguía funcionando perfectamente, ayudándome a aprender inglés y a descargar muchas aplicaciones extranjeras. Se sentía como si aún estuviera en Macao. La recomiendo encarecidamente. Más tarde, probé la tarjeta SIM Azul de Macao, que también fue buena. Aquí tienes un resumen rápido de ambas:

#### Tarjeta SIM China Telecom Easy+

¡Fácil de usar en cualquier momento!

### Puntos Clave
- Sin depósito; activación automática para China continental, Macao y Hong Kong.
- Sin contrato ni tarifa de cancelación; lista para usar al comprar.
- Número de Macao incluido; número opcional de China continental para uso con doble número.
- Recarga en línea o con tarjetas de valor.

### Opciones de Tarifa Diaria
- $2/día: 4GB de alta velocidad, luego ilimitado a velocidad reducida; 5,000 minutos de llamadas locales.
- $3/día: 10GB de alta velocidad, luego ilimitado a velocidad reducida; 5,000 minutos de llamadas locales.
- $5/día: 20GB de alta velocidad, luego ilimitado a velocidad reducida; 5,000 minutos de llamadas locales.

### Extras
- Uso de datos en Hong Kong: $0.1/MB.
- Cambia de plan en cualquier momento enviando un mensaje de texto.

#### Tarjeta SIM Azul de Macao

### Puntos Clave
- Sin renta mensual; pago por uso.
- Llamadas locales: 0.39 MOP/minuto; Internet: 0.1 MOP/MB; SMS: 1 MOP/mensaje.
- Paquetes de datos opcionales sin vencimiento: 10GB por 98 MOP, 20GB por 188 MOP, 40GB por 288 MOP.
- Recarga cada 180 días para mantenerla activa.

#### Dispositivos Compatibles

- Requiere un teléfono 4G de red completa o compatible con China Telecom.

Para más información, visita [China Telecom Macau](https://www.1888.com.mo/).

---

También puedes encontrarlos en Taobao:

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Problemas con el Proxy Shadowsocks

*2025.01.03*

Zhiwei:

Salí a hacer una barbacoa con un amigo y usé Shadowsocks con un servidor basado en Singapur como mi proxy para eludir el Gran Cortafuegos (GFW). Usando 5G afuera, no pude conectarme, y la prueba agotó el tiempo al intentar acceder a YouTube. Sin embargo, cuando estoy en casa usando 4G o mi red doméstica de China Telecom, Shadowsocks funciona bien. ¿Por qué ocurre esto?

Mistral:

Parece que estás experimentando problemas de conectividad con tu proxy Shadowsocks cuando usas 5G en el exterior, pero no cuando usas 4G o tu red doméstica. Esto podría deberse a varias razones:

1. Diferencias en la configuración de red:
   - Red 5G: La red 5G podría tener diferentes configuraciones o restricciones en comparación con 4G. Algunos operadores podrían tener reglas de firewall más estrictas o un enrutamiento de red diferente para 5G, lo que podría afectar el rendimiento de tu proxy Shadowsocks.
   - Red 4G: La red 4G podría tener configuraciones más relajadas o un mejor enrutamiento que permite que tu proxy Shadowsocks funcione correctamente.

2. Restricciones del ISP:
   - Políticas del operador: Diferentes operadores podrían tener diferentes políticas con respecto al uso de VPNs o proxies. Tu operador 5G podría tener políticas más estrictas que bloquean o limitan el tráfico VPN, incluyendo Shadowsocks.
   - Red doméstica: Tu red doméstica, proporcionada por China Telecom, podría tener menos restricciones, lo que permite que Shadowsocks funcione sin problemas.

3. Fuerza y estabilidad de la señal:
   - Señal 5G: La estabilidad y fuerza de la señal 5G pueden variar, especialmente en entornos exteriores. Las señales débiles o inestables pueden causar problemas de conectividad, incluyendo tiempos de espera.
   - Señal 4G: La señal 4G podría ser más estable y consistente, proporcionando una mejor conexión para tu proxy Shadowsocks.

4. Ubicación del servidor proxy:
   - Servidor de Singapur: La ubicación de tu servidor Shadowsocks en Singapur podría afectar la latencia y la conectividad. La red 5G podría tener una latencia más alta o un enrutamiento menos óptimo hacia el servidor de Singapur en comparación con la red 4G o tu red doméstica.

5. Configuración del dispositivo:
   - Configuración: Asegúrate de que la configuración de tu dispositivo esté correctamente configurada para usar Shadowsocks. A veces, cambiar de red (de 5G a 4G o Wi-Fi doméstico) puede hacer que la configuración se reinicie o cambie.
   - Permisos de la aplicación: Asegúrate de que la aplicación Shadowsocks tenga los permisos necesarios para operar en diferentes redes.

### Pasos para la resolución de problemas:

1. Verificar la configuración de red:
   - Asegúrate de que tu configuración de Shadowsocks esté correctamente configurada tanto para redes 5G como 4G.
   - Verifica que no haya restricciones o configuraciones específicas en tu red 5G que puedan estar bloqueando el proxy.

2. Probar diferentes servidores:
   - Intenta conectarte a diferentes servidores Shadowsocks para ver si el problema es específico del servidor de Singapur.
   - Verifica la latencia y la estabilidad de la conexión al servidor.

3. Contactar a tu operador:
   - Si el problema persiste, contacta a tu operador 5G para preguntar sobre cualquier restricción o configuración que pueda estar afectando tu conexión Shadowsocks.

4. Actualizar software:
   - Asegúrate de que tu aplicación Shadowsocks y el software del dispositivo estén actualizados. A veces, las actualizaciones pueden resolver problemas de conectividad.

5. Usar proxies alternativos:
   - Considera usar servicios proxy o VPN alternativos que puedan tener una mejor compatibilidad con tu red 5G.

Al verificar sistemáticamente estos factores, deberías poder identificar la causa del problema de conectividad y encontrar una solución adecuada.

--

Actualización:

En realidad, mi Wi-Fi doméstico utiliza China Mobile Communications Corporation, y su dirección es como 120.235.8.xx.

Curiosamente, he observado patrones de conectividad inconsistentes: mientras que mi servidor proxy funciona normalmente en datos móviles y redes de China Telecom, ocasionalmente falla al conectarse cuando uso mi red Wi-Fi doméstica.

---

## Registrarse en Cualquier Plataforma Independientemente de la Identidad

Soy un ciudadano chino y un ingeniero de software centrado en la última tecnología. Es frustrante ver muchos productos que prohíben el acceso desde China. Aunque todavía estoy trabajando en mi título de asociado y espero trabajar fuera de China algún día, permaneceré en China por unos años más. Mientras tanto, me gustaría compartir información sobre cómo superar las barreras de Internet basadas en la nacionalidad.

#### Correo electrónico

Tener varias cuentas de correo electrónico es mejor. Claude prohibió mi Gmail debido al acceso VPN, así que registré un nuevo correo electrónico de Outlook y funcionó bien.

#### Número de Teléfono

A través de [http://sms-activate.org](http://sms-activate.org), es posible alquilar un número de teléfono para registrarse. Sin embargo, el problema es que las cuentas registradas con dichos números de teléfono pueden tener algunos riesgos.

En China, personalmente recomiendo [https://www.1888.com.mo](https://www.1888.com.mo) para una tarjeta China Telecom Macau. También he probado la tarjeta SIM Giffgaff del Reino Unido y recientemente pedí una tarjeta SIM PayGo T-Mobile USA.

#### Región de la Apple Store

Para cambiar la App Store a la región de EE. UU., activa un proxy global (EE. UU.) y mostrará la opción de pago "Ninguno", lo que te permitirá cambiar libremente.

Puedes usar una tarjeta Visa para comprar tarjetas de regalo de Amazon o usar el portal de tarjetas de regalo de Apple para financiar tu cuenta de App Store.

El mismo método se aplica a Singapur u otras regiones.

#### Pago

Tener una tarjeta Visa es conveniente. Sin embargo, las tarjetas Visa emitidas por China todavía tienen algunas restricciones. Por ejemplo, Anthropic u OpenAI no aceptan tarjetas Visa emitidas en China.

#### VPN

Puedes consultar [Soluciones de Proxy en China](./proxy-en) y [Configura tu Servidor Proxy](./diy-proxy-en).

#### Identidad

Tengo una tarjeta de identidad de ciudadano chino y pasaporte, lo cual puede ser útil en ciertas situaciones.