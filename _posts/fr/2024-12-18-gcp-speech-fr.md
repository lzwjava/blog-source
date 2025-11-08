---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Débuter avec l'API Google Text-to-Speech
translated: true
type: post
---

Je prévois de convertir certains articles de Yin Wang en audio en utilisant l'API Google Text-to-Speech. Voici un guide étape par étape, accompagné de quelques tutoriels utiles fournis par ChatGPT. Une fois que tout sera prêt, je téléverserai l'audio ici pour que vous puissiez l'écouter.

---

### Étape 1 : Configurer un compte Google Cloud

1. Créez un compte Google Cloud  
   Si vous n'en avez pas encore, inscrivez-vous sur la [Google Cloud Console](https://console.cloud.google.com/).

2. Créer un Nouveau Projet  
   - Dans la Console Cloud, cliquez sur le menu déroulant des projets (en haut à gauche).  
   - Sélectionnez "Nouveau projet", donnez-lui un nom, puis créez le projet.

3. Activer l'API Text-to-Speech  
   - Rendez-vous sur la [page de l'API Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech).  
   - Cliquez sur "Activer" pour activer l'API pour votre projet.

4. Créer des identifiants API  
   - Accédez à APIs & Services > Credentials dans la Cloud Console.  
   - Cliquez sur Create Credentials, puis sélectionnez Service Account.  
   - Suivez les instructions pour créer le compte de service et téléchargez le fichier de clé privée au format JSON.  
   - Conservez ce fichier JSON en lieu sûr, car il est utilisé pour authentifier vos requêtes API.

---

### Étape 2 : Installer Google Cloud SDK et la bibliothèque cliente

1. Installez Google Cloud SDK  
   Si vous ne l'avez pas encore fait, suivez les instructions pour installer le [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) pour votre système d'exploitation.

2. Installez la bibliothèque cliente Python  
   Si vous utilisez Python, installez la bibliothèque `google-cloud-texttospeech` avec :

   ```bash
   pip install google-cloud-texttospeech
   ```

---

### Étape 3 : Configurer l'authentification

Avant d'utiliser l'API, vous devez vous authentifier avec vos identifiants. Définissez la variable d'environnement sur le chemin de votre fichier d'identifiants :

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/chemin/vers/votre/fichier-de-compte-de-service.json"
```

Remplacez le chemin par l'emplacement réel de votre fichier JSON téléchargé.

---

### Étape 4 : Mettre en œuvre la conversion texte-parole

Voici un exemple en Python pour convertir du texte en parole en utilisant l'API Google Cloud Text-to-Speech :

```python
from google.cloud import texttospeech
```

```python
def text_to_speech(text, output_filename):
    # Initialiser le client de synthèse vocale
    client = texttospeech.TextToSpeechClient()
```

    # Configurer l'entrée de synthèse
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Définir les paramètres de la voix (en utilisant 'en-US-Journey-D')
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # Anglais (États-Unis)
        name="en-US-Journey-D"  # Modèle de voix spécifique (Journey)
    )

    # Configuration de l'audio
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # Format MP3
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # Optimisé pour les enceintes Bluetooth
        pitch=0.0,  # Aucune modification de la hauteur
        speaking_rate=0.9,  # Vitesse de parole ajustée (peut être modifiée si nécessaire)
        volume_gain_db=5.0  # Volume plus élevé
    )

    # Effectuer la requête de synthèse vocale
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Écrire le contenu audio dans un fichier
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"Contenu audio écrit dans {output_filename}")

# Exemple d'utilisation
article_text = "Les films, oh mon Dieu, je les adore absolument. Ils sont comme des machines à voyager dans le temps qui vous emmènent dans des mondes et des paysages différents, et je ne m'en lasse jamais."
output_file = "output_audio.mp3"  # Sortie au format MP3

# Convertir du texte en parole
text_to_speech(article_text, output_file)
```

---

### Étape 5 : Exécuter le Script

1. Enregistrez le script sous le nom `text_to_speech.py`.
2. Exécutez le script avec :

```bash
python text_to_speech.py
```

Cela générera un fichier audio (`output_audio.mp3`) à partir du texte fourni.

---

### Étape 6 : Clé de compte de service

La clé JSON de votre compte de service devrait ressembler à ceci :

```json
{
  "type": "service_account",
  "project_id": "votre-project-id",
  "private_key_id": "votre-private-key-id",
  "private_key": "votre-private-key",
  "client_email": "votre-service-account-email@votre-project-id.iam.gserviceaccount.com",
  "client_id": "votre-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "votre-client-cert-url"
}
```

---

### Pourquoi choisir Journey ?

Google Cloud Text-to-Speech propose plusieurs voix, mais Journey se distingue par son son naturel et proche de celui d'un humain. Contrairement à d'autres modèles qui ont souvent un ton robotique, Journey excelle dans l'expressivité et la livraison réaliste. Il est particulièrement adapté pour les contenus longs tels que les podcasts, les livres audio ou toute application nécessitant un ton plus conversationnel.

Caractéristiques clés de Journey :
- Parole naturelle : Sonne plus proche d'une voix humaine.
- Expressivité : Ajuste le ton et l'intonation en fonction du contexte.
- Idéal pour le contenu long : Parfait pour les podcasts et les narrations.

Pour plus de détails sur les avantages de Google Cloud Text-to-Speech, consultez la [présentation de Google Cloud](https://cloud.google.com/text-to-speech#benefits).

---

### Étape 7 : Générer une nouvelle clé de compte de service (si nécessaire)

Si votre clé de compte de service ne correspond pas à l'exemple ci-dessus, vous pouvez en générer une nouvelle depuis la Google Cloud Console.

Pour générer une nouvelle clé :
1. Allez sur la [Google Cloud Console](https://console.cloud.google.com/).
2. Accédez à IAM & Admin > Comptes de service.
3. Créez un nouveau compte de service :
   - Cliquez sur Créer un compte de service et attribuez les rôles appropriés.
   - Cliquez sur Créer.
4. Générez une clé :
   - Après avoir créé le compte de service, cliquez dessus.
   - Allez dans l'onglet Clés, cliquez sur Ajouter une clé, et choisissez JSON. Ensuite, téléchargez la clé.

---

### Exemple de sortie audio

Une fois que tout est configuré, vous pouvez générer un fichier audio, qui sera disponible ici :  
[Télécharger le fichier audio](assets/audios/output-audio.mp3).

---

### Conclusion

L'API Google Cloud Text-to-Speech permet de convertir facilement du texte en une voix naturelle. Que vous développiez une application nécessitant une sortie vocale ou que vous expérimentiez simplement la synthèse vocale, cette API propose des fonctionnalités puissantes et des options de personnalisation. Consultez la documentation complète pour découvrir des sélections de voix supplémentaires, des langues et des fonctionnalités avancées.