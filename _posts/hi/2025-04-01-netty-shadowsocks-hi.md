---
audio: false
generated: true
lang: hi
layout: post
title: नेटी के साथ एक शैडोसॉक्स क्लाइंट बनाना
translated: true
type: note
---

Netty का उपयोग करके Clash या मूल Shadowsocks क्लाइंट जैसा Shadowsocks क्लाइंट बनाने में Shadowsocks प्रोटोकॉल को समझना और Netty के अतुल्यकालिक, इवेंट-संचालित नेटवर्क एप्लिकेशन फ्रेमवर्क का लाभ उठाना शामिल है। यहां शामिल चरणों और मुख्य अवधारणाओं का विवरण दिया गया है:

**1. Shadowsocks प्रोटोकॉल को समझना**

Netty में गोता लगाने से पहले, आपको Shadowsocks प्रोटोकॉल को अच्छी तरह से समझने की आवश्यकता है। एक उच्च स्तर पर, इसमें शामिल है:

*   **कनेक्शन स्थापना:** एक क्लाइंट Shadowsocks सर्वर से कनेक्शन शुरू करता है।
*   **प्रमाणीकरण और विधि वार्ता:** क्लाइंट प्रमाणीकरण के लिए चुनी गई एन्क्रिप्शन विधि और पासवर्ड सर्वर को भेजता है।
*   **पता एन्कोडिंग:** क्लाइंट वास्तविक गंतव्य सर्वर के लक्ष्य पते (IP पता और पोर्ट) को एक विशिष्ट एन्कोडेड प्रारूप में भेजता है।
*   **डेटा फॉरवर्डिंग:** सफल प्रमाणीकरण और पता एन्कोडिंग के बाद, क्लाइंट और Shadowsocks सर्वर के बीच आदान-प्रदान किया गया सभी डेटा सहमत विधि का उपयोग करके एन्क्रिप्ट/डिक्रिप्ट किया जाता है।

**प्रोटोकॉल के प्रमुख पहलू जिन्हें आपको लागू करने की आवश्यकता होगी:**

*   **विधि और पासवर्ड हैंडलिंग:** चुनी गई एन्क्रिप्शन विधि (जैसे, `aes-256-cfb`, `chacha20-ietf-poly1305`) और पासवर्ड को संग्रहीत करना और भेजना।
*   **पता एन्कोडिंग:** लक्ष्य पते को एक विशिष्ट प्रारूप (टाइप बाइट, पता, पोर्ट) में एन्कोड करना। टाइप बाइट इंगित करता है कि पता एक IPv4 पता (0x01), एक IPv6 पता (0x04), या एक होस्टनाम (0x03) है।
*   **एन्क्रिप्शन और डिक्रिप्शन:** चुनी गई एन्क्रिप्शन और डिक्रिप्शन एल्गोरिदम को लागू करना। इसके लिए `PyCryptodome` (Python) या `Bouncy Castle` (Java) जैसी लाइब्रेरी मददगार हो सकती हैं।
*   **TCP फॉरवर्डिंग:** एक स्थानीय TCP सर्वर स्थापित करना जो एप्लिकेशन से कनेक्शन को सुनता है और ट्रैफ़िक को Shadowsocks टनल के माध्यम से फॉरवर्ड करता है।

**2. एक Netty प्रोजेक्ट सेट करना**

सबसे पहले, आपको अपने प्रोजेक्ट में Netty निर्भरता शामिल करनी होगी (उदाहरण के लिए, Java प्रोजेक्ट के लिए Maven या Gradle का उपयोग करके)।

**3. प्रॉक्सी क्लाइंट के लिए Core Netty Components**

आप मुख्य रूप से निम्नलिखित Netty components का उपयोग करेंगे:

*   **`Bootstrap`:** क्लाइंट-साइड एप्लिकेशन को कॉन्फ़िगर और शुरू करने के लिए उपयोग किया जाता है।
*   **`EventLoopGroup`:** इवेंट लूप का प्रबंधन करता है जो क्लाइंट के लिए I/O ऑपरेशन को संभालते हैं। आप आमतौर पर नॉन-ब्लॉकिंग I/O के लिए `NioEventLoopGroup` का उपयोग करेंगे।
*   **`Channel`:** एक नेटवर्क कनेक्शन का प्रतिनिधित्व करता है।
*   **`ChannelPipeline`:** `ChannelHandler` की एक श्रृंखला जो इनबाउंड और आउटबाउंड इवेंट और डेटा को प्रोसेस करती है।
*   **`ChannelHandler`:** इंटरफेस जिन्हें आप विशिष्ट इवेंट और डेटा परिवर्तनों को संभालने के लिए लागू करते हैं। आप Shadowsocks प्रोटोकॉल के लिए कस्टम हैंडलर बनाएंगे।
*   **`ByteBuf`:** बाइनरी डेटा को संभालने के लिए Netty का बफर।

**4. Netty Handlers के साथ Shadowsocks प्रोटोकॉल को लागू करना**

Shadowsocks लॉजिक को लागू करने के लिए आपको अपने `ChannelPipeline` के भीतर कई कस्टम `ChannelHandler` बनाने की आवश्यकता होगी। यहां एक संभावित संरचना है:

*   **लोकल प्रॉक्सी सर्वर हैंडलर (`ChannelInboundHandlerAdapter`):**
    * यह हैंडलर एक लोकल सर्वर सॉकेट पर चलेगा जिससे आपके एप्लिकेशन कनेक्ट होंगे (उदाहरण के लिए, `localhost:1080`)।
    * जब कोई नया कनेक्शन लोकल एप्लिकेशन से आता है, तो यह हैंडलर:
        * रिमोट Shadowsocks सर्वर से कनेक्शन स्थापित करेगा।
        * प्रारंभिक कनेक्शन अनुरोध (लक्ष्य पता) को प्रोटोकॉल के अनुसार एन्कोड करने के बाद Shadowsocks सर्वर को फॉरवर्ड करेगा।
        * लोकल एप्लिकेशन और Shadowsocks सर्वर के बीच डेटा के प्रवाह का प्रबंधन करेगा।

*   **Shadowsocks क्लाइंट एनकोडर (`ChannelOutboundHandlerAdapter`):**
    * यह हैंडलर Shadowsocks सर्वर को भेजे जा रहे डेटा को एन्कोड करने के लिए जिम्मेदार होगा।
    * यह:
        * लक्ष्य पते को Shadowsocks प्रोटोकॉल (टाइप, पता, पोर्ट) के अनुसार एन्कोड करेगा।
        * चुनी गई एन्क्रिप्शन विधि का उपयोग करके डेटा को एन्क्रिप्ट करेगा।

*   **Shadowsocks क्लाइंट डिकोडर (`ChannelInboundHandlerAdapter`):**
    * यह हैंडलर Shadowsocks सर्वर से प्राप्त डेटा को डिकोड करने के लिए जिम्मेदार होगा।
    * यह:
        * प्राप्त डेटा को डिक्रिप्ट करेगा।

*   **रिमोट सर्वर फॉरवर्डिंग हैंडलर (`ChannelInboundHandlerAdapter`):**
    * यह हैंडलर तब invoked होगा जब रिमोट Shadowsocks सर्वर से डेटा प्राप्त होता है।
    * यह डिक्रिप्ट किए गए डेटा को मूल लोकल एप्लिकेशन पर वापस फॉरवर्ड करेगा।

**5. Netty पाइपलाइन की उदाहरण संरचना**

यहां एक सरलीकृत उदाहरण है कि Shadowsocks सर्वर से कनेक्शन के लिए आपकी `ChannelPipeline` कैसी दिख सकती है:

```java
public class ShadowsocksClientInitializer extends ChannelInitializer<SocketChannel> {

    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClientInitializer(String serverAddress, int serverPort, String method, String password) {
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // आउटबाउंड हैंडलर (Shadowsocks सर्वर पर जाने वाला डेटा)
        pipeline.addLast("encoder", new ShadowsocksClientEncoder(method, password));

        // इनबाउंड हैंडलर (Shadowsocks सर्वर से आने वाला डेटा)
        pipeline.addLast("decoder", new ShadowsocksClientDecoder(method, password));
        pipeline.addLast("remoteForwarder", new RemoteServerForwardingHandler());
    }
}
```

और लोकल प्रॉक्सी सर्वर के लिए:

```java
public class LocalProxyInitializer extends ChannelInitializer<SocketChannel> {

    private final String shadowsocksServerAddress;
    private final int shadowsocksServerPort;
    private final String method;
    private final String password;

    public LocalProxyInitializer(String shadowsocksServerAddress, int shadowsocksServerPort, String method, String password) {
        this.shadowsocksServerAddress = shadowsocksServerAddress;
        this.shadowsocksServerPort = shadowsocksServerPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // Shadowsocks सर्वर से कनेक्शन शुरू करने और डेटा फॉरवर्ड करने के लिए हैंडलर
        pipeline.addLast("localProxyHandler",
                new LocalProxyHandler(shadowsocksServerAddress, shadowsocksServerPort, method, password));
    }
}
```

**6. प्रमुख कार्यान्वयन विवरण**

*   **एन्क्रिप्शन/डिक्रिप्शन कार्यान्वयन:** आपको अपने `ShadowsocksClientEncoder` और `ShadowsocksClientDecoder` के भीतर चुनी गई एन्क्रिप्शन और डिक्रिप्शन एल्गोरिदम को लागू करने की आवश्यकता होगी। इसमें संभवतः बाहरी लाइब्रेरी का उपयोग शामिल होगा। चुनी गई विधि द्वारा आवश्यक होने पर key derivation और initialization vectors के साथ सावधान रहें।
*   **`LocalProxyHandler` में पता एन्कोडिंग:** जब `LocalProxyHandler` को लोकल एप्लिकेशन से प्रारंभिक कनेक्शन अनुरोध प्राप्त होता है, तो उसे लक्ष्य पते और पोर्ट को निकालने और उन्हें Shadowsocks सर्वर पर भेजने से पहले Shadowsocks प्रारूप में एन्कोड करने की आवश्यकता होती है।
*   **`LocalProxyHandler` में Shadowsocks सर्वर से कनेक्ट होना:** `LocalProxyHandler` कॉन्फ़िगर किए गए Shadowsocks सर्वर से कनेक्शन स्थापित करने के लिए एक अलग Netty `Bootstrap` का उपयोग करेगा।
*   **डेटा फॉरवर्डिंग:** एक बार Shadowsocks सर्वर से कनेक्शन स्थापित हो जाने के बाद, हैंडलर को लोकल एप्लिकेशन के कनेक्शन और Shadowsocks सर्वर के कनेक्शन के बीच डेटा को कुशलतापूर्वक फॉरवर्ड करने की आवश्यकता होती है। आपको संभवतः दोनों कनेक्शनों के लिए `Channel` ऑब्जेक्ट का प्रबंधन करने की आवश्यकता होगी।
*   **त्रुटि हैंडलिंग:** नेटवर्क समस्याओं, प्रोटोकॉल त्रुटियों और एन्क्रिप्शन/डिक्रिप्शन विफलताओं के लिए उचित त्रुटि हैंडलिंग लागू करें।
*   **Concurrency:** Netty अपने इवेंट लूप मॉडल के साथ concurrency को कुशलतापूर्वक संभालता है। सुनिश्चित करें कि यदि आपको state साझा करने की आवश्यकता है तो आपके हैंडलर thread-safe होने के लिए डिज़ाइन किए गए हैं।

**7. प्रॉक्सी क्लाइंट शुरू करना**

आपको लोकल प्रॉक्सी सर्वर (लोकल कनेक्शन के लिए सुनना) को शुरू करने और संभावित रूप से कॉन्फ़िगरेशन को संभालने के लिए एक मुख्य क्लास बनाने की आवश्यकता होगी।

```java
public class ShadowsocksClient {

    private final int localPort;
    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClient(int localPort, String serverAddress, int serverPort, String method, String password) {
        this.localPort = localPort;
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    public void run() throws Exception {
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();

        try {
            ServerBootstrap b = new ServerBootstrap();
            b.group(bossGroup, workerGroup)
             .channel(NioServerSocketChannel.class)
             .childHandler(new LocalProxyInitializer(serverAddress, serverPort, method, password))
             .option(ChannelOption.SO_BACKLOG, 128)
             .childOption(ChannelOption.SO_KEEPALIVE, true);

            ChannelFuture f = b.bind(localPort).sync();
            System.out.println("Shadowsocks client started on port: " + localPort);
            f.channel().closeFuture().sync();
        } finally {
            workerGroup.shutdownGracefully();
            bossGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        // अपनी कॉन्फ़िगरेशन के साथ बदलें
        int localPort = 1080;
        String serverAddress = "your_server_ip";
        int serverPort = 8388;
        String method = "aes-256-cfb";
        String password = "your_password";

        new ShadowsocksClient(localPort, serverAddress, serverPort, method, password).run();
    }
}
```

**8. उन्नत विचार (Clash जैसा)**

Clash जैसा क्लाइंट बनाने के लिए, आपको अधिक उन्नत सुविधाओं पर विचार करने की आवश्यकता होगी:

*   **एकाधिक प्रॉक्सी प्रोटोकॉल:** Clash विभिन्न प्रॉक्सी प्रोटोकॉल (Shadowsocks, SOCKS5, HTTP) का समर्थन करता है। आपको प्रत्येक प्रोटोकॉल के लिए हैंडलर जोड़ने की आवश्यकता होगी।
*   **नियम-आधारित रूटिंग:** Clash आपको डोमेन, IP पते, GEOIP आदि के आधार पर ट्रैफ़िक रूट करने के लिए नियम परिभाषित करने की अनुमति देता है। इसमें आपके क्लाइंट के भीतर एक नियम इंजन लागू करना शामिल होगा।
*   **कॉन्फ़िगरेशन प्रबंधन:** Clash YAML कॉन्फ़िगरेशन फ़ाइलों का उपयोग करता है। आपको ऐसे कॉन्फ़िगरेशन को लोड और पार्स करने का एक तरीका लागू करने की आवश्यकता होगी।
*   **DNS हैंडलिंग:** Clash अक्सर DNS अनुरोधों को इंटरसेप्ट करता है और उन्हें प्रॉक्सी के माध्यम से रूट करता है। आपको DNS इंटरसेप्शन और फॉरवर्डिंग लागू करने की आवश्यकता होगी।
*   **UDP सपोर्ट:** Shadowsocks UDP फॉरवर्डिंग का भी समर्थन करता है। आपको Netty की UDP क्षमताओं का उपयोग करके UDP हैंडलिंग लागू करने की आवश्यकता होगी।
*   **प्लगइन और एक्सटेंशन:** Clash में एक प्लगइन सिस्टम है। ऐसी प्रणाली को लागू करने से महत्वपूर्ण जटिलता बढ़ जाएगी।

**संक्षेप में, Netty के साथ एक बुनियादी Shadowsocks क्लाइंट बनाने में शामिल है:**

1.  Shadowsocks प्रोटोकॉल को समझना।
2.  एक Netty प्रोजेक्ट स्थापित करना।
3.  डेटा को एन्कोडिंग, डिकोडिंग और फॉरवर्डिंग के लिए कस्टम `ChannelHandler` बनाना।
4.  एन्क्रिप्शन और डिक्रिप्शन लॉजिक को लागू करना।
5.  एप्लिकेशन से कनेक्शन स्वीकार करने के लिए एक लोकल सर्वर शुरू करना।
6.  रिमोट Shadowsocks सर्वर से कनेक्ट होना।

Clash जैसा अधिक फीचर-समृद्ध क्लाइंट बनाने के लिए नेटवर्किंग, प्रॉक्सी प्रोटोकॉल और अधिक जटिल सॉफ़्टवेयर आर्किटेक्चर की गहरी समझ की आवश्यकता होती है। एक बुनियादी Shadowsocks कार्यान्वयन से शुरुआत करें और आवश्यकतानुसार धीरे-धीरे सुविधाएँ जोड़ें। अधिक विस्तृत जानकारी के लिए आधिकारिक Shadowsocks दस्तावेज़ और Netty उदाहरणों से परामर्श लेना याद रखें।