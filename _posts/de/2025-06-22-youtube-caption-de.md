---
audio: false
generated: true
lang: de
layout: post
title: Methoden zur Extraktion von YouTube-Video-Untertiteln
translated: true
type: note
---

Um alle Untertitel eines YouTube-Videos zu erhalten, folgen Sie diesen Schritten, je nach Ihren Bedürfnissen und ob Sie einen manuellen oder automatisierten Ansatz bevorzugen. Beachten Sie, dass Untertitel für das Video verfügbar sein müssen (entweder automatisch generiert oder vom Ersteller hochgeladen).

### Manuelle Methode (Verwendung der integrierten Transkript-Funktion von YouTube)
1. **Öffnen Sie das Video**: Gehen Sie in einem Webbrowser zu YouTube und navigieren Sie zum gewünschten Video.
2. **Prüfen Sie auf Untertitel**: Klicken Sie auf das Video, um es zu pausieren. Suchen Sie nach einem "CC"-Symbol (Closed Captions) in der unteren rechten Ecke des Players. Wenn es sichtbar ist, sind Untertitel verfügbar.
3. **Greifen Sie auf das Transkript zu**:
   - Scrollen Sie nach unten zur Videobeschreibung und klicken Sie auf "Mehr anzeigen".
   - Finden und klicken Sie auf "Transkript anzeigen" (falls verfügbar). Dies öffnet ein Transkript-Panel auf der rechten Seite des Videos mit Zeitstempeln und Text.
4. **Zeitstempel umschalten**: Klicken Sie auf die drei vertikalen Punkte oben rechts im Transkript-Panel und wählen Sie "Zeitstempel umschalten", um Zeitstempel je nach Präferenz anzuzeigen oder auszublenden.
5. **Kopieren Sie das Transkript**:
   - Scrollen Sie zum Ende des Transkripts, klicken und halten Sie nach dem letzten Wort, und ziehen Sie dann nach oben, um den gesamten Text zu markieren.
   - Drücken Sie `Strg + C` (Windows) oder `Befehl + C` (Mac), um zu kopieren.
6. **Einfügen und Speichern**: Öffnen Sie einen Texteditor (z.B. Notepad, TextEdit oder Word), fügen Sie den Text mit `Strg + V` oder `Befehl + V` ein und speichern Sie ihn als `.txt`-Datei oder in Ihrem bevorzugten Format.

**Hinweis**: Diese Methode funktioniert nur auf der YouTube-Website, nicht in der mobilen App.[](https://www.wikihow.com/Download-YouTube-Video-Subtitles)

### Für Content-Ersteller (Herunterladen von Untertiteln aus Ihrem eigenen Video)
Wenn Sie der Besitzer des Videos sind, können Sie Untertitel direkt aus dem YouTube Studio herunterladen:
1. **Melden Sie sich im YouTube Studio an**: Gehen Sie zu [studio.youtube.com](https://studio.youtube.com).
2. **Wählen Sie ein Video aus**: Klicken Sie im linken Menü auf "Inhalt" und wählen Sie dann das Video aus.
3. **Greifen Sie auf Untertitel zu**: Klicken Sie im linken Menü auf "Untertitel" und wählen Sie dann die Sprache aus.
4. **Untertitel herunterladen**: Klicken Sie auf das Drei-Punkte-Menü neben der Untertitelspur und wählen Sie "Herunterladen". Wählen Sie ein Format wie `.srt`, `.vtt` oder `.sbv`.
5. **Bearbeiten oder Verwenden**: Öffnen Sie die heruntergeladene Datei in einem Texteditor oder Untertitel-Editor (z.B. Aegisub) zur weiteren Verwendung.

**Hinweis**: Sie können Untertiteldateien nur für Videos auf Kanälen herunterladen, die Sie verwalten.[](https://ito-engineering.screenstepslive.com/s/ito_fase/a/1639680-how-do-i-download-a-caption-file-from-youtube)

### Automatisierte Methode (Verwendung von Drittanbieter-Tools)
Wenn Sie Untertitel in einem bestimmten Format (z.B. `.srt`) oder für Videos benötigen, die Ihnen nicht gehören, verwenden Sie ein seriöses Drittanbieter-Tool:
1. **Wählen Sie ein Tool aus**: Beliebte Optionen sind:
   - **DownSub**: Ein kostenloses Online-Tool zum Herunterladen von Untertiteln.
   - **Notta**: Bietet Transkription und Untertitel-Downloads mit hoher Genauigkeit.[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)
   - **4K Download**: Eine Desktop-App zum Extrahieren von Untertiteln.[](https://verbit.ai/captioning/a-guide-to-downloading-subtitles-and-captions-from-youtube-enhancing-accessibility-and-user-experience/)
2. **Kopieren Sie die Video-URL**: Öffnen Sie das YouTube-Video, klicken Sie auf "Teilen" unter dem Video und kopieren Sie die URL.
3. **Verwenden Sie das Tool**:
   - Fügen Sie die URL in das Eingabefeld des Tools ein.
   - Wählen Sie die gewünschte Sprache und das Format (z.B. `.srt`, `.txt`).
   - Klicken Sie auf "Herunterladen" oder "Extrahieren" und speichern Sie die Datei.
4. **Überprüfen Sie die Datei**: Öffnen Sie die Datei, um die Genauigkeit sicherzustellen, da automatisch generierte Untertitel Fehler enthalten können.

**Vorsicht**: Verwenden Sie vertrauenswürdige Tools, um Sicherheitsrisiken zu vermeiden. Einige Tools können Werbung enthalten oder erfordern Zahlung für erweiterte Funktionen.[](https://gotranscript.com/blog/how-to-download-subtitles-from-youtube)

### Verwendung der YouTube API (Für Entwickler)
Für das Massenherunterladen von Untertiteln oder die App-Integration verwenden Sie die YouTube Data API:
1. **Richten Sie den API-Zugang ein**: Erstellen Sie ein Projekt in der [Google Cloud Console](https://console.cloud.google.com), aktivieren Sie die YouTube Data API v3 und erhalten Sie einen API-Schlüssel.
2. **Untertitelspuren auflisten**: Verwenden Sie den Endpoint `captions.list`, um verfügbare Untertitelspuren für ein Video abzurufen. Beispiel:
   ```
   GET https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=VIDEO_ID&key=API_KEY
   ```
3. **Untertitel herunterladen**: Verwenden Sie den Endpoint `captions.download`, um eine bestimmte Untertitelspur abzurufen. Beispiel:
   ```
   GET https://www.googleapis.com/youtube/v3/captions/CAPTION_ID?tfmt=srt&key=API_KEY
   ```
4. **Einschränkungen**:
   - Sie können nur Untertitel für Ihre eigenen Videos herunterladen, es sei denn, der Videobesitzer hat sie öffentlich zugänglich gemacht.
   - Die API-Nutzung unterliegt Quotenbeschränkungen (etwa 200 Einheiten pro Untertitel-Download).[](https://developers.google.com/youtube/v3/docs/captions)[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)
5. **Alternative**: Einige Entwickler scrapen die timed text URL (z.B. `https://www.youtube.com/api/timedtext?...`) aus dem Seitenquelltext des Videos, aber dies ist unzuverlässig, kann gegen die Nutzungsbedingungen von YouTube verstoßen und birgt das Risiko einer IP-Sperre.[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)

### Zusätzliche Tipps
- **Sprachauswahl**: Wenn Untertitel in mehreren Sprachen verfügbar sind, wählen Sie Ihre bevorzugte Sprache aus den "Untertitel/CC"-Einstellungen oder dem Dropdown-Menü des Transkripts.[](https://riverside.fm/blog/youtube-transcription)
- **Automatisch generierte Untertitel**: Diese können aufgrund von Akzenten, Hintergrundgeräuschen oder komplexen Audioinhalten Fehler aufweisen. Überprüfen und bearbeiten Sie sie, wenn Genauigkeit kritisch ist.[](https://support.google.com/youtube/answer/6373554?hl=en)
- **Barrierefreiheit**: Untertitel verbessern die Barrierefreiheit für gehörlose oder schwerhörige Zuschauer und steigern die SEO, indem sie Inhalte durchsuchbar machen.[](https://www.descript.com/blog/article/transcript-of-youtube-videos)
- **Keine Untertitel verfügbar?**: Wenn das Video keine Untertitel hat, ziehen Sie in Betracht, Transkriptionsdienste wie Rev oder Notta zu verwenden, um ein Transkript aus dem Audio zu generieren.[](https://www.rev.com/resources/how-to-download-youtube-subtitles-as-text-files)[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)

### Einschränkungen
- Nicht alle Videos haben Untertitel, insbesondere wenn der Ersteller sie deaktiviert hat oder die automatische Untertitelung von YouTube für die Sprache oder Audioqualität nicht unterstützt wird.[](https://support.google.com/youtube/answer/6373554?hl=en)
- Die YouTube Mobile App unterstützt nicht das Anzeigen von Transkripten, aber Sie können Untertitel über die "CC"-Schaltfläche aktivieren.[](https://riverside.fm/blog/youtube-transcription)
- Einige Drittanbieter-Tools oder API-Methoden funktionieren möglicherweise nicht für automatisch generierte Untertitel oder eingeschränkte Videos.[](https://stackoverflow.com/questions/9611397/how-to-extract-closed-caption-transcript-from-youtube-video)

Wenn Sie Untertitel für ein bestimmtes Video oder in einem bestimmten Format benötigen, lassen Sie es mich wissen, und ich kann Sie weiter unterstützen!