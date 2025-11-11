---
audio: false
generated: true
lang: de
layout: post
title: Transportschicht
translated: true
type: note
---

Hier folgt ein detailliertes Tutorial, das Ihnen hilft, das Kapitel **Transport Layer** in einem Kurs wie *Computer Networks Technology (02141)* im Rahmen des chinesischen Hochschul-Selbststudien-Examens (自考) zu lernen. Dieses Tutorial konzentriert sich auf die Funktionen der Transportschicht (Ende-zu-Ende-Kommunikation, Zuverlässigkeit, Überlastkontrolle), Protokolle (TCP und UDP), Portnummern und Multiplexing sowie Fluss- und Fehlerkontrollmechanismen. Es ist umfassend, einsteigerfreundlich und auf die technische Tiefe abgestimmt, die in einem solchen Kurs erwartet wird.

---

### Schritt 1: Verstehen Sie die Rolle der Transportschicht
Die **Transportschicht** ist die vierte Schicht im OSI-Modell und die dritte im TCP/IP-Modell. Sie fungiert als Brücke zwischen den unteren Schichten (die den physischen Datentransfer handhaben) und den oberen Schichten (Anwendungen des Benutzers). Ihre Hauptaufgabe ist es, Daten effizient und zuverlässig (falls erforderlich) von einem Gerät zu einem anderen zu übertragen.

- **Warum sie wichtig ist:** Ohne die Transportschicht wüssten Anwendungen wie Webbrowser oder E-Mail-Clients nicht, wie sie Daten richtig über das Internet senden oder empfangen sollen.

---

### Schritt 2: Lernen Sie die Funktionen der Transportschicht
Die Transportschicht hat mehrere Schlüsselaufgaben. Lassen Sie uns diese aufschlüsseln:

#### 1. Ende-zu-Ende-Kommunikation
- **Was es bedeutet:** Stellt sicher, dass Daten vom Quellgerät zum Zielgerät gelangen, unabhängig von den dazwischenliegenden Netzwerken.
- **Wie es funktioniert:** Die Transportschicht des Senders kommuniziert direkt mit der Transportschicht des Empfängers und ignoriert die komplexen Details von Routern und Switches (die von der Vermittlungsschicht gehandhabt werden).
- **Analogie:** Wie das direkte Verschicken eines Briefes an einen Freund, ohne sich um die Postämter zu kümmern, die er passiert.

#### 2. Zuverlässigkeit
- **Was es bedeutet:** Garantiert, dass Daten vollständig, in der richtigen Reihenfolge und ohne Fehler ankommen (falls vom Protokoll gefordert).
- **Wie es funktioniert:** Einige Protokolle (z.B. TCP) prüfen auf verlorene oder beschädigte Daten und übertragen sie bei Bedarf erneut. Andere (z.B. UDP) verzichten der Geschwindigkeit wegen darauf.
- **Analogie:** Ein Kurier, der bestätigt, dass Ihr Paket unbeschädigt angekommen ist, im Gegensatz dazu, es einfach über den Zaun zu werfen.

#### 3. Überlastkontrolle (Congestion Control)
- **Was es bedeutet:** Verhindert, dass das Netzwerk durch zu viele Daten überlastet wird.
- **Wie es funktioniert:** Passt die Senderate der Daten basierend auf den Netzwerkbedingungen an (z.B. TCP verlangsamt sich bei hohem Datenaufkommen).
- **Analogie:** Wie das Verlangsamen Ihres Autos bei starkem Verkehr, um einen Stau zu vermeiden.

---

### Schritt 3: Erkunden Sie die Protokolle der Transportschicht
Die Transportschicht verwendet zwei Hauptprotokolle: **TCP** und **UDP**. Jedes hat einen unterschiedlichen Ansatz.

#### 1. TCP (Transmission Control Protocol) – Verbindungsorientiert
- **Was es tut:** Stellt eine zuverlässige, geordnete Zustellung von Daten sicher.
- **Schlüsselmerkmale:**
  - **Verbindungsaufbau:** Verwendet einen 3-Wege-Handshake (SYN → SYN-ACK → ACK), um eine Verbindung aufzubauen.
  - **Zuverlässigkeit:** Überträgt verlorene Pakete erneut, stellt sicher, dass es keine Duplikate oder Daten in falscher Reihenfolge gibt.
  - **Flusskontrolle:** Passt die Senderate an die Kapazität des Empfängers an.
  - **Überlastkontrolle:** Verlangsamt sich, wenn das Netzwerk ausgelastet ist.
- **Beispiele:** Webbrowsing (HTTP/HTTPS), E-Mail (SMTP), Dateiübertragung (FTP).
- **Analogie:** Ein Telefonanruf – beide Seiten bestätigen, dass sie bereit sind, sprechen in der richtigen Reihenfolge und beenden den Anruf ordnungsgemäß.

#### 2. UDP (User Datagram Protocol) – Verbindungslos
- **Was es tut:** Sendet Daten schnell, ohne Garantien.
- **Schlüsselmerkmale:**
  - **Keine Verbindung:** Sendet Pakete (Datagramme) einfach ohne vorherigen Aufbau.
  - **Keine Zuverlässigkeit:** Prüft nicht auf verlorene oder falsch geordnete Daten.
  - **Schnell:** Geringer Overhead, ideal für zeitkritische Aufgaben.
- **Beispiele:** Video-Streaming, Online-Spiele, DNS-Abfragen.
- **Analogie:** Das Verschicken von Postkarten – keine Bestätigung der Ankunft, aber es ist schnell und einfach.

**Vergleichstabelle:**

| **Merkmal**         | **TCP**               | **UDP**              |
|---------------------|-----------------------|----------------------|
| **Verbindung**      | Ja (Handshake)        | Nein                 |
| **Zuverlässigkeit** | Ja (Wiederholung)     | Nein                 |
| **Geschwindigkeit** | Langsamer (Overhead)  | Schneller (leichtgewichtig) |
| **Reihenfolge**     | Garantiert            | Nicht garantiert     |
| **Anwendungsfall**  | Web, E-Mail           | Streaming, Gaming    |

---

### Schritt 4: Verstehen Sie Portnummern und Multiplexing
Die Transportschicht verwendet **Portnummern**, um mehrere Anwendungen auf demselben Gerät zu verwalten.

#### 1. Portnummern
- **Was sie sind:** 16-Bit-Zahlen (0–65.535), die bestimmte Anwendungen oder Dienste auf einem Gerät identifizieren.
- **Typen:**
  - **Wohlbekannte Ports (0–1023):** Reserviert für gängige Dienste (z.B. 80 für HTTP, 443 für HTTPS, 25 für SMTP).
  - **Registrierte Ports (1024–49151):** Werden von bestimmten Apps verwendet.
  - **Dynamische Ports (49152–65535):** Temporär, für clientseitige Verbindungen vergeben.
- **Analogie:** Wie Wohnungsnummern in einem Gebäude – jede App erhält ihre eigene "Adresse".

#### 2. Multiplexing und Demultiplexing
- **Multiplexing (Senderseite):** Kombiniert Daten von mehreren Apps in einen Datenstrom, der über das Netzwerk gesendet wird. Jedes Paket erhält eine Portnummer, um seine App zu identifizieren.
- **Demultiplexing (Empfängerseite):** Teilt eingehende Daten auf und liefert sie basierend auf der Portnummer an die richtige App.
- **Wie es funktioniert:** Die Transportschicht fügt jedem Paket einen Header mit Quell- und Ziel-Portnummern hinzu.
- **Beispiel:** Ihr Browser (Port 50000) und Ihr E-Mail-Client (Port 50001) können gleichzeitig dieselbe Netzwerkverbindung nutzen.

**Wesentliche Erkenntnis:** IP-Adressen bringen die Daten zum richtigen Gerät; Portnummern bringen sie zur richtigen App auf diesem Gerät.

---

### Schritt 5: Vertiefen Sie sich in Fluss- und Fehlerkontrollmechanismen
Diese Mechanismen stellen sicher, dass sich Daten reibungslos und korrekt bewegen (hauptsächlich in TCP).

#### 1. Flusskontrolle (Flow Control)
- **Was es bedeutet:** Verhindert, dass der Sender den Empfänger überfordert.
- **Wie es funktioniert:**
  - **Schiebefenster (Sliding Window):** TCP verwendet ein "Fenster" von Daten, die der Sender senden kann, bevor er eine Bestätigung (ACK) benötigt. Der Empfänger teilt seine Fenstergröße mit (wie viel er verarbeiten kann).
  - **Dynamische Anpassung:** Wenn der Puffer des Empfängers voll ist, verkleinert sich das Fenster; wenn er bereit ist, vergrößert es sich.
- **Analogie:** Wie das Eingießen von Wasser in ein Glas – Sie verlangsamen sich, wenn es kurz davor ist, überzulaufen.

#### 2. Fehlerkontrolle (Error Control)
- **Was es bedeutet:** Erkennt und korrigiert Fehler in der Datenübertragung.
- **Wie es funktioniert:**
  - **Sequenznummern:** Jedes TCP-Segment hat eine Nummer, um die Reihenfolge zu verfolgen und fehlende Daten zu erkennen.
  - **Bestätigungen (ACKs):** Der Empfänger bestätigt den Empfang; fehlende ACKs lösen eine erneute Übertragung aus.
  - **Prüfsummen (Checksums):** Ein aus den Daten berechneter Wert, um Beschädigungen zu erkennen. Wenn er nicht übereinstimmt, wird das Paket erneut übertragen.
- **Analogie:** Wie das Überprüfen einer Einkaufsliste – fehlende oder beschädigte Artikel werden nachbestellt.

**Hinweis zu UDP:** UDP führt keine Fluss- oder Fehlerkontrolle durch – das überlässt es bei Bedarf der Anwendung.

---

### Schritt 6: Lerntipps für 自考 (Selbststudien-Examen)
1. **Merken Sie sich Schlüsselkonzepte:**
   - Funktionen: Ende-zu-Ende, Zuverlässigkeit, Überlastkontrolle.
   - Protokolle: TCP (zuverlässig), UDP (schnell).
   - Ports: Wohlbekannt (z.B. 80, 443), dynamisch.
2. **Visualisieren Sie:**
   - Zeichnen Sie den 3-Wege-Handshake von TCP (SYN → SYN-ACK → ACK).
   - Skizzieren Sie Multiplexing: mehrere Apps → Ports → ein Netzwerkstrom.
3. **Übungsfragen:**
   - Was ist der Unterschied zwischen TCP und UDP?
   - Wie verwendet die Transportschicht Portnummern?
   - Erklären Sie, wie TCP Zuverlässigkeit sicherstellt.
4. **Verwenden Sie Eselsbrücken:** "TCP = Total Control Protocol" (zuverlässig); "UDP = Ultra Datagram Protocol" (schnell).
5. **Beispiele aus der Praxis:** Beziehen Sie es auf Browsen (TCP) vs. Streaming (UDP).

---

### Schritt 7: Testen Sie Ihr Verständnis
Beantworten Sie diese Fragen, um Ihr Verständnis zu überprüfen:
1. Welches Protokoll verwendet einen 3-Wege-Handshake? (TCP)
2. Welche Rolle spielen Portnummern beim Multiplexing? (Apps identifizieren)
3. Wie behandelt TCP ein verlorenes Paket? (Überträgt es erneut mithilfe von Sequenznummern und ACKs)
4. Warum könnte UDP TCP vorgezogen werden? (Geschwindigkeit, geringer Overhead)

---

### Zusätzliche Ressourcen
- **Bücher:** "Computer Networking: A Top-Down Approach" (Kurose & Ross) – Kapitel zur Transportschicht.
- **Online:** Ciscos Tutorials zur Transportschicht, YouTube (z.B. "PowerCert" zu TCP vs. UDP).
- **Werkzeuge:** Verwenden Sie Wireshark, um TCP/UDP-Pakete mitzuschneiden und Portnummern in Aktion zu sehen.

---

Dieses Tutorial behandelt die Transportschicht im Detail. Studieren Sie jeden Abschnitt, üben Sie das Erklären von Konzepten (großartig für die 自考 mündliche Vorbereitung) und besuchen Sie schwierige Bereiche wie Flusskontrolle oder Multiplexing erneut. Wenn Sie mehr Beispiele oder Erklärungen benötigen, fragen Sie einfach! Viel Erfolg bei Ihrem Studium!