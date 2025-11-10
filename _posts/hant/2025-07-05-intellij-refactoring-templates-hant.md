---
audio: false
generated: true
lang: hant
layout: post
title: IntelliJ 結構性替換範本
translated: true
type: note
---

以下是 10 個 IntelliJ 結構化替換模板的範例，已分類整理以便理解。這些模板在重構程式碼、強制執行編碼標準及自動化常見程式碼轉換方面極具威力。

**基礎重構與簡化：**

1. **將 `if (condition) return true; else return false;` 替換為 `return condition;`**

      * **搜尋模板：**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **替換模板：**
        ```java
        return $CONDITION$;
        ```
      * **適用情境：** 簡化布林回傳陳述式。

2. **將 `if (condition) { statement; }` 替換為 `if (!condition) { continue/break/return; }`（防衛陳述式）**

      * **搜尋模板：**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **替換模板：**（此模板主要用於建議轉換方式，實際需手動調整內部內容）
        ```java
        if (!$CONDITION$) {
            // 可考慮在此處使用 continue、break 或 return
        }
        $STATEMENTS$;
        ```
      * **適用情境：** 鼓勵使用防衛陳述式來簡化程式流程。通常會在找到結構後使用「替換為」操作。

**集合與串流操作：**

3. **將 `for (Type item : collection) { if (item.getProperty() == value) { ... } }` 替換為串流的 `filter` 操作**

      * **搜尋模板：**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **替換模板：**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // 或使用 .map().collect() 等操作
        ```
      * **適用情境：** 將傳統迴圈遷移至 Java Stream 進行過濾。此為通用範例，實際應用中可能需要更針對 `map`、`collect` 等操作的專用模板。

4. **將 `new ArrayList<>().add(item1); new ArrayList<>().add(item2);` 替換為 `List.of(item1, item2);`**

      * **搜尋模板：**（此操作可能需要針對不同數量的 `add` 呼叫設計多個模板，或使用更複雜的正則表達式。此為針對兩個項目的簡化版本）：
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **替換模板：**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **適用情境：** 使用 Java 9+ 的 `List.of()` 建立不可變列表。

**錯誤處理與資源管理：**

5. **將 `try { ... } catch (Exception e) { e.printStackTrace(); }` 替換為更完善的日誌記錄**

      * **搜尋模板：**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **替換模板：**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // 替換為您偏好的日誌記錄框架，例如：
            // logger.error("發生錯誤", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // 或重新拋出特定例外
        }
        ```
      * **適用情境：** 鼓勵使用正確的錯誤日誌記錄，而非僅印出堆疊追蹤。

6. **將 `try { ... } finally { closeable.close(); }` 替換為 `try-with-resources`**

      * **搜尋模板：**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **替換模板：**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **適用情境：** 將資源管理現代化，改用 `try-with-resources`（Java 7+）。

**類別與方法結構：**

7. **找出可宣告為 `final` 的欄位**

      * **搜尋模板：**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **替換模板：**（此模板主要用於標記，後續可使用快速修復功能）
        ```java
        class $CLASS$ {
            // 若此欄位僅被賦值一次，可考慮宣告為 final
            final $TYPE$ $FIELD$;
        }
        ```
      * **適用情境：** 識別可提升不可變性的機會。需設定過濾條件僅顯示未被多次賦值的欄位。

8. **將 `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` 替換為自訂日誌工具**

      * **搜尋模板：**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **替換模板：**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // 或使用您工具類別中更特定的 getLogger($CLASS_NAME$.class) 方法
        ```
      * **適用情境：** 在程式碼庫中強制實施統一的日誌初始化模式。

**註解與樣板程式碼：**

9. **為覆寫父類別的方法添加 `@Override` 註解（若缺失時）**

      * **搜尋模板：**（此操作較複雜，通常使用 IntelliJ 內建檢查功能更為合適，此處僅供示範）
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **替換模板：**（同樣主要用於標記，後續應用快速修復）
        ```java
        class $CLASS$ {
            @Override // 若此方法覆寫了父類別方法，請添加此註解
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **適用情境：** 強制實施良好實踐並捕捉拼寫錯誤。需使用過濾器檢查方法是否存在於父類別/介面中。

10. **將重複的 `getter/setter` 方法替換為 Lombok 註解**

      * **搜尋模板：**（針對單個 getter，此操作在類別層級會顯得重複）
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **替換模板：**（此為概念性模板，實際操作需刪除 getter 並在欄位或類別添加 `@Getter`）
        ```java
        // 可考慮使用 @lombok.Getter 註解替換：
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **適用情境：** 自動化遷移至 Lombok。對於完整類別，可針對類別本身進行操作，並根據現有方法建議使用 `@Data` 或 `@Getter/@Setter` 註解。這是較進階且可能需多步驟的轉換操作。

**在 IntelliJ 中的使用方法：**

1.  前往 `Analyze` -> `Inspect Code...`
2.  在 `Inspection Profile` 視窗中，點擊設定檔名稱旁的 `...` 進行編輯
3.  導覽至 `Java` -> `General` -> `Structural Search Inspection`
4.  點擊 `+` 按鈕新增搜尋/替換模板
5.  定義您的 `Search Template` 和 `Replacement Template`
6.  使用 `Variables` 分頁定義變數的約束條件（例如類型、文字、數量）
7.  對您的程式碼執行檢查，IntelliJ 將建議替換或標示發現項目

這些範例展示了結構化搜尋與替換的多功能性。模板設計得越具體、約束條件越嚴格，替換結果就越準確實用。