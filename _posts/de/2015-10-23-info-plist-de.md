---
audio: false
lang: de
layout: post
title: Entschlüsseln der Info.plist-Datei
translated: true
---

Wenn Sie mit der Entwicklung für macOS oder iOS gearbeitet haben, sind Sie wahrscheinlich auf eine `Info.plist`-Datei gestoßen. Diese XML-basierte Datei ist ein wesentlicher Bestandteil jeder Apple-Anwendung oder jedes Plugins und fungiert wie ein Pass, der dem System mitteilt, wer es ist, was es tut und wie es sich verhalten soll. Heute erkunden wir die `Info.plist` von "Reveal-In-GitHub", einem Xcode-Plugin, das wir in einem vorherigen Beitrag vorgestellt haben. Anstatt jede Zeile zu zerlegen, konzentrieren wir uns auf die Kernkonzepte und Muster, die seinen Zweck und seine Funktionalität definieren.

---

#### Was ist eine `Info.plist`-Datei?

Die `Info.plist` (kurz für "Information Property List") ist eine strukturierte Datei, die Metadaten über eine App, ein Plugin oder ein Bundle enthält. In XML (mit einem spezifischen, von Apple definierten Schema) geschrieben, verwendet sie Schlüssel-Wert-Paare, um Wesentliches wie den Namen der App, die Version und die Kompatibilität zu beschreiben. Für "Reveal-In-GitHub" identifiziert diese Datei es als ein Xcode-Plugin und stellt sicher, dass es nahtlos in die IDE integriert wird.

Im Gegensatz zur `.pbxproj`-Datei, die sich darum kümmert, *wie* etwas gebaut wird, geht es bei der `Info.plist` darum, *was* das etwas ist. Es ist eine Erklärung der Identität und Absicht.

---

#### Wichtige Konzepte in der Datei

1. **Bundle-Grundlagen**
   Mehrere Schlüssel definieren das Plugin als ein macOS-Bundle:
   - **`CFBundleExecutable`**: Setzt auf `$(EXECUTABLE_NAME)`, ein Platzhalter für den Namen der kompilierten Binärdatei (während des Build-Prozesses definiert).
   - **`CFBundleIdentifier`**: `$(PRODUCT_BUNDLE_IDENTIFIER)` löst sich zu `com.lzwjava.Reveal-In-GitHub` auf, eine eindeutige reverse-DNS-Art-ID, die dieses Plugin von anderen unterscheidet.
   - **`CFBundlePackageType`**: `BNDL` markiert es als ein Bundle, ein häufiges Format für Plugins und Bibliotheken auf macOS.
   - **`CFBundleName`**: `$(PRODUCT_NAME)` wird zu "Reveal-In-GitHub", dem benutzerfreundlichen Namen.

2. **Versionierung und Eigentum**
   - **`CFBundleShortVersionString`**: "1.0" ist die benutzerfreundliche Version.
   - **`CFBundleVersion`**: "1" ist eine interne Build-Nummer.
   - **`NSHumanReadableCopyright`**: "Copyright © 2015年 lzwjava. Alle Rechte vorbehalten." gibt den Ersteller, `lzwjava`, an und datiert das Plugin auf 2015.
   - **`CFBundleSignature`**: "????" ist ein Platzhalter (normalerweise ein vierstelliger Code), obwohl er für Plugins weniger kritisch ist.

3. **Lokalisierung**
   - **`CFBundleDevelopmentRegion`**: "en" setzt Englisch als Standardsprache, was die Lokalisierung von Ressourcen (falls vorhanden) beeinflusst.

4. **Xcode-Plugin-Kompatibilität**
   Das herausragende Merkmal hier ist **`DVTPlugInCompatibilityUUIDs`**, eine lange Liste von UUIDs. Diese passen zu spezifischen Xcode-Versionen (z.B. Xcode 6, 7 usw.), sodass das Plugin nur in kompatiblen IDEs geladen wird. Diese Liste ist ungewöhnlich umfangreich, was darauf hindeutet, dass "Reveal-In-GitHub" so gestaltet wurde, dass es mit vielen Xcode-Releases funktioniert – ein Zeichen für sorgfältige Vorwärts- und Rückwärtskompatibilität.

5. **Plugin-spezifische Einstellungen**
   - **`NSPrincipalClass`**: Leer (`<string></string>`), was darauf hindeutet, dass das Plugin seinen Einstiegspunkt möglicherweise dynamisch definiert oder auf die Konventionen von Xcode angewiesen ist.
   - **`XC4Compatible` und `XC5Compatible`**: Beide `<true/>`, was die Kompatibilität mit Xcode 4 und 5 bestätigt.
   - **`XCGCReady`**: `<true/>` zeigt die Bereitschaft für die Garbage Collection, ein älteres macOS-Speicherverwaltungsmerkmal (meistens 2015 zugunsten von ARC veraltet).
   - **`XCPluginHasUI`**: `<false/>` deutet darauf hin, dass keine benutzerdefinierte Benutzeroberfläche über das in Xcode eingebaute hinaus vorhanden ist – obwohl dies im Widerspruch zur `.xib`-Datei in der `.pbxproj` zu stehen scheint. Vielleicht ist die Benutzeroberfläche minimal oder wird anders gehandhabt.

---

#### Muster, die man beachten sollte

1. **Platzhalter für Flexibilität**
   Schlüssel wie `$(EXECUTABLE_NAME)` und `$(PRODUCT_BUNDLE_IDENTIFIER)` verwenden Variablen, die mit dem Build-System (in der `.pbxproj` definiert) verbunden sind. Dies hält die `Info.plist` über Konfigurationen hinweg wiederverwendbar (z.B. Debug vs. Release).

2. **Minimalistisches Design**
   Die Datei ist schlank und konzentriert sich auf das Wesentliche. Keine fancy Icons, Berechtigungen oder app-spezifische Einstellungen – nur das, was ein Xcode-Plugin benötigt, um zu funktionieren. Diese Einfachheit ist typisch für Plugins, die eine bestehende App (Xcode) erweitern, anstatt eigenständige Programme zu sein.

3. **Fokus auf Kompatibilität**
   Die lange Liste `DVTPlugInCompatibilityUUIDs` und Flags wie `XC4Compatible` zeigen ein Plugin, das für die Ewigkeit gebaut wurde. Dieses Muster ist bei Entwicklertools üblich, bei denen Benutzer möglicherweise ältere Xcode-Versionen für Stabilität beibehalten.

4. **Metadaten statt Verhalten**
   Im Gegensatz zu Code-Dateien *macht* die `Info.plist` nichts – sie beschreibt. Ihre Rolle ist passiv, indem sie Informationen bereitstellt, die Xcode und macOS zur Laufzeit interpretieren.

---

#### Was sagt uns das über Reveal-In-GitHub?

Diese `Info.plist` stellt "Reveal-In-GitHub" als ein leichtgewichtiges, fokussiertes Xcode-Plugin aus dem Jahr 2015 dar, das wahrscheinlich von einem Einzelentwickler (`lzwjava`) erstellt wurde. Seine breite Kompatibilität deutet darauf hin, dass es weit verbreitet nutzbar sein sollte, während das Fehlen eines UI-Flags (trotz einer `.xib` im Projekt) auf eine subtile Integration hinweist – möglicherweise ein Menüpunkt oder eine kontextbezogene Aktion anstelle einer auffälligen Benutzeroberfläche. Angesichts des Namens und des Kontexts aus der `.pbxproj` verknüpft es wahrscheinlich GitHub-Workflows, wie das Verknüpfen von Xcode-Dateien mit ihren Online-Repos.

---

#### Warum das wichtig ist

Die `Info.plist` ist der Handshake Ihrer App mit dem System. Für Entwickler bedeutet das, dass Sie die Kompatibilität, Versionierung oder das Verhalten anpassen können, ohne den Code zu ändern. Für "Reveal-In-GitHub" ist es der Schlüssel zur nahtlosen Integration in Xcode. Beim nächsten Mal, wenn Sie ein Plugin debuggen oder Ihr eigenes erstellen, wird diese Datei Ihr Ausgangspunkt sein – klein, aber mächtig.