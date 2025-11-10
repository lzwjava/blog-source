---
audio: false
generated: true
lang: ja
layout: post
title: 安定拡散プロキシ問題
translated: true
type: note
---

エラーと環境に基づいて、「Unknown scheme for proxy URL」の問題を修正する方法を以下に示します：

### 解決策：
このエラーは、**`httpx` がデフォルトでは `socks://` プロキシをサポートしていない**ために発生します。以下の2つの選択肢があります：

#### 選択肢 1: SOCKS プロキシ参照を削除する
1. 環境変数から不要なプロキシ設定を確認します：
   ```bash
   env | grep -i proxy
   ```
   `socks://` 参照（特に `ALL_PROXY` または `http_proxy`）を探してください。

2. 問題のある変数を未設定にします（上記で見つかった実際の変数名で `VAR_NAME` を置き換えてください）：
   ```bash
   unset VAR_NAME  # 例: unset ALL_PROXY
   ```

#### 選択肢 2: `httpx` に SOCKS サポートを追加する
1. Python 仮想環境をアクティベートします：
   ```bash
   source /home/lzw/Projects/stable-diffusion-webui/venv/bin/activate
   ```

2. 必要な依存関係をインストールします：
   ```bash
   pip install -U "httpx[socks]"
   ```

3. 環境をデアクティベートします：
   ```bash
   deactivate
   ```

### 原因：
- メインプロキシ（`HTTP_PROXY/HTTPS_PROXY`）は `http://`（サポート対象）を使用していますが、何か（別のアプリやスクリプト）が `httpx` が追加パッケージなしでは扱えない `socks://` プロキシを設定しています。
- スタックトレースは、Gradio/`httpx` が `socks://127.0.0.1:7891` を使用しようとしていることを示していますが、これは `checkproxy` の出力にはありません。

### 検証：
修正後、以下を実行します：
```bash
./webui.sh
```
SOCKS プロキシエラーは消えるはずです。

> 💡 **注意**: SOCKS プロキシを意図的に設定していない場合は、プロキシを自動設定する可能性のあるアプリケーション（VPN、ネットワークマネージャ、または `~/.bashrc` などのシェル設定ファイル）を調査してください。

---

エラー `Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check` は、Stable Diffusion WebUI で使用されている PyTorch が、互換性のある GPU を検出またはアクセスできないことを示しています。これは、CUDA ライブラリの欠落、互換性のない GPU、ドライバの問題、または設定の問題が原因である可能性があります。以下に、お使いの環境（glibc 2.35、Python 3.10.12、GCC 11.4.0、glibc バージョンから Ubuntu 22.04 と思われる）に合わせたこの問題を修正する手順を示します。

### 問題を修正する手順

#### 1. **GPU と CUDA の互換性を確認する**
   - **NVIDIA GPU があるか確認**：
     以下を実行：
     ```bash
     lspci | grep -i nvidia
     ```
     これにより NVIDIA ハードウェアが一覧表示されます。出力がない場合、システムに NVIDIA GPU がない可能性があり、PyTorch は CUDA サポートに NVIDIA GPU を必要とします。
   - **NVIDIA ドライバのインストールを確認**：
     以下を実行：
     ```bash
     nvidia-smi
     ```
     インストールされている場合、GPU の詳細（ドライババージョン、CUDA バージョンなど）を含むテーブルが表示されます。インストールされていない場合は、NVIDIA ドライバをインストールします：
     ```bash
     sudo apt-get update
     sudo apt-get install nvidia-driver-<version> nvidia-utils-<version> -y
     ```
     `<version>` は最新の安定版ドライバ（例: `535` または `550`）に置き換えてください。適切なドライババージョンは以下で確認できます：
     ```bash
     ubuntu-drivers devices
     sudo ubuntu-drivers autoinstall
     ```
   - **CUDA バージョンを確認**：
     PyTorch は CUDA ライブラリを必要とします。インストールされている CUDA バージョンを確認します：
     ```bash
     nvcc --version
     ```
     インストールされていない場合は、CUDA Toolkit をインストールします：
     ```bash
     sudo apt-get install nvidia-cuda-toolkit -y
     ```
     または、NVIDIA のウェブサイトから最新の CUDA Toolkit（例: CUDA 11.8 または 12.1）をダウンロードし、インストールガイドに従ってください。

#### 2. **PyTorch のインストールを確認する**
   このエラーは、PyTorch がインストールされているが GPU を使用できないことを示唆しています。CUDA サポートを含む正しい PyTorch バージョンがインストールされていることを確認してください。
   - **PyTorch のインストールを確認**：
     以下を実行：
     ```bash
     python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
     ```
     期待される出力は、PyTorch バージョン（例: `2.0.1`）と `torch.cuda.is_available()` が `True` であることです。`False` の場合、PyTorch は GPU を検出していません。
   - **CUDA サポートを含む PyTorch を再インストール**：
     Python 3.10 および CUDA（例: 11.8）の場合、Stable Diffusion 環境内で PyTorch をインストールします：
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```
     `cu118` をお使いの CUDA バージョン（例: CUDA 12.1 の場合は `cu121`）に置き換えてください。サポートされているバージョンは PyTorch の公式サイトで確認してください。
   - **再インストール後に確認**：
     再度チェックを実行：
     ```bash
     python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
     ```

#### 3. **CUDA チェックをバイパスする（一時的な回避策）**
   GPU サポートなしで Stable Diffusion を実行したい場合（例: CPU でのテスト）、コマンドライン引数に `--skip-torch-cuda-test` を追加して CUDA チェックをバイパスします。
   - `webui-user.sh` を編集（存在しない場合は作成）：
     ```bash
     nano /home/lzw/Projects/stable-diffusion-webui/webui-user.sh
     ```
     `COMMANDLINE_ARGS` 行を追加または修正：
     ```bash
     export COMMANDLINE_ARGS="--skip-torch-cuda-test"
     ```
     保存して終了。
   - スクリプトを実行：
     ```bash
     ./webui.sh
     ```
     これにより CPU で Stable Diffusion が実行されますが、パフォーマンスは大幅に低下します。

#### 4. **TCMalloc が適切に設定されていることを確認する**
   出力では TCMalloc（`libtcmalloc_minimal.so.4`）が検出され、`LD_PRELOAD` でリンクされていることが示されています。動作を確認します：
   ```bash
   echo $LD_PRELOAD
   ```
   `/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4` が出力される場合は設定済みです。そうでない場合は、手動で設定します：
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```
   または `webui-user.sh` に追加：
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```

#### 5. **環境変数とパスを確認する**
   環境が正しく設定されていることを確認します：
   - **LD_LIBRARY_PATH を確認**：
     CUDA ライブラリにアクセスできる必要があります。必要に応じて追加：
     ```bash
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     永続化するには、これを `~/.bashrc` または `webui-user.sh` に追加します。
   - **仮想環境をアクティベート**：
     実行前には常に Stable Diffusion 仮想環境をアクティベート：
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     ```

#### 6. **Stable Diffusion WebUI を更新する**
   お使いのバージョン（`v1.10.1`、コミット `82a973c`）に互換性の問題がある可能性があります。最新バージョンに更新：
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   git pull
   ```
   その後、依存関係を再インストール：
   ```bash
   ./webui.sh
   ```

#### 7. **トラブルシューティング**
   - **`nvidia-smi` が失敗する場合**：NVIDIA ドライバを再インストールするか、GPU ハードウェアの問題を確認。
   - **PyTorch がまだ GPU を検出しない場合**：
     - CUDA と cuDNN が正しくインストールされていることを確認。cuDNN が欠落している場合はインストール：
       ```bash
       sudo apt-get install libcudnn8
       ```
     - お使いの GPU および PyTorch との CUDA バージョン互換性を確認。例えば、古い GPU（Kepler シリーズなど）は CUDA 12 をサポートしていない可能性があります。
   - **エラーが解消しない場合**：詳細なエラーについて Stable Diffusion ログを確認：
     ```bash
     cat /home/lzw/Projects/stable-diffusion-webui/log/webui.log
     ```
     具体的なエラーがあれば、さらなる支援のために共有してください。
   - **ハードウェア制限**：GPU が古すぎる場合（2016年以前の NVIDIA GPU など）、最新の CUDA バージョンをサポートしていない可能性があります。この場合、`--skip-torch-cuda-test` を使用するか、GPU をアップグレードしてください。

#### 8. **アプリケーションを実行する**
   修正を適用後、WebUI を実行：
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   ./webui.sh
   ```
   GPU の問題を修正した場合、エラーは消えるはずです。`--skip-torch-cuda-test` を使用している場合、CPU で実行されます。

### 注意点
- **システム情報**：お使いの設定（glibc 2.35、Python 3.10.12、GCC 11.4.0）は Ubuntu 22.04 を示唆しており、CUDA 11.8 または 12.1 および最近の PyTorch バージョンと互換性があります。
- **パフォーマンス**：CPU での実行（`--skip-torch-cuda-test` 使用）は代替手段ですが、低速になります。Stable Diffusion には GPU サポートの修正を推奨します。
- **TCMalloc**：出力に基づくと、TCMalloc の問題は解決したようです。メモリ関連の問題が発生した場合は、`LD_PRELOAD` が設定されたままにしてください。

まだ問題が発生する場合、または特定のエラーメッセージについてヘルプが必要な場合は、追加の詳細（GPU モデル、CUDA バージョン、完全なログなど）を提供していただければ、解決策を改良できます！