---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 Active Directory 管理手提電腦存取權限
translated: true
type: note
---

### 什麼是 Windows 中的 Active Directory (AD)？

Active Directory (AD) 是微軟為 Windows 網域網路開發的目錄服務。它作為一個集中式資料庫，儲存並組織網路物件的相關資訊，例如使用者帳戶、電腦帳戶、印表機、共享資料夾及其他資源。這種階層式結構讓管理員能夠有效率地管理和保護整個組織內對這些資源的存取。

其核心元件是 **Active Directory Domain Services (AD DS)**，負責儲存目錄資料並提供給使用者和管理員使用。主要功能包括：
- **安全整合**：使用單一使用者名稱和密碼在整個網路中進行身份驗證和存取控制。
- **結構描述**：定義物件類型（例如使用者、電腦）及其屬性的規則。
- **通用類別目錄**：一個可搜尋的目錄物件索引，無論物件位置為何都能快速查詢。
- **複寫**：自動在網域控制站之間同步變更，以保持資料一致性。
- **查詢和索引機制**：允許使用者和應用程式搜尋及擷取目錄資訊。

**AD 帳戶**通常指在 AD 中建立和儲存的使用者帳戶（或電腦帳戶）。這些帳戶包含使用者名稱、密碼、電子郵件地址和群組成員資格等詳細資訊，從而實現安全登入和資源存取。

本質上，AD 透過在 Windows 環境中為身份識別和權限提供單一控制點，取代了分散在各個電腦上的本機帳戶，從而簡化了 IT 管理。

### 如何使用 Active Directory 管理員工筆記型電腦存取權限

AD 在管理筆記型電腦存取方面非常強大，因為它集中管理使用者身份識別和原則，即使對於遠端或移動設備也能確保一致執行。這可以防止員工擁有完整的本機管理員權限（降低安全風險），同時允許受控存取必要的工具。以下是逐步指南：

1. **設定 AD 網域**：
   - 在 Windows Server（作為網域控制站）上安裝 AD DS。
   - 透過伺服器管理員或 PowerShell 建立您的網域（例如 company.local）。

2. **將筆記型電腦加入網域**：
   - 在每位員工的筆記型電腦（運行 Windows 10/11 Pro 或 Enterprise）上，前往 **設定 > 系統 > 關於 > 加入網域**（或在執行對話框中輸入 `sysdm.cpl`）。
   - 輸入網域名稱並提供網域管理員憑證以加入。
   - 重新啟動筆記型電腦。一旦加入，筆記型電腦將針對 AD 進行身份驗證，而不是使用本機帳戶，從而實現網域範圍的管理。

3. **建立和組織使用者帳戶**：
   - 在網域控制站上使用 **Active Directory Users and Computers** (dsa.msc) 為員工建立使用者帳戶。
   - 將使用者分配到**安全性群組**（例如「銷售團隊」或「遠端工作者」）以便更輕鬆地管理權限。透過使用者內容中的「隸屬於」標籤新增群組。

4. **套用群組原則進行存取控制**：
   - 使用**群組原則物件 (GPO)** — AD 的原則引擎 — 在已加入網域的筆記型電腦上強制執行設定。
     - 在網域控制站上開啟 **Group Policy Management** (gpmc.msc)。
     - 建立新的 GPO（例如「筆記型電腦使用者限制」）並將其連結到包含筆記型電腦的組織單位 (OU)（在 AD 中建立 OU，例如「員工筆記型電腦」，以對設備進行分組）。
     - 要設定的常見原則：
       - **使用者權限**：在 電腦設定 > 原則 > Windows 設定 > 安全性設定 > 本機原則 > 使用者權限指派 下，從標準使用者中移除「Administrators」，以防止本機管理員權限提升。
       - **軟體限制**：透過軟體限制原則封鎖未經授權的應用程式安裝。
       - **資料夾/印表機存取**：根據群組成員資格授予 NTFS/共享權限（例如，銷售群組對共享磁碟機具有讀取/寫入權限）。
       - **遠端存取**：為離線網路筆記型電腦設定 VPN 或條件式存取。
     - 套用 GPO — 它會自動傳播（或在筆記型電腦上使用 `gpupdate /force` 強制執行）。
   - 對於進階控制，可透過 Windows Admin Center 整合**基於角色的存取控制 (RBAC)**：
     - 在伺服器上安裝 Windows Admin Center。
     - 在筆記型電腦上啟用 RBAC（安裝 Just Enough Administration 端點）。
     - 將 AD 群組指派給角色，例如「Administrators」（完全存取）或「Readers」（唯讀）。

5. **監控和維護**：
   - 使用 Event Viewer 或 PowerShell（例如 `Get-ADUser` 或 `Get-GPResultantSetOfPolicy`）等工具稽核存取情況。
   - 對於自動化，可以使用 PowerShell 編寫批次變更的指令碼（例如，將使用者新增至群組）。
   - 如果使用混合設定（例如與 Microsoft Entra ID），請同步 AD 以用於雲端原則，例如多重要素驗證。

此設定確保員工使用 AD 憑證登入，繼承基於群組的權限，並且無法繞過限制 — 非常適合合規性和安全性。從一個測試 OU 開始小規模實施，以避免中斷。

[Active Directory Domain Services 概述](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)  
[設定使用者存取控制和權限](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/configure/user-access-control)  
[Windows Server 的群組原則概述](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)