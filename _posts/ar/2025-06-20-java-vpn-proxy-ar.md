---
audio: false
generated: true
lang: ar
layout: post
title: عميل بروكسي VPN لجافا باستخدام نيتي
translated: true
type: note
---

لبناء عميل وكيل VPN لـ Clash في Java باستخدام Netty أو Spring Boot، نحتاج إلى إطار عمل قوي للتعامل مع الشبكات، وتحليل تكوين YAML، وبروتوكولات الوكيل مثل SOCKS وHTTP وShadowsocks. تعتبر Netty مثالية للشبكات عالية الأداء، بينما يمكن لـ Spring Boot تبسيط إدارة التكوين والتبعيات. أدناه، سأوضح المنطق الأساسي، والمكتبات الرئيسية، وسأقدم تنفيذًا نموذجياً يركز على Netty لطبقة الشبكات، حيث أنها أكثر ملاءمة لعمليات الوكيل منخفضة المستوى. سيدعم العميل تكوينات Clash YAML الشائعة (مثل: الوكيلاء، القواعد، و DNS).

### المنطق الرئيسي
1. **تحليل التكوين**:
   - تحليل ملفات تكوين YAML المتوافقة مع Clash (مثل `config.yaml`) التي تحتوي على خوادم الوكيل، والقواعد، وإعدادات DNS.
   - دعم أنواع الوكيل الشائعة: HTTP، SOCKS5، Shadowsocks، إلخ.
   - تعيين حقول YAML إلى كائنات Java لسهولة الوصول.

2. **إعداد خادم الوكيل**:
   - تهيئة خادم Netty للاستماع إلى اتصالات العملاء الواردة (مثل على منفذ محلي مثل 7890).
   - معالجة بروتوكولات الوكيل SOCKS5/HTTP لقبول طلبات العملاء.

3. **التوجيه ومعالجة القواعد**:
   - تنفيذ التوجيه القائم على القواعد (مثل النطاق، IP، أو الجغرافي) كما هو محدد في تكوين YAML.
   - توجيه طلبات العملاء إلى خادم الوكيل المنبع المناسب أو الاتصال المباشر.

4. **إدارة الاتصال**:
   - استخدام نموذج Netty القائم على الأحداث لإدارة اتصالات العميل إلى الوكيل والوكيل إلى الوجهة.
   - دعم تجميع الاتصالات والإبقاء على الاتصال نشطًا للكفاءة.

5. **تحليل DNS**:
   - معالجة استعلامات DNS كما هو محدد في التكوين (مثل استخدام DNS المنبع أو محلل محلي).
   - دعم DNS عبر HTTPS (DoH) أو بروتوكولات آمنة أخرى إذا تم تكوينها.

6. **معالجة البروتوكول**:
   - تنفيذ منطق محدد للبروتوكول لـ Shadowsocks (مثل تشفير AEAD)، وSOCKS5، وHTTP.
   - استخدام معالجات بروتوكول قابلة للإضافة لدعم الإضافات.

7. **معالجة الأخطاء والتسجيل**:
   - معالجة فشل الاتصال، والتكوينات غير الصالحة، أو البروتوكولات غير المدعومة بشكل متحضر.
   - توفير سجلات مفصلة لتصحيح الأخطاء.

### المكتبات الرئيسية
- **Netty**: للشبكات عالية الأداء والإدخال/الإخراج القائم على الأحداث. تتعامل مع اتصالات العملاء، التوجيه عبر الوكيل، وتشفير/فك تشفير البروتوكول.
- **SnakeYAML**: لتحليل ملفات تكوين YAML المتوافقة مع Clash.
- **Bouncy Castle**: للعمليات التشفيرية (مثل تشفير Shadowsocks AEAD).
- **SLF4J**: للتسجيل.
- **Apache Commons**: للوظائف المساعدة (مثل التحقق من صحة التكوين).
- **Jackson (اختياري)**: إذا كنت تفضل التعامل مع YAML بتنسيق مشابه لـ JSON أو تنسيقات تكوين إضافية.
- **DNSJava (اختياري)**: لتحليل DNS مخصص إذا لزم الأمر.

### التنفيذ الأساسي
أدناه تنفيذ مبسط قائم على Netty لعميل وكيل VPN يشبه Clash. يركز على:
- تحليل تكوين Clash YAML.
- إعداد خادم وكيل SOCKS5.
- توجيه الطلبات إلى الوكيل المنبع أو الوجهة.
- التوجيه الأساسي القائم على القواعد.

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

    // فئة التكوين لحفظ بيانات YAML المحللة
    static class ProxyConfig {
        List<Map<String, String>> proxies;
        List<String> rules;

        public ProxyConfig(Map<String, Object> config) {
            this.proxies = (List<Map<String, String>>) config.get("proxies");
            this.rules = (List<String>) config.get("rules");
        }
    }

    // تحميل تكوين Clash YAML
    public void loadConfig(String configPath) throws Exception {
        Yaml yaml = new Yaml();
        try (FileReader reader = new FileReader(configPath)) {
            config = yaml.load(reader);
            logger.info("تم تحميل التكوين من {}", configPath);
        }
    }

    // بدء خادم الوكيل
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
                            // إضافة معالجات بروتوكول SOCKS5
                            pipeline.addLast(new Socks5ServerEncoder());
                            pipeline.addLast(new Socks5InitialRequestDecoder());
                            pipeline.addLast(new Socks5InitialRequestHandler());
                            pipeline.addLast(new Socks5CommandRequestDecoder());
                            pipeline.addLast(new ProxyHandler(new ProxyConfig(config)));
                        }
                    });

            ChannelFuture future = bootstrap.bind(DEFAULT_PORT).sync();
            logger.info("بدأ خادم الوكيل على المنفذ {}", DEFAULT_PORT);
            future.channel().closeFuture().sync();
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    // معالجة طلبات أمر SOCKS5 وتوجيه حركة المرور
    static class ProxyHandler extends SimpleChannelInboundHandler<Socks5CommandRequest> {
        private final ProxyConfig config;

        public ProxyHandler(ProxyConfig config) {
            this.config = config;
        }

        @Override
        protected void channelRead0(ChannelHandlerContext ctx, Socks5CommandRequest request) {
            String destination = request.dstAddr() + ":" + request.dstPort();
            logger.info("معالجة الطلب لـ {}", destination);

            // التوجيه المبسط القائم على القواعد (قم بتوسيعه بتحليل القواعد الفعلي)
            String selectedProxy = selectProxy(destination);
            if (selectedProxy != null) {
                logger.info("التوجيه إلى الوكيل: {}", selectedProxy);
                // تنفيذ منطق التوجيه عبر الوكيل هنا
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.SUCCESS, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            } else {
                logger.warn("لم يتم العثور على وكيل مطابق لـ {}", destination);
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.FAILURE, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            }
        }

        private String selectProxy(String destination) {
            // تنفيذ اختيار الوكيل القائم على القواعد
            for (String rule : config.rules) {
                // مثال: مطابقة قواعد النطاق أو IP
                if (destination.matches(rule)) {
                    return config.proxies.get(0).get("name"); // مبسط
                }
            }
            return null; // اتصال مباشر أو تراجع
        }
    }

    // معالجة طلب SOCKS5 الأولي
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

### نموذج تكوين YAML
إليك مثال `config.yaml` متوافق مع الكود أعلاه:

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

### شرح المنطق الأساسي
- **تحليل YAML**: تستخدم طريقة `loadConfig` مكتبة SnakeYAML لتحليل تكوين Clash إلى كائن `ProxyConfig`، الذي يحتفظ بتعريفات الوكيل وقواعد التوجيه.
- **خادم Netty**: تقوم طريقة `start` بإعداد خادم Netty يستمع على المنفذ 7890، ويتعامل مع طلبات بروتوكول SOCKS5 باستخدام برامج ترميز وفك ترميز SOCKS5 المدمجة في Netty.
- **معالجة الطلبات**: يقوم `ProxyHandler` بمعالجة طلبات أمر SOCKS5، ويطبق قواعد التوجيه، ويختار الوكيل المنبع المناسب أو الاتصال المباشر.
- **التوجيه**: تقوم طريقة `selectProxy` (المبسطة) بمطابقة عناوين الوجهة مع القواعد لاختيار الوكيل المناسب.
- **القدرة على التوسع**: الكود معياري، مما يسمح بإضافة بروتوكولات جديدة بسهولة (مثل Shadowsocks) من خلال توسيع `ProxyHandler`.

### الخطوات التالية
1. **دعم البروتوكول**: إضافة معالجات لـ Shadowsocks (باستخدام Bouncy Castle للتشفير) ووكلاء HTTP.
2. **التوجيه المتقدم**: تنفيذ تحليل قواعد Clash الكاملة (مثل GEOIP، DOMAIN-SUFFIX) باستخدام regex أو محرك قواعد.
3. **معالجة DNS**: دمج DNSJava أو محلل مخصص لإعدادات DNS في Clash.
4. **تجميع الاتصالات**: استخدام `ChannelPool` الخاص بـ Netty للاتصالات المنبع الفعالة.
5. **Spring Boot (اختياري)**: إذا كنت تفضل Spring Boot، فاستخدمه لإدارة التكوين ونقاط نهاية REST للمراقبة، ولكن احتفظ بـ Netty لمنطق الوكيل الأساسي.

### التبعيات (Maven)
أضف هذه إلى `pom.xml` الخاصة بك:

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

يوفر هذا أساسًا لعميل وكيل VPN يشبه Clash. يمكنك توسيعه من خلال إضافة دعم للمزيد من البروتوكولات، والتوجيه المتقدم، وميزات DNS بناءً على احتياجاتك.