---
audio: false
generated: true
lang: de
layout: post
title: Verbesserung der Audioqualität in yt-dlp
translated: true
type: note
---

Um Ihr Problem mit der Audioqualität beim Herunterladen von YouTube-Videos mit Ihrem Skript und `yt-dlp` anzugehen, zeige ich Ihnen, wie Sie das Skript ändern können, um sicherzustellen, dass es **immer die bestmögliche Audioqualität** herunterlädt, unabhängig von der gewählten Videoauflösung (720p oder 480p). Lassen Sie uns das Schritt für Schritt durchgehen und eine klare Lösung bereitstellen.

### Das aktuelle Skript verstehen
Ihr Skript verwendet `yt-dlp`, um YouTube-Videos herunterzuladen, und ermöglicht es Ihnen, eine Auflösung (720p oder 480p) anzugeben. Die Formatauswahl wird durch die Variable `format_str` gesteuert, die an die Option `-f` in `yt-dlp` übergeben wird. Hier ist, was es aktuell tut:

- **Für 720p**: `format_str = 'bestvideo[height<=720]+bestaudio/best[height<=720]'`
- **Für 480p**: `format_str = 'bestvideo[height<=480]+bestaudio/best[height<=720]'`

In `yt-dlp`:
- `bestvideo[height<=720]` wählt den besten Videostream mit einer Höhe von 720 Pixeln oder weniger aus.
- `bestaudio` wählt den besten reinen Audio-Stream aus, typischerweise den mit der höchsten Bitrate.
- Der `+`-Operator weist `yt-dlp` an, die Video- und Audiostreams separat herunterzuladen und sie zu einer einzelnen Datei zusammenzuführen.
- Der `/`-Operator bietet einen Fallback: Wenn die Kombination davor (z.B. `bestvideo[height<=720]+bestaudio`) nicht verfügbar ist, wird das Format danach verwendet (z.B. `best[height<=720]`), welches das beste Einzelformat ist, das sowohl Video als auch Audio bis zu 720p enthält.

Da `bestaudio` enthalten ist, sollte das Skript bereits die beste verfügbare Audioqualität auswählen. Dennoch ist Ihnen aufgefallen, dass die Audioqualität "weniger gut" erscheint. Lassen Sie uns untersuchen, warum das so sein könnte und wie man es behebt.

### Warum die Audioqualität suboptimal sein könnte
Obwohl `bestaudio` verwendet wird, gibt es ein mögliches Problem:
- Die Fallback-Option (`best[height<=720]`) könnte in seltenen Fällen ausgelöst werden, in denen separate Video- und Audiostreams nicht wie angegeben kombiniert werden können. Dieser Fallback wählt ein kombiniertes Video+Audio-Format aus, das eine niedrigere Audioqualität haben könnte (z.B. 128kbps anstelle eines separaten 256kbps-Audiostreams).
- Im Fall von 480p ist der Fallback `best[height<=720]`, was inkonsistent ist – es könnte ein 720p-Video heruntergeladen werden, wenn Sie 480p angefordert haben, und die Audioqualität in diesem kombinierten Format ist möglicherweise nicht die beste.

Da YouTube typischerweise separate Video- und Audiostreams bereitstellt, sollte die Kombination `bestvideo + bestaudio` fast immer funktionieren. Um jedoch die beste Audioqualität zu garantieren und einen Fallback auf ein potenziell qualitativ minderwertigeres kombiniertes Format zu vermeiden, können wir das Skript verfeinern.

### Lösung: Sicherstellen der besten Audioqualität
Um sicherzustellen, dass `yt-dlp` immer die beste Audioqualität herunterlädt:
1. **Verwenden Sie `bestaudio` ohne Fallback**: Dies zwingt `yt-dlp` dazu, den besten verfügbaren Audiostream zusammen mit dem besten Videostream bis zur gewählten Auflösung herunterzuladen. Wenn diese Kombination nicht möglich ist, bricht der Vorgang mit einem Fehler ab, anstatt bei der Audioqualität Kompromisse einzugehen, was akzeptabel ist, da YouTube-Videos fast immer separate Streams haben.
2. **Beheben Sie die Inkonsistenz beim 480p-Fallback**: Gleichen Sie den Fallback (falls beibehalten) mit der angefragten Auflösung ab, wobei es einfacher ist, ihn zu entfernen, was Ihrem Ziel entspricht.

So ändern Sie das Skript:

#### Modifizierter Code
Aktualisieren Sie die `format_str`-Definitionen in Ihrem Skript wie folgt:

```python
import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos at specified resolution.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--resolution",
        choices=["720p", "480p"],
        default="720p",
        help="Video resolution to download (default: 720p)"
    )
    args = parser.parse_args()

    output_dir = "test"
    os.makedirs(output_dir, exist_ok=True)

    # Aktualisierte Format-Strings, um die beste Audioqualität sicherzustellen
    if args.resolution == "720p":
        format_str = 'bestvideo[height<=720]+bestaudio'
    else:  # 480p
        format_str = 'bestvideo[height<=480]+bestaudio'

    command = [
        "yt-dlp",
        "--cookies-from-browser", "firefox",
        "-f", format_str,
        "-P", output_dir,
        args.url
    ]

    subprocess.run(command)

if __name__ == "__main__":
    main()
```

#### Erläuterung der Änderungen
- **720p**: Geändert von `'bestvideo[height<=720]+bestaudio/best[height<=720]'` zu `'bestvideo[height<=720]+bestaudio'`.
- **480p**: Geändert von `'bestvideo[height<=480]+bestaudio/best[height<=720]'` zu `'bestvideo[height<=480]+bestaudio'`.
- **Fallback entfernt (`/best[height<=...]`)**: Dies stellt sicher, dass `yt-dlp` immer den besten Audiostream (`bestaudio`) verwendet, anstatt möglicherweise auf ein kombiniertes Format mit niedrigerer Audioqualität zurückzufallen.

### Warum das funktioniert
- **`bestaudio`**: Wählt den Audiostream mit der höchsten Bitrate aus (z.B. Opus mit 160kbps oder AAC mit 256kbps, abhängig vom Video) und stellt so die bestmögliche Audioqualität sicher.
- **Kein Fallback**: Durch das Entfernen von `/best[height<=720]` verhindern Sie, dass `yt-dlp` ein kombiniertes Format herunterlädt, das möglicherweise minderwertiges Audio enthält. Da YouTube-Videos typischerweise separate Streams haben, sollte `bestvideo + bestaudio` immer erfolgreich sein.
- **Auflösung respektiert**: Die Videoauflösung bleibt innerhalb Ihrer Wahl (720p oder 480p), während die Audioqualität maximiert wird.

### Überprüfen des Ergebnisses
Um zu bestätigen, dass Sie das beste Audio erhalten:
1. **Verfügbare Formate prüfen**: Führen Sie `yt-dlp --list-formats <youtube_url>` aus, um die verfügbaren Video- und Audiostreams für ein bestimmtes Video zu sehen. Suchen Sie nach den reinen Audioformaten (z.B. `m4a`, `webm`) und deren Bitraten.
2. **Den Download überwachen**: Wenn Sie das Skript ausführen, gibt `yt-dlp` aus, welche Formate es herunterlädt (z.B. "Downloading video stream (code)" und "Downloading audio stream (code)"). Stellen Sie sicher, dass es einen separaten Audiostream mit einer hohen Bitrate auswählt.
3. **Die Wiedergabe testen**: Spielen Sie die heruntergeladene Datei ab und überprüfen Sie die Audioqualität. Wenn sie immer noch schlecht ist, könnte das beste verfügbare Audio des Videos durch den Uploader begrenzt sein, nicht durch das Skript.

### Was, wenn es fehlschlägt?
Wenn `yt-dlp` einen Fehler ausgibt, weil `bestvideo[height<=720]+bestaudio` nicht verfügbar ist (sehr unwahrscheinlich bei YouTube), könnten Sie:
- Einen Fallback wie `/best[height<=720]'` wieder hinzufügen, aber dies könnte die Audioqualität beeinträchtigen, was Sie vermeiden möchten.
- Das spezifische Video mit `--list-formats` untersuchen und das Skript für diesen Fall anpassen, was jedoch selten nötig ist.

### Schlussfolgerung
Ihr Skript ist nun so eingestellt, dass es immer die bestmögliche Audioqualität herunterlädt, indem es `bestaudio` ohne Fallback zusammen mit Ihrer gewählten Videoauflösung verwendet. Die modifizierten `format_str`-Werte sind:

- Für 720p: `'bestvideo[height<=720]+bestaudio'`
- Für 480p: `'bestvideo[height<=480]+bestaudio'`

Diese Änderung sollte Ihr Problem lösen und die höchstmögliche Audioqualität innerhalb Ihrer Auflösungspräferenzen sicherstellen. Wenn das Audio immer noch mangelhaft erscheint, könnte es an der ursprünglichen Upload-Qualität des Videos liegen, was außerhalb der Kontrolle des Skripts liegt. Probieren Sie es aus und lassen Sie mich wissen, wie es funktioniert!