---
audio: false
generated: true
lang: de
layout: post
title: Training von ML-Modellen auf GCP mit NVIDIA-GPUs
translated: true
type: note
---

Google Cloud Platform (GCP) bietet robuste Optionen für das Training von Machine-Learning-Modellen mit NVIDIA GPUs über Dienste wie Vertex AI (für verwaltete Trainingsjobs) und Compute Engine (für benutzerdefinierte virtuelle Maschinen). Allerdings sind NVIDIA RTX 4090 GPUs auf GCP nicht verfügbar. Die RTX 4090 ist eine Consumer-Grade-GPU, die primär für Desktops und Gaming konzipiert ist und nicht für Cloud-Rechenzentren. Stattdessen bietet GCP Enterprise-Grade-NVIDIA-GPUs wie A100, H100, L4 und andere an, die für KI-Workloads optimiert sind und in Trainingsszenarien aufgrund höherer Speicherbandbreite und Tensor-Core-Effizienz oft die RTX 4090 übertreffen.

Für Multi-GPU-Setups (mindestens 2 GPUs) können Sie Ressourcen konfigurieren, um 2, 4, 8 oder mehr GPUs zu verwenden, abhängig vom Maschinentyp. Ich konzentriere mich der Einfachheit halber auf Vertex AI, da es für ML-Training maßgeschneidert ist und die Skalierung automatisch handhabt. Falls Sie mehr Kontrolle benötigen, gehe ich kurz auf Compute Engine ein.

## Voraussetzungen
- Richten Sie einen Google Cloud Account ein und erstellen Sie ein Projekt.
- Aktivieren Sie die Vertex AI API und die Compute Engine API in Ihrem Projekt.
- Installieren Sie das Google Cloud SDK (gcloud CLI) und das Vertex AI SDK, falls Sie Python verwenden.
- Bereiten Sie Ihren Trainingscode in einem Docker-Container vor (z. B. mit TensorFlow oder PyTorch mit Unterstützung für verteiltes Training wie Horovod oder torch.distributed).
- Stellen Sie sicher, dass Ihr Modellcode Multi-GPU-Training unterstützt (z. B. via DataParallel oder DistributedDataParallel in PyTorch).

## Verwendung von Vertex AI für Multi-GPU-Training
Vertex AI ist die verwaltete Plattform von GCP für ML-Workflows. Sie unterstützt benutzerdefinierte Trainingsjobs, bei denen Sie Maschinentypen mit mehreren GPUs angeben können.

### Verfügbare GPU-Typen für Multi-GPU
Häufige NVIDIA GPUs, die die Anbindung von mindestens 2 GPUs unterstützen:
- NVIDIA H100 (80GB oder Mega 80GB): Hochleistungsfähig für große Modelle; unterstützt 2, 4 oder 8 GPUs.
- NVIDIA A100 (40GB oder 80GB): Weit verbreitet für Training; unterstützt 2, 4, 8 oder 16 GPUs.
- NVIDIA L4: Kosteneffektiv für Inference und leichteres Training; unterstützt 2, 4 oder 8 GPUs.
- NVIDIA T4 oder V100: Älter, aber noch verfügbar; unterstützt 2, 4 oder 8 GPUs.

Die vollständige Liste umfasst GB200, B200, H200, P4, P100 – prüfen Sie die Verfügbarkeit in den Regionen, da nicht alle in jeder Zone verfügbar sind.

### Schritte zur Erstellung eines Trainingsjobs mit mindestens 2 GPUs
1. **Bereiten Sie Ihren Container vor**: Bauen Sie ein Docker-Image mit Ihrem Trainingsskript und pushen Sie es in die Google Container Registry oder Artifact Registry. Beispiel-Dockerfile für PyTorch:
   ```
   FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
   COPY train.py /app/train.py
   WORKDIR /app
   CMD ["python", "train.py"]
   ```

2. **Konfigurieren Sie den Job mit der gcloud CLI**:
   - Erstellen Sie eine `config.yaml`-Datei:
     ```yaml
     workerPoolSpecs:
       machineSpec:
         machineType: a3-highgpu-2g  # Beispiel: 2x H100 GPUs; Alternativen: a2-ultragpu-2g (2x A100), g2-standard-24 (2x L4)
         acceleratorType: NVIDIA_H100_80GB  # Oder NVIDIA_A100_80GB, NVIDIA_L4
         acceleratorCount: 2  # Mindestens 2
       replicaCount: 1
       containerSpec:
         imageUri: gcr.io/your-project/your-image:latest  # Ihre Docker-Image-URI
     ```
   - Führen Sie den Befehl aus:
     ```bash
     gcloud ai custom-jobs create \
       --region=us-central1 \  # Wählen Sie eine Region mit GPU-Verfügbarkeit
       --display-name=your-training-job \
       --config=config.yaml
     ```

3. **Verwendung des Python SDK**:
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

4. **Überwachung und Skalierung**:
   - Verwenden Sie die Vertex AI-Konsole, um den Job-Status und die Protokolle einzusehen.
   - Für verteiltes Training über mehrere Maschinen (z. B. mehr Replikate) fügen Sie zusätzliche Worker-Pools hinzu und verwenden Sie ggf. Reduction-Server für groß angelegte Jobs.
   - Kosten: GPUs werden pro Stunde abgerechnet; prüfen Sie die Preise in Ihrer Region (z. B. könnten 2x H100 ~$6-10/Stunde kosten).

5. **Tipps für Multi-GPU-Training**:
   - Aktivieren Sie verteiltes Training in Ihrem Code (z. B. `torch.nn.parallel.DistributedDataParallel`).
   - Verwenden Sie Spot-VMs oder Reservierungen für Kosteneinsparungen, falls Unterbrechungen in Ordnung sind.
   - Überprüfen Sie die GPU-Verfügbarkeit in Ihrer Region/Zone über die GCP-Konsole.

## Alternative: Verwendung von Compute Engine VMs
Falls Sie ein benutzerdefiniertes Setup ohne Vertex AI bevorzugen:
1. Erstellen Sie eine VM-Instanz:
   - Gehen Sie zu Compute Engine > VM-Instanzen > Instanz erstellen.
   - Maschinentyp: Wählen Sie aus der A3 (H100), A2 (A100), G2 (L4) Serie, z. B. `a3-highgpu-2g` für 2x H100.
   - Startfestplatte: Verwenden Sie ein Deep Learning VM Image (vorinstalliert mit CUDA, TensorFlow/PyTorch).
   - GPUs hinzufügen: Geben Sie 2 Acceleratoren des gewählten Typs an.

2. SSH in die VM und führen Sie Ihr Trainingsskript aus:
   ```bash
   gcloud compute ssh your-vm-name --zone=your-zone
   python train.py  # Stellen Sie sicher, dass CUDA erkannt wird: nvidia-smi
   ```

3. Für Multi-GPU: Ihr Code muss dies handhaben (z. B. `CUDA_VISIBLE_DEVICES=0,1`).

Dies ist aufwändiger, bietet aber volle Kontrolle.

## Einschränkungen und Alternativen
- Falls Sie spezifisch RTX-4090-ähnliche Leistung benötigen, ziehen Sie Alternativen wie AWS (das in einigen Fällen Consumer-GPUs anbietet) oder On-Premises-Setups in Betracht.
- Für kostenloses/begrenztes GPU-Training versuchen Sie Google Colab (bis zu 1-2 GPUs, aber Multi-GPU oder 4090-äquivalent nicht garantiert).
- Prüfen Sie immer die Kontingente und beantragen Sie bei Bedarf Erhöhungen über die GCP-Konsole.

[Configure compute resources for custom training | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[GPU machine types | Compute Engine Documentation | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[Cloud GPUs (Graphics Processing Units) - Google Cloud](https://cloud.google.com/gpu)