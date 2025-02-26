---
audio: false
lang: hi
layout: post
title: NIO का उपयोग Java में
translated: true
---

मुझे NIO (New Input/Output) का उपयोग Java में कुछ प्रैक्टिकल उदाहरणों के साथ समझाने दो। Java NIO एक नॉन-ब्लॉकिंग I/O API है जो पारंपरिक java.io पैकेज के मुकाबले I/O ऑपरेशंस को अधिक दक्षता से हँडल करने का एक तरीका प्रदान करता है।

यहाँ कुछ प्रमुख घटकों का विवरण और एक सरल उदाहरण है:

### प्रमुख NIO घटक
1. **Buffers**: डेटा के लिए कंटेनर (उदाहरण के लिए, `ByteBuffer`).
2. **Channels**: डेटा पढ़ने/लिखने के लिए स्ट्रीम (उदाहरण के लिए, `FileChannel`, `SocketChannel`).
3. **Selectors**: नॉन-ब्लॉकिंग मोड में कई चैनलों को मल्टीप्लेक्स करने के लिए.

### बेसिक उदाहरण: NIO के साथ फाइल पढ़ना
यहाँ `FileChannel` और `ByteBuffer` का उपयोग करके फाइल पढ़ने का तरीका है:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // एक फाइल चैनल खोलें
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"),
                StandardOpenOption.READ
            );

            // एक बफर आवंटित करें
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // डेटा बफर में पढ़ें
            while (fileChannel.read(buffer) > 0) {
                // बफर को पढ़ने के लिए तैयार करने के लिए फ्लिप करें
                buffer.flip();

                // डेटा को प्रोसेस करें
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // अगले पढ़ने के लिए बफर को क्लियर करें
                buffer.clear();
            }

            // चैनल को बंद करें
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### यह कैसे काम करता है
1. **FileChannel**: फाइल के साथ एक कनेक्शन खोलता है।
2. **ByteBuffer**: डेटा के लिए एक अस्थायी स्टोरेज के रूप में कार्य करता है। आप इसका आकार आवंटित करते हैं (उदाहरण के लिए, 1024 बाइट्स).
3. **Buffer Operations**:
   - `flip()`: डेटा को बफर में लिखने के बाद इसे पढ़ने के लिए तैयार करता है।
   - `clear()`: अगले डेटा चंक के लिए बफर को रीसेट करता है.
4. **Reading**: `read()` विधि बफर को भरती है, और आप डेटा को बाइट-बाइट निकालते हैं।

---

### NIO के साथ फाइल में लिखना
यहाँ एक फाइल में डेटा लिखने का उदाहरण है:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // लिखने के लिए एक फाइल चैनल खोलें
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"),
                StandardOpenOption.CREATE,
                StandardOpenOption.WRITE
            );

            // लिखने के लिए डेटा
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // डेटा को बफर में डालें
            buffer.put(data.getBytes());

            // बफर को लिखने के लिए फ्लिप करें
            buffer.flip();

            // बफर को फाइल में लिखें
            fileChannel.write(buffer);

            // चैनल को बंद करें
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### Selector के साथ नॉन-ब्लॉकिंग उदाहरण
नेटवर्क प्रोग्रामिंग (उदाहरण के लिए, एक सर्वर) के लिए, आप `Selector` के साथ `SocketChannel` का उपयोग कर सकते हैं:

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
        // एक सेलेक्टर खोलें
        Selector selector = Selector.open();

        // एक सर्वर सॉकेट चैनल खोलें
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // चैनल को सेलेक्टर के साथ रजिस्टर करें
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("Server started on port 8080");

        while (true) {
            selector.select(); // घटनाएं होने तक ब्लॉक करें
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // नया कनेक्शन स्वीकार करें
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("Client connected");
                } else if (key.isReadable()) {
                    // क्लाइंट से डेटा पढ़ें
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

### NIO का उपयोग करने के लिए टिप्स
- **Buffer Management**: बफर में लिखने के बाद और पढ़ने से पहले हमेशा `flip()` करें और फिर से उपयोग करने के लिए `clear()` करें।
- **Non-Blocking**: `configureBlocking(false)` और `Selector` का उपयोग करें स्केलेबल नेटवर्क ऐप्स के लिए.
- **Performance**: NIO कई समकालीन कनेक्शंस या बड़े डेटा ट्रांसफर्स के साथ काम करने में चमकता है.

मुझे बताएं अगर आप किसी विशेष हिस्से में गहरी जानकारी चाहते हैं!