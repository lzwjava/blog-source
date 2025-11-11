---
audio: false
generated: true
lang: hant
layout: post
title: Java中的NIO應用
translated: true
type: note
---

讓我用一些實際範例來說明如何在 Java 中使用 NIO（New Input/Output）。Java NIO 是一種非阻塞 I/O API，與傳統的 java.io 套件相比，提供了更高效的 I/O 操作處理方式。

以下是關鍵組件的解析和一個簡單範例：

### 關鍵 NIO 組件
1. **緩衝區（Buffers）**：資料容器（例如 `ByteBuffer`）
2. **通道（Channels）**：讀寫資料的串流（例如 `FileChannel`、`SocketChannel`）
3. **選擇器（Selectors）**：用於在非阻塞模式下多工處理多個通道

### 基礎範例：使用 NIO 讀取檔案
以下是使用 `FileChannel` 和 `ByteBuffer` 讀取檔案的方法：

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // 開啟檔案通道
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"), 
                StandardOpenOption.READ
            );

            // 配置緩衝區
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // 將資料讀入緩衝區
            while (fileChannel.read(buffer) > 0) {
                // 翻轉緩衝區以準備讀取
                buffer.flip();

                // 處理資料
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // 清除緩衝區以進行下一次讀取
                buffer.clear();
            }

            // 關閉通道
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### 運作原理
1. **FileChannel**：開啟與檔案的連接
2. **ByteBuffer**：作為資料的臨時儲存空間，可配置其大小（例如 1024 位元組）
3. **緩衝區操作**：
   - `flip()`：在寫入資料後準備緩衝區以供讀取
   - `clear()`：重置緩衝區以處理下一批資料
4. **讀取**：`read()` 方法填充緩衝區，然後逐位元組提取資料

---

### 使用 NIO 寫入檔案
以下是將資料寫入檔案的範例：

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // 開啟用於寫入的檔案通道
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"), 
                StandardOpenOption.CREATE, 
                StandardOpenOption.WRITE
            );

            // 要寫入的資料
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // 將資料放入緩衝區
            buffer.put(data.getBytes());

            // 翻轉緩衝區以準備寫入
            buffer.flip();

            // 將緩衝區寫入檔案
            fileChannel.write(buffer);

            // 關閉通道
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### 使用選擇器的非阻塞範例
對於網路程式設計（例如伺服器），您可以將 `Selector` 與 `SocketChannel` 搭配使用：

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
        // 開啟選擇器
        Selector selector = Selector.open();

        // 開啟伺服器通訊端通道
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // 向選擇器註冊通道
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("伺服器已在端口 8080 啟動");

        while (true) {
            selector.select(); // 阻塞直到事件發生
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // 接受新連接
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("客戶端已連接");
                } else if (key.isReadable()) {
                    // 從客戶端讀取資料
                    SocketChannel client = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    int bytesRead = client.read(buffer);
                    if (bytesRead == -1) {
                        client.close();
                    } else {
                        buffer.flip();
                        System.out.println("收到: " + new String(buffer.array(), 0, bytesRead));
                        buffer.clear();
                    }
                }
            }
        }
    }
}
```

### 使用 NIO 的提示
- **緩衝區管理**：在寫入緩衝區後和讀取前務必使用 `flip()`，重複使用時使用 `clear()`
- **非阻塞**：使用 `configureBlocking(false)` 和 `Selector` 來實現可擴展的網路應用程式
- **效能**：NIO 在處理大量並行連接或大資料傳輸的場景中表現出色

如果您想深入了解任何特定部分，請告訴我！