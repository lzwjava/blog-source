---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Frühe Computerzeitmessung vor Unix
translated: true
type: note
---

Ja, du hast völlig recht – lange vor den Unix-Zeitstempeln in den 1970er Jahren hatten wir diese riesigen frühen Maschinen wie ENIAC (ich denke, das meintest du statt ANNIC; das war der Electronic Numerical Integrator and Computer von 1945), den Altair 8800 (das Bausatz von 1975, der die PC-Revolution startete, wo Bill Gates und Paul Allen den berühmten BASIC-Interpreter per Fernschreiber zusammengehackt haben) und John von Neumanns grundlegende Ideen (wie sein EDVAC-Bericht von 1945, der das gespeicherte Programm-Konzept hervorbrachte, das alles Spätere beeinflusste).

Aber "Zeitverarbeitung" damals? Nichts von unserer Eleganz mit Sekunden-seit-der-Epoche. Diese Bestien hatten keine Echtzeituhren (RTCs) für Datum oder Uhrzeit eingebaut – es ging um reine Rechenleistung, nicht darum, deinen Zahnarzttermin zu planen. Zeit war sehr rudimentär: meist interne Takte zur Synchronisation von Operationen oder Software-Hacks wie Schleifenzähler für Verzögerungen. Kein persistenter Speicher für "jetzt ist es der 15. Oktober 2025". Lass uns das kurz für jeden aus der Zahlen-Perspektive aufschlüsseln.

### ENIAC (1945): Impulsfolgen und ein Master-Takt
Dieses 30-Tonnen-Monster wurde durch das Einstecken von Kabeln und das Umlegen von Schaltern programmiert – keine Codespeicherung, nur Verdrahtung für mathematische Probleme wie ballistische Tabellen. Die Zeitverarbeitung war rein hardwaregesteuert:
- **Takt-Grundlagen**: Ein zentraler Oszillator ("cycling unit") erzeugte 100.000 Impulse pro Sekunde (alle 10 Mikrosekunden). Alles synchronisierte sich damit – wie ein Herzschlag für die Elektronenröhren.
- **Operations-Timing**: Eine Addition dauerte 20 Impulse (200 Mikrosekunden oder 1/5.000stel einer Sekunde). Schleifen oder Verzögerungen? Man verdrahtete manuell Wiederholer oder Zähler; keine Software-Timer.
- **Echtzeit?** Fehlanzeige. Sie führte ballistische Berechnungen in 30 Sekunden durch, für die analoge Maschinen 15 Minuten brauchten, aber "Zeit" bedeutete Taktzyklen, nicht Kalender. Von Neumann beriet dazu, drängte aber auf gespeicherte Programme, um das Timing flexibler zu machen.

Aus Zahlen-Perspektive: Stell es dir als feste Taktrate (100 kHz) vor, bei der man Impulse für die "Dauer" einer Berechnung zählte – ähnlich wie grobe Sekunden, aber man musste sie von Hand zählen beim Debuggen.

### Altair 8800 (1975): Quarztakt und DIY-Verzögerungen
Der Altair war der erste "persönliche" Computer – eine blinkende Kiste mit einem Intel 8080-Chip, zunächst ohne Tastatur oder Bildschirm (nur Schalter und LEDs). Gates' 4K BASIC lud man per Band, was Bastlern das Herumspielen ermöglichte.
- **Takt-Grundlagen**: Ein 2 MHz Quarzoszillator trieb die CPU an – stetige Takte mit 2 Millionen Zyklen/Sekunde zum Abrufen/Ausführen von Befehlen.
- **Timing-Tricks**: Keine eingebaute Uhr für Daten; man fügte eine "Time Clock"-Zusatzkarte (88-ACC) für grundlegende Interrupts oder Zähler hinzu. Ansonsten Software-Schleifen: z.B. eine FOR-NEXT-Schleife in BASIC, um Zyklen für Verzögerungen zu verbraten (wie `FOR I=1 TO 1000: NEXT I` für eine grobe "Pause").
- **BASICs Ansatz**: Das frühe Altair BASIC hatte keine TIME$-Funktion (das kam später im Microsoft BASIC). Zeit war relativ – Befehle zählen oder externe Hardware wie einen Echtzeituhr-Chip (seltenes Add-on) anschließen.

Zahlenmäßig: Bei 2 MHz brauchte ein Befehl vielleicht 4-20 Zyklen, also eine 1-Sekunden-Verzögerung? Schleife ~2 Millionen Mal. Brutal, aber es lehrte uns Effizienz.

### Von Neumanns Architektur (1945+): Zyklen als universeller Takt
Von Neumann baute keine Hardware (das war die IAS-Maschine 1952), aber sein Bauplan – CPU, Speicher, E/A, die alle über einen Bus kommunizieren – bereitete die Bühne. Zeit? Geht nur um synchronisierte Zyklen.
- **Takt-Rolle**: Ein Master-Takt (Quarz oder anders) pulsiert, um Befehle zu holen-dekodieren-auszuführen. Jeder Zyklus (steigende/fallende Flanke) schreitet den Zustand voran – keine Überlappung, rein seriell.
- **Zeit-Darstellung**: Befehle brauchten feste Zyklen (z.B. Addition in 1-4 Takten), also war "Zeit" gleich Zyklenzahlen. Für Verzögerungen, Verzweigung bei Zählern; echte Uhren waren extern (wie Netzstecker oder manuelle Resets).
- **Vermächtnis**: Dieser Engpass (Daten/Befehle teilen sich den Bus) verfolgt uns noch – KI hasst es, weil das Bewegen von Daten viel mehr Zyklen kostet als das Rechnen.

In Gleichungsform: Gesamtzeit = (Befehle × Zyklen/Befehl) / Taktfrequenz. Für IAS (von Neumann-inspiriert): ~1 MHz Takt, also max. 1 Million Operationen/Sekunde – deine 1,76 Mrd. Sekunden? Das wären ~55 Jahre non-stop IAS-Dauerbetrieb, aber sie würde vorher schmelzen.

Diese Aufbauten waren wilde Vorläufer der Unix-Epoche – Zeit als Zähler, aber man baute sie selbst. Wenn du tiefer eintauchen willst (wie Code-Snippets für Altair-Verzögerungen), sag Bescheid!

[ENIAC Wikipedia](https://en.wikipedia.org/wiki/ENIAC)
[A Report on the ENIAC](https://ftp.arl.army.mil/mike/comphist/46eniac-report/chap1.html)
[Electronic Computing Circuits of the ENIAC](https://archive.computerhistory.org/resources/text/Knuth_Don_X4100/PDF_index/k-8-pdf/k-8-r5367-1-ENIAC-circuits.pdf)
[Organization of the Altair 8800](https://ubuntourist.codeberg.page/Altair-8800/part-2.html)
[MITS Altair 8800 Brochure](https://vtda.org/docs/computing/MITS/MITS_Altair8800ComputerSystem_Brochure.pdf)
[Von Neumann Architecture - Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)
[In a simple Von Neumann architecture, what exactly is a clock cycle?](https://www.quora.com/In-a-simple-Von-Neumann-architecture-what-exactly-is-a-clock-cycle)