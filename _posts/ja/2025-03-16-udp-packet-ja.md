---
audio: false
generated: true
lang: ja
layout: post
title: UDPパケットをデコードするCプログラム
translated: true
type: note
---

以下はC言語でUDPパケットをデコードする例です。このコードはUDPパケットを受信し、その主要な構成要素を抽出する方法を示しています：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

// UDPヘッダー構造体
struct udp_header {
    uint16_t source_port;      // 送信元ポート
    uint16_t dest_port;       // 宛先ポート
    uint16_t length;          // UDPパケットの長さ（ヘッダー + データ）
    uint16_t checksum;        // チェックサム
};

void decode_udp_packet(unsigned char* buffer, int size) {
    // IPヘッダーは20バイトと仮定（オプションなし）
    struct udp_header* udp = (struct udp_header*)(buffer + 20);
    
    printf("\nUDP Header\n");
    printf("Source Port: %u\n", ntohs(udp->source_port));
    printf("Destination Port: %u\n", ntohs(udp->dest_port));
    printf("Length: %u\n", ntohs(udp->length));
    printf("Checksum: 0x%04x\n", ntohs(udp->checksum));
    
    // データ長とポインタを計算
    int udp_header_size = 8;  // UDPヘッダーは8バイト
    int data_length = ntohs(udp->length) - udp_header_size;
    unsigned char* data = buffer + 20 + udp_header_size;
    
    printf("Data: ");
    for(int i = 0; i < data_length && i < 20; i++) {  // 最大20バイトまで表示
        printf("%02x ", data[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    unsigned char buffer[65535];  // 最大UDPパケットサイズ
    
    // UDPソケット作成
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return 1;
    }
    
    // サーバーアドレス初期化
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345);  // 例示用ポート
    
    // ソケットバインド
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(sockfd);
        return 1;
    }
    
    printf("ポート12345でUDPパケットを待機中...\n");
    
    while (1) {
        socklen_t client_len = sizeof(client_addr);
        int received_bytes = recvfrom(sockfd, buffer, sizeof(buffer), 0,
                                    (struct sockaddr*)&client_addr, &client_len);
                                    
        if (received_bytes < 0) {
            perror("Receive failed");
            continue;
        }
        
        decode_udp_packet(buffer, received_bytes);
    }
    
    close(sockfd);
    return 0;
}
```

このコードは以下の処理を行います：

1. UDPパケットヘッダー形式に一致する`udp_header`構造体を定義：
   - 送信元ポート（16ビット）
   - 宛先ポート（16ビット）
   - 長さ（16ビット）
   - チェックサム（16ビット）

2. UDPソケットを作成し、ポート12345にバインド（このポート番号は変更可能）

3. `decode_udp_packet`関数：
   - 生のパケットバッファを入力として受け取る
   - UDPヘッダーの前に20バイトのIPヘッダーがあると仮定（注：IPオプションが存在する場合は変動あり）
   - `ntohs`を使用してヘッダーフィールドをネットワークバイトオーダー（ビッグエンディアン）からホストバイトオーダーに変換・抽出
   - ヘッダー情報を表示
   - ペイロードデータを抽出して表示

コンパイルと実行方法：
```bash
gcc udp_decoder.c -o udp_decoder
sudo ./udp_decoder  # 生ソケット使用のためsudoが必要
```

重要な注意点：
1. これは基本的な例です - 実際のアプリケーションでは以下が必要になる場合があります：
   - パケットサイズのエラーチェック
   - IPヘッダーオプション（可変長）の処理
   - チェックサム検証
   - より高度なデータ処理

2. テスト方法：
   - netcatを使用してUDPパケットを送信：`echo "test" | nc -u 127.0.0.1 12345`
   - パケット生成ツールを使用

3. このコードはパケットにIPヘッダーが含まれると仮定しています。生のUDPデータを扱う場合は、+20オフセットを削除してください。

4. 製品版では、より多くのエラーハンドリングを追加し、カスタム構造体の代わりに`<netinet/udp.h>`の`struct udphdr`を使用することを検討してください。

特定の部分についてより詳細な説明や、このコードのバリエーションを見たい場合はお知らせください。