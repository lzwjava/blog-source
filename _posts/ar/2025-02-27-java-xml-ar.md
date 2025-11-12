---
audio: false
generated: true
lang: ar
layout: post
title: استخدام XML في جافا
translated: true
type: note
---

يمكن استخدام XML في جافا بعدة طرق اعتمادًا على ما تريد تحقيقه - تحليل، إنشاء، أو معالجة بيانات XML. إليك دليل موجز لبدء استخدام بعض الأساليب الشائعة:

### 1. **تحليل XML باستخدام DOM (نموذج كائن المستند)**
إذا كنت تريد قراءة ومعالجة XML كبنية شجرية في الذاكرة، فإن واجهة برمجة تطبيقات DOM خيار جيد.

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

            // تطبيع بنية XML
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

**XML مثال (example.xml):**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **الإيجابيات**: سهل التنقل والتعديل في بنية XML.
- **السلبيات**: يستهلك الكثير من الذاكرة للملفات الكبيرة.

---

### 2. **تحليل XML باستخدام SAX (واجهة برمجة تطبيقات XML البسيطة)**
للملفات XML الكبيرة حيث تكون كفاءة الذاكرة مهمة، SAX يعتمد على الأحداث ولا يحمل الملف بالكامل في الذاكرة.

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

- **الإيجابيات**: خفيف الوزن وسريع للملفات الكبيرة.
- **السلبيات**: لا يوفر وصولاً عشوائيًا؛ تقوم بمعالجته بشكل تسلسلي.

---

### 3. **إنشاء XML باستخدام DOM**
لتوليد XML من الصفر:

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

            // الحفظ في ملف
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("XML file created!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

هذا ينشئ ملف `output.xml` بالبنية الموضحة سابقًا.

---

### 4. **استخدام JAXB (هندسة ربط XML لجافا)**
إذا كنت تعمل مع XML يتم تعيينه إلى كائنات جافا (مثل التسلسل/إلغاء التسلسل)، فإن JAXB خيار عالي المستوى. ستحتاج إلى تعريف فئة مع شرح annotations.

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
            // Marshalling (من جافا إلى XML)
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // Unmarshalling (من XML إلى جافا)
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Loaded item: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **الإيجابيات**: يبسط تعيين XML إلى كائن.
- **السلبيات**: يتطلب فئات مشروحة بـ annotations وليس مثاليًا لـ XML معقد وغير منتظم.

---

### البدء
- **التبعيات**: هذه الأمثلة تستخدم مكتبات جافا المدمجة (مثل `javax.xml.parsers`)، لذا لا حاجة لتبعيات خارجية لـ DOM أو SAX. بالنسبة لـ JAXB، تأكد من استخدام إصدار جافا الذي يتضمنه (ما قبل جافا 9) أو أضفه عبر Maven/Gradle إذا كنت تستخدم إصدارًا أحدث.
- **الملف**: استبدل `"example.xml"` أو `"output.xml"` بمسارات الملفات الفعلية الخاصة بك.

الأسلوب الذي يناسبك يعتمد على احتياجاتك - DOM للمرونة، SAX للكفاءة، أو JAXB لتعيين الكائنات. هل تريد مني الخوض بشكل أعمق في أي من هذه؟