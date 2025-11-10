---
audio: false
generated: true
lang: es
layout: post
title: Monitor Inteligente de Lavadora con Arduino y Alertas de Telegram
translated: true
type: note
---

Para crear un sistema que detecte cuándo tu lavadora Maytag MHW8630HW se detiene (utilizando su luz del panel como indicador) y te notifique a través de un bot de Telegram para que cuelgues la ropa, puedes usar un Arduino con un módulo de cámara para monitorear el estado de la máquina. A continuación, se presenta una guía detallada sobre la pila tecnológica, la configuración del hardware, el algoritmo y los pasos de implementación.

---

### Pila Tecnológica
#### Hardware
1. **Placa Arduino**:
   - **ESP32-CAM** (recomendado) – Combina un microcontrolador con una cámara OV2640 integrada y capacidad Wi-Fi, perfecto para procesamiento de imágenes e integración con Telegram.
   - Alternativa: Arduino Uno + módulo de cámara separado (por ejemplo, OV7670) y ESP8266 para Wi-Fi, pero esto es más complejo de configurar.
2. **Módulo de Cámara**:
   - OV2640 (incluido con ESP32-CAM) – Cámara de 2MP suficiente para detectar la luz del panel.
3. **Sensor de Luz (Opcional)**:
   - Fotorresistencia (LDR) o TSL2561 – Para complementar la detección de luz basada en cámara para redundancia o configuraciones más simples.
4. **Fuente de Alimentación**:
   - Adaptador de energía USB de 5V o paquete de baterías para el ESP32-CAM.
5. **Montaje**:
   - Carcasa pequeña o caja impresa en 3D para sostener el ESP32-CAM, con una vista clara del panel de control de la lavadora.
6. **Router Wi-Fi**:
   - Para que el ESP32-CAM se conecte a internet y se comunique con el bot de Telegram.

#### Software
1. **Arduino IDE**:
   - Para programar el ESP32-CAM.
2. **Librerías**:
   - **Universal Arduino Telegram Bot Library** por Brian Lough – Para la integración con el bot de Telegram.
   - **ArduinoJson** – Para manejar datos JSON para la comunicación con la API de Telegram.
   - **ESP32-CAM Camera Libraries** – Librerías integradas para capturar y procesar imágenes.
3. **Bot de Telegram**:
   - Usa BotFather en Telegram para crear un bot y obtener un token de bot y un ID de chat.
4. **Lenguaje de Programación**:
   - C++ (sketch de Arduino).
5. **Herramientas Opcionales**:
   - OpenCV (Python) para prototipar algoritmos de procesamiento de imágenes en una computadora antes de pasarlos al Arduino (simplificado para ESP32-CAM).

---

### Algoritmo para Detectar el Estado de la Lavadora
Dado que la Maytag MHW8630HW tiene una luz en el panel que indica cuándo la máquina está encendida, puedes usar la cámara para detectar esta luz. El algoritmo procesará imágenes para determinar si la luz está encendida o apagada, indicando el estado de la máquina.

#### Algoritmo de Detección
1. **Captura de Imagen**:
   - Capturar imágenes periódicamente del panel de control de la lavadora usando el ESP32-CAM.
2. **Selección de la Región de Interés (ROI)**:
   - Definir un área específica en la imagen donde se encuentra la luz del panel (por ejemplo, una región rectangular alrededor del indicador de encendido).
3. **Procesamiento de Imagen**:
   - **Conversión a Escala de Grises**: Convertir la imagen capturada a escala de grises para simplificar el procesamiento.
   - **Umbralización**: Aplicar un umbral de brillo para detectar la presencia de la luz. La luz del panel producirá un punto brillante cuando está encendida, en comparación con un área más oscura cuando está apagada.
   - **Análisis de Intensidad de Píxeles**: Calcular la intensidad promedio de los píxeles en la ROI. Una intensidad alta indica que la luz está encendida, mientras que una baja indica que está apagada.
4. **Máquina de Estados**:
   - Rastrear el estado de la máquina (ENCENDIDA o APAGADA) basado en lecturas consecutivas.
   - Si la luz se detecta como ENCENDIDA durante varios ciclos, asumir que la máquina está funcionando.
   - Si la luz cambia a APAGADA y permanece apagada durante un período establecido (por ejemplo, 5 minutos), asumir que el ciclo de lavado ha terminado.
5. **Eliminación de Rebotes (Debouncing)**:
   - Implementar un retardo (por ejemplo, 5 minutos) para confirmar que la máquina se ha detenido, evitando notificaciones falsas durante pausas en el ciclo de lavado (por ejemplo, durante el remojo o el llenado).
6. **Notificación**:
   - Cuando se confirma que la máquina se ha detenido, enviar un mensaje de Telegram (por ejemplo, "¡La lavadora se detuvo! Es hora de colgar la ropa.").

#### ¿Por Qué No Usar Algoritmos Más Complejos?
- Los algoritmos avanzados como el machine learning (por ejemplo, CNNs para detección de objetos) son excesivos para esta tarea y consumen muchos recursos para la limitada capacidad de procesamiento del ESP32-CAM.
- La umbralización simple es suficiente ya que la luz del panel es un indicador binario claro (ENCENDIDA/APAGADA).

---

### Guía de Implementación
#### Paso 1: Configurar el Bot de Telegram
1. **Crear un Bot de Telegram**:
   - Abre Telegram, busca **@BotFather** e inicia un chat.
   - Envía `/newbot`, nombra tu bot (por ejemplo, "WasherBot") y obtén el **Token del Bot**.
   - Envía `/start` a tu bot y obtén tu **ID de Chat** usando un servicio como `@GetIDsBot` o revisando los mensajes entrantes en tu código.
2. **Instalar Telegram en tu Teléfono**:
   - Asegúrate de poder recibir mensajes de tu bot.

#### Paso 2: Configuración del Hardware
1. **Posicionar el ESP32-CAM**:
   - Monta el ESP32-CAM en una carcasa pequeña o con cinta adhesiva, frente al panel de control de la lavadora.
   - Asegúrate de que la cámara tenga una vista clara de la luz del panel (prueba con una foto de muestra).
   - Asegura la configuración para evitar movimientos, ya que esto podría afectar la consistencia de la ROI.
2. **Alimentar el ESP32-CAM**:
   - Conecta un adaptador de energía USB de 5V o un paquete de baterías al pin 5V del ESP32-CAM.
   - Asegura una fuente de alimentación estable, ya que la cámara y el Wi-Fi consumen mucha energía.
3. **Sensor de Luz Opcional**:
   - Si usas una fotorresistencia, conéctala a un pin analógico del ESP32-CAM (por ejemplo, GPIO 4) con un circuito divisor de voltaje (por ejemplo, una resistencia de 10kΩ a tierra).

#### Paso 3: Configuración del Software
1. **Instalar Arduino IDE**:
   - Descarga e instala el Arduino IDE desde [arduino.cc](https://www.arduino.cc/en/software).
2. **Agregar Soporte para la Placa ESP32**:
   - En Arduino IDE, ve a **Archivo > Preferencias**, agrega la siguiente URL a las URLs adicionales del Administrador de Placas:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - Ve a **Herramientas > Placa > Administrador de Placas**, busca "ESP32" e instala el paquete ESP32.
3. **Instalar Librerías**:
   - Instala **Universal Arduino Telegram Bot Library**:
     - Descárgala desde [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) y agrégalo mediante **Sketch > Incluir Librería > Añadir Librería .ZIP**.
   - Instala **ArduinoJson**:
     - Ve a **Sketch > Incluir Librería > Gestionar Librerías**, busca "ArduinoJson" e instala la versión 6.x.x.
4. **Configurar Wi-Fi**:
   - Asegúrate de que tu ESP32-CAM pueda conectarse a tu red Wi-Fi doméstica (2.4GHz, ya que 5GHz no es compatible).

#### Paso 4: Escribir el Código de Arduino
A continuación se muestra un sketch de Arduino de ejemplo para que el ESP32-CAM detecte la luz del panel y envíe notificaciones por Telegram. Este código asume que has identificado las coordenadas de la ROI para la luz del panel.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// Credenciales Wi-Fi
#define WIFI_SSID "tu_ssid_wifi"
#define WIFI_PASSWORD "tu_contraseña_wifi"

// Credenciales del Bot de Telegram
#define BOT_TOKEN "tu_token_del_bot"
#define CHAT_ID "tu_chat_id"

// Configuración de la cámara (para ESP32-CAM)
#define PWDN_GPIO_NUM 32
#define RESET_GPIO_NUM -1
#define XCLK_GPIO_NUM 0
#define SIOD_GPIO_NUM 26
#define SIOC_GPIO_NUM 27
#define Y9_GPIO_NUM 35
#define Y8_GPIO_NUM 34
#define Y7_GPIO_NUM 39
#define Y6_GPIO_NUM 36
#define Y5_GPIO_NUM 21
#define Y4_GPIO_NUM 19
#define Y3_GPIO_NUM 18
#define Y2_GPIO_NUM 5
#define VSYNC_GPIO_NUM 25
#define HREF_GPIO_NUM 23
#define PCLK_GPIO_NUM 22

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

#define ROI_X 100 // Ajustar según la vista de la cámara (coordenada x de la ROI)
#define ROI_Y 100 // coordenada y de la ROI
#define ROI_WIDTH 50 // Ancho de la ROI
#define ROI_HEIGHT 50 // Alto de la ROI
#define THRESHOLD 150 // Umbral de brillo (0-255)
#define STOP_DELAY 300000 // 5 minutos en milisegundos

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // Inicializar cámara
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_GRAYSCALE; // Escala de grises para simplificar
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // Conectar a Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Configurar cliente de Telegram
  client.setInsecure(); // Por simplicidad; considerar SSL adecuado en producción
}

void loop() {
  // Capturar imagen
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }

  // Calcular brillo promedio en la ROI
  uint32_t totalBrightness = 0;
  uint16_t pixelCount = 0;
  for (int y = ROI_Y; y < ROI_Y + ROI_HEIGHT; y++) {
    for (int x = ROI_X; x < ROI_X + ROI_WIDTH; x++) {
      if (x < fb->width && y < fb->height) {
        totalBrightness += fb->buf[y * fb->width + x];
        pixelCount++;
      }
    }
  }
  esp_camera_framebuffer_return(fb);

  float avgBrightness = pixelCount > 0 ? (float)totalBrightness / pixelCount : 0;

  // Máquina de estados
  if (avgBrightness > THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("Machine is ON");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("Machine stopped");
      bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
    }
  }

  delay(10000); // Verificar cada 10 segundos
}
```

#### Paso 5: Personalizar el Código
1. **Actualizar Credenciales**:
   - Reemplaza `tu_ssid_wifi`, `tu_contraseña_wifi`, `tu_token_del_bot` y `tu_chat_id` con tus valores reales.
2. **Ajustar ROI y Umbral**:
   - Captura una imagen de prueba usando el ESP32-CAM (modifica el código para guardar una imagen en una tarjeta SD o transmitirla).
   - Determina las coordenadas de la ROI (`ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT`) analizando la imagen para enfocarte en la luz del panel.
   - Ajusta `THRESHOLD` basándote en imágenes de prueba (por ejemplo, más brillante cuando está ENCENDIDA, más oscura cuando está APAGADA).
3. **Ajustar `STOP_DELAY`**:
   - Establécelo en 300000 (5 minutos) para evitar notificaciones falsas durante pausas del ciclo.

#### Paso 6: Probar y Desplegar
1. **Cargar el Código**:
   - Conecta el ESP32-CAM a tu computadora a través de un adaptador USB-a-serial (por ejemplo, módulo FTDI).
   - Selecciona **ESP32 Wrover Module** en Arduino IDE y carga el sketch.
2. **Probar el Sistema**:
   - Enciende la lavadora y monitorea el Monitor Serie para ver los cambios de estado.
   - Verifica las notificaciones de Telegram cuando la máquina se detenga.
3. **Ajustes Finos**:
   - Ajusta la ROI, el umbral o el retardo si ocurren falsos positivos/negativos.
4. **Instalación Permanente**:
   - Asegura el ESP32-CAM en su carcasa y asegura una fuente de alimentación estable.

---

### Enfoque Alternativo: Sensor de Luz
Si la detección basada en cámara es demasiado compleja o poco confiable (por ejemplo, debido a la luz ambiental), usa una fotorresistencia:
- **Configuración**: Adjunta una fotorresistencia a la luz del panel (por ejemplo, con cinta) y conéctala a un pin analógico.
- **Modificación del Código**: Reemplaza el procesamiento de imágenes con lecturas analógicas:
  ```cpp
  int lightValue = analogRead(A0); // Fotorresistencia en GPIO 4
  if (lightValue > 500) { // Ajustar umbral
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
  }
  ```
- **Pros**: Más simple, consume menos recursos.
- **Contras**: Requiere fijación física a la luz, menos flexible.

---

### Notas
- **Consumo de Energía**: El ESP32-CAM consume mucha energía cuando usa la cámara y el Wi-Fi. Asegura una fuente de alimentación confiable.
- **Luz Ambiental**: La detección basada en cámara puede verse afectada por la iluminación de la habitación. Prueba en varias condiciones o usa un sensor de luz para mayor robustez.
- **Seguridad**: El código de ejemplo usa `setInsecure()` por simplicidad. Para producción, configura certificados SSL adecuados para la comunicación con Telegram.
- **Referencias**: Este enfoque está inspirado en proyectos como el sistema de seguridad ESP32-CAM Telegram y monitores de lavandería que usan sensores de vibración, adaptados para la detección basada en luz.[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### Resolución de Problemas
- **La Cámara Falla al Inicializar**: Verifica el cableado, asegura energía suficiente y verifica la configuración de la cámara.
- **Problemas de Conexión Wi-Fi**: Confirma que sea Wi-Fi de 2.4GHz y las credenciales correctas.
- **No Llegan Mensajes de Telegram**: Verifica el token del bot y el ID de chat, revisa el Monitor Serie en busca de errores.
- **Notificaciones Falsas**: Ajusta `THRESHOLD` o `STOP_DELAY` para tener en cuenta las pausas del ciclo.

Esta solución aprovecha las capacidades del ESP32-CAM para una forma económica y no invasiva de monitorear tu lavadora y notificarte a través de Telegram. ¡Avísame si necesitas ayuda con pasos específicos o depuración!