---
audio: false
generated: true
lang: ja
layout: post
title: GCPとNVIDIA GPUを用いた機械学習モデルトレーニング
translated: true
type: note
---

Google Cloud Platform（GCP）は、Vertex AI（マネージドトレーニングジョブ用）やCompute Engine（カスタム仮想マシン用）などのサービスを通じて、NVIDIA GPUを使用した機械学習モデルのトレーニングに対する堅牢なオプションを提供します。ただし、NVIDIA RTX 4090 GPUはGCPでは利用できません。RTX 4090は、主にデスクトップやゲーミング向けのコンシューマー向けGPUであり、クラウドデータセンター向けには設計されていません。代わりに、GCPはエンタープライズ向けNVIDIA GPU（A100、H100、L4など）を提供しており、これらはAIワークロード向けに最適化されており、メモリ帯域幅とテンソルコアの効率が高いため、トレーニングシナリオでは多くの場合RTX 4090を上回るパフォーマンスを発揮します。

マルチGPUセットアップ（少なくとも2 GPU）の場合、マシンタイプに応じて2、4、8、またはそれ以上のGPUを使用するようにリソースを構成できます。ここでは、MLトレーニングに特化し、スケーリングを自動的に処理するVertex AIに焦点を当てて説明します。より制御が必要な場合は、Compute Engineについても簡単に説明します。

## 前提条件
- Google Cloudアカウントをセットアップし、プロジェクトを作成します。
- プロジェクトでVertex AI APIとCompute Engine APIを有効にします。
- Google Cloud SDK（gcloud CLI）と、Pythonを使用する場合はVertex AI SDKをインストールします。
- トレーニングコードをDockerコンテナ（例：TensorFlowまたはPyTorchと、Horovodやtorch.distributedなどの分散トレーニングサポートを使用）で準備します。
- モデルコードがマルチGPUトレーニング（例：PyTorchのDataParallelまたはDistributedDataParallel経由）をサポートしていることを確認します。

## マルチGPUトレーニングでのVertex AIの使用
Vertex AIは、MLワークフローのためのGCPのマネージドプラットフォームです。複数のGPUを搭載したマシンタイプを指定できるカスタムトレーニングジョブをサポートしています。

### マルチGPUで利用可能なGPUタイプ
少なくとも2つの接続をサポートする一般的なNVIDIA GPU：
- NVIDIA H100（80GBまたはMega 80GB）：大規模モデル向けの高性能。2、4、または8 GPUをサポート。
- NVIDIA A100（40GBまたは80GB）：トレーニングに広く使用。2、4、8、または16 GPUをサポート。
- NVIDIA L4：推論および軽量なトレーニング向けのコスト効率が良い。2、4、または8 GPUをサポート。
- NVIDIA T4またはV100：旧世代ですが利用可能。2、4、または8 GPUをサポート。

完全なリストにはGB200、B200、H200、P4、P100が含まれます。すべてのGPUがすべてのゾーンで利用可能ではないため、リージョンの可用性を確認してください。

### 少なくとも2 GPUを使用するトレーニングジョブの作成手順
1.  **コンテナの準備**：トレーニングスクリプトを含むDockerイメージをビルドし、Google Container RegistryまたはArtifact Registryにプッシュします。PyTorchのDockerfile例：
    ```
    FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime
    COPY train.py /app/train.py
    WORKDIR /app
    CMD ["python", "train.py"]
    ```

2.  **gcloud CLIを使用したジョブの構成**：
    - `config.yaml`ファイルを作成：
      ```yaml
      workerPoolSpecs:
        machineSpec:
          machineType: a3-highgpu-2g  # 例: 2x H100 GPU; 代替: a2-ultragpu-2g (2x A100), g2-standard-24 (2x L4)
          acceleratorType: NVIDIA_H100_80GB  # または NVIDIA_A100_80GB, NVIDIA_L4
          acceleratorCount: 2  # 少なくとも2
        replicaCount: 1
        containerSpec:
          imageUri: gcr.io/your-project/your-image:latest  # あなたのDockerイメージURI
      ```
    - コマンドを実行：
      ```bash
      gcloud ai custom-jobs create \
        --region=us-central1 \  # GPUが利用可能なリージョンを選択
        --display-name=your-training-job \
        --config=config.yaml
      ```

3.  **Python SDKの使用**：
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

4.  **監視とスケーリング**：
    - Vertex AIコンソールを使用してジョブステータスとログを表示します。
    - 複数のマシンにわたる分散トレーニング（例：より多くのレプリカ）の場合、追加のワーカープールを追加し、大規模ジョブには必要に応じてリダクションサーバーを使用します。
    - コスト：GPUは時間単位で課金されます。リージョンの価格を確認してください（例：2x H100は約$6-10/時間）。

5.  **マルチGPUトレーニングのヒント**：
    - コードで分散トレーニングを有効にします（例：`torch.nn.parallel.DistributedDataParallel`）。
    - 中断が許容される場合は、スポットVMまたはリザベーションを使用してコストを削減します。
    - GCPコンソールでリージョン/ゾーンのGPU可用性を確認します。

## 代替案：Compute Engine VMの使用
Vertex AIを使用しないカスタムセットアップを希望する場合：
1.  VMインスタンスを作成：
    - Compute Engine > VM instances > Create instanceに移動します。
    - マシンタイプ：A3（H100）、A2（A100）、G2（L4）シリーズから選択、例：2x H100の場合は`a3-highgpu-2g`。
    - ブートディスク：Deep Learning VMイメージ（CUDA、TensorFlow/PyTorchがプリインストール済み）を使用します。
    - GPUを追加：選択したタイプのアクセラレータを2つ指定します。

2.  VMにSSH接続してトレーニングスクリプトを実行：
    ```bash
    gcloud compute ssh your-vm-name --zone=your-zone
    python train.py  # CUDAが検出されることを確認: nvidia-smi
    ```

3.  マルチGPUの場合：コードがそれを処理する必要があります（例：`CUDA_VISIBLE_DEVICES=0,1`）。

これはより手動での操作が必要ですが、完全な制御が可能です。

## 制限事項と代替案
- RTX 4090と同等の性能が特に必要な場合は、AWS（場合によってはコンシューマーGPUを提供）またはオンプレミスセットアップなどの代替案を検討してください。
- 無料/制限付きのGPUトレーニングの場合は、Google Colab（最大1-2 GPU、ただしマルチGPUまたは4090相当は保証されない）を試してください。
- 必要に応じて、GCPコンソールからクォータを確認し、増加をリクエストしてください。

[カスタムトレーニングのコンピュートリソースを構成する | Vertex AI | Google Cloud](https://cloud.google.com/vertex-ai/docs/training/configure-compute)  
[GPUマシンタイプ | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/gpus)  
[Cloud GPU（グラフィックスプロセッシングユニット）- Google Cloud](https://cloud.google.com/gpu)