---
audio: false
generated: true
lang: ar
layout: post
title: بناء عميل شادوسوكس باستخدام نيتي
translated: true
type: note
---

بناء عميل Shadowsocks مثل Clash أو عميل Shadowsocks الأصلي باستخدام Netty يتطلب فهم بروتوكول Shadowsocks والاستفادة من إطار عمل Netty غير المتزامن والقائم على الأحداث للتطبيقات الشبكية. إليك تفصيل للخطوات والمفاهيم الأساسية المعنية:

**1. فهم بروتوكول Shadowsocks**

قبل الخوض في Netty، تحتاج إلى فهم بروتوكول Shadowsocks بشكل شامل. على مستوى عالٍ، يتضمن:

*   **إنشاء الاتصال:** يقوم العميل ببدء اتصال بخادم Shadowsocks.
*   **المصادقة وتبني الطريقة:** يرسل العميل طريقة التشفير وكلمة المرور المختارة إلى الخادم للمصادقة.
*   **ترميز العنوان:** يرسل العميل عنوان الوجهة (عنوان IP والمنفذ) لخادم الوجهة الفعلي بتنسيق مشفر محدد.
*   **توجيه البيانات:** بعد المصادقة الناجحة وترميز العنوان، يتم تشفير/فك تشفير جميع البيانات المتبادلة اللاحقة بين العميل وخادم Shadowsocks باستخدام الطريقة المتفق عليها.

**الجوانب الرئيسية للبروتوكول التي ستحتاج إلى تنفيذها:**

*   **معالجة الطريقة وكلمة المرور:** تخزين وإرسال طريقة التشفير المختارة (مثل `aes-256-cfb`، `chacha20-ietf-poly1305`) وكلمة المرور.
*   **ترميز العنوان:** ترميز عنوان الوجهة إلى تنسيق محدد (نوع البايت، العنوان، المنفذ). يشير نوع البايت إلى ما إذا كان العنوان هو عنوان IPv4 (0x01)، أو عنوان IPv6 (0x04)، أو اسم نطاق (0x03).
*   **التشفير وفك التشفير:** تنفيذ خوارزميات التشفير وفك التشفير المختارة. يمكن أن تكون المكتبات مثل `PyCryptodome` (لـPython) أو `Bouncy Castle` (لـJava) مفيدة في هذا.
*   **توجيه TCP:** إنشاء خادم TCP محلي يستمع لاتصالات من التطبيقات ويوجه الحركة عبر نفق Shadowsocks.

**2. إعداد مشروع Netty**

أولاً، ستحتاج إلى تضمين اعتمادية Netty في مشروعك (على سبيل المثال، باستخدام Maven أو Gradle لمشروع Java).

**3. مكونات Netty الأساسية لعملاء الوكيل**

ستستخدم بشكل أساسي مكونات Netty التالية:

*   **`Bootstrap`:** يُستخدم لتكوين وتشغيل التطبيق من جانب العميل.
*   **`EventLoopGroup`:** يدير حلقات الأحداث التي تتعامل مع عمليات الإدخال/الإخراج للعميل. ستستخدم عادةً `NioEventLoopGroup` للإدخال/الإخراج غير المعيق.
*   **`Channel`:** يمثل اتصالاً شبكياً.
*   **`ChannelPipeline`:** سلسلة من معالجات `ChannelHandler` التي تعالج البيانات والأحداث الواردة والصادرة.
*   **`ChannelHandler`:** واجهات تقوم بتنفيذها للتعامل مع أحداث وتحويلات بيانات محددة. ستقوم بإنشاء معالجات مخصصة لبروتوكول Shadowsocks.
*   **`ByteBuf`:** المخزن المؤقت لـ Netty للتعامل مع البيانات الثنائية.

**4. تنفيذ بروتوكول Shadowsocks باستخدام معالجات Netty**

ستحتاج إلى إنشاء عدة معالجات `ChannelHandler` مخصصة داخل `ChannelPipeline` لتنفيذ منطق Shadowsocks. إليك هيكل محتمل:

*   **معالج خادم الوكيل المحلي (`ChannelInboundHandlerAdapter`):**
    *   سيعمل هذا المعالج على مقبس خادم محلي ستتصل به تطبيقاتك (مثل `localhost:1080`).
    *   عندما يأتي اتصال جديد من تطبيق محلي، سيقوم هذا المعالج بما يلي:
        *   إنشاء اتصال بخادم Shadowsocks البعيد.
        *   توجيه طلب الاتصال الأولي (عنوان الوجهة) إلى خادم Shadowsocks بعد ترميزه وفقًا للبروتوكول.
        *   إدارة تدفق البيانات بين التطبيق المحلي وخادم Shadowsocks.

*   **مشفر عميل Shadowsocks (`ChannelOutboundHandlerAdapter`):**
    *   سيكون هذا المعالج مسؤولاً عن تشفير البيانات المرسلة إلى خادم Shadowsocks.
    *   سيقوم بما يلي:
        *   ترميز عنوان الوجهة وفقًا لبروتوكول Shadowsocks (النوع، العنوان، المنفذ).
        *   تشفير البيانات باستخدام طريقة التشفير المختارة.

*   **فاك تشفير عميل Shadowsocks (`ChannelInboundHandlerAdapter`):**
    *   سيكون هذا المعالج مسؤولاً عن فك تشفير البيانات المستلمة من خادم Shadowsocks.
    *   سيقوم بما يلي:
        *   فك تشفير البيانات المستلمة.

*   **معالج توجيه الخادم البعيد (`ChannelInboundHandlerAdapter`):**
    *   سيتم استدعاء هذا المعالج عند استلام بيانات من خادم Shadowsocks البعيد.
    *   سيقوم بتوجيه البيانات المفكوكة تشفيرها مرة أخرى إلى التطبيق المحلي الأصلي.

**5. مثال على هيكل Netty Pipeline**

إليك مثالاً مبسطاً لكيفية ظهور `ChannelPipeline` الخاص بك للاتصال بخادم Shadowsocks:

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

        // معالجات صادرة (بيانات ذاهبة إلى خادم Shadowsocks)
        pipeline.addLast("encoder", new ShadowsocksClientEncoder(method, password));

        // معالجات واردة (بيانات قادمة من خادم Shadowsocks)
        pipeline.addLast("decoder", new ShadowsocksClientDecoder(method, password));
        pipeline.addLast("remoteForwarder", new RemoteServerForwardingHandler());
    }
}
```

ولخادم الوكيل المحلي:

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

        // معالج لبدء الاتصال بخادم Shadowsocks وتوجيه البيانات
        pipeline.addLast("localProxyHandler",
                new LocalProxyHandler(shadowsocksServerAddress, shadowsocksServerPort, method, password));
    }
}
```

**6. تفاصيل التنفيذ الرئيسية**

*   **تنفيذ التشفير/فك التشفير:** ستحتاج إلى تنفيذ خوارزميات التشفير وفك التشفير المختارة داخل `ShadowsocksClientEncoder` و `ShadowsocksClientDecoder`. من المرجح أن يتضمن ذلك استخدام مكتبات خارجية. كن حذراً بشاشت اشتقاق المفاتيح ومتجهات التهيئة إذا كانت مطلوبة من قبل الطريقة المختارة.
*   **ترميز العنوان في `LocalProxyHandler`:** عندما يستلم `LocalProxyHandler` طلب الاتصال الأولي من التطبيق المحلي، يحتاج إلى استخراج عنوان الوجهة والمنفذ وترميزهما إلى تنسيق Shadowsocks قبل إرسالهما إلى خادم Shadowsocks.
*   **الاتصال بخادم Shadowsocks في `LocalProxyHandler`:** س يستخدم `LocalProxyHandler` `Bootstrap` منفصل لـ Netty لإنشاء اتصال بخادم Shadowsocks المُكون.
*   **توجيه البيانات:** بمجرد إنشاء الاتصال بخادم Shadowsocks، تحتاج المعالجات إلى توجيه البيانات بكفاءة بين اتصال التطبيق المحلي واتصال خادم Shadowsocks. من المرجح أنك ستحتاج إلى إدارة كائنات `Channel` لكلا الاتصالين.
*   **معالجة الأخطاء:** نفذ معالجة مناسبة للأخطاء للمشاكل الشبكية وأخطاء البروتوكول وفشل التشفير/فك التشفير.
*   **التزامن:** يتعامل Netty مع التزامن بكفاءة من خلال نموذج حلقة الأحداث الخاص به. تأكد من أن معالجاتك مصممة لتكون آمنة للخيط إذا كنت بحاجة إلى مشاركة الحالة.

**7. بدء تشغيل عميل الوكيل**

ستحتاج إلى إنشاء فئة رئيسية لبدء تشغيل كل من خادم الوكيل المحلي (الاستماع للاتصالات المحلية) وربما التعامل مع التكوين.

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
        // استبدل هذه بالقيم الخاصة بتكوينك
        int localPort = 1080;
        String serverAddress = "your_server_ip";
        int serverPort = 8388;
        String method = "aes-256-cfb";
        String password = "your_password";

        new ShadowsocksClient(localPort, serverAddress, serverPort, method, password).run();
    }
}
```

**8. اعتبارات متقدمة (مثل Clash)**

لبناء عميل مثل Clash، ستحتاج إلى مراعاة ميزات أكثر تقدمًا:

*   **بروتوكولات وكيل متعددة:** يدعم Clash بروتوكولات وكيل متنوعة (Shadowsocks، SOCKS5، HTTP). ستحتاج إلى إضافة معالجات لكل بروتوكول.
*   **التوجيه القائم على القواعد:** يسمح لك Clash بتعريف قواعد لتوجيه الحركة بناءً على النطاق، عنوان IP، GEOIP، إلخ. سيتضمن ذلك تنفيذ محرك قواعد داخل عميلك.
*   **إدارة التكوين:** يستخدم Clash ملفات تكوين YAML. ستحتاج إلى تنفيذ طريقة لتحميل وتحليل مثل هذه التكوينات.
*   **معالجة DNS:** غالبًا ما يعترض Clash طلبات DNS ويوجهها عبر الوكيل. ستحتاج إلى تنفيذ اعتراض DNS وتوجيهه.
*   **دعم UDP:** يدعم Shadowsocks أيضًا توجيه UDP. ستحتاج إلى تنفيذ معالجة UDP باستخدام إمكانيات UDP في Netty.
*   **الإضافات والامتدادات:** يمتلك Clash نظام إضافات. س تضيف تنفيذ مثل هذا النظام تعقيدًا كبيرًا.

**باختصار، بناء عميل Shadowsocks أساسي باستخدام Netty يتضمن:**

1.  فهم بروتوكول Shadowsocks.
2.  إعداد مشروع Netty.
3.  إنشاء معالجات `ChannelHandler` مخصصة لتشفير البيانات وفك تشفيرها وتوجيهها.
4.  تنفيذ منطق التشفير وفك التشفير.
5.  بدء تشغيل خادم محلي لقبول الاتصالات من التطبيقات.
6.  الاتصال بخادم Shadowsocks البعيد.

يتطلب بناء عميل غني بالميزات مثل Clash فهماً أعمق للشبكات وبروتوكولات الوكيل وبنية برمجية أكثر تعقيدًا. ابدأ بتنفيذ أساسي لـ Shadowsocks وأضف الميزات تدريجيًا حسب الحاجة. تذكر الرجوع إلى الوثائق الرسمية لـ Shadowsocks وأمثلة Nettery للحصول على معلومات أكثر تفصيلاً.