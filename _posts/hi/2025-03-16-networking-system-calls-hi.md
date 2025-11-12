---
audio: false
generated: true
lang: hi
layout: post
title: नेटवर्किंग सिस्टम कॉल
translated: true
type: note
---

Linux/Unix जैसे ऑपरेटिंग सिस्टम में, नेटवर्किंग के लिए सबसे निम्न-स्तरीय सिस्टम कॉल, विशेष रूप से TCP कनेक्शन स्थापित करने के लिए, Berkeley Sockets API (जिसे अक्सर सिर्फ "sockets" कहा जाता है) से आती हैं। ये सिस्टम कॉल सीधे कर्नेल के नेटवर्किंग स्टैक के साथ इंटरैक्ट करती हैं। TCP कनेक्शन के लिए सबसे मौलिक कॉल ये हैं:

1. **`socket()`** - एक नया सॉकेट बनाता है।
2. **`bind()`** - सॉकेट को एक एड्रेस असाइन करता है (क्लाइंट के लिए वैकल्पिक)।
3. **`connect()`** - रिमोट सर्वर से कनेक्शन शुरू करता है (क्लाइंट के लिए)।
4. **`listen()`** - सॉकेट को कनेक्शन स्वीकार करने के लिए चिह्नित करता है (सर्वर के लिए)।
5. **`accept()`** - एक आने वाले कनेक्शन को स्वीकार करता है (सर्वर के लिए)।
6. **`send()` / `recv()`** - कनेक्शन पर डेटा भेजता या प्राप्त करता है।
7. **`close()`** - सॉकेट को बंद करता है।

ये वे कच्ची सिस्टम कॉल हैं जिनका उपयोग आप सबसे निचले स्तर पर, `libcurl` या फ्रेमवर्क जैसी किसी भी उच्च-स्तरीय लाइब्रेरी के नीचे करेंगे। यहाँ C में एक सरल उदाहरण दिया गया है जो TCP क्लाइंट और सर्वर दोनों को कनेक्शन स्थापित करते हुए दिखाता है।

---

### TCP सर्वर उदाहरण
यह कोड एक सर्वर सेट अप करता है जो पोर्ट 8080 पर कनेक्शन के लिए प्रतीक्षा करता है, उसे स्वीकार करता है, और एक संदेश भेजता है।

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

    // सॉकेट बनाएं
    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // सर्वर एड्रेस स्ट्रक्चर सेट अप करें
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY; // किसी भी एड्रेस से बाइंड करें
    server_addr.sin_port = htons(8080);       // पोर्ट 8080

    // सॉकेट बाइंड करें
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // कनेक्शन के लिए प्रतीक्षा करें
    if (listen(server_fd, 3) < 0) { // अधिकतम 3 कतारबद्ध कनेक्शन की अनुमति दें
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port 8080...\n");

    // आने वाले कनेक्शन को स्वीकार करें
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }
    printf("Connection accepted\n");

    // क्लाइंट को संदेश भेजें
    send(client_fd, message, strlen(message), 0);

    // सफाई करें
    close(client_fd);
    close(server_fd);
    return 0;
}
```

---

### TCP क्लाइंट उदाहरण
यह कोड `127.0.0.1:8080` पर सर्वर से कनेक्ट होता है और संदेश पढ़ता है।

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

    // सॉकेट बनाएं
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // सर्वर एड्रेस स्ट्रक्चर सेट अप करें
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);              // पोर्ट 8080
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr); // लोकलहोस्ट

    // सर्वर से कनेक्ट करें
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }
    printf("Connected to server\n");

    // सर्वर से संदेश प्राप्त करें
    recv(sock_fd, buffer, sizeof(buffer), 0);
    printf("Server message: %s", buffer);

    // सफाई करें
    close(sock_fd);
    return 0;
}
```

---

### प्रमुख सिस्टम कॉल की व्याख्या
- **`socket(AF_INET, SOCK_STREAM, 0)`**: एक TCP सॉकेट बनाता है (`AF_INET` IPv4 के लिए, `SOCK_STREAM` TCP के लिए)।
- **`bind()`**: सॉकेट को एक लोकल एड्रेस और पोर्ट से जोड़ता है (सर्वर-साइड)।
- **`listen()`**: सॉकेट को कनेक्शन स्वीकार करने के लिए तैयार करता है (सर्वर-साइड)।
- **`accept()`**: तब तक ब्लॉक करता है जब तक कोई क्लाइंट कनेक्ट नहीं हो जाता, फिर कम्युनिकेशन के लिए एक नया सॉकेट रिटर्न करता है।
- **`connect()`**: सर्वर के साथ TCP हैंडशेक शुरू करता है (क्लाइंट-साइड)।
- **`send()` / `recv()`**: स्थापित कनेक्शन पर डेटा ट्रांसफर को संभालते हैं।
- **`close()`**: सॉकेट को समाप्त करता है।

ये यूजर स्पेस में TCP नेटवर्किंग के लिए जितना निम्न-स्तरीय हो सकता है उतना ही है। इसके नीचे, आप कर्नेल इंटर्नल्स (जैसे, TCP/IP स्टैक स्वयं) से निपट रहे होंगे, जो कर्नेल कोड लिखे बिना सीधे सिस्टम कॉल के माध्यम से एक्सेसिबल नहीं है।

कंपाइल और रन करने के लिए:
1. सर्वर कोड को `server.c` और क्लाइंट कोड को `client.c` के रूप में सेव करें।
2. कंपाइल करें: `gcc server.c -o server` और `gcc client.c -o client`।
3. पहले सर्वर रन करें: `./server`।
4. दूसरे टर्मिनल में, क्लाइंट रन करें: `./client`।

यदि आप और अधिक विवरण या गहराई से जानकारी चाहते हैं तो मुझे बताएं!