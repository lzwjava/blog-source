---
audio: false
generated: true
lang: hi
layout: post
title: जावा में एक्सएमएल का उपयोग
translated: true
type: note
---

Java में XML का उपयोग आप कई तरीकों से कर सकते हैं, यह इस बात पर निर्भर करता है कि आप क्या हासिल करना चाहते हैं—XML डेटा को पार्स करना, बनाना, या उसमें हेरफेर करना। यहां कुछ सामान्य तरीकों से शुरुआत करने के लिए एक संक्षिप्त मार्गदर्शिका दी गई है:

### 1. **DOM (Document Object Model) के साथ XML पार्सिंग**
यदि आप XML को मेमोरी में एक ट्री स्ट्रक्चर के रूप में पढ़ना और उसमें हेरफेर करना चाहते हैं, तो DOM API एक अच्छा विकल्प है।

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // XML फ़ाइल लोड और पार्स करें
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // XML स्ट्रक्चर को नॉर्मलाइज़ करें
            doc.getDocumentElement().normalize();

            // एलिमेंट्स तक पहुंचें (उदाहरण के लिए, सभी "item" टैग)
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

- **फायदे**: XML स्ट्रक्चर में नेविगेट और मॉडिफाई करना आसान।
- **नुकसान**: बड़ी फाइलों के लिए मेमोरी इंटेंसिव।

---

### 2. **SAX (Simple API for XML) के साथ XML पार्सिंग**
बड़ी XML फाइलों के लिए जहां मेमोरी एफिशिएंसी मायने रखती है, SAX इवेंट-ड्रिवन है और पूरी फाइल को मेमोरी में लोड नहीं करता है।

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

- **फायदे**: बड़ी फाइलों के लिए हल्का और तेज़।
- **नुकसान**: रैंडम एक्सेस नहीं; आप इसे सीक्वेंशियली प्रोसेस करते हैं।

---

### 3. **DOM के साथ XML बनाना**
स्क्रैच से XML जनरेट करने के लिए:

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

            // रूट एलिमेंट
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // चाइल्ड एलिमेंट
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // फ़ाइल में सेव करें
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

यह पहले दिखाए गए स्ट्रक्चर के साथ एक `output.xml` फाइल बनाता है।

---

### 4. **JAXB (Java Architecture for XML Binding) का उपयोग करना**
यदि आप ऐसे XML के साथ काम कर रहे हैं जो Java ऑब्जेक्ट्स से मैप होता है (जैसे, सीरियलाइज़ेशन/डी-सीरियलाइज़ेशन), तो JAXB एक हायर-लेवल विकल्प है। आपको एनोटेशन के साथ एक क्लास डिफाइन करनी होगी।

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
            // मार्शलिंग (Java से XML)
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // अनमार्शलिंग (XML से Java)
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Loaded item: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **फायदे**: XML-टू-ऑब्जेक्ट मैपिंग को सरल बनाता है।
- **नुकसान**: एनोटेटेड क्लासेज की आवश्यकता होती है और यह कॉम्प्लेक्स, इरेगुलर XML के लिए आदर्श नहीं है।

---

### शुरुआत कैसे करें
- **डिपेंडेंसीज़**: इन उदाहरणों में Java की बिल्ट-इन लाइब्रेरीज़ (जैसे `javax.xml.parsers`) का उपयोग किया गया है, इसलिए DOM या SAX के लिए किसी बाहरी डिपेंडेंसी की आवश्यकता नहीं है। JAXB के लिए, सुनिश्चित करें कि आप Java का ऐसा वर्जन उपयोग कर रहे हैं जिसमें यह शामिल हो (Java 9 से पहले) या यदि नए वर्जन का उपयोग कर रहे हैं तो इसे Maven/Gradle के माध्यम से एड करें।
- **फ़ाइल**: `"example.xml"` या `"output.xml"` को अपनी वास्तविक फाइल पाथ से रिप्लेस करें।

कौन सा तरीका आपके लिए उपयुक्त है, यह आपकी जरूरतों पर निर्भर करता है—फ्लेक्सिबिलिटी के लिए DOM, एफिशिएंसी के लिए SAX, या ऑब्जेक्ट मैपिंग के लिए JAXB। क्या आप इनमें से किसी एक के बारे में और गहराई से जानना चाहेंगे?