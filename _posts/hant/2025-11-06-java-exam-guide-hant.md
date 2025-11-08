---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Java 程式設計考試溫習指南
translated: true
type: note
---

這是一份針對 **「08553 程序設計導論—Java」第一部分** 的實用且面向考試的指南，依據《中國國家高等教育自學考試》教學大綱編寫。它專注於初學者必須掌握的概念、範例和關鍵點。

---

## 1. Java 語言概述

### 1.1 Java 特性

* **平台獨立性：** Java 代碼編譯成 *字節碼*，可在任何裝有 *Java 虛擬機 (JVM)* 的設備上運行 ——「一次編寫，到處運行」。
* **物件導向：** 支持 *封裝、繼承* 和 *多型*。
* **安全與健壯性：** 自動記憶體管理（垃圾收集）和強型別檢查可減少錯誤。
* **多執行緒：** 支持多任務並行執行。
* **豐富的標準函式庫 (API)：** 包含現成的數學、字串、檔案、網路等類別。

### 1.2 Java 版本與組件

* **JDK (Java Development Kit)：** 供開發者使用 —— 包含編譯器 (`javac`)、JVM 和開發工具。
* **JRE (Java Runtime Environment)：** 供終端使用者使用 —— 包含 JVM + 核心函式庫。
* **API (Application Programming Interface)：** Java 的內建類別庫，例如 `java.lang`、`java.util`、`java.io` 等。

---

## 2. Java 開發工具 (IDE 與 CLI)

### 2.1 常見的 IDE

對於考試，你只需要知道它們的用途：

* **Eclipse, IntelliJ IDEA, NetBeans：** 用於輕鬆編寫、編譯和運行 Java 代碼。

### 2.2 命令列工作流程

典型的編譯與執行步驟：

1. **編寫** 你的代碼到一個 `.java` 檔案中，例如 `Hello.java`
2. **編譯** 它：

   ```bash
   javac Hello.java
   ```

   → 產生 `Hello.class` (字節碼檔案)
3. **運行** 它：

   ```bash
   java Hello
   ```

   (運行時不需要 `.class` 副檔名)

### 2.3 簡單範例

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

---

## 3. 程式設計風格指南

### 3.1 命名約定

* **類別：** `CamelCase`，首字母大寫 → `StudentInfo`
* **變數與方法：** `camelCase`，首字母小寫 → `studentName`, `calculateScore()`
* **常數：** 全部大寫並使用底線 → `MAX_SIZE`

### 3.2 縮排與註解

* 使用 **一致的縮排** (通常為 4 個空格)。
* 撰寫清晰的 **註解**：

  ```java
  // 這是單行註解
  /* 這是多行註解 */
  ```

### 3.3 代碼結構

遵循邏輯分組與可讀性：

* 每個檔案包含 **一個 public 類別**，且 **類別名稱與檔案名稱相同**。
* 保持行數簡短且有意義；一行一個陳述式。

---

## 4. 常見程式設計錯誤與除錯基礎

### 4.1 語法錯誤

由編譯器偵測：

* 缺少分號 `;`
* 大括號 `{ }` 不匹配
* 錯誤的大小寫 (Java 是 **區分大小寫的**)

  ```java
  System.out.println("Hi"); // 正確
  system.out.println("Hi"); // 錯誤
  ```

### 4.2 執行時錯誤

在程式運行時發生：

* 除以零
* 陣列索引超出範圍
* 空指標異常

### 4.3 邏輯錯誤

程式可以運行，但輸出錯誤的結果。
→ 使用 **print 陳述式** 或 IDE 中的 **除錯器工具** 來逐步追蹤變數值。

---

## 5. 考試關鍵重點

* 理解 **JDK、JRE、JVM** 的角色與區別。
* 知道如何從 IDE 和命令列 **編譯和運行** Java 程式。
* 記住 **基本語法規則** 和 **風格標準**。
* 能夠 **識別常見錯誤** 並解釋其成因。
* 練習編寫小型程式，能夠：

  * 輸出訊息
  * 使用變數和表達式
  * 遵循正確的結構和命名

---

## 6. 考試題型範例

**範例 1:**

> 下列關於 Java 的敘述，哪一項是*不正確*的？
> A. Java 透過字節碼支持平台獨立性
> B. Java 程式必須始終編譯成本地機器碼
> C. JVM 執行編譯後的字節碼
> D. Java 程式可以在任何安裝了 JVM 的系統上運行

**答案：** B

**範例 2:**

> 哪個指令用於編譯名為 `Test.java` 的 Java 原始碼檔案？
> A. java Test
> B. javac Test.java
> C. run Test
> D. compile Test

**答案：** B

---

你想讓我繼續介紹 **第二部分：基本語法與資料型別** 嗎（本課程的下一個主要部分）？它將遵循同樣清晰、面向考試的結構。