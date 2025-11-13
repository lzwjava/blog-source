---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 基於角色的存取控制在 Jenkins
translated: true
type: note
---

### 企業級 Jenkins（CloudBees CI）中的基於角色的存取控制（RBAC）

企業級 Jenkins（由 CloudBees CI 提供支援）使用 CloudBees 基於角色的存取控制（RBAC）外掛來實現細粒度的基於角色的權限管理。這允許管理員定義自訂角色、將其分配給使用者或群組，並在全局、資料夾或任務層級控制存取。它與 Folders 外掛整合，實現基於團隊的隔離，並支援外部身份供應商（如 LDAP 或 Active Directory）進行群組管理。權限會從分配給使用者群組的所有角色中匯總，並且除非被固定或過濾，否則可以傳播到子物件（例如子資料夾）。

RBAC 取代或增強了 Jenkins 內建的基於矩陣的授權機制，實現無需完整系統存取權限的管理委派。其配置位於 **管理 Jenkins > 管理安全性 > 授權**，在此處您需選擇「基於角色的矩陣授權策略」。

#### 關鍵權限與存取權利
權限定義了使用者可以在 Jenkins 物件（例如任務、資料夾、代理、視圖）上執行的原子操作。企業級 Jenkins 包含核心 Jenkins 權限以及外掛擴展的權限。權限具有層次結構——某些權限隱含了其他權限（例如 `Job/Configure` 隱含 `Job/Read`）。

以下是常見權限類別及範例的表格，重點關注建置/讀取權限：

| 類別          | 權限範例                                                                 | 描述 |
|-------------------|-----------------------------------------------------------------------------------------|-------------|
| **讀取/唯讀** | - `Overall/Read`<br>- `Job/Read`<br>- `View/Read`<br>- `Agent/Read`                     | 授予檢視配置、建置、日誌和產出物的存取權限，但無法修改。適用於稽核人員或檢視者。擴展讀取權限外掛增加了細粒度的讀取控制（例如，無需建置權限即可檢視工作區）。 |
| **建置/執行** | - `Job/Build`<br>- `Job/Cancel`<br>- `Job/Workspace`<br>- `Job/Read`                    | 允許啟動、停止或存取建置輸出。可以限定於特定任務/資料夾。 |
| **配置/修改** | - `Job/Configure`<br>- `Job/Create`<br>- `Job/Delete`<br>- `Folder/Configure`            | 允許編輯任務參數、新增觸發器或管理子項目。 |
| **管理** | - `Overall/Administer`<br>- `Overall/Configure`<br>- `Group/Manage`<br>- `Role/View`     | 完整的系統控制或委派任務，例如管理角色/群組。`Overall/Administer` 是超級使用者權限。 |
| **其他**         | - `SCM/Tag`<br>- `Credentials/View`<br>- `Agent/Launch`<br>- `RunScripts`                | SCM 操作、憑證存取、節點管理或指令碼執行。否定權限（例如 `-Job/Build`）可以限制繼承的權利。 |

存取權利在多個範圍內受到控制：
- **全局**：適用於整個實例（例如，透過根層級群組）。
- **物件特定**：在任務、資料夾或代理上覆寫（例如，團隊只能在其資料夾內進行建置）。
- **傳播**：角色會自動繼承到子物件，除非被「固定」（本地覆寫）或過濾（例如，對某個角色隱藏專案）。
- **隱含關係**：某些權限會自動授予下屬權限（在近期版本中可配置以增強安全性）。

管理員可以過濾角色以防止傳播（例如，透過任務上的 **Roles > Filter**），或使用不可過濾的角色來強制實施全局存取。

#### 管理使用者角色
角色是預先定義的權限集合：
1. 前往 **管理 Jenkins > 管理角色**。
2. 點擊 **新增角色** 並為其命名（例如「Developer」）。
3. 透過勾選方框分配權限（使用「全選」或「全部清除」進行批量操作）。系統角色如「anonymous」（用於未驗證使用者）和「authenticated」（已登入使用者）是預先建置的且無法刪除。
4. 儲存。角色可以標記為「不可過濾」，以始終全局應用。

使用者從分配給其群組的角色繼承權限——沒有直接的使用者-角色分配；基於群組的設計是為了可擴展性。

#### 將角色分配給群組和使用者
群組將使用者和角色捆綁在一起，便於委派：
1. 在物件上（例如根目錄、資料夾或任務），前往 **Groups > New Group**。
2. 輸入群組名稱（例如「DevTeam」）。
3. 透過勾選來分配角色（預設情況下會傳播到子項；取消勾選以在本地固定）。
4. 新增成員（見下文）。
5. 儲存。

群組支援嵌套（例如子群組）和外部整合（例如 LDAP 群組）。

#### 管理員如何將使用者新增至群組
擁有 `Group/Manage` 權限的管理員可以編輯成員資格：
1. 導航至群組的配置（例如，根目錄或物件上的 **Groups**）。
2. 在「Members」部分，點擊 **Add user**（或 **Add group** 用於外部/嵌套群組）。
3. 輸入使用者 ID（例如，來自 Jenkins 使用者資料庫的使用者名稱、LDAP DN 或外部群組名稱）。使用 `/whoAmI` 來驗證 ID。
4. 點擊 **Add** 並儲存。如果需要，系統會提示確認移除。
5. 對於批量/自動化操作：
   - 使用 CLI：`java -jar jenkins-cli.jar group-membership <object-path> <group-name> <user-id>`（列出/設定成員）。
   - REST API：POST 到 `/rbac/api/v1/groups/<group>/members` 並附上 JSON 負載。

避免循環群組成員資格以防止迴圈。對於外部領域（例如 Active Directory），請先在 **管理安全性 > 安全領域** 下配置安全領域。

此設定確保了安全、可擴展的控制——例如，開發人員在其資料夾中獲得 `Job/Build` + `Job/Read` 權限，而管理員則處理所有事務。

[使用基於角色的存取控制來限制存取並委派管理權限](https://docs.cloudbees.com/docs/cloudbees-ci/latest/secure/rbac)