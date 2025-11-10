---
audio: false
generated: true
lang: de
layout: post
title: Intelligenter Waschmaschinenmonitor mit Arduino und Telegram-Benachrichtigungen
translated: true
type: note
---

Um ein System zu erstellen, das erkennt, wann Ihre Maytag MHW8630HW Waschmaschine stoppt (indem die Panel-Leuchte als Indikator verwendet wird) und Sie über einen Telegram-Bot benachrichtigt, um Ihre Kleidung aufzuhängen, können Sie ein Arduino mit einem Kameramodul verwenden, um den Status der Maschine zu überwachen. Im Folgenden finden Sie eine detaillierte Anleitung zum Tech Stack, Hardware-Setup, Algorithmus und Implementierungsschritten.

---

### Tech Stack
#### Hardware
1. **Arduino Board**:
   - **ESP32-CAM** (empfohlen) – Kombiniert einen Mikrocontroller mit einer eingebauten OV2640-Kamera und Wi-Fi-Fähigkeit, perfekt für Bildverarbeitung und Telegram-Integration.
   - Alternative: Arduino Uno + separates Kameramodul (z.B. OV7670) und ESP8266 für Wi-Fi, aber dies ist komplexer einzurichten.
2. **Kameramodul**:
   - OV2640 (im ESP32-CAM enthalten) – 2MP Kamera, ausreichend zum Erkennen der Panel-Leuchte.
3. **Lichtsensor (Optional)**:
   - Fotowiderstand (LDR) oder TSL2561 – Um die kamerabasierte Lichterkennung für Redundanz oder einfachere Setups zu ergänzen.
4. **Stromversorgung**:
   - 5V USB-Netzteil oder Akkupack für den ESP32-CAM.
5. **Montage**:
   - Kleines Gehäuse oder 3D-gedruckter Halter für den ESP32-CAM, mit freier Sicht auf das Bedienfeld der Waschmaschine.
6. **Wi-Fi Router**:
   - Damit sich der ESP32-CAM mit dem Internet verbinden und mit dem Telegram-Bot kommunizieren kann.

#### Software
1. **Arduino IDE**:
   - Zum Programmieren des ESP32-CAM.
2. **Bibliotheken**:
   - **Universal Arduino Telegram Bot Library** von Brian Lough – Für die Telegram-Bot-Integration.
   - **ArduinoJson** – Zum Verarbeiten von JSON-Daten für die Telegram-API-Kommunikation.
   - **ESP32-CAM Camera Libraries** – Eingebaute Bibliotheken zum Erfassen und Verarbeiten von Bildern.
3. **Telegram Bot**:
   - Verwenden Sie BotFather auf Telegram, um einen Bot zu erstellen und ein Bot-Token und eine Chat-ID zu erhalten.
4. **Programmiersprache**:
   - C++ (Arduino Sketch).
5. **Optionale Tools**:
   - OpenCV (Python) zum Prototypen von Bildverarbeitungsalgorithmen auf einem Computer, bevor sie auf Arduino portiert werden (vereinfacht für ESP32-CAM).

---

### Algorithmus zur Erkennung des Waschmaschinenstatus
Da die Maytag MHW8630HW eine Panel-Leuchte hat, die anzeigt, wann die Maschine eingeschaltet ist, können Sie die Kamera verwenden, um dieses Licht zu erkennen. Der Algorithmus verarbeitet Bilder, um festzustellen, ob das Licht ein- oder ausgeschaltet ist, und zeigt so den Status der Maschine an.

#### Erkennungsalgorithmus
1. **Bilderfassung**:
   - Erfassen Sie periodisch Bilder des Bedienfelds der Waschmaschine mit dem ESP32-CAM.
2. **Region of Interest (ROI) Auswahl**:
   - Definieren Sie einen bestimmten Bereich im Bild, in dem sich die Panel-Leuchte befindet (z.B. ein rechteckiger Bereich um den Power-Indikator).
3. **Bildverarbeitung**:
   - **Graustufenkonvertierung**: Konvertieren Sie das aufgenommene Bild in Graustufen, um die Verarbeitung zu vereinfachen.
   - **Schwellwertverarbeitung**: Wenden Sie einen Helligkeitsschwellwert an, um das Vorhandensein des Lichts zu erkennen. Die Panel-Leuchte erzeugt einen hellen Fleck, wenn sie eingeschaltet ist, im Vergleich zu einem dunkleren Bereich, wenn sie ausgeschaltet ist.
   - **Pixelintensitätsanalyse**: Berechnen Sie die durchschnittliche Pixelintensität in der ROI. Eine hohe Intensität zeigt an, dass das Licht eingeschaltet ist, eine niedrige Intensität, dass es ausgeschaltet ist.
4. **Zustandsautomat**:
   - Verfolgen Sie den Status der Maschine (EIN oder AUS) basierend auf aufeinanderfolgenden Messwerten.
   - Wenn das Licht für mehrere Zyklen als EIN erkannt wird, wird angenommen, dass die Maschine läuft.
   - Wenn das Licht auf AUS wechselt und für einen festgelegten Zeitraum (z.B. 5 Minuten) aus bleibt, wird angenommen, dass der Waschzyklus beendet ist.
5. **Entprellung**:
   - Implementieren Sie eine Verzögerung (z.B. 5 Minuten), um zu bestätigen, dass die Maschine gestoppt hat, und um falsche Benachrichtigungen während Pausen im Waschzyklus (z.B. Einweichen oder Befüllen) zu vermeiden.
6. **Benachrichtigung**:
   - Wenn bestätigt ist, dass die Maschine gestoppt hat, senden Sie eine Telegram-Nachricht (z.B. "Waschmaschine gestoppt! Zeit, die Wäsche aufzuhängen.").

#### Warum nicht komplexere Algorithmen verwenden?
- Fortgeschrittene Algorithmen wie Machine Learning (z.B. CNNs für Objekterkennung) sind für diese Aufgabe übertrieben und ressourcenintensiv für die begrenzte Rechenleistung des ESP32-CAM.
- Einfache Schwellwertverarbeitung ist ausreichend, da die Panel-Leuchte ein klares binäres Signal (EIN/AUS) ist.

---

### Implementierungsanleitung
#### Schritt 1: Richten Sie den Telegram-Bot ein
1. **Erstellen Sie einen Telegram-Bot**:
   - Öffnen Sie Telegram, suchen Sie nach **@BotFather** und starten Sie einen Chat.
   - Senden Sie `/newbot`, benennen Sie Ihren Bot (z.B. "WasherBot") und erhalten Sie das **Bot Token**.
   - Senden Sie `/start` an Ihren Bot und erhalten Sie Ihre **Chat ID** über einen Dienst wie `@GetIDsBot` oder indem Sie eingehende Nachrichten in Ihrem Code überprüfen.
2. **Installieren Sie Telegram auf Ihrem Telefon**:
   - Stellen Sie sicher, dass Sie Nachrichten von Ihrem Bot empfangen können.

#### Schritt 2: Hardware-Setup
1. **Positionieren Sie den ESP32-CAM**:
   - Montieren Sie den ESP32-CAM in einem kleinen Gehäuse oder mit Klebeband, ausgerichtet auf das Bedienfeld der Waschmaschine.
   - Stellen Sie sicher, dass die Kamera eine freie Sicht auf die Panel-Leuchte hat (testen Sie mit einem Beispielbild).
   - Sichern Sie den Aufbau, um Bewegung zu vermeiden, da dies die ROI-Konsistenz beeinträchtigen könnte.
2. **Stromversorgung für den ESP32-CAM**:
   - Schließen Sie ein 5V USB-Netzteil oder ein Akkupack an den 5V-Pin des ESP32-CAM an.
   - Stellen Sie eine stabile Stromquelle sicher, da Kamera und Wi-Fi erheblichen Strom verbrauchen.
3. **Optionaler Lichtsensor**:
   - Wenn Sie einen Fotowiderstand verwenden, schließen Sie ihn an einen analogen Pin des ESP32-CAM (z.B. GPIO 4) mit einem Spannungsteiler (z.B. 10kΩ Widerstand zu Masse) an.

#### Schritt 3: Software-Setup
1. **Installieren Sie die Arduino IDE**:
   - Laden Sie die Arduino IDE von [arduino.cc](https://www.arduino.cc/en/software) herunter und installieren Sie sie.
2. **Fügen Sie ESP32-Board-Unterstützung hinzu**:
   - Gehen Sie in der Arduino IDE zu **Datei > Einstellungen** und fügen Sie die folgende URL zu Zusätzliche Board-Verwalter-URLs hinzu:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - Gehen Sie zu **Werkzeuge > Board > Boardverwalter**, suchen Sie nach "ESP32" und installieren Sie das ESP32-Paket.
3. **Installieren Sie Bibliotheken**:
   - Installieren Sie die **Universal Arduino Telegram Bot Library**:
     - Laden Sie sie von [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) herunter und fügen Sie sie über **Sketch > Bibliothek einbinden > .ZIP-Bibliothek hinzufügen** hinzu.
   - Installieren Sie **ArduinoJson**:
     - Gehen Sie zu **Sketch > Bibliothek einbinden > Bibliotheken verwalten**, suchen Sie nach "ArduinoJson" und installieren Sie Version 6.x.x.
4. **Konfigurieren Sie Wi-Fi**:
   - Stellen Sie sicher, dass sich Ihr ESP32-CAM mit Ihrem Heim-Wi-Fi-Netzwerk verbinden kann (2.4GHz, da 5GHz nicht unterstützt wird).

#### Schritt 4: Schreiben Sie den Arduino-Code
Im Folgenden finden Sie einen Beispiel-Sketch für den ESP32-CAM, um die Panel-Leuchte zu erkennen und Telegram-Benachrichtigungen zu senden. Dieser Code setzt voraus, dass Sie die ROI-Koordinaten für die Panel-Leuchte identifiziert haben.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// Wi-Fi Zugangsdaten
#define WIFI_SSID "ihre_wifi_ssid"
#define WIFI_PASSWORD "ihre_wifi_password"

// Telegram Bot Zugangsdaten
#define BOT_TOKEN "ihr_bot_token"
#define CHAT_ID "ihre_chat_id"

// Kamera-Konfiguration (für ESP32-CAM)
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

#define ROI_X 100 // Anpassen basierend auf Kamerablick (x-Koordinate der ROI)
#define ROI_Y 100 // y-Koordinate der ROI
#define ROI_WIDTH 50 // Breite der ROI
#define ROI_HEIGHT 50 // Höhe der ROI
#define THRESHOLD 150 // Helligkeitsschwellwert (0-255)
#define STOP_DELAY 300000 // 5 Minuten in Millisekunden

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // Kamera initialisieren
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
  config.pixel_format = PIXFORMAT_GRAYSCALE; // Graustufen für Einfachheit
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Kamera-Initialisierung fehlgeschlagen mit Fehler 0x%x", err);
    return;
  }

  // Mit Wi-Fi verbinden
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi verbunden");

  // Telegram-Client konfigurieren
  client.setInsecure(); // Zur Vereinfachung; für Produktion ordnungsgemäße SSL-Zertifikate in Betracht ziehen
}

void loop() {
  // Bild aufnehmen
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Kameraaufnahme fehlgeschlagen");
    return;
  }

  // Durchschnittliche Helligkeit in der ROI berechnen
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

  // Zustandsautomat
  if (avgBrightness > THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("Maschine ist EIN");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("Maschine gestoppt");
      bot.sendMessage(CHAT_ID, "Waschmaschine gestoppt! Zeit, die Wäsche aufzuhängen.", "");
    }
  }

  delay(10000); // Überprüfe alle 10 Sekunden
}
```

#### Schritt 5: Passen Sie den Code an
1. **Aktualisieren Sie die Zugangsdaten**:
   - Ersetzen Sie `ihre_wifi_ssid`, `ihre_wifi_password`, `ihr_bot_token` und `ihre_chat_id` mit Ihren tatsächlichen Werten.
2. **Justieren Sie ROI und Schwellwert**:
   - Erfassen Sie ein Testbild mit dem ESP32-CAM (modifizieren Sie den Code, um ein Bild auf einer SD-Karte zu speichern oder es zu streamen).
   - Bestimmen Sie die ROI-Koordinaten (`ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT`), indem Sie das Bild analysieren, um sich auf die Panel-Leuchte zu konzentrieren.
   - Passen Sie `THRESHOLD` basierend auf Testbildern an (z.B. heller bei EIN, dunkler bei AUS).
3. **Passen Sie `STOP_DELAY` an**:
   - Setzen Sie es auf 300000 (5 Minuten), um falsche Benachrichtigungen während Zykluspausen zu vermeiden.

#### Schritt 6: Testen und Implementieren
1. **Laden Sie den Code hoch**:
   - Verbinden Sie den ESP32-CAM über einen USB-zu-Serial-Adapter (z.B. FTDI-Modul) mit Ihrem Computer.
   - Wählen Sie **ESP32 Wrover Module** in der Arduino IDE und laden Sie den Sketch hoch.
2. **Testen Sie das System**:
   - Starten Sie die Waschmaschine und überwachen Sie den Serial Monitor auf Statusänderungen.
   - Überprüfen Sie die Telegram-Benachrichtigungen, wenn die Maschine stoppt.
3. **Feinabstimmung**:
   - Passen Sie ROI, Schwellwert oder Verzögerung an, wenn falsche Positive/Negative auftreten.
4. **Dauerhafte Installation**:
   - Sichern Sie den ESP32-CAM in seinem Gehäuse und stellen Sie eine stabile Stromversorgung sicher.

---

### Alternativer Ansatz: Lichtsensor
Wenn die kamerabasierte Erkennung zu komplex oder unzuverlässig ist (z.B. aufgrund von Umgebungslicht), verwenden Sie einen Fotowiderstand:
- **Setup**: Bringen Sie einen Fotowiderstand an der Panel-Leuchte an (z.B. mit Klebeband) und schließen Sie ihn an einen analogen Pin an.
- **Code-Modifikation**: Ersetzen Sie die Bildverarbeitung durch analoge Messwerte:
  ```cpp
  int lightValue = analogRead(A0); // Fotowiderstand an GPIO 4
  if (lightValue > 500) { // Schwellwert anpassen
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Waschmaschine gestoppt! Zeit, die Wäsche aufzuhängen.", "");
  }
  ```
- **Vorteile**: Einfacher, weniger ressourcenintensiv.
- **Nachteile**: Erfordert physische Befestigung am Licht, weniger flexibel.

---

### Hinweise
- **Stromverbrauch**: Der ESP32-CAM verbraucht erheblichen Strom, wenn Kamera und Wi-Fi verwendet werden. Stellen Sie eine zuverlässige Stromquelle sicher.
- **Umgebungslicht**: Die kamerabasierte Erkennung kann durch Raumbeleuchtung beeinflusst werden. Testen Sie unter verschiedenen Bedingungen oder verwenden Sie einen Lichtsensor für Robustheit.
- **Sicherheit**: Der Beispielcode verwendet `setInsecure()` zur Vereinfachung. Für den Produktionseinsatz konfigurieren Sie ordnungsgemäße SSL-Zertifikate für die Telegram-Kommunikation.
- **Referenzen**: Dieser Ansatz ist inspiriert von Projekten wie dem ESP32-CAM Telegram-Sicherheitssystem und Waschmonitoren mit Vibrationssensoren, angepasst für lichtbasierte Erkennung.[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### Fehlerbehebung
- **Kamera initialisiert nicht**: Überprüfen Sie die Verkabelung, stellen Sie ausreichend Stromversorgung sicher und verifizieren Sie die Kamerakonfiguration.
- **Wi-Fi-Verbindungsprobleme**: Bestätigen Sie 2.4GHz Wi-Fi und korrekte Zugangsdaten.
- **Keine Telegram-Nachrichten**: Überprüfen Sie Bot-Token und Chat-ID, prüfen Sie den Serial Monitor auf Fehler.
- **Falsche Benachrichtigungen**: Passen Sie `THRESHOLD` oder `STOP_DELAY` an, um Zykluspausen zu berücksichtigen.

Diese Lösung nutzt die Fähigkeiten des ESP32-CAM für eine kostengünstige, nicht-invasive Möglichkeit, Ihre Waschmaschine zu überwachen und Sie über Telegram zu benachrichtigen. Lassen Sie mich wissen, wenn Sie Hilfe bei bestimmten Schritten oder beim Debugging benötigen!