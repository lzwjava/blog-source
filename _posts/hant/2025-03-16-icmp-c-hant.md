---
audio: false
generated: true
lang: hant
layout: post
title: C語言編寫的ICMP Ping程式
translated: true
type: note
---

ICMP（網際網路控制訊息協定）是一種網路層協定，用於IP網路中的診斷和錯誤回報。它最著名的應用是透過 `ping` 工具來測試主機之間的連線能力。ICMP訊息直接封裝在IP封包中（無TCP或UDP層），並包含類型、代碼、校驗和與承載資料。對於 `ping` 而言，「回送請求」（類型8）和「回送應答」（類型0）訊息是關鍵。

以下是ICMP在高層次上的運作方式：
1. 發送方（例如你的機器）向目標IP傳送ICMP回送請求。
2. 若目標可達且設定為回應，則會傳回ICMP回送應答。
3. 發送方根據回應到達時間計算往返時間（RTT）。

為了在不使用 `libpcap` 或 `libnet` 等函式庫的情況下，以C語言實現類似 `ping` 的程式，我們將使用原始通訊端（`SOCK_RAW`）直接構造和傳送ICMP封包。這需要root權限（例如 `sudo`），因為原始通訊端繞過了高層抽象。

以下是一個簡化的C程式，用於傳送ICMP回送請求並監聽回送應答，模擬基本的 `ping` 功能。

---

### C語言實現ICMP Ping程式

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <time.h>
#include <errno.h>

// 計算ICMP校驗和
unsigned short checksum(void *b, int len) {
    unsigned short *buf = b;
    unsigned int sum = 0;
    unsigned short result;

    for (sum = 0; len > 1; len -= 2) {
        sum += *buf++;
    }
    if (len == 1) {
        sum += *(unsigned char *)buf;
    }
    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    result = ~sum;
    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("用法：%s <目標IP>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int sock_fd;
    struct sockaddr_in dest_addr;
    char packet[64];  // ICMP標頭 + 部分資料
    struct icmphdr *icmp;
    char recv_buffer[1024];
    struct timespec start, end;

    // 建立ICMP原始通訊端
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock_fd < 0) {
        perror("通訊端建立失敗（請以root權限執行）");
        exit(EXIT_FAILURE);
    }

    // 設定目標地址
    dest_addr.sin_family = AF_INET;
    if (inet_pton(AF_INET, argv[1], &dest_addr.sin_addr) <= 0) {
        perror("無效IP地址");
        close(sock_fd);
        exit(EXIT_FAILURE);
    }

    // 準備ICMP回送請求封包
    memset(packet, 0, sizeof(packet));
    icmp = (struct icmphdr *)packet;
    icmp->type = ICMP_ECHO;        // 類型8：回送請求
    icmp->code = 0;
    icmp->un.echo.id = getpid();   // 使用行程ID作為識別符
    icmp->un.echo.sequence = 1;    // 序號
    for (int i = sizeof(*icmp); i < 64; i++) {
        packet[i] = i;             // 以虛擬資料填充承載
    }
    icmp->checksum = 0;            // 填充封包後計算校驗和
    icmp->checksum = checksum(packet, 64);

    printf("正在 Ping %s...\n", argv[1]);

    for (int i = 0; i < 4; i++) { // 傳送4次ping
        // 記錄傳送時間
        clock_gettime(CLOCK_MONOTONIC, &start);

        // 傳送ICMP回送請求
        if (sendto(sock_fd, packet, 64, 0, (struct sockaddr *)&dest_addr, sizeof(dest_addr)) < 0) {
            perror("傳送失敗");
            close(sock_fd);
            exit(EXIT_FAILURE);
        }

        // 接收ICMP回送應答
        struct sockaddr_in from_addr;
        socklen_t from_len = sizeof(from_addr);
        int bytes_received = recvfrom(sock_fd, recv_buffer, sizeof(recv_buffer), 0,
                                      (struct sockaddr *)&from_addr, &from_len);
        if (bytes_received < 0) {
            perror("接收失敗");
            continue;
        }

        // 記錄接收時間
        clock_gettime(CLOCK_MONOTONIC, &end);

        // 解析接收的IP和ICMP標頭
        struct iphdr *ip = (struct iphdr *)recv_buffer;
        struct icmphdr *icmp_reply = (struct icmphdr *)(recv_buffer + (ip->ihl * 4));
        if (icmp_reply->type == ICMP_ECHOREPLY && icmp_reply->un.echo.id == getpid()) {
            double rtt = (end.tv_sec - start.tv_sec) * 1000.0 +
                         (end.tv_nsec - start.tv_nsec) / 1000000.0;
            printf("%d 位元組來自 %s：序號=%d 時間=%.2f 毫秒\n",
                   bytes_received - (ip->ihl * 4), argv[1], icmp_reply->un.echo.sequence, rtt);
        } else {
            printf("非預期ICMP回應：類型=%d\n", icmp_reply->type);
        }

        sleep(1); // 每次ping之間等待1秒
        icmp->un.echo.sequence++; // 序號遞增
        icmp->checksum = 0;
        icmp->checksum = checksum(packet, 64); // 重新計算校驗和
    }

    close(sock_fd);
    return 0;
}
```

---

### 運作原理

1. **通訊端建立**：
   - `socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)` 建立用於ICMP的原始通訊端，使我們能夠手動構造ICMP封包。

2. **ICMP封包構造**：
   - ICMP標頭（`struct icmphdr`）填充以下內容：
     - `type = ICMP_ECHO`（8）用於回送請求。
     - `code = 0`。
     - `id` 設為行程ID以識別我們的ping。
     - `sequence` 用於追蹤個別請求。
   - 添加承載（虛擬資料），並計算整個封包的校驗和。

3. **傳送**：
   - `sendto()` 將封包傳送至目標IP。由於ICMP在傳輸層以下運作，因此不需要端口。

4. **接收**：
   - `recvfrom()` 捕獲包含ICMP回送應答的原始IP封包。
   - 我們跳過IP標頭（`ihl * 4` 位元組）以取得ICMP標頭。
   - 檢查是否為回送應答（類型0）且與我們的 `id` 匹配。

5. **計時**：
   - `clock_gettime()` 以毫秒為單位測量RTT。

6. **校驗和**：
   - `checksum()` 函式計算ICMP所需的16位元一補數和。

---

### 編譯與使用
- 編譯：`gcc ping.c -o ping`
- 執行（需root權限）：`sudo ./ping 8.8.8.8`
- 範例輸出：
  ```
  正在 Ping 8.8.8.8...
  64 位元組來自 8.8.8.8：序號=1 時間=12.34 毫秒
  64 位元組來自 8.8.8.8：序號=2 時間=11.89 毫秒
  ...
  ```

---

### 注意事項
- **Root權限**：原始通訊端需要 `sudo`，因為它們直接操作網路封包。
- **防火牆**：目標必須回應ICMP回送請求（部分主機可能阻擋此類請求）。
- **簡化說明**：此版本未處理所有邊界情況（例如超時、封包遺失或IP選項）。

這是在用戶空間中使用ICMP所能達到的最低層級。若需更低層級，則需要核心層級程式碼來直接與IP堆疊互動。如有進一步調整需求，請隨時告知！