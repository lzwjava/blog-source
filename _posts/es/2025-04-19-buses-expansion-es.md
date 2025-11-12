---
audio: false
generated: true
lang: es
layout: post
title: 'Parte 5: Autobuses y Expansión'
translated: true
type: note
---

### 1. Estándares del Bus del Sistema

#### ¿Qué es un Bus del Sistema?

Un bus del sistema es una ruta de comunicación que conecta la CPU con la memoria y los dispositivos periféricos. Facilita la transferencia de datos, la señalización de direcciones y las señales de control entre estos componentes, permitiendo que la CPU interactúe eficientemente con otras partes del sistema informático[^3].

---

### 2. Descripción General del Bus ISA

- **ISA (Industry Standard Architecture)** es uno de los estándares de bus del sistema más antiguos, introducido con la IBM PC AT en la década de 1980.
- Es un bus de 16 bits que funciona a 4.77 MHz, capaz de alcanzar velocidades de transferencia de datos de aproximadamente 9 MB/s[^5].
- ISA admite múltiples tarjetas de expansión, cada una con su propia línea de petición de interrupción, permitiendo conectar dispositivos como tarjetas de red, puertos serie y tarjetas de video.
- El bus es compatible con versiones anteriores de sistemas PC XT de 8 bits y utiliza un conector de 98 pines que combina dos conectores de borde en una sola ranura.
- ISA utiliza señalización asíncrona y bus mastering, pero solo accede directamente a los primeros 16 MB de la memoria principal[^5].
- Debido a su antigüedad, ISA está prácticamente obsoleto, pero es históricamente importante como base para diseños de bus posteriores.

---

### 3. Descripción General del Bus PCI

- **PCI (Peripheral Component Interconnect)** es un estándar de bus paralelo y síncrono más moderno, diseñado para superar las limitaciones de ISA[^1][^3].
- Los buses PCI funcionan a 33 MHz con un bus de direcciones/datos multiplexado de 32 bits, ofreciendo un ancho de banda base de 44 a 66 MB/s.
- Para accesos secuenciales a memoria, PCI puede alcanzar hasta 132 MB/s transfiriendo una palabra de 32 bits por ciclo de reloj sin necesidad de reenviar direcciones[^1].
- PCI utiliza una interfaz puente para conectarse al bus de la CPU, que almacena en búfer los datos y optimiza el acceso a la memoria, permitiendo que la CPU continúe su ejecución sin estados de espera durante la comunicación con periféricos[^1].
- PCI admite bus mastering y DMA (Acceso Directo a Memoria), donde los dispositivos pueden tomar el control del bus para transferir datos directamente.
- Existe una extensión de 64 bits de PCI para aumentar aún más el ancho de banda.
- Los dispositivos PCI se identifican por número de bus, número de dispositivo y función, con registros de configuración que especifican el fabricante, el tipo de dispositivo, las direcciones de memoria y E/S, y las interrupciones[^3].
- Las transacciones PCI incluyen fases de dirección y fases de datos, y admiten varios comandos como lectura/escritura de memoria y lectura/escritura de E/S[^3].

---

### 4. Tecnologías de Interfaz Modernas

La comunicación con periféricos moderna ha migrado hacia interfaces serie que son más simples y flexibles que los buses paralelos.

---

#### USB (Universal Serial Bus)

- USB es una interfaz serie de alta velocidad ampliamente utilizada, diseñada para conectar periféricos como teclados, ratones, dispositivos de almacenamiento y más.
- Admite plug-and-play y hot-swapping, permitiendo conectar y desconectar dispositivos sin apagar el equipo.
- USB utiliza una topología de estrella escalonada y admite velocidades de datos desde 1.5 Mbps (Baja Velocidad) hasta 10 Gbps (USB 3.1 y superiores).
- Proporciona energía a los dispositivos y admite múltiples clases de dispositivos con protocolos estandarizados.
- Los controladores USB gestionan las transferencias de datos utilizando endpoints y pipes, con diferentes tipos de transferencia como control, bulk, interrupción e isócronas.

---

#### SPI (Serial Peripheral Interface)

- SPI es un bus de comunicación serie síncrono comúnmente utilizado para comunicación a corta distancia con dispositivos periféricos como sensores, EEPROMs y pantallas[^4].
- Utiliza cuatro señales: SCLK (reloj), MOSI (Salida del Maestro, Entrada del Esclavo), MISO (Entrada del Maestro, Salida del Esclavo) y CS (Selección de Chip).
- SPI es full-duplex, permitiendo la transmisión y recepción de datos simultáneamente.
- Es simple y rápido, pero requiere una línea de selección de chip por dispositivo, lo que puede limitar la escalabilidad.
- La configuración del modo SPI incluye la polaridad y fase del reloj, que definen cuándo se muestrea y se desplazan los datos[^6].
- SPI se utiliza típicamente en sistemas embebidos y aplicaciones con microcontroladores.

---

#### I²C (Inter-Integrated Circuit)

- I²C es un bus serie de dos hilos utilizado para la comunicación entre microcontroladores y periféricos como sensores y EEPROMs[^4].
- Utiliza dos líneas bidireccionales: SDA (datos) y SCL (reloj).
- I²C admite múltiples maestros y esclavos en el mismo bus, con dispositivos direccionados por direcciones únicas de 7 o 10 bits.
- Admite comunicación half-duplex y utiliza salidas de drenador abierto/colector abierto con resistencias pull-up.
- I²C es más lento que SPI pero requiere menos pines y admite comunicación multi-dispositivo con un cableado simple.
- Las velocidades típicas son 100 kHz (Modo Estándar), 400 kHz (Modo Rápido) y superiores en especificaciones más nuevas.

---

### Tabla Resumen: ISA vs PCI vs USB vs SPI vs I²C

| Característica | ISA | PCI | USB | SPI | I²C |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Tipo de Bus | Paralelo, asíncrono | Paralelo, síncrono | Serie, asíncrono | Serie, síncrono | Serie, síncrono |
| Ancho de Datos | 8 o 16 bits | 32 o 64 bits multiplexados | Serie (1 bit) | 1 bit por línea, full duplex | 1 bit por línea, half duplex |
| Velocidad de Reloj | 4.77 MHz | 33 MHz (PCI base) | Hasta 10 Gbps (USB 3.1) | Típicamente hasta varios MHz | Típicamente hasta 400 kHz+ |
| Ancho de Banda Máximo | ~9 MB/s | 44-132 MB/s | Varía según versión USB | Depende de la velocidad del reloj | Menor que SPI |
| Número de Cables | Muchos (dirección, datos, control) | Muchos (líneas multiplexadas) | 4 (alimentación, tierra, D+, D-) | 4 (SCLK, MOSI, MISO, CS) | 2 (SDA, SCL) |
| Direccionamiento de Dispositivos | Basado en ranura | Número de bus/dispositivo/función | Enumeración de dispositivos | Selección de chip por dispositivo | Dispositivos direccionados |
| Casos de Uso Típicos | Tarjetas de expansión legacy | Tarjetas de expansión modernas | Periféricos externos | Periféricos embebidos | Periféricos embebidos |
| Bus Mastering | Sí | Sí | Gestionado por controlador host | Maestro/esclavo | Multi-maestro admitido |

---

### Notas Prácticas sobre el Uso de SPI e I²C

- En plataformas como Raspberry Pi, las interfaces SPI e I²C no están habilitadas por defecto y requieren configuración a través de los ajustes del sistema (ej., `raspi-config`)[^4].
- Bibliotecas como `wiringPi`, `spidev` (para SPI) y `smbus` (para I²C) proporcionan interfaces de programación en C/C++ y Python para comunicarse con dispositivos en estos buses.
- La configuración de SPI implica establecer el modo (polaridad y fase del reloj), el orden de los bits (MSB o LSB primero) y seleccionar el pin de selección de chip correcto[^6].
- La comunicación I²C implica especificar direcciones de dispositivo y manejar las condiciones de inicio/parada para la transferencia de datos.

---

Este tutorial describe los conceptos fundamentales y los aspectos prácticos de los buses del sistema y las interfaces periféricas modernas, proporcionando una base sólida para comprender las arquitecturas de bus de microcomputadoras y las tecnologías de expansión.

<div style="text-align: center">⁂</div>

[^1]: https://people.ece.ubc.ca/~edc/464/lectures/lec17.pdf

[^2]: https://spotpear.com/wiki/USB-TO-UART-I2C-SPI-JTAG-Wiki.html

[^3]: https://home.mit.bme.hu/~rtamas/rendszerarchitekturak/eloadas/08_bus_introduction.pdf

[^4]: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

[^5]: https://www.techtarget.com/searchwindowsserver/definition/ISA-Industry-Standard-Architecture

[^6]: https://www.ratocsystems.com/english/download/pdffiles/usb61_e_10.pdf

[^7]: https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/files/PCI.pdf

[^8]: https://www.infineon.com/dgdl/Infineon-USB-Serial_VCP_I2CSPI_API_Guide-Software-v01_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f6a8b015fe6\&da=t

[^9]: https://network.nvidia.com/pdf/whitepapers/PCI_3GIO_IB_WP_120.pdf

[^10]: https://people.scs.carleton.ca/~sivarama/org_book/org_book_web/slides/chap_1_versions/ch5_1.pdf

[^11]: https://www.youtube.com/watch?v=BBobCtfOjbM

[^12]: https://www.sciencedirect.com/topics/engineering/peripheral-component-interconnect-bus

[^13]: http://mcatutorials.com/mca-tutorials-bus-standards-and-types.php

[^14]: https://www.youtube.com/watch?v=YRJ9gWaxfJY

[^15]: https://docs.nxp.com/bundle/UM12018/page/topics/connecting_to_a_target_through_a_usb-to-spi_or_usb.html

[^16]: https://www.i2ctools.com/Downloads/USBtoI2Cpro/USB-to-SPI_Software_Users_Manual.pdf

[^17]: https://www.youtube.com/watch?v=WIIR77fCHYc

[^18]: https://ftdichip.com/wp-content/uploads/2021/08/AN_255_USB-to-I2C-Example-using-the-FT232H-and-FT201X-devices.pdf

[^19]: https://www.youtube.com/watch?v=IyGwvGzrqp8