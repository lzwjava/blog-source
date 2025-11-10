---
audio: false
generated: true
lang: hant
layout: post
title: Java SQL 語句類型比較
translated: true
type: note
---

在 Java 的 `java.sql` 套件中，`Statement`、`PreparedStatement` 和 `CallableStatement` 都是用於執行 SQL 查詢的介面，但它們各有不同的用途和特性。以下是簡明比較：

1. **Statement**：
   - **用途**：用於執行不帶參數的靜態 SQL 查詢。
   - **運作方式**：將完整的 SQL 查詢以字串形式傳遞給 `executeQuery()` 或 `executeUpdate()` 方法。
   - **主要特性**：
     - 適用於簡單的一次性查詢。
     - 無參數綁定功能，需手動將數值串接到 SQL 字串中，可能導致 SQL 注入風險。
     - 重複查詢時效率較低，因為資料庫每次都需要重新解析 SQL。
   - **範例**：
     ```java
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = 1");
     ```

2. **PreparedStatement**：
   - **用途**：用於預編譯的參數化 SQL 查詢。
   - **運作方式**：使用佔位符 (`?`) 定義查詢，並透過 `setInt()`、`setString()` 等方法設定參數值。
   - **主要特性**：
     - 透過分離 SQL 邏輯與資料來防止 SQL 注入。
     - 重複查詢時效率更高，因為 SQL 只需編譯一次即可重複使用。
     - 支援動態參數綁定，更安全且靈活。
   - **範例**：
     ```java
     PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     pstmt.setInt(1, 1);
     ResultSet rs = pstmt.executeQuery();
     ```

3. **CallableStatement**：
   - **用途**：用於執行資料庫中的預存程序。
   - **運作方式**：繼承 `PreparedStatement` 以處理預存程序呼叫，支援輸入 (`IN`)、輸出 (`OUT`) 及輸入輸出 (`IN OUT`) 參數。
   - **主要特性**：
     - 專為資料庫預存程序設計。
     - 允許使用 `registerOutParameter()` 等方法註冊輸出參數。
     - 支援處理預存程序中的複雜參數邏輯。
   - **範例**：
     ```java
     CallableStatement cstmt = conn.prepareCall("{call getUserName(?, ?)}");
     cstmt.setInt(1, 1);
     cstmt.registerOutParameter(2, Types.VARCHAR);
     cstmt.execute();
     String username = cstmt.getString(2);
     ```

**主要差異**：
| 功能特徵          | Statement                          | PreparedStatement                  | CallableStatement                 |
|-------------------|------------------------------------|------------------------------------|------------------------------------|
| **用途**          | 靜態 SQL 查詢                     | 參數化 SQL 查詢                   | 預存程序執行                      |
| **SQL 注入防護**  | 存在風險（手動拼接）              | 安全（參數綁定）                  | 安全（參數綁定）                  |
| **效能表現**      | 效率較低（無預編譯）              | 效率更高（預編譯）                | 針對預存程序優化                 |
| **適用場景**      | 簡單的一次性查詢                  | 重複性或參數化查詢                | 帶參數的預存程序                 |
| **參數支援**      | 不支援參數                        | 僅支援輸入參數                    | 支援輸入、輸出及輸入輸出參數     |

**使用時機**：
- 當需要執行簡單且非重複性的查詢，且安全性與效能要求不高時，使用 `Statement`。
- 當需要執行參數化查詢、重複性操作或需防範 SQL 注入時，使用 `PreparedStatement`。
- 當需呼叫帶有輸入輸出參數的資料庫預存程序時，使用 `CallableStatement`。

此說明基於標準 Java SQL API 的行為（截至知識截止日期）。如需進一步細節或範例，請隨時告知！