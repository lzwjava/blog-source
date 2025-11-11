---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるXMLの利用
translated: true
type: note
---

JavaでXMLを扱うには、解析、作成、操作など目的に応じて様々な方法があります。主なアプローチを紹介します：

### 1. **DOM（Document Object Model）によるXML解析**
メモリ内でXMLをツリー構造として読み取り操作したい場合、DOM APIが適しています。

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // XMLファイルの読み込みと解析
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // XML構造の正規化
            doc.getDocumentElement().normalize();

            // 要素へのアクセス（例：すべての"item"タグ）
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

**XML例（example.xml）：**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **利点**: XML構造のナビゲートと変更が容易
- **欠点**: 大容量ファイルにはメモリを多く消費する

---

### 2. **SAX（Simple API for XML）による解析**
メモリ効率が重要な大容量XMLファイルの場合、SAXはイベント駆動型でファイル全体をメモリに読み込みません。

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

- **利点**: 軽量で大容量ファイルの処理が高速
- **欠点**: ランダムアクセス不可、順次処理のみ

---

### 3. **DOMによるXML作成**
ゼロからXMLを生成する場合：

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

            // ルート要素
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // 子要素
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // ファイル保存
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

これにより前述の構造を持つ`output.xml`ファイルが作成されます。

---

### 4. **JAXB（Java Architecture for XML Binding）の使用**
Javaオブジェクトとのマッピング（シリアライズ/デシリアライズ）を行う場合、JAXBは高レベルな選択肢です。アノテーション付きクラスを定義する必要があります。

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
            // マーシャリング（JavaからXMLへ）
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // アンマーシャリング（XMLからJavaへ）
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Loaded item: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **利点**: XMLとオブジェクトのマッピングを簡素化
- **欠点**: アノテーション付きクラスが必要、複雑な不規則なXMLには不向き

---

### はじめに
- **依存関係**: これらの例はJava組み込みライブラリ（`javax.xml.parsers`など）を使用しているため、DOMやSAXには外部依存関係は不要です。JAXBについては、含まれているJavaバージョン（Java 9以前）を使用するか、新しいバージョンではMaven/Gradle経由で追加してください。
- **ファイル**: `"example.xml"`や`"output.xml"`は実際のファイルパスに置き換えてください。

どのアプローチを選ぶかは要件によります - 柔軟性ならDOM、効率性ならSAX、オブジェクトマッピングならJAXBです。どれか詳しく知りたいですか？