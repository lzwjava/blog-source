---
audio: false
generated: true
lang: es
layout: post
title: 'Introducción a la Raspberry Pi Pico: Un Microcontrolador Versátil'
translated: true
type: note
---

El **Raspberry Pi Pico** es una placa de microcontrolador versátil y de bajo costo desarrollada por la Raspberry Pi Foundation, diseñada para sistemas embebidos, prototipado y proyectos de electrónica DIY. A diferencia de los computadores de placa única (SBC) de Raspberry Pi, como el Raspberry Pi 4, el Pico es un microcontrolador, lo que significa que está optimizado para controlar hardware, ejecutar programas ligeros e interactuar con sensores, motores y otros componentes. Lanzado en enero de 2021, marcó la entrada de la Fundación en el mercado de los microcontroladores, ofreciendo una plataforma asequible pero potente para aficionados, educadores y profesionales.

A continuación se presenta una introducción completa al Raspberry Pi Pico, que cubre sus características, especificaciones, capacidades de programación, aplicaciones y más.

---

### **Descripción General**
El Raspberry Pi Pico está construido alrededor del **RP2040**, un chip microcontrolador diseñado a medida por la Raspberry Pi Foundation. Con un precio de alrededor de $4 USD, compite con plataformas como Arduino y ESP32, pero se destaca por su alto rendimiento, bajo costo y amplio soporte comunitario. El Pico es compacto, mide solo 51mm x 21mm, y está diseñado tanto para principiantes como para usuarios avanzados que trabajan en proyectos que van desde el parpadeo simple de un LED hasta aplicaciones complejas de IoT y robótica.

---

### **Características Principales**
1.  **Microcontrolador RP2040**:
    - Procesador **Arm Cortex-M0+** de doble núcleo que funciona hasta **133 MHz** (overclockeable).
    - **264 KB de SRAM** y **2 MB de memoria flash QSPI integrada** para el almacenamiento de programas.
    - Bajo consumo de energía con modos de sueño e inactivo para aplicaciones alimentadas por batería.
    - Configuración de reloj flexible para optimización del rendimiento.

2.  **Pines GPIO**:
    - 26 pines **GPIO** multifunción.
    - Admite interfaces **I2C**, **SPI**, **UART** y **PWM** para conectar periféricos.
    - 2x UART, 2x controladores SPI, 2x controladores I2C y 16x canales PWM.
    - 3x Convertidores Analógico-Digital (ADC) de 12 bits para entradas de sensores analógicos.
    - 8x bloques de E/S Programables (PIO) para protocolos personalizados (por ejemplo, control de LED WS2812, salida VGA).

3.  **Alimentación y Conectividad**:
    - Alimentado mediante **USB micro-B** (5V) o fuente de alimentación externa (1.8–5.5V).
    - Nivel lógico de **3.3V** para los pines GPIO.
    - **Sensor de temperatura** integrado en el RP2040.
    - Controlador **USB 1.1** para modos dispositivo y host (utilizado para programación y depuración).

4.  **Diseño Físico**:
    - Tamaño compacto: 51mm x 21mm.
    - Diseño de 40 pines estilo DIP con **bordes castelados**, que permite soldarlo directamente a un PCB o usarlo con una protoboard.
    - Colocación de componentes en una sola cara para facilitar el soldado.

5.  **Bajo Costo**:
    - Precio de aproximadamente $4, lo que lo convierte en uno de los microcontroladores más asequibles disponibles.

---

### **Variantes**
Desde su lanzamiento, la Raspberry Pi Foundation y sus socios han lanzado variantes del Pico:
-   **Raspberry Pi Pico W** (2022): Añade **Wi-Fi** (2.4 GHz 802.11n) y **Bluetooth 5.2** mediante un chip Infineon CYW43439, permitiendo aplicaciones inalámbricas de IoT. Precio alrededor de $6.
-   **Raspberry Pi Pico H**: Incluye un conector de 40 pines pre-soldado para un prototipado más fácil.
-   **Raspberry Pi Pico WH**: Combina las capacidades inalámbricas del Pico W con conectores pre-soldados.
-   **Pico 2** (2024): Presenta el microcontrolador **RP2350**, una versión mejorada del RP2040 con núcleos duales **Arm Cortex-M33** o **RISC-V Hazard3** (seleccionable por el usuario), 520 KB de SRAM, eficiencia energética mejorada y características de seguridad mejoradas (por ejemplo, Arm TrustZone, aceleración SHA-256).

---

### **Programando el Raspberry Pi Pico**
El Pico admite múltiples lenguajes y entornos de programación, haciéndolo accesible para una amplia gama de usuarios:

1.  **MicroPython**:
    - La opción más popular para principiantes y prototipado rápido.
    - Firmware oficial de MicroPython proporcionado por la Raspberry Pi Foundation.
    - Admite bibliotecas para GPIO, I2C, SPI, PWM, ADC y PIO.
    - REPL interactivo a través de USB para programación en tiempo real.

2.  **C/C++**:
    - Ofrece control total sobre las características del RP2040 utilizando el **Pico SDK** oficial.
    - Adecuado para aplicaciones críticas en rendimiento y control de hardware de bajo nivel.
    - Admite características avanzadas como programación PIO y procesamiento multi-núcleo.
    - Se utilizan herramientas como CMake y GCC para la compilación.

3.  **Otros Lenguajes**:
    - **CircuitPython**: Una bifurcación de MicroPython por Adafruit, optimizada para la educación y facilidad de uso.
    - **Rust**: Soporte impulsado por la comunidad para programar en Rust en el RP2040.
    - **Arduino**: El Pico se puede programar usando el IDE de Arduino con el paquete oficial de placas RP2040.
    - Soporte experimental para otros lenguajes como JavaScript (vía Espruino) y Lua.

4.  **Herramientas de Desarrollo**:
    - **Programación drag-and-drop**: Cargue archivos de firmware .uf2 de MicroPython o CircuitPython vía USB manteniendo presionado el botón BOOTSEL.
    - **Depuración**: Admite SWD para depuración avanzada con herramientas como la Raspberry Pi Debug Probe.
    - Entornos de desarrollo integrado como **Thonny** (para Python) y **Visual Studio Code** (para C/C++) son comúnmente utilizados.

---

### **Aplicaciones**
La flexibilidad del Raspberry Pi Pico lo hace adecuado para una amplia gama de proyectos, incluyendo:
-   **Prototipado y Educación**: Ideal para aprender sistemas embebidos, programación y electrónica.
-   **Proyectos de IoT**: Con el Pico W, los usuarios pueden crear dispositivos con Wi-Fi como controladores para domótica o estaciones meteorológicas.
-   **Robótica**: Controlar motores, servos y sensores para aplicaciones robóticas.
-   **Interfaces Personalizadas**: Usar PIO para implementar protocolos como control de LED WS2812 (NeoPixel), salida VGA o DVI.
-   **Registro de Datos**: Interfazar con sensores (por ejemplo, temperatura, humedad, luz) para monitoreo ambiental.
-   **Wearables y Sistemas Embebidos**: Su tamaño compacto y bajo consumo de energía lo hacen adecuado para tecnología ponible y dispositivos alimentados por batería.

---

### **Ecosistema y Comunidad**
El Raspberry Pi Pico se beneficia de un ecosistema robusto:
-   **Documentación Oficial**: La Raspberry Pi Foundation proporciona guías detalladas, incluyendo la guía *Pico Getting Started*, la hoja de datos del RP2040 y los archivos de diseño de hardware.
-   **Soporte Comunitario**: Una gran comunidad en plataformas como X, Reddit y los foros de Raspberry Pi comparte proyectos, tutoriales y consejos para resolver problemas.
-   **Accesorios de Terceros**: Hay disponibles numerosos complementos, como placas de breakout para sensores, pantallas y shields de empresas como Adafruit, SparkFun y Pimoroni.
-   **Hardware de Código Abierto**: El diseño del RP2040 está bien documentado, fomentando el desarrollo de placas personalizadas.

---

### **Comparación con Alternativas**
-   **Arduino**: El Pico es más rápido (doble núcleo, 133 MHz vs. 16 MHz del Arduino Uno) y más barato, con más GPIO y características avanzadas como PIO. Sin embargo, Arduino tiene un ecosistema más grande de shields y bibliotecas.
-   **ESP32**: El ESP32 ofrece Wi-Fi y Bluetooth integrados, pero el Pico W iguala esto a un costo menor. El PIO del Pico es único para protocolos personalizados.
-   **STM32**: El Pico es más fácil de programar para principiantes (por ejemplo, con MicroPython) y más asequible que muchas placas STM32.

---

### **Limitaciones**
-   **Sin conectividad inalámbrica integrada (Modelo Base)**: El Pico original carece de Wi-Fi/Bluetooth, aunque el Pico W soluciona esto.
-   **Almacenamiento integrado limitado**: 2 MB de flash son suficientes para la mayoría de proyectos, pero pueden limitar aplicaciones complejas.
-   **Lógica de 3.3V**: Requiere adaptadores de nivel lógico para periféricos de 5V.
-   **Sin botón de reset integrado**: Una inconveniencia menor para algunos usuarios.

---

### **Cómo Empezar**
Para comenzar con el Raspberry Pi Pico:
1.  **Preparación del Hardware**: Conecte el Pico a un computador vía USB o aliméntelo externamente.
2.  **Instalar Firmware**: Descargue el firmware de MicroPython o CircuitPython del sitio web de Raspberry Pi o Adafruit y cárguelo manteniendo presionado BOOTSEL y conectando el Pico.
3.  **Programación**: Use Thonny para Python o configure el Pico SDK para desarrollo en C/C++.
4.  **Proyectos**: Comience con proyectos simples como hacer parpadear un LED o leer un sensor, luego explore aplicaciones avanzadas como IoT o robótica.

---

### **Conclusión**
El Raspberry Pi Pico es un microcontrolador potente, asequible y fácil de usar que ha democratizado el desarrollo de sistemas embebidos. Su chip personalizado RP2040, sus extensas capacidades GPIO y su soporte para múltiples lenguajes de programación lo convierten en una opción ideal para aficionados, educadores y profesionales. Con variantes como el Pico W y el Pico 2, continúa evolucionando, ofreciendo conectividad inalámbrica y rendimiento mejorado para aplicaciones modernas. Respaldado por la excelente documentación de la Raspberry Pi Foundation y una comunidad vibrante, el Pico es una plataforma ideal para aprender, prototipar y construir proyectos innovadores.

Si deseas detalles específicos sobre cómo programar el Pico, ideas de proyectos o comparaciones con otros microcontroladores, ¡házmelo saber