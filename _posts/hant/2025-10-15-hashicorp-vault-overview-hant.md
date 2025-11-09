---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: HashiCorp Vault 概覽
translated: true
type: note
---

### 什麼是 HashiCorp Vault？

HashiCorp Vault 是一款開源工具，專為安全地管理、儲存及存取敏感資料（通常稱為「機密」）而設計。這些機密包括 API 金鑰、密碼、憑證、令牌及加密金鑰。它作為一個基於身份識別的集中式機密管理系統，提供加密服務與特權存取控制，協助企業在動態、多雲或混合環境中保護敏感資訊。

#### 主要功能
- **機密管理**：Vault 能處理靜態機密（如長期有效的密碼）與動態機密（按需生成的短期憑證，例如會自動過期的資料庫使用者）。
- **加密與審計**：所有資料在靜態儲存與傳輸過程中皆經過加密，並提供完整的日誌記錄與審計功能以追蹤存取與變更。
- **基於身份的存取**：可與身份供應商（如 LDAP、OIDC）整合，對使用者與系統進行身份驗證，並實施精細化的存取策略控制。
- **動態憑證與租期機制**：機密設有有效期限，降低長期暴露的風險。
- **雲端無關與自託管**：適用於任何基礎架構，支援本地部署或託管服務選項。

#### 運作原理
Vault 以客戶端-伺服器模式運作。客戶端（應用程式或使用者）向 Vault 伺服器進行身份驗證，伺服器根據策略對請求進行授權。一旦核准，Vault 可擷取儲存的機密、生成新機密或撤銷存取權限。例如，應用程式可請求臨時資料庫憑證，使用後讓其自動失效。其架構包含用於資料持久化的儲存後端（如 Consul、PostgreSQL），並透過集群支援高可用性。

此工具廣泛應用於 DevOps、安全性與合規場景，取代手動處理機密的方式，在低信任度環境中降低外洩風險。

#### 參考資料
- [什麼是 Vault？ | Vault - HashiCorp Developer](https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault)
- [HashiCorp Vault | 基於身份識別的機密管理](https://www.hashicorp.com/en/products/vault)
- [hashicorp/vault：用於機密管理、加密的工具... - GitHub](https://github.com/hashicorp/vault)
- [什麼是 HashiCorp Vault 及其運作原理？ - KodeKloud](https://kodekloud.com/blog/what-is-hashicorp-vault/)