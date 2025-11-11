---
audio: false
generated: true
lang: fr
layout: post
title: Utilisation de XML en Java
translated: true
type: note
---

L'utilisation de XML en Java peut se faire de plusieurs manières selon ce que vous souhaitez accomplir—parser, créer ou manipuler des données XML. Voici un guide concis pour commencer avec quelques approches courantes :

### 1. **Parser du XML avec DOM (Document Object Model)**
Si vous voulez lire et manipuler le XML comme une structure arborescente en mémoire, l'API DOM est un bon choix.

```java
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class XMLParser {
    public static void main(String[] args) {
        try {
            // Charger et parser le fichier XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse("example.xml");

            // Normaliser la structure XML
            doc.getDocumentElement().normalize();

            // Accéder aux éléments (par ex., tous les tags "item")
            NodeList list = doc.getElementsByTagName("item");
            for (int i = 0; i < list.getLength(); i++) {
                Element element = (Element) list.item(i);
                System.out.println("Élément : " + element.getNodeName());
                System.out.println("Valeur : " + element.getTextContent());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**Exemple XML (example.xml) :**
```xml
<root>
    <item>Item 1</item>
    <item>Item 2</item>
</root>
```

- **Avantages** : Facile à naviguer et à modifier la structure XML.
- **Inconvénients** : Consomme beaucoup de mémoire pour les gros fichiers.

---

### 2. **Parser du XML avec SAX (Simple API for XML)**
Pour les gros fichiers XML où l'efficacité mémoire est importante, SAX est événementiel et ne charge pas tout le fichier en mémoire.

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
                        System.out.println("Item : " + new String(ch, start, length));
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

- **Avantages** : Léger et rapide pour les gros fichiers.
- **Inconvénients** : Pas d'accès aléatoire ; vous le traitez séquentiellement.

---

### 3. **Créer du XML avec DOM**
Pour générer du XML à partir de zéro :

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

            // Élément racine
            Element root = doc.createElement("root");
            doc.appendChild(root);

            // Élément enfant
            Element item = doc.createElement("item");
            item.appendChild(doc.createTextNode("Item 1"));
            root.appendChild(item);

            // Sauvegarder dans un fichier
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult("output.xml");
            transformer.transform(source, result);

            System.out.println("Fichier XML créé !");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

Ceci crée un fichier `output.xml` avec la structure montrée précédemment.

---

### 4. **Utiliser JAXB (Java Architecture for XML Binding)**
Si vous travaillez avec du XML qui correspond à des objets Java (par ex., sérialisation/désérialisation), JAXB est une option de plus haut niveau. Vous devrez définir une classe avec des annotations.

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
            // Marshalling (Java vers XML)
            JAXBContext context = JAXBContext.newInstance(Item.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            Item item = new Item();
            item.setName("Item 1");
            marshaller.marshal(item, new File("item.xml"));

            // Unmarshalling (XML vers Java)
            Unmarshaller unmarshaller = context.createUnmarshaller();
            Item loadedItem = (Item) unmarshaller.unmarshal(new File("item.xml"));
            System.out.println("Item chargé : " + loadedItem.getName());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- **Avantages** : Simplifie le mapping XML-objet.
- **Inconvénients** : Nécessite des classes annotées et n'est pas idéal pour du XML complexe et irrégulier.

---

### Pour Commencer
- **Dépendances** : Ces exemples utilisent les bibliothèques intégrées à Java (comme `javax.xml.parsers`), donc aucune dépendance externe n'est nécessaire pour DOM ou SAX. Pour JAXB, assurez-vous d'utiliser une version de Java qui l'inclut (pré-Java 9) ou ajoutez-le via Maven/Gradle si vous utilisez une version plus récente.
- **Fichier** : Remplacez `"example.xml"` ou `"output.xml"` par vos chemins de fichier réels.

L'approche qui vous convient dépend de vos besoins—DOM pour la flexibilité, SAX pour l'efficacité, ou JAXB pour le mapping objet. Vous voulez que j'approfondisse l'une d'entre elles ?