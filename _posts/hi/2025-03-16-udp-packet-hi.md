---
audio: false
generated: true
lang: hi
layout: post
title: यूडीपी पैकेट डिकोड करने का सी प्रोग्राम
translated: true
type: note
---

यहाँ C में UDP पैकेट को डिकोड करने का एक उदाहरण दिया गया है। यह कोड एक UDP पैकेट प्राप्त करने और उसके मुख्य घटकों को निकालने का प्रदर्शन करता है:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

// UDP हेडर संरचना
struct udp_header {
    uint16_t source_port;      // स्रोत पोर्ट
    uint16_t dest_port;       // गंतव्य पोर्ट
    uint16_t length;          // UDP पैकेट की लंबाई (हेडर + डेटा)
    uint16_t checksum;        // चेकसम
};

void decode_udp_packet(unsigned char* buffer, int size) {
    // यह मानते हुए कि IP हेडर 20 बाइट्स का है (बिना विकल्पों के)
    struct udp_header* udp = (struct udp_header*)(buffer + 20);
    
    printf("\nUDP Header\n");
    printf("Source Port: %u\n", ntohs(udp->source_port));
    printf("Destination Port: %u\n", ntohs(udp->dest_port));
    printf("Length: %u\n", ntohs(udp->length));
    printf("Checksum: 0x%04x\n", ntohs(udp->checksum));
    
    // डेटा लंबाई और पॉइंटर की गणना करें
    int udp_header_size = 8;  // UDP हेडर 8 बाइट्स का होता है
    int data_length = ntohs(udp->length) - udp_header_size;
    unsigned char* data = buffer + 20 + udp_header_size;
    
    printf("Data: ");
    for(int i = 0; i < data_length && i < 20; i++) {  // अधिकतम पहले 20 बाइट्स प्रिंट करें
        printf("%02x ", data[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    unsigned char buffer[65535];  // अधिकतम UDP पैकेट आकार
    
    // UDP सॉकेट बनाएं
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return 1;
    }
    
    // सर्वर एड्रेस को इनिशियलाइज़ करें
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345);  // उदाहरण पोर्ट
    
    // सॉकेट को बाइंड करें
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(sockfd);
        return 1;
    }
    
    printf("Listening for UDP packets on port 12345...\n");
    
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

यह कोड निम्नलिखित कार्य करता है:

1. एक `udp_header` संरचना को परिभाषित करता है जो UDP पैकेट हेडर फॉर्मेट से मेल खाती है:
   - स्रोत पोर्ट (16 बिट्स)
   - गंतव्य पोर्ट (16 बिट्स)
   - लंबाई (16 बिट्स)
   - चेकसम (16 बिट्स)

2. एक UDP सॉकेट बनाता है और इसे पोर्ट 12345 पर बाइंड करता है (आप इस पोर्ट नंबर को बदल सकते हैं)।

3. `decode_udp_packet` फ़ंक्शन:
   - इनपुट के रूप में एक कच्चा पैकेट बफ़र लेता है
   - यह मानता है कि UDP हेडर से पहले 20-बाइट का IP हेडर होता है (नोट: यह भिन्न हो सकता है यदि IP विकल्प मौजूद हों)
   - हेडर फ़ील्ड्स को नेटवर्क बाइट ऑर्डर (बिग-एंडियन) से होस्ट बाइट ऑर्डर में `ntohs` का उपयोग करके परिवर्तित और निकालता है
   - हेडर जानकारी को प्रिंट करता है
   - पेलोड डेटा को निकालता और प्रदर्शित करता है

कंपाइल और रन करने के लिए:
```bash
gcc udp_decoder.c -o udp_decoder
sudo ./udp_decoder  # रॉ सॉकेट उपयोग के कारण sudo की आवश्यकता है
```

महत्वपूर्ण नोट्स:
1. यह एक बुनियादी उदाहरण है - वास्तव-विश्व के एप्लिकेशन को इनकी आवश्यकता हो सकती है:
   - पैकेट आकार के लिए त्रुटि जांच
   - IP हेडर विकल्पों (परिवर्तनशील लंबाई) का हैंडलिंग
   - चेकसम सत्यापन
   - अधिक परिष्कृत डेटा प्रोसेसिंग

2. इसका परीक्षण करने के लिए, आप यह कर सकते हैं:
   - netcat का उपयोग करके UDP पैकेट भेजें: `echo "test" | nc -u 127.0.0.1 12345`
   - एक पैकेट जनरेटर टूल का उपयोग करें

3. कोड यह मानता है कि पैकेट में एक IP हेडर शामिल है। यदि आप रॉ UDP डेटा के साथ काम कर रहे हैं, तो +20 ऑफ़सेट को हटा दें।

4. प्रोडक्शन उपयोग के लिए, अधिक त्रुटि हैंडलिंग जोड़ें और संभवतः कस्टम स्ट्रक्चर के बजाय `<netinet/udp.h>` से `struct udphdr` का उपयोग करें।