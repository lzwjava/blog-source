---
audio: false
generated: true
lang: de
layout: post
title: 'Xvfb: Kopfgeloser X11-Displayserver'
translated: true
type: note
---

### Was ist Xvfb?

Xvfb (X Virtual Framebuffer) ist ein X11-Display-Server, der grafische Anwendungen ausführt, ohne einen physischen Bildschirm oder Hardware-Grafikbeschleunigung zu benötigen. Es handelt sich im Wesentlichen um einen "Headless"-X-Server, der einen Bildschirm im Arbeitsspeicher simuliert. Dadurch können Programme, die eine grafische Umgebung benötigen (wie Browser, GUI-Tests oder Rendering-Tools), auf Servern oder in Umgebungen ohne Monitor, Tastatur oder Maus ausgeführt werden.

Es wird häufig für automatisiertes Testen (z.B. mit Selenium für Web-Scraping oder UI-Tests), CI/CD-Pipelines oder in jedem Szenario verwendet, in dem X11-basierte Anwendungen im Hintergrund ausgeführt werden müssen, ohne dass etwas auf einem Bildschirm angezeigt wird.

### Wie funktioniert Xvfb?

1.  **Erstellung eines virtuellen Displays**:
    *   Wenn Sie Xvfb starten, erstellt es ein virtuelles Display (z.B. `:99` oder eine andere Display-Nummer), das vollständig im RAM existiert. Dieses Display hat eine festgelegte Auflösung, Farbtiefe und andere Parameter, die beim Start definiert werden.
    *   Beispielbefehl: `Xvfb :99 -screen 0 1024x768x24` (startet ein virtuelles Display mit 1024x768 Auflösung und 24-Bit-Farbe).

2.  **Verarbeitung grafischer Operationen**:
    *   Xvfb fängt X11-Protokollanfragen von Anwendungen ab (wie das Zeichnen von Fenstern, das Rendern von Bildern oder das Verarbeiten von Ereignissen).
    *   Anstatt die Ausgabe an einen physischen Bildschirm zu senden, führt es alle Operationen in einem Speicherpuffer (dem "Framebuffer") aus. Dieser Puffer wirkt wie ein virtueller Bildschirm, auf den Pixel geschrieben, aber nie angezeigt werden.
    *   Es unterstützt grundlegende X11-Funktionen, bietet jedoch keine Hardware-Beschleunigung, daher ist es nicht für Hochleistungsgrafiken wie Spiele geeignet – es eignet sich eher für einfaches Rendering oder Tests.

3.  **Ereignissimulation**:
    *   Xvfb kann bei Bedarf Eingabeereignisse (z.B. Maus/Tastatur) simulieren, aber typischerweise laufen Anwendungen so ab, als wären sie auf einem echten Display.
    *   Die Ausgabe ist nicht sichtbar, aber Sie können Screenshots aufnehmen oder den Framebuffer zu Dateien dumpen (mit Tools wie `xwd` oder `import` von ImageMagick), um sie zu überprüfen.

4.  **Integration mit Tools**:
    *   Bibliotheken wie pyvirtualdisplay (wie in Ihrer Fehlerausgabe) kapseln Xvfb, um das Starten/Stoppen aus dem Code heraus zu erleichtern. Zum Beispiel in Python:
        ```python
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(1024, 768))
        display.start()
        # Führen Sie hier Ihre grafische Anwendung aus
        display.stop()
        ```
    *   Es läuft im Hintergrund, und Ihre Anwendung setzt die `DISPLAY`-Umgebungsvariable (z.B. `export DISPLAY=:99`), um auf den virtuellen Server zu verweisen.

5.  **Einschränkungen**:
    *   Keine echte Hardware-Interaktion, daher keine GPU-Unterstützung oder direkte Videoausgabe.
    *   Der Speicherverbrauch kann bei größeren Auflösungen oder langen Laufzeitsitzungen ansteigen.
    *   Es ist Teil des X.org-Projekts und auf Linux/Unix-Systemen verfügbar; nicht nativ für macOS oder Windows (obwohl Alternativen wie Xming für Windows existieren).

Bezüglich des von Ihnen eingefügten Fehlers: Es scheint, dass Xvfb nicht auf Ihrem System installiert ist (der `FileNotFoundError` für 'Xvfb'). Unter macOS (basierend auf Ihren Homebrew-Pfaden) können Sie es über `brew install --cask xvfb` oder ähnlich installieren, aber stellen Sie sicher, dass es in Ihrem PATH verfügbar ist. pyvirtualdisplay setzt voraus, dass es als ausführbare Datei verfügbar ist.

[Xvfb Man Page](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml)  
[Wikipedia: Xvfb](https://en.wikipedia.org/wiki/Xvfb)  
[How to Use Xvfb for Headless Testing](https://www.browserstack.com/guide/what-is-xvfb)