---
audio: false
generated: true
lang: es
layout: post
title: Detección Basada en Sonido para Lavadoras Maytag
translated: true
type: note
---

Utilizar el sonido para detectar cuando tu lavadora Maytag MHW8630HW se detiene es una alternativa viable al enfoque basado en cámara. Colocando un sensor de sonido cerca de la lavadora, puedes monitorear el ruido generado durante su operación (por ejemplo, el zumbido del motor, el flujo de agua o la rotación del tambor) y detectar cuándo se detiene, lo que indica el final del ciclo de lavado. A continuación, explicaré cómo adaptar el proyecto anterior para usar un sensor de sonido en lugar de una cámara, centrándome en el hardware, el algoritmo y los cambios en el código, manteniendo el sistema de notificaciones de Telegram.

---

### Tech Stack
#### Hardware
1. **Placa Arduino**:
   - **ESP32-CAM** (todavía utilizable) – Conserva el Wi-Fi para la integración con Telegram, aunque la cámara no es necesaria.
   - Alternativa: **ESP8266 NodeMCU** o **Arduino Uno** con un módulo ESP8266 para Wi-Fi (más simple si no necesitas la cámara).
2. **Sensor de Sonido**:
   - **Sensor de Sonido con Micrófono KY-038** o similar – Económico, detecta niveles de sonido a través de una salida analógica.
   - Alternativa: **Amplificador de Micrófono Electret MAX9814** – Más sensible, con ganancia ajustable para una mejor detección.
3. **Fuente de Alimentación**:
   - Adaptador de corriente USB de 5V o paquete de baterías para la placa ESP32 u otra.
4. **Montaje**:
   - Coloca el sensor de sonido cerca de la lavadora (por ejemplo, pegado al lateral o la parte superior) donde pueda detectar los sonidos de funcionamiento, pero evita la exposición directa al agua.
   - Utiliza una pequeña caja para proteger el sensor y la placa.
5. **Router Wi-Fi**:
   - Para la conectividad a internet y enviar notificaciones de Telegram.

#### Software
- **Arduino IDE**: Para programar la placa ESP32 u otra.
- **Librerías**:
  - **Universal Arduino Telegram Bot Library** por Brian Lough – Para la integración con Telegram.
  - **ArduinoJson** – Para manejar datos JSON en la comunicación con la API de Telegram.
- **Bot de Telegram**: Igual que antes, usando BotFather para obtener un token de bot y un ID de chat.
- **Lenguaje de Programación**: C++ (sketch de Arduino).

---

### Algoritmo para Detectar el Estado de la Lavadora con Sonido
El sensor de sonido detectará el nivel de ruido producido por la lavadora. Cuando la máquina está en funcionamiento, genera sonidos consistentes (por ejemplo, motor, agua o tambor). Cuando se detiene, el nivel de sonido cae significativamente. El algoritmo procesa estos niveles de sonido para determinar el estado de la máquina.

#### Algoritmo de Detección
1. **Muestreo de Sonido**:
   - Lee continuamente la salida analógica del sensor de sonido para medir los niveles de ruido.
2. **Procesamiento de Señal**:
   - **Promediado**: Calcula el nivel de sonido promedio en una ventana corta (por ejemplo, 1-2 segundos) para suavizar los ruidos transitorios (por ejemplo, un portazo).
   - **Umbralización**: Compara el nivel de sonido promedio con un umbral predefinido. Un nivel alto indica que la máquina está en funcionamiento, mientras que un nivel bajo sugiere que está detenida.
3. **Máquina de Estados**:
   - Rastrea el estado de la máquina (ON o OFF) basándose en los niveles de sonido.
   - Si el nivel de sonido excede el umbral durante varios ciclos, asume que la máquina está en funcionamiento.
   - Si el nivel de sonido cae por debajo del umbral y permanece bajo durante un período establecido (por ejemplo, 5 minutos), asume que el ciclo de lavado ha terminado.
4. **Debouncing**:
   - Implementa un retardo (por ejemplo, 5 minutos) para confirmar que la máquina se ha detenido, evitando notificaciones falsas durante las fases silenciosas (por ejemplo, remojo o pausas en el ciclo).
5. **Notificación**:
   - Cuando se confirma que la máquina se ha detenido, envía un mensaje de Telegram (por ejemplo, "¡La lavadora se ha detenido! Es hora de tender la ropa.").

#### ¿Por qué Detección por Sonido?
- La detección por sonido es más simple que el procesamiento de imágenes, ya que no requiere algoritmos complejos ni altos recursos computacionales.
- Es menos sensible a los cambios de luz ambiental en comparación con la detección basada en cámara.
- Sin embargo, puede verse afectada por el ruido de fondo (por ejemplo, un televisor alto), por lo que la ubicación y el ajuste del umbral son críticos.

---

### Guía de Implementación
#### Paso 1: Configurar el Bot de Telegram
- Sigue los mismos pasos que en la guía original:
  - Crea un bot usando **@BotFather** para obtener un **Bot Token**.
  - Obtén tu **Chat ID** usando **@GetIDsBot** o revisando los mensajes entrantes.
  - Asegúrate de tener Telegram configurado en tu teléfono para recibir notificaciones.

#### Paso 2: Configuración del Hardware
1. **Elige un Sensor de Sonido**:
   - **KY-038**: Proporciona una salida analógica (0-1023 para el ADC de 10 bits del ESP32) proporcional a la intensidad del sonido. También tiene una salida digital, pero la analógica es mejor para una detección matizada.
   - **MAX9814**: Más sensible, con ganancia ajustable a través de un potenciómetro. Conecta a un pin analógico.
2. **Conecta el Sensor de Sonido**:
   - Para KY-038:
     - **VCC** a 5V (o 3.3V, dependiendo de la placa).
     - **GND** a GND.
     - **Salida Analógica (A0)** a un pin analógico en el ESP32 (por ejemplo, GPIO 4).
   - Para MAX9814:
     - Conexiones similares, pero ajusta la ganancia usando el potenciómetro integrado para una sensibilidad óptima.
3. **Posiciona el Sensor**:
   - Coloca el sensor cerca de la lavadora (por ejemplo, en el lateral o la parte superior) donde pueda detectar el ruido del motor o del tambor. Evita áreas con exposición al agua.
   - Prueba la ubicación monitoreando los niveles de sonido durante un ciclo de lavado (usa el Monitor Serie para registrar los valores).
4. **Alimenta la Placa**:
   - Conecta un adaptador de corriente USB de 5V o un paquete de baterías a la placa ESP32 u otra.
   - Asegura una alimentación estable, ya que la comunicación Wi-Fi requiere un voltaje consistente.
5. **Montaje**:
   - Usa una pequeña caja o cinta para asegurar el sensor y la placa, garantizando que el micrófono esté expuesto para capturar el sonido.

#### Paso 3: Configuración del Software
- **Arduino IDE**: Instala como se describe en la guía original.
- **Soporte para Placa ESP32**: Añade el paquete de la placa ESP32 a través del Boards Manager (misma URL que antes).
- **Librerías**:
  - Instala **Universal Arduino Telegram Bot Library** y **ArduinoJson** como se describió.
- **Wi-Fi**: Asegúrate de que la placa pueda conectarse a tu red Wi-Fi de 2.4GHz.

#### Paso 4: Escribe el Código Arduino
A continuación se muestra un sketch de Arduino de ejemplo para el ESP32 (o ESP8266) para detectar niveles de sonido y enviar notificaciones de Telegram. Esto asume un sensor de sonido KY-038 conectado al GPIO 4.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Credenciales Wi-Fi
#define WIFI_SSID "tu_ssid_wifi"
#define WIFI_PASSWORD "tu_password_wifi"

// Credenciales del Bot de Telegram
#define BOT_TOKEN "tu_bot_token"
#define CHAT_ID "tu_chat_id"

// Pin del sensor de sonido
#define SOUND_PIN 4 // GPIO 4 para entrada analógica

// Parámetros de detección de sonido
#define SOUND_THRESHOLD 300 // Ajustar basado en pruebas (0-1023)
#define SAMPLE_WINDOW 2000 // 2 segundos para promediar
#define STOP_DELAY 300000 // 5 minutos en milisegundos

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // Conectar a Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Configurar cliente Telegram
  client.setInsecure(); // Por simplicidad; considera SSL adecuado en producción

  // Configurar pin del sensor de sonido
  pinMode(SOUND_PIN, INPUT);
}

void loop() {
  // Muestrear nivel de sonido en una ventana
  unsigned long startMillis = millis();
  uint32_t totalSound = 0;
  uint16_t sampleCount = 0;

  while (millis() - startMillis < SAMPLE_WINDOW) {
    totalSound += analogRead(SOUND_PIN);
    sampleCount++;
    delay(10); // Pequeño retardo entre muestras
  }

  float avgSound = sampleCount > 0 ? (float)totalSound / sampleCount : 0;
  Serial.print("Nivel de sonido promedio: ");
  Serial.println(avgSound);

  // Máquina de estados
  if (avgSound > SOUND_THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("Máquina ENCENDIDA");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("Máquina DETENIDA");
      bot.sendMessage(CHAT_ID, "¡La lavadora se ha detenido! Es hora de tender la ropa.", "");
    }
  }

  delay(10000); // Verificar cada 10 segundos
}
```

#### Paso 5: Personaliza el Código
1. **Actualiza Credenciales**:
   - Reemplaza `tu_ssid_wifi`, `tu_password_wifi`, `tu_bot_token` y `tu_chat_id` con tus valores reales.
2. **Ajusta `SOUND_THRESHOLD`**:
   - Ejecuta la lavadora y monitorea los niveles de sonido a través del Monitor Serie (`Serial.println(analogRead(SOUND_PIN));`).
   - Establece `SOUND_THRESHOLD` a un valor por encima del ruido ambiental pero por debajo del ruido operativo de la máquina (por ejemplo, 200-500, dependiendo de tu configuración).
3. **Ajusta `SAMPLE_WINDOW`**:
   - Una ventana de 2 segundos (`2000` ms) suaviza los ruidos transitorios. Auméntala si el ruido de fondo causa lecturas falsas.
4. **Ajusta `STOP_DELAY`**:
   - Establécelo en `300000` (5 minutos) para evitar notificaciones falsas durante fases silenciosas como el remojo.

#### Paso 6: Prueba y Despliega
1. **Carga el Código**:
   - Conecta el ESP32 a tu computadora a través de un adaptador USB-a-serial.
   - Selecciona **ESP32 Wrover Module** (o **NodeMCU** para ESP8266) en Arduino IDE y carga el sketch.
2. **Prueba el Sistema**:
   - Inicia la lavadora y monitorea el Monitor Serie para ver los niveles de sonido y los cambios de estado.
   - Verifica las notificaciones de Telegram cuando la máquina se detenga.
3. **Ajusta**:
   - Ajusta `SOUND_THRESHOLD` o `STOP_DELAY` si ocurren falsos positivos/negativos.
   - Prueba en diferentes condiciones (por ejemplo, con ruido de fondo) para asegurar la fiabilidad.
4. **Instalación Permanente**:
   - Asegura el sensor y la placa en una caja cerca de la máquina, garantizando que el micrófono esté expuesto pero protegido del agua.

---

### Ventajas de la Detección por Sonido
- **Procesamiento Más Simple**: Sin procesamiento de imágenes, reduciendo la carga computacional en el ESP32.
- **Económico**: Los sensores de sonido como el KY-038 son económicos (a menudo menos de $5).
- **No Invasivo**: No es necesario conectar nada directamente a la luz del panel de la máquina.

### Desafíos y Mitigaciones
- **Ruido de Fondo**: Los ruidos del hogar (por ejemplo, TV, conversaciones) pueden interferir. Mitiga mediante:
  - Colocando el sensor cerca del motor o tambor de la máquina.
  - Ajustando `SOUND_THRESHOLD` para ignorar el ruido ambiental.
  - Usando un micrófono direccional o ajustando la ganancia en el MAX9814.
- **Fases Silenciosas**: Algunos ciclos de lavado tienen pausas (por ejemplo, remojo). El `STOP_DELAY` asegura que las notificaciones se envíen solo después de un silencio prolongado.
- **Exposición al Agua**: Asegura que el sensor esté en una caja resistente al agua, ya que las lavadoras pueden tener salpicaduras o humedad.

### Mejoras Opcionales
- **Análisis de Frecuencia**: Si el ruido de fondo es un problema persistente, analiza las frecuencias del sonido (por ejemplo, el zumbido del motor a 50-200 Hz) usando una librería de Transformada Rápida de Fourier (FFT) como `arduinoFFT`. Esto requiere más potencia de procesamiento y puede no ser factible en un ESP32 básico sin optimización.
- **Sensores Duales**: Combina sensores de sonido y vibración (por ejemplo, SW-420) para redundancia. Si ambos indican que la máquina está apagada, la confianza en la detección aumenta.
- **Alimentación por Batería**: Para portabilidad, usa una batería LiPo recargable con un módulo de carga (por ejemplo, TP4056) en lugar de un adaptador USB.

---

### Resolución de Problemas
- **No Detecta Sonido**: Verifica el cableado del sensor, prueba con el Monitor Serie y asegúrate de que el sensor esté cerca de la fuente de ruido de la máquina.
- **Notificaciones Falsas**: Aumenta `STOP_DELAY` o ajusta `SOUND_THRESHOLD` para filtrar el ruido de fondo o las pausas del ciclo.
- **Problemas de Wi-Fi**: Verifica las credenciales de la red Wi-Fi de 2.4GHz y la fuerza de la señal cerca de la máquina.
- **No Llegan Mensajes de Telegram**: Confirma el token del bot y el ID del chat, revisa el Monitor Serie en busca de errores.

Este enfoque basado en sonido es más simple y robusto en condiciones de luz variables en comparación con el método basado en cámara, lo que lo hace ideal para un monitor de lavadora. ¡Avísame si necesitas ayuda con pasos específicos, calibración del sensor o integración de características adicionales!