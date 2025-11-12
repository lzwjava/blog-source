---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるNIOの使用
translated: true
type: note
---

Java NIO（New Input/Output）の実践的な使用例を紹介します。Java NIOは非ブロッキングI/O APIで、従来のjava.ioパッケージに比べて効率的なI/O操作を実現します。

### 主なNIOコンポーネント
1. **Buffers**: データを格納するコンテナ（例: `ByteBuffer`）
2. **Channels**: データの読み書きを行うストリーム（例: `FileChannel`, `SocketChannel`）
3. **Selectors**: 非ブロッキングモードで複数のチャネルを多重化する仕組み

### 基本例: NIOでのファイル読み込み
`FileChannel`と`ByteBuffer`を使用したファイルの読み込み方法:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileReader {
    public static void main(String[] args) {
        try {
            // ファイルチャネルを開く
            FileChannel fileChannel = FileChannel.open(
                Paths.get("example.txt"), 
                StandardOpenOption.READ
            );

            // バッファを割り当て
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // データをバッファに読み込み
            while (fileChannel.read(buffer) > 0) {
                // バッファを読み込み用に準備
                buffer.flip();

                // データを処理
                while (buffer.hasRemaining()) {
                    System.out.print((char) buffer.get());
                }

                // 次の読み込みのためにバッファをクリア
                buffer.clear();
            }

            // チャネルを閉じる
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### 動作の仕組み
1. **FileChannel**: ファイルへの接続を開く
2. **ByteBuffer**: データの一時的なストレージとして機能。サイズを割り当て（例: 1024バイト）
3. **バッファ操作**:
   - `flip()`: データ書き込み後、読み込み準備を行う
   - `clear()`: 次のデータチャンクのためにバッファをリセット
4. **読み込み**: `read()`メソッドでバッファを埋め、バイト単位でデータを抽出

---

### NIOでのファイル書き込み
ファイルへのデータ書き込み例:

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // 書き込み用ファイルチャネルを開く
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"), 
                StandardOpenOption.CREATE, 
                StandardOpenOption.WRITE
            );

            // 書き込むデータ
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // データをバッファに格納
            buffer.put(data.getBytes());

            // 書き込み準備のためにバッファをフリップ
            buffer.flip();

            // バッファをファイルに書き込み
            fileChannel.write(buffer);

            // チャネルを閉じる
            fileChannel.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

### Selectorを使用した非ブロッキング例
ネットワークプログラミング（サーバーなど）では、`Selector`と`SocketChannel`を使用:

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
        // セレクターを開く
        Selector selector = Selector.open();

        // サーバーソケットチャネルを開く
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // チャネルをセレクターに登録
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("Server started on port 8080");

        while (true) {
            selector.select(); // イベント発生までブロック
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // 新しい接続を受け入れる
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("Client connected");
                } else if (key.isReadable()) {
                    // クライアントからデータを読み込み
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

### NIO使用時のヒント
- **バッファ管理**: バッファへの書き込み後、読み込み前に必ず`flip()`を呼び出し、再利用時には`clear()`を呼び出す
- **非ブロッキング**: スケーラブルなネットワークアプリには`configureBlocking(false)`と`Selector`を使用
- **パフォーマンス**: NIOは多数の同時接続や大規模データ転送のシナリオで効果を発揮

特定の部分についてさらに詳しく知りたい場合はお知らせください！