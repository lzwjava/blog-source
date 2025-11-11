---
audio: false
generated: true
lang: ar
layout: post
title: اتصالات آمنة في جافا
translated: true
type: note
---

لاستخدام حزمة `javax.net.ssl` في جافا، تحتاج إلى الاستفادة من فئاتها لإقامة اتصال آمن عبر الشبكة باستخدام بروتوكولات SSL (Secure Sockets Layer) أو TLS (Transport Layer Security). هذه الحزمة أساسية لإنشاء اتصالات آمنة، مثل تلك المستخدمة في اتصالات HTTPS. أدناه، سأشرح كيفية استخدامها لكل من التطبيقات من جانب العميل ومن جانب الخادم، بما في ذلك الأمثلة الأساسية والاعتبارات الرئيسية.

---

### **نظرة عامة على `javax.net.ssl`**
توفر حزمة `javax.net.ssl` أدوات للاتصال الآمن عبر المقابس (Sockets). تتضمن:
- **`SSLSocket`**: مأخذ (Socket) من جانب العميل للاتصال الآمن.
- **`SSLServerSocket`**: مأخذ (Socket) من جانب الخادم لقبول الاتصالات الآمنة.
- **`SSLSocketFactory`**: مصنع لإنشاء نسخ من `SSLSocket`.
- **`SSLServerSocketFactory`**: مصنع لإنشاء نسخ من `SSLServerSocket`.
- **`SSLContext`**: فئة لتكوين بروتوكول SSL/TLS، مما يسمح بتخصيص إعدادات الأمان.
- **`KeyManager` و `TrustManager`**: فئات لإدارة الشهادات وقرارات الثقة.

هذه المكونات تمكن تبادل البيانات المشفرة، مما يضمن السرية والسلامة بين العميل والخادم.

---

### **استخدام `javax.net.ssl` كعميل**
لتطبيق عميل يتصل بخادم آمن (مثل خادم HTTPS)، تستخدم عادةً `SSLSocketFactory` لإنشاء `SSLSocket`. إليك الطريقة:

#### **الخطوات**
1.  **الحصول على `SSLSocketFactory`**:
    استخدم المصنع الافتراضي المقدم من جافا، والذي يعتمد على إعدادات SSL/TLS الافتراضية للنظام ومستودع الثقة (Truststore) (مستودع الشهادات الموثوقة).

    ```java
    import javax.net.ssl.SSLSocketFactory;
    SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
    ```

2.  **إنشاء `SSLSocket`**:
    استخدم المصنع للاتصال بخادم عن طريق تحديد اسم المضيف والمنفذ (مثال: 443 لـ HTTPS).

    ```java
    import javax.net.ssl.SSLSocket;
    SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);
    ```

3.  **الاتصال عبر المأخذ (Socket)**:
    استخدم تدفقات الإدخال والإخراج الخاصة بالمأخذ (Socket) لإرسال البيانات واستقبالها. تحدث مصافحة SSL/TLS (التي تنشئ الاتصال الآمن) تلقائيًا عندما تقرأ من المأخذ (Socket) أو تكتب إليه لأول مرة.

#### **مثال: إرسال طلب HTTP GET**
إليك مثالًا كاملاً يتصل بخادم ويسترجع صفحة ويب:

```java
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import java.io.*;

public class SSLClientExample {
    public static void main(String[] args) {
        try {
            // الحصول على SSLSocketFactory الافتراضي
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // إنشاء SSLSocket للاتصال بـ example.com على المنفذ 443
            SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);

            // الحصول على تدفقات الإدخال والإخراج
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // إرسال طلب HTTP GET بسيط
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            // قراءة الرد وطباعته
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // إغلاق المأخذ (Socket)
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### **ملاحظات رئيسية**
- **المصافحة**: يتم التعامل مع مصافحة SSL/TLS تلقائيًا عند استخدام المأخذ (Socket).
- **الثقة**: بشكل افتراضي، تثق جافا بالشهادات الموقعة من قبل سلطات الشهادات المعروفة (CAs) المخزنة في مستودع الثقة (Truststore) الخاص بها. إذا لم تكن شهادة الخادم موثوقة، فستحتاج إلى تكوين مستودع ثقة مخصص (المزيد عن هذا لاحقًا).
- **التحقق من اسم المضيف**: `SSLSocket` لا يقوم بالتحقق من اسم المضيف بشكل افتراضي (على عكس `HttpsURLConnection`). لتمكينه، استخدم `SSLParameters`:

    ```java
    import javax.net.ssl.SSLParameters;
    SSLParameters params = new SSLParameters();
    params.setEndpointIdentificationAlgorithm("HTTPS");
    socket.setSSLParameters(params);
    ```

    هذا يضمن تطابق شهادة الخادم مع اسم المضيف، مما يمنع هجمات الرجل في المنتصف (Man-in-the-Middle).

---

### **استخدام `javax.net.ssl` كخادم**
لخادم يقبل اتصالات آمنة، تستخدم `SSLServerSocketFactory` لإنشاء `SSLServerSocket`. يجب على الخادم تقديم شهادة، يتم تخزينها عادةً في مستودع المفاتيح (Keystore).

#### **الخطوات**
1.  **إعداد مستودع المفاتيح (Keystore)**:
    أنشئ مستودع مفاتيح يحتوي على المفتاح الخاص للخادم وشهادته (مثال: باستخدام أداة `keytool` الخاصة بجافا لإنشاء ملف `.jks`).

2.  **تهيئة `SSLContext`**:
    استخدم مستودع المفاتيح لتكوين `SSLContext` مع `KeyManager`.

    ```java
    import javax.net.ssl.*;
    import java.io.FileInputStream;
    import java.security.KeyStore;

    KeyStore ks = KeyStore.getInstance("JKS");
    ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

    KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
    kmf.init(ks, "password".toCharArray());

    SSLContext context = SSLContext.getInstance("TLS");
    context.init(kmf.getKeyManagers(), null, null);
    ```

3.  **إنشاء `SSLServerSocket`**:
    استخدم `SSLServerSocketFactory` من `SSLContext` لإنشاء مأخذ خادم (Server Socket).

    ```java
    SSLServerSocketFactory factory = context.getServerSocketFactory();
    SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);
    ```

4.  **قبول الاتصالات**:
    اقبل اتصالات العملاء وتواصل عبر `SSLSocket` الناتج.

#### **مثال: خادم SSL بسيط**
```java
import javax.net.ssl.*;
import java.io.*;
import java.security.KeyStore;

public class SSLServerExample {
    public static void main(String[] args) {
        try {
            // تحميل مستودع المفاتيح
            KeyStore ks = KeyStore.getInstance("JKS");
            ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

            // تهيئة KeyManagerFactory
            KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
            kmf.init(ks, "password".toCharArray());

            // تهيئة SSLContext
            SSLContext context = SSLContext.getInstance("TLS");
            context.init(kmf.getKeyManagers(), null, null);

            // إنشاء SSLServerSocket
            SSLServerSocketFactory factory = context.getServerSocketFactory();
            SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);

            System.out.println("Server started on port 8443...");
            while (true) {
                SSLSocket socket = (SSLSocket) serverSocket.accept();
                System.out.println("Client connected.");

                // التعامل مع اتصال العميل
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                out.println("Hello from the secure server!");
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### **ملاحظات رئيسية**
- **مستودع المفاتيح (Keystore)**: الخادم يتطلب شهادة، عادةً في ملف `.jks`، والتي يجب أن تنشئها وتكونها.
- **مصادقة العميل**: إذا كان الخادم يتطلب من العملاء تقديم شهادات، فقم بتهيئة `SSLContext` مع `TrustManager` واستدعِ `serverSocket.setNeedClientAuth(true)`.

---

### **التكوين المتقدم**
لمزيد من التحكم في سلوك SSL/TLS، يمكنك تخصيص ما يلي:

#### **1. مستودع ثقة مخصص (Custom Truststore)**
إذا لم تكن شهادة الخادم موقعة من قبل سلطة شهادات موثوقة (CA)، فقم بتحميل مستودع ثقة مخصص:

```java
KeyStore trustStore = KeyStore.getInstance("JKS");
trustStore.load(new FileInputStream("truststore.jks"), "password".toCharArray());

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(trustStore);

SSLContext context = SSLContext.getInstance("TLS");
context.init(null, tmf.getTrustManagers(), null);

SSLSocketFactory factory = context.getSocketFactory();
```

#### **2. إصدارات البروتوكول**
حدد البروتوكولات الآمنة (مثل TLS 1.2 أو 1.3) لتجنب الإصدارات غير الآمنة القديمة:

```java
socket.setEnabledProtocols(new String[] {"TLSv1.2", "TLSv1.3"});
```

#### **3. مجموعات التشفير (Cipher Suites)**
اقصر مجموعات التشفير المستخدمة للتشفير:

```java
socket.setEnabledCipherSuites(new String[] {"TLS_AES_128_GCM_SHA256"});
```

---

### **ملخص**
لاستخدام `javax.net.ssl`:
- **للعملاء**: استخدم `SSLSocketFactory` لإنشاء `SSLSocket`، والتصل بخادم، وقم بشكل اختياري بتكوين التحقق من اسم المضيف باستخدام `SSLParameters`.
- **للخوادم**: قم بتكوين `SSLContext` مع مستودع مفاتيح و `KeyManager`، ثم استخدم `SSLServerSocketFactory` لإنشاء `SSLServerSocket`.
- **التخصيص**: استخدم `SSLContext` و `KeyManager` و `TrustManager` للتعامل المتقدم مع الشهادات، وحدد البروتوكولات أو مجموعات التشفير حسب الحاجة.

توفر هذه الحزمة الأساس للاتصال الآمن في جافا، وهي مناسبة لكل من التطبيقات البسيطة والمعقدة. بالنسبة لـ HTTPS تحديدًا، فكر في استخدام واجهات برمجة تطبيقات (APIs) ذات مستوى أعلى مثل `HttpsURLConnection`، لكن `javax.net.ssl` يمنحك تحكمًا مباشرًا في مقابس (Sockets) SSL/TLS عندما تحتاج إلى ذلك.