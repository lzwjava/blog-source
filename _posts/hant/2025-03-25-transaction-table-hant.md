---
audio: false
generated: true
lang: hant
layout: post
title: 交易表格
translated: true
type: note
---

銀行系統中的**交易表格**通常儲存銀行處理的所有金融交易詳情。這張表格對於追蹤客戶交易、核對帳戶及確保合規性至關重要。

---

### **銀行交易表格關鍵欄位**

| **欄位名稱**               | **資料類型**     | **描述** |
|---------------------------|------------------|----------|
| **Transaction_ID**        | `VARCHAR` / `BIGINT` | 每筆交易的唯一識別碼 |
| **Account_Number**        | `VARCHAR` / `BIGINT` | 交易涉及的客戶銀行帳戶號碼 |
| **Transaction_Type**      | `VARCHAR` | 交易類型（例如：DEPOSIT、WITHDRAWAL、TRANSFER、PAYMENT） |
| **Transaction_Amount**    | `DECIMAL(15,2)` | 交易涉及的金額 |
| **Currency_Code**         | `VARCHAR(3)` | 交易幣種（例如：USD、EUR、INR） |
| **Transaction_Date**      | `DATETIME` | 交易發生的時間戳記 |
| **Value_Date**            | `DATETIME` | 交易結算或處理的日期 |
| **Debit_Credit_Flag**     | `CHAR(1)` | 交易類型標示：**借方 ('D')** 或 **貸方 ('C')** |
| **Counterparty_Account**  | `VARCHAR` | 目標帳戶號碼（如適用） |
| **Transaction_Mode**      | `VARCHAR` | 支付方式（SWIFT、RTGS、NEFT、ACH、UPI、Card、Wallet 等） |
| **Transaction_Status**    | `VARCHAR` | 交易狀態（PENDING、SUCCESS、FAILED、REVERSED） |
| **Reference_Number**      | `VARCHAR` | 外部系統唯一識別碼（例如：SWIFT Reference、UTR、UPI Transaction ID） |
| **Transaction_Description** | `TEXT` | 交易補充說明（例如：「Bill Payment - Electricity」、「Salary Credit」） |
| **Branch_Code**           | `VARCHAR(10)` | 處理交易的銀行分行代碼 |
| **Transaction_Fee**       | `DECIMAL(10,2)` | 交易產生的手續費 |
| **Exchange_Rate**         | `DECIMAL(10,6)` | 涉及貨幣兌換時適用的匯率 |
| **Initiating_Channel**    | `VARCHAR` | 交易發起渠道（ATM、Mobile Banking、Internet Banking、POS、Teller） |
| **Fraud_Check_Status**    | `VARCHAR` | 欺詐檢測狀態（例如：PASSED、FLAGGED、UNDER REVIEW） |
| **Reversal_Transaction_ID** | `VARCHAR` | 若交易被撤銷，連結至原始交易ID |

---

### **交易記錄範例**

| Transaction_ID | Account_Number | Type      | Amount  | Currency | Date                 | Debit/Credit | Counterparty | Mode   | Status  |
|---------------|---------------|-----------|---------|----------|----------------------|--------------|--------------|--------|---------|
| 100001       | 123456789012   | DEPOSIT   | 1000.00 | USD      | 2025-03-25 10:15:00 | C            | -            | ATM    | SUCCESS |
| 100002       | 123456789012   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | D            | 987654321098 | SWIFT  | SUCCESS |
| 100003       | 987654321098   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | C            | 123456789012 | SWIFT  | SUCCESS |
| 100004       | 123456789012   | PAYMENT   | 50.00   | USD      | 2025-03-25 14:00:00 | D            | Utility Co.  | ACH    | PENDING |

---

### **銀行如何運用這些欄位**
1. **交易追蹤：** 每筆交易皆具唯一ID，可透過狀態進行追蹤
2. **帳戶核對：** 協助匹配借貸記錄以確保財務記錄準確性
3. **欺詐檢測：** 透過欺詐檢查狀態與監控交易模式標記可疑交易
4. **監管申報：** 確保符合金融監管要求（AML、KYC、Basel III）
5. **客戶服務：** 協助銀行處理有關失敗或待處理交易的爭議與查詢

需要包含 SQL 查詢的詳細結構說明嗎？🚀