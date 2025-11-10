---
audio: false
generated: true
lang: fr
layout: post
title: Créer des vidéos éducatives avec Python
translated: true
type: note
---

Pour créer des vidéos éducatives courtes avec un fond noir et des sous-titres synchronisés avec l'audio généré à partir de texte en utilisant l'API DeepSeek et l'API Google Cloud Text-to-Speech, vous pouvez utiliser Python pour orchestrer le processus. Voici un guide étape par étape et un script Python qui réalise cela. Le script va :
1. Utiliser l'API DeepSeek pour générer ou affiner un script (en supposant que vous fournissez le contenu éducatif).
2. Utiliser l'API Google Cloud Text-to-Speech pour convertir le script en audio.
3. Utiliser une bibliothèque comme `moviepy` pour créer une vidéo avec un fond noir et des sous-titres synchronisés avec l'audio.

### Prérequis
- **Clé API DeepSeek** : Inscrivez-vous sur [DeepSeek](https://api-docs.deepseek.com/) et obtenez une clé API.
- **API Google Cloud Text-to-Speech** :
  - Configurez un projet Google Cloud et activez l'API Text-to-Speech.
  - Créez un compte de service et téléchargez le fichier JSON d'identification.
  - Installez la bibliothèque cliente Google Cloud Text-to-Speech : `pip install google-cloud-texttospeech`.
- **Bibliothèques Python** :
  - Installez les bibliothèques requises : `pip install openai moviepy requests`.
- **FFmpeg** : Assurez-vous que FFmpeg est installé pour que `moviepy` puisse gérer le rendu vidéo (téléchargez-le depuis le [site web de FFmpeg](https://ffmpeg.org/) ou installez-le via un gestionnaire de paquets).

### Étapes
1. **Générer ou affiner le script avec l'API DeepSeek** : Utilisez DeepSeek pour créer ou peaufiner le script éducatif, en veillant à ce qu'il soit concis et adapté à une vidéo d'une minute.
2. **Convertir le texte en audio avec Google Cloud Text-to-Speech** : Divisez le script en paragraphes, générez l'audio pour chacun et enregistrez-les dans des fichiers audio séparés.
3. **Créer la vidéo avec MoviePy** : Générez une vidéo avec un fond noir, affichez les sous-titres pour chaque paragraphe synchronisés avec l'audio et combinez-les en une vidéo finale d'une minute.

### Script Python
Le script suivant suppose que vous avez un fichier texte avec le contenu éducatif (paragraphes) et génère une vidéo avec un fond noir et des sous-titres.

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# Configurer les variables d'environnement
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chemin/vers/votre/google-credentials.json"  # Mettez à jour avec le chemin de votre fichier d'identification
DEEPSEEK_API_KEY = "votre_cle_api_deepseek"  # Mettez à jour avec votre clé API DeepSeek

# Initialiser le client DeepSeek
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# Fonction pour affiner le script avec DeepSeek
def refine_script_with_deepseek(script):
    prompt = f"""
    Vous êtes un scénariste expert pour les vidéos éducatives. Affinez le script suivant pour qu'il soit concis, clair et engageant pour une vidéo éducative d'une minute. Assurez-vous qu'il est adapté à une narration parlée et tient dans 60 secondes lorsqu'il est parlé à un rythme naturel. Divisez le script en 2-3 courts paragraphes pour l'affichage des sous-titres. Renvoyez le script affiné sous forme de liste de paragraphes.

    Script original :
    {script}

    Format de sortie :
    ["paragraphe 1", "paragraphe 2", "paragraphe 3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # Convertir la chaîne en liste
    return refined_script

# Fonction pour générer l'audio pour chaque paragraphe en utilisant Google Cloud Text-to-Speech
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # Une voix anglaise naturelle
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

# Fonction pour créer la vidéo avec sous-titres et fond noir
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # Créer un clip texte pour les sous-titres
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # Résolution HD standard
            method="caption",
            align="center"
        )
        # Charger l'audio et obtenir sa durée
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # Définir la durée du clip texte pour correspondre à l'audio
        text_clip = text_clip.set_duration(duration)
        # Créer un clip de fond noir
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # Combiner le texte et le fond
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # Ajouter l'audio au clip vidéo
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # Concaténer tous les clips
    final_clip = concatenate_videoclips(clips)
    # Écrire la vidéo finale
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# Fonction principale
def main():
    # Exemple de script d'entrée (remplacez par votre contenu éducatif)
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # Étape 1 : Affiner le script avec DeepSeek
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Script affiné :", refined_paragraphs)
    
    # Étape 2 : Générer l'audio pour chaque paragraphe
    audio_files = generate_audio(refined_paragraphs)
    print("Fichiers audio générés :", audio_files)
    
    # Étape 3 : Créer la vidéo avec sous-titres et fond noir
    create_video(refined_paragraphs, audio_files)
    print("Vidéo créée : educational_video.mp4")

if __name__ == "__main__":
    main()

```

### Comment utiliser
1. **Configurer les identifiants** :
   - Remplacez `"chemin/vers/votre/google-credentials.json"` par le chemin vers votre fichier JSON de compte de service Google Cloud.
   - Remplacez `"votre_cle_api_deepseek"` par votre clé API DeepSeek.
2. **Préparer le script d'entrée** :
   - Modifiez la variable `input_script` dans la fonction `main()` avec votre contenu éducatif. Le script doit être une chaîne unique avec le texte complet que vous souhaitez convertir en vidéo.
3. **Exécuter le script** :
   - Enregistrez le script sous `create_educational_video.py` et exécutez-le avec `python create_educational_video.py`.
   - Le script va :
     - Affiner le script en utilisant l'API DeepSeek pour s'assurer qu'il est concis et divisé en 2-3 paragraphes.
     - Générer des fichiers audio MP3 pour chaque paragraphe en utilisant Google Cloud Text-to-Speech.
     - Créer une vidéo avec un fond noir, affichant chaque paragraphe comme sous-titre synchronisé avec son audio correspondant.
4. **Sortie** :
   - La vidéo finale sera enregistrée sous `educational_video.mp4` dans le même répertoire que le script.
   - Les fichiers audio pour chaque paragraphe seront enregistrés dans le répertoire `audio`.

### Notes
- **API DeepSeek** : Le script utilise le modèle `deepseek-chat` pour affiner le script. Assurez-vous que votre clé API est valide et que vous avez suffisamment de crédits. L'API DeepSeek est utilisée ici pour structurer le script pour la narration vidéo, car elle excelle dans la génération et l'optimisation de texte.
- **Google Cloud Text-to-Speech** : Le script utilise la voix `en-US-Wavenet-D` pour une narration anglaise naturelle. Vous pouvez changer la voix en modifiant le paramètre `name` dans `VoiceSelectionParams` (voir la documentation Google Cloud Text-to-Speech pour d'autres options de voix).
- **MoviePy** : La vidéo est créée en résolution 1280x720 (HD). Vous pouvez ajuster le paramètre `size` dans `TextClip` et `ColorClip` pour différentes résolutions.
- **Timing** : Le script assure la synchronisation des sous-titres avec l'audio en définissant la durée du clip texte pour correspondre à la durée de l'audio. Pour une vidéo d'une minute, l'invite DeepSeek impose un script concis.
- **Dépendances** : Assurez-vous que FFmpeg est installé et accessible dans le PATH de votre système pour que `moviepy` fonctionne correctement.

### Exemple de sortie
Si votre script d'entrée concerne le machine learning, le script affiné pourrait ressembler à :
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
- Chaque paragraphe génère un fichier audio (par exemple, `paragraph_1.mp3`, `paragraph_2.mp3`, etc.).
- La vidéo finale montre un fond noir avec des sous-titres blancs apparaissant séquentiellement, synchronisés avec la narration audio.

Cette approche est simple, économique et produit des vidéos éducatives d'aspect professionnel adaptées à des plateformes comme YouTube ou des sites web éducatifs. Si vous avez besoin de personnalisations supplémentaires (par exemple, différentes polices, styles de sous-titres ou effets supplémentaires), faites-le moi savoir !