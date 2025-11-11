---
audio: false
generated: true
lang: hant
layout: post
title: Apache POI 程式庫
translated: true
type: note
---

看來你的查詢中可能存在拼寫錯誤「how to use com.apache.poi」。在 Java 中，Apache POI 的套件名稱以 `org.apache.poi` 開頭，而非 `com.apache.poi`，因為 Apache 專案通常使用 `org` 網域。我假設你指的是 `org.apache.poi`，這是一個用於處理 Microsoft Office 檔案格式（如 Excel、Word 和 PowerPoint）的熱門 Java 函式庫。以下將重點介紹最常見的使用情境：處理 Excel 檔案。

---

### **什麼是 Apache POI？**
Apache POI（Poor Obfuscation Implementation）是一個 Java 函式庫，可讓您以程式方式讀取、寫入和操作 Microsoft Office 文件。它廣泛用於 Excel 檔案（.xls 和 .xlsx），但也支援 Word 和 PowerPoint 格式。

---

### **步驟 1：將 Apache POI 加入專案**
要使用 Apache POI，您需要將其加入 Java 專案中。如果您使用 **Maven**，請將以下依賴項加入 `pom.xml` 檔案：

- 用於基本 Excel 支援（同時支援 .xls 和 .xlsx）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- 專門用於 .xlsx 檔案（需要額外的 OOXML 支援）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**注意**：請查閱 [Apache POI 官網](https://poi.apache.org/) 或 Maven Central 以獲取最新版本。

如果您不使用 Maven，請從 Apache POI 官網下載 JAR 檔案，並將其加入專案的 classpath 中。

---

### **步驟 2：Excel 檔案的基本用法**
Apache POI 提供了用於處理 Excel 活頁簿、工作表、列和儲存格的類別。以下是開始讀取和寫入 Excel 檔案的方法。

#### **讀取 Excel 檔案**
要讀取 Excel 檔案，您將使用 `WorkbookFactory` 建立 `Workbook` 實例，然後瀏覽工作表、列和儲存格。

以下是一個簡單範例，用於讀取並列印 Excel 檔案的內容：

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // 您的 Excel 檔案路徑
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // 循環所有工作表
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("工作表: " + sheet.getSheetName());
                // 循環列和儲存格
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // 每列後換行
                }
                System.out.println(); // 每個工作表後換行
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**關鍵點**：
- `WorkbookFactory.create()` 適用於 .xls（HSSF）和 .xlsx（XSSF）檔案。
- `DataFormatter` 透過將不同儲存格類型（字串、數字、日期）格式化為字串，簡化了處理過程。
- 使用 `try-with-resources` 自動關閉檔案和活頁簿。

#### **處理不同儲存格類型**
如果您需要根據儲存格類型（例如字串、數字、日期）處理儲存格值，請明確檢查儲存格類型：

```java
Cell cell = row.getCell(0); // 取得列中的第一個儲存格
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
        System.out.println("未知的儲存格類型");
}
```

#### **寫入 Excel 檔案**
要建立或修改 Excel 檔案，您需要建立活頁簿、新增工作表、列和儲存格，然後儲存。

以下是一個建立新 .xlsx 檔案的範例：

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // 第一列
            Cell cell = row.createCell(0); // 第一個儲存格
            cell.setCellValue("Hello, POI!");

            // 寫入檔案
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
- 使用 `XSSFWorkbook` 處理 .xlsx 檔案，或使用 `HSSFWorkbook` 處理 .xls 檔案。
- 呼叫 `workbook.write()` 以儲存檔案。

---

### **步驟 3：關鍵類別與概念**
以下是 Apache POI 中用於 Excel 的主要類別：
- **`Workbook`**：代表整個 Excel 檔案（.xlsx 使用 `XSSFWorkbook`，.xls 使用 `HSSFWorkbook`）。
- **`Sheet`**：活頁簿中的單個工作表。
- **`Row`**：工作表中的列。
- **`Cell`**：列中的儲存格。
- **`WorkbookFactory`**：從檔案或流建立活頁簿，處理兩種檔案類型。
- **`DataFormatter`**：將儲存格值格式化為字串。
- **`DateUtil`**：協助識別和處理日期格式的數字儲存格。

對於其他格式：
- **Word**：使用 `XWPFDocument`（.docx）或 `HWPFDocument`（.doc）。
- **PowerPoint**：使用 `XMLSlideShow`（.pptx）或 `HSLFSlideShow`（.ppt）。

---

### **步驟 4：提示與最佳實踐**
- **資源管理**：始終使用 `try-with-resources` 關閉檔案和活頁簿，防止記憶體洩漏。
- **錯誤處理**：捕獲檔案操作的 `IOException`，並在按索引存取時檢查 null 列/儲存格（例如，`sheet.getRow(i)` 可能返回 null）。
- **大型檔案**：對於大型 Excel 檔案，考慮使用串流 API（寫入使用 `SXSSFWorkbook`，讀取使用 `XSSFSheetXMLHandler`）以減少記憶體使用。
- **相容性**：POI 可能不支援最新 Office 格式的所有功能——請查閱[官方文件](https://poi.apache.org/)以獲取詳細資訊。

---

### **總結**
要使用 `org.apache.poi`：
1. 將函式庫加入專案（例如透過 Maven）。
2. 使用 `WorkbookFactory` 讀取現有檔案，或使用 `XSSFWorkbook`/`HSSFWorkbook` 建立新活頁簿。
3. 透過 `Sheet`、`Row` 和 `Cell` 物件存取和操作資料。
4. 透過寫入檔案儲存變更。
5. 正確處理異常並關閉資源。

這涵蓋了使用 Apache POI 的基礎知識，重點在於 Excel 檔案。如果您有特定的任務需求（例如處理 Word 或 PowerPoint），請告訴我，我可以進一步調整說明！