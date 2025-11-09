---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-sonnet-4
title: Xdotool Befehlszeilen-Automatisierungsleitfaden
translated: true
type: note
---

## Was ist xdotool?

xdotool ist ein Befehlszeilen-Automatisierungstool für X11 (Linux-Desktopumgebungen), das Ihnen erlaubt:
- Mausbewegungen und Klicks zu steuern
- Tastatureingaben an Anwendungen zu senden
- Fenster zu manipulieren (verschieben, vergrößern, fokussieren)
- Nach Fenstern anhand verschiedener Kriterien zu suchen
- Desktop-Interaktionen programmatisch zu automatisieren

## Installation

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# Aus dem Quellcode
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## Kernbefehle

### Fensterinformationsbefehle

#### `getactivewindow`
Ermittelt die Fenster-ID des aktuell aktiven/fokussierten Fensters.
```bash
xdotool getactivewindow
# Ausgabe: 52428807 (Fenster-ID)

# Fenstertitel des aktiven Fensters abrufen
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
Ähnlich wie getactivewindow, kann sich aber in einigen Fenstermanagern anders verhalten.
```bash
xdotool getwindowfocus
```

#### `getwindowname`
Ermittelt den Titel/Namen eines Fensters.
```bash
# Namen des aktiven Fensters abrufen
xdotool getactivewindow getwindowname

# Namen einer bestimmten Fenster-ID abrufen
xdotool getwindowname 52428807
```

#### `getwindowpid`
Ermittelt die Prozess-ID (PID), die einem Fenster zugeordnet ist.
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
Ermittelt Positions- und Größeninformationen eines Fensters.
```bash
xdotool getactivewindow getwindowgeometry
# Ausgabe: Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
Ermittelt die Bildschirm/Display-Abmessungen.
```bash
xdotool getdisplaygeometry
# Ausgabe: 1920x1080
```

### Fenstersuche und -auswahl

#### `search`
Nach Fenstern anhand verschiedener Kriterien suchen.
```bash
# Nach Fensternamen/-titel suchen
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# Nach Klassenname suchen
xdotool search --class "firefox"

# Groß-/Kleinschreibung ignorieren
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# Häufige Suchoptionen:
# --name: Fenstertitel durchsuchen
# --class: Fensterklassennamen durchsuchen
# --classname: Fensterklasseninstanznamen durchsuchen
# --onlyvisible: Nur sichtbare Fenster
# --maxdepth N: Suchtiefe begrenzen
# --limit N: Anzahl der Ergebnisse begrenzen
# --desktop N: Bestimmten Desktop/Arbeitsbereich durchsuchen
```

#### `selectwindow`
Interaktive Fensterauswahl (durch Klick auswählen).
```bash
xdotool selectwindow
# Auf ein beliebiges Fenster klicken, um dessen ID zu erhalten
```

### Maussteuerung

#### `click`
Simuliert Mausklicks.
```bash
# Linksklick an aktueller Position
xdotool click 1

# Rechtsklick
xdotool click 3

# Mittelklick
xdotool click 2

# Doppelklick
xdotool click --repeat 2 1

# Klick an bestimmten Koordinaten
xdotool mousemove 500 300 click 1

# Klick mit Verzögerung
xdotool click --delay 500 1
```

#### `getmouselocation`
Ermittelt die aktuelle Mauszeigerposition.
```bash
xdotool getmouselocation
# Ausgabe: x:500 y:300 screen:0 window:52428807

# Nur Koordinaten abrufen
xdotool getmouselocation --shell
# Ausgabe: X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### Mausbewegung
```bash
# Maus an absolute Position bewegen
xdotool mousemove 500 300

# Maus relativ zur aktuellen Position bewegen
xdotool mousemove_relative 10 -20

# Bewegen und klicken in einem Befehl
xdotool mousemove 500 300 click 1
```

### Tastatureingabe

#### `key`
Sendet Tastatureingaben an das aktive Fenster.
```bash
# Einzelne Taste senden
xdotool key Return
xdotool key Escape
xdotool key Tab

# Tastenkombinationen senden
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# Mehrere Tasten in Sequenz senden
xdotool key ctrl+l type "https://google.com" key Return

# Häufige Tastennamen:
# - Buchstaben: a, b, c, ... (Kleinbuchstaben)
# - Zahlen: 1, 2, 3, ...
# - Spezial: Return, Escape, Tab, space, BackSpace, Delete
# - Funktion: F1, F2, ... F12
# - Modifikatoren: ctrl, alt, shift, super (Windows-Taste)
# - Pfeile: Up, Down, Left, Right
```

#### Texteingabe
```bash
# Text eingeben (simuliert Eingabe jedes Zeichens)
xdotool type "Hello World"

# Text mit Verzögerung zwischen Zeichen eingeben
xdotool type --delay 100 "Slow typing"

# Verzögerung für schnelle Eingabe löschen
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### Fenstermanipulation

```bash
# Fenster fokussieren/aktivieren
xdotool windowactivate WINDOW_ID

# Fenster minimieren
xdotool windowminimize WINDOW_ID

# Fenster maximieren
xdotool windowmaximize WINDOW_ID

# Fenster schließen
xdotool windowclose WINDOW_ID

# Fenster an Position verschieben
xdotool windowmove WINDOW_ID 100 50

# Fenstergröße ändern
xdotool windowsize WINDOW_ID 800 600

# Fenster auf bestimmten Desktop verschieben
xdotool set_desktop_for_window WINDOW_ID 2

# Fenster in den Vordergrund bringen
xdotool windowraise WINDOW_ID

# Fenster anzeigen (map)
xdotool windowmap WINDOW_ID

# Fenster ausblenden (unmap)
xdotool windowunmap WINDOW_ID
```

### Erweiterte Funktionen

#### `behave`
Fensterereignis-Verhalten (Trigger) einrichten.
```bash
# Befehl ausführen, wenn Fenster Fokus erhält
xdotool behave WINDOW_ID focus exec echo "Window focused"

# Befehl ausführen, wenn Fenster erstellt wird
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# Verfügbare Ereignisse: focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
Aktionen auslösen, wenn Maus Bildschirmränder erreicht.
```bash
# Befehl ausführen, wenn Maus linken Rand erreicht
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# Verfügbare Ränder: left, right, top, bottom
```

## Praktische Beispiele

### Grundlegende Automatisierungsskripte

#### Terminal öffnen und Befehl ausführen
```bash
#!/bin/bash
# Terminal öffnen und ls-Befehl ausführen
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### Screenshot des aktiven Fensters
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### Bestimmte Anwendung fokussieren
```bash
#!/bin/bash
# Firefox fokussieren oder öffnen, falls nicht läuft
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### Fensterverwaltungsskripte

#### Fenster nebeneinander anordnen
```bash
#!/bin/bash
# Bildschirmgeometrie abrufen
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# Zwei neueste Fenster abrufen
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# Erstes Fenster links positionieren
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# Zweites Fenster rechts positionieren
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### Aktives Fenster zentrieren
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### Anwendungsspezifische Automatisierung

#### Browser-Automatisierung
```bash
#!/bin/bash
# Neuen Tab öffnen und navigieren
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### Texteditor-Automatisierung
```bash
#!/bin/bash
# Alles auswählen und in Zwischenablage kopieren
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## Tipps und Best Practices

### Timing und Verzögerungen
```bash
# Verzögerungen für langsame Anwendungen hinzufügen
xdotool key ctrl+alt+t
sleep 2  # Warten bis Terminal geöffnet ist
xdotool type "echo hello"

# Eingebaute xdotool-Verzögerungen nutzen
xdotool key --delay 100 ctrl+alt+t
```

### Fehlerbehandlung
```bash
#!/bin/bash
# Prüfen, ob Fenster existiert, bevor gehandelt wird
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### Arbeiten mit mehreren Fenstern
```bash
#!/bin/bash
# Auf alle Fenster einer bestimmten Anwendung wirken
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # Aktualisieren
    sleep 0.5
done
```

### Debugging
```bash
# Ausführliche Ausgabe aktivieren
xdotool --verbose key Return

# Detaillierte Fensterinformationen abrufen
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## Häufige Anwendungsfälle

1. **Fensterverwaltung**: Fenster programmatisch fokussieren, verschieben, vergrößern
2. **Anwendungstests**: GUI-Testszenarien automatisieren
3. **Präsentationstools**: Foliennavigation und Fensterwechsel automatisieren
4. **Gaming-Makros**: Wiederholende Spielaufgaben automatisieren
5. **Barrierefreiheit**: Benutzerdefinierte Eingabemethoden für Benutzer mit Behinderungen erstellen
6. **Systemadministration**: GUI-basierte Admin-Aufgaben automatisieren
7. **Entwicklungstools**: Integration mit IDEs und Entwicklungs-Workflows

## Problembehandlung

### Häufige Probleme

- **Befehle funktionieren nicht**: Sicherstellen, dass X11 läuft (nicht Wayland)
- **Berechtigungsprobleme**: Einige Operationen erfordern möglicherweise entsprechende Benutzerberechtigungen
- **Fenster nicht gefunden**: `xdotool search` verwenden, um zu überprüfen, ob Fenster existiert und sichtbar ist
- **Timing-Probleme**: Angemessene Verzögerungen zwischen Befehlen hinzufügen
- **Sonderzeichen**: Korrekte Escaping für Sonderzeichen in Texteingabe verwenden

### Sicherheitsüberlegungen

- xdotool kann jede Anwendung steuern, mit Vorsicht verwenden
- Vermeiden Sie das Ausführen nicht vertrauenswürdiger xdotool-Skripte
- Vorsicht bei Automatisierung, die sensible Daten verarbeitet
- xdotool nur in kontrollierten Umgebungen verwenden

Diese Anleitung behandelt die wesentlichen und erweiterten Funktionen von xdotool. Experimentieren Sie mit diesen Befehlen, um leistungsstarke Desktop-Automatisierungsskripte zu erstellen, die auf Ihre spezifischen Bedürfnisse zugeschnitten sind.