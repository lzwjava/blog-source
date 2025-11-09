---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: SOAP 信封 XML 詳解
translated: true
type: note
---

### 什麼是 Envelope XML？

我相信「envalop」是「envelope」的筆誤，指的是 XML 中的 **SOAP Envelope**。SOAP（簡單物件存取協定）是一種使用 XML 在網路服務中交換結構化資訊的協定。SOAP Envelope 是 SOAP 訊息的根元素，它封裝了整個訊息，以識別其為 SOAP 文件。它確保接收者知道這是一個完整的訊息。

基本的 SOAP Envelope 結構如下：

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- 可選：元數據，例如身份驗證 -->
  </soap:Header>
  <soap:Body>
    <!-- 必需：實際的承載數據 -->
    <YourCustomElement>
      <Data>Some value</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

- **Envelope**：定義訊息的開始/結束和命名空間。
- **Header**（可選）：用於非主體資訊，例如安全性或路由。
- **Body**（必需）：包含請求/回應數據。

這種格式使 SOAP 訊息自包含且與傳輸方式無關（例如透過 HTTP）。

### 如何在 Java 中使用 SOAP Envelope XML

Java 透過 **JAX-WS**（Java API for XML Web Services）和 **SAAJ**（SOAP with Attachments API for Java）函式庫內建支援 SOAP，這些是 JDK 的一部分（基礎功能無需外部依賴）。

#### 建立和發送 SOAP 訊息的步驟：
1. **建立 SOAP 訊息**：使用 `javax.xml.soap` 以程式方式構建信封。
2. **添加內容**：填充 Body（如果需要，也填充 Header）。
3. **透過 HTTP 發送**：使用 `HttpURLConnection` 或像 JAX-WS 這樣的客戶端進行完整的 Web 服務呼叫。

以下是一個簡單的 Java 範例，用於建立 SOAP Envelope 並列印它（您可以擴展此範例以透過 HTTP 發送）：

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // 建立 SOAP 工廠
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // 建立訊息和信封
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // SOAP 的命名空間（版本 1.2）
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // 建立 Body 元素
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // 儲存並列印訊息
        soapMessage.saveChanges();
        System.out.println("SOAP Envelope:");
        soapMessage.writeTo(System.out);
    }
}
```

- **輸出**：這會生成帶有信封、主體和自定義元素的 SOAP XML。
- **發送它**：將其包裝在 JAX-WS 客戶端中。使用 `wsimport` 工具從 WSDL 檔案生成存根：`wsimport -keep YourService.wsdl`。然後使用生成的客戶端類別自動呼叫方法，這些方法會自動處理信封。
- **函式庫**：對於進階使用，如果需要，可以添加 Apache CXF 或 Axis2，但為了簡單起見，請堅持使用 JDK。

在任何 Java 環境（JDK 8+）中運行此程式。對於完整的 Web 服務，請確保您的專案處理像 `SOAPException` 這樣的異常。

### Finacle 是否使用 Envelope (SOAP XML)？

是的，Finacle（Infosys 的核心銀行軟體）在整合中廣泛使用 SOAP XML 信封。它透過 **Finacle Integrator** 層暴露了透過 HTTP 的 SOAP Web 服務，允許外部系統使用標準 SOAP 協定進行通訊。這包括 EJB 互動和中間件，用於帳戶查詢或交易等服務。Finacle 的 API 通常遵循 SOAP 標準，用於銀行整合中的安全、基於 XML 的訊息傳遞。

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)  
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)  
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)  
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)  
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)  
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)  
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)  
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)