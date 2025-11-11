---
audio: false
generated: true
lang: de
layout: post
title: Installation der Arduino IDE auf Ubuntu
translated: true
type: note
---

Um die Arduino IDE auf Ubuntu Linux zu installieren, folgen Sie diesen Schritten:

1. **Arduino IDE herunterladen**:
   - Besuchen Sie die offizielle Arduino-Website unter [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software).
   - Wählen Sie im Abschnitt "Arduino IDE" die Download-Option "Linux 64 bits" (oder die passende Version für Ihr System, z.B. Linux ARM für Raspberry Pi).

2. **Die heruntergeladene Datei entpacken**:
   - Die heruntergeladene Datei ist ein komprimiertes `.tar.xz`-Archiv (z.B. `arduino-1.8.19-linux64.tar.xz`).
   - Öffnen Sie ein Terminal und navigieren Sie zum Download-Verzeichnis (z.B. `cd ~/Downloads`).
   - Extrahieren Sie die Datei mit:
     ```bash
     tar -xf arduino-*.tar.xz
     ```
   - Dies erstellt einen Ordner wie `arduino-1.8.19`.

3. **In ein geeignetes Verzeichnis verschieben (Optional)**:
   - Für einen systemweiten Zugriff verschieben Sie den extrahierten Ordner nach `/opt` (erfordert Superuser-Rechte):
     ```bash
     sudo mv arduino-1.8.19 /opt/arduino
     ```

4. **Das Installationsskript ausführen**:
   - Navigieren Sie zum Arduino-Ordner:
     ```bash
     cd /opt/arduino
     ```
   - Führen Sie das Installationsskript aus:
     ```bash
     sudo ./install.sh
     ```
   - Dies erstellt einen Desktop-Verknüpfung und richtet die notwendigen Berechtigungen ein.

5. **Ihren Benutzer zur Dialout-Gruppe hinzufügen**:
   - Um auf das Arduino-Board über den seriellen Port zugreifen zu können, müssen Sie Ihren Benutzer zur `dialout`-Gruppe hinzufügen:
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Melden Sie sich ab und wieder an, oder starten Sie den Computer neu, damit die Gruppenänderung wirksam wird.

6. **Die Arduino IDE starten**:
   - Wenn Sie das `install.sh`-Skript ausgeführt haben, können Sie die IDE über das Anwendungsmenü starten oder nach "Arduino IDE" suchen.
   - Alternativ können Sie sie direkt aus dem Terminal starten:
     ```bash
     /opt/arduino/arduino
     ```

7. **Berechtigungen für das Arduino-Board aktualisieren (falls nötig)**:
   - Wenn Sie Ihr Arduino anschließen, stellen Sie sicher, dass es erkannt wird (z.B. `/dev/ttyACM0` oder `/dev/ttyUSB0`).
   - Falls Sie Berechtigungsprobleme haben, setzen Sie die korrekten Berechtigungen:
     ```bash
     sudo chmod a+rw /dev/ttyACM0
     ```
   - Ersetzen Sie `/dev/ttyACM0` mit dem entsprechenden Port.

8. **Installation überprüfen**:
   - Schließen Sie Ihr Arduino-Board per USB an.
   - Öffnen Sie die IDE, gehen Sie zu **Werkzeuge > Board** und wählen Sie Ihr Arduino-Modell (z.B. Arduino Uno).
   - Gehen Sie zu **Werkzeuge > Port** und wählen Sie den Port (z.B. `/dev/ttyACM0`).
   - Versuchen Sie, einen Beispiel-Sketch hochzuladen (z.B. **Datei > Beispiele > 01.Basics > Blink**), um zu bestätigen, dass alles funktioniert.

**Alternative: Installation über Snap oder Flatpak**:
- **Snap**:
  ```bash
  sudo snap install arduino
  ```
- **Flatpak**:
  ```bash
  sudo flatpak install flathub cc.arduino.ArduinoIDE
  ```
- Diese Methoden vereinfachen die Installation, können aber Einschränkungen bei Berechtigungen oder der Board-Erkennung haben.

**Hinweise**:
- Stellen Sie sicher, dass Java installiert ist, da die Arduino IDE es benötigt. Installieren Sie es bei Bedarf:
  ```bash
  sudo apt update
  sudo apt install default-jre
  ```
- Für die neueste Version oder Fehlerbehebung, lesen Sie die Arduino-Foren oder die [offizielle Dokumentation](https://www.arduino.cc/en/Guide/Linux).

Wenn Sie auf Probleme stoßen, teilen Sie mir Ihre Ubuntu-Version oder die spezifische Fehlermeldung für eine maßgeschneiderte Hilfe mit!

---

Da Ihr Arduino Uno in der Arduino IDE unter Ubuntu erkannt wird und Sie ein einfaches Beispiel ohne Steckbrett oder externe Komponenten wünschen, hier ein einfacher Sketch, der die eingebaute LED auf dem Arduino Uno (an digitalem Pin 13) blinken lässt. Dies erfordert keine zusätzliche Hardware.

```cpp
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); // Setze den Pin der eingebauten LED (Pin 13) als Ausgang
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH); // Schalte die LED ein
  delay(1000);                     // Warte 1 Sekunde
  digitalWrite(LED_BUILTIN, LOW);  // Schalte die LED aus
  delay(1000);                     // Warte 1 Sekunde
}
```

### So führen Sie es aus:
1. Öffnen Sie die Arduino IDE.
2. Kopieren Sie den obigen Code und fügen Sie ihn in die IDE ein.
3. Stellen Sie sicher, dass Ihr Arduino Uno per USB verbunden und erkannt ist:
   - Gehen Sie zu **Werkzeuge > Board** und wählen Sie **Arduino Uno**.
   - Gehen Sie zu **Werkzeuge > Port** und wählen Sie den Port (z.B. `/dev/ttyACM0` oder `/dev/ttyUSB0`).
4. Klicken Sie auf die Schaltfläche **Hochladen** (Pfeil-nach-rechts-Symbol), um den Sketch zu kompilieren und auf Ihren Arduino Uno hochzuladen.
5. Sobald der Upload abgeschlossen ist, sollte die eingebaute LED (mit "L" auf dem Board gekennzeichnet) für 1 Sekunde aufleuchten, dann für 1 Sekunde ausgehen, und dies wiederholt.

### Was es tut:
- In `setup()` konfiguriert die `pinMode`-Funktion den Pin der eingebauten LED als Ausgang.
- In `loop()` schaltet die `digitalWrite`-Funktion die LED ein (`HIGH`) und aus (`LOW`), wobei `delay` für 1 Sekunde zwischen jedem Zustand pausiert und so einen Blinkeffekt erzeugt.

### Hinweise:
- Es werden keine externen Komponenten benötigt, da der Arduino Uno eine eingebaute LED an Pin 13 hat.
- Wenn die LED nicht blinkt, überprüfen Sie die Portauswahl oder stellen Sie sicher, dass das Board korrekt verbunden ist. Sie können auch den **Seriellen Monitor** öffnen (Werkzeuge > Serieller Monitor), um Fehler zu suchen, wenn Sie `Serial.begin(9600);` in `setup()` hinzufügen und Nachrichten wie `Serial.println("Blink");` in `loop()` ausgeben.
- Wenn Sie die Blinkgeschwindigkeit ändern möchten, passen Sie die `delay(1000)`-Werte an (z.B. `delay(500)` für schnelleres Blinken).

Teilen Sie mir mit, wenn Sie auf Probleme stoßen oder ein weiteres einfaches Beispiel wünschen!

---

Die Fehlermeldung weist auf ein Berechtigungsproblem beim Hochladen des Sketches auf Ihren Arduino Uno unter Ubuntu hin. Die Arduino IDE kann nicht auf den seriellen Port `/dev/ttyUSB0` zugreifen, da die Berechtigungen nicht ausreichen. So beheben Sie das Problem:

### Lösung: Berechtigungen für den seriellen Port korrigieren

1. **Fügen Sie Ihren Benutzer zur `dialout`-Gruppe hinzu**:
   - Die `dialout`-Gruppe kontrolliert typischerweise den Zugriff auf serielle Ports in Ubuntu. Fügen Sie Ihren Benutzer dieser Gruppe hinzu:
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Nachdem Sie diesen Befehl ausgeführt haben, melden Sie sich ab und wieder an, oder starten Sie Ihr System neu, damit die Änderung wirksam wird:
     ```bash
     sudo reboot
     ```

2. **Überprüfen Sie den Port**:
   - Nach dem Neustart schließen Sie Ihren Arduino Uno wieder an und öffnen die Arduino IDE.
   - Gehen Sie zu **Werkzeuge > Port** und stellen Sie sicher, dass `/dev/ttyUSB0` (oder `/dev/ttyACM0` für einige Arduino-Boards) ausgewählt ist. Wenn kein Port erscheint, überprüfen Sie die USB-Verbindung oder versuchen Sie ein anderes Kabel/einen anderen Port.

3. **Port-Berechtigungen temporär ändern (Optional)**:
   - Wenn das Problem nach dem Hinzufügen Ihres Benutzers zur `dialout`-Gruppe weiterhin besteht, können Sie die Berechtigungen für den Port manuell setzen (dies ist eine temporäre Lösung, da die Berechtigungen nach einem Neustart zurückgesetzt werden):
     ```bash
     sudo chmod a+rw /dev/ttyUSB0
     ```
   - Ersetzen Sie `/dev/ttyUSB0` durch den korrekten Port, falls dieser abweicht (z.B. `/dev/ttyACM0`).

4. **Versuchen Sie erneut hochzuladen**:
   - Klicken Sie in der Arduino IDE auf die Schaltfläche **Hochladen**, um Ihren Sketch hochzuladen (z.B. den Blink-Sketch von vorhin).
   - Wenn der Upload erfolgreich ist, sollte die eingebaute LED auf Ihrem Arduino Uno zu blinken beginnen.

### Zusätzliche Fehlerbehebung

- **Überprüfen Sie das Arduino-Board und das Kabel**:
  - Stellen Sie sicher, dass der Arduino Uno korrekt per USB verbunden ist und von Ubuntu erkannt wird. Führen Sie diesen Befehl aus, um verbundene Geräte aufzulisten:
    ```bash
    ls /dev/tty*
    ```
    Suchen Sie nach `/dev/ttyUSB0` oder `/dev/ttyACM0`, wenn das Board eingesteckt ist.
  - Versuchen Sie ein anderes USB-Kabel oder einen anderen Port, wenn das Board nicht erkannt wird.

- **Überprüfen Sie die Board- und Port-Einstellungen**:
  - Stellen Sie in der Arduino IDE sicher, dass unter **Werkzeuge > Board** die Option **Arduino Uno** ausgewählt ist.
  - Wenn `/dev/ttyUSB0` nicht erscheint, versuchen Sie es unter **Werkzeuge > Port** erneut, nachdem Sie das Board aus- und wieder eingesteckt haben.

- **Arduino IDE als Root ausführen (Temporäre Problemumgehung)**:
  - Wenn die obigen Schritte nicht funktionieren, können Sie die IDE mit Superuser-Rechten ausführen, um Berechtigungsprobleme zu umgehen (nicht für den langfristigen Gebrauch empfohlen):
    ```bash
    sudo arduino
    ```
    Ersetzen Sie `arduino` durch den Pfad zu Ihrer Arduino-IDE-Executable, falls diese nicht im System-PATH liegt (z.B. `/opt/arduino/arduino`).

- **Auf konfliktverursachende Software prüfen**:
  - Andere Software (z.B. `brltty`, ein Braille-Display-Treiber) kann mit seriellen Ports interferieren. Entfernen Sie sie, falls installiert:
    ```bash
    sudo apt remove brltty
    ```

- **Treiberprobleme**:
  - Einige Arduino-Klone verwenden den CH340/CH341-Chip, der einen Treiber benötigt. Installieren Sie ihn bei Bedarf:
    ```bash
    sudo apt install linux-modules-extra-$(uname -r)
    ```
    Schließen Sie das Board danach erneut an.

### Lösung bestätigen
Sobald die Berechtigungsprobleme behoben sind, versuchen Sie erneut, den vorherigen Blink-Sketch hochzuladen:
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Wenn Sie weiterhin Probleme haben, teilen Sie die neue Fehlermeldung mit oder führen Sie `ls -l /dev/ttyUSB0` im Terminal aus und geben Sie die Ausgabe zur weiteren Diagnose an.

---

Es scheint, dass Sie ein Problem beim Hochladen eines Sketches auf Ihren Arduino Uno mit der Arduino IDE unter Ubuntu haben. Die von Ihnen bereitgestellte Fehlermeldung lautet:

```
avrdude: ser_open(): can't open device "/dev/ttyUSB0": Permission denied
Failed uploading: uploading error: exit status 1
```

Dieser Fehler zeigt an, dass die Arduino IDE nicht die notwendigen Berechtigungen hat, um auf den seriellen Port (`/dev/ttyUSB0`) zuzugreifen, an den Ihr Arduino Uno angeschlossen ist. Dies ist ein häufiges Problem auf Linux-Systemen wie Ubuntu aufgrund der Verwaltung des seriellen Port-Zugriffs. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Behebung dieses Problems.

---

### Lösung: Problem mit den seriellen Port-Berechtigungen beheben

#### 1. Fügen Sie Ihren Benutzer zur `dialout`-Gruppe hinzu
In Ubuntu kontrolliert die `dialout`-Gruppe den Zugriff auf serielle Ports. Um das Berechtigungsproblem zu lösen, müssen Sie Ihren Benutzer dieser Gruppe hinzufügen.

- Öffnen Sie ein Terminal, indem Sie `Ctrl + Alt + T` drücken.
- Führen Sie den folgenden Befehl aus:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- Dieser Befehl fügt Ihren aktuellen Benutzer zur `dialout`-Gruppe hinzu. Die Variable `$USER` verwendet automatisch Ihren Benutzernamen.

#### 2. Melden Sie sich ab und wieder an
Damit die Gruppenänderung wirksam wird, müssen Sie sich von Ihrer aktuellen Sitzung ab- und wieder anmelden. Alternativ können Sie Ihr System neu starten.

- **Um sich ab- und wieder anzumelden:**
  - Speichern Sie alle geöffneten Arbeiten.
  - Klicken Sie auf Ihren Benutzernamen in der oberen rechten Ecke des Ubuntu-Desktops und wählen Sie "Abmelden".
  - Melden Sie sich erneut mit Ihrem Benutzernamen und Passwort an.
- **Um neu zu starten (optional):**
  - Führen Sie diesen Befehl im Terminal aus:
    ```bash
    sudo reboot
    ```
  - Warten Sie, bis Ihr System neu gestartet wurde.

#### 3. Überprüfen Sie den seriellen Port
Nachdem Sie sich wieder angemeldet haben, stellen Sie sicher, dass Ihr Arduino Uno ordnungsgemäß vom System erkannt wird.

- Schließen Sie Ihren Arduino Uno erneut an den USB-Port an.
- Öffnen Sie die Arduino IDE.
- Gehen Sie im Menü zu **Werkzeuge > Port** und prüfen Sie, ob `/dev/ttyUSB0` (oder `/dev/ttyACM0` für einige Arduino-Boards) aufgeführt und ausgewählt ist.
- Wenn der Port nicht erscheint:
  - Stecken Sie den Arduino Uno aus und wieder ein.
  - Überprüfen Sie die USB-Verbindung oder versuchen Sie ein anderes Kabel/einen anderen Port.

#### 4. Laden Sie den Sketch erneut hoch
Wählen Sie den korrekten Port aus und versuchen Sie erneut, Ihren Sketch hochzuladen:

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Setze den Pin der eingebauten LED (Pin 13) als Ausgang
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Schalte die LED ein
  delay(1000);                     // Warte 1 Sekunde
  digitalWrite(LED_BUILTIN, LOW);  // Schalte die LED aus
  delay(1000);                     // Warte 1 Sekunde
}
```

- Klicken Sie auf die Schaltfläche **Hochladen** (das Pfeil-nach-rechts-Symbol) in der Arduino IDE.
- Wenn der Upload erfolgreich ist, sollte die eingebaute LED auf Ihrem Arduino Uno zu blinken beginnen (für 1 Sekunde an, für 1 Sekunde aus).

---

### Zusätzliche Fehlerbehebung
Wenn die obigen Schritte das Problem nicht lösen, versuchen Sie diese zusätzlichen Überprüfungen:

#### Gruppenmitgliedschaft überprüfen
Stellen Sie sicher, dass Ihr Benutzer Teil der `dialout`-Gruppe ist:
- Führen Sie diesen Befehl im Terminal aus:
  ```bash
  groups $USER
  ```
- Suchen Sie in der Ausgabe nach `dialout`. Wenn es fehlt, wiederholen Sie Schritt 1 und stellen Sie sicher, dass Sie sich ab-/anmelden oder neu starten.

#### Temporäre Berechtigungsbehebung (Nicht für langfristigen Gebrauch empfohlen)
Wenn Sie eine schnelle Lösung benötigen, können Sie die Berechtigungen des seriellen Ports manuell ändern:
- Führen Sie aus:
  ```bash
  sudo chmod a+rw /dev/ttyUSB0
  ```
- Versuchen Sie dann erneut hochzuladen. Hinweis: Dies ist temporär und wird nach dem Ausstecken des Arduinos oder einem Neustart zurückgesetzt.

#### Auf konfliktverursachende Software prüfen
Einige Software, wie `brltty` (ein Braille-Display-Treiber), kann mit seriellen Ports interferieren. Um es zu entfernen:
- Führen Sie aus:
  ```bash
  sudo apt remove brltty
  ```
- Schließen Sie Ihren Arduino erneut an und versuchen Sie es noch einmal.

#### Die Arduino-Verbindung überprüfen
Stellen Sie sicher, dass Ubuntu Ihr Arduino erkennt:
- Führen Sie aus:
  ```bash
  ls /dev/tty*
  ```
- Suchen Sie nach `/dev/ttyUSB0` oder `/dev/ttyACM0`, wenn der Arduino eingesteckt ist. Wenn es fehlt, überprüfen Sie Ihr USB-Kabel oder den Port.

#### Arduino IDE als Root ausführen (Temporäre Problemumgehung)
Als letzten Ausweg können Sie die IDE mit Superuser-Rechten ausführen:
- Schließen Sie die Arduino IDE.
- Öffnen Sie ein Terminal und führen Sie aus:
  ```bash
  sudo arduino-ide
  ```
- Ersetzen Sie `arduino-ide` durch den korrekten Befehl oder Pfad, falls nötig (z.B. `/home/lzw/arduino-ide_2.3.6_Linux_64bit/arduino-ide`).
- Versuchen Sie erneut hochzuladen. Vermeiden Sie diese Methode für den regulären Gebrauch, da sie weniger sicher ist.

---

### Lösung bestätigen
Nachdem Sie diese Schritte befolgt haben, sollte Ihr Sketch erfolgreich hochgeladen werden und die LED auf Ihrem Arduino Uno wie erwartet blinken. Wenn Sie weiterhin auf Probleme stoßen, teilen Sie bitte zusätzliche Details mit, wie z.B.:
- Die Ausgabe von `ls -l /dev/ttyUSB0` (um Berechtigungen zu überprüfen).
- Alle neuen Fehlermeldungen aus der Arduino IDE.

Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!