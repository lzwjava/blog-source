---
audio: false
generated: true
lang: hi
layout: post
title: टीसीपी पैकेट डिकोड करने के लिए सी प्रोग्राम
translated: true
type: note
---

C में TCP पैकेट को डिकोड करने में रॉ नेटवर्क डेटा को कैप्चर करना (आमतौर पर रॉ सॉकेट या पैकेट कैप्चर मैकेनिज्म का उपयोग करके) और फिर हेडर को चरणबद्ध तरीके से पार्स करना शामिल है: ईथरनेट हेडर (यदि मौजूद हो), IP हेडर, और अंत में TCP हेडर। चूंकि TCP, IP पर चलता है, इसलिए पैकेट के भीतर TCP सेगमेंट को लोकेट करने के लिए आपको पहले IP हेडर निकालने की आवश्यकता होगी। सरलता के लिए, मैं मानूंगा कि हम IPv4 और एक रॉ सॉकेट के साथ काम कर रहे हैं जो IP पैकेट कैप्चर कर रहा है (कोई ईथरनेट लेयर नहीं)।

यहां एक C प्रोग्राम है जो एक रॉ सॉकेट का उपयोग करके एक TCP पैकेट को कैप्चर करता है, IP हेडर को डिकोड करता है, और फिर TCP हेडर को डिकोड करके स्रोत/गंतव्य पोर्ट, अनुक्रम संख्या, पावती संख्या, फ्लैग्स और विंडो आकार जैसे प्रमुख फ़ील्ड्स को प्रदर्शित करता है।

---

### TCP पैकेट डिकोड करने के लिए C प्रोग्राम

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // struct iphdr के लिए
#include <netinet/tcp.h>  // struct tcphdr के लिए

// TCP फ्लैग्स को मानव-पठनीय रूप में प्रिंट करें
void print_tcp_flags(struct tcphdr *tcp) {
    printf("फ्लैग्स: ");
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
    char buffer[65535]; // अधिकतम IP पैकेट आकार
    struct sockaddr_in source_addr, dest_addr;

    // TCP पैकेट कैप्चर करने के लिए रॉ सॉकेट बनाएं
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("सॉकेट निर्माण विफल (रूट के रूप में चलाएं?)");
        exit(EXIT_FAILURE);
    }

    printf("TCP पैकेट सुन रहा हूं...\n");

    while (1) {
        // रॉ पैकेट प्राप्त करें
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("प्राप्त करने में विफल");
            continue;
        }

        // IP हेडर (struct iphdr) पैकेट की शुरुआत में होता है
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihl 32-बिट शब्दों में है, बाइट्स में बदलें

        // जांचें कि क्या यह IPv4 पैकेट है जिसका प्रोटोकॉल TCP है
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // TCP हेडर IP हेडर के बाद आता है
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // स्रोत और गंतव्य IP पते निकालें
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // TCP पैकेट विवरण डिकोड करें और प्रिंट करें
            printf("\n--- TCP पैकेट ---\n");
            printf("स्रोत IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("गंतव्य IP: %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("स्रोत पोर्ट: %u\n", ntohs(tcp->source));
            printf("गंतव्य पोर्ट: %u\n", ntohs(tcp->dest));
            printf("अनुक्रम संख्या: %u\n", ntohl(tcp->seq));
            printf("पावती संख्या: %u\n", ntohl(tcp->ack_seq));
            printf("डेटा ऑफसेट: %d बाइट्स\n", tcp->doff * 4); // TCP हेडर लंबाई
            print_tcp_flags(tcp);
            printf("विंडो आकार: %u\n", ntohs(tcp->window));
            printf("चेकसम: 0x%04x\n", ntohs(tcp->check));
            printf("अर्जेंट पॉइंटर: %u\n", ntohs(tcp->urg_ptr));

            // पेलोड (TCP हेडर के बाद का डेटा)
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("पेलोड लंबाई: %d बाइट्स\n", payload_len);
                printf("पेलोड (पहले 16 बाइट्स): ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("कोई पेलोड नहीं\n");
            }
        }
    }

    close(sock_fd); // इस लूप में पहुंच से बाहर, लेकिन अच्छा अभ्यास है
    return 0;
}
```

---

### यह कैसे काम करता है

1.  **सॉकेट सेटअप**:
    *   `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` एक रॉ सॉकेट बनाता है जो होस्ट के लिए निर्धारित सभी TCP पैकेट्स को कैप्चर करता है। इसके लिए रूट विशेषाधिकार (`sudo`) की आवश्यकता होती है।

2.  **पैकेट कैप्चर**:
    *   `recvfrom()` रॉ IP पैकेट को पकड़ता है, जिसमें IP हेडर, TCP हेडर और पेलोड शामिल होता है।

3.  **IP हेडर पार्सिंग**:
    *   `struct iphdr` IPv4 हेडर को परिभाषित करता है (`<netinet/ip.h>` से)।
    *   `ihl` (IP हेडर लंबाई) को बाइट ऑफसेट प्राप्त करने के लिए 4 से गुणा किया जाता है, क्योंकि इसे 32-बिट शब्दों में मापा जाता है।
    *   यह सुनिश्चित करने के लिए जांचें कि `version == 4` और `protocol == IPPROTO_TCP` है कि यह एक IPv4 TCP पैकेट है।

4.  **TCP हेडर पार्सिंग**:
    *   `struct tcphdr` (`<netinet/tcp.h>` से) TCP हेडर को परिभाषित करता है, जो IP हेडर के ठीक बाद शुरू होता है।
    *   प्रमुख फ़ील्ड्स:
        *   `source` और `dest`: स्रोत और गंतव्य पोर्ट (`ntohs` के साथ नेटवर्क से होस्ट बाइट ऑर्डर में परिवर्तित)।
        *   `seq` और `ack_seq`: अनुक्रम और पावती संख्याएं (32-बिट रूपांतरण के लिए `ntohl`)।
        *   `doff`: डेटा ऑफसेट (बाइट्स में TCP हेडर लंबाई, इसे भी 4 से गुणा किया जाता है)।
        *   `syn`, `ack`, `fin`, आदि: पैकेट प्रकार इंगित करने वाले फ्लैग।
        *   `window`: रिसीवर का विंडो आकार।
        *   `check`: चेकसम (सरलता के लिए यहां मान्य नहीं किया गया)।
        *   `urg_ptr`: अर्जेंट पॉइंटर (URG फ्लैग के साथ प्रयुक्त)।

5.  **पेलोड एक्सट्रैक्शन**:
    *   पेलोड TCP हेडर के बाद शुरू होता है। इसकी लंबाई इस प्रकार गणना की जाती है: `कुल बाइट्स - IP हेडर लंबाई - TCP हेडर लंबाई`।
    *   पेलोड का एक स्निपेट हेक्स में प्रिंट किया जाता है।

---

### कंपाइलेशन और उपयोग
*   कंपाइल करें: `gcc tcp_decode.c -o tcp_decode`
*   चलाएं (रूट के रूप में): `sudo ./tcp_decode`
*   उदाहरण आउटपुट (जब TCP ट्रैफिक मौजूद हो, उदा. वेब ब्राउज़ करना):
    ```
    TCP पैकेट सुन रहा हूं...

    --- TCP पैकेट ---
    स्रोत IP: 192.168.1.100
    गंतव्य IP: 93.184.216.34
    स्रोत पोर्ट: 54321
    गंतव्य पोर्ट: 80
    अनुक्रम संख्या: 123456789
    पावती संख्या: 987654321
    डेटा ऑफसेट: 20 बाइट्स
    फ्लैग्स: SYN
    विंडो आकार: 64240
    चेकसम: 0x1a2b
    अर्जेंट पॉइंटर: 0
    कोई पेलोड नहीं
    ```

---

### प्रमुख संरचनाएं
*   **IP हेडर (`struct iphdr`)**:
    ```c
    struct iphdr {
        unsigned int ihl:4;    // हेडर लंबाई (32-बिट शब्दों में)
        unsigned int version:4;// IP संस्करण (IPv4 के लिए 4)
        uint8_t tos;           // सेवा का प्रकार
        uint16_t tot_len;      // कुल लंबाई
        uint16_t id;           // पहचान
        uint16_t frag_off;     // फ्रैगमेंट ऑफसेट
        uint8_t ttl;           // टाइम टू लाइव
        uint8_t protocol;      // प्रोटोकॉल (TCP के लिए 6)
        uint16_t check;        // चेकसम
        uint32_t saddr;        // स्रोत पता
        uint32_t daddr;        // गंतव्य पता
    };
    ```

*   **TCP हेडर (`struct tcphdr`)**:
    ```c
    struct tcphdr {
        uint16_t source;       // स्रोत पोर्ट
        uint16_t dest;         // गंतव्य पोर्ट
        uint32_t seq;          // अनुक्रम संख्या
        uint32_t ack_seq;      // पावती संख्या
        uint16_t doff:4;       // डेटा ऑफसेट (हेडर लंबाई 32-बिट शब्दों में)
        uint16_t res1:4;       // आरक्षित
        uint16_t res2:2;       // आरक्षित
        uint16_t urg:1;        // अर्जेंट फ्लैग
        uint16_t ack:1;        // पावती फ्लैग
        uint16_t psh:1;        // पुश फ्लैग
        uint16_t rst:1;        // रीसेट फ्लैग
        uint16_t syn:1;        // सिंक्रोनाइज़ फ्लैग
        uint16_t fin:1;        // फिनिश फ्लैग
        uint16_t window;       // विंडो आकार
        uint16_t check;        // चेकसम
        uint16_t urg_ptr;      // अर्जेंट पॉइंटर
    };
    ```

---

### नोट्स
*   **रूट विशेषाधिकार**: रॉ सॉकेट के लिए `sudo` की आवश्यकता होती है क्योंकि वे सीधे नेटवर्क स्टैक तक पहुंचते हैं।
*   **प्रोमिस्क्यूअस मोड**: यह केवल होस्ट के लिए निर्धारित पैकेट्स को कैप्चर करता है। सभी ट्रैफिक (जैसे Wireshark) के लिए आपको `libpcap` या एक अलग दृष्टिकोण (जैसे, प्रोमिस्क्यूअस मोड के साथ `PF_PACKET` सॉकेट) की आवश्यकता होगी।
*   **बाइट ऑर्डर**: नेटवर्क बाइट ऑर्डर (बिग-एंडियन) को `ntohs` (16-बिट) और `ntohl` (32-बिट) का उपयोग करके होस्ट बाइट ऑर्डर में परिवर्तित किया जाता है।
*   **सीमाएं**: यह चेकसम को वैलिडेट नहीं करता है या खंडित पैकेट्स को हैंडल नहीं करता है।

मुझे बताएं कि क्या आप इसे और परिष्कृत करना चाहते हैं (जैसे, चेकसम वैलिडेशन जोड़ें या विशिष्ट पोर्ट्स को फ़िल्टर करें)!