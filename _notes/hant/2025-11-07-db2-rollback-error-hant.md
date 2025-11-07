---
audio: false
generated: true
image: false
lang: hant
layout: post
model: moonshotai/kimi-k2-thinking
title: DB2 交易回滾與錯誤檢測
translated: true
---

## 當 DB2 因系統錯誤執行回滾時

IBM DB2 在遇到威脅資料完整性的關鍵系統錯誤時會自動回滾交易。常見情況包括：

- **死結或逾時**：SQLCODE -911 且 SQLSTATE 40001，原因碼「2」表示交易因死結而被回滾
- **程序異常終止**：在所有 DB2 環境中，程序終止會觸發隱式回滾
- **系統資源故障**：記憶體、磁碟或網路故障導致交易無法完成
- **時間戳記衝突**：當模組與 DBRM 之間的內部時間戳記不匹配時會發生 SQLCODE -818
- **連線池安全機制**：某些實作在釋放連線時會自動回滾，以防止未提交的交易導致鎖定問題

## 如何偵測詳細錯誤資訊

### 1. 主要錯誤偵測機制

**SQLCODE 和 SQLSTATE**
每個 SQL 語句執行後，DB2 會設定這些變數：

```sql
-- 在語句執行後立即檢查
IF SQLCODE < 0 THEN
    -- 發生錯誤
    ROLLBACK;
END IF;
```

SQLSTATE 類別碼專門識別錯誤類型：
- **類別 58**：系統錯誤（例如資源不可用、操作員介入）
- **類別 40**：交易回滾
- **類別 25**：無效交易狀態

**GET DIAGNOSTICS 語句**
用於在 SQL PL 預存程序中取得詳細錯誤資訊：

```sql
DECLARE v_sqlcode INTEGER;
DECLARE v_sqlstate CHAR(5);
DECLARE v_sqlmessage VARCHAR(256);

GET DIAGNOSTICS CONDITION 1
    v_sqlcode = DB2_RETURNED_SQLCODE,
    v_sqlstate = RETURNED_SQLSTATE,
    v_sqlmessage = MESSAGE_TEXT;
```

### 2. 命令列錯誤偵測

透過 `db2` 命令列執行指令碼時，檢查結束代碼：

- **結束代碼 8**：系統錯誤
- **結束代碼 4**：DB2 錯誤（限制違反、物件找不到）
- **結束代碼 2**：DB2 警告
- **結束代碼 1**：找不到列

**建議的指令碼模式**：
```bash
db2 -l migration.log +c -stf migration.sql
if [ $? -ge 4 ]; then
    db2 rollback
    tail -10 migration.log  # 檢視詳細錯誤
else
    db2 commit
fi
```

### 3. 預存程序錯誤處理

在 SQL PL 中進行全面錯誤偵測，使用宣告的處理程序：

```sql
CREATE PROCEDURE my_procedure()
BEGIN
    DECLARE v_sqlcode INTEGER DEFAULT 0;
    DECLARE v_sqlstate CHAR(5) DEFAULT '00000';
    DECLARE v_error_message VARCHAR(256);
    
    -- 宣告任何異常的退出處理程序
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1
            v_sqlcode = DB2_RETURNED_SQLCODE,
            v_sqlstate = RETURNED_SQLSTATE,
            v_error_message = MESSAGE_TEXT;
            
        -- 將錯誤詳細資訊記錄到資料表或檔案
        INSERT INTO error_log (sqlcode, sqlstate, message, timestamp)
        VALUES (v_sqlcode, v_sqlstate, v_error_message, CURRENT_TIMESTAMP);
        
        ROLLBACK;
    END;
    
    -- 您的交易邏輯在此
    UPDATE employee SET salary = salary + 1000 WHERE job = 'MANAGER';
    INSERT INTO audit_log VALUES (CURRENT_TIMESTAMP, 'Salary update');
    
    COMMIT;
END
```

### 4. DB2 診斷記錄檔

對於系統層級錯誤，請務必檢查：

- **db2diag.log**：主要診斷記錄檔，包含詳細的系統錯誤資訊
- **通知記錄檔**：包含錯誤摘要
- **命令列記錄檔**：使用 `-l logfile.txt` 選項來擷取錯誤

## 錯誤偵測的最佳實踐

1. **在關鍵操作後立即檢查 SQLCODE/SQLSTATE**
2. **在預存程序中使用 GET DIAGNOSTICS** 以取得豐富的錯誤上下文
3. **實作交易回滾百分比監控** - 超過 1% 即需調查
4. **啟用指令執行的命令選項**：
   ```bash
   db2 +c -s -v -l error.log -f script.sql
   ```
   其中 `+c` 停用自動提交，`-s` 在錯誤時停止
5. **在複雜交易中使用儲存點** 進行部分回滾
6. **在回滾前將錯誤詳細資訊記錄** 到持久化資料表，以保留診斷資訊

## 需監控的關鍵系統錯誤 SQLSTATE

| SQLSTATE | 描述 | 處理動作 |
|----------|-------------|--------|
| **58004** | 系統錯誤（各種原因） | 立即檢查 db2diag.log |
| **58008** | 通訊錯誤 | 驗證網路/連線 |
| **HY000** | 一般驅動程式錯誤 | 檢查 ODBC/JDBC 驅動程式記錄檔 |
| **40001** | 死結/逾時 | 使用退避機制重試交易 |

在生產環境中，監控工具應對 **SQLCODE < 0** 和 **類別 58 SQLSTATE** 發出警報，以便在系統層級問題級聯之前主動偵測。