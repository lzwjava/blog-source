---
audio: false
generated: true
lang: ar
layout: post
title: برنامج سي لفك تشفير حزمة UDP
translated: true
type: note
---

إليك مثالًا لكيفية فك تشفير حزمة UDP في لغة C. يوضح هذا الكود استقبال حزمة UDP واستخراج مكوناتها الرئيسية:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

// هيكل رأس UDP
struct udp_header {
    uint16_t source_port;      // منفذ المصدر
    uint16_t dest_port;       // منفذ الوجهة
    uint16_t length;          // طول حزمة UDP (الرأس + البيانات)
    uint16_t checksum;        // المجموع الاختباري
};

void decode_udp_packet(unsigned char* buffer, int size) {
    // بافتراض أن رأس IP هو 20 بايت (بدون خيارات)
    struct udp_header* udp = (struct udp_header*)(buffer + 20);
    
    printf("\nUDP Header\n");
    printf("Source Port: %u\n", ntohs(udp->source_port));
    printf("Destination Port: %u\n", ntohs(udp->dest_port));
    printf("Length: %u\n", ntohs(udp->length));
    printf("Checksum: 0x%04x\n", ntohs(udp->checksum));
    
    // حساب طول البيانات والمؤشر
    int udp_header_size = 8;  // رأس UDP هو 8 بايت
    int data_length = ntohs(udp->length) - udp_header_size;
    unsigned char* data = buffer + 20 + udp_header_size;
    
    printf("Data: ");
    for(int i = 0; i < data_length && i < 20; i++) {  // طباعة أول 20 بايت كحد أقصى
        printf("%02x ", data[i]);
    }
    printf("\n");
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    unsigned char buffer[65535];  // الحد الأقصى لحجم حزمة UDP
    
    // إنشاء مأخذ UDP
    sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd < 0) {
        perror("Socket creation failed");
        return 1;
    }
    
    // تهيئة عنوان الخادم
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345);  // منفذ مثال
    
    // ربط المأخذ
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

يقوم هذا الكود بما يلي:

1. يحدد هيكل `udp_header` الذي يتطابق مع تنسيق رأس حزمة UDP:
   - منفذ المصدر (16 بت)
   - منفذ الوجهة (16 بت)
   - الطول (16 بت)
   - المجموع الاختباري (16 بت)

2. ينشئ مأخذ UDP ويربطه بالمنفذ 12345 (يمكنك تغيير رقم المنفذ هذا).

3. دالة `decode_udp_packet`:
   - تأخذ مخزن مؤقت للحزمة الخام كمدخل
   - تفترض أن رأس IP بطول 20 بايت يسبق رأس UDP (ملاحظة: قد يختلف هذا إذا كانت هناك خيارات IP موجودة)
   - تستخرج وتحول حقول الرأس من ترتيب البايتات للشبكة (big-endian) إلى ترتيب البايتات للمضيف باستخدام `ntohs`
   - تطبع معلومات الرأس
   - تستخرج وتعرض بيانات الحمولة

للترجمة والتشغيل:
```bash
gcc udp_decoder.c -o udp_decoder
sudo ./udp_decoder  # يحتاج إلى sudo بسبب استخدام raw socket
```

ملاحظات مهمة:
1. هذا مثال أساسي - قد تحتاج التطبيقات الواقعية إلى:
   - فحص الأخطاء لحجم الحزمة
   - معالجة خيارات رأس IP (طول متغير)
   - التحقق من المجموع الاختباري
   - معالجة بيانات أكثر تطورًا

2. لاختباره، يمكنك:
   - إرسال حزم UDP باستخدام netcat: `echo "test" | nc -u 127.0.0.1 12345`
   - استخدام أداة توليد الحزم

3. يفترض الكود أن الحزمة تتضمن رأس IP. إذا كنت تعمل مع بيانات UDP خام، فقم بإزالة الإزاحة +20.

4. للاستخدام في الإنتاج، أضف المزيد من معالجة الأخطاء وربما استخدم `struct udphdr` من `<netinet/udp.h>` بدلاً من الهيكل المخصص.