---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: AWS IAM 存取管理指南
translated: true
type: note
---

AWS Identity and Access Management (IAM) 是一項免費服務，可協助您安全地控制對 AWS 資源的存取。它讓您能夠管理使用者及其權限，確保合適的人員和應用程式擁有對應資源的適當存取權。IAM 負責處理身份驗證（誰可以登入）和授權（他們可以執行哪些操作）。

## IAM 的核心組件

- **使用者**：代表需要存取 AWS 的個人或應用程式。每位使用者都擁有獨特的安全憑證（例如密碼或存取金鑰）。
- **群組**：使用者的集合，以便更輕鬆地管理權限。權限會附加到群組，而非直接附加到個別使用者。
- **角色**：具有權限的臨時身份，可供使用者、服務或應用程式擔任。角色沒有永久憑證；它們提供短期的安全令牌。
- **政策**：定義權限的 JSON 文件。它們指定操作（例如讀取、寫入）、資源（例如 S3 儲存貯體）和條件（例如 IP 限制）。政策分為 AWS 託管、客戶託管和內嵌政策。

## 入門指南：逐步教學

### 先決條件
- 以根使用者身份（您的帳戶電郵和密碼）登入 AWS Management Console。**重要**：避免在日常工作中使用根使用者 — 請立即建立管理員使用者。
- 為根使用者啟用多重要素驗證 (MFA) 以增強安全性。

### 1. 建立 IAM 使用者
為求簡便，請使用 AWS Management Console（也可使用 CLI 或 API 選項進行自動化）。

1. 在 https://console.aws.amazon.com/iam/ 開啟 IAM 主控台。
2. 在導覽窗格中，選擇 **Users** > **Create user**。
3. 輸入使用者名稱（例如 "admin-user"）並選擇 **Next**。
4. 在 **Set permissions** 下，選擇 **Attach policies directly** 並選擇一個 AWS 託管政策，例如 "AdministratorAccess" 以獲得完整存取權限（在生產環境中應從最小權限開始）。
5. （可選）設定主控台密碼：選擇 **Custom password** 並啟用 **Require password reset**。
6. 檢視並選擇 **Create user**。
7. 向使用者提供其登入網址（例如 https://[account-alias].signin.aws.amazon.com/console）、使用者名稱和臨時密碼。

若需程式設計存取，請產生存取金鑰（但建議應用程式優先使用角色）。

### 2. 建立和管理群組
群組可簡化權限的擴展。

1. 在 IAM 主控台中，選擇 **User groups** > **Create group**。
2. 輸入群組名稱（例如 "Developers"）。
3. 附加政策（例如 "AmazonEC2ReadOnlyAccess"）。
4. 選擇 **Create group**。
5. 若要新增使用者：選擇該群組 > **Add users to group** > 選擇現有使用者。

使用者會繼承所有群組權限。一個使用者可以屬於多個群組。

### 3. 建立和附加政策
政策定義允許哪些操作。

- **類型**：
  - AWS 託管：為常見工作預先建立（例如 "ReadOnlyAccess"）。
  - 客戶託管：根據您的需求自訂 JSON。
  - 內嵌：直接嵌入到使用者/群組/角色中（請謹慎使用）。

建立自訂政策：
1. 在 IAM 主控台中，選擇 **Policies** > **Create policy**。
2. 使用視覺化編輯器或 JSON 標籤（例如，允許在特定儲存貯體上執行 "s3:GetObject"）。
3. 為其命名並選擇 **Create policy**。
4. 透過 **Attach policy** 將其附加到使用者/群組/角色。

最佳實踐：授予最小權限 — 從寬鬆開始，然後使用 IAM Access Analyzer 等工具進行細化。

### 4. 使用 IAM 角色
角色非常適合臨時存取，可避免使用長期憑證。

1. 在 IAM 主控台中，選擇 **Roles** > **Create role**。
2. 選擇受信任的實體（例如，用於 EC2 的 "AWS service"，或用於跨帳戶存取的 "Another AWS account"）。
3. 附加權限政策。
4. 新增信任政策（定義誰可以擔任該角色的 JSON，例如 EC2 服務主體）。
5. 為其命名並選擇 **Create role**。

**常見情境**：
- **EC2 執行個體**：將角色附加到執行個體，以便安全存取其他服務（例如 S3），而無需嵌入金鑰。
- **跨帳戶存取**：在帳戶 A（信任方）中建立一個角色，其信任政策允許來自帳戶 B 的主體。B 帳戶中的使用者透過 AWS STS 擔任該角色以存取 A 的資源。

透過主控台、CLI (`aws sts assume-role`) 或 SDK 擔任角色以取得臨時憑證。

### 5. 啟用 MFA 和其他安全措施
- 對於使用者：在 IAM 主控台 > Users > 選擇使用者 > **Security credentials** > Manage MFA。
- 使用虛擬（基於應用程式）或硬體 MFA 裝置。

## 安全最佳實踐
- **鎖定根使用者**：僅在需要時使用（例如變更帳戶設定）。啟用 MFA 且不要建立存取金鑰。
- **使用臨時憑證**：優先使用聯合身份驗證（例如透過 IAM Identity Center）和角色，而非長期金鑰。若使用金鑰，請定期輪換。
- **最小權限原則**：授予最小權限；在政策中使用條件（例如時間/IP 限制）。
- **監控和稽核**：啟用 AWS CloudTrail，使用 IAM Access Analyzer 偵測未使用的權限或非預期存取，並檢視最後使用資訊。
- **移除未使用的資源**：定期刪除非活躍的使用者/角色/政策。
- **對於多帳戶**：使用 AWS Organizations 並搭配服務控制政策 (SCP) 作為防護機制。
- **驗證政策**：在應用前使用 IAM Access Analyzer 的政策檢查功能。

如需動手學習，請在主控台或文件中探索 IAM 教學課程，例如基於屬性的存取控制 (ABAC) 等情境。

## 參考資料
- [什麼是 IAM？](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
- [建立 IAM 使用者](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [IAM 群組](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html)
- [IAM 角色](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [IAM 最佳實踐](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM 教學課程](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorials.html)