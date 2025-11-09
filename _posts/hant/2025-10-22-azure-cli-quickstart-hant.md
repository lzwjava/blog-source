---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Azure CLI 快速入門指南
translated: true
type: note
---

Azure CLI（命令列介面）是一套跨平台工具組，可透過命令列管理 Azure 資源。它非常適合用於自動化任務、編寫部署腳本，以及與 Azure 服務互動，而無需使用網頁入口網站。它支援在 Windows、macOS 和 Linux 上使用 Bash、PowerShell 及命令提示字元。

## 安裝

1. **先決條件**：確保已安裝 Python 3.8 或更高版本（可透過 `python --version` 檢查）。

2. **透過套件管理員安裝**（推薦）：
   - **Windows**：使用 Winget（`winget install Microsoft.AzureCLI`）或 Chocolatey（`choco install azure-cli`）。
   - **macOS**：使用 Homebrew（`brew install azure-cli`）。
   - **Linux（Ubuntu/Debian）**：執行 `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`。
   - **其他 Linux**：使用 RPM 或從官方網站手動下載。

3. **驗證安裝**：開啟終端機並執行 `az --version`。您應該會看到 CLI 版本（例如，截至 2025 年底為 2.64.0）。

如需詳細的平台特定步驟，請參閱官方安裝文件。

## 驗證

使用 Azure CLI 前，請先登入您的 Azure 帳戶：

1. **互動式登入**：執行 `az login`。這將開啟瀏覽器進行 Microsoft Entra ID 驗證。請按照提示登入。

2. **服務主體（用於自動化）**：使用 `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}` 建立服務主體。然後使用 `az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>`。

3. **檢查登入狀態**：使用 `az account show` 驗證您的有效訂閱。

4. **登出**：`az logout`。

支援多重要素驗證（MFA），您可以使用 `az account set --subscription <id>` 管理多個訂閱。

## 基本命令

Azure CLI 使用 `az` 命令，後接群組（例如 `vm`、`storage`）和子命令。使用 `az --help` 取得概覽，或使用 `az <group> --help` 取得特定說明。

### 常用全域選項
- `--help` 或 `-h`：顯示說明。
- `--output table/json/yaml`：格式化輸出（預設：表格）。
- `--query`：用於篩選 JSON 輸出的 JMESPath 查詢（例如 `--query "[].name"`）。

### 關鍵範例
- **列出訂閱**：`az account list --output table`
- **取得資源群組**：`az group list --output table`
- **建立資源群組**：`az group create --name "MyResourceGroup" --location "eastus"`

## 管理虛擬機器（VM）
Azure CLI 擅長管理 VM 生命週期。

1. **建立 VM**：
   ```
   az vm create \
     --resource-group "MyResourceGroup" \
     --name "MyVM" \
     --image Ubuntu2204 \
     --admin-username azureuser \
     --admin-password MyP@ssw0rd123! \
     --location "eastus"
   ```

2. **列出 VM**：`az vm list --output table`

3. **啟動/停止 VM**：`az vm start --name "MyVM" --resource-group "MyResourceGroup"` 或 `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4. **SSH 連線至 VM**：`az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5. **刪除 VM**：`az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## 管理儲存體帳戶
1. **建立儲存體帳戶**：
   ```
   az storage account create \
     --name mystorageaccount \
     --resource-group "MyResourceGroup" \
     --location "eastus" \
     --sku Standard_LRS
   ```

2. **上傳 Blob**：首先使用 `az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"` 取得金鑰。然後：`az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## 其他常見情境
- **部署 ARM 範本**：`az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
- **查詢資源**：`az resource list --resource-group "MyResourceGroup" --output table`
- **更新 CLI**：`az upgrade`
- **擴充功能**：安裝擴充功能，例如 `az extension add --name azure-devops` 以取得額外命令。

用於腳本編寫時，可結合 Bash/PowerShell 迴圈，或在 CI/CD 管道（如 GitHub Actions）中使用 Azure CLI。

## 提示與最佳實踐
- 使用 `--dry-run` 進行預覽（在支援的情況下）。
- 啟用自動完成：在 Bash 上執行 `az completion`。
- 處理錯誤：檢查結束代碼（0 表示成功）並使用 `--debug` 進行疑難排解。
- 安全性：避免硬編碼憑證；使用環境變數或 Azure Key Vault。

## 參考資料
[安裝 Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  
[Azure CLI 參考](https://learn.microsoft.com/en-us/cli/azure/)  
[Azure CLI 快速入門](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)