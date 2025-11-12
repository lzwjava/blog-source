---
audio: false
generated: true
lang: hant
layout: post
title: 解碼UDP封包的C程式
translated: true
type: note
---

以下是在 C 語言中解析 UDP 封包的範例。這段程式碼展示了如何接收 UDP 封包並提取其關鍵組件：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

// UDP 標頭結構
struct udp_header {
    uint16_t source_port;      // 來源連接埠
    uint16_t dest_port;       // 目的連接埠
    uint16_t length;          // UDP 封包長度（標頭 + 資料）
    uint16_t checksum;        // 檢查碼
};

void decode_udp_packet(unsigned char* buffer, int size) {
    // 假設 IP 標頭為 20 位元組（不含選項）
    struct udp_header* udp = (struct udp_header*)(buffer + 20);
    
    printf("\nUDP 標頭\n");
    printf("來源連接埠: %u\n", ntohs(udp->source_port));
    printf("目的連接埠: %u\n", ntohs(udp->dest_port));
    printf("長度: %u\n", ntohs(udp->length));
    printf("檢查碼: 0x%04x\n", ntohs(udp->checksum));
    
    // 計算資料長度與指標
    int udp_header_size = 8;  // UDP 標頭為 8 位元組
    int data_length = ntohs(udp->length) - udp_header_size;
    unsigned char* data = buffer + 20 + udp_header_size;
    
    printf("資料: ");
    for(int i = 0; i < data_length && i < 20; i++) {  // 最多顯示前 20 位元組
        printf("%02x ", data[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    unsigned char buffer[65535];  // 最大 UDP 封包大小
    
    // 建立 UDP socket
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Socket 建立失敗");
        return 1;
    }
    
    // 初始化伺服器位址
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345);  // 範例連接埠
    
    // 綁定 socket
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("綁定失敗");
        close(sockfd);
        return 1;
    }
    
    printf("正在監聽連接埠 12345 的 UDP 封包...\n");
    
    while (1) {
        socklen_t client_len = sizeof(client_addr);
        int received_bytes = recvfrom(sockfd, buffer, sizeof(buffer), 0,
                                    (struct sockaddr*)&client_addr, &client_len);
                                    
        if (received_bytes < 0) {
            perror("接收失敗");
            continue;
        }
        
        decode_udp_packet(buffer, received_bytes);
    }
    
    close(sockfd);
    return 0;
}
```

這段程式碼的功能如下：

1. 定義符合 UDP 封包標頭格式的 `udp_header` 結構：
   - 來源連接埠（16 位元）
   - 目的連接埠（16 位元）
   - 長度（16 位元）
   - 檢查碼（16 位元）

2. 建立 UDP socket 並綁定到連接埠 12345（可自行更改連接埠號）。

3. `decode_udp_packet` 函式：
   - 接收原始封包緩衝區作為輸入
   - 假設 UDP 標頭前有 20 位元組的 IP 標頭（注意：若存在 IP 選項時長度可能變化）
   - 使用 `ntohs` 將標頭欄位從網路位元組順序（大端序）轉換為主機位元組順序
   - 列印標頭資訊
   - 提取並顯示承載資料

編譯與執行方式：
```bash
gcc udp_decoder.c -o udp_decoder
sudo ./udp_decoder  # 因使用原始 socket 需要 sudo 權限
```

重要注意事項：
1. 此為基礎範例 - 實際應用可能需要：
   - 封包大小的錯誤檢查
   - 處理 IP 標頭選項（可變長度）
   - 檢查碼驗證
   - 更複雜的資料處理

2. 測試方法：
   - 使用 netcat 發送 UDP 封包：`echo "test" | nc -u 127.0.0.1 12345`
   - 使用封包產生工具

3. 程式碼假設封包包含 IP 標頭。若處理原始 UDP 資料，請移除 +20 的偏移量。

4. 於正式環境使用時，請增加錯誤處理機制，並可考慮使用 `<netinet/udp.h>` 中的 `struct udphdr` 取代自訂結構。

需要針對任何特定部分進一步說明或展示程式碼的變化形式嗎？