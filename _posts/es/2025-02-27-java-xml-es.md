---
audio: false
generated: true
lang: es
layout: post
title: Uso de XML en Java
translated: true
type: note
---

El uso de XML en Java se puede realizar de varias maneras dependiendo de lo que quieras lograr: analizar, crear o manipular datos XML. Aquí tienes una guía concisa para comenzar con algunos enfoques comunes:

### 1. **Analizar XML con DOM (Document Object Model)**
Si quieres leer y manipular XML como una estructura de árbol en memoria, la API DOM es una buena opción.

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // Cargar y analizar el archivo XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // Normalizar la estructura XML
            doc.getDocumentElement().normalize();

            // Acceder a elementos (por ejemplo, todas las etiquetas "item")
            NodeList list = doc.getElementsByTagName("item");
            for (int i = 0; i < list.getLength(); i++) {
                Element element = (Element) list.item(i);
                System.out.println("Elemento: " + element.getNodeName());
                System.out.println("Valor: " + element.getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**XML de ejemplo (example.xml):**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **Ventajas**: Fácil de navegar y modificar la estructura XML.
- **Desventajas**: Intensivo en memoria para archivos grandes.

---

### 2. **Analizar XML con SAX (Simple API for XML)**
Para archivos XML grandes donde la eficiencia de memoria es importante, SAX es dirigido por eventos y no carga todo el archivo en memoria.

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

- **Ventajas**: Ligero y rápido para archivos grandes.
- **Desventajas**: No hay acceso aleatorio; lo procesas secuencialmente.

---

### 3. **Crear XML con DOM**
Para generar XML desde cero:

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

            // Elemento raíz
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // Elemento hijo
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // Guardar en archivo
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("¡Archivo XML creado!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

Esto crea un archivo `output.xml` con la estructura mostrada anteriormente.

---

### 4. **Usar JAXB (Java Architecture for XML Binding)**
Si trabajas con XML que se asigna a objetos Java (por ejemplo, serialización/deserialización), JAXB es una opción de más alto nivel. Necesitarás definir una clase con anotaciones.

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
            // Marshalling (Java a XML)
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // Unmarshalling (XML a Java)
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Item cargado: " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **Ventajas**: Simplifica el mapeo de XML a objetos.
- **Desventajas**: Requiere clases anotadas y no es ideal para XML complejo o irregular.

---

### Para Comenzar
- **Dependencias**: Estos ejemplos usan las bibliotecas integradas de Java (como `javax.xml.parsers`), por lo que no se necesitan dependencias externas para DOM o SAX. Para JAXB, asegúrate de usar una versión de Java que lo incluya (pre-Java 9) o agrégalo vía Maven/Gradle si usas una versión más nueva.
- **Archivo**: Reemplaza `"example.xml"` o `"output.xml"` con tus rutas de archivo reales.

El enfoque que te conviene depende de tus necesidades: DOM para flexibilidad, SAX para eficiencia o JAXB para mapeo de objetos. ¿Quieres que profundice más en alguno de estos?