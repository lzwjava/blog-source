---
audio: false
generated: true
lang: es
layout: post
title: Raspberry Pi frente a Arduino para la monitorización de lavadoras con alertas
  de Telegram
translated: true
type: note
---

Utilizar una Raspberry Pi en lugar de un Arduino (como el ESP32-CAM) para detectar cuándo tu lavadora Maytag MHW8630HW se detiene y enviar una notificación por Telegram es una alternativa viable, que ofrece más potencia de procesamiento y flexibilidad a costa de una mayor complejidad y consumo de energía. A continuación, compararé el enfoque de Raspberry Pi con la solución Arduino, describiré otras opciones de microcontroladores y proporcionaré una guía detallada para implementar el sistema con una Raspberry Pi. También discutiré enfoques alternativos (por ejemplo, otro hardware o sensores) para garantizar una respuesta integral.

---

### Comparación: Raspberry Pi vs. Arduino vs. Otras Opciones

| **Característica**         | **Raspberry Pi**                                                                 | **Arduino (ESP32-CAM)**                                                  | **Otras Opciones (ej., NodeMCU, ESP8266)**                              |
|----------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Potencia de Procesamiento** | Alta (CPU quad-core, 1-8GB RAM) – Soporta procesamiento de imagen avanzado, OpenCV. | Limitada (dual-core, 520KB SRAM) – Solo procesamiento de imagen básico. | Muy limitada – No es adecuada para procesamiento basado en cámara.       |
| **Soporte de Cámara**      | Fácil con cámaras web USB o Pi Camera Module (ej., Pi Camera v2 de 8MP).        | Cámara integrada OV2640 (2MP), pero menor resolución y calidad.          | Requiere módulo de cámara externo, complejo de integrar.                |
| **Wi-Fi**                  | Integrado (en la mayoría de modelos, ej., Pi 4, Zero 2 W).                      | Integrado (ESP32-CAM).                                                 | Integrado (ej., ESP8266), pero sin soporte nativo para cámara.          |
| **Programación**           | Python, OpenCV, versátil pero requiere configuración del SO (Raspberry Pi OS).  | C++ en Arduino IDE, más simple para principiantes.                      | C++ o Lua (ej., NodeMCU), librerías limitadas para procesamiento de imagen. |
| **Consumo de Energía**     | Mayor (~2.5W para Pi Zero, ~5-10W para Pi 4).                                   | Menor (~1-2W para ESP32-CAM).                                          | Más bajo (~0.5-1W para ESP8266).                                       |
| **Costo**                  | $10 (Pi Zero W) a $35+ (Pi 4) + $15 para Pi Camera.                            | ~$10 (ESP32-CAM con cámara).                                           | ~$5-10 (ESP8266/NodeMCU) + costos de sensores.                          |
| **Facilidad de Configuración** | Moderada (configuración del SO, codificación en Python).                        | Fácil (Arduino IDE, un solo sketch).                                    | Fácil para sensores simples, complejo para cámaras.                     |
| **Mejor Caso de Uso**      | Procesamiento de imagen avanzado, flexible para expansiones futuras (ej., modelos de ML). | Detección de luz simple y de bajo costo con integración en Telegram.    | Soluciones sin cámara (ej., sensores de vibración o de corriente).      |

**Ventajas de Raspberry Pi**:
- Procesamiento de imagen superior con OpenCV para una detección de luz robusta.
- Más fácil de depurar y expandir (ej., añadir una interfaz web o múltiples sensores).
- Soporta cámaras de mayor calidad para una mejor precisión en distintas condiciones de luz.

**Desventajas de Raspberry Pi**:
- Requiere más configuración (instalación del SO, entorno Python).
- Mayor consumo de energía, menos ideal para configuraciones con batería.
- Más costosa que el ESP32-CAM.

**Otras Opciones**:
- **NodeMCU/ESP8266**: Adecuado para soluciones sin cámara (ej., usar un sensor de vibración o de corriente). Su potencia de procesamiento limitada hace que la integración de cámara sea impracticable.
- **Sensor de Vibración**: Detecta las vibraciones de la máquina en lugar de la luz del panel. Simple pero puede pasar por alto cambios sutiles en el ciclo.
- **Sensor de Corriente**: Mide el consumo de energía (ej., módulo ACS712) para detectar cuándo se detiene la máquina. No invasivo pero requiere configuración eléctrica.

---

### Guía de Implementación con Raspberry Pi

#### Stack Tecnológico
**Hardware**:
1. **Raspberry Pi**:
   - **Raspberry Pi Zero 2 W** ($15, compacta, con Wi-Fi) o **Raspberry Pi 4** ($35+, más potente).
2. **Cámara**:
   - **Raspberry Pi Camera Module v2** ($15, 8MP) o una cámara web USB.
3. **Fuente de Alimentación**:
   - 5V USB-C (Pi 4) o micro-USB (Pi Zero) con salida de 2-3A.
4. **Montaje**:
   - Carcasa o soporte adhesivo para posicionar la cámara frente a la luz del panel de la lavadora.

**Software**:
1. **SO**: Raspberry Pi OS (Lite para eficiencia, Full para configuración más fácil).
2. **Lenguaje de Programación**: Python.
3. **Librerías**:
   - **OpenCV**: Para el procesamiento de imagen y detectar la luz del panel.
   - **python-telegram-bot**: Para las notificaciones de Telegram.
   - **picamera2** (para Pi Camera) o **fswebcam** (para cámara web USB).
4. **Bot de Telegram**: La misma configuración que para Arduino (usar BotFather para el token del bot y el ID del chat).

#### Algoritmo
El algoritmo es similar al enfoque de Arduino pero aprovecha OpenCV para un procesamiento de imagen más robusto:
1. **Captura de Imagen**: Usar la Pi Camera o la cámara web para capturar imágenes periódicamente (ej., cada 10 segundos).
2. **Región de Interés (ROI)**: Definir un rectángulo alrededor de la luz del panel en la imagen.
3. **Procesamiento de Imagen**:
   - Convertir a escala de grises.
   - Aplicar desenfoque gaussiano para reducir el ruido.
   - Usar umbralización adaptativa para detectar la luz brillante del panel contra el fondo.
   - Calcular la intensidad promedio de píxeles en la ROI o contar píxeles brillantes.
4. **Máquina de Estados**:
   - Si la ROI está brillante (luz ENCENDIDA), marcar la máquina como en funcionamiento.
   - Si la ROI está oscura (luz APAGADA) durante 5 minutos, marcar la máquina como detenida y enviar una notificación por Telegram.
5. **Eliminación de Rebotes**: Implementar un retraso de 5 minutos para confirmar que la máquina se ha detenido.

#### Pasos de Implementación
1. **Configurar la Raspberry Pi**:
   - Descargar y flashear **Raspberry Pi OS** (Lite o Full) en una tarjeta SD usando Raspberry Pi Imager.
   - Conectar la Pi al Wi-Fi editando `/etc/wpa_supplicant/wpa_supplicant.conf` o usando la GUI.
   - Habilitar la interfaz de la cámara mediante `raspi-config` (Opciones de Interfaz > Cámara).

2. **Instalar Dependencias**:
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-picamera2 python3-pip
   pip3 install python-telegram-bot
   ```

3. **Posicionar la Cámara**:
   - Montar la Pi Camera o la cámara web USB para que apunte hacia la luz del panel de la lavadora.
   - Probar la cámara con:
     ```bash
     libcamera-still -o test.jpg
     ```
     o para cámara web USB:
     ```bash
     fswebcam test.jpg
     ```

4. **Script de Python**:
A continuación se muestra un script de Python de ejemplo para que la Raspberry Pi detecte la luz del panel y envíe notificaciones por Telegram.

```python
import cv2
import numpy as np
from picamera2 import Picamera2
import telegram
import asyncio
import time

# Configuración del bot de Telegram
BOT_TOKEN = "tu_bot_token"
CHAT_ID = "tu_chat_id"
bot = telegram.Bot(token=BOT_TOKEN)

# Configuración de la cámara
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))
picam2.start()

# Configuración de la ROI (ajustar según la vista de la cámara)
ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT = 200, 150, 50, 50
THRESHOLD = 150  # Umbral de brillo (0-255)
STOP_DELAY = 300  # 5 minutos en segundos

machine_running = False
last_on_time = 0

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def is_light_on(frame):
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Aplicar desenfoque gaussiano
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # Extraer la ROI
    roi = gray[ROI_Y:ROI_Y+ROI_HEIGHT, ROI_X:ROI_X+ROI_WIDTH]
    # Calcular el brillo promedio
    avg_brightness = np.mean(roi)
    return avg_brightness > THRESHOLD

async def main():
    global machine_running, last_on_time
    while True:
        # Capturar imagen
        frame = picam2.capture_array()
        # Verificar si la luz está encendida
        if is_light_on(frame):
            if not machine_running:
                machine_running = True
                print("La máquina está ENCENDIDA")
            last_on_time = time.time()
        else:
            if machine_running and (time.time() - last_on_time > STOP_DELAY):
                machine_running = False
                print("La máquina se detuvo")
                await send_telegram_message("¡La lavadora se detuvo! Es hora de colgar la ropa.")
        time.sleep(10)  # Verificar cada 10 segundos

if __name__ == "__main__":
    asyncio.run(main())
```

5. **Personalizar el Script**:
   - Reemplaza `BOT_TOKEN` y `CHAT_ID` con tus credenciales de Telegram.
   - Ajusta `ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT` capturando una imagen de prueba y analizándola con una herramienta como GIMP o Python para ubicar la luz del panel.
   - Ajusta `THRESHOLD` basándote en imágenes de prueba (mayor para luces más brillantes).
   - Modifica `STOP_DELAY` si es necesario.

6. **Ejecutar el Script**:
   ```bash
   python3 washer_monitor.py
   ```
   - Ejecuta en segundo plano con `nohup python3 washer_monitor.py &` o usa un servicio systemd para mayor confiabilidad.

7. **Probar y Desplegar**:
   - Inicia la lavadora y monitorea la salida del script.
   - Verifica las notificaciones de Telegram.
   - Asegura la Pi y la cámara en una configuración permanente.

---

### Otras Alternativas
1. **Sensor de Vibración**:
   - **Hardware**: Usar un sensor de vibración (ej., SW-420) con un ESP8266 o Raspberry Pi.
   - **Configuración**: Adjuntar el sensor a la lavadora para detectar vibraciones.
   - **Algoritmo**: Monitorear la ausencia sostenida de vibraciones (ej., 5 minutos) para detectar cuándo se detiene la máquina.
   - **Pros**: Simple, bajo costo, no afectado por la luz ambiental.
   - **Contras**: Puede pasar por alto ciclos con pausas largas (ej., remojo).
   - **Ejemplo de Código (ESP8266)**:
     ```cpp
     #include <ESP8266WiFi.h>
     #include <UniversalTelegramBot.h>
     #define VIBRATION_PIN D5
     #define BOT_TOKEN "tu_bot_token"
     #define CHAT_ID "tu_chat_id"
     WiFiClientSecure client;
     UniversalTelegramBot bot(BOT_TOKEN, client);
     bool machineRunning = false;
     unsigned long lastVibrationTime = 0;
     void setup() {
       pinMode(VIBRATION_PIN, INPUT);
       WiFi.begin("ssid", "password");
       while (WiFi.status() != WL_CONNECTED) delay(500);
       client.setInsecure();
     }
     void loop() {
       if (digitalRead(VIBRATION_PIN)) {
         machineRunning = true;
         lastVibrationTime = millis();
       } else if (machineRunning && (millis() - lastVibrationTime > 300000)) {
         machineRunning = false;
         bot.sendMessage(CHAT_ID, "¡La lavadora se detuvo!", "");
       }
       delay(1000);
     }
     ```

2. **Sensor de Corriente**:
   - **Hardware**: Usar un sensor de corriente ACS712 con un ESP8266 o Raspberry Pi.
   - **Configuración**: Colocar el sensor de forma no invasiva alrededor del cable de alimentación de la lavadora.
   - **Algoritmo**: Detectar cuando la corriente cae por debajo de un umbral (ej., <0.5A) durante 5 minutos.
   - **Pros**: Preciso, no invasivo.
   - **Contras**: Requiere conocimientos eléctricos, calibración para el consumo de energía de la máquina.

3. **Micrófonos**:
   - **Hardware**: Usar un módulo de micrófono (ej., KY-038) con una Raspberry Pi.
   - **Algoritmo**: Analizar los niveles de sonido para detectar cuándo cesa el ruido de la máquina.
   - **Pros**: No visual, funciona en condiciones de poca luz.
   - **Contras**: Sensible al ruido ambiental, requiere procesamiento de señales.

---

### Recomendación
- **Raspberry Pi**: La mejor opción para un procesamiento de imagen robusto y expansibilidad futura. Úsala si te sientes cómodo con Python y quieres una alta confiabilidad en distintas condiciones de luz.
- **Arduino (ESP32-CAM)**: La mejor opción para una configuración simple y de bajo costo. Ideal si quieres una configuración mínima y te conformas con un procesamiento de imagen básico.
- **Sensor de Vibración o Corriente**: La mejor opción para soluciones sin cámara, especialmente si la luz del panel no es confiable (ej., tenue u obstruida). Úsalos con ESP8266 por simplicidad.
- **Micrófono**: Menos confiable debido al ruido ambiental, pero viable como sensor secundario.

Para tu casa de dos pisos, la Raspberry Pi o el ESP32-CAM con una cámara son ideales ya que estás en el segundo piso y necesitas notificaciones remotas confiables vía Telegram. La Raspberry Pi ofrece una mejor precisión para la detección de luz, mientras que el ESP32-CAM es más económico y simple de desplegar. Si prefieres un enfoque sin cámara, un sensor de vibración con un ESP8266 es la alternativa más fácil.

¡Avísame si quieres una inmersión más profunda en algún enfoque específico, necesitas ayuda con la configuración o quieres código para un sensor alternativo!