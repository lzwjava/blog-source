---
audio: false
generated: true
lang: hi
layout: post
title: एपाचे पीओआई लाइब्रेरी
translated: true
type: note
---

ऐसा लगता है कि आपके क्वेरी "how to use com.apache.poi." में एक टाइपो हो सकता है। Java में, Apache POI का पैकेज नाम `org.apache.poi` से शुरू होता है, न कि `com.apache.poi` से, क्योंकि Apache प्रोजेक्ट आमतौर पर `org` डोमेन का उपयोग करते हैं। मैं मानकर चलूंगा कि आपका मतलब `org.apache.poi` था, जो Microsoft Office फ़ाइल फॉर्मेट जैसे Excel, Word, और PowerPoint के साथ काम करने के लिए एक लोकप्रिय Java लाइब्रेरी है। नीचे इसका उपयोग करने का एक गाइड दिया गया है, जो सबसे आम उपयोग के मामले पर केंद्रित है: Excel फाइलों को हैंडल करना।

---

### **Apache POI क्या है?**
Apache POI (Poor Obfuscation Implementation) एक Java लाइब्रेरी है जो आपको Microsoft Office दस्तावेज़ों को प्रोग्रामेटिक रूप से पढ़ने, लिखने और मैनिपुलेट करने की अनुमति देती है। इसका व्यापक रूप से Excel फ़ाइलों (.xls और .xlsx) के लिए उपयोग किया जाता है, लेकिन यह Word और PowerPoint फॉर्मेट को भी सपोर्ट करती है।

---

### **चरण 1: अपने प्रोजेक्ट में Apache POI जोड़ें**
Apache POI का उपयोग करने के लिए, आपको इसे अपने Java प्रोजेक्ट में शामिल करना होगा। यदि आप **Maven** का उपयोग कर रहे हैं, तो अपनी `pom.xml` फ़ाइल में निम्नलिखित डिपेंडेंसीज जोड़ें:

- बेसिक Excel सपोर्ट (दोनों .xls और .xlsx) के लिए:
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```

- विशेष रूप से .xlsx फ़ाइलों के लिए (अतिरिक्त OOXML सपोर्ट की आवश्यकता होती है):
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>
```

**नोट**: नवीनतम संस्करण के लिए [Apache POI वेबसाइट](https://poi.apache.org/) या Maven Central जांचें।

यदि आप Maven का उपयोग नहीं कर रहे हैं, तो Apache POI वेबसाइट से JAR फाइलें डाउनलोड करें और उन्हें अपने प्रोजेक्ट के classpath में जोड़ें।

---

### **चरण 2: Excel फ़ाइलों के लिए बेसिक उपयोग**
Apache POI Excel वर्कबुक, शीट, पंक्तियों और सेल के साथ काम करने के लिए क्लासेस प्रदान करता है। यहां Excel फाइलों को पढ़ने और लिखने के साथ शुरुआत करने का तरीका बताया गया है।

#### **एक Excel फाइल पढ़ना**
एक Excel फाइल को पढ़ने के लिए, आप एक `Workbook` इंस्टेंस बनाने के लिए `WorkbookFactory` का उपयोग करेंगे, फिर शीट, पंक्तियों और सेल के माध्यम से नेविगेट करेंगे।

यहां एक Excel फाइल की सामग्री को पढ़ने और प्रिंट करने का एक सरल उदाहरण दिया गया है:

```java
import org.apache.poi.ss.usermodel.*;
import java.io.FileInputStream;
import java.io.IOException;

public class ExcelReader {
    public static void main(String[] args) {
        String filePath = "example.xlsx"; // आपकी Excel फाइल का पथ
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            // सभी शीट के माध्यम से लूप करें
            for (int i = 0; i < workbook.getNumberOfSheets(); i++) {
                Sheet sheet = workbook.getSheetAt(i);
                System.out.println("Sheet: " + sheet.getSheetName());
                // पंक्तियों और सेल के माध्यम से लूप करें
                for (Row row : sheet) {
                    for (Cell cell : row) {
                        DataFormatter formatter = new DataFormatter();
                        String value = formatter.formatCellValue(cell);
                        System.out.print(value + "\t");
                    }
                    System.out.println(); // प्रत्येक पंक्ति के बाद नई लाइन
                }
                System.out.println(); // प्रत्येक शीट के बाद नई लाइन
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**मुख्य बिंदु**:
- `WorkbookFactory.create()` दोनों .xls (HSSF) और .xlsx (XSSF) फाइलों के साथ काम करता है।
- `DataFormatter` उन्हें स्ट्रिंग के रूप में फॉर्मेट करके विभिन्न सेल प्रकारों (स्ट्रिंग्स, नंबर, तिथियां) को हैंडल करना सरल बनाता है।
- फाइल और वर्कबुक को स्वचालित रूप से बंद करने के लिए `try-with-resources` का उपयोग करें।

#### **विभिन्न सेल प्रकारों को हैंडल करना**
यदि आपको उनके प्रकार (जैसे, स्ट्रिंग, नंबर, तिथि) के आधार पर सेल वैल्यू को प्रोसेस करने की आवश्यकता है, तो सेल प्रकार को स्पष्ट रूप से चेक करें:

```java
Cell cell = row.getCell(0); // एक पंक्ति में पहला सेल प्राप्त करें
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

#### **एक Excel फाइल में लिखना**
एक Excel फाइल बनाने या संशोधित करने के लिए, आप एक वर्कबुक बनाएंगे, शीट, पंक्तियां और सेल जोड़ेंगे, फिर इसे सेव करेंगे।

यहां एक नई .xlsx फाइल बनाने का एक उदाहरण दिया गया है:

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelWriter {
    public static void main(String[] args) {
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("MySheet");
            Row row = sheet.createRow(0); // पहली पंक्ति
            Cell cell = row.createCell(0); // पहला सेल
            cell.setCellValue("Hello, POI!");

            // फाइल में लिखें
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
- .xlsx फाइलों के लिए `XSSFWorkbook` या .xls फाइलों के लिए `HSSFWorkbook` का उपयोग करें।
- फाइल को सेव करने के लिए `workbook.write()` को कॉल करें।

---

### **चरण 3: मुख्य कक्षाएं और अवधारणाएं**
यहां Excel के लिए Apache POI में आपके द्वारा उपयोग की जाने वाली मुख्य कक्षाएं दी गई हैं:
- **`Workbook`**: संपूर्ण Excel फाइल का प्रतिनिधित्व करता है (.xlsx के लिए `XSSFWorkbook`, .xls के लिए `HSSFWorkbook`)।
- **`Sheet`**: वर्कबुक में एक एकल शीट।
- **`Row`**: एक शीट में एक पंक्ति।
- **`Cell`**: एक पंक्ति में एक सेल।
- **`WorkbookFactory`**: एक फाइल या स्ट्रीम से एक वर्कबुक बनाता है, दोनों फाइल प्रकारों को हैंडल करता है।
- **`DataFormatter`**: सेल वैल्यू को स्ट्रिंग के रूप में फॉर्मेट करता है।
- **`DateUtil`**: तिथि-फॉर्मेटेड न्यूमेरिक सेल की पहचान करने और हैंडल करने में मदद करता है।

अन्य फॉर्मेट के लिए:
- **Word**: `XWPFDocument` (.docx) या `HWPFDocument` (.doc) का उपयोग करें।
- **PowerPoint**: `XMLSlideShow` (.pptx) या `HSLFSlideShow` (.ppt) का उपयोग करें।

---

### **चरण 4: सुझाव और सर्वोत्तम अभ्यास**
- **संसाधन प्रबंधन**: मेमोरी लीक को रोकने के लिए फाइलों और वर्कबुक को बंद करने के लिए हमेशा `try-with-resources` का उपयोग करें।
- **त्रुटि प्रबंधन**: फाइल ऑपरेशन के लिए `IOException` को कैच करें और इंडेक्स द्वारा एक्सेस करते समय null पंक्तियों/सेल के लिए चेक करें (उदाहरण के लिए, `sheet.getRow(i)` null लौटा सकता है)।
- **बड़ी फाइलें**: बड़ी Excel फाइलों के लिए, मेमोरी उपयोग को कम करने के लिए स्ट्रीमिंग API (`SXSSFWorkbook` लिखने के लिए, `XSSFSheetXMLHandler` पढ़ने के लिए) पर विचार करें।
- **संगतता**: POI नवीनतम Office फॉर्मेट की सभी सुविधाओं का समर्थन नहीं कर सकता है—विवरण के लिए [आधिकारिक दस्तावेज़ीकरण](https://poi.apache.org/) जांचें।

---

### **सारांश**
`org.apache.poi` का उपयोग करने के लिए:
1. लाइब्रेरी को अपने प्रोजेक्ट में जोड़ें (उदाहरण के लिए, Maven के माध्यम से)।
2. मौजूदा फाइलों को पढ़ने के लिए `WorkbookFactory` का उपयोग करें या `XSSFWorkbook`/`HSSFWorkbook` के साथ नई वर्कबुक बनाएं।
3. `Sheet`, `Row`, और `Cell` ऑब्जेक्ट के माध्यम से डेटा तक पहुंचें और उसे मैनिपुलेट करें।
4. एक फाइल में लिखकर परिवर्तनों को सेव करें।
5. एक्सेप्शन को हैंडल करें और संसाधनों को ठीक से बंद करें।

यह Apache POI के उपयोग की मूल बातें कवर करता है, जिसमें Excel फाइलों पर ध्यान केंद्रित किया गया है। यदि आपके मन में कोई विशिष्ट कार्य था (जैसे, Word या PowerPoint के साथ काम करना), तो मुझे बताएं, और मैं स्पष्टीकरण को और अधिक विशिष्ट बना सकता हूं!