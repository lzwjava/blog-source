---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上安裝 Outline Client
translated: true
type: note
---

是的，你可以在 Ubuntu 上安裝 Outline Client，因為它是基於 Debian 的 Linux 發行版，而 Outline Client 以 Debian 套件形式提供，與 Ubuntu 相容。有兩種安裝方法：推薦使用軟體庫的方法，以及直接下載 Debian 套件的替代方法。下面我將說明如何使用推薦的軟體庫方法進行安裝，這種方法更可取，因為它能與 Ubuntu 的套件管理工具整合，讓更新管理更輕鬆。

### 在 Ubuntu 上安裝 Outline Client 的步驟（推薦方法）

請按照以下步驟在你的 Ubuntu 系統上安裝 Outline Client：

1. **開啟終端機**  
   啟動 Ubuntu 系統上的終端機應用程式。你可以透過在應用程式選單中搜尋「Terminal」或按 `Ctrl + Alt + T` 來完成此操作。

2. **安裝 Outline 的軟體庫金鑰**  
   執行以下命令，將軟體庫的簽署金鑰下載並添加到系統的受信任金鑰中。這可確保來自該軟體庫的套件經過真實性驗證：
   ```bash
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   ```

3. **添加 Outline Client 軟體庫**  
   執行此命令，將 Outline Client 軟體庫添加到系統的來源列表中。這會告訴 Ubuntu 在哪裡找到 Outline Client 套件：
   ```bash
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
   - 注意：`[arch=amd64]` 部分指定這是用於 64 位元系統。大多數現代的 Ubuntu 安裝都是 64 位元，但你可以執行 `uname -m` 來確認系統的架構。如果輸出是 `x86_64`，則表示你使用的是 64 位元系統，此命令將按原樣運作。

4. **更新套件列表**  
   重新整理系統的套件列表，以包含新添加的 Outline 軟體庫：
   ```bash
   sudo apt update
   ```

5. **安裝 Outline Client**  
   使用此命令安裝最新版本的 Outline Client：
   ```bash
   sudo apt install outline-client
   ```

### 安裝後步驟

- **啟動 Outline Client**：安裝後，你可以在應用程式選單中找到 Outline Client，或透過在終端機中輸入 `outline-client` 來啟動它。
- **保持更新**：要檢查並安裝更新，請使用 Ubuntu 的標準更新命令：
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
  這些命令將更新所有已安裝的套件，包括 Outline Client，因為它是透過軟體庫管理的。請注意，從 1.15 版開始，Linux 版 Outline Client 的應用程式內自動更新功能已被停用，因此依賴套件管理工具是保持最新的最佳方式。
- **解除安裝**：如果需要移除 Outline