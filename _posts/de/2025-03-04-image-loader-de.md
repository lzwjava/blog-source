---
audio: false
generated: true
lang: de
layout: post
title: Universeller Bildlader in Android
translated: true
type: note
---

Universal Image Loader (UIL) Version 1.9.3 ist eine leistungsstarke und flexible Bibliothek zum Laden, Zwischenspeichern und Anzeigen von Bildern in Android-Anwendungen. Nachfolgend finden Sie eine Schritt-für-Schritt-Anleitung zur Verwendung in Ihrem Android-Projekt. Beachten Sie, dass diese Bibliothek älter ist und nicht mehr weiterentwickelt wird (letztes Update um 2015). Für moderne Projekten sollten Sie Alternativen wie Glide oder Picasso in Betracht ziehen. Wenn Sie jedoch speziell UIL 1.9.3 verwenden müssen, geht das so:

---

### Schritt 1: Fügen Sie die Bibliothek zu Ihrem Projekt hinzu
Da UIL 1.9.3 über Maven verfügbar ist, können Sie es mit Gradle zu Ihrem Projekt hinzufügen. Wenn Sie mit einem älteren Setup arbeiten (z.B. Eclipse), können Sie die JAR-Datei manuell herunterladen.

#### Mit Gradle (Android Studio):
1. Öffnen Sie die `build.gradle` Datei Ihres App-Moduls (Module: app).
2. Fügen Sie die folgende Abhängigkeit im `dependencies` Block hinzu:
   ```gradle
   implementation 'com.nostra13.universalimageloader:universal-image-loader:1.9.3'
   ```
3. Synchronisieren Sie Ihr Projekt mit Gradle, indem Sie in Android Studio auf "Sync Now" klicken.

#### Manuelles JAR-Setup (z.B. Eclipse):
1. Laden Sie die `universal-image-loader-1.9.3.jar` aus dem Maven Repository oder von GitHub herunter.
2. Legen Sie die JAR-Datei im `libs` Ordner Ihres Projekts ab.
3. Klicken Sie in Ihrer IDE mit der rechten Maustaste auf die JAR und wählen Sie "Add to Build Path" (Eclipse) oder konfigurieren Sie sie manuell in Ihren Projekteinstellungen.

---

### Schritt 2: Fügen Sie Berechtigungen hinzu
Um Bilder aus dem Internet zu laden oder auf dem Speicher zu sichern, fügen Sie die folgenden Berechtigungen zu Ihrer `AndroidManifest.xml` hinzu:
```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```
- `INTERNET`: Erforderlich zum Herunterladen von Bildern von URLs.
- `WRITE_EXTERNAL_STORAGE`: Erforderlich für die Disk-Zwischenspeicherung (optional, aber für Offline-Nutzung empfohlen). Für Android 6.0+ (API 23+) müssen Sie diese Berechtigung auch zur Laufzeit anfordern.

---

### Schritt 3: Initialisieren Sie den ImageLoader
Bevor Sie