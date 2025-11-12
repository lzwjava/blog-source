---
audio: false
generated: true
lang: ja
layout: post
title: TCPパケットをデコードするCプログラム
translated: true
type: note
---

C言語でTCPパケットをデコードするには、生のネットワークデータ（通常はrawソケットまたはパケットキャプチャメカニズムを使用）をキャプチャし、ヘッダーを段階的に解析します：イーサネットヘッダー（存在する場合）、IPヘッダー、そして最後にTCPヘッダーです。TCPはIP上で動作するため、パケット内のTCPセグメントを特定するには、まずIPヘッダーを抽出する必要があります。簡単のため、IPv4を扱い、イーサネット層なしのIPパケットをキャプチャするrawソケットを使用することを前提とします。

以下は、rawソケットを使用してTCPパケットをキャプチャし、IPヘッダーをデコードした後、TCPヘッダーをデコードして送信元/送信先ポート、シーケンス番号、確認応答番号、フラグ、ウィンドウサイズなどの主要なフィールドを表示するCプログラムです。

---

### TCPパケットをデコードするCプログラム

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // struct iphdr用
#include <netinet/tcp.h>  // struct tcphdr用

// TCPフラグを人間が読める形式で表示
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
    char buffer[65535]; // IPパケットの最大サイズ
    struct sockaddr_in source_addr, dest_addr;

    // TCPパケットをキャプチャするrawソケットを作成
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("ソケットの作成に失敗しました (root権限で実行?)");
        exit(EXIT_FAILURE);
    }

    printf("TCPパケットを待機中...\n");

    while (1) {
        // 生パケットを受信
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("受信に失敗しました");
            continue;
        }

        // IPヘッダー (struct iphdr) はパケットの先頭にある
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihlは32ビットワード単位なのでバイトに変換

        // IPv4パケットでTCPプロトコルか確認
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // TCPヘッダーはIPヘッダーの後に続く
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // 送信元と送信先のIPアドレスを抽出
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // TCPパケットの詳細をデコードして表示
            printf("\n--- TCP Packet ---\n");
            printf("Source IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("Dest IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("Source Port: %u\n", ntohs(tcp->source));
            printf("Dest Port: %u\n", ntohs(tcp->dest));
            printf("Sequence Number: %u\n", ntohl(tcp->seq));
            printf("Acknowledgment Number: %u\n", ntohl(tcp->ack_seq));
            printf("Data Offset: %d bytes\n", tcp->doff * 4); // TCPヘッダー長
            print_tcp_flags(tcp);
            printf("Window Size: %u\n", ntohs(tcp->window));
            printf("Checksum: 0x%04x\n", ntohs(tcp->check));
            printf("Urgent Pointer: %u\n", ntohs(tcp->urg_ptr));

            // ペイロード (TCPヘッダーの後のデータ)
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("Payload Length: %d bytes\n", payload_len);
                printf("Payload (先頭16バイト): ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("ペイロードなし\n");
            }
        }
    }

    close(sock_fd); // このループでは到達不能だが、良い習慣として
    return 0;
}
```

---

### 動作の説明

1. **ソケット設定**:
   - `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` は、ホスト宛てのすべてのTCPパケットをキャプチャするrawソケットを作成します。これにはroot権限（`sudo`）が必要です。

2. **パケットキャプチャ**:
   - `recvfrom()` は、IPヘッダー、TCPヘッダー、ペイロードを含む生のIPパケットを取得します。

3. **IPヘッダーの解析**:
   - `struct iphdr` はIPv4ヘッダーを定義します（`<netinet/ip.h>` から）。
   - `ihl`（IPヘッダー長）は32ビットワード単位で測定されるため、バイトオフセットを取得するために4を乗算します。
   - `version == 4` と `protocol == IPPROTO_TCP` をチェックして、IPv4のTCPパケットであることを確認します。

4. **TCPヘッダーの解析**:
   - `struct tcphdr`（`<netinet/tcp.h>` から）は、IPヘッダーの直後に始まるTCPヘッダーを定義します。
   - 主要フィールド:
     - `source` と `dest`: 送信元ポートと送信先ポート（`ntohs` でネットワークバイトオーダーからホストバイトオーダーに変換）。
     - `seq` と `ack_seq`: シーケンス番号と確認応答番号（32ビット変換には `ntohl`）。
     - `doff`: データオフセット（バイト単位のTCPヘッダー長、これも4を乗算）。
     - `syn`, `ack`, `fin` など: パケットタイプを示すフラグ。
     - `window`: 受信者のウィンドウサイズ。
     - `check`: チェックサム（簡単のためここでは検証しない）。
     - `urg_ptr`: 緊急ポインタ（URGフラグと共に使用）。

5. **ペイロードの抽出**:
   - ペイロードはTCPヘッダーの後に始まります。その長さは `総バイト数 - IPヘッダー長 - TCPヘッダー長` として計算されます。
   - ペイロードの一部が16進数で表示されます。

---

### コンパイルと使用方法
- コンパイル: `gcc tcp_decode.c -o tcp_decode`
- 実行（root権限）: `sudo ./tcp_decode`
- 出力例（TCPトラフィックがある場合、例: ウェブ閲覧時）:
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

### 主要な構造体
- **IPヘッダー (`struct iphdr`)**:
  ```c
  struct iphdr {
      unsigned int ihl:4;    // ヘッダー長 (32ビットワード単位)
      unsigned int version:4;// IPバージョン (IPv4の場合は4)
      uint8_t tos;           // サービスタイプ
      uint16_t tot_len;      // 全長
      uint16_t id;           // 識別子
      uint16_t frag_off;     // フラグメントオフセット
      uint8_t ttl;           // Time to Live
      uint8_t protocol;      // プロトコル (TCPの場合は6)
      uint16_t check;        // チェックサム
      uint32_t saddr;        // 送信元アドレス
      uint32_t daddr;        // 送信先アドレス
  };
  ```

- **TCPヘッダー (`struct tcphdr`)**:
  ```c
  struct tcphdr {
      uint16_t source;       // 送信元ポート
      uint16_t dest;         // 送信先ポート
      uint32_t seq;          // シーケンス番号
      uint32_t ack_seq;      // 確認応答番号
      uint16_t doff:4;       // データオフセット (32ビットワード単位のヘッダー長)
      uint16_t res1:4;       // 予約済み
      uint16_t res2:2;       // 予約済み
      uint16_t urg:1;        // 緊急フラグ
      uint16_t ack:1;        // 確認応答フラグ
      uint16_t psh:1;        // プッシュフラグ
      uint16_t rst:1;        // リセットフラグ
      uint16_t syn:1;        // 同期フラグ
      uint16_t fin:1;        // 終了フラグ
      uint16_t window;       // ウィンドウサイズ
      uint16_t check;        // チェックサム
      uint16_t urg_ptr;      // 緊急ポインタ
  };
  ```

---

### 注意点
- **Root権限**: rawソケットはネットワークスタックに直接アクセスするため、`sudo` が必要です。
- **プロミスキャスモード**: これはホスト宛てのパケットのみをキャプチャします。すべてのトラフィック（Wiresharkのように）をキャプチャするには、`libpcap` または別のアプローチ（例: プロミスキャスモードでの `PF_PACKET` ソケット）が必要です。
- **バイトオーダー**: ネットワークバイトオーダー（ビッグエンディアン）は、`ntohs`（16ビット）および `ntohl`（32ビット）を使用してホストバイトオーダーに変換されます。
- **制限事項**: このプログラムはチェックサムを検証せず、フラグメント化されたパケットを処理しません。

さらに改良したい場合（例: チェックサム検証の追加や特定のポートのフィルタリング）は、お知らせください！