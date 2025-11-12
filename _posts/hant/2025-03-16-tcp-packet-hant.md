---
audio: false
generated: true
lang: hant
layout: post
title: 解碼 TCP 封包的 C 程式
translated: true
type: note
---

在 C 語言中解碼 TCP 封包涉及捕獲原始網路數據（通常使用原始通訊端或封包捕獲機制），然後逐步解析標頭：乙太網標頭（如果存在）、IP 標頭，最後是 TCP 標頭。由於 TCP 運行在 IP 之上，您需要先提取 IP 標頭以定位封包中的 TCP 區段。為簡化說明，我假設我們使用 IPv4 和捕獲 IP 封包的原始通訊端（不包含乙太網層）。

以下是一個 C 程式，使用原始通訊端捕獲 TCP 封包，解碼 IP 標頭，然後解碼 TCP 標頭以顯示關鍵字段，如來源/目的地連接埠、序號、確認號、標誌和視窗大小。

---

### 用於解碼 TCP 封包的 C 程式

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // For struct iphdr
#include <netinet/tcp.h>  // For struct tcphdr

// 以人類可讀形式列印 TCP 標誌
void print_tcp_flags(struct tcphdr *tcp) {
    printf("Flags: ");
    if (tcp->syn) printf("SYN ");
    if (tcp->ack) printf("ACK ");
    if (tcp->fin) printf("FIN ");
    if (tcp->rst) printf("RST ");
    if (tcp->psh) printf("PSH ");
    if (tcp->urg) printf("URG ");
    printf("\n");
}

int main() {
    int sock_fd;
    char buffer[65535]; // Max IP packet size
    struct sockaddr_in source_addr, dest_addr;

    // 建立原始通訊端以捕獲 TCP 封包
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("Socket creation failed (run as root?)");
        exit(EXIT_FAILURE);
    }

    printf("Listening for TCP packets...\n");

    while (1) {
        // 接收原始封包
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("Receive failed");
            continue;
        }

        // IP 標頭 (struct iphdr) 位於封包開頭
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihl 以 32 位元字為單位，轉換為位元組

        // 檢查是否為 IPv4 封包且協議為 TCP
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // TCP 標頭位於 IP 標頭之後
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // 提取來源和目的地 IP 地址
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // 解碼並列印 TCP 封包詳細資訊
            printf("\n--- TCP Packet ---\n");
            printf("Source IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("Dest IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("Source Port: %u\n", ntohs(tcp->source));
            printf("Dest Port: %u\n", ntohs(tcp->dest));
            printf("Sequence Number: %u\n", ntohl(tcp->seq));
            printf("Acknowledgment Number: %u\n", ntohl(tcp->ack_seq));
            printf("Data Offset: %d bytes\n", tcp->doff * 4); // TCP 標頭長度
            print_tcp_flags(tcp);
            printf("Window Size: %u\n", ntohs(tcp->window));
            printf("Checksum: 0x%04x\n", ntohs(tcp->check));
            printf("Urgent Pointer: %u\n", ntohs(tcp->urg_ptr));

            // 有效負載（TCP 標頭後的數據）
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("Payload Length: %d bytes\n", payload_len);
                printf("Payload (first 16 bytes): ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("No payload\n");
            }
        }
    }

    close(sock_fd); // 在此循環中無法到達，但為良好實踐
    return 0;
}
```

---

### 運作原理

1. **通訊端設定**：
   - `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` 建立一個原始通訊端，用於捕獲所有發往主機的 TCP 封包。這需要 root 權限 (`sudo`)。

2. **封包捕獲**：
   - `recvfrom()` 抓取原始 IP 封包，其中包括 IP 標頭、TCP 標頭和有效負載。

3. **IP 標頭解析**：
   - `struct iphdr` 定義 IPv4 標頭（來自 `<netinet/ip.h>`）。
   - `ihl`（IP 標頭長度）乘以 4 以獲得位元組偏移量，因為它以 32 位元字為單位測量。
   - 檢查 `version == 4` 和 `protocol == IPPROTO_TCP` 以確保是 IPv4 TCP 封包。

4. **TCP 標頭解析**：
   - `struct tcphdr`（來自 `<netinet/tcp.h>`）定義 TCP 標頭，緊接在 IP 標頭之後開始。
   - 關鍵字段：
     - `source` 和 `dest`：來源和目的地連接埠（使用 `ntohs` 從網路位元組順序轉換為主機位元組順序）。
     - `seq` 和 `ack_seq`：序號和確認號（使用 `ntohl` 進行 32 位元轉換）。
     - `doff`：數據偏移量（TCP 標頭長度，以位元組為單位，同樣乘以 4）。
     - `syn`、`ack`、`fin` 等：指示封包類型的標誌。
     - `window`：接收端視窗大小。
     - `check`：校驗和（為簡化，此處未驗證）。
     - `urg_ptr`：緊急指針（與 URG 標誌一起使用）。

5. **有效負載提取**：
   - 有效負載從 TCP 標頭之後開始。其長度計算為：`總位元組數 - IP 標頭長度 - TCP 標頭長度`。
   - 有效負載的前 16 個位元組以十六進制形式列印。

---

### 編譯與使用
- 編譯：`gcc tcp_decode.c -o tcp_decode`
- 執行（需 root 權限）：`sudo ./tcp_decode`
- 範例輸出（當存在 TCP 流量時，例如瀏覽網頁）：
  ```
  Listening for TCP packets...

  --- TCP Packet ---
  Source IP: 192.168.1.100
  Dest IP: 93.184.216.34
  Source Port: 54321
  Dest Port: 80
  Sequence Number: 123456789
  Acknowledgment Number: 987654321
  Data Offset: 20 bytes
  Flags: SYN
  Window Size: 64240
  Checksum: 0x1a2b
  Urgent Pointer: 0
  No payload
  ```

---

### 關鍵結構
- **IP 標頭 (`struct iphdr`)**：
  ```c
  struct iphdr {
      unsigned int ihl:4;    // 標頭長度（以 32 位元字為單位）
      unsigned int version:4;// IP 版本（4 表示 IPv4）
      uint8_t tos;           // 服務類型
      uint16_t tot_len;      // 總長度
      uint16_t id;           // 識別碼
      uint16_t frag_off;     // 分段偏移
      uint8_t ttl;           // 存活時間
      uint8_t protocol;      // 協議（6 表示 TCP）
      uint16_t check;        // 校驗和
      uint32_t saddr;        // 來源地址
      uint32_t daddr;        // 目的地地址
  };
  ```

- **TCP 標頭 (`struct tcphdr`)**：
  ```c
  struct tcphdr {
      uint16_t source;       // 來源連接埠
      uint16_t dest;         // 目的地連接埠
      uint32_t seq;          // 序號
      uint32_t ack_seq;      // 確認號
      uint16_t doff:4;       // 數據偏移量（標頭長度，以 32 位元字為單位）
      uint16_t res1:4;       // 保留
      uint16_t res2:2;       // 保留
      uint16_t urg:1;        // 緊急標誌
      uint16_t ack:1;        // 確認標誌
      uint16_t psh:1;        // 推送標誌
      uint16_t rst:1;        // 重設標誌
      uint16_t syn:1;        // 同步標誌
      uint16_t fin:1;        // 結束標誌
      uint16_t window;       // 視窗大小
      uint16_t check;        // 校驗和
      uint16_t urg_ptr;      // 緊急指針
  };
  ```

---

### 注意事項
- **Root 權限**：原始通訊端需要 `sudo`，因為它們直接訪問網路堆疊。
- **混雜模式**：此程式僅捕獲發往主機的封包。要捕獲所有流量（如 Wireshark），您需要 `libpcap` 或不同的方法（例如，使用混雜模式的 `PF_PACKET` 通訊端）。
- **位元組順序**：使用 `ntohs`（16 位元）和 `ntohl`（32 位元）將網路位元組順序（大端序）轉換為主機位元組順序。
- **限制**：此程式不驗證校驗和或處理分段封包。

如果您想進一步改進（例如，添加校驗和驗證或過濾特定連接埠），請告訴我！