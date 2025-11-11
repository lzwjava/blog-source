---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast:free
title: DB2 SQLCODE -551 缺少 SELECT 權限
translated: true
type: note
---

### IBM DB2 SQLCODE -551：授權失敗（缺少 SELECT 權限）

**含義**：SQLCODE -551 是 IBM DB2 中的授權錯誤，表示當前用戶或應用程式缺乏對一個或多個資料庫物件執行指定操作所需的權限。在您的情況中，「缺少 SELECT 權限」突顯了用戶無法查詢（讀取）目標資料表、視圖或資料庫物件。

**常見原因**：
- 用戶未被授予該物件的 SELECT 權限（例如透過 `GRANT SELECT ON table_name TO user_name`）。
- 使用了權限受限或權限不足的共享連線。
- 嘗試在沒有適當權限的情況下查詢系統物件或受限視圖。
- 隱含權限問題（例如透過未包含 SELECT 權限的角色或群組）。

**診斷方法**：
- 在日誌或透過 `db2 diag`/`db2 ? SQLCODE -551` 檢查完整錯誤訊息，以了解受影響的具體物件。
- 使用 DB2 指令（如 `db2 "GET AUTHORIZATIONS"`）或查詢 syscat 資料表（例如 SYSCAT.TABAUTH 用於資料表權限）來驗證用戶權限。

**解決步驟**：
1. **授予權限**：管理員應執行 `GRANT SELECT ON object_name TO user_name [WITH GRANT OPTION]`（請替換為實際物件和用戶名稱）。
2. **檢查角色/群組**：確保用戶屬於具有 SELECT 存取權限的群組或角色。
3. **使用提升權限測試**：如果使用 DB2 CLP，請以權限較高的用戶身份連線（例如 DBADM）。
4. **檢視安全政策**：參考 DB2 安全文件（IBM Knowledge Center）以了解基於角色的存取控制（RBAC）配置。
5. 若問題持續存在，請重啟 DB2 或稽核連線設定。

此錯誤優先考慮安全性，防止未經授權的資料存取。若為複雜設定，請升級至您的 DBA 處理。參考：IBM DB2 SQL 訊息與代碼手冊。