---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: C言語によるLinux TCP/IPプログラミング
translated: true
type: note
---

### LinuxにおけるTCP/IPプロトコル：概要とC言語での使用方法

Linuxでは、TCP（Transmission Control Protocol）とIP（Internet Protocol）は、Linux TCP/IPスタックの一部として**カーネル内**に実装されたコアネットワーキングプロトコルです。このスタックは、パケットルーティング、輻輳制御、接続管理といった低レベルの詳細を処理します。ユーザー空間アプリケーション（例えば、あなたのCプログラム）は、**Berkeley sockets API**（POSIXソケットとしても知られる）を介してこのスタックと対話します。このAPIは、ネットワーク接続を作成する標準化された方法を提供します。

あなた自身がTCP/IPを実装する必要はありません—カーネルがそれを行います。代わりに、ソケットAPIを使用してカーネルと「対話」します。このAPIは、Linuxでは**標準Cライブラリ（glibc）に組み込まれている**ので、別途「TCP/IPライブラリ」をインストールしたりリンク against したりする必要はありません。すべてが `libc`（GNU C Library）によって提供されます。

#### 主要なライブラリとヘッダー
- **メインライブラリ**: `libc` (glibc)。すべてのソケット関数はここに含まれています。あなたのプログラムをこれと暗黙的にリンクします（通常、`gcc` では自動的です）。
  - 場所: 典型的には `/lib/x86_64-linux-gnu/libc.so.6`（または、アーキテクチャとディストリビューションに応じて類似のパス）。`ldd /bin/ls` または `locate libc.so` で見つけることができます。
- **ヘッダー**（宣言用）: これらはLinux開発ヘッダーの一部です。
  - `<sys/socket.h>`: コアソケット関数（例: `socket()`, `bind()`, `connect()`）。
  - `<netinet/in.h>`: インターネットアドレス構造体（例: IPv4用の `struct sockaddr_in`）。
  - `<arpa/inet.h>`: アドレス変換関数（例: `inet_addr()`）。
  - `<sys/types.h>`: 基本型（しばしば間接的にインクルードされます）。
  - 場所: 通常 `/usr/include/`（例: `/usr/include/sys/socket.h`）。開発ヘッダーが不足している場合はインストールしてください（例: Debianベースのシステムでは `sudo apt install libc6-dev`）。

Linuxでは（いくつかの古いUnixシステムとは異なり）、`-lsocket` のような追加のフラグは必要ありません。単に `gcc your_program.c -o your_program` でコンパイルします。

#### 基本的な例：C言語でのシンプルなTCPクライアント
以下は、サーバー（例: example.com のポート80）に接続する最小限のTCPクライアントです。これはソケットAPIの使用法を示しています。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>  // close()用

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);  // TCPソケットを作成 (AF_INETはIPv4用, SOCK_STREAMはTCP用)
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);  // ホストからネットワークへのバイトオーダー
    inet_pton(AF_INET, "93.184.216.34", &server_addr.sin_addr);  // example.comのIP

    if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        close(sockfd);
        return 1;
    }

    const char* msg = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
    send(sockfd, msg, strlen(msg), 0);

    char buffer[1024];
    int bytes = recv(sockfd, buffer, sizeof(buffer) - 1, 0);
    buffer[bytes] = '\0';
    printf("Response: %s\n", buffer);

    close(sockfd);
    return 0;
}
```

- コンパイル: `gcc -o tcp_client tcp_client.c`
- 実行: `./tcp_client`

サーバーの場合は、`connect()` の代わりに `bind()`, `listen()`, `accept()` を使用します。

#### さらに学ぶためのリソース
- **Manページ**: 詳細なドキュメントについては、Linuxシステムで `man socket` または `man 7 ip` を実行してください。
- **カーネル側**: カーネルレベルの実装を意味する場合は、`/usr/src/linux/net/ipv4/`（TCP）または `/usr/src/linux/net/ipv6/`（IPv6）のソースを確認してください。カーネルヘッダーは `sudo apt install linux-headers-$(uname -r)` でインストールできます。
- リソース:
  - [Socket Programming in C (GeeksforGeeks)](https://www.geeksforgeeks.org/c/socket-programming-cc/)
  - [Programming Linux Sockets with TCP/IP (IBM Developer)](https://developer.ibm.com/tutorials/l-sock/)

これが意図したものではない場合（例えば、カーネルモジュールなど）、詳細を提供してください！