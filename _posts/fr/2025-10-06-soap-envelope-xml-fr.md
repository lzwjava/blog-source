---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Enveloppe SOAP XML expliquée
translated: true
type: note
---

### Qu'est-ce qu'une Envelope XML ?

Je pense que "envalop" est une faute de frappe pour "envelope", faisant référence à **l'Enveloppe SOAP** en XML. SOAP (Simple Object Access Protocol) est un protocole pour échanger des informations structurées dans les services web en utilisant XML. L'Enveloppe SOAP est l'élément racine d'un message SOAP, qui encapsule l'intégralité du message pour l'identifier comme un document SOAP. Elle garantit que le récepteur sait qu'il s'agit d'un message complet.

Une structure basique d'Enveloppe SOAP ressemble à ceci :

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- Optionnel : Métadonnées comme l'authentification -->
  </soap:Header>
  <soap:Body>
    <!-- Obligatoire : La charge utile / les données réelles -->
    <YourCustomElement>
      <Data>Une valeur</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

- **Envelope** : Définit le début/la fin du message et l'espace de noms.
- **Header** (optionnel) : Pour les informations hors corps du message, comme la sécurité ou le routage.
- **Body** (requis) : Contient les données de requête/réponse.

Ce format rend les messages SOAP autonomes et indépendants du transport (par exemple, via HTTP).

### Comment utiliser une Envelope SOAP XML en Java

Java prend nativement en charge SOAP via les bibliothèques **JAX-WS** (Java API for XML Web Services) et **SAAJ** (SOAP with Attachments API for Java), qui font partie du JDK (aucune dépendance externe n'est nécessaire pour les bases).

#### Étapes pour créer et envoyer un message SOAP :
1.  **Créer un message SOAP** : Utilisez `javax.xml.soap` pour construire l'enveloppe de manière programmatique.
2.  **Ajouter du contenu** : Remplissez le Body (et le Header si nécessaire).
3.  **Envoyer via HTTP** : Utilisez `HttpURLConnection` ou un client comme JAX-WS pour des appels de service web complets.

Voici un exemple Java simple pour créer une Enveloppe SOAP et l'afficher (vous pouvez l'étendre pour l'envoyer via HTTP) :

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // Créer une factory SOAP
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // Créer le message et l'enveloppe
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // Espace de noms pour SOAP (version 1.2)
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // Créer l'élément Body
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // Sauvegarder et afficher le message
        soapMessage.saveChanges();
        System.out.println("Enveloppe SOAP :");
        soapMessage.writeTo(System.out);
    }
}
```

- **Sortie** : Ceci génère un XML SOAP avec l'enveloppe, le corps et vos éléments personnalisés.
- **Pour l'envoyer** : Intégrez-le dans un client JAX-WS. Générez les stubs à partir d'un fichier WSDL en utilisant l'outil `wsimport` : `wsimport -keep YourService.wsdl`. Ensuite, utilisez les classes client générées pour invoquer les méthodes, ce qui gère automatiquement l'enveloppe.
- **Bibliothèques** : Pour une utilisation avancée, ajoutez Apache CXF ou Axis2 si nécessaire, mais restez sur le JDK pour la simplicité.

Exécutez ceci dans n'importe quel environnement Java (JDK 8+). Pour les services web complets, assurez-vous que votre projet gère les exceptions comme `SOAPException`.

### Est-ce que Finacle utilise l'Envelope (SOAP XML) ?

Oui, Finacle (le logiciel bancaire central d'Infosys) utilise largement les enveloppes SOAP XML pour l'intégration. Il expose des services web via SOAP over HTTP à travers la couche **Finacle Integrator**, permettant aux systèmes externes de communiquer en utilisant les protocoles SOAP standard. Cela inclut les interactions EJB et le middleware pour des services comme les requêtes de compte ou les transactions. Les APIs de Finacle suivent souvent les normes SOAP pour une messagerie sécurisée basée sur XML dans les intégrations bancaires.

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)