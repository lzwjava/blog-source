---
audio: false
generated: true
lang: ar
layout: post
title: استخدام NIO في جاڤا
translated: true
---

أفهم كيف يمكن استخدام NIO (New Input/Output) في Java مع بعض الأمثلة العملية. Java NIO هو API I/O غير متزامن يوفر طريقة أكثر كفاءة للتعامل مع عمليات I/O مقارنة بالباقة التقليدية java.io.

هنا هو تحليل المكونات الرئيسية ومثال بسيط:

### المكونات الرئيسية في NIO
1. **الBuffers**: أوعية للبيانات (مثل `ByteBuffer`).
2. **Channels**: قنوات للقراءة/الكتابة للبيانات (مثل `FileChannel`, `SocketChannel`).
3. **Selectors**: لتعدد القنوات في الوضع غير المتزامن.

### مثال أساسي: قراءة ملف باستخدام NIO
هكذا يمكنك قراءة ملف باستخدام `FileChannel` و `ByteBuffer`:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // فتح قناة ملف
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"),
                StandardOpenOption.READ
            );

            // تخصيص حافظة
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // قراءة البيانات إلى الحافظة
            while (fileChannel.read(buffer) > 0) {
                // تبديل الحافظة لتجهيزها للقراءة
                buffer.flip();

                // معالجة البيانات
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // مسح الحافظة للقراءة التالية
                buffer.clear();
            }

            // إغلاق القناة
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### كيف يعمل
1. **FileChannel**: يفتح اتصالًا بالملف.
2. **ByteBuffer**: يعمل كخزن مؤقت للبيانات. يمكنك تخصيص حجمه (مثل 1024 بايت).
3. **عمليات الحافظة**:
   - `flip()`: يجهز الحافظة للقراءة بعد كتابة البيانات فيها.
   - `clear()`: يعيد تعيين الحافظة للقطعة التالية من البيانات.
4. **القراءة**: طريقة `read()` تمليء الحافظة، وتستخرج البيانات بايتًا بايتًا.

---

### كتابة في ملف باستخدام NIO
هنا مثال للكتابة في ملف:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // فتح قناة ملف للكتابة
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"),
                StandardOpenOption.CREATE,
                StandardOpenOption.WRITE
            );

            // البيانات للكتابة
            String data = "مرحبًا، NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // وضع البيانات في الحافظة
            buffer.put(data.getBytes());

            // تبديل الحافظة لتجهيزها للكتابة
            buffer.flip();

            // كتابة الحافظة في الملف
            fileChannel.write(buffer);

            // إغلاق القناة
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### مثال غير متزامن باستخدام Selector
للبرمجة الشبكية (مثل الخادم)، يمكنك استخدام `Selector` مع `SocketChannel`:

```java
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.net.InetSocketAddress;
import java.util.Iterator;

public class NIOServer {
    public static void main(String[] args) throws Exception {
        // فتح Selector
        Selector selector = Selector.open();

        // فتح قناة خادم Socket
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // تسجيل القناة مع Selector
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("بدأ الخادم على الميناء 8080");

        while (true) {
            selector.select(); // انتظار حتى تحدث الأحداث
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // قبول اتصال جديد
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("تم الاتصال بالعميل");
                } else if (key.isReadable()) {
                    // قراءة البيانات من العميل
                    SocketChannel client = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    int bytesRead = client.read(buffer);
                    if (bytesRead == -1) {
                        client.close();
                    } else {
                        buffer.flip();
                        System.out.println("تم الاستقبال: " + new String(buffer.array(), 0, bytesRead));
                        buffer.clear();
                    }
                }
            }
        }
    }
}
```

### نصائح لاستخدام NIO
- **إدارة الحافظة**: دائمًا `flip()` بعد كتابة في الحافظة وقبل القراءة، و `clear()` عند إعادة استخدامها.
- **غير متزامن**: استخدم `configureBlocking(false)` و `Selector` للبرامج الشبكية قابلة للتوسيع.
- **الأداء**: NIO يلمع في السيناريوهات التي تحتوي على العديد من الإتصالات المتزامن أو نقل البيانات الكبيرة.

أعلمني إذا كنت ترغب في غوص أعمق في أي جزء معين!