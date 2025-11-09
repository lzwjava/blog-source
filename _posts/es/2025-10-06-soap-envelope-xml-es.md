---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Sobre de SOAP XML Explicado
translated: true
type: note
---

### ¿Qué es un Envelope XML?

Creo que "envalop" es un error tipográfico de "envelope", refiriéndose al **SOAP Envelope** en XML. SOAP (Protocolo Simple de Acceso a Objetos) es un protocolo para intercambiar información estructurada en servicios web utilizando XML. El SOAP Envelope es el elemento raíz de un mensaje SOAP, que envuelve todo el mensaje para identificarlo como un documento SOAP. Asegura que el receptor sepa que es un mensaje completo.

Una estructura básica de SOAP Envelope se ve así:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- Opcional: Metadatos como autenticación -->
  </soap:Header>
  <soap:Body>
    <!-- Obligatorio: La carga útil/datos reales -->
    <YourCustomElement>
      <Data>Algún valor</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

- **Envelope**: Define el inicio/fin del mensaje y el espacio de nombres.
- **Header** (opcional): Para información que no es del cuerpo, como seguridad o enrutamiento.
- **Body** (obligatorio): Contiene los datos de la solicitud/respuesta.

Este formato hace que los mensajes SOAP sean autónomos e independientes del transporte (por ejemplo, a través de HTTP).

### Cómo usar SOAP Envelope XML en Java

Java tiene soporte integrado para SOAP a través de las bibliotecas **JAX-WS** (Java API for XML Web Services) y **SAAJ** (SOAP with Attachments API for Java), parte del JDK (no se necesitan dependencias externas para lo básico).

#### Pasos para crear y enviar un mensaje SOAP:
1.  **Crear un mensaje SOAP**: Usa `javax.xml.soap` para construir el envelope de forma programática.
2.  **Agregar contenido**: Llena el Body (y el Header si es necesario).
3.  **Enviar via HTTP**: Usa `HttpURLConnection` o un cliente como JAX-WS para llamadas completas a servicios web.

Aquí hay un ejemplo simple en Java para crear un SOAP Envelope e imprimirlo (puedes extender esto para enviarlo por HTTP):

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // Crear una fábrica SOAP
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // Crear el mensaje y el envelope
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // Espacio de nombres para SOAP (versión 1.2)
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // Crear elemento Body
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // Guardar e imprimir el mensaje
        soapMessage.saveChanges();
        System.out.println("SOAP Envelope:");
        soapMessage.writeTo(System.out);
    }
}
```

- **Salida**: Esto genera un XML SOAP con el envelope, body y tus elementos personalizados.
- **Para enviarlo**: Encapsúlalo en un cliente JAX-WS. Genera stubs a partir de un archivo WSDL usando la herramienta `wsimport`: `wsimport -keep YourService.wsdl`. Luego usa las clases cliente generadas para invocar métodos, lo que maneja el envelope automáticamente.
- **Bibliotecas**: Para uso avanzado, añade Apache CXF o Axis2 si es necesario, pero usa el JDK por simplicidad.

Ejecuta esto en cualquier entorno Java (JDK 8+). Para servicios web completos, asegúrate de que tu proyecto maneje excepciones como `SOAPException`.

### ¿Usa Finacle Envelope (SOAP XML)?

Sí, Finacle (el software bancario central de Infosys) utiliza extensivamente los envelopes SOAP XML para la integración. Expone servicios web a través de SOAP sobre HTTP mediante la capa **Finacle Integrator**, permitiendo que los sistemas externos se comuniquen utilizando protocolos SOAP estándar. Esto incluye interacciones EJB y middleware para servicios como consultas de cuentas o transacciones. Las APIs de Finacle a menudo siguen los estándares SOAP para mensajería segura basada en XML en integraciones bancarias.

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)  
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)  
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)  
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)  
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)  
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)  
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)  
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)