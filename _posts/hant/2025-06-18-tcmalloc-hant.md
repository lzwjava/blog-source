---
audio: false
generated: true
lang: hant
layout: post
title: 修復 TCMalloc 錯誤
translated: true
type: note
---

錯誤「Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)」表示您的 Linux 系統中未安裝或未正確配置 TCMalloc 庫（Google gperftools 的一部分）。TCMalloc 是一種記憶體分配器，可提升效能並減少記憶體使用量，特別是在 Stable Diffusion 這類應用程式中。以下是解決此問題的方法：

### 修復 TCMalloc 錯誤的步驟

1. **安裝 TCMalloc 與 Google Perftools**
   根據您的 Linux 發行版，使用適當的套件管理員安裝所需函式庫。

   - **適用於 Ubuntu/Debian 系統**：
     ```bash
     sudo apt-get update
     sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
     ```
     此指令會安裝完整的 `libgoogle-perftools-dev`（包含 TCMalloc）及輕量版 `libtcmalloc-minimal4`。

   - **適用於 Fedora 系統**：
     ```bash
     sudo dnf install gperftools-libs -y
     ```
     此指令會安裝必要的 TCMalloc 函式庫。

   - **適用於 CentOS/RHEL 系統**：
     ```bash
     sudo yum install gperftools-libs -y
     ```
     若預設儲存庫中沒有此套件，您可能需要先啟用 EPEL 儲存庫：
     ```bash
     sudo yum install epel-release
     sudo yum install gperftools-libs -y
     ```

2. **驗證安裝**
   安裝完成後，檢查 TCMalloc 是否已安裝：
   ```bash
   dpkg -l | grep tcmalloc
   ```
   您應該會看到 `libtcmalloc-minimal4` 或類似套件列於清單中。或者檢查函式庫路徑：
   ```bash
   dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
   ```
   此指令將顯示 TCMalloc 函式庫的路徑（例如 `/usr/lib/libtcmalloc.so.4`）。

3. **設定 LD_PRELOAD 環境變數**
   為確保應用程式使用 TCMalloc，請將 `LD_PRELOAD` 環境變數指向 TCMalloc 函式庫。此設定可暫時或永久生效。

   - **暫時設定（僅當前工作階段有效）**：
     執行應用程式時設定 `LD_PRELOAD`：
     ```bash
     export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
     ./launch.py
     ```
     若步驟 2 中找到的路徑不同，請將 `/usr/lib/libtcmalloc.so.4` 替換為實際路徑。

   - **永久設定（適用於 Stable Diffusion 等應用）**：
     若您使用如 `webui.sh` 的腳本（常見於 Stable Diffusion），請編輯腳本（例如 `webui-user.sh`）並加入：
     ```bash
     export LD_PRELOAD=libtcmalloc.so.4
     ```
     儲存檔案後重新執行腳本：
     ```bash
     ./webui.sh
     ```
     或將其加入您的 shell 設定檔（例如 `~/.bashrc` 或 `~/.zshrc`）：
     ```bash
     echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
     source ~/.bashrc
     ```

4. **重新執行應用程式**
   安裝 TCMalloc 並設定 `LD_PRELOAD` 後，重新啟動應用程式：
   ```bash
   ./launch.py
   ```
   錯誤訊息應不再出現，且您可能會觀察到記憶體使用量或效能有所改善。

5. **疑難排解**
   - **若函式庫路徑不正確**：若 `LD_PRELOAD` 設定失敗（例如「cannot open shared object file」），請驗證確切的函式庫名稱與路徑：
     ```bash
     find /usr/lib -name "libtcmalloc*.so*"
     ```
     使用正確路徑更新 `LD_PRELOAD`（例如若使用輕量版則為 `libtcmalloc_minimal.so.4`）。
   - **若錯誤持續出現**：請確認安裝的 TCMalloc 版本與您的系統相容（您的系統環境為 glibc 2.35 與 GCC 11.4.0）。若問題仍未解決，可嘗試從原始碼編譯安裝：
     ```bash
     git clone https://github.com/google/tcmalloc.git
     cd tcmalloc
     bazel build //tcmalloc:hello_main
     bazel run //tcmalloc:hello_main
     ```
     詳細操作請參閱 TCMalloc 快速入門指南。
   - **記憶體問題**：若遇到記憶體分配失敗或程式崩潰，請確保系統記憶體充足且 TCMalloc 未與其他記憶體分配器衝突。

6. **選項：驗證 TCMalloc 使用狀態**
   若要確認 TCMalloc 正常運作，可執行簡單測試程式，或在應用程式運行時使用 `top` 或 `htop` 等工具檢查記憶體使用狀況。TCMalloc 通常能減少記憶體碎片化並帶來輕微的效能提升。

### 補充說明
- **為何使用 TCMalloc？** TCMalloc 是一種高效能記憶體分配器，可降低 CPU 記憶體使用量與碎片化問題，尤其對 Stable Diffusion 這類多執行緒應用程式效果顯著。雖非必要安裝，但能有效提升效能。
- **相容性**：您的系統環境（glibc 2.35、Python 3.10.12、GCC 11.4.0）與最新版 TCMalloc 相容，因此上述步驟應可正常運作。若使用自編譯應用程式，請確保其編譯時已啟用 TCMalloc 支援。
- **Stable Diffusion 相關情境**：此錯誤常出現於 AUTOMATIC1111 的 Stable Diffusion WebUI 中。上述步驟（特別是安裝 `libgoogle-perftools-dev` 與設定 `LD_PRELOAD`）經確認可解決此問題。

若您遇到特定錯誤或需要針對某個 Linux 發行版的進一步協助，請告知，我將提供更詳細的客製化說明！