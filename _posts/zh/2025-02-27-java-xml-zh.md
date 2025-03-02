---
audio: false
generated: false
lang: zh
layout: post
title: 使用 XML 于 Java
translated: true
---

在 Java 中使用 XML 可以通过多种方式实现，具体取决于你想要实现的目标——解析、创建或操作 XML 数据。以下是一个简明的指南，帮助你开始使用一些常见的方法：

### 1. **使用 DOM（文档对象模型）解析 XML**
如果你想将 XML 读取和操作为内存中的树结构，DOM API 是一个不错的选择。

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // 加载并解析 XML 文件
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // 规范化 XML 结构
            doc.getDocumentElement().normalize();

            // 访问元素（例如，所有的 "item" 标签）
            NodeList list = doc.getElementsByTagName("item");
            for (int i = 0; i < list.getLength(); i++) {
                Element element = (Element) list.item(i);
                System.out.println("元素: " + element.getNodeName());
                System.out.println("值: " + element.getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**示例 XML（example.xml）:**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **优点**: 易于导航和修改 XML 结构。
- **缺点**: 对于大文件来说内存消耗大。

---

### 2. **使用 SAX（简单 API 为 XML）解析 XML**
对于大 XML 文件，内存效率很重要，SAX 是事件驱动的，不会将整个文件加载到内存中。

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

- **优点**: 对于大文件来说轻量级且快速。
- **缺点**: 无法随机访问；你需要按顺序处理它。

---

### 3. **使用 DOM 创建 XML**
从头开始生成 XML：

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
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // 保存到文件
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("XML 文件创建成功！");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

这将创建一个 `output.xml` 文件，结构如上所示。

---

### 4. **使用 JAXB（Java 架构为 XML 绑定）**
如果你在处理映射到 Java 对象的 XML（例如序列化/反序列化），JAXB 是一个更高级的选项。你需要定义一个带有注解的类。

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
            // 将 Java 对象转换为 XML（序列化）
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // 将 XML 转换为 Java 对象（反序列化）
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("加载的项: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **优点**: 简化了 XML 到对象的映射。
- **缺点**: 需要带有注解的类，对于复杂、不规则的 XML 并不理想。

---

### 入门
- **依赖项**: 这些示例使用了 Java 的内置库（如 `javax.xml.parsers`），因此对于 DOM 或 SAX 不需要外部依赖。对于 JAXB，确保你使用的是包含它的 Java 版本（Java 9 之前），或者通过 Maven/Gradle 添加它（如果使用较新版本）。
- **文件**: 将 `"example.xml"` 或 `"output.xml"` 替换为你的实际文件路径。

哪种方法适合你取决于你的需求——DOM 适用于灵活性，SAX 适用于效率，JAXB 适用于对象映射。想要深入了解其中任何一种吗？