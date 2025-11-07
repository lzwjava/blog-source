---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-4.5-sonnet
title: Java 程式設計基礎學習指南
translated: true
---

## 全國高等教育自學考試

本指南涵蓋 Java 程式設計課程第一部分需要掌握的基本概念。

---

## 1. Java 語言規範、API、JDK 和 IDE 工具

### **Java 語言規範**
Java 語言規範定義了 Java 的語法和語義。需要理解的關鍵概念：

- **平台獨立性**：「一次編寫，到處運行」(WORA) - Java 程式碼編譯為位元組碼，可在任何具有 JVM (Java 虛擬機) 的平台上運行
- **物件導向**：Java 中的所有內容都圍繞物件和類別組織
- **強型別**：變數必須使用特定的資料型別宣告
- **自動記憶體管理**：垃圾回收處理記憶體釋放

### **Java API (應用程式介面)**
Java API 是一個龐大的預先編寫類別庫，組織成套件：

- **核心套件**：`java.lang` (自動匯入)、`java.util`、`java.io`
- **目的**：提供即用功能 (集合、檔案 I/O、網路等)
- **文件**：可在 Oracle 官方 Java 文件網站取得
- **使用方法**：使用 `import` 語句匯入套件

### **JDK (Java 開發工具包)**
JDK 的基本組件：

- **javac**：Java 編譯器 (將 .java 檔案轉換為 .class 位元組碼檔案)
- **java**：Java 執行環境啟動器
- **javadoc**：文件生成器
- **jar**：Java 歸檔工具
- **包含 JRE**：用於執行程式的 Java 執行環境
- **標準函式庫**：完整的 Java API 實作

**安裝與設定**：
- 從 Oracle 下載或使用 OpenJDK
- 設定 JAVA_HOME 環境變數
- 將 JDK bin 目錄添加到系統 PATH 中

### **IDE (整合開發環境) 工具**
Java 開發的熱門 IDE：

1. **Eclipse** - 免費、開源，在教育領域廣泛使用
2. **IntelliJ IDEA** - 功能強大，提供免費和付費版本
3. **NetBeans** - 官方 Oracle 支援的 IDE
4. **VS Code** - 輕量級，帶有 Java 擴充功能

**IDE 優勢**：
- 語法突顯和錯誤檢測
- 程式碼完成和建議
- 整合式除錯工具
- 專案管理
- 版本控制整合

---

## 2. 建立、編譯和執行 Java 程式

### **基本 Java 程式結構**

```java
// 每個 Java 應用程式都需要一個主類別
public class HelloWorld {
    // main 方法 - 程式的進入點
    public static void main(String[] args) {
        // 你的程式碼放在這裡
        System.out.println("Hello, World!");
    }
}
```

### **逐步流程**

**步驟 1：建立 Java 程式**
- 建立一個副檔名為 `.java` 的文字檔案
- 檔案名稱必須與公開類別名稱相符 (區分大小寫)
- 範例：類別 `HelloWorld` 對應檔案 `HelloWorld.java`

**步驟 2：編譯**
```bash
javac HelloWorld.java
```
- 這會建立 `HelloWorld.class` (位元組碼檔案)
- 編譯器檢查語法錯誤
- 如果存在錯誤，編譯失敗並顯示錯誤訊息

**步驟 3：執行**
```bash
java HelloWorld
```
- 注意：使用類別名稱，不帶 `.class` 副檔名
- JVM 載入類別並執行 main 方法

### **命令列與 IDE 工作流程**

**命令列**：
- 開啟終端機/命令提示字元
- 導航到包含你的 .java 檔案的目錄
- 使用 `javac` 編譯，`java` 執行
- 有助於理解底層流程

**IDE 工作流程**：
- 建立新的 Java 專案
- 建立新的類別
- 在編輯器中編寫程式碼
- 點擊「執行」按鈕 (IDE 自動處理編譯)
- 對於較大的專案更方便

---

## 3. 程式設計風格指南

良好的程式設計風格使程式碼易讀且易於維護。遵循這些慣例：

### **命名慣例**

- **類別**：PascalCase (每個單字的首字母大寫)
  - 範例：`StudentRecord`、`BankAccount`、`HelloWorld`

- **方法和變數**：camelCase (第一個單字小寫，後續單字首字母大寫)
  - 範例：`calculateTotal()`、`firstName`、`studentAge`

- **常數**：全部大寫並使用底線
  - 範例：`MAX_SIZE`、`PI`、`DEFAULT_VALUE`

- **套件**：全部小寫，通常使用反向網域名稱
  - 範例：`com.company.project`、`java.util`

### **程式碼格式化**

**縮排**：
```java
public class Example {
    public static void main(String[] args) {
        if (condition) {
            // 縮排 4 個空格或 1 個 tab
            statement;
        }
    }
}
```

**大括號**：
- 左大括號在同一行 (Java 慣例)
- 右大括號單獨一行，與語句對齊

**間距**：
```java
// 良好的間距
int sum = a + b;
if (x > 0) {

// 不良的間距
int sum=a+b;
if(x>0){
```

### **註解**

**單行註解**：
```java
// 這是單行註解
int age = 20; // 程式碼後的註解
```

**多行註解**：
```java
/*
 * 這是多行註解
 * 用於較長的解釋
 */
```

**Javadoc 註解** (用於文件)：
```java
/**
 * 計算兩個數字的總和。
 * @param a 第一個數字
 * @param b 第二個數字
 * @return a 和 b 的總和
 */
public int add(int a, int b) {
    return a + b;
}
```

### **最佳實踐**

1. **有意義的名稱**：使用描述性的變數和方法名稱
   - 良好：`studentCount`、`calculateAverage()`
   - 不良：`x`、`doStuff()`

2. **每行一個語句**：避免在一行中擠入多個語句

3. **一致的風格**：在整個程式碼中遵循相同的慣例

4. **空白行**：使用空行分隔邏輯部分

5. **保持方法簡短**：每個方法應該做好一件事

---

## 4. 常見程式設計錯誤和除錯基礎

### **錯誤類型**

#### **A. 語法錯誤 (編譯時錯誤)**
這些錯誤阻止編譯，必須在執行前修復：

**常見語法錯誤**：
```java
// 缺少分號
int x = 5  // 錯誤：缺少 ;

// 大括號不匹配
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello");
    // 缺少右大括號 }

// 大小寫敏感度
String name = "John";
system.out.println(name); // 錯誤：應為 'System'

// 檔案名稱不匹配
// 檔案：Test.java
public class MyClass { // 錯誤：類別名稱必須與檔案名稱相符
```

#### **B. 執行時錯誤**
程式編譯成功，但在執行期間崩潰：

```java
// 除以零
int result = 10 / 0; // ArithmeticException

// 空指標
String str = null;
int length = str.length(); // NullPointerException

// 陣列索引超出範圍
int[] arr = {1, 2, 3};
int value = arr[5]; // ArrayIndexOutOfBoundsException
```

#### **C. 邏輯錯誤**
程式運行但產生錯誤結果：

```java
// 錯誤的運算子
int average = (a + b) * 2; // 應為 / 而不是 *

// 差一錯誤
for (int i = 0; i <= arr.length; i++) { // 應為 i < arr.length

// 錯誤的條件
if (age > 18) { // 對於「18 歲及以上」應為 >=
```

### **除錯技巧**

#### **1. 仔細閱讀錯誤訊息**
```
HelloWorld.java:5: error: ';' expected
        int x = 5
                 ^
1 error
```
- **行號**：顯示錯誤發生的位置 (第 5 行)
- **錯誤類型**：告訴你哪裡出錯 (缺少分號)
- **指標**：顯示確切位置

#### **2. 列印語句除錯**
```java
public static int calculateSum(int a, int b) {
    System.out.println("除錯：a = " + a + ", b = " + b);
    int sum = a + b;
    System.out.println("除錯：sum = " + sum);
    return sum;
}
```

#### **3. 使用 IDE 除錯器**
- **中斷點**：在特定行暫停執行
- **單步跳越**：執行目前行並移至下一行
- **單步進入**：進入方法呼叫以查看內部執行
- **監看變數**：即時監控變數值
- **呼叫堆疊**：查看方法呼叫的順序

#### **4. 分而治之**
- 註解掉程式碼部分以隔離問題
- 獨立測試小部分
- 逐漸添加程式碼直到錯誤再次出現

#### **5. 橡皮鴨除錯法**
- 向某人 (或某物) 逐行解釋你的程式碼
- 通常能幫助你自己發現問題

### **常見初學者錯誤**

1. **更改後忘記重新編譯**
   - 執行前務必重新編譯

2. **類別名稱與檔案名稱不符**
   - `public class Student` 必須在 `Student.java` 中

3. **缺少 main 方法簽章**
   - 必須完全符合：`public static void main(String[] args)`

4. **忘記匯入套件**
   ```java
   import java.util.Scanner; // 不要忘記這個！
   ```

5. **錯誤的大小寫**
   - `String` 不是 `string`，`System` 不是 `system`

6. **在條件中使用 = 而不是 ==**
   ```java
   if (x = 5) { // 錯誤：賦值，不是比較
   if (x == 5) { // 正確
   ```

---

## 考試準備技巧

### **學習內容**

1. **記憶**：
   - Main 方法簽章
   - 基本程式結構
   - 命名慣例
   - 常見錯誤類型

2. **理解**：
   - JDK、JRE 和 JVM 之間的區別
   - 編譯與執行過程
   - 為什麼 Java 是平台獨立的

3. **練習**：
   - 手寫簡單程式
   - 識別程式碼範例中的錯誤
   - 追蹤程式執行

### **常見考試題型**

1. **多選題**：「什麼是正確的 main 方法簽章？」
2. **錯誤識別**：「找出此程式碼中的語法錯誤」
3. **程式碼追蹤**：「此程式的輸出是什麼？」
4. **簡答題**：「解釋 JDK 和 JRE 的區別」
5. **程式碼編寫**：「編寫一個輸出 'Hello, China!' 的程式」

### **練習題**

嘗試識別並修復此程式碼中的所有錯誤：

```java
public class test {
    Public Static Void Main(string[] args) {
        int x = 5
        int y = 10;
        System.Out.Println(x + y)
    }
}
```

**答案**：
- 類別名稱應為 `Test` (大寫 T) 並與檔案名稱相符
- `Public` → `public`，`Static` → `static`，`Void` → `void`
- `string` → `String`
- `int x = 5` 後缺少分號
- `System.Out` → `System.out`
- println 語句後缺少分號

---

## 總結檢查清單

考試前，確保你能夠：

- ☐ 解釋什麼是 JDK、JRE、JVM 和 API
- ☐ 編寫具有正確結構的基本 Java 程式
- ☐ 使用命令列編譯和執行程式
- ☐ 遵循 Java 命名慣例
- ☐ 識別語法、執行時和邏輯錯誤
- ☐ 使用基本除錯技巧
- ☐ 編寫格式正確且帶有註解的程式碼

祝考試順利！加油！