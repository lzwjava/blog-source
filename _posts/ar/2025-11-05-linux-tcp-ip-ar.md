---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: برمجة الـ TCP/IP على لينكس باستخدام لغة C
translated: true
type: note
---

### بروتوكولات TCP/IP في لينكس: نظرة عامة واستخدامها في لغة C

في لينكس، يُعتبر بروتوكولا TCP (بروتوكول التحكم بالإرسال) و IP (بروتوكول الإنترنت) من بروتوكولات الشبكة الأساسية المنفذة **في النواة** كجزء من مجموعة بروتوكولات TCP/IP في لينكس. تتعامل هذه المجموعة مع التفاصيل منخفضة المستوى مثل توجيه الحزم، والتحكم في الازدحام، وإدارة الاتصالات. تتفاعل التطبيقات في فضاء المستخدم (مثل برامجك المكتوبة بلغة C) مع هذه المجموعة عبر **واجهة برمجة تطبيقات مقابس بيركلي** (المعروفة أيضًا باسم مقابس POSIX)، والتي توفر طريقة موحدة لإنشاء اتصالات الشبكة.

لا تحتاج إلى تنفيذ TCP/IP بنفسك — النواة تقوم بذلك. بدلاً من ذلك، تستخدم واجهة برمجة تطبيقات المقابس "للحديث" إلى النواة. هذه الواجهة **مضمنة في مكتبة C القياسية (glibc)** على لينكس، لذلك لا توجد "مكتبة TCP/IP" منفصلة لتثبيتها أو ربطها. كل شيء مُقدم من خلال `libc` (مكتبة GNU C).

#### المكتبات والملفات الرئيسية
- **المكتبة الرئيسية**: `libc` (glibc). جميع دوال المقبس مدرجة هنا. اربط برنامجك بها ضمنيًا (عادة ما يكون ذلك تلقائيًا مع `gcc`).
  - الموقع: عادة `/lib/x86_64-linux-gnu/libc.so.6` (أو ما شابه، اعتمادًا على بنية النظام والتوزيعة). يمكنك العثور عليه باستخدام `ldd /bin/ls` أو `locate libc.so`.
- **الملفات الرئيسية** (للتوصيفات): هذه جزء من رؤوس التطوير في لينكس.
  - `<sys/socket.h>`: دوال المقبس الأساسية (مثل `socket()`, `bind()`, `connect()`).
  - `<netinet/in.h>`: هياكل عناوين الإنترنت (مثل `struct sockaddr_in` لـ IPv4).
  - `<arpa/inet.h>`: دوال تحويل العناوين (مثل `inet_addr()`).
  - `<sys/types.h>`: الأنواع الأساسية (غالبًا ما يتم تضمينها بشكل غير مباشر).
  - الموقع: عادة `/usr/include/` (مثال: `/usr/include/sys/socket.h`). قم بتثبيت رؤوس التطوير إذا كانت مفقودة (مثال: `sudo apt install libc6-dev` على الأنظمة القائمة على دبيان).

لا حاجة لإشارات إضافية مثل `-lsocket` على لينكس (على عكس بعض أنظمة يونكس القديمة). فقط قم بالتجميع باستخدام `gcc your_program.c -o your_program`.

#### مثال أساسي: عميل TCP بسيط بلغة C
إليك عميل TCP بسيط يتصل بخادم (مثال: المنفذ 80 على example.com). يوضح هذا استخدام واجهة برمجة تطبيقات المقابس.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>  // For close()

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);  // إنشاء مقبس TCP (AF_INET لـ IPv4، SOCK_STREAM لـ TCP)
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);  // ترتيب البايتات من المضيف إلى الشبكة
    inet_pton(AF_INET, "93.184.216.34", &server_addr.sin_addr);  // عنوان IP لـ example.com

    if (connect(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        close(sockfd);
        return 1;
    }

    const char* msg = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
    send(sockfd, msg, strlen(msg), 0);

    char buffer[1024];
    int bytes = recv(sockfd, buffer, sizeof(buffer) - 1, 0);
    buffer[bytes] = '\0';
    printf("Response: %s\n", buffer);

    close(sockfd);
    return 0;
}
```

- التجميع: `gcc -o tcp_client tcp_client.c`
- التشغيل: `./tcp_client`

بالنسبة للخادم، ستستخدم `bind()`, `listen()`, و `accept()` بدلاً من `connect()`.

#### أين تتعلم المزيد
- **صفحات الدليل**: نفذ `man socket` أو `man 7 ip` على نظام لينكس الخاص بك للحصول على وثائق مفصلة.
- **جانب النواة**: إذا كنت تقصد التنفيذ على مستوى النواة، فتحقق من المصدر في `/usr/src/linux/net/ipv4/` (TCP) أو `/usr/src/linux/net/ipv6/` (لـ IPv6). قم بتثبيت رؤوس النواة باستخدام `sudo apt install linux-headers-$(uname -r)`.
- المصادر:
  - [برمجة المقابس في C (GeeksforGeeks)](https://www.geeksforgeeks.org/c/socket-programming-cc/)
  - [برمجة مقابس لينكس باستخدام TCP/IP (IBM Developer)](https://developer.ibm.com/tutorials/l-sock/)

إذا لم يكن هذا ما تقصده (مثل وحدات النواة أو شيء آخر)، فقدم المزيد من التفاصيل!