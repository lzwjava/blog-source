---
audio: false
generated: true
lang: hant
layout: post
title: 穩定擴散代理問題
translated: true
type: note
---

根據錯誤訊息和您的環境，以下是修復「Unknown scheme for proxy URL」問題的方法：

### 解決方案：
此錯誤發生是因為 **`httpx` 預設不支援 `socks://` 代理**。您有兩個選擇：

#### 選項 1：移除 SOCKS 代理參考
1. 檢查環境變數中是否有殘留的代理設定：
   ```bash
   env | grep -i proxy
   ```
   尋找 `socks://` 相關參考（特別是 `ALL_PROXY` 或 `http_proxy`）。

2. 取消設定有問題的變數（將 `VAR_NAME` 替換為上面找到的實際變數名稱）：
   ```bash
   unset VAR_NAME  # 例如：unset ALL_PROXY
   ```

#### 選項 2：為 `httpx` 添加 SOCKS 支援
1. 啟動您的 Python 虛擬環境：
   ```bash
   source /home/lzw/Projects/stable-diffusion-webui/venv/bin/activate
   ```

2. 安裝必要的依賴項：
   ```bash
   pip install -U "httpx[socks]"
   ```

3. 停用環境：
   ```bash
   deactivate
   ```

### 問題原因：
- 您的主要代理（`HTTP_PROXY/HTTPS_PROXY`）使用 `http://`（受支援），但某些程式（可能是其他應用程式/腳本）設定了一個 `httpx` 在沒有額外套件時無法處理的 `socks://` 代理。
- 堆疊追蹤顯示 Gradio/`httpx` 正嘗試使用 `socks://127.0.0.1:7891`，但這不在您的 `checkproxy` 輸出中。

### 驗證：
修復後，請執行：
```bash
./webui.sh
```
SOCKS 代理錯誤應該會消失。

> 💡 **注意**：如果您沒有故意設定 SOCKS 代理，請檢查可能自動設定代理的應用程式（例如 VPN、網路管理員或 Shell 設定檔如 `~/.bashrc`）。

---

錯誤 `Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check` 表示 Stable Diffusion WebUI 使用的 PyTorch 無法偵測或存取相容的 GPU。這可能是由於缺少 CUDA 函式庫、不相容的 GPU、驅動程式問題或設定問題所致。以下是針對您的環境（glibc 2.35、Python 3.10.12、GCC 11.4.0，根據 glibc 版本推測為 Ubuntu 22.04）修復此問題的步驟。

### 解決問題的步驟

#### 1. **驗證 GPU 和 CUDA 相容性**
   - **檢查是否擁有 NVIDIA GPU**：
     執行：
     ```bash
     lspci | grep -i nvidia
     ```
     這將列出 NVIDIA 硬體。如果沒有輸出，表示您的系統可能沒有 NVIDIA GPU，而 PyTorch 需要 NVIDIA GPU 才能支援 CUDA。
   - **檢查 NVIDIA 驅動程式安裝**：
     執行：
     ```bash
     nvidia-smi
     ```
     如果已安裝，將顯示包含 GPU 詳細資訊的表格（例如驅動程式版本、CUDA 版本）。如果未安裝，請安裝 NVIDIA 驅動程式：
     ```bash
     sudo apt-get update
     sudo apt-get install nvidia-driver-<version> nvidia-utils-<version> -y
     ```
     將 `<version>` 替換為最新的穩定驅動程式版本（例如 `535` 或 `550`）。使用以下指令尋找合適的驅動程式版本：
     ```bash
     ubuntu-drivers devices
     sudo ubuntu-drivers autoinstall
     ```
   - **檢查 CUDA 版本**：
     PyTorch 需要 CUDA 函式庫。檢查已安裝的 CUDA 版本：
     ```bash
     nvcc --version
     ```
     如果未安裝，請安裝 CUDA Toolkit：
     ```bash
     sudo apt-get install nvidia-cuda-toolkit -y
     ```
     或者，從 NVIDIA 官網下載最新的 CUDA Toolkit（例如 CUDA 11.8 或 12.1）並遵循其安裝指南。

#### 2. **驗證 PyTorch 安裝**
   錯誤表明 PyTorch 已安裝但無法使用 GPU。請確保您擁有正確且支援 CUDA 的 PyTorch 版本。
   - **檢查 PyTorch 安裝**：
     執行：
     ```bash
     python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
     ```
     預期輸出應包含 PyTorch 版本（例如 `2.0.1`）和 `torch.cuda.is_available()` 為 `True`。如果為 `False`，表示 PyTorch 無法偵測到 GPU。
   - **重新安裝支援 CUDA 的 PyTorch**：
     對於 Python 3.10 和 CUDA（例如 11.8），請在您的 Stable Diffusion 環境中安裝 PyTorch：
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```
     將 `cu118` 替換為您的 CUDA 版本（例如 CUDA 12.1 使用 `cu121`）。請在 PyTorch 官網查看支援的版本。
   - **重新安裝後驗證**：
     再次執行檢查：
     ```bash
     python3 -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
     ```

#### 3. **繞過 CUDA 檢查（臨時解決方案）**
   如果您想在沒有 GPU 支援的情況下執行 Stable Diffusion（例如在 CPU 上測試），請透過將 `--skip-torch-cuda-test` 加入命令列參數來繞過 CUDA 檢查。
   - 編輯 `webui-user.sh`（如果不存在則建立）：
     ```bash
     nano /home/lzw/Projects/stable-diffusion-webui/webui-user.sh
     ```
     新增或修改 `COMMANDLINE_ARGS` 行：
     ```bash
     export COMMANDLINE_ARGS="--skip-torch-cuda-test"
     ```
     儲存並離開。
   - 執行腳本：
     ```bash
     ./webui.sh
     ```
     這將允許 Stable Diffusion 在 CPU 上執行，但效能會顯著較慢。

#### 4. **確保 TCMalloc 正確設定**
   您的輸出顯示已偵測到 TCMalloc（`libtcmalloc_minimal.so.4`）並透過 `LD_PRELOAD` 連結。請確認其運作正常：
   ```bash
   echo $LD_PRELOAD
   ```
   如果輸出為 `/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4`，表示設定正確。如果沒有，請手動設定：
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```
   或將其加入 `webui-user.sh`：
   ```bash
   export LD_PRELOAD=/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
   ```

#### 5. **檢查環境變數和路徑**
   確保您的環境已正確設定：
   - **檢查 LD_LIBRARY_PATH**：
     CUDA 函式庫必須可存取。如有需要，請加入：
     ```bash
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     將此行加入 `~/.bashrc` 或 `webui-user.sh` 以永久生效。
   - **啟動虛擬環境**：
     執行前請務必啟動 Stable Diffusion 虛擬環境：
     ```bash
     cd /home/lzw/Projects/stable-diffusion-webui
     source venv/bin/activate
     ```

#### 6. **更新 Stable Diffusion WebUI**
   您的版本（`v1.10.1`，提交 `82a973c`）可能存在相容性問題。請更新至最新版本：
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   git pull
   ```
   然後，重新安裝依賴項：
   ```bash
   ./webui.sh
   ```

#### 7. **疑難排解**
   - **如果 `nvidia-smi` 失敗**：請重新安裝 NVIDIA 驅動程式或檢查 GPU 硬體問題。
   - **如果 PyTorch 仍無法偵測 GPU**：
     - 確保 CUDA 和 cuDNN 已正確安裝。如果缺少 cuDNN，請安裝：
       ```bash
       sudo apt-get install libcudnn8
       ```
     - 驗證 CUDA 版本與您的 GPU 和 PyTorch 的相容性。例如，較舊的 GPU（例如 Kepler 系列）可能不支援 CUDA 12。
   - **如果錯誤持續存在**：請檢查 Stable Diffusion 日誌以獲取詳細錯誤：
     ```bash
     cat /home/lzw/Projects/stable-diffusion-webui/log/webui.log
     ```
     分享任何特定錯誤以獲得進一步協助。
   - **硬體限制**：如果您的 GPU 過於老舊（例如 2016 年以前的 NVIDIA GPU），可能不支援現代 CUDA 版本。在這種情況下，請使用 `--skip-torch-cuda-test` 或升級您的 GPU。

#### 8. **執行應用程式**
   套用修復後，執行 WebUI：
   ```bash
   cd /home/lzw/Projects/stable-diffusion-webui
   ./webui.sh
   ```
   如果您修復了 GPU 問題，錯誤應該會消失。如果使用 `--skip-torch-cuda-test`，它將在 CPU 上執行。

### 注意事項
- **系統資訊**：您的設定（glibc 2.35、Python 3.10.12、GCC 11.4.0）推測為 Ubuntu 22.04，它與 CUDA 11.8 或 12.1 以及近期 PyTorch 版本相容。
- **效能**：在 CPU 上執行（使用 `--skip-torch-cuda-test`）是一種備用方案，但速度會很慢。建議修復 GPU 支援以獲得 Stable Diffusion 的最佳效能。
- **TCMalloc**：根據您的輸出，TCMalloc 問題似乎已解決。如果遇到記憶體相關問題，請確保 `LD_PRELOAD` 保持設定。

如果您仍然遇到問題或需要有關特定錯誤訊息的幫助，請提供更多詳細資訊（例如 GPU 型號、CUDA 版本或完整日誌），我們可以進一步完善解決方案！