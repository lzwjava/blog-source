---
audio: false
generated: true
lang: hi
layout: post
title: जावा में एनआईओ का उपयोग
translated: true
type: note
---

मैं Java में NIO (New Input/Output) का उपयोग कैसे करें, इसे कुछ व्यावहारिक उदाहरणों के साथ समझाता हूँ। Java NIO एक नॉन-ब्लॉकिंग I/O API है जो पारंपरिक java.io पैकेज की तुलना में I/O ऑपरेशन्स को हैंडल करने का एक अधिक कुशल तरीका प्रदान करता है।

यहाँ मुख्य घटकों का विवरण और एक सरल उदाहरण दिया गया है:

### मुख्य NIO घटक
1.  **Buffers**: डेटा के कंटेनर (उदाहरण के लिए, `ByteBuffer`)।
2.  **Channels**: डेटा पढ़ने/लिखने के लिए स्ट्रीम (उदाहरण के लिए, `FileChannel`, `SocketChannel`)।
3.  **Selectors**: नॉन-ब्लॉकिंग मोड में एकाधिक चैनलों को मल्टीप्लेक्स करने के लिए।

### बेसिक उदाहरण: NIO के साथ एक फ़ाइल पढ़ना
यहाँ बताया गया है कि आप `FileChannel` और `ByteBuffer` का उपयोग करके एक फ़ाइल कैसे पढ़ सकते हैं:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // एक फ़ाइल चैनल खोलें
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"), 
                StandardOpenOption.READ
            );

            // एक बफ़र आवंटित करें
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // बफ़र में डेटा पढ़ें
            while (fileChannel.read(buffer) > 0) {
                // पढ़ने के लिए तैयार करने के लिए बफ़र को फ्लिप करें
                buffer.flip();

                // डेटा को प्रोसेस करें
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // अगले रीड के लिए बफ़र साफ़ करें
                buffer.clear();
            }

            // चैनल बंद करें
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### यह कैसे काम करता है
1.  **FileChannel**: फ़ाइल से कनेक्शन खोलता है।
2.  **ByteBuffer**: डेटा के लिए एक अस्थायी स्टोरेज के रूप में कार्य करता है। आप इसका आकार आवंटित करते हैं (उदाहरण के लिए, 1024 बाइट्स)।
3.  **Buffer Operations**:
    - `flip()`: इसमें डेटा लिखने के बाद बफ़र को पढ़ने के लिए तैयार करता है।
    - `clear()`: डेटा के अगले हिस्से के लिए बफ़र को रीसेट करता है।
4.  **Reading**: `read()` मेथड बफ़र को भरती है, और आप डेटा को बाइट-बाइट निकालते हैं।

---

### NIO के साथ एक फ़ाइल में लिखना
यहाँ एक फ़ाइल में डेटा लिखने का एक उदाहरण दिया गया है:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // लिखने के लिए एक फ़ाइल चैनल खोलें
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"), 
                StandardOpenOption.CREATE, 
                StandardOpenOption.WRITE
            );

            // लिखने के लिए डेटा
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // बफ़र में डेटा डालें
            buffer.put(data.getBytes());

            // लिखने के लिए तैयार करने के लिए बफ़र को फ्लिप करें
            buffer.flip();

            // फ़ाइल में बफ़र लिखें
            fileChannel.write(buffer);

            // चैनल बंद करें
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### Selector के साथ नॉन-ब्लॉकिंग उदाहरण
नेटवर्क प्रोग्रामिंग (उदाहरण के लिए, एक सर्वर) के लिए, आप `SocketChannel` के साथ `Selector` का उपयोग कर सकते हैं:

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

        // सेलेक्टर के साथ चैनल रजिस्टर करें
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("Server started on port 8080");

        while (true) {
            selector.select(); // तब तक ब्लॉक रहे जब तक इवेंट्स नहीं होते
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
-   **Buffer Management**: बफ़र में लिखने के बाद और पढ़ने से पहले हमेशा `flip()` करें, और इसे दोबारा उपयोग करते समय `clear()` करें।
-   **Non-Blocking**: स्केलेबल नेटवर्क ऐप्स के लिए `configureBlocking(false)` और `Selector` का उपयोग करें।
-   **Performance**: NIO बहुत सारे समवर्ती कनेक्शन या बड़े डेटा ट्रांसफर के परिदृश्य में बेहतर प्रदर्शन करता है।

मुझे बताएं अगर आप किसी विशिष्ट भाग में गहराई से जाना चाहते हैं!