---
audio: false
generated: true
lang: es
layout: post
title: Entrenamiento de Modelos de ML en GCP con GPU de NVIDIA
translated: true
type: note
---

Google Cloud Platform (GCP) ofrece opciones robustas para entrenar modelos de machine learning utilizando GPUs de NVIDIA a través de servicios como Vertex AI (para trabajos de entrenamiento gestionados) y Compute Engine (para máquinas virtuales personalizadas). Sin embargo, las GPUs NVIDIA RTX 4090 no están disponibles en GCP. La RTX 4090 es una GPU de consumo principalmente para equipos de escritorio y gaming, no diseñada para centros de datos en la nube. En su lugar, GCP ofrece GPUs NVIDIA de grado empresarial como A100, H100, L4 y otras, que están optimizadas para cargas de trabajo de IA y a menudo superan a la RTX 4090 en escenarios de entrenamiento debido a su mayor ancho de banda de memoria y eficiencia de los Tensor Cores.

Para configuraciones multi-GPU (al menos 2 GPUs), puedes configurar recursos para usar 2, 4, 8 o más GPUs dependiendo del tipo de máquina. Me centraré en Vertex AI por simplicidad, ya que está diseñado para entrenamiento de ML y maneja el escalado automáticamente. Si necesitas más control, cubriré Compute Engine brevemente.

## Prerrequisitos
- Configurar una cuenta de Google Cloud y crear un proyecto.
- Habilitar la API de Vertex AI y la API de Compute Engine en tu proyecto.
- Instalar el SDK de Google Cloud (CLI de gcloud) y el SDK de Vertex AI si usas Python.
- Preparar tu código de entrenamiento en un contenedor Docker (por ejemplo, usando TensorFlow o PyTorch con soporte para entrenamiento distribuido como Horovod o torch.distributed).
- Asegurarse de que el código de tu modelo soporta entrenamiento multi-GPU (por ejemplo, mediante DataParallel o DistributedDataParallel en PyTorch).

## Usar Vertex AI para Entrenamiento Multi-GPU
Vertex AI es la plataforma gestionada de GCP para flujos de trabajo de ML. Soporta trabajos de entrenamiento personalizados donde puedes especificar tipos de máquina con múltiples GPUs.

### Tipos de GPU Disponibles para Multi-GPU
GPUs NVIDIA comunes que soportan al menos 2 adjuntos:
- NVIDIA H100 (80GB o Mega 80GB): Alto rendimiento para modelos grandes; soporta 2, 4 u 8 GPUs.
- NVIDIA A100 (40GB u 80GB): Muy utilizada para entrenamiento; soporta 2, 4, 8 o 16 GPUs.
- NVIDIA L4: Rentable para inferencia y entrenamiento más ligero; soporta 2, 4 u 8 GPUs.
- NVIDIA T4 o V100: Más antiguas pero aún disponibles; soportan 2, 4 u 8 GPUs.

La lista completa incluye GB200, B200, H200, P4, P100—verifica la disponibilidad en las regiones, ya que no todas están en cada zona.

### Pasos para Crear un Trabajo de Entrenamiento con al Menos 2 GPUs
1. **Preparar tu Contenedor**: Construye una imagen Docker con tu script de entrenamiento y súbela a Google Container Registry o Artifact Registry. Dockerfile de ejemplo para PyTorch:
   ```
   FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
   COPY train.py /app/train.py
   WORKDIR /app
   CMD ["python", "train.py"]
   ```

2. **Configurar el Trabajo Usando la CLI de gcloud**:
   - Crea un archivo `config.yaml`:
     ```yaml
     workerPoolSpecs:
       machineSpec:
         machineType: a3-highgpu-2g  # Ejemplo: 2x GPUs H100; alternativas: a2-ultragpu-2g (2x A100), g2-standard-24 (2x L4)
         acceleratorType: NVIDIA_H100_80GB  # O NVIDIA_A100_80GB, NVIDIA_L4
         acceleratorCount: 2  # Al menos 2
       replicaCount: 1
       containerSpec:
         imageUri: gcr.io/your-project/your-image:latest  # Tu URI de imagen Docker
     ```
   - Ejecuta el comando:
     ```bash
     gcloud ai custom-jobs create \
       --region=us-central1 \  # Elige una región con disponibilidad de GPU
       --display-name=your-training-job \
       --config=config.yaml
     ```

3. **Usar el SDK de Python**:
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

4. **Monitorear y Escalar**:
   - Usa la consola de Vertex AI para ver el estado del trabajo y los logs.
   - Para entrenamiento distribuido en múltiples máquinas (por ejemplo, más réplicas), añade grupos de trabajadores adicionales y usa servidores de reducción si es necesario para trabajos a gran escala.
   - Costos: Las GPUs se facturan por hora; consulta los precios en tu región (por ejemplo, 2x H100 podrían costar ~$6-10/hora).

5. **Consejos para Entrenamiento Multi-GPU**:
   - Habilita el entrenamiento distribuido en tu código (por ejemplo, `torch.nn.parallel.DistributedDataParallel`).
   - Usa Spot VMs o reservas para ahorrar costos si las interrupciones son aceptables.
   - Verifica la disponibilidad de GPU en tu región/zona a través de la consola de GCP.

## Alternativa: Usar Máquinas Virtuales de Compute Engine
Si prefieres una configuración personalizada sin Vertex AI:
1. Crea una instancia de VM:
   - Ve a Compute Engine > Instancias de VM > Crear instancia.
   - Tipo de máquina: Selecciona de las series A3 (H100), A2 (A100), G2 (L4), por ejemplo, `a3-highgpu-2g` para 2x H100.
   - Disco de arranque: Usa una imagen de Deep Learning VM (con CUDA, TensorFlow/PyTorch preinstalados).
   - Añade GPUs: Especifica 2 aceleradores del tipo elegido.

2. Conéctate por SSH a la VM y ejecuta tu script de entrenamiento:
   ```bash
   gcloud compute ssh your-vm-name --zone=your-zone
   python train.py  # Asegúrate de que CUDA se detecte: nvidia-smi
   ```

3. Para multi-GPU: Tu código debe manejarlo (por ejemplo, `CUDA_VISIBLE_DEVICES=0,1`).

Esto es más manual pero da control total.

## Limitaciones y Alternativas
- Si necesitas específicamente un rendimiento similar al de la RTX 4090, considera alternativas como AWS (que ofrece GPUs de consumo en algunos casos) o configuraciones on-premises.
- Para entrenamiento con GPU gratuito/limitado, prueba Google Colab (hasta 1-2 GPUs, pero no garantiza multi-GPU o equivalente a 4090).
- Siempre verifica las cuotas y solicita aumentos si es necesario a través de la consola de GCP.

[Configurar recursos de computación para entrenamiento personalizado | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[Tipos de máquina con GPU | Documentación de Compute Engine | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[GPUs en la nube (Unidades de Procesamiento de Gráficos) - Google Cloud](https://cloud.google.com/gpu)