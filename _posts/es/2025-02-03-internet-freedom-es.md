---
audio: false
generated: false
image: false
lang: es
layout: post
title: El viaje en busca de la libertad en Internet
translated: true
---

### Tabla de Contenidos

1. [Soluciones Proxy en China](#soluciones-proxy-en-china)
   - Soluciones con Tarjeta SIM de Macao (Mejor Opción)
   - Recomendaciones de Servidores Proxy
   - Configuración y Ajustes de Aplicaciones
   - Configuración de Pagos y Ajustes Regionales

2. [El Camino hacia la Libertad en Internet](#el-camino-hacia-la-libertad-en-internet)
   - Cronología de Métodos Proxy (2010-2025)
   - Comparación entre Libertad en Internet y Soluciones para la Miopía
   - Configuración Actual y Rendimiento
   - Métodos de Recuperación y Lecciones Aprendidas

3. [Tarjetas SIM de Macao](#tarjetas-sim-de-macao)
   - Detalles de la Tarjeta SIM China Telecom Easy+
   - Opciones de Tarjeta SIM Blue Macau
   - Precios y Planes de Datos
   - Compatibilidad con Dispositivos

4. [Problemas con Shadowsocks Proxy](#problemas-con-shadowsocks-proxy)
   - Problemas de Conectividad Específicos de Red
   - Diferencias de Rendimiento entre 5G y 4G
   - Pasos para Solucionar Problemas y Soluciones
   - Impacto de las Políticas de ISP y Operadoras

---

## Soluciones Proxy en China

*29.12.2024*

* La mejor opción es conseguir una tarjeta SIM de China Macao para usar datos móviles directamente cuando sea necesario. Visita [https://www.1888.com.mo](https://www.1888.com.mo). Cuesta alrededor de 80 CNY por 10 GB de datos móviles, ofreciendo una experiencia rápida y sin complicaciones.

* Las tarjetas SIM de China Telecom Macao están disponibles en dos tipos: roja y azul. Las tarjetas rojas ofrecen planes diarios, que suelen costar 2, 3 o 5 dólares de Macao por día. Las tarjetas azules proporcionan planes de datos, como 10 GB por 98 dólares de Macao o 20 GB por 198 dólares de Macao, sin cargos mensuales.

* Si necesitas más datos de red o usas una computadora portátil con frecuencia, considera usar [zhs.cloud](https://zhs.cloud). Proporciona acceso a aproximadamente 15 servidores proxy globales por solo 30 CNY al mes.

* En iOS, usa Shadowrocket con reglas de Shadowsocks: [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever). Configura el enrutamiento global para separar el tráfico de China del tráfico internacional.

* En Android, usa V2Ray. En Fire TV, usa la aplicación V2Ray. En Apple TV, usa la aplicación Shadowrocket. En Mac, usa la aplicación ShadowsocksX-NG o ClashX.

* No se recomienda configurar un servidor proxy por tu cuenta. Protocolos como Shadowsocks, VMess o Trojan son fácilmente bloqueados, independientemente del servidor utilizado.

* Para cambiar la App Store a la región de EE. UU., activa un proxy global (EE. UU.) y mostrará la opción de pago "Ninguno", permitiéndote cambiar abiertamente.

* Usa una tarjeta Visa para comprar tarjetas de regalo en Amazon o utiliza el portal de tarjetas de regalo de Apple para cargar tu cuenta de la App Store.

---

## El Camino hacia la Libertad en Internet

*03.02.2025, Esta publicación se actualizó por última vez en agosto de 2025.*

#### El Camino

De 2010 a 2013, usé Goagent y la herramienta proxy SwitchyOmega para evadir el GFW.

Entre 2014 y 2015, utilicé Qujing (曲径) para proxy y seguí a su autor en Twitter, quien ahora vive en Japón.

De junio de 2016 a julio de 2018, usé Digital Ocean para alojar mi servidor proxy de Shadowsocks.

A partir de 2019, comencé a usar https://zhs.cloud.

En marzo de 2023, empecé a usar una tarjeta SIM de Macao en mi teléfono móvil para acceder a internet sin proxy ni VPN. Esto costaba alrededor de 150 CNY al mes por 20 GB de datos móviles, y utilicé este método durante aproximadamente un año.

En 2024, volví a usar Outline Manager con mi servidor proxy de Shadowsocks, experimentando con varios proveedores de nube.

En febrero de 2025, mi configuración preferida es Outline Manager con un servidor de Aliyun en Hong Kong para uso diario y un servidor fuera de Hong Kong (como Singapur o Japón) para herramientas de IA. Mantengo la misma configuración de reglas proxy utilizada en Shadowrocket o Clash.

A partir de junio de 2025, comencé a usar un script en Python en mi computadora portátil para seleccionar automáticamente un servidor proxy cada 10 minutos según los resultados de pruebas de velocidad. El script prioriza los servidores de Singapur sobre los de Hong Kong para usar herramientas de IA. Para más detalles, consulta [Automatización de la Gestión de Proxy en Clash](/clash-en). Para el proveedor de nube VPN, seguí usando https://zhs.cloud.

Además, en iOS, volví a usar una tarjeta SIM de Macao, con un costo de 150 CNY al mes por 20 GB de datos. También compré 5 GB adicionales de datos tres veces por 20 MOP cada uno, totalizando alrededor de 200 CNY por 35 GB de datos en mi teléfono móvil.

Ha funcionado muy bien durante los últimos 2 meses. Espero poder seguir usando este método para navegar por internet hasta que me vaya de China para trabajar en el extranjero.

#### La Diferencia en Comparación con la Reversión de la Miopía

Un desafío es luchar contra el GFW, que es creado por el hombre. El otro es abordar los principios del funcionamiento de los músculos oculares.

Es fácil medir la efectividad de una solución proxy. Sin embargo, revertir la miopía requiere tiempo para determinar si el globo ocular está cambiando.

#### Similitudes con la Reversión de la Miopía

Una similitud es que tanto una solución proxy como los anteojos con una reducción de 200 grados suelen funcionar bien. Una implica acceder a internet y la otra mejorar la vista. Ambas abordan problemas muy importantes.

El principio subyacente es que si entendemos cómo funciona el GFW y encontramos una manera de eludirlo, la solución debería ser sencilla.

#### Razonamiento y Matices

Todavía no entiendo completamente cómo funciona el GFW. Cuando la IP de mi servidor proxy es bloqueada, ahora tengo más formas de investigar la causa.

Puedo verificar si el bloqueo ocurre en la red móvil o en el banda ancha doméstica. Si es en la red móvil, puedo comprobar si es en 4G o 5G.

Del mismo modo, si mi miopía no mejora después de seis meses o un año, debo investigar si hay diferencias entre mis ojos. También debo considerar si he estado viendo las cosas apenas con claridad sin forzar mis ojos durante la mayor parte del año.

#### Estado Actual

Mi servidor proxy está funcionando muy bien actualmente. Las velocidades de descarga en mi teléfono alcanzan los 80 Mbps y las de subida 50 Mbps al conectarme al servidor proxy de Hong Kong. Lo mismo ocurre en mi computadora portátil.

Uso las mismas configuraciones de proxy en mi computadora portátil y teléfonos, y funcionan perfectamente. Normalmente, uso un servidor proxy para visitar sitios fuera de China y un servidor no HK para herramientas de IA.

#### Recuperación

Si algo falla, mi método de recuperación es simple. Solo necesito cambiar la IP elástica de mi servidor proxy de Aliyun en Hong Kong y subir la nueva URL del proxy al almacenamiento en la nube. Esto significa que debo ejecutar dos scripts, lo que toma alrededor de 1 minuto, y mi computadora portátil y teléfonos pueden actualizar la dirección del servidor proxy.

#### Arrepentimiento

Luché contra el GFW demasiadas veces y durante demasiado tiempo. Probé muchos protocolos proxy, sabiendo que serían detectados por el GFW y bloqueados. Sin un servidor proxy confiable, es difícil configurar un proxy en un router OpenWrt.

Una cosa que lamento es no haber aprendido las técnicas de los proveedores de proxy antes, como [zhs.cloud](https://zhs.cloud). Ahora conozco la mayoría de sus secretos.

Lo otro es que, cada vez que mi servidor proxy era bloqueado, no lo pensaba demasiado. Parecía que solo necesitaba configurar un nuevo servidor proxy para obtener una nueva dirección IP que no hubiera sido bloqueada. Pero ese era un pensamiento superficial.

#### Métricas

Lamento no haber usado Speedtest antes. Conocía el nombre de la herramienta desde hace mucho tiempo, pero no aprendí a usarla correctamente.

Es bueno usar Speedtest con frecuencia al conectarse a estaciones de señal móvil 5G o 4G o a una red de banda ancha doméstica.

Para revertir la miopía, es lo mismo. Compré un optotipo en forma de C y un optotipo estándar.

Sin medición, no hay mejora. Medir las cosas te ayuda a aprender. Usar Speedtest con frecuencia me ayuda a descubrir que en una red 5G es fácil superar los 100 Mbps, mientras que en una red de banda ancha doméstica es difícil superar los 100 Mbps.

#### Todavía es Temprano

¿Caerá el muro del GFW en los próximos años? Es difícil decirlo.

Cuando, después de revertir la miopía durante dos años, le dije a un amigo que mi método de reversión necesitaba mejorar y que necesitaba usar gafas con 200 grados menos que mi graduación real en lugar de 150 grados menos,

él dijo que no había problema, que estaba bien, que no era una pérdida de tiempo y que aún era temprano. Sí. Estas cosas son fundamentales. Como la miopía, la gente debería descubrirlo antes. Todd Becker compartió este descubrimiento en YouTube en 2014, y los videos obtuvieron más de 1 millón de visitas. Y ahora es 2025, ¿cuántas personas lo saben realmente en el mundo? Supongo que serán menos de 10 mil.

---

## Tarjetas SIM de Macao

*20.04.2023*

#### Mi Experiencia con Tarjetas SIM de Macao

Durante mi visita de fin de semana a Macao en 2023, compré una tarjeta SIM China Telecom Easy+ Macau. Al llegar a Guangzhou, descubrí que seguía funcionando perfectamente, ayudándome a aprender inglés y descargar muchas aplicaciones extranjeras. Me sentía como si aún estuviera en Macao. La recomiendo encarecidamente. Más tarde, probé la tarjeta SIM Blue Macau, que también era buena. Aquí tienes un resumen rápido de ambas:

#### Tarjeta SIM China Telecom Easy+ Macau

¡Fácil de usar en cualquier momento!

### Puntos Clave
- Sin depósito; activación automática para China continental, Macao y Hong Kong.
- Sin contrato ni tarifa de cancelación; lista para usar al comprar.
- Número de Macao incluido; número opcional de China continental para uso de doble número.
- Recarga en línea o con tarjetas de valor.

### Opciones de Tarifa Diaria
- $2/día: 4 GB de alta velocidad, luego ilimitado a velocidad reducida; 5,000 minutos de llamadas locales.
- $3/día: 10 GB de alta velocidad, luego ilimitado a velocidad reducida; 5,000 minutos de llamadas locales.
- $5/día: 20 GB de alta velocidad, luego ilimitado a velocidad reducida; 5,000 minutos de llamadas locales.

### Extras
- Uso de datos en Hong Kong: $0.1/MB.
- Cambia de plan en cualquier momento enviando un mensaje de texto.

#### Tarjeta SIM Blue Macau

### Puntos Clave
- Sin renta mensual; paga según uses.
- Llamadas locales: 0.39 MOP/minuto; Internet: 0.1 MOP/MB; SMS: 1 MOP/mensaje.
- Paquetes de datos opcionales sin caducidad: 10 GB por 98 MOP, 20 GB por 188 MOP, 40 GB por 288 MOP.
- Recarga cada 180 días para mantenerla activa.

#### Dispositivos Compatibles

- Requiere un teléfono con red completa 4G o compatible con China Telecom.

Para más información, visita [China Telecom Macau](https://www.1888.com.mo/).

---

También puedes encontrarlas en Taobao:

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Problemas con Shadowsocks Proxy

*03.01.2025*

Zhiwei:

Salí a una barbacoa con un amigo y usé Shadowsocks con un servidor basado en Singapur como proxy para evadir el Gran Cortafuegos (GFW). Mientras usaba 5G fuera, no podía conectarme y la prueba fallaba al intentar acceder a YouTube. Sin embargo, cuando estoy en casa usando 4G o mi red doméstica de China Telecom, Shadowsocks funciona bien. ¿Por qué ocurre esto?

Mistral:

Parece que estás experimentando problemas de conectividad con tu proxy Shadowsocks cuando usas 5G fuera, pero no cuando usas 4G o tu red doméstica. Puede haber varias razones para esto:

1. Diferencias en la Configuración de la Red:
   - Red 5G: La red 5G puede tener configuraciones o restricciones diferentes en comparación con 4G. Algunos operadores pueden tener reglas de firewall más estrictas o un enrutamiento de red diferente para 5G, lo que podría afectar el rendimiento de tu proxy Shadowsocks.
   - Red 4G: La red 4G puede tener configuraciones más relajadas o mejor enrutamiento que permite que tu proxy Shadowsocks funcione correctamente.

2. Restricciones del ISP:
   - Políticas del Operador: Diferentes operadores pueden tener políticas distintas con respecto al uso de VPN o proxies. Tu operador de 5G puede tener políticas más estrictas que bloquean o limitan el tráfico de VPN, incluyendo Shadowsocks.
   - Red Doméstica: Tu red doméstica, proporcionada por China Telecom, puede tener menos restricciones, permitiendo que Shadowsocks funcione sin problemas.

3. Fuerza y Estabilidad de la Señal:
   - Señal 5G: La estabilidad y fuerza de la señal 5G puede variar, especialmente en entornos al aire libre. Señales débiles o inestables pueden causar problemas de conectividad, incluyendo tiempo de espera.
   - Señal 4G: La señal 4G puede ser más estable y consistente, proporcionando una mejor conexión para tu proxy Shadowsocks.

4. Ubicación del Servidor Proxy:
   - Servidor en Singapur: La ubicación de tu servidor Shadowsocks en Singapur puede afectar la latencia y la conectividad. La red 5G puede tener mayor latencia o un enrutamiento menos óptimo hacia el servidor de Singapur en comparación con la red 4G o tu red doméstica.

5. Configuración del Dispositivo:
   - Configuración: Asegúrate de que la configuración de tu dispositivo esté correctamente ajustada para usar Shadowsocks. A veces, cambiar de red (de 5G a 4G o Wi-Fi doméstico) puede hacer que la configuración se restablezca o cambie.
   - Permisos de la Aplicación: Asegúrate de que la aplicación Shadowsocks tenga los permisos necesarios para operar en diferentes redes.

### Pasos para Solucionar Problemas:

1. Verifica la Configuración de la Red:
   - Asegúrate de que la configuración de Shadowsocks esté correctamente ajustada para redes 5G y 4G.
   - Verifica que no haya restricciones o configuraciones específicas en tu red 5G que puedan estar bloqueando el proxy.

2. Prueba Diferentes Servidores:
   - Intenta conectarte a diferentes servidores Shadowsocks para ver si el problema es específico del servidor de Singapur.
   - Revisa la latencia y estabilidad de la conexión al servidor.

3. Contacta a tu Operador:
   - Si el problema persiste, contacta a tu operador de 5G para preguntar sobre restricciones o configuraciones que puedan estar afectando tu conexión Shadowsocks.

4. Actualiza el Software:
   - Asegúrate de que la aplicación Shadowsocks y el software de tu dispositivo estén actualizados. A veces, las actualizaciones pueden resolver problemas de conectividad.

5. Usa Proxies Alternativos:
   - Considera usar servicios de proxy o VPN alternativos que puedan tener mejor compatibilidad con tu red 5G.

Al revisar sistemáticamente estos factores, deberías poder identificar la causa del problema de conectividad y encontrar una solución adecuada.

--

Actualización:

En realidad, mi Wi-Fi doméstico usa China Mobile Communications Corporation, y su dirección es como 120.235.8.xx.

Curiosamente, he observado patrones de conectividad inconsistentes: mientras que mi servidor proxy funciona normalmente en datos móviles y redes de China Telecom, ocasionalmente falla al conectarse cuando uso mi red Wi-Fi doméstica.