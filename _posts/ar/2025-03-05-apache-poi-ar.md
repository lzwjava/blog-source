---
audio: false
generated: true
lang: ar
layout: post
title: مكتبة Apache POI
translated: true
---

يبدو أن هناك خطأ في استفسارك "how to use com.apache.poi." في Java، يبدأ اسم حزمة Apache POI بـ `org.apache.poi` وليس `com.apache.poi`، حيث أن مشاريع Apache تستخدم عادةً نطاق `org`. سأفترض أنك قصدت `org.apache.poi`، وهو مكتبة Java شائعة للاستخدام مع تنسيقات ملفات Microsoft Office مثل Excel، Word، و PowerPoint. أدناه دليل على كيفية استخدامه، مع التركيز على الحالة الشائعة الأكثر شيوعًا: معالجة ملفات Excel.

---

### **ما هو Apache POI؟**
Apache POI (Poor Obfuscation Implementation) هي مكتبة Java تسمح لك بقراءة، كتابة، وتعديل مستندات Microsoft Office بشكل برمجي. وهي تستخدم بشكل واسع لملفات Excel (.xls و .xlsx)، ولكنها تدعم أيضًا تنسيقات Word و PowerPoint.

---

### **الخطوة 1: إضافة Apache POI إلى مشروعك**
لاستخدام Apache POI، عليك تضمينه في مشروع Java الخاص بك. إذا كنت تستخدم **Maven**، أضف التبعيات التالية إلى ملف `pom.xml` الخاص بك:

- للدعم الأساسي لملفات Excel (كل من .xls و .xlsx):
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- لملفات .xlsx بشكل خاص (يحتاج إلى دعم OOXML إضافي):
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**ملاحظة**: تحقق من [موقع Apache POI](https://poi.apache.org/) أو Maven Central للحصول على أحدث الإصدار.

إذا كنت لا تستخدم Maven، قم بتنزيل ملفات JAR من موقع Apache POI وأضفها إلى مسار تصنيفات مشروعك.

---

### **الخطوة 2: الاستخدام الأساسي لملفات Excel**
يوفر Apache POI فئات للعمل مع كتيبات Excel، الأوراق، الصفوف، والأخدات. إليك كيفية البدء في قراءة وكتابة ملفات Excel.

#### **قراءة ملف Excel**
لقراءة ملف Excel، ستستخدم `WorkbookFactory` لإنشاء مثيل `Workbook`، ثم التنقل عبر الأوراق، الصفوف، والأخدات.

إليك مثالًا بسيطًا لقراءة وإظهار محتويات ملف Excel:

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // مسار ملف Excel الخاص بك
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // التنقل عبر جميع الأوراق
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // التنقل عبر الصفوف والأخدات
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
- `WorkbookFactory.create()` يعمل مع كل من ملفات .xls (HSSF) و .xlsx (XSSF).
- `DataFormatter` يسهل معالجة أنواع مختلفة من الأخدات (نصوص، أرقام، تواريخ) من خلال تنسيقها كنصوص.
- استخدم `try-with-resources` لإغلاق الملف والكتيب تلقائيًا.

#### **معالجة أنواع مختلفة من الأخدات**
إذا كنت تحتاج إلى معالجة قيم الأخدات بناءً على نوعها (مثل نص، رقم، تاريخ)، تحقق من نوع الأخدة بشكل صريح:

```java
Cell cell = row.getCell(0); // الحصول على أول أخدة في صف
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
        System.out.println("نوع أخدة مجهول");
}
```

#### **كتابة في ملف Excel**
لإنشاء أو تعديل ملف Excel، ستخلق كتيبًا، وتضيف أوراقًا، صفوفًا، وأخدات، ثم تحفظه.

إليك مثالًا لإنشاء ملف .xlsx جديد:

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
            Cell cell = row.createCell(0); // الأخدة الأولى
            cell.setCellValue("Hello, POI!");

            // كتابة إلى الملف
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
- استخدم `XSSFWorkbook` لملفات .xlsx أو `HSSFWorkbook` لملفات .xls.
- استدعاء `workbook.write()` لحفظ الملف.

---

### **الخطوة 3: الفئات الرئيسية والمفاهيم**
إليك الفئات الرئيسية التي ستستخدمها في Apache POI لملفات Excel:
- **`Workbook`**: يمثل الملف الكامل لملف Excel (`XSSFWorkbook` لملفات .xlsx، `HSSFWorkbook` لملفات .xls).
- **`Sheet`**: ورقة واحدة في الكتيب.
- **`Row`**: صف في ورقة.
- **`Cell`**: أخدة في صف.
- **`WorkbookFactory`**: يخلق كتيبًا من ملف أو تدفق، يدعم كل من أنواع الملفات.
- **`DataFormatter`**: ينسق قيم الأخدات كنصوص.
- **`DateUtil`**: يساعد في تحديد وتعامل مع أخدات الأرقام التي تنسيقها تاريخ.

لملفات أخرى:
- **Word**: استخدم `XWPFDocument` (.docx) أو `HWPFDocument` (.doc).
- **PowerPoint**: استخدم `XMLSlideShow` (.pptx) أو `HSLFSlideShow` (.ppt).

---

### **الخطوة 4: النصائح والممارسات الجيدة**
- **إدارة الموارد**: استخدم دائمًا `try-with-resources` لإغلاق الملفات والكتيبات، لمنع تسرب الذاكرة.
- **معالجة الأخطاء**: احرص على استثناءات `IOException` لعملية الملفات، وتحقق من الصفوف/الأخدات الفارغة عند الوصول إليها حسب الفهرس (مثل `sheet.getRow(i)` قد يعيد `null`).
- **ملفات كبيرة**: لملفات Excel الكبيرة، اعتبر استخدام واجهة التدفق (`SXSSFWorkbook` للكتابة، `XSSFSheetXMLHandler` للقراءة) لتقلل من استخدام الذاكرة.
- **التوافق**: قد لا يدعم POI جميع ميزات أحدث تنسيقات Office—تحقق من [التوثيق الرسمي](https://poi.apache.org/) للحصول على التفاصيل.

---

### **الملخص**
لاستخدام `org.apache.poi`:
1. أضف المكتبة إلى مشروعك (مثلًا عبر Maven).
2. استخدم `WorkbookFactory` لقراءة الملفات الموجودة أو إنشاء كتيبات جديدة مع `XSSFWorkbook`/`HSSFWorkbook`.
3. الوصول إلى البيانات والتعديل عبر كائنات `Sheet`، `Row`، و `Cell`.
4. حفظ التغييرات من خلال الكتابة إلى ملف.
5. معالجة الاستثناءات وإغلاق الموارد بشكل صحيح.

هذا يغطي الأساسيات لاستخدام Apache POI، مع التركيز على ملفات Excel. إذا كان لديك مهمة محددة في ذهنك (مثل العمل مع Word أو PowerPoint)، أخبرني، وسأقوم بتخصيص التفسير بشكل أكبر!