---
audio: false
generated: true
lang: de
layout: post
title: Erstelle Lehrvideos mit Python
translated: true
type: note
---

Um kurze Bildungsvideos mit schwarzem Hintergrund und Untertiteln, die mit einer aus Text generierten Audiospur synchronisiert sind, zu erstellen, können Sie Python verwenden, um den Prozess zu orchestrieren. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung und ein Python-Skript, das dies umsetzt. Das Skript wird:
1.  Die DeepSeek API verwenden, um ein Skript zu generieren oder zu verfeinern (unter der Annahme, dass Sie den Bildungsinhalt bereitstellen).
2.  Die Google Cloud Text-to-Speech API verwenden, um das Skript in Audio umzuwandeln.
3.  Eine Bibliothek wie `moviepy` verwenden, um ein Video mit schwarzem Hintergrund und mit dem Audio synchronisierten Untertiteln zu erstellen.

### Voraussetzungen
-   **DeepSeek API-Schlüssel**: Melden Sie sich bei [DeepSeek](https://api-docs.deepseek.com/) an und erhalten Sie einen API-Schlüssel.
-   **Google Cloud Text-to-Speech API**:
    -   Richten Sie ein Google Cloud-Projekt ein und aktivieren Sie die Text-to-Speech API.
    -   Erstellen Sie ein Servicekonto und laden Sie die JSON-Anmeldedatei herunter.
    -   Installieren Sie die Google Cloud Text-to-Speech Client-Bibliothek: `pip install google-cloud-texttospeech`.
-   **Python-Bibliotheken**:
    -   Installieren Sie die erforderlichen Bibliotheken: `pip install openai moviepy requests`.
-   **FFmpeg**: Stellen Sie sicher, dass FFmpeg installiert ist, damit `moviepy` das Video-Rendering verarbeiten kann (laden Sie es von der [FFmpeg-Website](https://ffmpeg.org/) herunter oder installieren Sie es über einen Paketmanager).

### Schritte
1.  **Skript mit der DeepSeek API generieren oder verfeinern**: Verwenden Sie DeepSeek, um das Bildungsskript zu erstellen oder zu optimieren und stellen Sie sicher, dass es prägnant ist und für ein 1-minütiges Video geeignet ist.
2.  **Text mit Google Cloud Text-to-Speech in Audio umwandeln**: Teilen Sie das Skript in Absätze auf, generieren Sie Audio für jeden und speichern Sie sie als separate Audiodateien.
3.  **Video mit MoviePy erstellen**: Erstellen Sie ein Video mit schwarzem Hintergrund, zeigen Sie Untertitel für jeden Absatz an, die mit dem Audio synchronisiert sind, und kombinieren Sie sie zu einem endgültigen 1-minütigen Video.

### Python-Skript
Das folgende Skript geht davon aus, dass Sie eine Textdatei mit dem Bildungsinhalt (Absätzen) haben und ein Video mit schwarzem Hintergrund und Untertiteln generieren.

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# Umgebungsvariablen setzen
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pfad/zu/ihren/google-credentials.json"  # Aktualisieren Sie mit dem Pfad zu Ihrer Anmeldedatei
DEEPSEEK_API_KEY = "ihr_deepseek_api_schluessel"  # Aktualisieren Sie mit Ihrem DeepSeek API-Schlüssel

# DeepSeek-Client initialisieren
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# Funktion zum Verfeinern des Skripts mit DeepSeek
def refine_script_with_deepseek(script):
    prompt = f"""
    Sie sind ein erfahrener Skriptautor für Bildungsvideos. Verfeinern Sie das folgende Skript, damit es prägnant, klar und fesselnd für ein 1-minütiges Bildungsvideo ist. Stellen Sie sicher, dass es für gesprochene Erzählung geeignet ist und in 60 Sekunden passt, wenn es in einem natürlichen Tempo gesprochen wird. Teilen Sie das Skript in 2-3 kurze Absätze für die Untertitelanzeige auf. Geben Sie das verfeinerte Skript als Liste von Absätzen zurück.

    Original-Skript:
    {script}

    Ausgabeformat:
    ["Absatz 1", "Absatz 2", "Absatz 3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # Konvertiere String in Liste
    return refined_script

# Funktion zum Generieren von Audio für jeden Absatz mit Google Cloud Text-to-Speech
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # Eine natürlich klingende englische Stimme
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        audio_file = os.path.join(output_dir, f"paragraph_{i+1}.mp3")
        with open(audio_file, "wb") as out:
            out.write(response.audio_content)
        audio_files.append(audio_file)
    return audio_files

# Funktion zum Erstellen eines Videos mit Untertiteln und schwarzem Hintergrund
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # Text-Clip für Untertitel erstellen
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # Standard HD-Auflösung
            method="caption",
            align="center"
        )
        # Audio laden und dessen Dauer abrufen
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # Dauer des Text-Clips an die Audio-Dauer anpassen
        text_clip = text_clip.set_duration(duration)
        # Clip mit schwarzem Hintergrund erstellen
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # Text und Hintergrund kombinieren
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # Audio zum Video-Clip hinzufügen
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # Alle Clips verketten
    final_clip = concatenate_videoclips(clips)
    # Endgültiges Video schreiben
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# Hauptfunktion
def main():
    # Beispiel-Eingabeskript (ersetzen Sie dies mit Ihrem Bildungsinhalt)
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # Schritt 1: Skript mit DeepSeek verfeinern
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Verfeinertes Skript:", refined_paragraphs)
    
    # Schritt 2: Audio für jeden Absatz generieren
    audio_files = generate_audio(refined_paragraphs)
    print("Audiodateien generiert:", audio_files)
    
    # Schritt 3: Video mit Untertiteln und schwarzem Hintergrund erstellen
    create_video(refined_paragraphs, audio_files)
    print("Video erstellt: educational_video.mp4")

if __name__ == "__main__":
    main()

```

### Verwendung
1.  **Anmeldedaten einrichten**:
    -   Ersetzen Sie `"pfad/zu/ihren/google-credentials.json"` durch den Pfad zu Ihrer Google Cloud Service Account JSON-Datei.
    -   Ersetzen Sie `"ihr_deepseek_api_schluessel"` durch Ihren DeepSeek API-Schlüssel.
2.  **Eingabeskript vorbereiten**:
    -   Modifizieren Sie die Variable `input_script` in der Funktion `main()` mit Ihrem Bildungsinhalt. Das Skript sollte ein einzelner String mit dem vollständigen Text sein, den Sie in ein Video umwandeln möchten.
3.  **Skript ausführen**:
    -   Speichern Sie das Skript als `create_educational_video.py` und führen Sie es mit `python create_educational_video.py` aus.
    -   Das Skript wird:
        -   Das Skript mit der DeepSeek API verfeinern, um sicherzustellen, dass es prägnant ist und in 2-3 Absätze aufgeteilt wird.
        -   MP3-Audiodateien für jeden Absatz mit Google Cloud Text-to-Speech generieren.
        -   Ein Video mit schwarzem Hintergrund erstellen, das jeden Absatz als Untertitel anzeigt, die mit dem entsprechenden Audio synchronisiert sind.
4.  **Ausgabe**:
    -   Das endgültige Video wird als `educational_video.mp4` im gleichen Verzeichnis wie das Skript gespeichert.
    -   Die Audiodateien für jeden Absatz werden im Verzeichnis `audio` gespeichert.

### Anmerkungen
-   **DeepSeek API**: Das Skript verwendet das `deepseek-chat`-Modell, um das Skript zu verfeinern. Stellen Sie sicher, dass Ihr API-Schlüssel gültig ist und Sie über ausreichend Guthaben verfügen. Die DeepSeek API wird hier verwendet, um das Skript für die Video-Erzählung zu strukturieren, da sie sich in der Textgenerierung und -optimierung auszeichnet.[](https://www.datacamp.com/tutorial/deepseek-api)
-   **Google Cloud Text-to-Speech**: Das Skript verwendet die Stimme `en-US-Wavenet-D` für natürlich klingende englische Erzählung. Sie können die Stimme ändern, indem Sie den `name`-Parameter in `VoiceSelectionParams` modifizieren (siehe Google Cloud Text-to-Speech-Dokumentation für andere Stimmoptionen).
-   **MoviePy**: Das Video wird in 1280x720 Auflösung (HD) erstellt. Sie können den `size`-Parameter in `TextClip` und `ColorClip` für andere Auflösungen anpassen.
-   **Timing**: Das Skript stellt sicher, dass die Untertitel mit dem Audio synchronisiert sind, indem die Dauer des Text-Clips an die Audio-Dauer angepasst wird. Für ein 1-minütiges Video erzwingt der DeepSeek-Prompt ein prägnantes Skript.
-   **Abhängigkeiten**: Stellen Sie sicher, dass FFmpeg installiert und in Ihrem System-PATH zugänglich ist, damit `moviepy` korrekt funktioniert.

### Beispielausgabe
Wenn Ihr Eingabeskript über Machine Learning handelt, könnte das verfeinerte Skript so aussehen:
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
-   Für jeden Absatz wird eine Audiodatei generiert (z.B. `paragraph_1.mp3`, `paragraph_2.mp3`, usw.).
-   Das endgültige Video zeigt einen schwarzen Hintergrund mit weißen Untertiteln, die sequenziell erscheinen und mit der Audio-Erzählung synchronisiert sind.

Dieser Ansatz ist einfach, kosteneffektiv und erzeugt professionell aussehende Bildungsvideos, die für Plattformen wie YouTube oder Bildungswebsites geeignet sind. Wenn Sie weitere Anpassungen benötigen (z.B. andere Schriftarten, Untertitelstile oder zusätzliche Effekte), lassen Sie es mich wissen!