---
audio: false
generated: true
lang: hant
layout: post
title: 網絡系統調用
translated: true
type: note
---

在 Linux/Unix 等作業系統中，網路功能最底層的系統呼叫，特別是建立 TCP 連線的部分，源自 Berkeley Sockets API（通常簡稱為「sockets」）。這些系統呼叫會直接與核心的網路堆疊互動。針對 TCP 連線最基礎的系統呼叫包括：

1. **`socket()`** - 建立新通訊端
2. **`bind()`** - 為通訊端分配位址（客戶端可選用）
3. **`connect()`** - 初始化與遠端伺服器的連線（用於客戶端）
4. **`listen()`** - 將通訊端標記為接受連線狀態（用於伺服器）
5. **`accept()`** - 接受傳入連線（用於伺服器）
6. **`send()` / `recv()`** - 透過連線傳送或接收資料
7. **`close()`** - 關閉通訊端

這些是您在最低層級會使用的原始系統呼叫，位於任何高階程式庫（如 `libcurl`）或框架之下。以下是一個簡單的 C 語言範例，展示 TCP 客戶端與伺服器建立連線的過程。

---

### TCP 伺服器範例
此程式碼設定一個在連接埠 8080 監聽連線的伺服器，接受連線後傳送訊息。

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

    // 建立通訊端
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 設定伺服器位址結構
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // 綁定至所有位址
    server_addr.sin_port = htons(8080);       // 連接埠 8080

    // 綁定通訊端
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // 監聽連線
    if (listen(server_fd, 3) < 0) { // 允許最多 3 個佇列連線
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port 8080...\n");

    // 接受傳入連線
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }
    printf("Connection accepted\n");

    // 傳送訊息至客戶端
    send(client_fd, message, strlen(message), 0);

    // 清理資源
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### TCP 客戶端範例
此程式碼連線至位於 `127.0.0.1:8080` 的伺服器並讀取訊息。

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

    // 建立通訊端
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // 設定伺服器位址結構
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);              // 連接埠 8080
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr); // 本機位址

    // 連線至伺服器
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Connected to server\n");

    // 接收來自伺服器的訊息
    recv(sock_fd, buffer, sizeof(buffer), 0);
    printf("Server message: %s", buffer);

    // 清理資源
    close(sock_fd);
    return 0;
}
```

---

### 關鍵系統呼叫說明
- **`socket(AF_INET, SOCK_STREAM, 0)`**：建立 TCP 通訊端（`AF_INET` 對應 IPv4，`SOCK_STREAM` 對應 TCP）
- **`bind()`**：將通訊端與本機位址及連接埠關聯（伺服器端）
- **`listen()`**：將通訊端設定為接受連線狀態（伺服器端）
- **`accept()`**：阻塞執行直到客戶端連線，然後回傳用於通訊的新通訊端
- **`connect()`**：與伺服器初始化 TCP 交握程序（客戶端）
- **`send()` / `recv()`**：處理已建立連線上的資料傳輸
- **`close()`**：終止通訊端

這些是使用者空間中 TCP 網路功能的最低層級實作。若需更底層的操作，則需處理核心內部機制（例如 TCP/IP 堆疊本身），這必須透過編寫核心程式碼才能直接存取，無法僅透過系統呼叫實現。

編譯與執行步驟：
1. 將伺服器程式碼存為 `server.c`，客戶端程式碼存為 `client.c`
2. 編譯：`gcc server.c -o server` 與 `gcc client.c -o client`
3. 先執行伺服器：`./server`
4. 在另一個終端機中執行客戶端：`./client`

如需更多詳細說明或深入探討，請隨時告知！