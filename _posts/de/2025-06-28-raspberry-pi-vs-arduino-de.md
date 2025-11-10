---
audio: false
generated: true
lang: de
layout: post
title: Raspberry Pi vs. Arduino zur Waschmaschinenüberwachung mit Telegram-Benachrichtigungen
translated: true
type: note
---

Die Verwendung eines Raspberry Pi anstelle eines Arduino (wie dem ESP32-CAM) zum Erkennen, wann Ihre Maytag MHW8630HW Waschmaschine stoppt, und zum Senden einer Telegram-Benachrichtigung ist eine praktikable Alternative, die mehr Rechenleistung und Flexibilität bietet, allerdings auf Kosten erhöhter Komplexität und eines höheren Stromverbrauchs. Im Folgenden werde ich den Raspberry Pi-Ansatz mit der Arduino-Lösung vergleichen, andere Mikrocontroller-Optionen skizzieren und eine detaillierte Anleitung zur Implementierung des Systems mit einem Raspberry Pi geben. Ich werde auch alternative Ansätze (z. B. andere Hardware oder Sensoren) besprechen, um eine umfassende Antwort zu gewährleisten.

---

### Vergleich: Raspberry Pi vs. Arduino vs. Andere Optionen

| **Merkmal**                | **Raspberry Pi**                                                                 | **Arduino (ESP32-CAM)**                                                  | **Andere Optionen (z.B. NodeMCU, ESP8266)**                              |
|----------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Rechenleistung**         | Hoch (Quad-Core CPU, 1-8GB RAM) – Unterstützt erweiterte Bildverarbeitung, OpenCV. | Begrenzt (Dual-Core, 520KB SRAM) – Nur grundlegende Bildverarbeitung.     | Sehr begrenzt – Nicht geeignet für kamerabasierte Verarbeitung.          |
| **Kameraunterstützung**    | Einfach mit USB-Webcams oder Pi Camera Module (z.B. 8MP Pi Camera v2).          | Integrierte OV2640 (2MP) Kamera, aber geringere Auflösung und Qualität.   | Erfordert externes Kameramodul, komplexe Integration.                   |
| **Wi-Fi**                  | Integriert (die meisten Modelle, z.B. Pi 4, Zero 2 W).                          | Integriert (ESP32-CAM).                                                 | Integriert (z.B. ESP8266), aber keine native Kamerunterstützung.         |
| **Programmierung**         | Python, OpenCV, vielseitig, erfordert aber OS-Setup (Raspberry Pi OS).           | C++ in Arduino IDE, einfacher für Anfänger.                              | C++ oder Lua (z.B. NodeMCU), begrenzte Bibliotheken für Bildverarbeitung.|
| **Stromverbrauch**         | Höher (~2.5W für Pi Zero, ~5-10W für Pi 4).                                     | Niedriger (~1-2W für ESP32-CAM).                                        | Niedrigster (~0.5-1W für ESP8266).                                      |
| **Kosten**                 | $10 (Pi Zero W) bis $35+ (Pi 4) + $15 für Pi Camera.                            | ~$10 (ESP32-CAM mit Kamera).                                            | ~$5-10 (ESP8266/NodeMCU) + Sensorkosten.                                |
| **Einfachheit der Einrichtung** | Mittel (OS-Setup, Python-Programmierung).                                      | Einfach (Arduino IDE, einzelner Sketch).                                 | Einfach für einfache Sensoren, komplex für Kameras.                      |
| **Bester Anwendungsfall**  | Erweiterte Bildverarbeitung, flexibel für zukünftige Erweiterungen (z.B. ML-Modelle). | Einfache, kostengünstige Lichterkennung mit Telegram-Integration.       | Nicht-Kamera-Lösungen (z.B. Vibrations- oder Stromsensoren).            |

**Vorteile Raspberry Pi**:
- Überlegene Bildverarbeitung mit OpenCV für robuste Lichterkennung.
- Einfacher zu debuggen und zu erweitern (z.B. um eine Weboberfläche oder mehrere Sensoren).
- Unterstützt hochwertigere Kameras für bessere Genauigkeit bei unterschiedlichen Lichtverhältnissen.

**Nachteile Raspberry Pi**:
- Erfordert mehr Setup (OS-Installation, Python-Umgebung).
- Höherer Stromverbrauch, weniger ideal für batteriebetriebene Setups.
- Teurer als der ESP32-CAM.

**Andere Optionen**:
- **NodeMCU/ESP8266**: Geeignet für Nicht-Kamera-Lösungen (z.B. mit einem Vibrationssensor oder Stromsensor). Begrenzte Rechenleistung macht Kameraintegration unpraktisch.
- **Vibrationssensor**: Erkennt Maschinenvibrationen anstelle des Anzeigelichts. Einfach, kann aber subtile Zyklusänderungen verpassen.
- **Stromsensor**: Misst den Stromverbrauch (z.B. ACS712-Modul), um zu erkennen, wann die Maschine stoppt. Nicht-invasiv, erfordert aber elektrisches Setup.

---

### Implementierungsleitfaden für Raspberry Pi

#### Tech Stack
**Hardware**:
1. **Raspberry Pi**:
   - **Raspberry Pi Zero 2 W** ($15, kompakt, Wi-Fi-fähig) oder **Raspberry Pi 4** ($35+, leistungsstärker).
2. **Kamera**:
   - **Raspberry Pi Camera Module v2** ($15, 8MP) oder eine USB-Webcam.
3. **Stromversorgung**:
   - 5V USB-C (Pi 4) oder micro-USB (Pi Zero) mit 2-3A Ausgang.
4. **Montage**:
   - Gehäuse oder Klemmmontage, um die Kamera auf das Anzeigelicht der Waschmaschine auszurichten.

**Software**:
1. **OS**: Raspberry Pi OS (Lite für Effizienz, Full für einfacheres Setup).
2. **Programmiersprache**: Python.
3. **Bibliotheken**:
   - **OpenCV**: Für Bildverarbeitung zur Erkennung des Anzeigelichts.
   - **python-telegram-bot**: Für Telegram-Benachrichtigungen.
   - **picamera2** (für Pi Camera) oder **fswebcam** (für USB-Webcam).
4. **Telegram Bot**: Gleiches Setup wie bei Arduino (verwende BotFather für Bot-Token und Chat-ID).

#### Algorithmus
Der Algorithmus ähnelt dem Arduino-Ansatz, nutzt aber OpenCV für eine robustere Bildverarbeitung:
1. **Bilderfassung**: Verwende die Pi-Kamera oder Webcam, um periodisch Bilder aufzunehmen (z.B. alle 10 Sekunden).
2. **Region of Interest (ROI)**: Definiere ein Rechteck um das Anzeigelicht im Bild.
3. **Bildverarbeitung**:
   - In Graustufen umwandeln.
   - Gaußschen Weichzeichner anwenden, um Rauschen zu reduzieren.
   - Adaptive Schwellenwertbildung verwenden, um das helle Anzeigelicht vom Hintergrund zu unterscheiden.
   - Durchschnittliche Pixelintensität in der ROI berechnen oder helle Pixel zählen.
4. **Zustandsautomat**:
   - Wenn die ROI hell ist (Licht EIN), markiere die Maschine als laufend.
   - Wenn die ROI dunkel ist (Licht AUS) für 5 Minuten, markiere die Maschine als gestoppt und sende eine Telegram-Benachrichtigung.
5. **Entprellung**: Implementiere eine 5-minütige Verzögerung, um zu bestätigen, dass die Maschine gestoppt hat.

#### Implementierungsschritte
1. **Richten Sie den Raspberry Pi ein**:
   - Laden Sie **Raspberry Pi OS** (Lite oder Full) herunter und spielen Sie es mit dem Raspberry Pi Imager auf eine SD-Karte.
   - Verbinden Sie den Pi mit Wi-Fi, indem Sie `/etc/wpa_supplicant/wpa_supplicant.conf` bearbeiten oder die GUI verwenden.
   - Aktivieren Sie die Kamera-Schnittstelle über `raspi-config` (Interfacing Options > Camera).

2. **Installieren Sie die Abhängigkeiten**:
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-picamera2 python3-pip
   pip3 install python-telegram-bot
   ```

3. **Positionieren Sie die Kamera**:
   - Montieren Sie die Pi-Kamera oder USB-Webcam so, dass sie auf das Anzeigelicht der Waschmaschine zeigt.
   - Testen Sie die Kamera mit:
     ```bash
     libcamera-still -o test.jpg
     ```
     oder für USB-Webcam:
     ```bash
     fswebcam test.jpg
     ```

4. **Python-Skript**:
Unten finden Sie ein Beispiel-Python-Skript für den Raspberry Pi, um das Anzeigelicht zu erkennen und Telegram-Benachrichtigungen zu senden.

```python
import cv2
import numpy as np
from picamera2 import Picamera2
import telegram
import asyncio
import time

# Telegram Bot Konfiguration
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
bot = telegram.Bot(token=BOT_TOKEN)

# Kamerakonfiguration
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))
picam2.start()

# ROI Konfiguration (anpassen basierend auf Kamerabild)
ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT = 200, 150, 50, 50
THRESHOLD = 150  # Helligkeitsschwellenwert (0-255)
STOP_DELAY = 300  # 5 Minuten in Sekunden

machine_running = False
last_on_time = 0

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def is_light_on(frame):
    # In Graustufen umwandeln
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gaußschen Weichzeichner anwenden
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # ROI extrahieren
    roi = gray[ROI_Y:ROI_Y+ROI_HEIGHT, ROI_X:ROI_X+ROI_WIDTH]
    # Durchschnittliche Helligkeit berechnen
    avg_brightness = np.mean(roi)
    return avg_brightness > THRESHOLD

async def main():
    global machine_running, last_on_time
    while True:
        # Bild aufnehmen
        frame = picam2.capture_array()
        # Prüfen, ob Licht an ist
        if is_light_on(frame):
            if not machine_running:
                machine_running = True
                print("Machine is ON")
            last_on_time = time.time()
        else:
            if machine_running and (time.time() - last_on_time > STOP_DELAY):
                machine_running = False
                print("Machine stopped")
                await send_telegram_message("Washing machine stopped! Time to hang up clothes.")
        time.sleep(10)  # Überprüfe alle 10 Sekunden

if __name__ == "__main__":
    asyncio.run(main())
```

5. **Passen Sie das Skript an**:
   - Ersetzen Sie `BOT_TOKEN` und `CHAT_ID` mit Ihren Telegram-Zugangsdaten.
   - Passen Sie `ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT` an, indem Sie ein Testbild aufnehmen und es mit einem Werkzeug wie GIMP oder Python analysieren, um die Position des Anzeigelichts zu finden.
   - Justieren Sie `THRESHOLD` basierend auf Testbildern (höher für hellere Lichter).
   - Ändern Sie `STOP_DELAY` bei Bedarf.

6. **Führen Sie das Skript aus**:
   ```bash
   python3 washer_monitor.py
   ```
   - Führen Sie es im Hintergrund mit `nohup python3 washer_monitor.py &` aus oder verwenden Sie einen systemd-Service für Zuverlässigkeit.

7. **Testen und Bereitstellen**:
   - Starten Sie die Waschmaschine und überwachen Sie die Ausgabe des Skripts.
   - Überprüfen Sie die Telegram-Benachrichtigungen.
   - Sichern Sie den Pi und die Kamera in einem permanenten Setup.

---

### Andere Alternativen
1. **Vibrationssensor**:
   - **Hardware**: Verwenden Sie einen Vibrationssensor (z.B. SW-420) mit einem ESP8266 oder Raspberry Pi.
   - **Setup**: Bringen Sie den Sensor an der Waschmaschine an, um Vibrationen zu erkennen.
   - **Algorithmus**: Überwachen Sie das anhaltende Fehlen von Vibrationen (z.B. 5 Minuten), um zu erkennen, wann die Maschine stoppt.
   - **Vorteile**: Einfach, kostengünstig, unempfindlich gegenüber Umgebungslicht.
   - **Nachteile**: Kann Zyklen mit langen Pausen (z.B. Einweichen) verpassen.
   - **Codebeispiel (ESP8266)**:
     ```cpp
     #include <ESP8266WiFi.h>
     #include <UniversalTelegramBot.h>
     #define VIBRATION_PIN D5
     #define BOT_TOKEN "your_bot_token"
     #define CHAT_ID "your_chat_id"
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
         bot.sendMessage(CHAT_ID, "Washing machine stopped!", "");
       }
       delay(1000);
     }
     ```

2. **Stromsensor**:
   - **Hardware**: Verwenden Sie einen ACS712 Stromsensor mit einem ESP8266 oder Raspberry Pi.
   - **Setup**: Nicht-invasiv den Sensor um das Stromkabel der Waschmaschine klemmen.
   - **Algorithmus**: Erkennen, wenn der Strom unter einen Schwellenwert fällt (z.B. <0.5A) für 5 Minuten.
   - **Vorteile**: Genau, nicht-invasiv.
   - **Nachteile**: Erfordert elektrotechnisches Wissen, Kalibrierung für den Stromverbrauch der Maschine.

3. **Mikrofone**:
   - **Hardware**: Verwenden Sie ein Mikrofonmodul (z.B. KY-038) mit einem Raspberry Pi.
   - **Algorithmus**: Analysieren Sie die Geräuschpegel, um zu erkennen, wann der Maschinenlärm stoppt.
   - **Vorteile**: Nicht-visuell, funktioniert bei schlechten Lichtverhältnissen.
   - **Nachteile**: Empfindlich gegenüber Umgebungsgeräuschen, erfordert Signalverarbeitung.

---

### Empfehlung
- **Raspberry Pi**: Am besten für robuste Bildverarbeitung und zukünftige Erweiterbarkeit. Verwenden Sie ihn, wenn Sie mit Python vertraut sind und hohe Zuverlässigkeit bei unterschiedlichen Lichtverhältnissen wünschen.
- **Arduino (ESP32-CAM)**: Am besten für ein kostengünstiges, einfaches Setup. Ideal, wenn Sie minimalen Konfigurationsaufwand wünschen und mit grundlegender Bildverarbeitung einverstanden sind.
- **Vibrations- oder Stromsensor**: Am besten für Nicht-Kamera-Lösungen, besonders wenn das Anzeigelicht unzuverlässig ist (z.B. schwach oder verdeckt). Verwenden Sie mit ESP8266 für Einfachheit.
- **Mikrofon**: Weniger zuverlässig aufgrund von Umgebungsgeräuschen, aber als sekundärer Sensor praktikabel.

Für Ihr zweistöckiges Haus ist der Raspberry Pi oder ESP32-CAM mit Kamera ideal, da Sie sich im zweiten Stock befinden und zuverlässige Fernbenachrichtigungen via Telegram benötigen. Der Raspberry Pi bietet eine bessere Genauigkeit für die Lichterkennung, während der ESP32-CAM günstiger und einfacher zu implementieren ist. Wenn Sie einen Nicht-Kamera-Ansatz bevorzugen, ist ein Vibrationssensor mit einem ESP8266 die einfachste Alternative.

Lassen Sie mich wissen, wenn Sie eine vertiefte Betrachtung eines bestimmten Ansatzes wünschen, Hilfe beim Setup benötigen oder Code für einen alternativen Sensor möchten!