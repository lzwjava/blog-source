---
audio: false
generated: true
lang: hant
layout: post
title: Apache POI 圖書館
translated: true
---

看來你的查詢 "how to use com.apache.poi." 可能有拼寫錯誤。在 Java 中，Apache POI 的套件名稱以 `org.apache.poi` 開頭，而不是 `com.apache.poi`，因為 Apache 專案通常使用 `org` 域。我會假設你指的是 `org.apache.poi`，這是一個流行的 Java 庫，用於處理 Microsoft Office 文件格式，如 Excel、Word 和 PowerPoint。以下是如何使用它的指南，重點放在最常見的用例：處理 Excel 文件。

---

### **什麼是 Apache POI？**
Apache POI（Poor Obfuscation Implementation）是一個 Java 庫，允許你以程式設計方式讀取、寫入和操作 Microsoft Office 文件。它廣泛用於 Excel 文件（.xls 和 .xlsx），但也支持 Word 和 PowerPoint 格式。

---

### **步驟 1：將 Apache POI 添加到你的項目**
要使用 Apache POI，你需要在 Java 專案中包含它。如果你使用 **Maven**，請將以下依賴項添加到你的 `pom.xml` 文件中：

- 針對基本 Excel 支持（.xls 和 .xlsx 兩者）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- 針對 .xlsx 文件（需要額外的 OOXML 支持）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**注意**：請檢查 [Apache POI 網站](https://poi.apache.org/) 或 Maven Central 以獲取最新版本。

如果你不使用 Maven，請從 Apache POI 網站下載 JAR 文件並將其添加到項目的類路徑中。

---

### **步驟 2：Excel 文件的基本使用**
Apache POI 提供了類來處理 Excel 工作簿、工作表、行和單元格。以下是如何開始讀取和寫入 Excel 文件。

#### **讀取 Excel 文件**
要讀取 Excel 文件，請使用 `WorkbookFactory` 來創建 `Workbook` 實例，然後導航到工作表、行和單元格。

以下是一個簡單的示例，用於讀取並打印 Excel 文件的內容：

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // Excel 文件的路徑
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // 循環遍歷所有工作表
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("工作表: " + sheet.getSheetName());
                // 循環遍歷行和單元格
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // 每行結束後換行
                }
                System.out.println(); // 每個工作表結束後換行
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**關鍵點**：
- `WorkbookFactory.create()` 可以處理 .xls（HSSF）和 .xlsx（XSSF）文件。
- `DataFormatter` 簡化了處理不同單元格類型（字符串、數字、日期）的方式，將它們格式化為字符串。
- 使用 `try-with-resources` 自動關閉文件和工作簿。

#### **處理不同的單元格類型**
如果你需要根據單元格類型（例如字符串、數字、日期）處理單元格值，請明確檢查單元格類型：

```java
Cell cell = row.getCell(0); // 获取行中的第一個單元格
switch (cell.getCellType()) {
    case STRING:
        System.out.println(cell.getStringCellValue());
        break;
    case NUMERIC:
        if (DateUtil.isCellDateFormatted(cell)) {
            System.out.println(cell.getDateCellValue());
        } else {
            System.out.println(cell.getNumericCellValue());
        }
        break;
    case BOOLEAN:
        System.out.println(cell.getBooleanCellValue());
        break;
    default:
        System.out.println("未知的單元格類型");
}
```

#### **寫入 Excel 文件**
要創建或修改 Excel 文件，請創建工作簿，添加工作表、行和單元格，然後保存它。

以下是創建新 .xlsx 文件的示例：

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // 第一行
            Cell cell = row.createCell(0); // 第一個單元格
            cell.setCellValue("Hello, POI!");

            // 寫入文件
            try (FileOutputStream fos = new FileOutputStream("output.xlsx")) {
                workbook.write(fos);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**關鍵點**：
- 使用 `XSSFWorkbook` 針對 .xlsx 文件或 `HSSFWorkbook` 針對 .xls 文件。
- 請呼叫 `workbook.write()` 來保存文件。

---

### **步驟 3：關鍵類和概念**
以下是你在 Apache POI 中使用的主要類，針對 Excel：
- **`Workbook`**：表示整個 Excel 文件（`XSSFWorkbook` 針對 .xlsx，`HSSFWorkbook` 針對 .xls）。
- **`Sheet`**：工作簿中的單個工作表。
- **`Row`**：工作表中的一行。
- **`Cell`**：行中的單元格。
- **`WorkbookFactory`**：從文件或流創建工作簿，處理兩種文件類型。
- **`DataFormatter`**：將單元格值格式化為字符串。
- **`DateUtil`**：幫助識別和處理日期格式的數字單元格。

針對其他格式：
- **Word**：使用 `XWPFDocument`（.docx）或 `HWPFDocument`（.doc）。
- **PowerPoint**：使用 `XMLSlideShow`（.pptx）或 `HSLFSlideShow`（.ppt）。

---

### **步驟 4：技巧和最佳實踐**
- **資源管理**：始終使用 `try-with-resources` 來關閉文件和工作簿，防止記憶體洩漏。
- **錯誤處理**：捕捉 `IOException` 進行文件操作，並檢查 null 行/單元格（例如，`sheet.getRow(i)` 可能返回 null）。
- **大文件**：針對大 Excel 文件，考慮使用流 API（`SXSSFWorkbook` 針對寫入，`XSSFSheetXMLHandler` 針對讀取）以減少記憶體使用。
- **兼容性**：POI 可能不支持最新 Office 格式的所有功能—請參閱 [官方文檔](https://poi.apache.org/) 以獲取詳細信息。

---

### **總結**
要使用 `org.apache.poi`：
1. 將庫添加到你的項目（例如，通過 Maven）。
2. 使用 `WorkbookFactory` 讀取現有文件或使用 `XSSFWorkbook`/`HSSFWorkbook` 創建新工作簿。
3. 通過 `Sheet`、`Row` 和 `Cell` 對象訪問和操作數據。
4. 通過寫入文件來保存更改。
5. 正確處理異常並關閉資源。

這涵蓋了使用 Apache POI 的基本知識，重點放在 Excel 文件上。如果你有特定的任務（例如，處理 Word 或 PowerPoint），請告訴我，我可以進一步針對說明！