---
audio: false
generated: true
lang: es
layout: post
title: Capa de Transporte
translated: true
type: note
---

A continuación se presenta un tutorial detallado para ayudarte a aprender el capítulo de la **Capa de Transporte** en un curso como *Tecnología de Redes Informáticas (02141)* del sistema chino de Exámenes de Autoeducación Superior (自考). Este tutorial se centra en las funciones de la Capa de Transporte (comunicación extremo a extremo, fiabilidad, control de congestión), los protocolos (TCP y UDP), los números de puerto y la multiplexación, y los mecanismos de control de flujo y de errores. Está diseñado para ser integral, apto para principiantes y alineado con la profundidad técnica esperada en dicho curso.

---

### Paso 1: Comprender la Función de la Capa de Transporte
La **Capa de Transporte** es la cuarta capa en el modelo OSI y la tercera en el modelo TCP/IP. Actúa como un puente entre las capas inferiores (que manejan la transferencia física de datos) y las capas superiores (aplicaciones de usuario). Su función principal es garantizar que los datos lleguen de un dispositivo a otro de manera eficiente y fiable (si es necesario).

- **Por qué es importante:** Sin la Capa de Transporte, aplicaciones como los navegadores web o los clientes de correo electrónico no sabrían cómo enviar o recibir datos correctamente a través de Internet.

---

### Paso 2: Aprender las Funciones de la Capa de Transporte
La Capa de Transporte tiene varias responsabilidades clave. Vamos a desglosarlas:

#### 1. Comunicación Extremo a Extremo
- **Qué significa:** Garantiza que los datos viajen desde el dispositivo de origen hasta el dispositivo de destino, independientemente de las redes intermedias.
- **Cómo funciona:** La Capa de Transporte en el emisor se comunica directamente con la Capa de Transporte en el receptor, ignorando los detalles complejos de los routers y switches (manejados por la Capa de Red).
- **Analogía:** Como enviar una carta directamente a un amigo, sin preocuparse por las oficinas de correos por las que pasa.

#### 2. Fiabilidad
- **Qué significa:** Garantiza que los datos lleguen completos, en orden y sin errores (si lo requiere el protocolo).
- **Cómo funciona:** Algunos protocolos (por ejemplo, TCP) verifican si hay datos perdidos o corruptos y los retransmiten si es necesario. Otros (por ejemplo, UDP) omiten esto para ganar velocidad.
- **Analogía:** Un mensajero que confirma que tu paquete llegó intacto frente a uno que simplemente lo lanza por encima de la valla.

#### 3. Control de Congestión
- **Qué significa:** Evita que la red se sature por un exceso de datos.
- **Cómo funciona:** Ajusta la velocidad de envío de datos en función de las condiciones de la red (por ejemplo, TCP reduce la velocidad si hay tráfico).
- **Analogía:** Como reducir la velocidad de tu coche en un tráfico denso para evitar un embotellamiento.

---

### Paso 3: Explorar los Protocolos de la Capa de Transporte
La Capa de Transporte utiliza dos protocolos principales: **TCP** y **UDP**. Cada uno tiene un enfoque diferente.

#### 1. TCP (Transmission Control Protocol) – Orientado a la Conexión
- **Qué hace:** Garantiza una entrega de datos fiable y ordenada.
- **Características clave:**
  - **Establecimiento de Conexión:** Utiliza un handshake de 3 vías (SYN → SYN-ACK → ACK) para establecer una conexión.
  - **Fiabilidad:** Retransmite paquetes perdidos, garantiza que no haya datos duplicados o fuera de orden.
  - **Control de Flujo:** Ajusta la velocidad de envío para que coincida con la capacidad del receptor.
  - **Control de Congestión:** Reduce la velocidad si la red está ocupada.
- **Ejemplos:** Navegación web (HTTP/HTTPS), correo electrónico (SMTP), transferencia de archivos (FTP).
- **Analogía:** Una llamada telefónica—ambas partes confirman que están listas, hablan en orden y cuelgan correctamente.

#### 2. UDP (User Datagram Protocol) – Sin Conexión
- **Qué hace:** Envía datos rápidamente sin garantías.
- **Características clave:**
  - **Sin Conexión:** Simplemente envía paquetes (datagramas) sin configuración previa.
  - **Sin Fiabilidad:** No verifica si hay datos perdidos o fuera de orden.
  - **Rápido:** Overhead mínimo, ideal para tareas sensibles al tiempo.
- **Ejemplos:** Transmisión de video, juegos online, consultas DNS.
- **Analogía:** Enviar postales—no hay confirmación de que lleguen, pero es rápido y sencillo.

**Tabla Comparativa:**

| **Característica**  | **TCP**               | **UDP**              |
|---------------------|-----------------------|----------------------|
| **Conexión**        | Sí (handshake)        | No                   |
| **Fiabilidad**      | Sí (retransmisiones)  | No                   |
| **Velocidad**       | Más lento (overhead)  | Más rápido (ligero)  |
| **Orden**           | Garantizado           | No garantizado       |
| **Caso de Uso**     | Web, email            | Streaming, gaming    |

---

### Paso 4: Comprender los Números de Puerto y la Multiplexación
La Capa de Transporte utiliza **números de puerto** para gestionar múltiples aplicaciones en el mismo dispositivo.

#### 1. Números de Puerto
- **Qué son:** Números de 16 bits (0–65,535) que identifican aplicaciones o servicios específicos en un dispositivo.
- **Tipos:**
  - **Puertos Bien Conocidos (0–1023):** Reservados para servicios comunes (por ejemplo, 80 para HTTP, 443 para HTTPS, 25 para SMTP).
  - **Puertos Registrados (1024–49151):** Utilizados por aplicaciones específicas.
  - **Puertos Dinámicos (49152–65535):** Temporales, asignados para conexiones del lado del cliente.
- **Analogía:** Como los números de apartamento en un edificio—cada aplicación tiene su propia "dirección".

#### 2. Multiplexación y Demultiplexación
- **Multiplexación (Lado del Emisor):** Combina datos de múltiples aplicaciones en un único flujo para enviar a través de la red. Cada paquete obtiene un número de puerto para identificar su aplicación.
- **Demultiplexación (Lado del Receptor):** Divide los datos entrantes y los entrega a la aplicación correcta basándose en el número de puerto.
- **Cómo funciona:** La Capa de Transporte añade una cabecera con los números de puerto de origen y destino a cada paquete.
- **Ejemplo:** Tu navegador (puerto 50000) y tu cliente de correo (puerto 50001) pueden usar la misma conexión de red simultáneamente.

**Ideas clave:** Las direcciones IP llevan los datos al dispositivo correcto; los números de puerto los llevan a la aplicación correcta en ese dispositivo.

---

### Paso 5: Profundizar en los Mecanismos de Control de Flujo y de Errores
Estos mecanismos garantizan que los datos se muevan de forma fluida y precisa (principalmente en TCP).

#### 1. Control de Flujo
- **Qué significa:** Evita que el emisor sature al receptor.
- **Cómo funciona:**
  - **Ventana Deslizante:** TCP utiliza una "ventana" de datos que el emisor puede enviar antes de necesitar un acuse de recibo (ACK). El receptor anuncia el tamaño de su ventana (cuánto puede manejar).
  - **Se Ajusta Dinámicamente:** Si el búfer del receptor está lleno, la ventana se reduce; si está listo, la ventana crece.
- **Analogía:** Como verter agua en un vaso—reduces la velocidad si está a punto de desbordarse.

#### 2. Control de Errores
- **Qué significa:** Detecta y corrige errores en la transmisión de datos.
- **Cómo funciona:**
  - **Números de Secuencia:** Cada segmento TCP tiene un número para rastrear el orden y detectar datos faltantes.
  - **Acuses de Recibo (ACKs):** El receptor confirma la recepción; la falta de ACKs provoca la retransmisión.
  - **Checksums:** Un valor calculado a partir de los datos para detectar corrupción. Si no coincide, el paquete se retransmite.
- **Analogía:** Como revisar una lista de la compra—los artículos faltantes o dañados se vuelven a pedir.

**Nota sobre UDP:** UDP no realiza control de flujo ni de errores—deja eso para la aplicación si es necesario.

---

### Paso 6: Consejos de Estudio para 自考 (Examen de Autoestudio)
1. **Memoriza Conceptos Clave:**
   - Funciones: Extremo a extremo, fiabilidad, control de congestión.
   - Protocolos: TCP (fiable), UDP (rápido).
   - Puertos: Bien conocidos (por ejemplo, 80, 443), dinámicos.
2. **Visualiza:**
   - Dibuja el handshake de 3 vías de TCP (SYN → SYN-ACK → ACK).
   - Esquematiza la multiplexación: múltiples apps → puertos → un flujo de red.
3. **Preguntas de Práctica:**
   - ¿Cuál es la diferencia entre TCP y UDP?
   - ¿Cómo utiliza la Capa de Transporte los números de puerto?
   - Explica cómo TCP garantiza la fiabilidad.
4. **Usa Nemotecnias:** "TCP = Protocolo de Control Total" (fiable); "UDP = Protocolo Ultra Datagrama" (rápido).
5. **Ejemplos del Mundo Real:** Relaciona con la navegación web (TCP) frente a la transmisión de video (UDP).

---

### Paso 7: Pon a Prueba tu Comprensión
Responde a esto para comprobar tu dominio:
1. ¿Qué protocolo utiliza un handshake de 3 vías? (TCP)
2. ¿Cuál es la función de los números de puerto en la multiplexación? (Identificar aplicaciones)
3. ¿Cómo maneja TCP un paquete perdido? (Lo retransmite usando números de secuencia y ACKs)
4. ¿Por qué se podría preferir UDP sobre TCP? (Velocidad, bajo overhead)

---

### Recursos Adicionales
- **Libros:** "Computer Networking: A Top-Down Approach" (Kurose & Ross) – Capítulo sobre la Capa de Transporte.
- **Online:** Tutoriales de Cisco sobre la Capa de Transporte, YouTube (por ejemplo, "PowerCert" sobre TCP vs. UDP).
- **Herramientas:** Usa Wireshark para capturar paquetes TCP/UDP y ver los números de puerto en acción.

---

Este tutorial cubre la Capa de Transporte en profundidad. Estudia cada sección, practica explicando los conceptos (ideal para la preparación oral de 自考) y revisa las áreas complicadas como el control de flujo o la multiplexación. Si necesitas más ejemplos o aclaraciones, ¡no dudes en preguntar! ¡Buena suerte con tus estudios