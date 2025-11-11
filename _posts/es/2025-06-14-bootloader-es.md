---
audio: false
generated: true
lang: es
layout: post
title: Quemar un Bootloader
translated: true
type: note
---

Quemar un bootloader en un Arduino Uno R3 es necesario si el microcontrolador (ATmega328P) está en blanco, corrupto o necesita ser reemplazado. Este proceso programa el chip con el firmware requerido para comunicarse con el Arduino IDE y ejecutar sketches. A continuación se presenta una guía paso a paso para quemar el bootloader usando métodos comunes.

---

### **Requisitos**
- **Arduino Uno R3** (la placa objetivo con el ATmega328P a programar).
- **Programador**: Uno de los siguientes:
  - Otra placa Arduino funcional (ej. otro Uno R3) como "Arduino as ISP".
  - Un programador dedicado como **USBasp**, **AVRISP mkII**, o **Atmel-ICE**.
- **Arduino IDE** (descargar de [arduino.cc](https://www.arduino.cc/en/software)).
- **Cables jumper** (si se usa Arduino como ISP).
- **Cable USB** (para conectar el programador o Arduino a tu computadora).

---

### **Método 1: Usando Otro Arduino (Arduino como ISP)**

Este método utiliza una segunda placa Arduino (ej. otro Uno R3) como un Programador en Sistema (ISP) para quemar el bootloader.

#### **Pasos**
1. **Preparar el Arduino Programador**:
   - Conecta el segundo Arduino (el programador) a tu computadora via USB.
   - Abre el Arduino IDE, ve a **Archivo > Ejemplos > 11.ArduinoISP > ArduinoISP**, y sube este sketch al Arduino programador. Esto lo convierte en un ISP.

2. **Conectar las Placas**:
   - Cablea el Arduino programador al Arduino Uno R3 objetivo (el que necesita el bootloader) de la siguiente manera:
     - **Arduino Programador** → **Arduino Uno R3 Objetivo**:
       - 5V → 5V
       - GND → GND
       - Pin 10 → Reset
       - Pin 11 → Pin 11 (MOSI)
       - Pin 12 → Pin 12 (MISO)
       - Pin 13 → Pin 13 (SCK)
   - Alternativamente, si el Uno R3 objetivo tiene un **conector ICSP**, conecta los pines ICSP correspondientes (MOSI, MISO, SCK, VCC, GND, Reset) directamente usando cables jumper.

3. **Configurar el Arduino IDE**:
   - En el Arduino IDE, ve a **Herramientas > Placa** y selecciona **Arduino Uno** (para el Uno R3 objetivo).
   - Ve a **Herramientas > Programador** y selecciona **Arduino as ISP**.
   - Asegúrate de que el puerto correcto para el Arduino programador esté seleccionado en **Herramientas > Puerto**.

4. **Quemar el Bootloader**:
   - Ve a **Herramientas > Quemar Bootloader**.
   - El IDE usará el Arduino programador para flashear el bootloader en el ATmega328P del Uno R3 objetivo. Esto puede tomar un minuto.
   - Si es exitoso, verás un mensaje "Done burning bootloader". Si hay un error, verifica las conexiones y asegúrate de que el Arduino programador esté ejecutando el sketch ArduinoISP.

5. **Probar la Placa Objetivo**:
   - Desconecta el Arduino programador y los cables.
   - Conecta el Uno R3 objetivo a tu computadora via USB.
   - Sube un sketch simple (ej., Blink de **Archivo > Ejemplos > 01.Basics > Blink**) para confirmar que el bootloader funciona.

---

### **Método 2: Usando un Programador ISP Dedicado (ej., USBasp)**

Si tienes un programador dedicado como USBasp, el proceso es más simple y a menudo más confiable.

#### **Pasos**
1. **Conectar el Programador**:
   - Conecta el USBasp (o programador similar) a tu computadora via USB.
   - Conecta el programador al **conector ICSP** del Arduino Uno R3 objetivo usando un cable ICSP de 6 pines. Asegura la orientación correcta (el pin 1 está marcado con un punto o muesca en el conector ICSP).

2. **Configurar el Arduino IDE**:
   - Abre el Arduino IDE.
   - Ve a **Herramientas > Placa** y selecciona **Arduino Uno**.
   - Ve a **Herramientas > Programador** y selecciona tu programador (ej., **USBasp** o **AVRISP mkII**).
   - Selecciona el puerto correcto en **Herramientas > Puerto** (si es aplicable, algunos programadores no requieren selección de puerto).

3. **Quemar el Bootloader**:
   - Ve a **Herramientas > Quemar Bootloader**.
   - El IDE usará el programador para flashear el bootloader. Esto toma unos 10-30 segundos.
   - Un mensaje "Done burning bootloader" indica éxito. Si falla, revisa las conexiones y asegúrate de que el programador sea reconocido por tu computadora.

4. **Probar la Placa**:
   - Desconecta el programador.
   - Conecta el Uno R3 a tu computadora via USB y sube un sketch de prueba (ej., Blink) para verificar la funcionalidad.

---

### **Consejos para Solución de Problemas**
- **Mensajes de Error**: Si recibes errores como “avrdude: stk500_getsync()” o “not in sync,” verifica:
  - Todas las conexiones (cables o cable ICSP).
  - Que el Arduino programador esté ejecutando el sketch ArduinoISP (Método 1).
  - Que el programador correcto esté seleccionado en el IDE.
- **Problemas de Controladores**: Para USBasp u otros programadores, asegúrate de que los controladores estén instalados (ej., Zadig para USBasp en Windows).
- **Microcontrolador en Blanco**: Si el ATmega328P es nuevo o está en blanco, puede necesitar un cristal externo de 16 MHz y dos capacitores de 22pF conectados a los pines 9 y 10 (XTAL1/XTAL2) si no están ya presentes en la placa Uno R3.
- **Fuente de Alimentación**: Asegúrate de que la placa objetivo esté alimentada (via USB o VIN) durante la programación.

---

### **Notas Adicionales**
- **¿Por Qué Quemar un Bootloader?**: El bootloader permite al Arduino Uno R3 comunicarse con el Arduino IDE via USB para subir sketches. Sin él, la placa no responderá a las subidas por USB.
- **Tipo de Bootloader**: El Uno R3 usa el **bootloader Optiboot**, que es compacto y soporta subidas más rápidas comparado con bootloaders más antiguos.
- **Reemplazar el Microcontrolador**: Si estás reemplazando el ATmega328P, asegúrate de que sea un ATmega328P-PU (paquete DIP) para el zócalo del Uno R3. Las versiones SMD requieren soldadura avanzada.
- **Herramientas Alternativas**: También puedes usar **AVRDUDE** o **PlatformIO** para quemar el bootloader, pero el Arduino IDE es el más fácil para principiantes.

Si necesitas aclaración en cualquier paso o ayuda con un programador específico, ¡avísame!