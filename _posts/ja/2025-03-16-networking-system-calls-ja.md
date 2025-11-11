---
audio: false
generated: true
lang: ja
layout: post
title: ネットワーキングシステムコール
translated: true
type: note
---

Linux/Unixのようなオペレーティングシステムでは、ネットワーキングのための最も低レベルなシステムコール、特にTCP接続を確立するものは、Berkeley Sockets API（単に「ソケット」と呼ばれることが多い）に由来します。これらのシステムコールはカーネルのネットワーキングスタックと直接対話します。TCP接続における最も基本的なものは以下の通りです：

1. **`socket()`** - 新しいソケットを作成します。
2. **`bind()`** - ソケットにアドレスを割り当てます（クライアント側ではオプション）。
3. **`connect()`** - リモートサーバーへの接続を開始します（クライアント側）。
4. **`listen()`** - ソケットを接続受け付け状態にします（サーバー側）。
5. **`accept()`** - 着信接続を受け入れます（サーバー側）。
6. **`send()` / `recv()`** - 接続を介してデータを送信または受信します。
7. **`close()`** - ソケットを閉じます。

これらは、`libcurl` のような高レベルライブラリやフレームワークの下位層で使用する生のシステムコールです。以下は、TCPクライアントとサーバーが接続を確立する様子をC言語で示した簡単な例です。

---

### TCPサーバー例
このコードは、ポート8080で接続を待ち受け、接続を受け入れ、メッセージを送信するサーバーをセットアップします。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    char *message = "Hello from server!\n";

    // ソケットの作成
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // サーバーアドレス構造体の設定
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // 任意のアドレスにバインド
    server_addr.sin_port = htons(8080);       // ポート8080

    // ソケットのバインド
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // 接続の待機
    if (listen(server_fd, 3) < 0) { // 最大3つの接続をキューイング
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port 8080...\n");

    // 着信接続の受け入れ
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }
    printf("Connection accepted\n");

    // クライアントへのメッセージ送信
    send(client_fd, message, strlen(message), 0);

    // クリーンアップ
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### TCPクライアント例
このコードは `127.0.0.1:8080` のサーバーに接続し、メッセージを読み取ります。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock_fd;
    struct sockaddr_in server_addr;
    char buffer[1024] = {0};

    // ソケットの作成
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // サーバーアドレス構造体の設定
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);              // ポート8080
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr); // ローカルホスト

    // サーバーへの接続
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Connected to server\n");

    // サーバーからのメッセージ受信
    recv(sock_fd, buffer, sizeof(buffer), 0);
    printf("Server message: %s", buffer);

    // クリーンアップ
    close(sock_fd);
    return 0;
}
```

---

### 主要なシステムコールの説明
- **`socket(AF_INET, SOCK_STREAM, 0)`**: TCPソケットを作成します（`AF_INET` はIPv4、`SOCK_STREAM` はTCP用）。
- **`bind()`**: ソケットをローカルアドレスとポートに関連付けます（サーバー側）。
- **`listen()`**: ソケットが接続を受け付ける準備をします（サーバー側）。
- **`accept()`**: クライアントの接続を待機し、接続されると通信用の新しいソケットを返します。
- **`connect()`**: サーバーとのTCPハンドシェイクを開始します（クライアント側）。
- **`send()` / `recv()`**: 確立された接続を介したデータ転送を処理します。
- **`close()`**: ソケットを終了します。

これらはユーザー空間におけるTCPネットワーキングの最も低レベルな操作です。これより下位層では、カーネル内部（例えばTCP/IPスタック自体）を扱うことになり、カーネルコードを書かない限りシステムコールでは直接アクセスできません。

コンパイルと実行方法：
1. サーバーコードを `server.c`、クライアントコードを `client.c` として保存します。
2. コンパイル：`gcc server.c -o server` および `gcc client.c -o client`。
3. まずサーバーを実行：`./server`。
4. 別のターミナルでクライアントを実行：`./client`。

さらに詳細な情報や深掘りが必要な場合はお知らせください！