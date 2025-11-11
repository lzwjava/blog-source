---
audio: false
generated: true
lang: ja
layout: post
title: 取引テーブル
translated: true
type: note
---

銀行システムにおける**取引テーブル**は、通常、銀行が処理するすべての金融取引の詳細を保存します。このテーブルは、顧客取引の追跡、口座の照合、規制遵守を確保するために不可欠です。

---

### **銀行取引テーブルの主要フィールド**

| **フィールド名**           | **データ型** | **説明** |
|--------------------------|--------------|----------------|
| **Transaction_ID**       | `VARCHAR` / `BIGINT` | 各取引の一意識別子 |
| **Account_Number**       | `VARCHAR` / `BIGINT` | 取引に関与する顧客の銀行口座番号 |
| **Transaction_Type**     | `VARCHAR` | 取引の種類 (例: DEPOSIT, WITHDRAWAL, TRANSFER, PAYMENT) |
| **Transaction_Amount**   | `DECIMAL(15,2)` | 取引に関与する金額 |
| **Currency_Code**        | `VARCHAR(3)` | 取引の通貨 (例: USD, EUR, INR) |
| **Transaction_Date**     | `DATETIME` | 取引が発生したタイムスタンプ |
| **Value_Date**           | `DATETIME` | 取引が決済または処理された日付 |
| **Debit_Credit_Flag**    | `CHAR(1)` | 取引が**借方 ('D')** か**貸方 ('C')** かを示すインジケーター |
| **Counterparty_Account** | `VARCHAR` | 相手先の口座番号 (該当する場合) |
| **Transaction_Mode**     | `VARCHAR` | 支払方法 (SWIFT, RTGS, NEFT, ACH, UPI, Card, Wallet など) |
| **Transaction_Status**   | `VARCHAR` | 取引のステータス (PENDING, SUCCESS, FAILED, REVERSED) |
| **Reference_Number**     | `VARCHAR` | 外部システム用の一意識別子 (例: SWIFT Reference, UTR, UPI Transaction ID) |
| **Transaction_Description** | `TEXT` | 取引に関する追加詳細 (例: 「Bill Payment - Electricity」、「Salary Credit」) |
| **Branch_Code**          | `VARCHAR(10)` | 取引を処理する銀行支店の識別子 |
| **Transaction_Fee**      | `DECIMAL(10,2)` | 取引に対して控除された手数料 |
| **Exchange_Rate**        | `DECIMAL(10,6)` | 通貨変換が関与する場合に適用される為替レート |
| **Initiating_Channel**   | `VARCHAR` | 取引に使用されたチャネル (ATM, Mobile Banking, Internet Banking, POS, Teller) |
| **Fraud_Check_Status**   | `VARCHAR` | 不正検出のステータス (例: PASSED, FLAGGED, UNDER REVIEW) |
| **Reversal_Transaction_ID** | `VARCHAR` | 取り消された場合、元の取引IDへのリンク |

---

### **取引レコードの例**

| Transaction_ID | Account_Number | Type      | Amount  | Currency | Date                 | Debit/Credit | Counterparty | Mode   | Status  |
|---------------|---------------|-----------|---------|----------|----------------------|--------------|--------------|--------|---------|
| 100001       | 123456789012   | DEPOSIT   | 1000.00 | USD      | 2025-03-25 10:15:00 | C            | -            | ATM    | SUCCESS |
| 100002       | 123456789012   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | D            | 987654321098 | SWIFT  | SUCCESS |
| 100003       | 987654321098   | TRANSFER  | 500.00  | USD      | 2025-03-25 12:30:00 | C            | 123456789012 | SWIFT  | SUCCESS |
| 100004       | 123456789012   | PAYMENT   | 50.00   | USD      | 2025-03-25 14:00:00 | D            | Utility Co.  | ACH    | PENDING |

---

### **銀行業務におけるこれらのフィールドの使用方法**
1.  **取引追跡:** すべての取引には一意のIDがあり、そのステータスを通じて追跡できます。
2.  **口座照合:** 借方と貸方を照合し、正確な財務記録を維持するのに役立ちます。
3.  **不正検出:** 不正チェックステータスと取引パターンの監視を使用して、不審な取引にフラグを立てることができます。
4.  **規制報告:** 金融規制 (AML, KYC, Basel III) へのコンプライアンスを確保します。
5.  **カスタマーサービス:** 銀行が失敗または保留中の取引に関する紛争や問い合わせを解決するのに役立ちます。

SQLクエリを含むより詳細なスキーマについて知りたいですか？ 🚀