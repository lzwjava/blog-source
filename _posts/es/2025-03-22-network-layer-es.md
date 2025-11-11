---
audio: false
generated: true
lang: es
layout: post
title: Capa de Red
translated: true
type: note
---

Bien, profundicemos en un tutorial detallado sobre la Capa de Red, específicamente adaptado para el curso de Tecnología de Redes Informáticas dentro del sistema chino de Exámenes de Autoaprendizaje (自考). Este capítulo es crucial para comprender cómo viajan los datos a través de las redes.

## Tutorial de la Capa de Red

La Capa de Red es la tercera capa en el modelo OSI y en el modelo TCP/IP. Su responsabilidad principal es facilitar el movimiento de paquetes de datos desde un host de origen a un host de destino a través de una o más redes. Piensa en ella como el servicio postal de Internet: determina la mejor ruta y asegura que tu "paquete" (paquete de datos) llegue a la dirección correcta.

Aquí tienes un desglose de los temas clave dentro de este capítulo:

### 1. Funciones de la Capa de Red

La Capa de Red realiza tres funciones principales:

#### a) Direccionamiento Lógico

*   **Propósito:** Identificar de forma única cada host en una red. Esto es diferente de la dirección física (dirección MAC) que identifica un dispositivo dentro de una red local. Las direcciones lógicas son jerárquicas y permiten un enrutamiento eficiente.
*   **Concepto Clave:** Las direcciones IP (direcciones del Protocolo de Internet) son la forma principal de direccionamiento lógico utilizado en la Capa de Red.
*   **Analogía:** Piensa en la dirección de tu casa. Es una dirección lógica que ayuda al servicio postal a encontrar tu casa específica dentro de una ciudad y un país, independientemente de la ubicación física de la oficina de correos.

#### b) Enrutamiento

*   **Propósito:** Determinar la mejor ruta para que un paquete de datos viaje desde el origen hasta el destino. Esto implica seleccionar una secuencia de dispositivos de red (routers) que atravesará el paquete.
*   **Concepto Clave:** Los algoritmos de enrutamiento son utilizados por los routers para construir y mantener tablas de enrutamiento, que contienen información sobre las mejores rutas hacia diferentes redes.
*   **Analogía:** Imagina planificar un viaje por carretera. Miras un mapa o usas un GPS para averiguar la mejor ruta a tu destino, considerando factores como la distancia y el tráfico. Los routers hacen algo similar para los paquetes de datos.

#### c) Reenvío

*   **Propósito:** El proceso real de mover un paquete de datos desde un puerto de entrada de un router al puerto de salida apropiado basándose en la decisión de enrutamiento.
*   **Concepto Clave:** Cuando un router recibe un paquete, examina la dirección IP de destino y consulta su tabla de enrutamiento para determinar el siguiente salto (otro router o el host de destino).
*   **Analogía:** Una vez que has planificado tu ruta, el reenvío es como conducir tu coche a lo largo de esa ruta, moviéndote de un punto al siguiente.

### 2. Direccionamiento IP

Las direcciones IP son fundamentales para la Capa de Red. Hay dos versiones principales: IPv4 e IPv6.

#### a) Estructura IPv4

*   **Formato:** Una dirección numérica de 32 bits escrita en notación decimal punteada (por ejemplo, 192.168.1.10). Se divide en cuatro octetos de 8 bits.
*   **Clases de Direcciones (Históricamente):** Aunque ahora son en gran parte obsoletas debido al Enrutamiento Inter-Dominio sin Clases (CIDR), comprender las clases históricas (A, B, C, D, E) puede ser útil para el conocimiento fundamental.
    *   **Clase A:** Redes grandes (primer octeto 1-126).
    *   **Clase B:** Redes de tamaño mediano (primer octeto 128-191).
    *   **Clase C:** Redes pequeñas (primer octeto 192-223).
    *   **Clase D:** Direcciones de multidifusión (primer octeto 224-239).
    *   **Clase E:** Reservadas para uso experimental (primer octeto 240-255).
*   **ID de Red e ID de Host:** Una dirección IPv4 consiste en un ID de red (identifica la red) y un ID de host (identifica un dispositivo específico dentro de esa red). La división entre estos IDs depende de la clase de dirección (o de la máscara de subred en CIDR).
*   **Direcciones IPv4 Especiales:**
    *   **0.0.0.0:** Representa la red actual.
    *   **127.0.0.1 (Dirección de Loopback):** Se utiliza para probar la pila de red de la máquina local.
    *   **Direcciones IP Privadas:** Rangos reservados para su uso dentro de redes privadas (por ejemplo, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). Estas direcciones no son enrutables en la Internet pública.
    *   **Direcciones IP Públicas:** Direcciones que son enrutables en la Internet pública.

#### b) Estructura IPv6

*   **Formato:** Una dirección numérica de 128 bits escrita en formato hexadecimal, agrupada en ocho segmentos de 16 bits separados por dos puntos (por ejemplo, 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
*   **Ventajas sobre IPv4:** Espacio de direcciones más grande (resuelve el agotamiento de direcciones IPv4), seguridad mejorada (IPsec a menudo está integrado), formato de cabecera simplificado, mejor soporte para dispositivos móviles.
*   **Representación de Direcciones:**
    *   **Ceros a la Izquierda:** Los ceros a la izquierda dentro de un segmento se pueden omitir (por ejemplo, 0000 se puede escribir como 0).
    *   **Doble Dos Puntos:** Un único doble dos puntos (::) se puede usar para representar uno o más segmentos consecutivos de todos ceros. Esto solo se puede usar una vez en una dirección.
*   **Tipos de Direcciones IPv6:**
    *   **Unicast:** Identifica una única interfaz.
    *   **Multidifusión (Multicast):** Identifica un grupo de interfaces.
    *   **Difusión Cercana (Anycast):** Identifica un conjunto de interfaces, entregándose los paquetes a la interfaz más cercana del conjunto.
*   **Direcciones de Enlace Local (fe80::/10):** Se utilizan para la comunicación dentro de un único enlace de red.
*   **Direcciones Unicast Globales:** Direcciones enrutables globalmente en Internet.

#### c) Subnetting

*   **Propósito:** Dividir una red más grande en subredes más pequeñas y manejables (subnets). Esto ayuda a organizar las redes, mejorar la seguridad y optimizar el rendimiento de la red.
*   **Mecanismo:** El subnetting se logra tomando prestados bits de la porción de host de una dirección IP y usándolos para crear IDs de subred. Esto se hace usando una **máscara de subred**.
*   **Máscara de Subred:** Un número de 32 bits (para IPv4) que identifica las porciones de red y subred de una dirección IP. Tiene una secuencia contigua de 1s para los bits de red y subred, seguida de una secuencia contigua de 0s para los bits de host.
*   **Notación CIDR (Enrutamiento Inter-Dominio sin Clases):** Una forma más flexible de representar prefijos de red usando una barra seguida del número de bits de red (por ejemplo, 192.168.1.0/24 indica que los primeros 24 bits representan la red). Este es el método estándar utilizado hoy en día.
*   **Cálculo de Subnetting (IPv4):**
    1.  Determinar el número de subredes necesarias.
    2.  Determinar el número de hosts necesarios por subred.
    3.  Calcular el número de bits requeridos para las subredes y los hosts.
    4.  Determinar la máscara de subred.
    5.  Identificar las direcciones de subred válidas, las direcciones de broadcast y los rangos de host utilizables para cada subred.
*   **Subnetting en IPv6:** Si bien el concepto de subnetting existe en IPv6, el vasto espacio de direcciones hace que sea menos para conservar direcciones y más para la organización de la red. Las subredes IPv6 son típicamente de un tamaño fijo (/64).

### 3. Algoritmos de Enrutamiento

Los algoritmos de enrutamiento son utilizados por los routers para determinar la mejor ruta para los paquetes de datos. Se pueden clasificar ampliamente en:

#### a) Enrutamiento Estático vs. Dinámico

*   **Enrutamiento Estático:**
    *   Las tablas de enrutamiento se configuran manualmente por el administrador de la red.
    *   Simple de implementar para redes pequeñas y estables.
    *   No se adapta a los cambios o fallos de la red.
    *   Adecuado para escenarios específicos como conectar a una única red remota.
*   **Enrutamiento Dinámico:**
    *   Los routers aprenden automáticamente sobre la topología de la red y actualizan sus tablas de enrutamiento intercambiando información con otros routers.
    *   Más complejo de configurar inicialmente pero muy adaptable a los cambios y fallos de la red.
    *   Escalable para redes más grandes y complejas.

#### b) Enrutamiento por Vector de Distancia

*   **Principio:** Cada router mantiene una tabla de enrutamiento que enumera la mejor distancia conocida (por ejemplo, número de saltos) y la dirección (siguiente router de salto) hacia cada red de destino.
*   **Intercambio de Información:** Los routers intercambian periódicamente sus tablas de enrutamiento completas con sus vecinos directamente conectados.
*   **Ejemplo de Algoritmo:** El **algoritmo Bellman-Ford** es un algoritmo común utilizado en protocolos de enrutamiento por vector de distancia.
*   **Protocolos:** RIP (Protocolo de Información de Enrutamiento) es un ejemplo conocido de un protocolo de enrutamiento por vector de distancia.
*   **Limitaciones:** Puede sufrir de convergencia lenta (toma tiempo para que la red se adapte a los cambios) y el problema de "conteo hasta infinito" (pueden ocurrir bucles de enrutamiento).

#### c) Enrutamiento por Estado de Enlace

*   **Principio:** Cada router mantiene un mapa completo de la topología de la red. Sabe sobre todos los routers y los enlaces entre ellos, junto con el costo de cada enlace.
*   **Intercambio de Información:** Los routers intercambian información sobre el estado de sus enlaces directamente conectados con todos los demás routers de la red. Esta información se llama Anuncio de Estado de Enlace (LSA).
*   **Ejemplo de Algoritmo:** El **algoritmo de Dijkstra** (Primero la Ruta Más Corta - SPF) es utilizado por cada router para calcular la ruta más corta a todos los demás destinos basándose en la información de estado de enlace recopilada.
*   **Protocolos:** OSPF (Primero la Ruta Más Corta Abierta) e IS-IS (Sistema Intermedio a Sistema Intermedio) son protocolos de enrutamiento por estado de enlace populares.
*   **Ventajas:** Convergencia más rápida, menos propenso a bucles de enrutamiento en comparación con el enrutamiento por vector de distancia.

### 4. Protocolos

Varios protocolos clave operan en la Capa de Red:

#### a) IP (Protocolo de Internet)

*   **Protocolo Central:** El protocolo fundamental responsable del direccionamiento y enrutamiento de paquetes a través de las redes.
*   **Sin Conexión y No Fiable:** IP proporciona un servicio sin conexión (sin establecimiento previo de conexión) y es no fiable (sin garantía de entrega). La detección de errores se realiza, pero la recuperación de errores es responsabilidad de los protocolos de capas superiores (como TCP).
*   **Formato de Paquete:** IP define la estructura de los paquetes IP (datagramas), incluyendo las direcciones IP de origen y destino, información de cabecera (por ejemplo, tiempo de vida - TTL) y la carga útil (datos de las capas superiores).

#### b) ICMP (Protocolo de Mensajes de Control de Internet)

*   **Propósito:** Se utiliza para enviar mensajes de error y mensajes de control/información entre dispositivos de red.
*   **Funcionalidad:** Los mensajes ICMP se utilizan para informar errores (por ejemplo, destino inalcanzable, tiempo excedido), solicitar información (por ejemplo, solicitud de eco/respuesta utilizada por el comando `ping`) y realizar otros diagnósticos de red.
*   **Ejemplos:** La utilidad `ping` utiliza solicitudes y respuestas de eco ICMP para probar la conectividad de red. `traceroute` (o `tracert` en Windows) utiliza mensajes ICMP de tiempo excedido para rastrear la ruta de un paquete.

#### c) ARP (Protocolo de Resolución de Direcciones)

*   **Propósito:** Se utiliza para resolver una dirección lógica (dirección IP) a una dirección física (dirección MAC) dentro del mismo segmento de red local.
*   **Proceso:** Cuando un host necesita enviar un paquete a otro host en la misma red, conoce la dirección IP de destino pero necesita la dirección MAC de destino para encuadrar el paquete en la Capa de Enlace de Datos. El host emisor difunde una solicitud ARP que contiene la dirección IP de destino. El host con esa dirección IP responde con una respuesta ARP que contiene su dirección MAC.
*   **Caché ARP:** Los hosts mantienen un caché ARP para almacenar las asignaciones recientemente resueltas de dirección IP a MAC para evitar enviar solicitudes ARP por cada comunicación.

### 5. Dispositivos de Red

La Capa de Red involucra principalmente dos tipos clave de dispositivos de red:

#### a) Routers

*   **Función Principal:** Reenviar paquetes de datos entre diferentes redes basándose en sus direcciones IP de destino.
*   **Características Clave:**
    *   Mantienen tablas de enrutamiento para determinar la mejor ruta para los paquetes.
    *   Conectan diferentes segmentos de red (pueden ser diferentes tecnologías de red).
    *   Realizan el reenvío de paquetes basándose en las decisiones de enrutamiento.
    *   Pueden implementar características de seguridad como firewalls y listas de control de acceso (ACL).

#### b) Gateways

*   **Término más Amplio:** Un gateway es un dispositivo que actúa como punto de entrada a otra red. Puede ser un router, un firewall u otro tipo de dispositivo.
*   **Gateway Predeterminado:** En el contexto de las redes IP, el gateway predeterminado es un router en la red local que un host utiliza para enviar tráfico a destinos fuera de su propia red.
*   **Conversión de Protocolos:** Los gateways también pueden realizar la conversión de protocolos entre diferentes arquitecturas de red o protocolos, aunque esto es menos común para el enrutamiento IP simple.

## Puntos Clave para el Examen de Autoaprendizaje

*   **Comprender las funciones centrales:** Direccionamiento lógico (direcciones IP), enrutamiento (selección de ruta) y reenvío (movimiento de paquetes).
*   **Dominar el direccionamiento IP:** Ser capaz de explicar la estructura de las direcciones IPv4 e IPv6, comprender los conceptos y cálculos de subnetting (especialmente para IPv4) y conocer los diferentes tipos de direcciones IP.
*   **Diferenciar los algoritmos de enrutamiento:** Comprender las diferencias entre el enrutamiento estático y dinámico, y ser capaz de explicar los principios básicos de los algoritmos de enrutamiento por vector de distancia y estado de enlace. Conocer los protocolos comunes asociados con cada uno.
*   **Conocer los protocolos clave de la Capa de Red:** Comprender el propósito y el funcionamiento básico de IP, ICMP y ARP.
*   **Identificar el papel de los dispositivos de red:** Comprender claramente la función de los routers y gateways en la Capa de Red.

## Práctica y Revisión

*   **Trabaja con ejemplos:** Practica cálculos de subnetting para IPv4.
*   **Compara y contrasta:** Crea tablas para comparar diferentes algoritmos de enrutamiento y versiones de direcciones IP.
*   **Relaciona con escenarios del mundo real:** Piensa en cómo se aplican estos conceptos a tu propio uso de Internet y configuraciones de red.
*   **Revisa exámenes anteriores:** Comprende los tipos de preguntas que se suelen hacer sobre este tema en el Examen Chino de Autoaprendizaje.

Al comprender a fondo estos conceptos, construirás una base sólida en la Capa de Red, que es esencial para estudios posteriores en redes informáticas. ¡Buena suerte con tus estudios!