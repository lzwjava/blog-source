---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Microsoft Entra ID 存取管理指南
translated: true
type: note
---

Microsoft Entra ID 是一項雲端身分識別與存取管理服務，能協助安全存取應用程式、資料與裝置等資源。它支援驗證（例如登入方法、MFA）、授權（例如角色型存取控制），並能與 Azure 服務整合。開始使用前，您需要擁有 Azure 訂閱帳戶及適當權限（例如全域管理員角色）。

## 開始使用
1. **登入 Azure 入口網站**：前往 [portal.azure.com](https://portal.azure.com)，使用您的 Microsoft 帳戶登入。
2. **導覽至 Microsoft Entra ID**：在頂端搜尋列搜尋「Microsoft Entra ID」，或於「Azure 服務」下尋找。
3. **探索儀表板**：檢視租用戶概覽，包括使用者、群組與應用程式。如有需要，可設定自訂網域等基礎功能。
4. **啟用關鍵功能**：
   - **驗證**：於「驗證方法」下設定自助密碼重設或多重要素驗證 (MFA)。
   - **條件式存取**：在「安全性」>「條件式存取」中建立原則，根據使用者、裝置或位置強制執行規則。

## 管理使用者與群組
- **新增使用者**：前往「使用者」>「新增使用者」，輸入姓名、使用者名稱（例如 user@yourdomain.com）等詳細資料，並指派角色或授權。
- **建立群組**：於「群組」>「新增群組」中選擇安全性或 Microsoft 365 類型，新增成員並用於存取指派。
- **指派授權**：在使用者/群組詳細資料中，前往「授權」指派 Entra ID P1/P2 以使用進階功能，例如 Privileged Identity Management (PIM)。
- **最佳實踐**：遵循最低權限原則——指派最小必要權限，並使用群組進行批次管理。

## 管理應用程式
- **註冊應用程式**：於「應用程式註冊」>「新增註冊」中提供名稱、重新導向 URI 及支援的帳戶類型（單一租用戶、多租用戶等）。
- **新增企業應用程式**：針對第三方應用程式，前往「企業應用程式」>「新增應用程式」瀏覽資源庫或建立非資源庫應用程式。
- **設定存取權**：於「使用者和群組」下指派使用者/群組至應用程式，並透過 SAML 或 OAuth 設定單一登入 (SSO)。
- **佈建身分識別**：於「佈建」下自動化使用者同步至應用程式，實現即時存取。

針對混合設定（內部部署 AD），請使用 Microsoft Entra Connect 同步身分識別。透過「監視」>「登入記錄」中的記錄監控使用情況。

# 如何檢查資料庫、Kubernetes (AKS) 或其他資源的存取權

Azure 中的存取權是透過與 Entra ID 整合的角色型存取控制 (RBAC) 進行管理。使用者透過 Entra 憑證進行驗證，角色則定義權限。若要檢查存取權，請使用 Azure 入口網站的 IAM（身分識別與存取管理）工具。這會列出直接指派、從父範圍（例如訂閱）繼承的指派，以及拒絕指派。

## 適用於任何 Azure 資源的通用步驟
1. **開啟資源**：在 Azure 入口網站中，導覽至目標資源（例如資源群組、VM、儲存體帳戶）。
2. **前往存取控制 (IAM)**：從左側選單選擇「存取控制 (IAM)」。
3. **檢查存取權**：
   - 檢查自身存取權：點擊「檢查存取權」>「檢視我的存取權」，查看此範圍及繼承的指派。
   - 檢查特定使用者/群組/服務主體：
     - 點擊「檢查存取權」>「檢查存取權」。
     - 選擇「使用者、群組或服務主體」。
     - 依名稱或電子郵件搜尋。
     - 在結果窗格中檢視角色指派（例如擁有者、參與者）與有效權限。
4. **檢視合格指派**（若使用 PIM）：切換至「合格指派」分頁查看即時角色。
5. **PowerShell/CLI 替代方案**：使用 `az role assignment list --assignee <user> --scope <resource-id>` 進行指令碼檢查。

注意：此操作不包含子範圍指派；如有需要請深入檢視。

## 檢查 Azure SQL Database 存取權
Azure SQL 使用 Entra 驗證適用於自主資料庫使用者（綁定至 Entra 身分識別，非 SQL 登入）。
1. **設定 Entra 管理員（若未設定）**：在 SQL 伺服器概覽 > 設定下的「Microsoft Entra ID」>「設定管理員」。搜尋並選擇使用者/群組，然後儲存。這將啟用整個叢集的 Entra 驗證。
2. **檢查伺服器層級存取權**：
   - 在 SQL 伺服器窗格 >「Microsoft Entra ID」中，檢視管理員欄位查看指派的身分識別。
   - 查詢 `master` 資料庫：`SELECT name, type_desc FROM sys.database_principals WHERE type IN ('E', 'X');`（E 代表外部使用者，X 代表外部群組）。
3. **檢查資料庫層級存取權**：
   - 使用 SSMS 透過 Entra 驗證連線至資料庫（在連線對話框中選擇「Microsoft Entra - 通用與 MFA」）。
   - 執行 `SELECT * FROM sys.database_principals;` 或 `EXEC sp_helprolemember;` 列出使用者與角色。
4. **疑難排解**：若登入失敗（例如錯誤 33134），請檢查 Entra 條件式存取原則是否允許 Microsoft Graph API 存取。

使用者預設擁有 `CONNECT` 權限；可透過 T-SQL 授予角色如 `db_datareader`：`ALTER ROLE db_datareader ADD MEMBER [user@domain.com];`。

## 檢查 AKS (Kubernetes 叢集) 存取權
AKS 整合 Entra ID 進行驗證，並使用 Azure RBAC 或 Kubernetes RBAC 進行授權。
1. **Azure 層級存取權（至 AKS 資源）**：
   - 在 AKS 叢集資源上遵循上述通用步驟。
   - 常見角色：「Azure Kubernetes Service 叢集管理員」擁有完整 kubeconfig 存取權；「讀者」為唯讀權限。
2. **Kubernetes API 存取權**：
   - 透過 `az login` 進行驗證（使用 Entra 權杖）。
   - 取得 kubeconfig：`az aks get-credentials --resource-group <rg> --name <cluster>`。
   - 檢查繫結：`kubectl auth can-i <verb> <resource> --as <user@domain.com> -n <namespace>`。
   - 列出叢集角色：`kubectl get clusterrolebindings | grep <user-or-group>`。
3. **使用 Entra 群組**：將 Kubernetes 角色/繫結指派給群組以實現擴展性。以下為命名空間角色的範例 YAML（使用 `kubectl apply -f file.yaml` 套用）：
   ```
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: example-binding
     namespace: default
   subjects:
   - kind: Group
     name: finance-group  # Entra 群組
     apiGroup: rbac.authorization.k8s.io
   roleRef:
     kind: Role
     name: example-role
     apiGroup: rbac.authorization.k8s.io
   ```
4. **最佳實踐**：使用最低權限角色、與 PIM 整合實現即時權限提升，並避免使用固定憑證——對 Pod 使用工作負載身分識別。

若 Pod 需存取資源（例如從 AKS 存取 SQL），請指派受控身分識別，並透過這些身分識別的 Azure RBAC 進行檢查。

[Microsoft Entra ID 文件](https://learn.microsoft.com/en-us/entra/identity/)  
[檢查單一 Azure 資源的存取權](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)  
[設定 Azure SQL 的 Entra 驗證](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure?view=azuresql)  
[AKS 身分識別與存取最佳實踐](https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-identity)