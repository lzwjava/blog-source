---
audio: false
generated: true
lang: ar
layout: post
title: برنامج سي لفك تشفير حزمة بروتوكول التحكم في الإرسال
translated: true
type: note
---

فك تشفير حزمة TCP في لغة C يتضمن التقاط بيانات الشبكة الخام (عادةً باستخدام مقابس خام أو آلية لالتقاط الحزم) ثم تحليل الرؤوس خطوة بخطوة: رأس الإيثرنت (إذا كان موجودًا)، ورأس IP، وأخيرًا رأس TCP. نظرًا لأن TCP يعمل فوق IP، ستحتاج إلى استخراج رأس IP أولاً لتحديد موقع مقطع TCP داخل الحزمة. للتبسيط، سأفترض أننا نعمل مع IPv4 ومقبس خام يلتقط حزم IP (بدون طبقة إيثرنت).

إليك برنامجًا بلغة C يلتقط حزمة TCP باستخدام مقبس خام، ويفك تشفير رأس IP، ثم يفك تشفير رأس TCP لعرض الحقول الرئيسية مثل منافذ المصدر/الوجهة، ورقم التسلسل، ورقم الإقرار، والإشارات، وحجم النافذة.

---

### برنامج C لفك تشفير حزمة TCP

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>   // For struct iphdr
#include <netinet/tcp.h>  // For struct tcphdr

// طباعة إشارات TCP بصيغة قابلة للقراءة البشرية
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
    char buffer[65535]; // أقصى حجم لحزمة IP
    struct sockaddr_in source_addr, dest_addr;

    // إنشاء مقبس خام لالتقاط حزم TCP
    sock_fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock_fd < 0) {
        perror("فشل إنشاء المقبس (قم بالتشغيل كمسؤول؟)");
        exit(EXIT_FAILURE);
    }

    printf("جاري الاستماع لحزم TCP...\n");

    while (1) {
        // استقبال الحزمة الخام
        ssize_t bytes_received = recvfrom(sock_fd, buffer, sizeof(buffer), 0, NULL, NULL);
        if (bytes_received < 0) {
            perror("فشل الاستقبال");
            continue;
        }

        // رأس IP (struct iphdr) موجود في بداية الحزمة
        struct iphdr *ip = (struct iphdr *)buffer;
        int ip_header_len = ip->ihl * 4; // ihl مقاسًا بكلمات 32-بت، تحويل إلى بايت

        // التحقق مما إذا كانت حزمة IPv4 مع بروتوكول TCP
        if (ip->version == 4 && ip->protocol == IPPROTO_TCP) {
            // رأس TCP يلي رأس IP
            struct tcphdr *tcp = (struct tcphdr *)(buffer + ip_header_len);

            // استخراج عناوين IP المصدر والوجهة
            inet_ntop(AF_INET, &ip->saddr, (char *)&source_addr.sin_addr, sizeof(source_addr));
            inet_ntop(AF_INET, &ip->daddr, (char *)&dest_addr.sin_addr, sizeof(dest_addr));

            // فك التشفير وطباعة تفاصيل حزمة TCP
            printf("\n--- حزمة TCP ---\n");
            printf("IP المصدر: %s\n", inet_ntoa(*(struct in_addr *)&ip->saddr));
            printf("IP الوجهة: %s\n", inet_ntoa(*(struct in_addr *)&ip->daddr));
            printf("منفذ المصدر: %u\n", ntohs(tcp->source));
            printf("منفذ الوجهة: %u\n", ntohs(tcp->dest));
            printf("رقم التسلسل: %u\n", ntohl(tcp->seq));
            printf("رقم الإقرار: %u\n", ntohl(tcp->ack_seq));
            printf("إزاحة البيانات: %d بايت\n", tcp->doff * 4); // طول رأس TCP
            print_tcp_flags(tcp);
            printf("حجم النافذة: %u\n", ntohs(tcp->window));
            printf("المجموع الاختباري: 0x%04x\n", ntohs(tcp->check));
            printf("مؤشر الطوارئ: %u\n", ntohs(tcp->urg_ptr));

            // الحمولة (البيانات بعد رأس TCP)
            int tcp_header_len = tcp->doff * 4;
            int payload_len = bytes_received - ip_header_len - tcp_header_len;
            if (payload_len > 0) {
                printf("طول الحمولة: %d بايت\n", payload_len);
                printf("الحمولة (أول 16 بايت): ");
                unsigned char *payload = (unsigned char *)(buffer + ip_header_len + tcp_header_len);
                for (int i = 0; i < payload_len && i < 16; i++) {
                    printf("%02x ", payload[i]);
                }
                printf("\n");
            } else {
                printf("لا توجد حمولة\n");
            }
        }
    }

    close(sock_fd); // لا يمكن الوصول إليه في هذه الحلقة، لكنها ممارسة جيدة
    return 0;
}
```

---

### آلية العمل

1. **إعداد المقبس**:
   - `socket(AF_INET, SOCK_RAW, IPPROTO_TCP)` ينشئ مقبسًا خامًا يلتقط جميع حزم TCP الموجهة إلى المضيف. هذا يتطلب صلاحيات المسؤول (`sudo`).

2. **التقاط الحزمة**:
   - `recvfrom()` تلتقط حزمة IP الخام، والتي تتضمن رأس IP، ورأس TCP، والحمولة.

3. **تحليل رأس IP**:
   - `struct iphdr` يحدد رأس IPv4 (من `<netinet/ip.h>`).
   - `ihl` (طول رأس IP) يُضرب في 4 للحصول على الإزاحة بالبايت، لأنه مقاس بكلمات 32-بت.
   - التحقق من `version == 4` و `protocol == IPPROTO_TCP` لضمان أنها حزمة TCP IPv4.

4. **تحليل رأس TCP**:
   - `struct tcphdr` (من `<netinet/tcp.h>`) يحدد رأس TCP، الذي يبدأ مباشرة بعد رأس IP.
   - الحقول الرئيسية:
     - `source` و `dest`: منافذ المصدر والوجهة (تم تحويلها من ترتيب بايتات الشبكة إلى ترتيب المضيف باستخدام `ntohs`).
     - `seq` و `ack_seq`: أرقام التسلسل والإقرار (`ntohl` للتحويل 32-بت).
     - `doff`: إزاحة البيانات (طول رأس TCP بالبايت، يُضرب أيضًا في 4).
     - `syn`, `ack`, `fin`, إلخ: إشارات تشير إلى نوع الحزمة.
     - `window`: حجم نافذة المستقبل.
     - `check`: المجموع الاختباري (غير مُتحقق منه هنا للتبسيط).
     - `urg_ptr`: مؤشر الطوارئ (يُستخدم مع إشارة URG).

5. **استخراج الحمولة**:
   - تبدأ الحمولة بعد رأس TCP. يتم حساب طولها كالتالي: `إجمالي البايتات - طول رأس IP - طول رأس TCP`.
   - تُطبع مقتطفات من الحمولة بالنظام الست عشري.

---

### الترجمة والاستخدام

- الترجمة: `gcc tcp_decode.c -o tcp_decode`
- التشغيل (كمسؤول): `sudo ./tcp_decode`
- مثال على الناتج (عند وجود حركة مرور TCP، مثل تصفح الويب):
  ```
  جاري الاستماع لحزم TCP...

  --- حزمة TCP ---
  IP المصدر: 192.168.1.100
  IP الوجهة: 93.184.216.34
  منفذ المصدر: 54321
  منفذ الوجهة: 80
  رقم التسلسل: 123456789
  رقم الإقرار: 987654321
  إزاحة البيانات: 20 بايت
  Flags: SYN
  حجم النافذة: 64240
  المجموع الاختباري: 0x1a2b
  مؤشر الطوارئ: 0
  لا توجد حمولة
  ```

---

### الهياكل الرئيسية

- **رأس IP (`struct iphdr`)**:
  ```c
  struct iphdr {
      unsigned int ihl:4;    // طول الرأس (بكلمات 32-بت)
      unsigned int version:4;// إصدار IP (4 لـ IPv4)
      uint8_t tos;           // نوع الخدمة
      uint16_t tot_len;      // الطول الإجمالي
      uint16_t id;           // المعرف
      uint16_t frag_off;     // إزاحة القطعة
      uint8_t ttl;           // وقت البقاء
      uint8_t protocol;      // البروتوكول (6 لـ TCP)
      uint16_t check;        // المجموع الاختباري
      uint32_t saddr;        // عنوان المصدر
      uint32_t daddr;        // عنوان الوجهة
  };
  ```

- **رأس TCP (`struct tcphdr`)**:
  ```c
  struct tcphdr {
      uint16_t source;       // منفذ المصدر
      uint16_t dest;         // منفذ الوجهة
      uint32_t seq;          // رقم التسلسل
      uint32_t ack_seq;      // رقم الإقرار
      uint16_t doff:4;       // إزاحة البيانات (طول الرأس بكلمات 32-بت)
      uint16_t res1:4;       // محجوز
      uint16_t res2:2;       // محجوز
      uint16_t urg:1;        // إشارة الطوارئ
      uint16_t ack:1;        // إشارة الإقرار
      uint16_t psh:1;        // إشارة الدفع
      uint16_t rst:1;        // إشارة إعادة التعيين
      uint16_t syn:1;        // إشارة المزامنة
      uint16_t fin:1;        // إشارة الانتهاء
      uint16_t window;       // حجم النافذة
      uint16_t check;        // المجموع الاختباري
      uint16_t urg_ptr;      // مؤشر الطوارئ
  };
  ```

---

### ملاحظات

- **صلاحيات المسؤول**: المقابس الخام تتطلب `sudo` لأنها تصل إلى مكدس الشبكة مباشرة.
- **الوضع المختلط**: هذا يلتقط فقط الحزم الموجهة إلى المضيف. لجميع حركة المرور (مثل Wireshark)، ستحتاج إلى `libpcap` أو نهج مختلف (مثل مقابس `PF_PACKET` مع الوضع المختلط).
- **ترتيب البايتات**: يتم تحويل ترتيب بايتات الشبكة (big-endian) إلى ترتيب بايتات المضيف باستخدام `ntohs` (16-بت) و `ntohl` (32-بت).
- **القيود**: هذا لا يتحقق من صحة المجموع الاختباري ولا يتعامل مع الحزم المجزأة.

أعلمني إذا كنت تريد تحسين هذا further (مثل إضافة التحقق من المجموع الاختباري أو تصفية منافذ محددة)!