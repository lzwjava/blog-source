---
audio: false
generated: true
lang: ar
layout: post
title: اتصالات آمنة في جاڤا
translated: true
---

لاستخدام حزمة `javax.net.ssl` في Java، عليك استغلال فئاتها لإنشاء اتصال آمن عبر الشبكة باستخدام بروتوكولات SSL (Secure Sockets Layer) أو TLS (Transport Layer Security). هذه الحزمة ضرورية لإنشاء اتصالات آمنة مثل تلك المستخدمة في HTTPS. أدناه، سأشرح كيفية استخدامها في تطبيقات الطرف العميل والطرف الخادم، بما في ذلك أمثلة أساسية ومفاهيم رئيسية.

---

### **نظرة عامة على `javax.net.ssl`**
توفر حزمة `javax.net.ssl` أدوات للاتصال الآمن عبر الجوكر. وتشمل:
- **`SSLSocket`**: جوكر طرف العميل للاتصال الآمن.
- **`SSLServerSocket`**: جوكر طرف الخادم لاستقبال الاتصالات الآمنة.
- **`SSLSocketFactory`**: مصنع لإنشاءInstances من `SSLSocket`.
- **`SSLServerSocketFactory`**: مصنع لإنشاءInstances من `SSLServerSocket`.
- **`SSLContext`**: فئة لتكوين بروتوكول SSL/TLS، مما يسمح بتخصيص إعدادات الأمان.
- **`KeyManager` و `TrustManager`**: فئات لإدارة الشهادات وقرارات الثقة.

تسمح هذه المكونات بتداول البيانات المشفرة، مما يضمن السرية والسلامة بين العميل والخادم.

---

### **استخدام `javax.net.ssl` كعميل**
لإتصال تطبيق العميل إلى خادم آمن (مثل خادم HTTPS)، تستخدم عادةً `SSLSocketFactory` لإنشاء `SSLSocket`. إليك كيفية ذلك:

#### **الخطوات**
1. **الحصول على `SSLSocketFactory`**:
   استخدم المصنع الافتراضي الذي يوفره Java، والذي يعتمد على إعدادات SSL/TLS الافتراضية للنظام و `truststore` (مخزن الشهادات المصدقة).

   ```java
   import javax.net.ssl.SSLSocketFactory;
   SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
   ```

2. **إنشاء `SSLSocket`**:
   استخدم المصنع للاتصال إلى الخادم عن طريق تحديد اسم المضيف والميناء (مثل 443 لـ HTTPS).

   ```java
   import javax.net.ssl.SSLSocket;
   SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);
   ```

3. **التواصل عبر الجوكر**:
   استخدم تدفقات الإدخال والإخراج للجوكر لإرسال واستقبال البيانات. تحدث عملية التزامن SSL/TLS (التي تحدد الاتصال الآمن) تلقائيًا عندما تقرأ أو تكتب في الجوكر لأول مرة.

#### **مثال: إرسال طلب HTTP GET**
هنا مثال كامل يربط إلى خادم ويسترجع صفحة ويب:

```java
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import java.io.*;

public class SSLClientExample {
    public static void main(String[] args) {
        try {
            // الحصول على SSLSocketFactory الافتراضي
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // إنشاء SSLSocket إلى example.com على الميناء 443
            SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);

            // الحصول على تدفقات الإدخال والإخراج
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // إرسال طلب HTTP GET بسيط
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            // قراءة وإظهار الرد
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // إغلاق الجوكر
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### **ملاحظات رئيسية**
- **التزامن**: يتم التعامل مع التزامن SSL/TLS تلقائيًا عند استخدام الجوكر.
- **الثقة**: يثق Java بشكل افتراضي بالشهادات الموقعة من السلطات المصدقة المعروفة (CAs) المخزنة في مخزن الثقة الخاص به. إذا لم يكن شهادة الخادم مصدقة، عليك تكوين مخزن ثقة مخصص (أكثر من ذلك لاحقًا).
- **تحقق من اسم المضيف**: لا يقوم `SSLSocket` بتحقق من اسم المضيف بشكل افتراضي (خلافًا لـ `HttpsURLConnection`). لتفعيل ذلك، استخدم `SSLParameters`:

   ```java
   import javax.net.ssl.SSLParameters;
   SSLParameters params = new SSLParameters();
   params.setEndpointIdentificationAlgorithm("HTTPS");
   socket.setSSLParameters(params);
   ```

   هذا يضمن أن شهادة الخادم تتطابق مع اسم المضيف، مما يمنع هجمات الرجل في الوسط.

---

### **استخدام `javax.net.ssl` كخادم**
لخادم يقبل الاتصالات الآمنة، تستخدم `SSLServerSocketFactory` لإنشاء `SSLServerSocket`. يجب على الخادم تقديم شهادة، عادةً مخزنة في مخزن.

#### **الخطوات**
1. **إعداد مخزن**:
   إنشاء مخزن يحتوي على المفتاح الخاص والخادم (مثل استخدام `keytool` من Java لإنشاء ملف `.jks`).

2. **تهيئة `SSLContext`**:
   استخدم المخزن لتكوين `SSLContext` مع `KeyManager`.

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

3. **إنشاء `SSLServerSocket`**:
   استخدم `SSLServerSocketFactory` من `SSLContext` لإنشاء جوكر خادم.

   ```java
   SSLServerSocketFactory factory = context.getServerSocketFactory();
   SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);
   ```

4. **قبول الاتصالات**:
   قبول اتصالات العميل وتواصل عبر `SSLSocket` الناتج.

#### **مثال: خادم SSL بسيط**
```java
import javax.net.ssl.*;
import java.io.*;
import java.security.KeyStore;

public class SSLServerExample {
    public static void main(String[] args) {
        try {
            // تحميل المخزن
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

            System.out.println("الخادم بدأ على الميناء 8443...");
            while (true) {
                SSLSocket socket = (SSLSocket) serverSocket.accept();
                System.out.println("عميل متصل.");

                // معالجة اتصال العميل
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                out.println("مرحبًا من الخادم الآمن!");
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### **ملاحظات رئيسية**
- **مخزن**: يتطلب الخادم شهادة، عادةً في ملف `.jks`، يجب عليك إنشاؤه وتكوينه.
- **تحقق من العميل**: إذا كان الخادم يتطلب من العميل تقديم شهادات، فاستخدم `TrustManager` وتهيئة `SSLContext` و `serverSocket.setNeedClientAuth(true)`.

---

### **تكوين متقدم**
للمزيد من التحكم في سلوك SSL/TLS، يمكنك تخصيص ما يلي:

#### **1. مخزن ثقة مخصص**
إذا لم تكن شهادة الخادم موقعة من سلطة مصدقة، قم بتحميل مخزن ثقة مخصص:

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
حدد البروتوكولات الآمنة (مثل TLS 1.2 أو 1.3) لتجنب الإصدارات القديمة غير الآمنة:

```java
socket.setEnabledProtocols(new String[] {"TLSv1.2", "TLSv1.3"});
```

#### **3. مجموعات التشفير**
قم بتقييد مجموعات التشفير المستخدمة للتشفير:

```java
socket.setEnabledCipherSuites(new String[] {"TLS_AES_128_GCM_SHA256"});
```

---

### **ملخص**
لاستخدام `javax.net.ssl`:
- **لعميل**: استخدم `SSLSocketFactory` لإنشاء `SSLSocket`، اتصل إلى خادم، وتكوين التحقق من اسم المضيف مع `SSLParameters` (اختياري).
- **لخادم**: قم بتكوين `SSLContext` مع مخزن و `KeyManager`، ثم استخدم `SSLServerSocketFactory` لإنشاء `SSLServerSocket`.
- **التخصيص**: استخدم `SSLContext` و `KeyManager` و `TrustManager` لتدبير الشهادات المتقدمة، وحدد البروتوكولات أو مجموعات التشفير حسب الحاجة.

توفر هذه الحزمة الأساس للاتصال الآمن في Java، مناسبة لكل من التطبيقات البسيطة والمتقدمة. بالنسبة لـ HTTPS بشكل خاص، فاعتبر استخدام واجهات برمجة التطبيقات ذات المستوى الأعلى مثل `HttpsURLConnection`، ولكن `javax.net.ssl` يوفر لك التحكم المباشر على جوكرات SSL/TLS عندما يكون ذلك ضروريًا.