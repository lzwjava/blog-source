---
audio: false
generated: true
lang: hant
layout: post
title: 在 GCP 上使用 NVIDIA GPU 訓練 ML 模型
translated: true
type: note
---

Google Cloud Platform (GCP) 透過 Vertex AI（用於託管訓練任務）和 Compute Engine（用於自訂虛擬機器）等服務，提供使用 NVIDIA GPU 訓練機器學習模型的強大選項。然而，GCP 並未提供 NVIDIA RTX 4090 GPU。RTX 4090 是主要用於桌面電腦和遊戲的消費級 GPU，並非為雲端資料中心設計。相反地，GCP 提供企業級 NVIDIA GPU，例如 A100、H100、L4 等，這些 GPU 針對 AI 工作負載進行了優化，並且由於更高的記憶體頻寬和張量核心效率，在訓練場景中通常表現優於 RTX 4090。

對於多 GPU 設置（至少 2 個 GPU），您可以根據機器類型配置資源以使用 2、4、8 或更多 GPU。為了簡化，我將重點介紹 Vertex AI，因為它專為 ML 訓練設計並能自動處理擴展。如果您需要更多控制，我將簡要介紹 Compute Engine。

## 先決條件
- 設定 Google Cloud 帳戶並建立專案。
- 在您的專案中啟用 Vertex AI API 和 Compute Engine API。
- 安裝 Google Cloud SDK（gcloud CLI）和 Vertex AI SDK（如果使用 Python）。
- 將您的訓練程式碼準備在 Docker 容器中（例如，使用支援分散式訓練的 TensorFlow 或 PyTorch，如 Horovod 或 torch.distributed）。
- 確保您的模型程式碼支援多 GPU 訓練（例如，透過 PyTorch 的 DataParallel 或 DistributedDataParallel）。

## 使用 Vertex AI 進行多 GPU 訓練
Vertex AI 是 GCP 用於 ML 工作流程的託管平台。它支援自訂訓練任務，您可以在其中指定具有多個 GPU 的機器類型。

### 支援至少 2 個 GPU 的常見 NVIDIA GPU 類型
- NVIDIA H100（80GB 或 Mega 80GB）：適用於大型模型的高效能 GPU；支援 2、4 或 8 個 GPU。
- NVIDIA A100（40GB 或 80GB）：廣泛用於訓練；支援 2、4、8 或 16 個 GPU。
- NVIDIA L4：適用於推理和較輕量訓練的成本效益選擇；支援 2、4 或 8 個 GPU。
- NVIDIA T4 或 V100：較舊但仍可用；支援 2、4 或 8 個 GPU。

完整列表包括 GB200、B200、H200、P4、P100 — 請檢查區域可用性，因為並非所有區域都提供全部型號。

### 建立至少使用 2 個 GPU 的訓練任務的步驟
1. **準備您的容器**：建立包含您訓練腳本的 Docker 映像，並將其推送到 Google Container Registry 或 Artifact Registry。PyTorch 的範例 Dockerfile：
   ```
   FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
   COPY train.py /app/train.py
   WORKDIR /app
   CMD ["python", "train.py"]
   ```

2. **使用 gcloud CLI 配置任務**：
   - 建立 `config.yaml` 檔案：
     ```yaml
     workerPoolSpecs:
       machineSpec:
         machineType: a3-highgpu-2g  # 範例：2x H100 GPU；替代方案：a2-ultragpu-2g (2x A100)、g2-standard-24 (2x L4)
         acceleratorType: NVIDIA_H100_80GB  # 或 NVIDIA_A100_80GB、NVIDIA_L4
         acceleratorCount: 2  # 至少 2 個
       replicaCount: 1
       containerSpec:
         imageUri: gcr.io/your-project/your-image:latest  # 您的 Docker 映像 URI
     ```
   - 執行指令：
     ```bash
     gcloud ai custom-jobs create \
       --region=us-central1 \  # 選擇有 GPU 可用性的區域
       --display-name=your-training-job \
       --config=config.yaml
     ```

3. **使用 Python SDK**：
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

4. **監控和擴展**：
   - 使用 Vertex AI 控制台查看任務狀態和日誌。
   - 對於跨多台機器的分散式訓練（例如，更多副本），請添加額外的工作節點池，並在需要時為大規模任務使用歸約伺服器。
   - 成本：GPU 按小時計費；請檢查您區域的定價（例如，2x H100 可能約為每小時 6-10 美元）。

5. **多 GPU 訓練提示**：
   - 在您的程式碼中啟用分散式訓練（例如，`torch.nn.parallel.DistributedDataParallel`）。
   - 如果允許中斷，請使用 Spot VM 或預留實例以節省成本。
   - 透過 GCP 控制台驗證您區域/地區的 GPU 可用性。

## 替代方案：使用 Compute Engine VM
如果您偏好不使用 Vertex AI 的自訂設定：
1. 建立 VM 實例：
   - 前往 Compute Engine > VM 實例 > 建立實例。
   - 機器類型：從 A3 (H100)、A2 (A100)、G2 (L4) 系列中選擇，例如，`a3-highgpu-2g` 用於 2x H100。
   - 啟動磁碟：使用 Deep Learning VM 映像（預先安裝了 CUDA、TensorFlow/PyTorch）。
   - 添加 GPU：指定所選類型的 2 個加速器。

2. SSH 到 VM 並執行您的訓練腳本：
   ```bash
   gcloud compute ssh your-vm-name --zone=your-zone
   python train.py  # 確保偵測到 CUDA：nvidia-smi
   ```

3. 對於多 GPU：您的程式碼必須處理它（例如，`CUDA_VISIBLE_DEVICES=0,1`）。

這種方式更手動，但提供完全控制。

## 限制與替代方案
- 如果您特別需要類似 RTX 4090 的效能，請考慮替代方案，例如 AWS（在某些情況下提供消費級 GPU）或本地設置。
- 對於免費/有限的 GPU 訓練，請嘗試 Google Colab（最多 1-2 個 GPU，但不保證多 GPU 或 4090 同等效能）。
- 始終檢查配額並透過 GCP 控制台請求增加（如果需要）。

[配置自訂訓練的計算資源 | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[GPU 機器類型 | Compute Engine 文件 | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[雲端 GPU（圖形處理單元）- Google Cloud](https://cloud.google.com/gpu)