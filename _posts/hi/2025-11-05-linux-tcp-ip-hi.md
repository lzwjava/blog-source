---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: लिनक्स टीसीपी/आईपी प्रोग्रामिंग सी में
translated: true
type: note
---

### लिनक्स में TCP/IP प्रोटोकॉल: अवलोकन और C में उनका उपयोग

लिनक्स में, TCP (ट्रांसमिशन कंट्रोल प्रोटोकॉल) और IP (इंटरनेट प्रोटोकॉल) मुख्य नेटवर्किंग प्रोटोकॉल हैं जिन्हें **कर्नेल में** लिनक्स TCP/IP स्टैक के हिस्से के रूप में लागू किया गया है। यह स्टैक पैकेट रूटिंग, कंजेशन कंट्रोल और कनेक्शन प्रबंधन जैसे लो-लेवल विवरणों को संभालता है। यूजर-स्पेस एप्लिकेशन (उदाहरण के लिए, आपके C प्रोग्राम) इस स्टैक के साथ **बर्कले सॉकेट्स API** (जिसे POSIX सॉकेट्स के नाम से भी जाना जाता है) के माध्यम से इंटरैक्ट करते हैं, जो नेटवर्क कनेक्शन बनाने का एक मानकीकृत तरीका प्रदान करता है।

आपको TCP/IP स्वयं लागू करने की आवश्यकता नहीं है — यह कर्नेल करता है। इसके बजाय, आप कर्नेल से "बात" करने के लिए सॉकेट्स API का उपयोग करते हैं। यह API लिनक्स पर **स्टैंडर्ड C लाइब्रेरी (glibc) में बिल्ट-इन** है, इसलिए इंस्टॉल करने या लिंक करने के लिए कोई अलग "TCP/IP लाइब्रेरी" नहीं है। सब कुछ `libc` (GNU C लाइब्रेरी) द्वारा प्रदान किया जाता है।

#### मुख्य लाइब्रेरीज और हेडर
- **मुख्य लाइब्रेरी**: `libc` (glibc). सभी सॉकेट फ़ंक्शन यहाँ शामिल हैं। इसे अपने प्रोग्राम के साथ इम्प्लिसिटली लिंक करें (यह आमतौर पर `gcc` के साथ ऑटोमैटिक होता है)।
  - लोकेशन: आमतौर पर `/lib/x86_64-linux-gnu/libc.so.6` (या इसी तरह, आपके आर्किटेक्चर और डिस्ट्रो पर निर्भर करता है)। आप इसे `ldd /bin/ls` या `locate libc.so` से ढूंढ सकते हैं।
- **हेडर** (डिक्लेरेशन के लिए): ये लिनक्स डेवलपमेंट हेडर का हिस्सा हैं।
  - `<sys/socket.h>`: कोर सॉकेट फ़ंक्शन (जैसे `socket()`, `bind()`, `connect()`)।
  - `<netinet/in.h>`: इंटरनेट एड्रेस स्ट्रक्चर (जैसे IPv4 के लिए `struct sockaddr_in`)।
  - `<arpa/inet.h>`: एड्रेस कन्वर्ज़न फ़ंक्शन (जैसे `inet_addr()`)।
  - `<sys/types.h>`: बेसिक टाइप्स (अक्सर इनडायरेक्टली शामिल)।
  - लोकेशन: आमतौर पर `/usr/include/` (जैसे `/usr/include/sys/socket.h`)। अगर गायब हैं तो डेवलपमेंट हेडर इंस्टॉल करें (उदाहरण के लिए, Debian-आधारित सिस्टम पर `sudo apt install libc6-dev`)।

लिनक्स पर `-lsocket` जैसे एक्स्ट्रा फ्लैग्स की आवश्यकता नहीं है (कुछ पुराने यूनिक्स सिस्टम के विपरीत)। बस `gcc your_program.c -o your_program` से कंपाइल करें।

#### बेसिक उदाहरण: C में सिंपल TCP क्लाइंट
यहाँ एक मिनिमल TCP क्लाइंट है जो एक सर्वर (उदाहरण के लिए, example.com पर पोर्ट 80) से कनेक्ट होता है। यह सॉकेट्स API के उपयोग को प्रदर्शित करता है।

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>  // close() के लिए

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);  // TCP सॉकेट बनाएं (IPv4 के लिए AF_INET, TCP के लिए SOCK_STREAM)
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80);  // होस्ट-टू-नेटवर्क बाइट ऑर्डर
    inet_pton(AF_INET, "93.184.216.34", &server_addr.sin_addr);  // example.com का IP

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

- कंपाइल: `gcc -o tcp_client tcp_client.c`
- रन: `./tcp_client`

एक सर्वर के लिए, आप `connect()` के बजाय `bind()`, `listen()`, और `accept()` का उपयोग करेंगे।

#### और अधिक जानने के लिए
- **मैन पेज**: डिटेल्ड डॉक्स के लिए अपने लिनक्स सिस्टम पर `man socket` या `man 7 ip` चलाएं।
- **कर्नेल साइड**: अगर आपका मतलब कर्नेल-लेवल इम्प्लीमेंटेशन था, तो सोर्स को `/usr/src/linux/net/ipv4/` (TCP) या `/usr/src/linux/net/ipv6/` (IPv6 के लिए) में चेक करें। कर्नेल हेडर `sudo apt install linux-headers-$(uname -r)` से इंस्टॉल करें।
- रिसोर्सेज:
  - [Socket Programming in C (GeeksforGeeks)](https://www.geeksforgeeks.org/c/socket-programming-cc/)
  - [Programming Linux Sockets with TCP/IP (IBM Developer)](https://developer.ibm.com/tutorials/l-sock/)

अगर यह वह नहीं है जिसका आपने मतलब किया था (जैसे, कर्नेल मॉड्यूल या कुछ और), तो कृपया अधिक विवरण प्रदान करें!