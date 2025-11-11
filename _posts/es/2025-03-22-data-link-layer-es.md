---
audio: false
generated: true
lang: es
layout: post
title: Capa de Enlace de Datos
translated: true
type: note
---

Aquí tienes un tutorial detallado para ayudarte a aprender el capítulo de la **Capa de Enlace de Datos** en el curso de **Tecnología de Redes de Computadoras** (02141 en el sistema chino de Exámenes de Autoestudio).

---

## **1. Visión General de la Capa de Enlace de Datos**
La Capa de Enlace de Datos es la **segunda capa** en el **modelo OSI**, responsable de proporcionar una **transferencia de datos fiable** entre nodos directamente conectados. Se asegura de que las tramas (paquetes de datos en esta capa) tengan el formato correcto, se transmitan y se reciban adecuadamente.

### **Responsabilidades Clave:**
- **Encapsulado (Framing)** – Encapsula los datos en tramas para su transmisión.
- **Detección y Corrección de Errores** – Identifica y corrige errores de transmisión.
- **Control de Flujo** – Asegura que el emisor no sature al receptor.
- **Control de Acceso al Medio (MAC)** – Determina cómo múltiples dispositivos comparten el medio de transmisión.
- **Técnicas de Conmutación (Switching)** – Gestiona cómo se mueven los datos a través de las redes.

---

## **2. Encapsulado (Framing)**
El encapsulado consiste en dividir un flujo continuo de datos en unidades más pequeñas, llamadas **tramas**, que incluyen información de sincronización.

### **Tipos de Métodos de Encapsulado:**
1. **Método de Recuento de Caracteres** – El primer campo de la trama especifica el número de caracteres.
2. **Encapsulado Basado en Banderas (Bit Stuffing)** – Utiliza bits de bandera especiales (ej., `01111110` en HDLC) para marcar el inicio y el final.
3. **Encapsulado Basado en Caracteres (Byte Stuffing)** – Utiliza secuencias de escape para diferenciar los caracteres de control de los datos.

---

## **3. Detección y Corrección de Errores**
El manejo de errores garantiza que la transmisión de datos sea precisa.

### **Técnicas de Detección de Errores:**
- **Bits de Paridad** – Un método simple que añade un bit extra para la detección de errores.
- **Comprobación de Redundancia Cíclica (CRC)** – Utiliza división polinómica para detectar errores.
- **Checksum (Suma de Comprobación)** – Un valor matemático calculado a partir de los datos para verificar su precisión.

### **Técnicas de Corrección de Errores:**
- **Corrección Directa de Errores (FEC)** – Utiliza datos redundantes para corregir errores sin retransmisión.
- **Petición Automática de Repetición (ARQ)** – Utiliza acuses de recibo y retransmisiones.
  - **ARQ Parada-y-Espera (Stop-and-Wait)** – Espera un acuse de recibo antes de enviar la siguiente trama.
  - **ARQ Ir-Regreso-N (Go-Back-N)** – Envía múltiples tramas pero retransmite desde el primer error.
  - **ARQ Repetición Selectiva (Selective Repeat)** – Retransmite solo las tramas erróneas.

---

## **4. Control de Flujo**
El control de flujo evita que el emisor sature al receptor.

### **Métodos de Control de Flujo:**
- **Parada-y-Espera (Stop-and-Wait)** – El emisor espera un acuse de recibo antes de enviar la siguiente trama.
- **Protocolo de Ventana Deslizante (Sliding Window)** – El emisor puede enviar múltiples tramas antes de necesitar un acuse de recibo.

---

## **5. Protocolos de la Capa de Enlace de Datos**

### **5.1 Ethernet (IEEE 802.3)**
**Ethernet** es una tecnología LAN ampliamente utilizada basada en el **estándar IEEE 802.3**.

#### **Estructura de la Trama Ethernet:**

| Campo | Descripción |
|--------|------------|
| Preámbulo | Sincronización |
| Dirección de Destino | Dirección MAC del receptor |
| Dirección de Origen | Dirección MAC del emisor |
| Tipo/Longitud | Identifica el tipo de protocolo (IPv4, IPv6, etc.) |
| Datos | Carga útil real |
| CRC | Valor de comprobación de errores |

#### **Modos de Transmisión Ethernet:**
- **Semidúplex (Half-duplex)** – Los dispositivos transmiten datos por turnos.
- **Dúplex Completo (Full-duplex)** – Los dispositivos pueden enviar y recibir datos simultáneamente.

---

### **5.2 Protocolo Punto a Punto (PPP)**
PPP se utiliza en **conexiones de acceso telefónico y banda ancha**.

#### **Características de PPP:**
- **Soporta autenticación** (ej., PAP, CHAP).
- **Soporte multiprotocolo** (ej., IPv4, IPv6).
- **Detección de errores** mediante CRC.

#### **Estructura de la Trama PPP:**

| Campo | Descripción |
|--------|------------|
| Bandera (Flag) | Marca el inicio y el final de la trama |
| Dirección (Address) | Normalmente `0xFF` (Difusión) |
| Control (Control) | Normalmente `0x03` (Información no numerada) |
| Protocolo (Protocol) | Indica el protocolo utilizado (IPv4, IPv6, etc.) |
| Datos (Data) | Carga útil de datos real |
| CRC | Comprobación de errores |

---

## **6. Métodos de Control de Acceso al Medio (MAC)**

### **6.1 Acceso Múltiple por Detección de Portadora con Detección de Colisiones (CSMA/CD)**
- Utilizado en **redes Ethernet cableadas**.
- Los dispositivos comprueban si el medio está libre antes de transmitir.
- **Si ocurre una colisión**, los dispositivos dejan de transmitir y lo intentan de nuevo después de un retardo aleatorio.

### **6.2 Acceso Múltiple por Detección de Portadora con Evitación de Colisiones (CSMA/CA)**
- Utilizado en **redes inalámbricas (Wi-Fi)**.
- Los dispositivos intentan evitar colisiones esperando antes de enviar datos.
- Utiliza mecanismos de **Petición para Enviar (RTS) y Listo para Enviar (CTS)**.

---

## **7. Técnicas de Conmutación (Switching)**
La conmutación determina cómo se reenvían los datos en una red.

### **7.1 Conmutación de Circuito (Circuit Switching)**
- Se establece una ruta de comunicación **dedicada** (ej., redes telefónicas).
- **Ventajas**: Transferencia de datos fiable y continua.
- **Desventajas**: Ineficiente para transferencia de datos intermitente.

### **7.2 Conmutación de Paquetes (Packet Switching)**
- Los datos se **dividen en paquetes** y se envían de forma independiente.
- Se utiliza en **redes IP** (ej., Internet).
- **Ventajas**: Eficiente, soporta múltiples usuarios.
- **Desventajas**: Los paquetes pueden llegar desordenados.

### **7.3 Conmutación de Mensajes (Message Switching)**
- Los mensajes completos se almacenan y reenvían.
- **Ventaja**: No necesita una conexión dedicada.
- **Desventaja**: Más lento que la conmutación de paquetes.

---

## **8. Introducción a las Tecnologías LAN**
Las tecnologías LAN (Red de Área Local) definen cómo se comunican los dispositivos en una red local.

### **Tipos de Tecnologías LAN:**
1. **Ethernet (IEEE 802.3)** – Utiliza CSMA/CD, soporta velocidades desde 10 Mbps hasta 100 Gbps.
2. **Wi-Fi (IEEE 802.11)** – Utiliza CSMA/CA, transmisión inalámbrica.
3. **Token Ring (IEEE 802.5)** – Utiliza un método de paso de testigo (token) para controlar el acceso.
4. **FDDI (Fiber Distributed Data Interface)** – Utiliza cables de fibra óptica para redes de alta velocidad.

---

## **9. Resumen**
- La **Capa de Enlace de Datos** asegura una **transmisión fiable** entre dispositivos directamente conectados.
- El **Encapsulado (Framing)** organiza los datos en unidades manejables.
- La **Detección y Corrección de Errores** mantiene la integridad de los datos.
- El **Control de Flujo** previene la sobrecarga de datos.
- **Ethernet y PPP** son los principales protocolos de la Capa de Enlace de Datos.
- **CSMA/CD y CSMA/CA** manejan el acceso al medio.
- Las **Técnicas de Conmutación** determinan los métodos de reenvío de datos.
- Las **Tecnologías LAN** incluyen Ethernet, Wi-Fi, Token Ring y FDDI.

---

## **10. Preguntas de Práctica**
1. ¿Cuál es la función principal de la Capa de Enlace de Datos en el modelo OSI?
2. Compara CSMA/CD y CSMA/CA.
3. Explica la diferencia entre conmutación de circuito y conmutación de paquetes.
4. ¿Cuáles son las diferencias clave entre Ethernet y PPP?
5. ¿Cómo funciona la detección de errores utilizando CRC?

---

Este tutorial proporciona una base sólida para dominar la **Capa de Enlace de Datos** en tu curso de **Tecnología de Redes de Computadoras (02141)**. Si necesitas más explicaciones, preguntas de práctica o ejemplos del mundo real, ¡no dudes en preguntar! 🚀