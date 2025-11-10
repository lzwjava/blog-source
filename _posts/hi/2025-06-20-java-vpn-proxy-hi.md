---
audio: false
generated: true
lang: hi
layout: post
title: नेट्टी के साथ जावा वीपीएन प्रॉक्सी क्लाइंट
translated: true
type: note
---

Netty या Spring Boot का उपयोग करके Java में Clash VPN प्रॉक्सी क्लाइंट बनाने के लिए, हमें नेटवर्किंग, YAML कॉन्फ़िगरेशन पार्सिंग, और SOCKS, HTTP, और Shadowsocks जैसे प्रॉक्सी प्रोटोकॉल को हैंडल करने के लिए एक मजबूत फ्रेमवर्क की आवश्यकता है। नेटवर्किंग के लिए Netty आदर्श है, जबकि Spring Boot कॉन्फ़िगरेशन और डिपेंडेंसी मैनेजमेंट को सरल बना सकता है। नीचे, मैं कोर लॉजिक, मुख्य लाइब्रेरीज़ का विवरण दूंगा, और नेटवर्किंग लेयर के लिए Netty पर ध्यान केंद्रित करते हुए एक सैंपल इम्प्लीमेंटेशन प्रदान करूंगा, क्योंकि यह लो-लेवल प्रॉक्सी ऑपरेशन्स के लिए अधिक उपयुक्त है। यह क्लाइंट लोकप्रिय Clash YAML कॉन्फ़िगरेशन (जैसे, प्रॉक्सी, नियम, और DNS के लिए) को सपोर्ट करेगा।

### मुख्य लॉजिक
1. **कॉन्फ़िगरेशन पार्सिंग**:
   - Clash-संगत YAML कॉन्फ़िगरेशन फ़ाइलों (जैसे, `config.yaml`) को पार्स करना जिसमें प्रॉक्सी सर्वर, नियम, और DNS सेटिंग्स हों।
   - सामान्य प्रॉक्सी प्रकारों को सपोर्ट करना: HTTP, SOCKS5, Shadowsocks, आदि।
   - YAML फ़ील्ड्स को Java ऑब्जेक्ट्स में मैप करना आसान एक्सेस के लिए।

2. **प्रॉक्सी सर्वर सेटअप**:
   - आने वाले क्लाइंट कनेक्शनों (जैसे, 7890 जैसे लोकल पोर्ट पर) को सुनने के लिए एक Netty सर्वर को इनिशियलाइज़ करना।
   - क्लाइंट रिक्वेस्ट्स को स्वीकार करने के लिए SOCKS5/HTTP प्रॉक्सी प्रोटोकॉल को हैंडल करना।

3. **रूटिंग और नियम हैंडलिंग**:
   - YAML कॉन्फ़िग में परिभाषित नियम-आधारित रूटिंग (जैसे, डोमेन, IP, या जियो-आधारित) को इम्प्लीमेंट करना।
   - क्लाइंट रिक्वेस्ट्स को उपयुक्त अपस्ट्रीम प्रॉक्सी सर्वर या डायरेक्ट कनेक्शन पर रूट करना।

4. **कनेक्शन मैनेजमेंट**:
   - क्लाइंट-टू-प्रॉक्सी और प्रॉक्सी-टू-डेस्टिनेशन कनेक्शनों को मैनेज करने के लिए Netty के इवेंट-ड्रिवन मॉडल का उपयोग करना।
   - दक्षता के लिए कनेक्शन पूलिंग और कीप-अलाइव को सपोर्ट करना।

5. **DNS रेजोल्यूशन**:
   - कॉन्फ़िग में निर्दिष्ट DNS क्वेरीज़ को हैंडल करना (जैसे, अपस्ट्रीम DNS या लोकल रिज़ॉल्वर का उपयोग)।
   - कॉन्फ़िगर किए जाने पर DNS over HTTPS (DoH) या अन्य सुरक्षित प्रोटोकॉल को सपोर्ट करना।

6. **प्रोटोकॉल हैंडलिंग**:
   - Shadowsocks (जैसे, AEAD एन्क्रिप्शन), SOCKS5, और HTTP के लिए प्रोटोकॉल-विशिष्ट लॉजिक को इम्प्लीमेंट करना।
   - एक्स्टेंसिबिलिटी को सपोर्ट करने के लिए प्लगेबल प्रोटोकॉल हैंडलर्स का उपयोग करना।

7. **एरर हैंडलिंग और लॉगिंग**:
   - कनेक्शन फेलियर, अमान्य कॉन्फ़िगरेशन, या असमर्थित प्रोटोकॉल को सहजता से हैंडल करना।
   - डीबगिंग के लिए विस्तृत लॉग प्रदान करना।

### मुख्य लाइब्रेरीज़
- **Netty**: हाई-परफॉर्मेंस नेटवर्किंग और इवेंट-ड्रिवन I/O के लिए। क्लाइंट कनेक्शन, प्रॉक्सी फॉरवर्डिंग, और प्रोटोकॉल एन्कोडिंग/डिकोडिंग को हैंडल करता है।
- **SnakeYAML**: Clash-संगत YAML कॉन्फ़िगरेशन फ़ाइलों को पार्स करने के लिए।
- **Bouncy Castle**: क्रिप्टोग्राफ़िक ऑपरेशन्स (जैसे, Shadowsocks AEAD एन्क्रिप्शन) के लिए।
- **SLF4J**: लॉगिंग के लिए।
- **Apache Commons**: यूटिलिटी फ़ंक्शन्स (जैसे, कॉन्फ़िगरेशन वैलिडेशन) के लिए।
- **Jackson (वैकल्पिक)**: यदि आप YAML या अतिरिक्त कॉन्फ़िग फॉर्मेट के लिए JSON-जैसी हैंडलिंग पसंद करते हैं।
- **DNSJava (वैकल्पिक)**: यदि आवश्यक हो तो कस्टम DNS रेजोल्यूशन के लिए।

### कोर इम्प्लीमेंटेशन
नीचे एक Clash-जैसे VPN प्रॉक्सी क्लाइंट का एक सरलीकृत Netty-आधारित इम्प्लीमेंटेशन दिया गया है। यह निम्नलिखित पर केंद्रित है:
- एक Clash YAML कॉन्फ़िग को पार्स करना।
- एक SOCKS5 प्रॉक्सी सर्वर सेटअप करना।
- रिक्वेस्ट्स को एक अपस्ट्रीम प्रॉक्सी या डेस्टिनेशन पर फॉरवर्ड करना।
- बेसिक नियम-आधारित रूटिंग।

```x-java-source
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.socksx.v5.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.yaml.snakeyaml.Yaml;

import java.io.FileReader;
import java.util.List;
import java.util.Map;

public class ClashProxyClient {
    private static final Logger logger = LoggerFactory.getLogger(ClashProxyClient.class);
    private static final int DEFAULT_PORT = 7890;
    private Map<String, Object> config;

    // कॉन्फ़िगरेशन क्लास पार्स किए गए YAML डेटा को होल्ड करने के लिए
    static class ProxyConfig {
        List<Map<String, String>> proxies;
        List<String> rules;

        public ProxyConfig(Map<String, Object> config) {
            this.proxies = (List<Map<String, String>>) config.get("proxies");
            this.rules = (List<String>) config.get("rules");
        }
    }

    // Clash YAML कॉन्फ़िगरेशन लोड करें
    public void loadConfig(String configPath) throws Exception {
        Yaml yaml = new Yaml();
        try (FileReader reader = new FileReader(configPath)) {
            config = yaml.load(reader);
            logger.info("कॉन्फ़िगरेशन {} से लोड किया गया", configPath);
        }
    }

    // प्रॉक्सी सर्वर शुरू करें
    public void start() throws Exception {
        EventLoopGroup bossGroup = new NioEventLoopGroup(1);
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try {
            ServerBootstrap bootstrap = new ServerBootstrap();
            bootstrap.group(bossGroup, workerGroup)
                    .channel(NioServerSocketChannel.class)
                    .childHandler(new ChannelInitializer<Channel>() {
                        @Override
                        protected void initChannel(Channel ch) {
                            ChannelPipeline pipeline = ch.pipeline();
                            // SOCKS5 प्रोटोकॉल हैंडलर्स जोड़ें
                            pipeline.addLast(new Socks5ServerEncoder());
                            pipeline.addLast(new Socks5InitialRequestDecoder());
                            pipeline.addLast(new Socks5InitialRequestHandler());
                            pipeline.addLast(new Socks5CommandRequestDecoder());
                            pipeline.addLast(new ProxyHandler(new ProxyConfig(config)));
                        }
                    });

            ChannelFuture future = bootstrap.bind(DEFAULT_PORT).sync();
            logger.info("प्रॉक्सी सर्वर पोर्ट {} पर शुरू हुआ", DEFAULT_PORT);
            future.channel().closeFuture().sync();
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    // SOCKS5 कमांड रिक्वेस्ट्स को हैंडल करें और ट्रैफ़िक रूट करें
    static class ProxyHandler extends SimpleChannelInboundHandler<Socks5CommandRequest> {
        private final ProxyConfig config;

        public ProxyHandler(ProxyConfig config) {
            this.config = config;
        }

        @Override
        protected void channelRead0(ChannelHandlerContext ctx, Socks5CommandRequest request) {
            String destination = request.dstAddr() + ":" + request.dstPort();
            logger.info("{} के लिए रिक्वेस्ट हैंडल की जा रही है", destination);

            // सरल नियम-आधारित रूटिंग (वास्तविक नियम पार्सिंग के साथ विस्तार करें)
            String selectedProxy = selectProxy(destination);
            if (selectedProxy != null) {
                logger.info("प्रॉक्सी पर रूट किया जा रहा है: {}", selectedProxy);
                // यहां प्रॉक्सी फॉरवर्डिंग लॉजिक इम्प्लीमेंट करें
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.SUCCESS, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            } else {
                logger.warn("{} के लिए कोई मेल खाता प्रॉक्सी नहीं मिला", destination);
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.FAILURE, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            }
        }

        private String selectProxy(String destination) {
            // नियम-आधारित प्रॉक्सी चयन इम्प्लीमेंट करें
            for (String rule : config.rules) {
                // उदाहरण: डोमेन या IP नियमों से मिलान करें
                if (destination.matches(rule)) {
                    return config.proxies.get(0).get("name"); // सरलीकृत
                }
            }
            return null; // डायरेक्ट कनेक्शन या फॉलबैक
        }
    }

    // SOCKS5 इनिशियल रिक्वेस्ट को हैंडल करें
    static class Socks5InitialRequestHandler extends SimpleChannelInboundHandler<Socks5InitialRequest> {
        @Override
        protected void channelRead0(ChannelHandlerContext ctx, Socks5InitialRequest msg) {
            ctx.write(new DefaultSocks5InitialResponse(Socks5AuthMethod.NO_AUTH));
        }
    }

    public static void main(String[] args) throws Exception {
        ClashProxyClient client = new ClashProxyClient();
        client.loadConfig("config.yaml");
        client.start();
    }
}
```

### सैंपल YAML कॉन्फ़िगरेशन
यहां उपरोक्त कोड के साथ संगत एक उदाहरण `config.yaml` दिया गया है:

```yaml
proxies:
  - name: proxy1
    type: socks5
    server: 192.168.1.100
    port: 1080
  - name: proxy2
    type: http
    server: 192.168.1.101
    port: 8080
rules:
  - DOMAIN,example.com,proxy1
  - IP-CIDR,192.168.0.0/16,DIRECT
```

### कोर लॉजिक की व्याख्या
- **YAML पार्सिंग**: `loadConfig` मेथड SnakeYAML का उपयोग Clash कॉन्फ़िगरेशन को एक `ProxyConfig` ऑब्जेक्ट में पार्स करने के लिए करती है, जो प्रॉक्सी परिभाषाएँ और रूटिंग नियम रखता है।
- **Netty सर्वर**: `start` मेथड पोर्ट 7890 पर सुनने वाले एक Netty सर्वर को सेटअप करती है, जो Netty के बिल्ट-इन SOCKS5 कोडेक्स का उपयोग करके SOCKS5 प्रोटोकॉल रिक्वेस्ट्स को हैंडल करती है।
- **रिक्वेस्ट हैंडलिंग**: `ProxyHandler` SOCKS5 कमांड रिक्वेस्ट्स को प्रोसेस करता है, रूटिंग नियम लागू करता है, और एक अपस्ट्रीम प्रॉक्सी या डायरेक्ट कनेक्शन का चयन करता है।
- **रूटिंग**: `selectProxy` मेथड (सरलीकृत) उपयुक्त प्रॉक्सी चुनने के लिए डेस्टिनेशन एड्रेस का नियमों से मिलान करती है।
- **एक्स्टेंसिबिलिटी**: कोड मॉड्यूलर है, जो `ProxyHandler` का विस्तार करके नए प्रोटोकॉल (जैसे, Shadowsocks) को आसानी से जोड़ने की अनुमति देता है।

### अगले कदम
1. **प्रोटोकॉल सपोर्ट**: Shadowsocks (एन्क्रिप्शन के लिए Bouncy Castle का उपयोग करके) और HTTP प्रॉक्सी के लिए हैंडलर्स जोड़ें।
2. **एडवांस्ड रूटिंग**: regex या रूल इंजन का उपयोग करके पूर्ण Clash नियम पार्सिंग (जैसे, GEOIP, DOMAIN-SUFFIX) को इम्प्लीमेंट करें।
3. **DNS हैंडलिंग**: Clash की DNS सेटिंग्स के लिए DNSJava या कस्टम रिज़ॉल्वर को इंटीग्रेट करें।
4. **कनेक्शन पूलिंग**: कुशल अपस्ट्रीम कनेक्शनों के लिए Netty के `ChannelPool` का उपयोग करें।
5. **Spring Boot (वैकल्पिक)**: यदि आप Spring Boot पसंद करते हैं, तो कॉन्फ़िगरेशन मैनेजमेंट और मॉनिटरिंग के लिए REST एंडपॉइंट्स के लिए इसका उपयोग करें, लेकिन कोर प्रॉक्सी लॉजिक के लिए Netty को बनाए रखें।

### डिपेंडेंसीज़ (Maven)
इन्हें अपने `pom.xml` में जोड़ें:

```xml
<dependencies>
    <dependency>
        <groupId>io.netty</groupId>
        <artifactId>netty-all</artifactId>
        <version>4.1.111.Final</version>
    </dependency>
    <dependency>
        <groupId>org.yaml</groupId>
        <artifactId>snakeyaml</artifactId>
        <version>2.3</version>
    </dependency>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-api</artifactId>
        <version>2.0.16</version>
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk18on</artifactId>
        <version>1.78.1</version>
    </dependency>
</dependencies>
```

यह एक Clash-जैसे VPN प्रॉक्सी क्लाइंट की नींव प्रदान करता है। आप इसे अधिक प्रोटोकॉल, एडवांस्ड रूटिंग, और DNS फीचर्स के सपोर्ट को जोड़कर विस्तारित कर सकते हैं, जो आपकी आवश्यकताओं पर निर्भर करता है। मुझे बताएं यदि आप किसी विशिष्ट भाग में गहराई से उतरना चाहते हैं!