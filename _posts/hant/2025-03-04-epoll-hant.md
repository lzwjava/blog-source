---
audio: false
generated: true
lang: hant
layout: post
title: 在 Linux 中使用 epoll
translated: true
type: note
---

`epoll` 是一個 Linux 系統呼叫，專為高效監控多個檔案描述符的事件而設計，例如當資料可讀取或通訊端準備好寫入時。它在網路程式設計中特別有用，因為伺服器可能需要同時處理多個連線。與舊式機制如 `select` 或 `poll` 相比，`epoll` 在處理大量檔案描述符時具有更好的擴展性，因為它避免了重複掃描所有描述符的準備狀態。

以下是在 Linux 中使用 `epoll` 的逐步指南，隨後是一個簡單的伺服器範例，該伺服器接受連線並回傳接收到的資料。

---

## 使用 `epoll` 的步驟

### 1. **建立 Epoll 實例**
要開始使用 `epoll`，首先需要建立一個 epoll 實例，該實例由一個檔案描述符表示。使用 `epoll_create1` 系統呼叫：

```c
int epoll_fd = epoll_create1(0);
```
- **參數**：傳遞 `0` 用於基本用法（無特殊標誌）。高級場景可使用如 `EPOLL_CLOEXEC` 等標誌。
- **回傳值**：成功時回傳檔案描述符 (`epoll_fd`)，錯誤時回傳 `-1`（檢查 `errno` 以獲取詳細資訊）。

舊的 `epoll_create` 函數類似，但接受一個大小提示（現已忽略），因此推薦使用 `epoll_create1`。

### 2. **添加要監控的檔案描述符**
使用 `epoll_ctl` 向 epoll 實例註冊檔案描述符（例如通訊端），並指定要監控的事件：

```c
struct epoll_event ev;
ev.events = EPOLLIN;  // 監控可讀性
ev.data.fd = some_fd; // 要監控的檔案描述符
epoll_ctl(epoll_fd, EPOLL_CTL_ADD, some_fd, &ev);
```
- **參數**：
  - `epoll_fd`：epoll 實例的檔案描述符。
  - `EPOLL_CTL_ADD`：添加檔案描述符的操作。
  - `some_fd`：要監控的檔案描述符（例如通訊端）。
  - `&ev`：指向 `struct epoll_event` 的指標，用於定義事件和可選的使用者資料。
- **常見事件**：
  - `EPOLLIN`：資料可讀取。
  - `EPOLLOUT`：準備好寫入。
  - `EPOLLERR`：發生錯誤。
  - `EPOLLHUP`：掛斷（例如連線關閉）。
- **使用者資料**：`struct epoll_event` 中的 `data` 欄位可以儲存檔案描述符（如上所示）或其他資料（例如指標），以便在事件發生時識別來源。

### 3. **等待事件**
使用 `epoll_wait` 阻塞並等待監控的檔案描述符上的事件：

```c
struct epoll_event events[MAX_EVENTS];
int nfds = epoll_wait(epoll_fd, events, MAX_EVENTS, -1);
```
- **參數**：
  - `epoll_fd`：epoll 實例。
  - `events`：用於儲存觸發事件的陣列。
  - `MAX_EVENTS`：要回傳的最大事件數（陣列大小）。
  - `-1`：超時時間（毫秒）（`-1` 表示無限期等待；`0` 表示立即回傳）。
- **回傳值**：具有事件的檔案描述符數量 (`nfds`)，錯誤時回傳 `-1`。

### 4. **處理事件**
循環遍歷 `epoll_wait` 回傳的事件並進行處理：

```c
for (int i = 0; i < nfds; i++) {
    if (events[i].events & EPOLLIN) {
        // 檔案描述符 events[i].data.fd 可讀取
    }
}
```
- 使用位元運算（例如 `events[i].events & EPOLLIN`）檢查 `events` 欄位以確定事件類型。
- 使用 `events[i].data.fd` 識別哪個檔案描述符觸發了事件。

### 5. **管理檔案描述符（可選）**
- **移除**：使用 `epoll_ctl` 和 `EPOLL_CTL_DEL` 停止監控檔案描述符：
  ```c
  epoll_ctl(epoll_fd, EPOLL_CTL_DEL, some_fd, NULL);
  ```
- **修改**：使用 `EPOLL_CTL_MOD` 調整事件：
  ```c
  ev.events = EPOLLOUT; // 更改為監控可寫性
  epoll_ctl(epoll_fd, EPOLL_CTL_MOD, some_fd, &ev);
  ```

---

## 關鍵概念

### **水平觸發 vs 邊緣觸發**
- **水平觸發（預設）**：只要條件持續存在（例如資料未被讀取），`epoll` 會重複通知。適用於大多數簡單情況。
- **邊緣觸發 (`EPOLLET`)**：僅在狀態變化時（例如新資料到達）通知一次。需要讀取/寫入所有資料直到 `EAGAIN` 以避免遺漏事件；效率更高但更複雜。
- 如果使用邊緣觸發模式，請在 `ev.events` 中設置 `EPOLLET`（例如 `EPOLLIN | EPOLLET`）。

### **非阻塞 I/O**
`epoll` 通常與非阻塞檔案描述符配對使用，以防止在 I/O 操作時阻塞。使用以下方式將通訊端設置為非阻塞模式：

```c
fcntl(fd, F_SETFL, fcntl(fd, F_GETFL) | O_NONBLOCK);
```

---

## 範例：簡單回顯伺服器

以下是一個基本範例，展示如何使用 `epoll` 來接受連線並將資料回傳給客戶端。為簡化起見，使用水平觸發模式。

```c
#include <sys/epoll.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#define MAX_EVENTS 10
#define PORT 8080

int main() {
    // 建立監聽通訊端
    int listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (listen_fd == -1) { perror("socket"); exit(1); }

    struct sockaddr_in addr = { .sin_family = AF_INET, .sin_addr.s_addr = INADDR_ANY, .sin_port = htons(PORT) };
    if (bind(listen_fd, (struct sockaddr*)&addr, sizeof(addr)) == -1) { perror("bind"); exit(1); }
    if (listen(listen_fd, 5) == -1) { perror("listen"); exit(1); }

    // 將監聽通訊端設置為非阻塞
    fcntl(listen_fd, F_SETFL, fcntl(listen_fd, F_GETFL) | O_NONBLOCK);

    // 建立 epoll 實例
    int epoll_fd = epoll_create1(0);
    if (epoll_fd == -1) { perror("epoll_create1"); exit(1); }

    // 將監聽通訊端添加到 epoll
    struct epoll_event ev, events[MAX_EVENTS];
    ev.events = EPOLLIN; // 水平觸發
    ev.data.fd = listen_fd;
    if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, listen_fd, &ev) == -1) { perror("epoll_ctl"); exit(1); }

    // 事件循環
    while (1) {
        int nfds = epoll_wait(epoll_fd, events, MAX_EVENTS, -1);
        if (nfds == -1) { perror("epoll_wait"); exit(1); }

        for (int i = 0; i < nfds; i++) {
            int fd = events[i].data.fd;

            if (fd == listen_fd) {
                // 接受新連線
                int client_fd = accept(listen_fd, NULL, NULL);
                if (client_fd == -1) { perror("accept"); continue; }

                // 將客戶端通訊端設置為非阻塞
                fcntl(client_fd, F_SETFL, fcntl(client_fd, F_GETFL) | O_NONBLOCK);

                // 將客戶端通訊端添加到 epoll
                ev.events = EPOLLIN;
                ev.data.fd = client_fd;
                if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, client_fd, &ev) == -1) {
                    perror("epoll_ctl: client_fd");
                    close(client_fd);
                }
            } else {
                // 處理客戶端資料
                char buf[1024];
                ssize_t n = read(fd, buf, sizeof(buf));
                if (n <= 0) {
                    // 錯誤或 EOF：關閉並從 epoll 中移除
                    if (n == -1 && (errno == EAGAIN || errno == EWOULDBLOCK)) continue;
                    close(fd);
                    epoll_ctl(epoll_fd, EPOLL_CTL_DEL, fd, NULL);
                } else {
                    // 回傳資料
                    write(fd, buf, n); // 注意：在實際應用中，需處理部分寫入的情況
                }
            }
        }
    }

    close(epoll_fd);
    close(listen_fd);
    return 0;
}
```

### 範例說明
- **監聽通訊端**：監控 `EPOLLIN` 以檢測新連線。
- **客戶端通訊端**：同樣監控 `EPOLLIN` 以檢測傳入資料。
- **簡化處理**：假設 `write` 操作完全成功。在生產環境中，應緩衝資料並使用 `EPOLLOUT` 處理部分寫入。
- **錯誤處理**：在錯誤或 EOF 時關閉通訊端並從 epoll 中移除。

---

## 總結
`epoll` 提供了在 Linux 中高效處理多個檔案描述符的方法：
1. 使用 `epoll_create1` 建立實例。
2. 使用 `epoll_ctl` 註冊檔案描述符和事件。
3. 使用 `epoll_wait` 等待事件。
4. 在循環中處理事件，根據需要調整監控的事件或移除描述符。

對於簡單應用，推薦使用水平觸發模式。對於高效能需求，可考慮使用邊緣觸發模式並仔細處理所有可用資料。為達到最佳效果，請始終將 `epoll` 與非阻塞 I/O 配對使用。