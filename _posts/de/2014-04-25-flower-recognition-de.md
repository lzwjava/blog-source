---
audio: false
generated: false
image: false
lang: de
layout: post
title: Blumen Erkennungs-App
translated: true
type: post
---

Dies ist die README.md von dem GitHub-Projekt [https://github.com/lzwjava/flower-recognition](https://github.com/lzwjava/flower-recognition).

---

### Flower Recognition App

Dies ist eine Blumen-Erkennungs-Android-Anwendung, die entwickelt wurde, um Benutzern zu helfen, Blumen durch das Aufnehmen von Fotos und Zeichnen von Kreisen zur Unterstützung der Erkennung zu identifizieren.

#### Funktionen:
- **Fotos aufnehmen**: Benutzer können innerhalb der App Fotos von Blumen aufnehmen.
- **Zeichnen**: Die Möglichkeit, Kreise und Anmerkungen auf Blumenbildern zu zeichnen, um die Erkennung zu unterstützen.
- **Authentifizierung**: Sichere Benutzerauthentifizierung mit einem Anmeldebildschirm.
- **Ergebnisanzeige**: Anzeige der Erkennungsergebnisse in einer benutzerfreundlichen Oberfläche.
- **Material Design**: Implementierung von Material-Design-Prinzipien für ein modernes und intuitives Benutzererlebnis.

#### Dateistruktur:
```
└── com
    └── lzw
        └── flower
            ├── activity
            │   ├── LoginActivity.java
            │   └── PhotoActivity.java
            ├── adapter
            │   └── PhotoAdapter.java
            ├── avobject
            │   └── Photo.java
            ├── base
            │   ├── App.java
            │   ├── ImageLoader.java
            │   └── SplashActivity.java
            ├── deprecated
            │   ├── CameraActivity.java
            │   └── Deprecated.java
            ├── draw
            │   ├── Draw.java
            │   ├── DrawActivity.java
            │   ├── DrawFragment.java
            │   ├── DrawView.java
            │   ├── HelpBtn.java
            │   ├── History.java
            │   ├── Tooltip.java
            │   └── ZoomImageView.java
            ├── fragment
            │   ├── RecogFragment.java
            │   └── WaitFragment.java
            ├── material
            │   └── MaterialActivity.java
            ├── result
            │   ├── FlowerAdapter.java
            │   ├── FlowerData.java
            │   ├── Image.java
            │   ├── ResultActivity.java
            │   └── ResultFragment.java
            ├── service
            │   └── PhotoService.java
            ├── utils
            │   ├── BitmapUtils.java
            │   ├── Crop.java
            │   ├── ImageListDialogBuilder.java
            │   ├── Logger.java
            │   ├── PathUtils.java
            │   └── Utils.java
            └── web
                ├── Upload.java
                ├── UploadImage.java
                └── Web.java
```

#### Komponenten:
- **Aktivitäten**: Enthält Klassen zur Verwaltung verschiedener App-Aktivitäten wie Anmeldung, Fotoaufnahme und Startbildschirm.
- **Adapter**: Verarbeitet die Anzeige von Fotos und Erkennungsergebnissen.
- **AVObject**: Stellt Fotoobjekte mit zugehörigen Metadaten dar.
- **Zeichnen**: Klassen, die mit dem Zeichnen von Kreisen und Anmerkungen auf Blumenbildern verbunden sind.
- **Fragments**: Bietet UI-Komponenten zur Anzeige von Erkennungsergebnissen und Warteanzeigen.
- **Material**: Möglicherweise mit der Implementierung von Material-Design-Richtlinien verbunden.
- **Dienste**: Verarbeitet Hintergrundaufgaben und Datenmanipulationen in Bezug auf Fotos.
- **Utils**: Enthält Hilfsklassen für verschiedene Aufgaben wie Bildbearbeitung und Protokollierung.

#### Nutzung:
1. Klonen Sie das Repository.
2. Öffnen Sie das Projekt in Android Studio.
3. Bauen und führen Sie die Anwendung auf einem Android-Gerät oder Emulator aus.

#### Lizenz:
Dieses Projekt unterliegt der [MIT-Lizenz](LICENSE).