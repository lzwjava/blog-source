---
audio: false
lang: ar
layout: post
title: استخدام XML في جاڤا
translated: true
---

استخدام XML في Java يمكن أن يتم على عدة طرق اعتمادًا على ما تريد تحقيقه - تحليل، إنشاء أو تعديل بيانات XML. إليك دليل مختصر للحصول على بداية جيدة مع بعض الطرق الشائعة:

### 1. **تحليل XML باستخدام DOM (Document Object Model)**
إذا كنت تريد قراءة وتعديل XML كهيكل شجرة في الذاكرة، فإن API DOM هو خيار جيد.

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // تحميل وتحليل ملف XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // تنسيق هيكل XML
            doc.getDocumentElement().normalize();

            // الوصول إلى العناصر (مثل جميع علامات "item")
            NodeList list = doc.getElementsByTagName("item");
            for (int i = 0; i < list.getLength(); i++) {
                Element element = (Element) list.item(i);
                System.out.println("Element: " + element.getNodeName());
                System.out.println("Value: " + element.getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**مثال XML (example.xml):**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **المزايا**: سهولة التنقل والتعديل في هيكل XML.
- **العيوب**: كثافة الذاكرة للملفات الكبيرة.

---

### 2. **تحليل XML باستخدام SAX (Simple API for XML)**
للملفات XML الكبيرة حيث تكون كفاءة الذاكرة مهمة، فإن SAX هو موجه الأحداث ولا يحمل الملف بأكمله إلى الذاكرة.

```java
import org.xml.sax.Attributes;
import org.xml.sax.helpers.DefaultHandler;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

public class SAXExample {
    public static void main(String[] args) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser saxParser = factory.newSAXParser();

            DefaultHandler handler = new DefaultHandler() {
                boolean inItem = false;

                @Override
                public void startElement(String uri, String localName, String qName, Attributes attributes) {
                    if (qName.equalsIgnoreCase("item")) {
                        inItem = true;
                    }
                }

                @Override
                public void characters(char[] ch, int start, int length) {
                    if (inItem) {
                        System.out.println("Item: " + new String(ch, start, length));
                        inItem = false;
                    }
                }
            };

            saxParser.parse("example.xml", handler);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **المزايا**: خفيف الوزن وسريع للملفات الكبيرة.
- **العيوب**: لا يوجد وصول عشوائي؛ يتم معالجة الملف تسلسليًا.

---

### 3. **إنشاء XML باستخدام DOM**
لإنشاء XML من الصفر:

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

public class XMLCreator {
    public static void main(String[] args) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            // العنصر الجذر
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // العنصر الفرعي
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // حفظ في ملف
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("تم إنشاء ملف XML!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

هذا يخلق ملف `output.xml` مع الهيكل الذي تم عرضه سابقًا.

---

### 4. **استخدام JAXB (Java Architecture for XML Binding)**
إذا كنت تعمل مع XML الذي يتم مابته إلى كائنات Java (مثل التسلسل/الترميز)، فإن JAXB هو خيار أعلى المستوى. عليك تعريف فئة مع تعليقات.

```java
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
class Item {
    private String name;

    @XmlElement
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}

import javax.xml.bind.JAXBContext;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
import java.io.File;

public class JAXBExample {
    public static void main(String[] args) {
        try {
            // التسلسل (Java إلى XML)
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // الترميز (XML إلى Java)
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Loaded item: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **المزايا**: يسهل ماب XML إلى كائن.
- **العيوب**: يتطلب فئات مع تعليقات ولا يكون مثاليًا للملفات XML المعقدة غير المنتظمة.

---

### البدء
- **التعليقات**: تستخدم هذه الأمثلة مكتبات Java المضمنة (مثل `javax.xml.parsers`)، لذا لا تحتاج إلى تعليقات خارجية لDOM أو SAX. بالنسبة إلى JAXB، تأكد من استخدام نسخة Java تتضمنها (قبل Java 9) أو أضيفها عبر Maven/Gradle إذا كنت تستخدم نسخة أحدث.
- **الملف**: استبدل `"example.xml"` أو `"output.xml"` بمسارات ملفاتك الفعلية.

تحدد الطريقة التي تناسبك اعتمادًا على احتياجاتك - DOM لللمونة، SAX للفعالية، أو JAXB لماب الكائن. هل تريد أن أعمق في أي من هذه؟