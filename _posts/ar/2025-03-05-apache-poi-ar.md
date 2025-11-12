---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة أباتشي POI
translated: true
type: note
---

يبدو أن هناك خطأ مطبعيًا في استفسارك "how to use com.apache.poi." في جافا، يبدأ اسم حزمة Apache POI بـ `org.apache.poi` وليس `com.apache.poi`، حيث تستخدم مشاريع Apache نطاق `org` عادةً. سأفترض أنك قصدت `org.apache.poi`، وهي مكتبة جافا شائعة للعمل مع تنسيقات ملفات Microsoft Office مثل Excel وWord وPowerPoint. فيما يلي دليل حول كيفية استخدامها، مع التركيز على حالة الاستخدام الأكثر شيوعًا: التعامل مع ملفات Excel.

---

### **ما هي Apache POI؟**
Apache POI (الاختصار لـ Poor Obfuscation Implementation) هي مكتبة جافا تسمح لك بقراءة وكتابة ومعالجة مستندات Microsoft Office برمجيًا. تُستخدم على نطاق واسع لملفات Excel (`.xls` و `.xlsx`)، ولكنها تدعم أيضًا تنسيقات Word وPowerPoint.

---

### **الخطوة 1: إضافة Apache POI إلى مشروعك**
لاستخدام Apache POI، تحتاج إلى تضمينها في مشروع جافا الخاص بك. إذا كنت تستخدم **Maven**، أضف التبعيات التالية إلى ملف `pom.xml` الخاص بك:

- للدعم الأساسي لـ Excel (كلاً من `.xls` و `.xlsx`):
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- لملفات `.xlsx` تحديدًا (يتطلب دعم OOXML إضافي):
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**ملاحظة**: تحقق من [موقع Apache POI](https://poi.apache.org/) أو Maven Central للحصول على أحدث إصدار.

إذا كنت لا تستخدم Maven، فقم بتنزيل ملفات JAR من موقع Apache POي وأضفها إلى classpath مشروعك.

---

### **الخطوة 2: الاستخدام الأساسي لملفات Excel**
توفر Apache POI فئات للعمل مع مصنفات Excel والأوراق والصفوف والخلايا. إليك كيفية البدء في قراءة وكتابة ملفات Excel.

#### **قراءة ملف Excel**
لقراءة ملف Excel، ستستخدم `WorkbookFactory` لإنشاء كائن `Workbook`، ثم التنقل عبر الأوراق والصفوف والخلايا.

إليك مثالاً بسيطًا لقراءة ومحتويات ملف Excel وطباعتها:

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // المسار إلى ملف Excel الخاص بك
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // التكرار عبر جميع الأوراق
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // التكرار عبر الصفوف والخلايا
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // سطر جديد بعد كل صف
                }
                System.out.println(); // سطر جديد بعد كل ورقة
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**النقاط الرئيسية**:
- `WorkbookFactory.create()` تعمل مع كلا نوعي الملفات `.xls` (HSSF) و `.xlsx` (XSSF).
- `DataFormatter` يبسط التعامل مع أنواع الخلايا المختلفة (نصوص، أرقام، تواريخ) عن طريق تنسيقها كسلاسل نصية.
- استخدم `try-with-resources` لإغلاق الملف والمصنف تلقائيًا.

#### **معالجة أنواع الخلايا المختلفة**
إذا كنت بحاجة إلى معالجة قيم الخلايا بناءً على نوعها (مثل: سلسلة نصية، رقم، تاريخ)، تحقق من نوع الخلية بشكل صريح:

```java
Cell cell = row.getCell(0); // الحصول على الخلية الأولى في الصف
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
        System.out.println("Unknown cell type");
}
```

#### **الكتابة إلى ملف Excel**
لإنشاء أو تعديل ملف Excel، ستقوم بإنشاء مصنف، وإضافة أوراق وصفوف وخلايا، ثم حفظه.

إليك مثالاً لإنشاء ملف `.xlsx` جديد:

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // الصف الأول
            Cell cell = row.createCell(0); // الخلية الأولى
            cell.setCellValue("Hello, POI!");

            // الكتابة إلى الملف
            try (FileOutputStream fos = new FileOutputStream("output.xlsx")) {
                workbook.write(fos);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**النقاط الرئيسية**:
- استخدم `XSSFWorkbook` لملفات `.xlsx` أو `HSSFWorkbook` لملفات `.xls`.
- استدعِ `workbook.write()` لحفظ الملف.

---

### **الخطوة 3: الفئات والمفاهيم الرئيسية**
إليك الفئات الرئيسية التي ستستخدمها في Apache POI لـ Excel:
- **`Workbook`**: يمثل ملف Excel بالكامل (`XSSFWorkbook` لـ `.xlsx`، `HSSFWorkbook` لـ `.xls`).
- **`Sheet`**: ورقة واحدة في المصنف.
- **`Row`**: صف في ورقة.
- **`Cell`**: خلية في صف.
- **`WorkbookFactory`**: ينشئ مصنفًا من ملف أو دفق، متعاملًا مع كلا نوعي الملفات.
- **`DataFormatter`**: يقوم بتنسيق قيم الخلايا كسلاسل نصية.
- **`DateUtil`**: يساعد في التعرف على الخلايا الرقمية ذات التنسيق التاريخي والتعامل معها.

لتنسيقات أخرى:
- **Word**: استخدم `XWPFDocument` (لـ `.docx`) أو `HWPFDocument` (لـ `.doc`).
- **PowerPoint**: استخدم `XMLSlideShow` (لـ `.pptx`) أو `HSLFSlideShow` (لـ `.ppt`).

---

### **الخطوة 4: نصائح وأفضل الممارسات**
- **إدارة الموارد**: استخدم دائمًا `try-with-resources` لإغلاق الملفات والمصنفات، لمنع تسرب الذاكرة.
- **معالجة الأخطاء**: اكتب كودًا للتعامل مع `IOException` لعمليات الملفات وتحقق من الصفوف/الخلايا الفارغة (null) عند الوصول عن طريق الفهرس (مثلًا، `sheet.getRow(i)` قد يعيد null).
- **الملفات الكبيرة**: لملفات Excel الكبيرة، فكر في استخدام واجهة برمجة التطبيقات (API) المتدفقة (`SXSSFWorkbook` للكتابة، `XSSFSheetXMLHandler` للقراءة) لتقليل استخدام الذاكرة.
- **التوافق**: قد لا يدعم POI جميع ميزات أحدث تنسيقات Office — تحقق من [التوثيق الرسمي](https://poi.apache.org/) للحصول على التفاصيل.

---

### **ملخص**
لاستخدام `org.apache.poi`:
1. أضف المكتبة إلى مشروعك (عبر Maven مثلًا).
2. استخدم `WorkbookFactory` لقراءة الملفات الموجودة أو إنشاء مصنفات جديدة باستخدام `XSSFWorkbook`/`HSSFWorkbook`.
3. الوصول إلى البيانات ومعالجتها عبر كائنات `Sheet` و `Row` و `Cell`.
4. احفظ التغييرات عن طريق الكتابة إلى ملف.
5. تعامل مع الاستثناءات وأغلق الموارد بشكل صحيح.

يغطي هذا الأساسيات الخاصة باستخدام Apache POI، مع التركيز على ملفات Excel. إذا كان لديك مهمة محددة في ذهنك (مثل العمل مع Word أو PowerPoint)، فأعلمني، ويمكنني تخصيص الشرح بشكل أكبر!