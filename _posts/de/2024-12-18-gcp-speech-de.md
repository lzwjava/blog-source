---
audio: false
generated: false
lang: de
layout: post
title: Erste Schritte mit der Google Text-to-Speech API
translated: true
---

Ich plane, einige Artikel von Yin Wang mit der Google Text-to-Speech API in Audio umzuwandeln. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung sowie einige hilfreiche Tutorials, die von ChatGPT bereitgestellt wurden. Sobald alles fertig ist, werde ich das Audio hier hochladen, damit Sie es anhören können.

---

### Schritt 1: Google Cloud-Konto einrichten

1. Erstellen Sie ein Google Cloud-Konto  
   Falls Sie noch keines besitzen, registrieren Sie sich bei der [Google Cloud Console](https://console.cloud.google.com/).

2. Erstellen Sie ein neues Projekt  
   - Klicken Sie in der Cloud-Konsole auf das Dropdown-Menü für Projekte (oben links).
   - Wählen Sie „Neues Projekt“, geben Sie ihm einen Namen und erstellen Sie das Projekt.

3. Aktivieren Sie die Text-to-Speech API  
   - Besuchen Sie die [Google Cloud Text-to-Speech API-Seite](https://cloud.google.com/text-to-speech).  
   - Klicken Sie auf "Aktivieren", um die API für Ihr Projekt zu aktivieren.

4. API-Zugangsdaten erstellen  
   - Navigieren Sie in der Cloud Console zu APIs & Dienste > Zugangsdaten.  
   - Klicken Sie auf „Zugangsdaten erstellen“ und wählen Sie dann „Dienstkonto“.  
   - Folgen Sie den Anweisungen, um das Dienstkonto zu erstellen, und laden Sie die private Schlüsseldatei im JSON-Format herunter.  
   - Bewahren Sie diese JSON-Datei sicher auf, da sie zur Authentifizierung Ihrer API-Anfragen verwendet wird.

---

### Schritt 2: Google Cloud SDK und Client-Bibliothek installieren

1. Installiere Google Cloud SDK  
   Falls du es noch nicht getan hast, folge den Anweisungen, um das [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) für dein Betriebssystem zu installieren.

2. Installieren Sie die Python-Client-Bibliothek  
   Wenn Sie Python verwenden, installieren Sie die `google-cloud-texttospeech`-Bibliothek mit:

```bash
pip install google-cloud-texttospeech
```

---

### Schritt 3: Authentifizierung einrichten

Bevor Sie die API verwenden, müssen Sie sich mit Ihren Anmeldeinformationen authentifizieren. Setzen Sie die Umgebungsvariable auf den Pfad zu Ihrer Anmeldeinformationsdatei:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/pfad/zu/deiner/service-account-datei.json"
```

Ersetzen Sie den Pfad durch den tatsächlichen Speicherort Ihrer heruntergeladenen JSON-Datei.

---

### Schritt 4: Implementierung der Text-zu-Sprache-Umwandlung

Hier ist ein Python-Beispiel, um Text in Sprache umzuwandeln, indem die Google Cloud Text-to-Speech API verwendet wird:

```python
from google.cloud import texttospeech
```

```python
def text_to_speech(text, output_filename):
    # Initialisiere den Text-zu-Sprache-Client
    client = texttospeech.TextToSpeechClient()
```

    # Setzen Sie den Synthese-Eingang
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Stimmparameter festlegen (mit 'en-US-Journey-D')
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # Englisch (Vereinigte Staaten)
        name="en-US-Journey-D"  # Spezifisches Stimmmodel (Journey)
    )

    # Audio-Konfiguration festlegen
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # MP3-Format
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # Optimiert für Bluetooth-Lautsprecher
        pitch=0.0,  # Keine Tonhöhenänderung
        speaking_rate=0.9,  # Angepasste Sprechgeschwindigkeit (kann bei Bedarf geändert werden)
        volume_gain_db=5.0  # Lautere Lautstärke
    )

    # Führe die Text-zu-Sprache-Anfrage aus
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Schreiben Sie den Audioinhalt in eine Datei
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"Audiocontent wurde in {output_filename} geschrieben")

# Beispielverwendung
article_text = "Filme, oh mein Gott, ich liebe sie einfach absolut. Sie sind wie Zeitmaschinen, die dich in verschiedene Welten und Landschaften entführen, und ich kann einfach nicht genug davon bekommen."
output_file = "output_audio.mp3"  # Ausgabe im MP3-Format

# Text in Sprache umwandeln
text_to_speech(article_text, output_file)
```

---

### Schritt 5: Das Skript ausführen

1. Speichern Sie das Skript als `text_to_speech.py`.
2. Führen Sie das Skript aus mit:

   ```bash
   python text_to_speech.py
   ```

Dadurch wird eine Audiodatei (`output_audio.mp3`) aus dem bereitgestellten Text generiert.

---

### Schritt 6: Dienstkonto-Schlüssel

Der JSON-Schlüssel für Ihr Dienstkonto sollte in etwa so aussehen:

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "your-private-key",
  "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your-client-cert-url"
}
```

---

### Warum Journey wählen?

Google Cloud Text-to-Speech bietet mehrere Stimmen an, aber Journey sticht durch seinen natürlichen, menschenähnlichen Klang hervor. Im Gegensatz zu anderen Modellen, die oft roboterhaft klingen, überzeugt Journey durch Ausdrucksstärke und lebensechte Wiedergabe. Es eignet sich besonders gut für langformatige Inhalte wie Podcasts, Hörbücher oder Anwendungen, die einen eher gesprächigen Ton erfordern.

Hauptmerkmale von Journey:
- Natürliche Sprache: Klingt eher wie eine menschliche Stimme.
- Ausdrucksstärke: Passt Tonfall und Betonung basierend auf dem Kontext an.
- Ideal für Langform-Inhalte: Perfekt für Podcasts und Erzählungen.

Weitere Details zu den Vorteilen von Google Cloud Text-to-Speech finden Sie in der [Google Cloud-Übersicht](https://cloud.google.com/text-to-speech#benefits).

---

### Schritt 7: Einen neuen Dienstkontoschlüssel generieren (falls erforderlich)

Wenn Ihr Dienstkontoschlüssel nicht mit dem obigen Beispiel übereinstimmt, können Sie einen neuen über die Google Cloud Console generieren.

Um einen neuen Schlüssel zu generieren:
1. Gehen Sie zur [Google Cloud Console](https://console.cloud.google.com/).
2. Navigieren Sie zu IAM & Admin > Dienstkonten.
3. Erstellen Sie ein neues Dienstkonto:
   - Klicken Sie auf "Dienstkonto erstellen" und weisen Sie die entsprechenden Rollen zu.
   - Klicken Sie auf "Erstellen".
4. Generieren Sie einen Schlüssel:
   - Nachdem Sie das Dienstkonto erstellt haben, klicken Sie darauf.
   - Gehen Sie zum Reiter "Schlüssel", klicken Sie auf "Schlüssel hinzufügen" und wählen Sie JSON. Laden Sie dann den Schlüssel herunter.

---

### Beispiel für Audioausgabe

Sobald alles eingerichtet ist, können Sie eine Audiodatei generieren, die hier verfügbar sein wird:  
[Laden Sie die Audiodatei herunter](assets/audios/output-audio.mp3).

---

### Fazit

Die Google Cloud Text-to-Speech API macht es einfach, Text in natürlich klingende Sprache umzuwandeln. Egal, ob Sie eine App entwickeln, die Sprachausgabe benötigt, oder einfach nur mit Text-zu-Sprache experimentieren möchten, diese API bietet leistungsstarke Funktionen und Anpassungsmöglichkeiten. Erkunden Sie die vollständige Dokumentation, um zusätzliche Sprachauswahlen, Sprachen und erweiterte Funktionen zu entdecken.