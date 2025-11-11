---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中使用 XML
translated: true
type: note
---

在 Java 中使用 XML 可透過多種方式實現，具體取決於你的目標——解析、建立或操作 XML 資料。以下簡明指南將介紹幾種常見方法助你入門：

### 1. **使用 DOM（文件物件模型）解析 XML**
若需將 XML 作為樹狀結構在記憶體中讀取和操作，DOM API 是個不錯的選擇。

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // 載入並解析 XML 檔案
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // 正規化 XML 結構
            doc.getDocumentElement().normalize();

            // 存取元素（例如所有 "item" 標籤）
            NodeList list = doc.getElementsByTagName("item");
            for (int i = 0; i < list.getLength(); i++) {
                Element element = (Element) list.item(i);
                System.out.println("元素: " + element.getNodeName());
                System.out.println("數值: " + element.getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**範例 XML (example.xml)：**
```xml
<root>
    <item>項目 1</item>
    <item>項目 2</item>
</root>
```

- **優點**：便於導覽和修改 XML 結構
- **缺點**：處理大型檔案時記憶體消耗較高

---

### 2. **使用 SAX（簡易 XML 處理 API）解析 XML**
針對記憶體效率至關重要的大型 XML 檔案，SAX 採用事件驅動模式，不會將整個檔案載入記憶體。

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
                        System.out.println("項目: " + new String(ch, start, length));
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

- **優點**：輕量級，處理大型檔案速度快
- **缺點**：無法隨機存取，只能順序處理

---

### 3. **使用 DOM 建立 XML**
從零開始生成 XML：

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

            // 根元素
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // 子元素
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("項目 1"));
            root.appendChild(item);

            // 儲存至檔案
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("XML 檔案已建立！");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

此程式會建立具有前述結構的 `output.xml` 檔案。

---

### 4. **使用 JAXB（Java XML 綁定架構）**
若需處理與 Java 物件對映的 XML（例如序列化/反序列化），JAXB 是更高階的選擇。你需要定義帶有註解的類別。

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
            // 封送處理（Java 轉 XML）
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("項目 1");
            marshaller.marshal(item, new File("item.xml"));

            // 解封送處理（XML 轉 Java）
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("已載入項目: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **優點**：簡化 XML 與物件的對映
- **缺點**：需要註解類別，不適用於複雜不規則的 XML 結構

---

### 入門指引
- **相依性**：這些範例使用 Java 內建函式庫（如 `javax.xml.parsers`），因此 DOM 或 SAX 無需外部相依性。對於 JAXB，請確保使用內含該模組的 Java 版本（Java 9 之前），若使用較新版本可透過 Maven/Gradle 添加
- **檔案路徑**：請將 `"example.xml"` 或 `"output.xml"` 替換為實際檔案路徑

選擇合適方法需視需求而定——DOM 適合靈活操作，SAX 注重效率，JAXB 則專精於物件對映。需要我更深入說明任何方法嗎？