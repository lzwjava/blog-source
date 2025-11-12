---
audio: false
generated: true
lang: ar
layout: post
title: نداءات نظام الشبكات
translated: true
type: note
---

في أنظمة التشغيل مثل Linux/Unix، تأتي استدعاءات النظام منخفضة المستوى للشبكات، خاصة لإنشاء اتصال TCP، من واجهة برمجة تطبيقات Berkeley Sockets (غالبًا ما تسمى ببساطة "sockets"). تتفاعل استدعاءات النظام هذه مباشرة مع نواة مكدس الشبكات. وأكثرها أساسية لاتصالات TCP هي:

1.  **`socket()`** - ينشئ مقبسًا جديدًا.
2.  **`bind()`** - يُعين عنوانًا للمقبس (اختياري للعملاء).
3.  **`connect()`** - يبدأ اتصالاً بخادم بعيد (للعملاء).
4.  **`listen()`** - يعلّم المقبس كقابل لقبول الاتصالات (للخوادم).
5.  **`accept()`** - يقبل اتصالاً واردًا (للخوادم).
6.  **`send() / recv()`** - يرسل أو يستقبل بيانات عبر الاتصال.
7.  **`close()`** - يُغلق المقبس.

هذه هي استدعاءات النظام الخام التي ستستخدمها في أدنى مستوى، تحت أي مكتبات عالية المستوى مثل `libcurl` أو الأطر. إليك مثالًا بسيطًا بلغة C يوضح كل من عميل TCP وخادم TCP ينشئان اتصالاً.

---

### مثال خادم TCP
ينشئ هذا الكود خادمًا يستمع لاتصال على المنفذ 8080، يقبله، ثم يرسل رسالة.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    char *message = "Hello from server!\n";

    // Create socket
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Set up server address structure
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // Bind to any address
    server_addr.sin_port = htons(8080);       // Port 8080

    // Bind socket
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen for connections
    if (listen(server_fd, 3) < 0) { // Allow up to 3 queued connections
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port 8080...\n");

    // Accept incoming connection
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }
    printf("Connection accepted\n");

    // Send message to client
    send(client_fd, message, strlen(message), 0);

    // Clean up
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### مثال عميل TCP
يتصل هذا الكود بالخادم على العنوان `127.0.0.1:8080` ويقرأ الرسالة.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock_fd;
    struct sockaddr_in server_addr;
    char buffer[1024] = {0};

    // Create socket
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Set up server address structure
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);              // Port 8080
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr); // Localhost

    // Connect to server
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Connected to server\n");

    // Receive message from server
    recv(sock_fd, buffer, sizeof(buffer), 0);
    printf("Server message: %s", buffer);

    // Clean up
    close(sock_fd);
    return 0;
}
```

---

### شرح استدعاءات النظام الرئيسية
- **`socket(AF_INET, SOCK_STREAM, 0)`**: ينشئ مقبس TCP (`AF_INET` لـ IPv4، `SOCK_STREAM` لـ TCP).
- **`bind()`**: يربط المقبس بعنوان وميناء محلي (جهة الخادم).
- **`listen()`**: يُجهز المقبس لقبول الاتصالات (جهة الخادم).
- **`accept()`**: يحجب العملية حتى يتصل عميل، ثم يُرجع مقبسًا جديدًا للاتصال.
- **`connect()`**: يبدأ مصافحة TCP مع الخادم (جهة العميل).
- **`send() / recv()`**: يتعامل مع نقل البيانات عبر الاتصال المُنشأ.
- **`close()`**: يُنهي المقبس.

هذه هي أدنى مستوى يمكن الوصول إليه للشبكات باستخدام TCP في مساحة المستخدم. دون هذا المستوى، ستتعامل مع البنى الداخلية للنواة (على سبيل المثال، مكدس TCP/IP نفسه)، وهو غير قابل للوصول المباشر عبر استدعاءات النظام دون كتابة كود للنواة.

للترجمة والتشغيل:
1.  احفظ كود الخادم كـ `server.c` وكود العميل كـ `client.c`.
2.  اترجم: `gcc server.c -o server` و `gcc client.c -o client`.
3.  شغل الخادم أولاً: `./server`.
4.  في طرفية أخرى، شغل العميل: `./client`.

أعلمني إذا كنت تريد المزيد من التفاصيل أو شرحًا أعمق!