---
audio: false
generated: true
lang: de
layout: post
title: Konvertierung von WebP zu JPG in Ubuntu
translated: true
type: note
---

Sie haben mehrere ausgezeichnete Optionen, um WebP in JPG unter Ubuntu zu konvertieren, sowohl über die Kommandozeile als auch mit GUI-Tools.

## Kommandozeilen-Tools

Diese sind im Allgemeinen am flexibelsten und effizientesten für einzelne Dateien oder Stapelkonvertierungen.

### 1. ImageMagick

ImageMagick ist eine leistungsstarke Sammlung von Kommandozeilen-Tools zur Bildbearbeitung und weit verbreitet.

*   **Installation:**
    ```bash
    sudo apt update
    sudo apt install imagemagick
    ```
*   **Eine einzelne Datei konvertieren:**
    ```bash
    convert input.webp output.jpg
    ```
    Oder, mit `magick` für ImageMagick v7+:
    ```bash
    magick input.webp output.jpg
    ```
*   **Mehrere Dateien konvertieren (Stapelkonvertierung) im aktuellen Verzeichnis:**
    ```bash
    mogrify -format JPEG *.webp
    ```
    Dies konvertiert alle `.webp`-Dateien im aktuellen Verzeichnis in `.jpeg` (oder `.jpg`)-Dateien mit demselben Dateinamen. Wenn Sie die konvertierten Dateien in einem separaten Verzeichnis haben möchten:
    ```bash
    mkdir output_jpgs # Ein Verzeichnis für die Ausgabe erstellen
    mogrify -format JPEG -path output_jpgs *.webp
    ```

### 2. `dwebp` (aus dem `libwebp` Paket)

`dwebp` ist ein spezielles Tool zum Dekodieren von WebP-Bildern.

*   **Installation:**
    ```bash
    sudo apt update
    sudo apt install webp
    ```
*   **Eine einzelne Datei konvertieren:**
    ```bash
    dwebp input.webp -o output.jpg
    ```
    Obwohl Sie `.jpg` als Ausgabe angeben, gibt `dwebp` oft in das PPM-Format aus und benötigt ein weiteres Tool wie ImageMagick, um in ein richtiges JPEG zu konvertieren. Einige Quellen deuten jedoch darauf hin, dass die direkte Verwendung von `.jpg` als Ausgabe in einfachen Fällen funktioniert. Wenn Sie auf Probleme stoßen, konvertieren Sie zuerst in PNG und dann in JPG:
    ```bash
    dwebp input.webp -o output.png
    convert output.png output.jpg
    ```

### 3. `ffmpeg`

`ffmpeg` ist primär für Video und Audio, aber es ist auch sehr fähig im Umgang mit Bildformaten.

*   **Installation:**
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```
*   **Eine einzelne Datei konvertieren:**
    ```bash
    ffmpeg -i input.webp output.jpg
    ```
*   **Mehrere Dateien konvertieren (Stapelkonvertierung):**
    ```bash
    for file in *.webp; do ffmpeg -i "$file" "${file%.*}.jpg"; done
    ```
    Dieser Befehl durchläuft alle `.webp`-Dateien im aktuellen Verzeichnis und konvertiert sie in `.jpg`-Dateien mit demselben Namen (z.B. wird `image.webp` zu `image.jpg`).

## GUI-Tools

Wenn Sie eine grafische Oberfläche bevorzugen, hier sind ein paar Optionen:

### 1. GIMP (GNU Image Manipulation Program)

GIMP ist ein leistungsstarker, quelloffener Bildeditor, der WebP unterstützt.

*   **Installation:**
    ```bash
    sudo apt update
    sudo apt install gimp
    ```
*   **So konvertieren Sie:**
    1.  Öffnen Sie das WebP-Bild in GIMP (Datei > Öffnen).
    2.  Gehen Sie zu Datei > Exportieren als.
    3.  Wählen Sie im Dialog "Bild exportieren" "JPEG-Bild" aus dem Dropdown-Menü "Dateityp auswählen (nach Endung)" aus.
    4.  Klicken Sie auf "Exportieren" und passen Sie bei Bedarf die Qualitätseinstellungen an.

### 2. XnView MP / XnConvert

Dies sind plattformübergreifende Bildbetrachter und Stapelkonverter mit umfassender Formatunterstützung, einschließlich WebP.

*   **Installation:**
    Möglicherweise müssen Sie das `.deb`-Paket von der offiziellen Website herunterladen und es mit `sudo dpkg -i <paketname.deb>` oder über einen grafischen Paketinstaller installieren.
*   **So konvertieren Sie (allgemein):**
    1.  Öffnen Sie XnView MP oder XnConvert.
    2.  Fügen Sie die WebP-Bilder hinzu, die Sie konvertieren möchten.
    3.  Wählen Sie JPG als Ausgabeformat.
    4.  Passen Sie ggf. Einstellungen an (Qualität, Größe ändern, etc.).
    5.  Starten Sie die Konvertierung.

### 3. Converseen

Converseen ist ein kostenloser Stapelbild-Konverter, der WebP unterstützt.

*   **Installation:** Sie finden es normalerweise im Ubuntu Software Center oder können es über apt installieren, falls es in Ihren Repositories verfügbar ist.
*   **So konvertieren Sie:** Es hat eine einfache GUI zum Hinzufügen von Bildern, Auswählen des Ausgabeformats und Konvertieren.

## Welche Methode sollten Sie wählen?

*   **Für schnelle, einzelne Konvertierungen oder das Automatisieren von Aufgaben per Skript:** Verwenden Sie `ffmpeg` oder `ImageMagick` von der Kommandozeile. Sie sind sehr effizient.
*   **Für gelegentliche Konvertierungen, bei denen Sie eine visuelle Oberfläche und mehr Kontrolle über die Bildbearbeitung wünschen:** GIMP ist eine gute Wahl.
*   **Für das Stapelkonvertieren vieler Bilder mit einer GUI und verschiedenen Optionen:** XnView MP/XnConvert oder Converseen sind ausgezeichnet.

Egal für welche Methode Sie sich entscheiden, stellen Sie sicher, dass Sie die notwendigen Pakete zuerst installieren.