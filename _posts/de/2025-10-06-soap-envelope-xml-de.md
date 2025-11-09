---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: SOAP-Envelope-XML erklärt
translated: true
type: note
---

### Was ist ein Envelope XML?

Ich glaube, "envalop" ist ein Tippfehler für "Envelope" und bezieht sich auf den **SOAP-Envelope** in XML. SOAP (Simple Object Access Protocol) ist ein Protokoll zum Austausch strukturierter Informationen in Webdiensten unter Verwendung von XML. Der SOAP-Envelope ist das Stammelement einer SOAP-Nachricht, das die gesamte Nachricht umschließt, um sie als SOAP-Dokument zu kennzeichnen. Es stellt sicher, dass der Empfänger erkennt, dass es sich um eine vollständige Nachricht handelt.

Eine grundlegende SOAP-Envelope-Struktur sieht folgendermaßen aus:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- Optional: Metadaten wie Authentifizierung -->
  </soap:Header>
  <soap:Body>
    <!-- Obligatorisch: Die eigentliche Nutzlast/Daten -->
    <YourCustomElement>
      <Data>Ein Wert</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

-   **Envelope**: Definiert den Start/das Ende der Nachricht und den Namespace.
-   **Header** (optional): Für Informationen, die nicht zum Hauptinhalt gehören, wie Sicherheit oder Routing.
-   **Body** (erforderlich): Enthält die Anfrage-/Antwortdaten.

Dieses Format macht SOAP-Nachrichten eigenständig und transportunabhängig (z. B. über HTTP).

### Wie man SOAP Envelope XML in Java verwendet

Java bietet eingebaute Unterstützung für SOAP über die **JAX-WS** (Java API for XML Web Services) und **SAAJ** (SOAP with Attachments API for Java) Bibliotheken, die Teil des JDK sind (für die Grundfunktionen sind keine externen Abhängigkeiten erforderlich).

#### Schritte zum Erstellen und Senden einer SOAP-Nachricht:
1.  **Erstellen einer SOAP-Nachricht**: Verwenden Sie `javax.xml.soap`, um den Envelope programmatisch zu erstellen.
2.  **Inhalt hinzufügen**: Füllen Sie den Body (und bei Bedarf den Header).
3.  **Senden über HTTP**: Verwenden Sie `HttpURLConnection` oder einen Client wie JAX-WS für vollständige Web Service-Aufrufe.

Hier ist ein einfaches Java-Beispiel, um einen SOAP-Envelope zu erstellen und auszugeben (Sie können dies erweitern, um ihn über HTTP zu senden):

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // Erstelle eine SOAP-Factory
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // Erstelle die Nachricht und den Envelope
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // Namespace für SOAP (Version 1.2)
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // Erstelle Body-Element
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // Speichere und gebe die Nachricht aus
        soapMessage.saveChanges();
        System.out.println("SOAP Envelope:");
        soapMessage.writeTo(System.out);
    }
}
```

-   **Ausgabe**: Dies generiert ein SOAP-XML mit dem Envelope, Body und Ihren benutzerdefinierten Elementen.
-   **Zum Senden**: Verpacken Sie es in einen JAX-WS-Client. Generieren Sie Stubs aus einer WSDL-Datei mit dem `wsimport`-Tool: `wsimport -keep YourService.wsdl`. Verwenden Sie dann die generierten Client-Klassen, um Methoden aufzurufen, die den Envelope automatisch handhaben.
-   **Bibliotheken**: Für erweiterte Anwendungsfälle können Sie Apache CXF oder Axis2 hinzufügen, bleiben Sie aber der Einfachheit halber beim JDK.

Führen Sie dies in einer beliebigen Java-Umgebung (JDK 8+) aus. Stellen Sie für vollständige Webdienste sicher, dass Ihr Projekt Ausnahmen wie `SOAPException` behandelt.

### Verwendet Finacle Envelope (SOAP XML)?

Ja, Finacle (die Kernbankensoftware von Infosys) verwendet SOAP-XML-Envelopes umfangreich für die Integration. Es stellt Webdienste über SOAP über HTTP durch die **Finacle Integrator**-Schicht bereit, die es externen Systemen ermöglicht, mit standardmäßigen SOAP-Protokollen zu kommunizieren. Dies schließt EJB-Interaktionen und Middleware für Dienste wie Kontenabfragen oder Transaktionen ein. Finacles APIs folgen oft SOAP-Standards für sichere, XML-basierte Nachrichtenübermittlung in Bankintegrationen.

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)  
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)  
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)  
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)  
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)  
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)  
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)  
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)