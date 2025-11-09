---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: SOAPエンベロープXMLの解説
translated: true
type: note
---

### Envelope XMLとは何ですか？

「envalop」は「envelope」のタイポだと考えられ、XMLにおける**SOAP Envelope**を指します。SOAP（Simple Object Access Protocol）は、XMLを使用したWebサービスにおける構造化情報交換のためのプロトコルです。SOAP EnvelopeはSOAPメッセージのルート要素であり、メッセージ全体をラップしてSOAPドキュメントとして識別します。これにより受信側が完全なメッセージであることを認識できます。

基本的なSOAP Envelopeの構造は以下のようになります：

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- オプション：認証などのメタデータ -->
  </soap:Header>
  <soap:Body>
    <!-- 必須：実際のペイロード/データ -->
    <YourCustomElement>
      <Data>Some value</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

- **Envelope**: メッセージの開始/終了と名前空間を定義します。
- **Header**（オプション）: セキュリティやルーティングなど、本文以外の情報を含みます。
- **Body**（必須）: リクエスト/レスポンスデータを含みます。

この形式により、SOAPメッセージは自己完結的かつ（HTTP経由など）トランスポートに依存しないものとなります。

### JavaでSOAP Envelope XMLを使用する方法

Javaには、**JAX-WS**（Java API for XML Web Services）および**SAAJ**（SOAP with Attachments API for Java）ライブラリを通じてSOAPの組み込みサポートがあり、これらはJDKの一部です（基本的な機能には外部依存関係は不要です）。

#### SOAPメッセージの作成と送信の手順：
1. **SOAPメッセージの作成**: `javax.xml.soap`を使用してプログラムでエンベロープを構築します。
2. **コンテンツの追加**: Body（および必要に応じてHeader）にデータを投入します。
3. **HTTP経由での送信**: `HttpURLConnection`またはJAX-WSクライアントなどを使用して送信します。

以下は、SOAP Envelopeを作成して出力する簡単なJavaの例です（HTTP経由で送信するように拡張できます）：

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // SOAPファクトリを作成
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // メッセージとエンベロープを作成
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // SOAPの名前空間（バージョン1.2）
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // Body要素を作成
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // メッセージを保存して出力
        soapMessage.saveChanges();
        System.out.println("SOAP Envelope:");
        soapMessage.writeTo(System.out);
    }
}
```

- **出力**: これにより、エンベロープ、ボディ、およびカスタム要素を含むSOAP XMLが生成されます。
- **送信するには**: JAX-WSクライアントでラップします。`wsimport`ツールを使用してWSDLファイルからスタブを生成します：`wsimport -keep YourService.wsdl`。その後、生成されたクライアントクラスを使用してメソッドを呼び出し、エンベロープを自動的に処理します。
- **ライブラリ**: 高度な使用法にはApache CXFやAxis2を追加できますが、シンプルさを重視する場合はJDKに固執します。

これは任意のJava環境（JDK 8以上）で実行できます。完全なWebサービスの場合は、プロジェクトが`SOAPException`などの例外を処理することを確認してください。

### FinacleはEnvelope（SOAP XML）を使用しますか？

はい、Finacle（Infosysのコアバンキングソフトウェア）は統合にSOAP XMLエンベロープを広範に使用しています。**Finacle Integrator**レイヤーを介してSOAP over HTTPでWebサービスを公開し、外部システムが標準的なSOAPプロトコルを使用して通信できるようにします。これには、EJBインタラクションや、口座照会や取引などのサービスのためのミドルウェアが含まれます。FinacleのAPIは、銀行統合における安全なXMLベースのメッセージングのために、SOAP標準に従うことが多いです。

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)  
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)  
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)  
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)  
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)  
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)  
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)  
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)