---
audio: false
generated: true
lang: fr
layout: post
title: Formation de modèles de ML sur GCP avec des GPU NVIDIA
translated: true
type: note
---

Google Cloud Platform (GCP) propose des options robustes pour entraîner des modèles de machine learning en utilisant des GPU NVIDIA via des services comme Vertex AI (pour les jobs d'entraînement managés) et Compute Engine (pour les machines virtuelles personnalisées). Cependant, les GPU NVIDIA RTX 4090 ne sont pas disponibles sur GCP. Le RTX 4090 est un GPU de consommation principalement destiné aux ordinateurs de bureau et au gaming, et n'est pas conçu pour les data centers cloud. À la place, GCP propose des GPU NVIDIA de grade entreprise tels que A100, H100, L4, et d'autres, qui sont optimisés pour les charges de travail d'IA et surpassent souvent le RTX 4090 dans les scénarios d'entraînement en raison d'une bande passante mémoire plus élevée et d'une meilleure efficacité des cœurs tensoriels.

Pour les configurations multi-GPU (au moins 2 GPU), vous pouvez configurer les ressources pour utiliser 2, 4, 8 GPU ou plus selon le type de machine. Je vais me concentrer sur Vertex AI pour plus de simplicité, car il est conçu pour l'entraînement de ML et gère la mise à l'échelle automatiquement. Si vous avez besoin de plus de contrôle, je couvrirai brièvement Compute Engine.

## Prérequis
- Configurer un compte Google Cloud et créer un projet.
- Activer l'API Vertex AI et l'API Compute Engine dans votre projet.
- Installer le Google Cloud SDK (CLI gcloud) et le SDK Vertex AI si vous utilisez Python.
- Préparer votre code d'entraînement dans un conteneur Docker (par exemple, en utilisant TensorFlow ou PyTorch avec un support pour l'entraînement distribué comme Horovod ou torch.distributed).
- S'assurer que votre code de modèle prend en charge l'entraînement multi-GPU (par exemple, via DataParallel ou DistributedDataParallel dans PyTorch).

## Utilisation de Vertex AI pour l'Entraînement Multi-GPU
Vertex AI est la plateforme managée de GCP pour les workflows de ML. Il prend en charge les jobs d'entraînement personnalisés où vous pouvez spécifier des types de machines avec plusieurs GPU.

### Types de GPU Disponibles pour le Multi-GPU
GPU NVIDIA courants supportant au moins 2 attachments :
- NVIDIA H100 (80GB ou Mega 80GB) : Haute performance pour les grands modèles ; supporte 2, 4 ou 8 GPU.
- NVIDIA A100 (40GB ou 80GB) : Très utilisé pour l'entraînement ; supporte 2, 4, 8 ou 16 GPU.
- NVIDIA L4 : Rentable pour l'inférence et l'entraînement léger ; supporte 2, 4 ou 8 GPU.
- NVIDIA T4 ou V100 : Plus anciens mais toujours disponibles ; supportent 2, 4 ou 8 GPU.

La liste complète inclut GB200, B200, H200, P4, P100 — vérifiez la disponibilité selon les régions, car tous ne sont pas disponibles dans chaque zone.

### Étapes pour Créer un Job d'Entraînement avec au Moins 2 GPU
1.  **Préparer Votre Conteneur** : Construisez une image Docker avec votre script d'entraînement et poussez-la vers Google Container Registry ou Artifact Registry. Exemple de Dockerfile pour PyTorch :
    ```
    FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
    COPY train.py /app/train.py
    WORKDIR /app
    CMD ["python", "train.py"]
    ```

2.  **Configurer le Job en utilisant la CLI gcloud** :
    - Créez un fichier `config.yaml` :
      ```yaml
      workerPoolSpecs:
        machineSpec:
          machineType: a3-highgpu-2g  # Exemple : 2x GPU H100 ; alternatives : a2-ultragpu-2g (2x A100), g2-standard-24 (2x L4)
          acceleratorType: NVIDIA_H100_80GB  # Ou NVIDIA_A100_80GB, NVIDIA_L4
          acceleratorCount: 2  # Au moins 2
        replicaCount: 1
        containerSpec:
          imageUri: gcr.io/your-project/your-image:latest  # L'URI de votre image Docker
      ```
    - Exécutez la commande :
      ```bash
      gcloud ai custom-jobs create \
        --region=us-central1 \  # Choisissez une région avec disponibilité des GPU
        --display-name=your-training-job \
        --config=config.yaml
      ```

3.  **Utilisation du SDK Python** :
    ```python
    from google.cloud import aiplatform

    aiplatform.init(project='your-project-id', location='us-central1')

    job = aiplatform.CustomJob(
        display_name='your-training-job',
        worker_pool_specs=[
            {
                'machine_spec': {
                    'machine_type': 'a3-highgpu-2g',  # 2x H100
                    'accelerator_type': 'NVIDIA_H100_80GB',
                    'accelerator_count': 2,
                },
                'replica_count': 1,
                'container_spec': {
                    'image_uri': 'gcr.io/your-project/your-image:latest',
                },
            }
        ],
    )
    job.run()
    ```

4.  **Surveillance et Mise à l'Échelle** :
    - Utilisez la console Vertex AI pour voir le statut du job et les logs.
    - Pour l'entraînement distribué sur plusieurs machines (par exemple, plus de réplicas), ajoutez des worker pools supplémentaires et utilisez des serveurs de réduction si nécessaire pour les jobs à grande échelle.
    - Coûts : Les GPU sont facturés à l'heure ; vérifiez les tarifs dans votre région (par exemple, 2x H100 pourrait coûter ~6-10$/heure).

5.  **Conseils pour l'Entraînement Multi-GPU** :
    - Activez l'entraînement distribué dans votre code (par exemple, `torch.nn.parallel.DistributedDataParallel`).
    - Utilisez des VM spot ou des réservations pour réduire les coûts si les interruptions sont acceptables.
    - Vérifiez la disponibilité des GPU dans votre région/zone via la console GCP.

## Alternative : Utilisation de VM Compute Engine
Si vous préférez une configuration personnalisée sans Vertex AI :
1. Créez une instance de VM :
   - Allez dans Compute Engine > Instances de VM > Créer une instance.
   - Type de machine : Sélectionnez dans les séries A3 (H100), A2 (A100), G2 (L4), par exemple, `a3-highgpu-2g` pour 2x H100.
   - Disque de démarrage : Utilisez une image Deep Learning VM (avec CUDA, TensorFlow/PyTorch pré-installés).
   - Ajoutez des GPU : Spécifiez 2 accélérateurs du type choisi.

2. Connectez-vous en SSH à la VM et exécutez votre script d'entraînement :
   ```bash
   gcloud compute ssh your-vm-name --zone=your-zone
   python train.py  # Vérifiez que CUDA est détecté : nvidia-smi
   ```

3. Pour le multi-GPU : Votre code doit le gérer (par exemple, `CUDA_VISIBLE_DEVICES=0,1`).

Cette méthode est plus manuelle mais donne un contrôle total.

## Limitations et Alternatives
- Si vous avez spécifiquement besoin de performances équivalentes au RTX 4090, envisagez des alternatives comme AWS (qui propose des GPU de consommation dans certains cas) ou des configurations sur site.
- Pour un entraînement gratuit/limité sur GPU, essayez Google Colab (jusqu'à 1-2 GPU, mais sans garantie de multi-GPU ou d'équivalent au 4090).
- Vérifiez toujours les quotas et demandez une augmentation si nécessaire via la console GCP.

[Configurer les ressources de calcul pour l'entraînement personnalisé | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[Types de machines avec GPU | Documentation Compute Engine | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[GPU Cloud (Graphics Processing Units) - Google Cloud](https://cloud.google.com/gpu)