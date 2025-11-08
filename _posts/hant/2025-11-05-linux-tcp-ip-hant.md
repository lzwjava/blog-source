---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Linux C 語言 TCP/IP 編程
translated: true
type: note
---

### Linux 中的 TCP/IP 協定：概述及在 C 語言中的應用

在 Linux 中，TCP（傳輸控制協定）和 IP（網際網路協定）是核心網路協定，**於核心層**實作為 Linux TCP/IP 堆疊的一部分。此堆疊負責處理封包路由、壅塞控制和連線管理等底層細節。使用者空間應用程式（例如您的 C 程式）透過 **Berkeley sockets API**（亦稱為 POSIX sockets）與此堆疊互動，該 API 提供了建立網路連線的標準化方式。

您無需自行實作 TCP/IP——核心會處理這部分。相反地，您使用 sockets API 來與核心「對話」。此 API **內建於 Linux 的標準 C 函式庫（glibc）** 中，因此無需安裝或連結獨立的「TCP/IP 函式庫」。所有功能均由 `libc`（GNU C 函式庫）提供。

#### 關鍵函式庫與標頭檔
- **主要函式庫**：`libc`（glibc）。所有 socket 函式均包含於此。隱式連結您的程式（通常使用 `gcc` 時會自動完成）。
  - 位置：通常為 `/lib/x86_64-linux-gnu/libc.so.6`（或類似路徑，取決於您的架構和發行版）。您可透過 `ldd /bin/ls` 或 `locate libc.so` 尋找。
- **標頭檔**（用於宣告）：這些屬於 Linux 開發標頭檔的一部分。
  - `<sys/socket.h>`：核心 socket 函式（例如 `socket()`、`bind()`、`connect()`）。
  - `<netinet/in.h>`：網際網路位址結構（例如 IPv4 用的 `struct sockaddr_in`）。
  - `<arpa/inet.h>`：位址轉換函式（例如 `inet_addr()`）。
  - `<sys/types.h>`：基礎型別（通常間接引入）。
  - 位置：通常為 `/usr/include/`（例如 `/usr/include/sys/socket.h`）。若遺失開發標頭檔請安裝（例如在 Debian 系系統上使用 `sudo apt install libc6-dev`）。

在 Linux 上無需額外標記如 `-lsocket`（與某些舊版 Unix 系統不同）。僅需使用 `gcc your_program.c -o your_program` 編譯即可。

#### 基礎範例：C 語言中的簡易 TCP 客戶端
以下是一個極簡的 TCP 客戶端，用於連線至伺服器（例如 example.com 的 80 埠）。此範例展示 sockets API 的使用方式。

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>  // 用於 close()

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);  // 建立 TCP socket（AF_INET 用於 IPv4，SOCK_STREAM 用於 TCP）
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);  // 主機至網路位元組順序
    inet_pton(AF_INET, "93.184.216.34", &server_addr.sin_addr);  // example.com 的 IP

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

- 編譯：`gcc -o tcp_client tcp_client.c`
- 執行：`./tcp_client`

若為伺服器，您需使用 `bind()`、`listen()` 和 `accept()` 而非 `connect()`。

#### 延伸學習資源
- **Man Pages**：在 Linux 系統上執行 `man socket` 或 `man 7 ip` 以獲取詳細文件。
- **核心層面**：若您意指核心層級的實作，請查閱 `/usr/src/linux/net/ipv4/`（TCP）或 `/usr/src/linux/net/ipv6/`（IPv6）中的原始碼。使用 `sudo apt install linux-headers-$(uname -r)` 安裝核心標頭檔。
- 資源：
  - [C 語言 Socket 程式設計 (GeeksforGeeks)](https://www.geeksforgeeks.org/c/socket-programming-cc/)
  - [使用 TCP/IP 進行 Linux Socket 程式設計 (IBM Developer)](https://developer.ibm.com/tutorials/l-sock/)

若這並非您所指的內容（例如核心模組或其他），請提供更多細節！