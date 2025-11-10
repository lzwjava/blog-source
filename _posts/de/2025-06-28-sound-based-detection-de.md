---
audio: false
generated: true
lang: de
layout: post
title: Geräuschbasierte Erkennung für Maytag Waschmaschinen
translated: true
type: note
---

Die Verwendung von Schall zur Erkennung, wann Ihre Maytag MHW8630HW Waschmaschine stoppt, ist eine praktikable Alternative zum kamera-basierten Ansatz. Indem Sie einen Schallsensor in der Nähe der Waschmaschine platzieren, können Sie den während des Betriebs erzeugten Lärm (z.B. Motorbrummen, Wasserfluss oder Trommeldrehung) überwachen und erkennen, wann dieser stoppt, was das Ende des Waschzyklus anzeigt. Im Folgenden werde ich erläutern, wie Sie das vorherige Projekt anpassen können, um einen Schallsensor anstelle einer Kamera zu verwenden. Der Fokus liegt auf der Hardware, dem Algorithmus und den Code-Änderungen, während das Telegram-Benachrichtigungssystem beibehalten wird.

---

### Tech Stack
#### Hardware
1. **Arduino Board**:
   - **ESP32-CAM** (immer noch verwendbar) – Behält Wi-Fi für die Telegram-Integration bei, obwohl die Kamera nicht benötigt wird.
   - Alternative: **ESP8266 NodeMCU** oder **Arduino Uno** mit einem ESP8266-Modul für Wi-Fi (einfacher, wenn Sie die Kamera nicht benötigen).
2. **Schallsensor**:
   - **KY-038 Mikrofon Sound Sensor** oder ähnlich – Günstig, erkennt Schallpegel über einen analogen Ausgang.
   - Alternative: **MAX9814 Electret Microphone Amplifier** – Empfindlicher, mit einstellbarer Verstärkung für eine bessere Erkennung.
3. **Stromversorgung**:
   - 5V USB-Netzteil oder Akku-Pack für das ESP32 oder ein anderes Board.
4. **Montage**:
   - Platzieren Sie den Schallsensor nahe der Waschmaschine (z.B. an der Seite oder Oberseite befestigt), wo er Betriebsgeräusche erfassen kann, aber direkter Wassereinwirkung ausweicht.
   - Verwenden Sie ein kleines Gehäuse, um den Sensor und das Board zu schützen.
5. **Wi-Fi Router**:
   - Für Internetkonnektivität zum Senden von Telegram-Benachrichtigungen.

#### Software
- **Arduino IDE**: Zum Programmieren des ESP32 oder eines anderen Boards.
- **Bibliotheken**:
  - **Universal Arduino Telegram Bot Library** von Brian Lough – Für die Telegram-Integration.
  - **ArduinoJson** – Für die Verarbeitung von JSON-Daten in der Telegram-API-Kommunikation.
- **Telegram Bot**: Wie zuvor, verwenden Sie BotFather, um ein Bot-Token und eine Chat-ID zu erhalten.
- **Programmiersprache**: C++ (Arduino Sketch).

---

### Algorithmus zur Erkennung des Waschmaschinenstatus mit Schall
Der Schallsensor erkennt den von der Waschmaschine erzeugten Geräuschpegel. Wenn die Maschine läuft, erzeugt sie konstante Geräusche (z.B. Motor, Wasser oder Trommel). Wenn sie stoppt, fällt der Geräuschpegel signifikant ab. Der Algorithmus verarbeitet diese Geräuschpegel, um den Status der Maschine zu bestimmen.

#### Erkennungsalgorithmus
1. **Schallabtastung**:
   - Lesen Sie kontinuierlich den analogen Ausgang des Schallsensors, um die Geräuschpegel zu messen.
2. **Signalverarbeitung**:
   - **Mittelwertbildung**: Berechnen Sie den durchschnittlichen Geräuschpegel über ein kurzes Zeitfenster (z.B. 1-2 Sekunden), um vorübergehende Geräusche (z.B. eine zuschlagende Tür) zu glätten.
   - **Schwellwertvergleich**: Vergleichen Sie den durchschnittlichen Geräuschpegel mit einem vordefinierten Schwellwert. Ein hoher Pegel zeigt an, dass die Maschine läuft, während ein niedriger Pegel darauf hindeutet, dass sie gestoppt ist.
3. **Zustandsautomat**:
   - Verfolgen Sie den Zustand der Maschine (EIN oder AUS) basierend auf den Geräuschpegeln.
   - Wenn der Geräuschpegel den Schwellwert für mehrere Zyklen überschreitet, gehen Sie davon aus, dass die Maschine läuft.
   - Wenn der Geräuschpegel unter den Schwellwert fällt und für eine festgelegte Zeit (z.B. 5 Minuten) niedrig bleibt, gehen Sie davon aus, dass der Waschzyklus abgeschlossen ist.
4. **Entprellung**:
   - Implementieren Sie eine Verzögerung (z.B. 5 Minuten), um zu bestätigen, dass die Maschine gestoppt hat, und um falsche Benachrichtigungen während ruhiger Phasen (z.B. Einweichen oder Pausen im Zyklus) zu vermeiden.
5. **Benachrichtigung**:
   - Wenn bestätigt ist, dass die Maschine gestoppt hat, senden Sie eine Telegram-Nachricht (z.B. "Waschmaschine gestoppt! Zeit, die Wäsche aufzuhängen.").

#### Warum Schallerfassung?
- Die Schallerfassung ist einfacher als Bildverarbeitung, da sie keine komplexen Algorithmen oder hohe Rechenressourcen erfordert.
- Sie ist weniger empfindlich gegenüber Änderungen der Umgebungsbeleuchtung im Vergleich zur kamerabasierten Erkennung.
- Allerdings kann sie durch Hintergrundgeräusche (z.B. ein lauter Fernseher) beeinflusst werden, daher sind Platzierung und Schwellwertabstimmung entscheidend.

---

### Implementierungsleitfaden
#### Schritt 1: Richten Sie den Telegram-Bot ein
- Befolgen Sie die gleichen Schritte wie in der ursprünglichen Anleitung:
  - Erstellen Sie einen Bot mit **@BotFather**, um ein **Bot-Token** zu erhalten.
  - Holen Sie sich Ihre **Chat-ID** mit **@GetIDsBot** oder durch Überprüfen eingehender Nachrichten.
  - Stellen Sie sicher, dass Telegram auf Ihrem Telefon eingerichtet ist, um Benachrichtigungen zu empfangen.

#### Schritt 2: Hardware-Einrichtung
1. **Wählen Sie einen Schallsensor**:
   - **KY-038**: Bietet einen analogen Ausgang (0-1023 für den 10-Bit-ADC des ESP32), der proportional zur Schallintensität ist. Es gibt auch einen digitalen Ausgang, aber analog ist besser für nuancierte Erkennung.
   - **MAX9814**: Empfindlicher, mit einstellbarer Verstärkung über ein Potentiometer. An einen analogen Pin anschließen.
2. **Schließen Sie den Schallsensor an**:
   - Für KY-038:
     - **VCC** an 5V (oder 3.3V, je nach Board).
     - **GND** an GND.
     - **Analog Out (A0)** an einen analogen Pin am ESP32 (z.B. GPIO 4).
   - Für MAX9814:
     - Ähnliche Anschlüsse, aber passen Sie die Verstärkung mit dem onboard Potentiometer für optimale Empfindlichkeit an.
3. **Positionieren Sie den Sensor**:
   - Platzieren Sie den Sensor in der Nähe der Waschmaschine (z.B. an der Seite oder Oberseite), wo er Motor- oder Trommelgeräusche erfassen kann. Vermeiden Sie Bereiche mit Wassereinwirkung.
   - Testen Sie die Platzierung, indem Sie die Geräuschpegel während eines Waschzyklus überwachen (verwenden Sie den Serial Monitor zum Protokollieren der Werte).
4. **Stromversorgung des Boards**:
   - Schließen Sie ein 5V-USB-Netzteil oder einen Akku-Pack an den ESP32 oder ein anderes Board an.
   - Stellen Sie eine stabile Stromversorgung sicher, da die Wi-Fi-Kommunikation eine konsistente Spannung erfordert.
5. **Montage**:
   - Verwenden Sie ein kleines Gehäuse oder Klebeband, um den Sensor und das Board zu sichern, und stellen Sie sicher, dass das Mikrofon frei ist, um Schall aufnehmen zu können.

#### Schritt 3: Software-Einrichtung
- **Arduino IDE**: Installieren Sie wie in der ursprünglichen Anleitung beschrieben.
- **ESP32 Board Support**: Fügen Sie das ESP32-Board-Paket über den Boards Manager hinzu (gleiche URL wie zuvor).
- **Bibliotheken**:
  - Installieren Sie **Universal Arduino Telegram Bot Library** und **ArduinoJson** wie beschrieben.
- **Wi-Fi**: Stellen Sie sicher, dass das Board eine Verbindung zu Ihrem 2.4GHz Wi-Fi-Netzwerk herstellen kann.

#### Schritt 4: Schreiben Sie den Arduino-Code
Unten finden Sie einen Beispiel-Arduino-Sketch für den ESP32 (oder ESP8266), um Geräuschpegel zu erkennen und Telegram-Benachrichtigungen zu senden. Dies setzt einen KY-038 Schallsensor an GPIO 4 voraus.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Wi-Fi Zugangsdaten
#define WIFI_SSID "ihre_wifi_ssid"
#define WIFI_PASSWORD "ihre_wifi_password"

// Telegram Bot Zugangsdaten
#define BOT_TOKEN "ihr_bot_token"
#define CHAT_ID "ihre_chat_id"

// Schallsensor Pin
#define SOUND_PIN 4 // GPIO 4 für analogen Eingang

// Schallerfassungsparameter
#define SOUND_THRESHOLD 300 // Anpassen basierend auf Tests (0-1023)
#define SAMPLE_WINDOW 2000 // 2 Sekunden für Mittelwertbildung
#define STOP_DELAY 300000 // 5 Minuten in Millisekunden

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // Verbindung zu Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Telegram Client konfigurieren
  client.setInsecure(); // Der Einfachheit halber; für Produktion ordentliche SSL in Betracht ziehen

  // Schallsensor Pin einrichten
  pinMode(SOUND_PIN, INPUT);
}

void loop() {
  // Geräuschpegel über ein Fenster abtasten
  unsigned long startMillis = millis();
  uint32_t totalSound = 0;
  uint16_t sampleCount = 0;

  while (millis() - startMillis < SAMPLE_WINDOW) {
    totalSound += analogRead(SOUND_PIN);
    sampleCount++;
    delay(10); // Kleine Verzögerung zwischen den Abtastungen
  }

  float avgSound = sampleCount > 0 ? (float)totalSound / sampleCount : 0;
  Serial.print("Durchschnittlicher Geräuschpegel: ");
  Serial.println(avgSound);

  // Zustandsautomat
  if (avgSound > SOUND_THRESHOLD) {
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

  delay(10000); // Überprüfung alle 10 Sekunden
}
```

#### Schritt 5: Passen Sie den Code an
1. **Aktualisieren Sie die Zugangsdaten**:
   - Ersetzen Sie `ihre_wifi_ssid`, `ihre_wifi_password`, `ihr_bot_token` und `ihre_chat_id` mit Ihren tatsächlichen Werten.
2. **Stimmen Sie `SOUND_THRESHOLD` ab**:
   - Lassen Sie die Waschmaschine laufen und überwachen Sie die Geräuschpegel über den Serial Monitor (`Serial.println(analogRead(SOUND_PIN));`).
   - Setzen Sie `SOUND_THRESHOLD` auf einen Wert über dem Umgebungsgeräusch, aber unter dem Betriebsgeräusch der Maschine (z.B. 200-500, abhängig von Ihrem Setup).
3. **Passen Sie `SAMPLE_WINDOW` an**:
   - Ein 2-Sekunden-Fenster (`2000` ms) glättet vorübergehende Geräusche. Erhöhen Sie es, wenn Hintergrundgeräusche falsche Messwerte verursachen.
4. **Passen Sie `STOP_DELAY` an**:
   - Setzen Sie es auf `300000` (5 Minuten), um falsche Benachrichtigungen während ruhiger Phasen wie dem Einweichen zu vermeiden.

#### Schritt 6: Testen und Bereitstellen
1. **Laden Sie den Code hoch**:
   - Verbinden Sie den ESP32 über einen USB-zu-Serial-Adapter mit Ihrem Computer.
   - Wählen Sie **ESP32 Wrover Module** (oder **NodeMCU** für ESP8266) in der Arduino IDE aus und laden Sie den Sketch hoch.
2. **Testen Sie das System**:
   - Starten Sie die Waschmaschine und überwachen Sie den Serial Monitor auf Geräuschpegel und Zustandsänderungen.
   - Überprüfen Sie die Telegram-Benachrichtigungen, wenn die Maschine stoppt.
3. **Feinabstimmung**:
   - Passen Sie `SOUND_THRESHOLD` oder `STOP_DELAY` an, wenn falsche Positive/Negative auftreten.
   - Testen Sie unter verschiedenen Bedingungen (z.B. mit Hintergrundgeräuschen), um die Zuverlässigkeit sicherzustellen.
4. **Dauerhafte Installation**:
   - Befestigen Sie den Sensor und das Board in einem Gehäuse in der Nähe der Maschine, und stellen Sie sicher, dass das Mikrofon frei, aber vor Wasser geschützt ist.

---

### Vorteile der Schallerfassung
- **Einfachere Verarbeitung**: Keine Bildverarbeitung, reduziert die Rechenlast auf dem ESP32.
- **Kostengünstig**: Schallsensoren wie der KY-038 sind preiswert (oft unter 5 $).
- **Nicht-invasiv**: Es muss nichts direkt an der Kontrollleuchte der Maschine befestigt werden.

### Herausforderungen und Gegenmaßnahmen
- **Hintergrundgeräusche**: Haushaltsgeräusche (z.B. Fernseher, Gespräche) können stören. Gegenmaßnahmen:
  - Platzieren Sie den Sensor nahe am Motor oder der Trommel der Maschine.
  - Stimmen Sie `SOUND_THRESHOLD` ab, um Umgebungsgeräusche zu ignorieren.
  - Verwenden Sie ein Richtmikrofon oder passen Sie die Verstärkung am MAX9814 an.
- **Ruhige Phasen**: Einige Waschzyklen haben Pausen (z.B. Einweichen). Der `STOP_DELAY` stellt sicher, dass Benachrichtigungen nur nach längerer Stille gesendet werden.
- **Wassereinwirkung**: Stellen Sie sicher, dass der Sensor in einem wasserdichten Gehäuse untergebracht ist, da Waschmaschinen Spritzer oder Feuchtigkeit verursachen können.

### Optionale Verbesserungen
- **Frequenzanalyse**: Wenn Hintergrundgeräusche ein anhaltendes Problem sind, analysieren Sie Schallfrequenzen (z.B. Motorbrummen bei 50-200 Hz) mit einer Fast Fourier Transform (FFT) Bibliothek wie `arduinoFFT`. Dies erfordert mehr Rechenleistung und ist auf einem einfachen ESP32 ohne Optimierung möglicherweise nicht machbar.
- **Duale Sensoren**: Kombinieren Sie Schall- und Vibrationssensoren (z.B. SW-420) für Redundanz. Wenn beide anzeigen, dass die Maschine aus ist, erhöht sich die Zuverlässigkeit der Erkennung.
- **Akkubetrieb**: Für Portabilität verwenden Sie einen wiederaufladbaren LiPo-Akku mit einem Lademodul (z.B. TP4056) anstelle eines USB-Adapters.

---

### Fehlerbehebung
- **Keine Schallerfassung**: Überprüfen Sie die Sensorverkabelung, testen Sie mit dem Serial Monitor und stellen Sie sicher, dass der Sensor nahe der Geräuschquelle der Maschine ist.
- **Falsche Benachrichtigungen**: Erhöhen Sie `STOP_DELAY` oder passen Sie `SOUND_THRESHOLD` an, um Hintergrundgeräusche oder Zykluspausen herauszufiltern.
- **Wi-Fi-Probleme**: Überprüfen Sie die 2.4GHz Wi-Fi-Zugangsdaten und die Signalstärke in der Nähe der Maschine.
- **Keine Telegram-Nachrichten**: Bestätigen Sie das Bot-Token und die Chat-ID, überprüfen Sie den Serial Monitor auf Fehler.

Dieser schallbasierte Ansatz ist einfacher und robuster bei unterschiedlichen Lichtverhältnissen im Vergleich zur kamerabasierten Methode, was ihn ideal für einen Waschmaschinenmonitor macht. Lassen Sie mich wissen, wenn Sie Hilfe bei bestimmten Schritten, der Sensor-Kalibrierung oder der Integration zusätzlicher Funktionen benötigen!