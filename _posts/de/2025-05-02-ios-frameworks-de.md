---
audio: false
generated: true
lang: de
layout: post
title: iOS Frameworks
translated: true
type: note
---

Neben UIKit bietet das iOS-System viele andere essentielle Frameworks, die Entwickler häufig zum Erstellen von Anwendungen verwenden. Diese Frameworks kümmern sich um verschiedene Aspekte, die über reine Benutzeroberflächenelemente hinausgehen. Hier sind einige der gebräuchlichsten:

1.  **Foundation:** Dies ist ein grundlegendes Framework, das Basisdatentypen (wie Strings, Zahlen, Arrays, Dictionaries), Sammlungstypen, Betriebssystemdienste und Kern-Programmiermuster bereitstellt. Es ist das Fundament für viele andere Frameworks und wird fast immer in ein iOS-Projekt importiert. Es enthält wesentliche Komponenten wie `URLSession` für Netzwerkfunktionen, `FileManager` für Dateisysteminteraktionen und `NotificationCenter` zur Verwaltung von Benachrichtigungen innerhalb einer Anwendung.

2.  **Core Data:** Dieses Framework bietet eine robuste und flexible Möglichkeit, die Modellschicht-Objekte in Ihrer Anwendung zu verwalten. Es ermöglicht Ihnen, Daten zu persistieren, Objektgraphen zu verwalten und die Datensynchronisation zu handhaben. Obwohl es oft als Datenbanktechnologie beschrieben wird, ist es genauer gesagt ein Framework zur Objektgraphverwaltung, das verschiedene persistente Speicher verwenden kann, wie z.B. SQLite, Binärdateien oder In-Memory-Speicher.

3.  **Core Animation:** Dieses Framework wird verwendet, um flüssige, hochleistungsfähige Animationen und visuelle Effekte zu erstellen. Es arbeitet mit UIKit (oder AppKit auf macOS) zusammen, um animierte Inhalte darzustellen. Sie können es verwenden, um Views, Layers und andere grafische Elemente zu animieren und so komplexe Übergänge und Effekte zu erstellen, ohne direkt Pixel zu manipulieren.

4.  **Core Graphics:** Auch bekannt als Quartz 2D, ist dies eine C-basierte Zeichen-Engine, die Low-Level-2D-Rendering-Fähigkeiten bereitstellt. Es ermöglicht Ihnen, Punkte, Linien, Pfade, Formen und Bilder mit hoher Genauigkeit zu zeichnen. Während UIKit höhere Abstraktionen für das Zeichnen bietet, wird Core Graphics oft für benutzerdefinierte Zeichenoperationen, das Erstellen von Verläufen, das Verwalten von Kontexten und das direkte Arbeiten mit grafischen Primitiven verwendet.

5.  **AVFoundation:** Dieses Framework bietet einen umfassenden Satz an Werkzeugen für die Arbeit mit zeitbasierten audiovisuellen Medien. Sie können es verwenden, um Audio und Video abzuspielen, aufzunehmen und zu bearbeiten. Es gibt Ihnen Kontrolle über Kameras, Mikrofone, Playback-Engines und Medienassets, was es für Apps, die Multimedia-Inhalte beinhalten, unerlässlich macht.

6.  **Core Location:** Dieses Framework ermöglicht es Ihrer Anwendung, auf die Ortungsdienste des Geräts zuzugreifen, wie z.B. den aktuellen geografischen Standort, die Höhe und die Richtung des Benutzers. Es kann GPS, Wi-Fi und Mobilfunksignale zur Standortermittlung nutzen und unterstützt Funktionen wie Region Monitoring und Geofencing.

7.  **UserNotifications:** Dieses Framework wird verwendet, um lokale und Remote-Benachrichtigungen zu planen und zu verarbeiten. Es ermöglicht Ihrer App, Benutzer über wichtige Ereignisse zu informieren, selbst wenn die App nicht aktiv läuft, indem es Warnungen anzeigt, Töne abspielt oder Badges auf dem App-Symbol aktualisiert.

8.  **SwiftUI:** Während UIKit das traditionelle Framework für den Aufbau von Benutzeroberflächen mit einem imperativen Ansatz ist, ist SwiftUI ein neueres, deklaratives Framework, das von Apple für den Aufbau von Benutzeroberflächen auf allen Apple-Plattformen eingeführt wurde. Es bietet ein anderes Paradigma für die UI-Entwicklung und ist in der modernen iOS-Entwicklung immer häufiger anzutreffen, oft in Verbindung mit oder als Alternative zu UIKit, insbesondere für neue Projekte oder Funktionen.

Diese Frameworks bilden zusammen mit vielen anderen wie Metal (für Grafikbeschleunigung), SpriteKit (für 2D-Spiele), SceneKit (für 3D-Grafiken) und Core ML (für Machine Learning) das leistungsstarke Ökosystem, das iOS-Entwickler nutzen, um vielfältige und funktionsreiche Anwendungen zu erstellen.