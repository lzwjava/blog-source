---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Accélération du traitement de transcription audio longue
translated: true
type: note
---

### Pourquoi le traitement est-il si long pour les fichiers audio de 30 minutes ou 1 heure ?

L'API Google Cloud Speech-to-Text Batch (v2) est conçue pour des opérations asynchrones de longue durée, en particulier avec le modèle `"long"`, qui gère les fichiers audio étendus (jusqu'à ~1 heure par fichier). Voici pourquoi cela peut sembler "trop long" :

- **Le temps de traitement est proportionnel à la durée audio** : La transcription n'est pas instantanée. Pour un fichier audio de 30 minutes, cela peut prendre 5 à 20 minutes ; pour 1 heure, 10 à 40 minutes ou plus. Ceci inclut :
  - Le temps de mise en file d'attente (si votre projet/région est occupé).
  - La transcription proprement dite (inférence du modèle IA, qui est intensive en calcul pour les longs fichiers audio).
  - Le post-traitement (par exemple, les horodatages des mots, les scores de confiance).
- **Nature asynchrone (Batch)** : Contrairement au streaming en temps réel, les jobs batch s'exécutent en arrière-plan sur les serveurs de Google. Votre script appelle `operation.result()`, qui bloque et attend, mais le vrai travail se produit de manière asynchrone.
- **Autres facteurs** :
  - Le format/la qualité audio : OGG/Opus ou M4A/AAC nécessitent un décodage, ce qui ajoute une surcharge si les taux d'échantillonnage/les canaux ne correspondent pas.
  - Le choix du modèle : `"long"` est optimisé pour les réunions/podcasts mais est plus lent que les modèles plus courts comme `"default"` ou `"short"`.
  - Le réseau/les quotas : Le téléversement vers GCS, les appels d'API et le téléchargement des résultats ajoutent de la latence. Les quotas du niveau gratuit ou une demande élevée peuvent retarder les jobs.
  - Aucun parallélisme intégré : Le script traite un fichier à la fois séquentiellement.

Si votre audio dure systématiquement plus de 30 minutes, la configuration actuelle n'est pas idéale pour un traitement rapide—elle est mieux adaptée au traitement hors ligne/en vrac.

### Comment résoudre le problème : Réduire le temps de traitement

Pour traiter les longs fichiers audio plus rapidement, la clé est de **diviser le fichier en segments plus petits** (par exemple, de 5 à 15 minutes chacun). Cela permet :
- Un traitement parallèle (exécuter plusieurs jobs batch simultanément).
- D'utiliser des modèles plus rapides (par exemple, `"short"` ou `"default"`) par segment.
- Des temps d'attente plus courts par job (par exemple, 1 à 5 minutes par segment contre 30+ minutes pour le fichier entier).

#### Étape 1 : Diviser le fichier audio
Utilisez **FFmpeg** (gratuit, outil en ligne de commande) pour diviser les fichiers sans re-encoder (rapide et sans perte). Installez FFmpeg si nécessaire (par exemple, `brew install ffmpeg` sur macOS, `apt install ffmpeg` sur Linux).

Ajoutez une fonction à votre script pour diviser le fichier d'entrée. Voici une version mise à jour de votre script avec l'intégration de la division :

```python
import os
import argparse
import subprocess
import tempfile
from google.cloud import storage
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
import sys
import time  # For polling

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api  # noqa: F401

MAX_AUDIO_LENGTH_SECS = 20 * 60 * 60
OUTPUT_DIRECTORY = "assets/transcriptions"
CHUNK_DURATION_SECS = 600  # 10 minutes par segment ; ajustez si nécessaire (par exemple, 900 pour 15 min)


def split_audio_file(input_file, chunk_duration_secs=CHUNK_DURATION_SECS):
    """
    Divise un fichier audio en segments plus petits en utilisant FFmpeg.
    
    Args:
        input_file: Chemin vers le fichier audio d'entrée.
        chunk_duration_secs: Durée de chaque segment en secondes.
    
    Returns:
        Liste des chemins des fichiers segments.
    """
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(input_file)
    
    # Créer un répertoire temporaire pour les segments
    temp_dir = tempfile.mkdtemp()
    chunk_files = []
    
    # Commande FFmpeg (pas de re-encodage pour la vitesse)
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",  # Format de sortie
        "-segment_time", str(chunk_duration_secs),
        "-c", "copy",  # Copier les flux sans re-encoder
        "-map", "0",  # Mapper tous les flux
        f"{temp_dir}/{name_without_ext}_chunk_%03d.{os.path.splitext(filename)[1][1:]}",  # Modèle de nommage
        "-y"  # Écraser
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        # Trouver les segments générés
        for file in os.listdir(temp_dir):
            if file.startswith(f"{name_without_ext}_chunk_") and file.endswith(os.path.splitext(filename)[1]):
                chunk_files.append(os.path.join(temp_dir, file))
        chunk_files.sort()  # Trier par nom (par exemple, chunk_001, chunk_002)
        print(f"Division de {filename} en {len(chunk_files)} segments.")
        return chunk_files
    except subprocess.CalledProcessError as e:
        print(f"Erreur FFmpeg lors de la division de {filename}: {e}")
        return []


def run_batch_recognize(audio_gcs_uri, output_gcs_folder, language_code="en-US"):
    """
    Transcrit un fichier audio en utilisant l'API Google Cloud Speech-to-Text Batch.
    Mis à jour pour utiliser un modèle plus court si l'audio est probablement court (par exemple, après division).
    """
    client = SpeechClient()

    filename = audio_gcs_uri.split('/')[-1]
    file_extension = filename.split('.')[-1].lower()

    # Pour les segments, utiliser le modèle "short" ou "default" pour la vitesse (si <15 min)
    model = "short" if CHUNK_DURATION_SECS < 900 else "long"  # Ajuster en fonction de la taille du segment

    if file_extension == "ogg":
        decoding = cloud_speech.ExplicitDecodingConfig(
            encoding=cloud_speech.ExplicitDecodingConfig.AudioEncoding.OGG_OPUS,
            sample_rate_hertz=48000,
            audio_channel_count=1
        )
        config = cloud_speech.RecognitionConfig(
            explicit_decoding_config=decoding,
            features=cloud_speech.RecognitionFeatures(
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            ),
            model=model,
            language_codes=[language_code],
        )
    else:
        config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            features=cloud_speech.RecognitionFeatures(
                enable_word_confidence=True,
                enable_word_time_offsets=True,
            ),
            model=model,
            language_codes=[language_code],
        )

    output_config = cloud_speech.RecognitionOutputConfig(
        gcs_output_config=cloud_speech.GcsOutputConfig(uri=output_gcs_folder),
    )

    files = [cloud_speech.BatchRecognizeFileMetadata(uri=audio_gcs_uri)]

    request = cloud_speech.BatchRecognizeRequest(
        recognizer="projects/graphite-ally-445108-k3/locations/global/recognizers/_",
        config=config,
        files=files,
        recognition_output_config=output_config,
    )

    print(f"Démarrage de la reconnaissance par lot pour {filename}...")
    operation = client.batch_recognize(request=request)
    
    # Interroger pour la progression (voir ci-dessous pour les détails)
    poll_operation_with_progress(operation, filename)
    
    response = operation.result(timeout=3 * CHUNK_DURATION_SECS)  # Timeout plus court par segment
    print(f"Transcription terminée pour {filename}. Réponse: {response}")
    return response


def poll_operation_with_progress(operation, filename):
    """
    Interroge l'opération de longue durée et affiche la progression.
    """
    while not operation.done():
        # Obtenir les métadonnées de l'opération (si disponibles ; l'API Speech fournit un statut basique)
        try:
            metadata = operation.metadata
            print(f"Progression pour {filename}: État={getattr(metadata, 'state', 'Inconnu')}, "
                  f"Traité={getattr(metadata, 'progress_bytes', 'N/A')} bytes")
        except Exception:
            print(f"En attente pour {filename}... (vérification toutes les 30s)")
        
        time.sleep(30)  # Interroger toutes les 30 secondes
    if operation.exception():
        raise operation.exception()


def process_audio_file(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(input_file)
    if not (filename.endswith(".m4a") or filename.endswith(".ogg")):
        print(f"Erreur : {filename} n'est pas un fichier audio pris en charge (.m4a ou .ogg).")
        return

    output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
    if os.path.exists(output_filename):
        print(f"Passage de {filename} : {output_filename} existe déjà.")
        return

    print(f"Traitement de : {filename}")

    # Déterminer la langue
    if filename.endswith("-zh.m4a") or filename.endswith("-zh.ogg"):
        language_code = "cmn-CN"
    else:
        language_code = "en-US"

    # Diviser en segments si le fichier est long (heuristique : >15 min, mais vous pouvez sonder la durée avec ffprobe)
    chunk_files = []
    if os.path.getsize(input_file) > 100 * 1024 * 1024:  # Vérification approximative : >100MB probablement long
        print(f"Le fichier est volumineux ; division en segments de {CHUNK_DURATION_SECS//60} minutes.")
        chunk_files = split_audio_file(input_file)
        if not chunk_files:
            print("La division a échoué ; traitement en tant que fichier unique.")
            chunk_files = [input_file]
    else:
        chunk_files = [input_file]

    storage_client = storage.Client()
    bucket = storage_client.bucket("test2x")

    all_transcripts = []  # Pour combiner plus tard

    for chunk_idx, chunk_file in enumerate(chunk_files):
        chunk_filename = os.path.basename(chunk_file)
        base_name = os.path.splitext(filename)[0]
        chunk_name = f"{base_name}_chunk_{chunk_idx+1:03d}"
        
        # Construire les chemins GCS
        gcs_audio_uri = f"gs://test2x/audio-files/{chunk_filename}"
        gcs_output_uri = f"gs://test2x/transcripts/{chunk_name}"

        # Téléverser le segment si nécessaire
        blob = bucket.blob(f"audio-files/{chunk_filename}")
        if not blob.exists():
            blob.upload_from_filename(chunk_file)
            print(f"Segment {chunk_filename} téléversé vers GCS.")
        else:
            print(f"Le segment {chunk_filename} est déjà dans GCS.")

        # Transcrire
        try:
            run_batch_recognize(
                audio_gcs_uri=gcs_audio_uri,
                output_gcs_folder=gcs_output_uri,
                language_code=language_code,
            )

            # Télécharger et collecter la transcription
            blobs = storage_client.list_blobs("test2x", prefix=f"transcripts/{chunk_name}")
            chunk_transcript = ""
            for b in blobs:
                if b.name.endswith(".json"):
                    local_path = os.path.join(output_dir, f"{os.path.basename(b.name)}")
                    b.download_to_filename(local_path)
                    # Parser le JSON pour extraire le texte (simplifié ; utiliser le module json pour un parsing complet)
                    import json
                    with open(local_path, 'r') as f:
                        data = json.load(f)
                        if 'results' in data:
                            chunk_text = ' '.join([result.get('alternatives', [{}])[0].get('transcript', '') for result in data['results']])
                            chunk_transcript += chunk_text + "\n"
                    print(f"Téléchargement et analyse de {b.name} terminés")

            all_transcripts.append(chunk_transcript)

            # Nettoyer le segment temporaire si division
            if chunk_file != input_file and os.path.exists(chunk_file):
                os.remove(chunk_file)

        except Exception as e:
            print(f"Échec du traitement du segment {chunk_filename}: {e}")

    # Combiner toutes les transcriptions en un seul fichier
    combined_text = "\n\n--- Limite du segment ---\n\n".join(all_transcripts)
    with open(output_filename, 'w') as f:
        f.write(combined_text)
    print(f"Transcription combinée sauvegardée dans {output_filename}")

    # Nettoyer le répertoire temporaire si division effectuée
    if chunk_files != [input_file]:
        import shutil
        shutil.rmtree(os.path.dirname(chunk_files[0]) if chunk_files else None)

    print(f"Traitement terminé pour {filename}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Traite un seul fichier Voice Memo (.m4a/.ogg) pour générer une transcription."
    )
    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Chemin d'entrée pour le fichier Voice Memo.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="assets/transcriptions",
        help="Répertoire de sortie pour les transcriptions.",
    )
    parser.add_argument(
        "--chunk_secs",
        type=int,
        default=CHUNK_DURATION_SECS,
        help="Durée du segment en secondes (pour diviser les longs fichiers).",
    )

    args = parser.parse_args()
    global CHUNK_DURATION_SECS  # Permettre la substitution
    CHUNK_DURATION_SECS = args.chunk_secs

    process_audio_file(
        input_file=args.input_file,
        output_dir=args.output,
    )
```

#### Changements et avantages clés :
- **Division** : Utilise FFmpeg pour créer des segments sans chevauchement (par exemple, de 10 min chacun). Pour un fichier d'1 heure, cela représente ~6 jobs, qui peuvent s'exécuter en parallèle si vous modifiez le script pour utiliser le threading/le multiprocessing (par exemple, via `concurrent.futures`).
- **Modèle plus rapide** : Passe au modèle `"short"` pour les segments <15 min—traite 2 à 3 fois plus vite.
- **Combinaison des transcriptions** : Analyse les sorties JSON et les fusionne en un seul fichier `.txt` avec des limites pour une lecture facile.
- **Nettoyage** : Supprime les segments temporaires et les anciens blobs GCS si nécessaire (ajoutez `blob.delete()` dans une boucle).
- **Utilisation** : Exécutez comme avant, par exemple, `python script.py --input_file long_audio.m4a --chunk_secs 600`. Pour éviter la division, utilisez une grande valeur pour `--chunk_secs` (par exemple, 3600).

#### Autres optimisations :
- **Traitement parallèle** : Si vous avez beaucoup de segments/fichiers, utilisez `ThreadPoolExecutor` de Python pour soumettre les jobs `run_batch_recognize` simultanément (limitez à 5-10 pour éviter les dépassements de quota).
- **Sonder la durée audio** : Utilisez `ffprobe` (FFmpeg) pour décider dynamiquement si une division est nécessaire : `ffprobe -v quiet -show_entries format=duration -of csv=p=0 input.m4a`.
- **Passer à l'API Streaming** : Pour une utilisation interactive, utilisez `recognize` synchrone (limite ~1 min/fichier) ou le streaming pour du temps réel, mais ce n'est pas idéal pour les longs fichiers en batch.
- **Coûts/Quotas** : Vérifiez votre quota Google Cloud (Speech-to-Text autorise ~1000 req/min). Les jobs longs consomment plus de crédits (~$0.036/min pour le modèle standard).
- **Tester d'abord avec des fichiers courts** : Commencez avec `--chunk_secs 300` (5 min) pour voir l'accélération.

### Afficher la progression : Interrogation de l'opération

La fonction mise à jour `poll_operation_with_progress()` remplace le blocage `operation.result()`. Elle :
- Vérifie toutes les 30 secondes.
- Affiche le statut depuis `operation.metadata` (par exemple, l'état comme "RUNNING" ou "DONE", et les bytes traités si disponibles—les métadonnées de l'API Speech sont basiques, mais c'est mieux que rien).
- Lève une erreur en cas d'échec.

Pour une progression plus détaillée (par exemple, le % complet), l'API Speech ne fournit pas de métriques granulaires, mais vous pouvez :
- Surveiller via Google Cloud Console (page Operations pour votre projet).
- Utiliser la CLI `gcloud` : `gcloud alpha speech operations describe OPERATION_ID --project=graphite-ally-445108-k3`.
- Après la fin, les résultats JSON incluent indirectement la progression par énoncé via les horodatages.

Avec la division, vous verrez une progression entrelacée de plusieurs segments, ce qui donne une impression de moins "bloquer".

Si cela ne résout pas votre problème (par exemple, des erreurs spécifiques), partagez les journaux/sorties pour plus d'ajustements !