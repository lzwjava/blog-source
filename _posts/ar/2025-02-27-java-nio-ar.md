---
audio: false
generated: true
lang: ar
layout: post
title: استخدام إن آي أو في جافا
translated: true
type: note
---

دعوني أوضح كيفية استخدام NIO (الإدخال/الإخراج الجديد) في Java مع بعض الأمثلة العملية. Java NIO هي واجهة برمجة تطبيقات غير معيقة (non-blocking I/O) توفر طريقة أكثر كفاءة للتعامل مع عمليات الإدخال/الإخراج مقارنة بحزمة java.io التقليدية.

إليك تفصيلًا للمكونات الرئيسية ومثالًا بسيطًا:

### المكونات الرئيسية في NIO
1.  **Buffers**: حاويات للبيانات (مثل `ByteBuffer`).
2.  **Channels**: تدفقات لقراءة/كتابة البيانات (مثل `FileChannel`، `SocketChannel`).
3.  **Selectors**: لتعددية الإرسال (multiplexing) للعديد من القنوات في الوضع غير المعيق.

### مثال أساسي: قراءة ملف باستخدام NIO
إليك كيف يمكنك قراءة ملف باستخدام `FileChannel` و `ByteBuffer`:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // افتح قناة ملف
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"), 
                StandardOpenOption.READ
            );

            // خصص buffer
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // اقرأ البيانات إلى buffer
            while (fileChannel.read(buffer) > 0) {
                // اقلب buffer للتحضير للقراءة
                buffer.flip();

                // معالجة البيانات
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // امسح buffer للقراءة التالية
                buffer.clear();
            }

            // أغلق القناة
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### كيف يعمل
1.  **FileChannel**: يفتح اتصالاً بالملف.
2.  **ByteBuffer**: يعمل كتخزين مؤقت للبيانات. تقوم بتحديد حجمه (مثل 1024 بايت).
3.  **عمليات Buffer**:
    - `flip()`: يحضر الـ buffer ليتم قراءته بعد كتابة البيانات فيه.
    - `clear()`: يعيد ضبط الـ buffer للجزء التالي من البيانات.
4.  **القراءة**: تملأ الدالة `read()` الـ buffer، وتقوم باستخراج البيانات بايتًا بايتًا.

---

### الكتابة إلى ملف باستخدام NIO
إليك مثالاً لكتابة البيانات إلى ملف:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // افتح قناة ملف للكتابة
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"), 
                StandardOpenOption.CREATE, 
                StandardOpenOption.WRITE
            );

            // البيانات المراد كتابتها
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // ضع البيانات في buffer
            buffer.put(data.getBytes());

            // اقلب buffer للتحضير للكتابة
            buffer.flip();

            // اكتب من buffer إلى الملف
            fileChannel.write(buffer);

            // أغلق القناة
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### مثال غير معيق باستخدام Selector
لبرمجة الشبكات (مثل الخادم)، يمكنك استخدام `Selector` مع `SocketChannel`:

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
        // افتح selector
        Selector selector = Selector.open();

        // افتح قناة مقبس خادم
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // سجل القناة مع selector
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("Server started on port 8080");

        while (true) {
            selector.select(); // احجب حتى تحدث الأحداث
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // اقبل اتصالاً جديدًا
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("Client connected");
                } else if (key.isReadable()) {
                    // اقرأ البيانات من العميل
                    SocketChannel client = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    int bytesRead = client.read(buffer);
                    if (bytesRead == -1) {
                        client.close();
                    } else {
                        buffer.flip();
                        System.out.println("Received: " + new String(buffer.array(), 0, bytesRead));
                        buffer.clear();
                    }
                }
            }
        }
    }
}
```

### نصائح لاستخدام NIO
-   **إدارة Buffer**: دائماً استخدم `flip()` بعد الكتابة إلى buffer وقبل القراءة منه، واستخدم `clear()` عند إعادة استخدامه.
-   **الوضع غير المعيق**: استخدم `configureBlocking(false)` و `Selector` للتطبيقات الشبكية القابلة للتوسع.
-   **الأداء**: NIO تتفوق في السيناريوهات التي تحتوي على العديد من الاتصالات المتزامنة أو نقل بيانات كبير.

دعني أعلم إذا كنت ترغب في شرح أعمق لأي جزء محدد!