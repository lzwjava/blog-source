---
audio: false
generated: true
lang: zh
layout: post
title: Apache POI 库
translated: true
---

看起来你的查询 "how to use com.apache.poi." 可能有拼写错误。在 Java 中，Apache POI 的包名以 `org.apache.poi` 开头，而不是 `com.apache.poi`，因为 Apache 项目通常使用 `org` 域。我会假设你指的是 `org.apache.poi`，这是一个用于处理 Microsoft Office 文件格式（如 Excel、Word 和 PowerPoint）的流行 Java 库。下面是如何使用它的指南，重点介绍最常见的用例：处理 Excel 文件。

---

### **什么是 Apache POI？**
Apache POI（Poor Obfuscation Implementation）是一个允许你以编程方式读取、写入和操作 Microsoft Office 文档的 Java 库。它广泛用于 Excel 文件（.xls 和 .xlsx），但也支持 Word 和 PowerPoint 格式。

---

### **步骤 1：将 Apache POI 添加到您的项目中**
要使用 Apache POI，你需要在 Java 项目中包含它。如果你使用 **Maven**，将以下依赖项添加到你的 `pom.xml` 文件中：

- 为了基本的 Excel 支持（包括 .xls 和 .xlsx）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- 专门用于 .xlsx 文件（需要额外的 OOXML 支持）：
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**注意**：请访问 [Apache POI 网站](https://poi.apache.org/) 或 Maven Central 以获取最新版本。

如果你不使用 Maven，请从 Apache POI 网站下载 JAR 文件并将其添加到项目的类路径中。

---

### **步骤 2：Excel 文件的基本使用**
Apache POI 提供了用于处理 Excel 工作簿、工作表、行和单元格的类。以下是如何开始读取和写入 Excel 文件的方法。

#### **读取 Excel 文件**
要读取 Excel 文件，你将使用 `WorkbookFactory` 创建一个 `Workbook` 实例，然后导航到工作表、行和单元格。

以下是一个简单的示例，用于读取并打印 Excel 文件的内容：

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // 到你的 Excel 文件的路径
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // 遍历所有工作表
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // 遍历行和单元格
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // 每行结束后换行
                }
                System.out.println(); // 每个工作表结束后换行
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**关键点**：
- `WorkbookFactory.create()` 可以处理 .xls（HSSF）和 .xlsx（XSSF）文件。
- `DataFormatter` 通过将它们格式化为字符串来简化处理不同类型的单元格（字符串、数字、日期）。
- 使用 `try-with-resources` 自动关闭文件和工作簿。

#### **处理不同类型的单元格**
如果你需要根据单元格类型（例如字符串、数字、日期）处理单元格值，请明确检查单元格类型：

```java
Cell cell = row.getCell(0); // 获取行中的第一个单元格
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
        System.out.println("未知单元格类型");
}
```

#### **写入 Excel 文件**
要创建或修改 Excel 文件，你将创建一个工作簿，添加工作表、行和单元格，然后保存它。

以下是一个创建新 .xlsx 文件的示例：

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // 第一个行
            Cell cell = row.createCell(0); // 第一个单元格
            cell.setCellValue("Hello, POI!");

            // 写入文件
            try (FileOutputStream fos = new FileOutputStream("output.xlsx")) {
                workbook.write(fos);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**关键点**：
- 使用 `XSSFWorkbook` 处理 .xlsx 文件或 `HSSFWorkbook` 处理 .xls 文件。
- 调用 `workbook.write()` 保存文件。

---

### **步骤 3：关键类和概念**
以下是你在 Apache POI 中用于 Excel 的主要类：
- **`Workbook`**：表示整个 Excel 文件（`XSSFWorkbook` 用于 .xlsx，`HSSFWorkbook` 用于 .xls）。
- **`Sheet`**：工作簿中的一个工作表。
- **`Row`**：工作表中的一行。
- **`Cell`**：行中的一个单元格。
- **`WorkbookFactory`**：从文件或流创建工作簿，处理两种文件类型。
- **`DataFormatter`**：将单元格值格式化为字符串。
- **`DateUtil`**：帮助识别和处理日期格式的数字单元格。

对于其他格式：
- **Word**：使用 `XWPFDocument`（.docx）或 `HWPFDocument`（.doc）。
- **PowerPoint**：使用 `XMLSlideShow`（.pptx）或 `HSLFSlideShow`（.ppt）。

---

### **步骤 4：技巧和最佳实践**
- **资源管理**：始终使用 `try-with-resources` 关闭文件和工作簿，防止内存泄漏。
- **错误处理**：捕获文件操作的 `IOException`，并在按索引访问时检查空行/单元格（例如，`sheet.getRow(i)` 可能返回 null）。
- **大文件**：对于大型 Excel 文件，考虑使用流 API（`SXSSFWorkbook` 用于写入，`XSSFSheetXMLHandler` 用于读取）以减少内存使用。
- **兼容性**：POI 可能不支持最新 Office 格式的所有功能——请参阅[官方文档](https://poi.apache.org/) 以获取详细信息。

---

### **总结**
要使用 `org.apache.poi`：
1. 将库添加到你的项目中（例如，通过 Maven）。
2. 使用 `WorkbookFactory` 读取现有文件，或者使用 `XSSFWorkbook`/`HSSFWorkbook` 创建新工作簿。
3. 通过 `Sheet`、`Row` 和 `Cell` 对象访问和操作数据。
4. 通过将其写入文件来保存更改。
5. 正确处理异常并关闭资源。

这涵盖了使用 Apache POI 的基础知识，重点介绍 Excel 文件。如果你有特定的任务（例如，处理 Word 或 PowerPoint），请告诉我，我可以进一步定制说明！