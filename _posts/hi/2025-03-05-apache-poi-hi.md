---
audio: false
generated: true
lang: hi
layout: post
title: Apache POI लाइब्रेरी
translated: true
---

आपके पुछे में "how to use com.apache.poi." में एक टाइपो हो सकता है। जावा में, Apache POI का पैकेज नाम `org.apache.poi` से शुरू होता है, नहीं `com.apache.poi`, क्योंकि Apache प्रोजेक्ट्स आमतौर पर `org` डोमेन का उपयोग करते हैं। मैं मानता हूँ कि आपने `org.apache.poi` का मतलब था, जो एक लोकप्रिय जावा लाइब्रेरी है Microsoft Office फ़ाइल फ़ॉर्मेट्स जैसे Excel, Word, और PowerPoint के साथ काम करने के लिए। नीचे एक गाइड है कि इसे कैसे उपयोग करें, जो सबसे आम उपयोग मामले पर ध्यान केंद्रित करता है: Excel फ़ाइलों का संचालन।

---

### **Apache POI क्या है?**
Apache POI (Poor Obfuscation Implementation) एक जावा लाइब्रेरी है जो आपको Microsoft Office दस्तावेज़ को प्रोग्रामेटिक रूप से पढ़ने, लिखने और संशोधित करने की अनुमति देता है। यह Excel फ़ाइलें (.xls और .xlsx) के लिए व्यापक रूप से उपयोग किया जाता है, लेकिन यह Word और PowerPoint फ़ॉर्मेट्स का भी समर्थन करता है।

---

### **Step 1: Add Apache POI to Your Project**
Apache POI का उपयोग करने के लिए, आपको इसे अपने जावा प्रोजेक्ट में शामिल करना होगा। अगर आप **Maven** का उपयोग कर रहे हैं, तो अपने `pom.xml` फ़ाइल में निम्नलिखित निर्भरताओं को जोड़ें:

- बुनियादी Excel समर्थन (दोनों .xls और .xlsx) के लिए:
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- विशेष रूप से .xlsx फ़ाइलों के लिए (जिसे अतिरिक्त OOXML समर्थन की आवश्यकता होती है):
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**नोट**: [Apache POI वेबसाइट](https://poi.apache.org/) या Maven Central पर नवीनतम संस्करण की जांच करें।

अगर आप Maven का उपयोग नहीं कर रहे हैं, तो Apache POI वेबसाइट से JAR फ़ाइलें डाउनलोड करें और उन्हें अपने प्रोजेक्ट के क्लासपाथ में जोड़ें।

---

### **Step 2: Basic Usage for Excel Files**
Apache POI Excel वर्कबुक, शीट, रows, और cells के साथ काम करने के लिए क्लास प्रदान करता है। यहाँ एक Excel फ़ाइलें पढ़ने और लिखने के लिए शुरू करने के लिए है।

#### **Reading an Excel File**
एक Excel फ़ाइल पढ़ने के लिए, आप `WorkbookFactory` का उपयोग करेंगे एक `Workbook` instance बनाना, फिर शीट, रows, और cells के माध्यम से नाविगेट करें।

यहाँ एक सरल उदाहरण है एक Excel फ़ाइल के सामग्री पढ़ने और प्रिंट करने के लिए:

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // आपकी Excel फ़ाइल के लिए पथ
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // सभी शीटों के माध्यम से लूप
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // रows और cells के माध्यम से लूप
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // प्रत्येक row के बाद नया लाइन
                }
                System.out.println(); // प्रत्येक शीट के बाद नया लाइन
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**मुख्य बिंदु**:
- `WorkbookFactory.create()` दोनों .xls (HSSF) और .xlsx (XSSF) फ़ाइलों के साथ काम करता है।
- `DataFormatter` विभिन्न cell प्रकारों (strings, numbers, dates) को string के रूप में फॉर्मेट करने से सरल बनाता है।
- `try-with-resources` का उपयोग करें फ़ाइल और workbook को स्वचालित रूप से बंद करने के लिए।

#### **Handling Different Cell Types**
अगर आपको cell values को उनके प्रकार (e.g., string, number, date) के आधार पर प्रोसेस करने की आवश्यकता है, तो cell प्रकार को स्पष्ट रूप से जांचें:

```java
Cell cell = row.getCell(0); // एक row में पहला cell
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
        System.out.println("अज्ञात cell प्रकार");
}
```

#### **Writing to an Excel File**
एक Excel फ़ाइल बनाना या संशोधित करना, आप एक workbook बनाएँगी, शीट, रows, और cells जोड़ें, फिर इसे save करें।

यहाँ एक नया .xlsx फ़ाइल बनाने के लिए एक उदाहरण है:

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // पहला row
            Cell cell = row.createCell(0); // पहला cell
            cell.setCellValue("Hello, POI!");

            // फ़ाइल में लिखें
            try (FileOutputStream fos = new FileOutputStream("output.xlsx")) {
                workbook.write(fos);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**मुख्य बिंदु**:
- .xlsx फ़ाइलों के लिए `XSSFWorkbook` का उपयोग करें या .xls फ़ाइलों के लिए `HSSFWorkbook` का उपयोग करें।
- `workbook.write()` को फ़ाइल को save करने के लिए call करें।

---

### **Step 3: Key Classes and Concepts**
यहाँ Apache POI के लिए Excel के लिए आप मुख्य क्लासों का उपयोग करेंगे:

- **`Workbook`**: पूरे Excel फ़ाइल का प्रतिनिधित्व करता है (`XSSFWorkbook` के लिए .xlsx, `HSSFWorkbook` के लिए .xls).
- **`Sheet`**: एक workbook में एक शीट.
- **`Row`**: एक शीट में एक row.
- **`Cell`**: एक row में एक cell.
- **`WorkbookFactory`**: एक फ़ाइल या stream से एक workbook बनाता है, दोनों फ़ाइल प्रकारों का समर्थन करता है।
- **`DataFormatter`**: cell values को strings के रूप में फॉर्मेट करता है.
- **`DateUtil`**: date-formatted numeric cells को पहचानने और संभालने में मदद करता है।

अन्य फ़ॉर्मेट्स के लिए:
- **Word**: `XWPFDocument` (.docx) या `HWPFDocument` (.doc) का उपयोग करें.
- **PowerPoint**: `XMLSlideShow` (.pptx) या `HSLFSlideShow` (.ppt) का उपयोग करें।

---

### **Step 4: Tips and Best Practices**
- **Resource Management**: हमेशा `try-with-resources` का उपयोग करें फ़ाइलें और workbooks को बंद करने के लिए, memory leaks को रोकने के लिए।
- **Error Handling**: फ़ाइल ऑपरेशन के लिए `IOException` को catch करें और index द्वारा रows/cells को एक्सेस करने के समय null रows/cells की जांच करें (e.g., `sheet.getRow(i)` null return कर सकता है).
- **Large Files**: बड़े Excel फ़ाइलों के लिए, streaming API (`SXSSFWorkbook` लिखने के लिए, `XSSFSheetXMLHandler` पढ़ने के लिए) का विचार करें memory usage को कम करने के लिए.
- **Compatibility**: POI may not support all features of the latest Office formats—check the [official documentation](https://poi.apache.org/) for details.

---

### **Summary**
`org.apache.poi` का उपयोग करने के लिए:
1. लाइब्रेरी को अपने प्रोजेक्ट में जोड़ें (e.g., via Maven).
2. `WorkbookFactory` का उपयोग करें मौजूदा फ़ाइलें पढ़ने के लिए या `XSSFWorkbook`/`HSSFWorkbook` के साथ नए workbooks बनाएं.
3. `Sheet`, `Row`, और `Cell` objects के माध्यम से data को एक्सेस और संशोधित करें.
4. फ़ाइल में लिखने के द्वारा बदलावों को save करें.
5. अपवादों को संभालें और resources को सही तरीके से बंद करें।

यह Apache POI के बारे में बुनियादी बातें कवर करता है, Excel फ़ाइलों पर ध्यान केंद्रित करते हुए। अगर आपके पास कोई विशेष कार्य था (e.g., Word या PowerPoint के साथ काम करना), तो मुझे बताएं, और मैं व्याख्या को और अधिक अनुकूलित कर सकता हूँ!