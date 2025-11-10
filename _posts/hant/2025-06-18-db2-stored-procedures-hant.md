---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用參數呼叫 DB2 預存程序
translated: true
type: note
---

### 假設與背景
您的查詢似乎涉及在 IBM 資料庫系統（例如 IBM DB2，運行於 Linux/Unix/Windows、z/OS 或 iSeries）中呼叫*預存程序*（可能為 "store procedure" 的筆誤）。預存程序是儲存在資料庫中的可執行腳本，能夠接受輸入參數、執行操作並回傳輸出或結果。確切語法取決於程式語言和 IBM 環境（例如 SQL、COBOL、RPG 或透過 JDBC 的 Java）。我將聚焦於最常見的情況：DB2 中基於 SQL 的 CALL 語句，因為這是關聯式資料庫的標準做法。

如果您使用的是其他 IBM 平台（例如 IBM i CL 指令、MQ 或 Watson Query），請提供更多細節以獲得針對性的建議。

### 如何在 DB2 預存程序呼叫中傳遞參數
在 DB2 中，預存程序使用 SQL 的 `CALL` 語句進行呼叫。參數以逗號分隔的清單形式置於括號內傳遞，並需與程序的定義相符（例如，IN 表示輸入，OUT 表示輸出，INOUT 表示兩者兼有）。

#### 逐步指南
1. **定義或了解程序簽章**：確保您知道程序的名稱和參數。例如，一個程序可能定義如下：
   ```sql
   CREATE PROCEDURE update_employee (IN emp_id INT, IN new_salary DECIMAL(10,2), OUT status_msg VARCHAR(100))
   ```
   - 此處，`emp_id` 為輸入（IN），`new_salary` 為輸入，`status_msg` 為輸出（OUT）。

2. **使用 CALL 語句**：在 SQL 環境中（例如 DB2 命令列處理器，或嵌入於如 Java 等程式中），如下呼叫程序：
   ```sql
   CALL update_employee(12345, 75000.00, ?);
   ```
   - `?` 是 OUT 參數的佔位符。在程式化呼叫中，需使用結果集或主變數來處理輸出。
   - 輸入以字面值或變數形式傳遞；輸出透過佔位符或綁定變數捕獲。

3. **處理參數類型**：
   - **IN 參數**：直接傳遞值（例如，數字、引號內的字符串）。
   - **OUT/INOUT 參數**：在 CALL 中使用 `?`，然後在程式碼中綁定它們以在執行後檢索值。
   - 嚴格匹配順序和類型；不匹配會導致錯誤（例如，無效參數的 SQLCODE -440）。

4. **程式碼範例**：
   - **透過 DB2 CLP（命令列）**：直接執行 SQL。
     ```sql
     CALL my_proc('input_value', ?);
     ```
     使用 `FETCH FIRST FROM` 或在腳本中檢索 OUT 參數。
   - **透過 JDBC (Java)**：
     ```java
     CallableStatement stmt = conn.prepareCall("{CALL update_employee(?, ?, ?)}");
     stmt.setInt(1, 12345);          // IN 參數
     stmt.setBigDecimal(2, new java.math.BigDecimal("75000.00")); // IN 參數
     stmt.registerOutParameter(3, Types.VARCHAR); // OUT 參數
     stmt.execute();
     String status = stmt.getString(3); // 檢索 OUT 參數
     ```
   - **在 IBM i 上透過 RPG**：使用 `CALLP` 並宣告與參數類型匹配的變數。
     ```rpg
     D PROC_PARAM    S                   LIKE(PARAM_TYPE)
     PROC_PARAM = 'value';
     CALLP MY_PROC(PROC_PARAM);
     ```
   - **錯誤處理**：呼叫後檢查 SQLSTATE 或 SQLCODE；例如，'00000' 表示成功。

#### 關鍵提示與證據
- **來自 DB2 文件的證據**：根據 IBM 官方的 DB2 SQL 參考（例如 LUW v11.5 或 z/OS），`CALL` 語句定義為可選參數清單。例如，語法為：`CALL procedure-name [(parameter [, parameter] ...)]`。這符合關聯式資料庫的行業標準，並在 DB2 變體中得到支援以確保一致性（參見 IBM Knowledge Center）。
- **變體**：在 IBM i (AS400) 中，程序可能使用 CL（命令語言）呼叫，如 `CALL PGM(MYPROC) PARM('value')` 用於 RPG 程式。對於大型主機 COBOL，則使用主變數嵌入 `EXEC SQL CALL...`。
- **測試**：在呼叫前使用 `db2 describe routine procedure_name` 檢查參數。
- **限制**：大量參數集可能需要陣列或結果集；複雜類型需要特定處理。

如果這與您的設定不符（例如，如果是 IBM Watson 或其他工具），請分享更多背景資訊（如平台或語言）以獲得精確指示。