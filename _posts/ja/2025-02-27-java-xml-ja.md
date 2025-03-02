---
audio: false
generated: false
lang: ja
layout: post
title: XMLをJavaで使用する
translated: true
---

JavaでXMLを使用する方法は、目的によって異なります。XMLデータを解析、作成、または操作するためのいくつかの一般的なアプローチを始めるための簡潔なガイドです。

### 1. **DOM（Document Object Model）を使用したXMLの解析**
XMLをメモリ内のツリー構造として読み取り、操作したい場合、DOM APIは良い選択です。

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // XMLファイルを読み込み、解析
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // XML構造を正規化
            doc.getDocumentElement().normalize();

            // 要素にアクセス（例：すべての「item」タグ）
            NodeList list = doc.getElementsByTagName("item");
            for (int i = 0; i < list.getLength(); i++) {
                Element element = (Element) list.item(i);
                System.out.println("要素: " + element.getNodeName());
                System.out.println("値: " + element.getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**例XML（example.xml）:**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **メリット**: XML構造のナビゲーションと修正が容易です。
- **デメリット**: 大きなファイルではメモリを多く消費します。

---

### 2. **SAX（Simple API for XML）を使用したXMLの解析**
メモリ効率が重要な大きなXMLファイルでは、SAXはイベント駆動型であり、ファイル全体をメモリに読み込みません。

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
                        System.out.println("アイテム: " + new String(ch, start, length));
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

- **メリット**: 大きなファイルでは軽量で高速です。
- **デメリット**: ランダムアクセスができず、順次処理します。

---

### 3. **DOMを使用したXMLの作成**
XMLをゼロから生成するには：

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

            // ファイルに保存
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("XMLファイルが作成されました！");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

これにより、先ほど示した構造の `output.xml` ファイルが作成されます。

---

### 4. **JAXB（Java Architecture for XML Binding）の使用**
JavaオブジェクトにマッピングされるXML（例：シリアライズ/デシリアライズ）を扱う場合、JAXBは高レベルのオプションです。アノテーション付きのクラスを定義する必要があります。

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
            // マーシャル（JavaからXML）
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // アンマーシャル（XMLからJava）
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("読み込まれたアイテム: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **メリット**: XML-to-objectマッピングを簡素化します。
- **デメリット**: アノテーション付きのクラスが必要で、複雑で不規則なXMLには適していません。

---

### 開始
- **依存関係**: これらの例はJavaの組み込みライブラリ（例：`javax.xml.parsers`）を使用しているため、DOMやSAXには外部の依存関係は必要ありません。JAXBの場合は、Java 9以前のバージョンを使用しているか、Maven/Gradleを使用して追加する必要があります。
- **ファイル**: `"example.xml"` または `"output.xml"` を実際のファイルパスに置き換えてください。

どのアプローチが適しているかは、DOMは柔軟性、SAXは効率、JAXBはオブジェクトマッピングに依存します。どれかに詳しく掘り下げますか？