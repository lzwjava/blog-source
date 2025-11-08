---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Leitfaden für die Entwicklung mobiler Anwendungen
translated: true
type: note
---

### Kursübersicht: 14567 Mobile Application Development Technology

**Kursinformationen**
- **Kursnummer**: 14567
- **Kursname**: Mobile Application Development Technology (移动应用开发技术)
- **Leistungspunkte**: 4
- **Niveau**: Fachspezifisch (专科)
- **Fachbereich**: Computer Application Technology (计算机应用技术)
- **Prüfungsart**: Schriftlich (笔试); Hinweis: Es gibt eine separate praktische Prüfung unter der Nummer 14568 (1 Leistungspunkt).
- **Prüfungsbehörde**: Guangdong Province Higher Education Self-Study Examination (广东省高等教育自学考试)
- **Lehrbuch**: *Android Mobile Development Basic Case Tutorial (2nd Edition)* von Heima Programmer (黑马程序员), People's Posts and Telecommunications Press (人民邮电出版社), ISBN: 9787115567680 (2022). Der Kursplan orientiert sich eng an der Struktur dieses Lehrbuchs und betont Android-Entwicklung als Kernbeispiel für die Programmierung mobiler Apps.
- **Kurscharakter und Ziele**: Dies ist ein praktischer, anwendungsorientierter Kurs für Studiengänge der Softwareentwicklung und Computeranwendungstechnik, der sich an den Bedürfnissen des Arbeitsmarktes orientiert. Er lehrt die Entwicklung mobiler Apps mit Android als primärer Plattform. Die Lernenden beherrschen die Android-Grundlagen und lernen, mobile Anwendungen zu entwickeln, wobei Theorie und praktische Programmierung kombiniert werden. Der Schwerpunkt liegt auf dem Aufbau einer Entwicklungsumgebung, der Implementierung von Benutzeroberflächen, Datenverwaltung und erweiterten Funktionen wie Vernetzung und Multimedia. Selbstlernende sollten theoretisches Studium mit Experimenten verbinden und Tools wie Android Studio für Debugging und Tests verwenden.

**Prüfungsziele**:
Die Prüfungen testen das umfassende Wissen über Android-Entwicklung, einschließlich Code-Implementierung, Problemlösung und Anwendungsdesign. Der Fokus liegt auf dem Verständnis von Syntax, Architektur und praktischen Szenarien. Theoretische Prüfungen decken breite Themen systematisch ab; die Praxis betont wichtige praktische Fähigkeiten (z.B. über separate 14568-Prüfung). Verwenden Sie Mind Maps zur Wissensintegration und Übungsaufgaben zur Wissensfestigung.

**Kursinhalt und Bewertungsanforderungen**
Der Inhalt ist um 12 Kapitel strukturiert, die von den Grundlagen zu fortgeschrittenen Themen und einem Abschlussprojekt fortschreiten. Jedes Kapitel umfasst Theorie, Code-Beispiele, praktische Übungen und Bewertungen zu Schlüsselkonzepten (z.B. Identifikation, Anwendung, Analyse). Nachfolgend die hierarchische Gliederung:

1. **Android-Grundlagen Einführung**
   - Android-Überblick (Kommunikationstechnologie, Geschichte, Architektur, Dalvik VM).
   - Entwicklungsumgebung einrichten (Android Studio Installation, Emulator, SDK).
   - Erstes Programm entwickeln und Struktur.
   - Ressourcenverwaltung (Bilder, Themen/Stile, Layouts, Strings, Farben, Dimensionen).
   - Debugging (Unit-Tests, Logcat).
   *Anforderungen*: Android-Ökosystem verstehen; einfache Apps erstellen/ausführen.

2. **Gängige Android-Schnittstellenlayouts**
   - View-Grundlagen und Layout-Erstellung (XML vs. Java-Code).
   - Gängige Attribute.
   - LinearLayout (z.B. Tier-Matching-Spiel UI).
   - RelativeLayout (z.B. Musikplayer-UI).
   - TableLayout (z.B. Taschenrechner-UI).
   - FrameLayout (z.B. Neonlicht-UI).
   *Anforderungen*: Responsive UIs entwerfen; Layouts in Projekten anwenden.

3. **Gängige Android-Schnittstellensteuerelemente**
   - Einfache Steuerelemente (TextView, EditText, Button, ImageView, RadioButton, CheckBox, Toast).
   - Listensteuerelemente (ListView mit Adaptern, RecyclerView; z.B. Einkaufszentrum, News-Feed).
   - Benutzerdefinierte Views.
   *Anforderungen*: Interaktive Elemente implementieren; Datenbindung handhaben.

4. **Programmaktivitätseinheit: Activity**
   - Lebenszyklus (Zustände, Methoden).
   - Erstellung, Konfiguration, Starten/Schließen.
   - Intent und IntentFilter.
   - Activity-Wechsel und Datenübermittlung/-rückgabe (z.B. Affe pflückt Pfirsiche Spiel).
   - Task-Stacks und Startmodi.
   - Fragment-Verwendung (Lebenszyklus, Erstellung, Integration; z.B. Meituan-Menü).
   *Anforderungen*: App-Ablauf verwalten; Fragmente für modulare UIs handhaben.

5. **Datenspeicherung**
   - Überblick Speichermethoden.
   - Dateispeicherung (schreiben/lesen; z.B. QQ-Login speichern).
   - SharedPreferences (speichern/lesen/löschen; z.B. QQ-Login).
   - SQLite-Datenbank (Erstellung, CRUD, Transaktionen; z.B. Grüne-Bohnen-Kontakte).
   *Anforderungen*: Daten persistent und sicher speichern; Datenbanken abfragen/verwalten.

6. **Content Provider**
   - Überblick.
   - Erstellung.
   - Zugriff auf andere Apps (Daten abfragen; z.B. Telefonkontakte lesen).
   - Content Observer (Änderungen überwachen; z.B. Datenänderungserkennung).
   *Anforderungen*: Daten über Apps teilen; Observer implementieren.

7. **Broadcast-Mechanismus**
   - Überblick.
   - Broadcast-Empfänger (Erstellung).
   - Benutzerdefinierte Broadcasts (z.B. Cafeteria-Broadcast).
   - Broadcast-Typen (z.B. Enten zählen).
   *Anforderungen*: System-/App-Ereignisse über Broadcasts handhaben.

8. **Services**
   - Überblick und Erstellung.
   - Lebenszyklus.
   - Startmethoden (startService, bindService).
   - Kommunikation (lokal/remote; z.B. NetEase Musikplayer).
   *Anforderungen*: Hintergrundaufgaben ausführen; Kommunikation zwischen Komponenten ermöglichen.

9. **Netzwerkprogrammierung**
   - HTTP-Zugriff (HttpURLConnection).
   - WebView-Entwicklung (HTML anzeigen, JS-Unterstützung).
   - JSON-Parsing (z.B. Pinduoduo Handeln UI).
   - Handler-Nachrichtenmechanismus.
   *Anforderungen*: Webdaten abrufen/parsen; asynchrone Operationen handhaben.

10. **Grafiken und Bildverarbeitung**
    - Zeichenklassen (Bitmap, BitmapFactory, Paint, Canvas; z.B. Welpen zeichnen).
    - Bildeffekte.
    - Animationen (Tween, Frame-by-Frame, Property; z.B. fliegende Schmetterlinge/Vögel).
    *Anforderungen*: Visuals/Animationen erstellen; Grafiken optimieren.

11. **Multimedia-Anwendungsentwicklung**
    - Audiowiedergabe (MediaPlayer, SoundPool; z.B. Klavier).
    - Videowiedergabe (VideoView, SurfaceView+MediaPlayer; z.B. Videoplayer).
    *Anforderungen*: Medien integrieren; Wiedergabe steuern.

12. **Umfassendes Projekt: Meituan Takeout Nachahmung**
    - Projektanalyse (Überblick, Umgebung, Module).
    - UI-Demos (Geschäfte, Details, Bestellungen).
    - Serverdatenvorbereitung.
    - Implementierung Geschäftsliste, Details, Menü/Warenkorb, Bestellungen/Bezahlung.
    *Anforderungen*: Alle Konzepte in einer vollständigen App integrieren.

**Zusätzliche Hinweise und Umsetzungsanforderungen**
- **Lerntipps**: Bauen Sie Labore früh auf; programmieren Sie mit den Beispielen. Konzentrieren Sie sich auf 70% Praxis, 30% Theorie. Verwenden Sie integrierte IDE-Hinweise während Übungsprüfungen.
- **Prüfungsformat**: Theoretisch: Multiple-Choice, Kurzantwort, Codeanalyse (80% Abdeckung der Kapitel 1-11). Praktisch (14568): Praktische Programmierung für Kernfunktionen (z.B. UI, Speicherung, Services).
- **Aktualisierungen**: Die Pläne können sich bei Lehrbuchüberarbeitungen anpassen; prüfen Sie die Guangdong Education Exam Authority (eea.gd.gov.cn) für die neuesten Versionen.

Für das vollständige offizielle Lehrplan-PDF besuchen Sie die Guangdong Selbststudium-Ressourcen oder laden Sie es von autorisierten Seiten wie zikaosw.cn herunter.

**Referenzen**
- [Guangdong Selbststudium Kursplan](https://eea.gd.gov.cn/attachment/0/532/532589/4262692.pdf)
- [Lehrbuchinhaltsverzeichnis](https://resource.ityxb.com/book/android_case2.html)
- [Guangdong Selbststudium Lehrplanübersicht](https://www.zikaosw.cn/news/22151554.html)