---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Estudio de Arquitectura y Modelos de Red
translated: true
type: note
---

Este capítulo sienta las bases para comprender cómo se estructuran las redes de computadoras y cómo se transmiten los datos a través de ellas. En el contexto del curso *Tecnología de Redes de Computadoras* (código de examen 02141 o similar), enfatiza modelos teóricos como OSI y TCP/IP, que son fundamentales para las preguntas del examen sobre capas, protocolos y flujo de datos. Concéntrate en memorizar los nombres de las capas, sus funciones y las correspondencias entre modelos. Espera preguntas de opción múltiple, respuesta corta o basadas en diagramas que evalúen comparaciones y responsabilidades.

## 1. Introducción a las Arquitecturas en Capas
Las redes utilizan **arquitecturas en capas** para simplificar la comunicación compleja dividiendo las tareas en capas modulares. Cada capa:
- Maneja funciones específicas (p. ej., verificación de errores, enrutamiento).
- Interactúa solo con las capas adyacentes a través de interfaces estandarizadas.
- Utiliza **encapsulación** (agregar encabezados y trailers) al enviar datos hacia abajo en la pila y **desencapsulación** al recibir.

**Beneficios**:
- Modularidad: Es fácil desarrollar, probar y actualizar capas individuales.
- Interoperabilidad: Los dispositivos de diferentes fabricantes pueden comunicarse.
- Escalabilidad: Las capas pueden evolucionar de forma independiente (p. ej., nuevos protocolos de transporte).

**Responsabilidades** (generales en todos los modelos):
- **Capas inferiores**: Se centran en el hardware y la transferencia confiable de datos (transmisión física, detección de errores).
- **Capas superiores**: Manejan tareas orientadas al usuario (p. ej., transferencia de archivos, navegación web).
- Los datos fluyen **hacia abajo** en la pila del emisor (encapsulación) y **hacia arriba** en la pila del receptor (desencapsulación).

## 2. Modelo de Referencia OSI
El modelo **Open Systems Interconnection (OSI)** es un marco conceptual de 7 capas desarrollado por ISO en 1984. Es teórico, no se implementa directamente, pero se utiliza como estándar para comprender los protocolos. Nemotecnia: **Please Do Not Throw Sausage Pizza Away** (Física → Aplicación).

| Número de Capa | Nombre de la Capa | Funciones y Protocolos Clave       | PDU (Unidad de Datos de Protocolo) | Dispositivos/Ejemplos |
|----------------|-------------------|------------------------------------|------------------------------------|-----------------------|
| 7              | Aplicación       | Proporciona servicios de red a aplicaciones de usuario (p. ej., correo electrónico, transferencia de archivos). Se interfaza con el software. | Datos | HTTP, FTP, SMTP; Navegador web |
| 6              | Presentación     | Traduce formatos de datos (p. ej., cifrado, compresión, ASCII a EBCDIC). Garantiza la compatibilidad sintáctica. | Datos | JPEG, SSL/TLS |
| 5              | Sesión           | Gestiona sesiones/conexiones (p. ej., establecimiento, sincronización, control de diálogo). Maneja puntos de control para recuperación. | Datos | NetBIOS, RPC |
| 4              | Transporte       | Entrega confiable de extremo a extremo (p. ej., segmentación, control de flujo, recuperación de errores). | Segmento (TCP) / Datagrama (UDP) | TCP, UDP; Puertos (p. ej., 80 para HTTP) |
| 3              | Red              | Direccionamiento lógico y enrutamiento (p. ej., determinación de ruta a través de redes). Maneja la congestión. | Paquete | IP, ICMP, OSPF; Routers |
| 2              | Enlace de Datos  | Entrega de nodo a nodo en la misma red (p. ej., entramado, detección de errores vía CRC, direccionamiento MAC). | Trama | Ethernet, PPP; Switches, NICs |
| 1              | Física           | Transmisión de bits sobre un medio físico (p. ej., señalización, cableado, topología). Se ocupa de especificaciones de hardware. | Bit | RJ-45, Fibra óptica; Hubs, Cables |

**Notas Clave**:
- Capas 1-2: Enfocadas en el medio (LAN/WAN).
- Capas 3-4: De host a host (interconexión de redes).
- Capas 5-7: Orientadas al usuario (soporte de aplicación).
- Consejo para el Examen: Dibuja la pila y etiqueta las PDU/encabezados (p. ej., un segmento TCP tiene encabezado TCP + datos).

## 3. Suite de Protocolos TCP/IP
El **modelo TCP/IP** (o Suite de Protocolos de Internet) es un modelo práctico de 4 capas desarrollado en la década de 1970 para ARPANET (base de Internet). Se implementa en todo el mundo y se corresponde de manera flexible con OSI. Nemotecnia: **LITA** (Enlace → Aplicación).

| Número de Capa | Nombre de la Capa | Funciones y Protocolos Clave       | PDU                  | Dispositivos/Ejemplos |
|----------------|-------------------|------------------------------------|----------------------|-----------------------|
| 4              | Aplicación       | Combina las Capas 5-7 de OSI: Servicios de usuario (p. ej., web, correo electrónico). | Datos/Segmento | HTTP, FTP, DNS; Aplicaciones como navegadores |
| 3              | Transporte       | Extremo a extremo (Capa 4 de OSI): Entrega confiable/no confiable. | Segmento/Datagrama | TCP (confiable, orientado a la conexión), UDP (mejor esfuerzo) |
| 2              | Internet         | Enrutamiento y direccionamiento (Capa 3 de OSI): Rutas lógicas a través de redes. | Paquete | IP (IPv4/IPv6), ICMP; Routers |
| 1              | Enlace (o Acceso a la Red) | Física + Enlace de Datos (Capas 1-2 de OSI): Entrega de hardware en la red local. | Trama/Bit | Ethernet, Wi-Fi; Switches, Cables |

**Notas Clave**:
- No tiene capas de sesión/presentación dedicadas; se manejan dentro de Aplicación.
- TCP/IP es una "familia de protocolos" – p. ej., IP es el núcleo, con TCP/UDP encima.
- Consejo para el Examen: Enfatiza el uso en el mundo real (p. ej., TCP asegura la confiabilidad mediante acuses de recibo, mientras que UDP es ligero para streaming de video).

## 4. Comparación de los Modelos OSI y TCP/IP
Utiliza esta tabla para una revisión rápida. OSI es teórico (referencia), TCP/IP es práctico (implementación).

| Aspecto             | Modelo OSI                           | Modelo TCP/IP                      |
|---------------------|--------------------------------------|------------------------------------|
| **Capas**          | 7 (detallado, conceptual)           | 4 (simplificado, práctico)        |
| **Desarrollo**     | ISO (1984), diseño de arriba hacia abajo | DoD/Internet (década de 1970), de abajo hacia arriba |
| **Enfoque**        | Estándares generales de redes       | Protocolos específicos de Internet |
| **Implementación** | No se implementa directamente; referencia para estándares | Ampliamente utilizado (base de Internet moderna) |
| **Mapeo de Capas** | 1: Física → Enlace<br>2: Enlace de Datos → Enlace<br>3: Red → Internet<br>4: Transporte → Transporte<br>5-6-7: Sesión/Presentación/Aplicación → Aplicación | Aplicación absorbe OSI 5-7; Enlace absorbe 1-2 |
| **Protocolos**     | Teóricos (p. ej., no tiene un IP único) | Específicos (p. ej., IP, TCP, HTTP) |
| **Flujo de PDU**   | Encabezados estrictos por capa      | Flexible (p. ej., el paquete IP incluye datos de transporte) |
| **Fortalezas**     | Integral, fácil de enseñar          | Eficiente, escalable, neutral para el proveedor |
| **Debilidades**    | Excesivamente complejo, no práctico | Menos detallado para las capas superiores |

**Diferencias Clave**:
- **Granularidad**: OSI separa sesión/presentación; TCP/IP las fusiona en Aplicación para simplificar.
- **Direccionamiento**: OSI utiliza puntos de acceso al servicio (SAP); TCP/IP utiliza puertos/direcciones IP.
- **Confiabilidad**: Ambos tienen confiabilidad en el transporte, pero el TCP de TCP/IP es orientado a la conexión como la Capa de Transporte de OSI.
- Consejo para el Examen: Las preguntas a menudo solicitan mapeos (p. ej., "¿Qué capa OSI corresponde a TCP?") o ventajas (p. ej., la adaptabilidad de TCP/IP condujo al crecimiento de Internet).

## 5. Funciones y Responsabilidades de la Arquitectura en Capas
**Principios Fundamentales**:
- **Abstracción**: Cada capa oculta los detalles de las capas inferiores (p. ej., a Transporte no le importan los cables físicos).
- **Primitivas de Servicio**: Las capas proporcionan servicios como CONECTAR, DATOS, DESCONECTAR a las capas superiores.
- **Manejo de Errores**: Las capas inferiores detectan errores; las superiores los recuperan (p. ej., Transporte retransmite paquetes perdidos).
- **Direccionamiento**: Jerárquico – físico (MAC), lógico (IP), de servicio (puertos).

**Ejemplo de Transmisión de Datos**:
1. Datos de aplicación → Transporte agrega encabezado de segmento (puertos, nº de secuencia) → Red agrega encabezado de paquete (direcciones IP) → Enlace agrega encabezado/trailer de trama (MAC) → Física envía bits.
2. Proceso inverso en el receptor.

**Errores Comunes**:
- No confundir las capas: Física son bits/señales; Enlace de Datos son tramas/tramas libres de errores.
- La capa de Enlace de TCP/IP = Capas 1+2 de OSI combinadas.

## Consejos de Estudio para el Examen 自考
- **Memorización**: Usa nemotecnias y dibuja diagramas de capas a diario. Concéntrate en el 80% del peso del examen en descripciones de OSI/TCP/IP.
- **Práctica**:
  - Compara capas en ensayos (200-300 palabras).
  - Preguntas de opción múltiple: "¿Qué capa maneja el enrutamiento? (A) Red".
  - Diagramas: Etiqueta el recorrido de una PDU.
- **Recursos**: Revisa las figuras del libro de texto para la encapsulación. Cronométrate: 30 minutos para la tabla de comparación.
- **Preguntas Comunes**: Explica por qué OSI tiene 7 capas frente a las 4 de TCP/IP; Describe las funciones de la capa de Transporte.

Domina este capítulo para un buen comienzo – se hace referencia a él en temas posteriores como protocolos (p. ej., IP en el Capítulo 3). A continuación, aborda los detalles de la capa física.

**Referencias**:
- [Computer Networking: A Top-Down Approach by Kurose & Ross](https://www.pearson.com/us/higher-education/program/Kurose-Computer-Networking-A-Top-Down-Approach-8th-Edition/PGM1836378.html) (para profundizar en TCP/IP).
- [OSI Model Explained - GeeksforGeeks](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/) (ayudas visuales).