---
audio: false
generated: true
lang: ja
layout: post
title: NIOをJavaで使用する
translated: true
---

NIO（New Input/Output）のJavaでの使用方法をいくつかの実践的な例を交えて説明します。Java NIOは、非同期I/O APIであり、伝統的なjava.ioパッケージに比べてI/O操作をより効率的に処理する方法を提供します。

以下に、主要なコンポーネントと簡単な例の概要を示します。

### 主要なNIOコンポーネント
1. **バッファ**: データのコンテナ（例：`ByteBuffer`）。
2. **チャネル**: データの読み書き用ストリーム（例：`FileChannel`、`SocketChannel`）。
3. **セレクタ**: 非同期モードでの複数のチャネルのマルチプレクシング。

### 基本的な例：NIOでファイルを読む
`FileChannel`と`ByteBuffer`を使用してファイルを読む方法は以下の通りです：

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

            // バッファを割り当てる
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // データをバッファに読み込む
            while (fileChannel.read(buffer) > 0) {
                // バッファを読み取り準備にするためにフリップ
                buffer.flip();

                // データを処理する
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

### 仕組み
1. **FileChannel**: ファイルへの接続を開く。
2. **ByteBuffer**: データの一時的な保存場所。サイズを割り当てます（例：1024バイト）。
3. **バッファ操作**:
   - `flip()`: データを書き込んだ後にバッファを読み取り準備にする。
   - `clear()`: 次のデータチャンクのためにバッファをリセットする。
4. **読み取り**: `read()`メソッドがバッファを埋め、バイト単位でデータを抽出します。

---

### NIOでファイルに書き込む
ファイルにデータを書き込む例は以下の通りです：

```java
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOFileWriter {
    public static void main(String[] args) {
        try {
            // 書き込み用のファイルチャネルを開く
            FileChannel fileChannel = FileChannel.open(
                Paths.get("output.txt"),
                StandardOpenOption.CREATE,
                StandardOpenOption.WRITE
            );

            // 書き込むデータ
            String data = "Hello, NIO!";
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // データをバッファに入れる
            buffer.put(data.getBytes());

            // バッファを書き込み準備にフリップ
            buffer.flip();

            // バッファをファイルに書き込む
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

### セレクタを使用した非同期例
ネットワークプログラミング（例：サーバー）では、`Selector`と`SocketChannel`を使用できます：

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
        // セレクタを開く
        Selector selector = Selector.open();

        // サーバーソケットチャネルを開く
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(8080));
        serverChannel.configureBlocking(false);

        // チャネルをセレクタに登録
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        System.out.println("サーバーがポート8080で開始されました");

        while (true) {
            selector.select(); // イベントが発生するまでブロック
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();

            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();

                if (key.isAcceptable()) {
                    // 新しい接続を受け入れる
                    SocketChannel client = serverChannel.accept();
                    client.configureBlocking(false);
                    client.register(selector, SelectionKey.OP_READ);
                    System.out.println("クライアントが接続しました");
                } else if (key.isReadable()) {
                    // クライアントからデータを読み取る
                    SocketChannel client = (SocketChannel) key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    int bytesRead = client.read(buffer);
                    if (bytesRead == -1) {
                        client.close();
                    } else {
                        buffer.flip();
                        System.out.println("受信: " + new String(buffer.array(), 0, bytesRead));
                        buffer.clear();
                    }
                }
            }
        }
    }
}
```

### NIOの使用に関するヒント
- **バッファ管理**: 書き込み後にバッファを`flip()`し、読み取り前に`clear()`します。
- **非同期**: スケーラブルなネットワークアプリケーションには`configureBlocking(false)`と`Selector`を使用します。
- **パフォーマンス**: NIOは、多くの同時接続や大量のデータ転送のシナリオで輝きます。

具体的な部分について深く掘り下げたい場合はお知らせください！