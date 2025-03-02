---
audio: false
generated: false
lang: hi
layout: post
title: XML का उपयोग Java में
translated: true
---

XML को Java में कई तरीकों से उपयोग किया जा सकता है, जो आप क्या करना चाहते हैं, पर निर्भर करता है—XML डेटा को पढ़ना, बनाना, या संशोधित करना। यहाँ कुछ आम तरीकों के साथ शुरू करने के लिए एक संक्षिप्त मार्गदर्शन है:

### 1. **DOM (Document Object Model) के साथ XML पढ़ना**
अगर आप XML को मेमोरी में एक पेड़ संरचना के रूप में पढ़ना और संशोधित करना चाहते हैं, तो DOM API एक अच्छा विकल्प है।

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // XML फ़ाइल को लोड और पर्स करें
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // XML संरचना को सामान्यीकृत करें
            doc.getDocumentElement().normalize();

            // तत्वों तक पहुंचें (उदाहरण के लिए, सभी "item" टैग)
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

**उदाहरण XML (example.xml):**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **फायदे**: XML संरचना को नाविगेट और संशोधित करना आसान है।
- **नुकसान**: बड़े फ़ाइलों के लिए मेमोरी-इंटेंसिव है।

---

### 2. **SAX (Simple API for XML) के साथ XML पढ़ना**
बड़े XML फ़ाइलों के लिए जहां मेमोरी दक्षता का महत्व है, SAX इवेंट-ड्राइव है और पूरा फ़ाइल मेमोरी में लोड नहीं करता है।

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

- **फायदे**: बड़े फ़ाइलों के लिए हल्का और तेज़ है।
- **नुकसान**: कोई रैंडम एक्सेस नहीं; आप इसे अनुक्रमिक रूप से प्रोसेस करते हैं।

---

### 3. **DOM के साथ XML बनाना**
नया XML से बनाना:

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

            // मूल तत्व
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // बच्चा तत्व
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // फ़ाइल में सहेजें
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("XML फ़ाइल बनाया गया!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

यह एक `output.xml` फ़ाइल बनाता है जिसका संरचना पहले दिखाया गया है।

---

### 4. **JAXB (Java Architecture for XML Binding) का उपयोग**
अगर आप Java ऑब्जेक्ट्स (उदाहरण के लिए, सीरियलाइज़ेशन/डिसीरियलाइज़ेशन) के साथ काम कर रहे हैं, तो JAXB एक उच्च स्तर का विकल्प है। आपको एक अनोटेशन के साथ वर्ग परिभाषित करना होगा।

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
            // Marshalling (Java to XML)
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // Unmarshalling (XML to Java)
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Loaded item: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **फायदे**: XML-to-object मापिंग को सरल बनाता है।
- **नुकसान**: अनोटेशन वाले वर्गों की आवश्यकता होती है और जटिल, अनियमित XML के लिए नहीं है।

---

### शुरू करना
- **Dependencies**: इन उदाहरणों में Java के बिल्ट-इन लाइब्रेरी (जैसे `javax.xml.parsers`) का उपयोग किया जाता है, इसलिए DOM या SAX के लिए कोई बाहरी dependencies की आवश्यकता नहीं है। JAXB के लिए, सुनिश्चित करें कि आप एक Java संस्करण का उपयोग कर रहे हैं जो इसे शामिल करता है (pre-Java 9) या अगर आप नए संस्करण का उपयोग कर रहे हैं तो Maven/Gradle के माध्यम से इसे जोड़ें।
- **फ़ाइल**: `"example.xml"` या `"output.xml"` को आपकी वास्तविक फ़ाइल पथों से बदलें।

आपके जरूरतों पर निर्भर करता है कि कौन-सा तरीका आपको उपयुक्त लगता है—DOM के लिए लचीलापन, SAX के लिए दक्षता, या JAXB के लिए ऑब्जेक्ट मापिंग। मुझे किसी भी में गहरे उतरने की आवश्यकता है?