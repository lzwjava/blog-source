---
audio: false
generated: true
lang: ar
layout: post
title: المصادقة باستخدام SASL في جافا
translated: true
type: note
---

لاستخدام حزمة `javax.security.sasl` في جافا، تحتاج إلى الاستفادة من فئاتها وواجهاتها لتنفيذ آليات طبقة المصادقة والأمان البسيطة (SASL) للمصادقة، وأمان البيانات اختياريًا في تطبيقات العميل والخادم. الفئات الأساسية المشاركة هي `Sasl` و `SaslClient` و `SaslServer`. فيما يلي دليل شامل حول كيفية استخدام هذه الحزمة، بما في ذلك الخطوات وكود المثال لكل من تطبيقات العميل والخادم.

---

### **نظرة عامة على javax.security.sasl**
توفر حزمة `javax.security.sasl` إطار عمل لمصادقة SASL، شائعة الاستخدام في بروتوكولات مثل LDAP أو IMAP أو التطبيقات المخصصة. وهي تشمل:
- **`Sasl`**: فئة أدوات مساعدة تحتوي على طرق ثابتة لإنشاء مثيلات `SaslClient` و `SaslServer`.
- **`SaslClient`**: تمثل جانب العميل في عملية مصادقة SASL.
- **`SaslServer`**: تمثل جانب الخادم في عملية مصادقة SASL.
- **`CallbackHandler`**: واجهة تقوم بتنفيذها للتعامل مع ردود الاتصال الخاصة بالمصادقة (مثل توفير أسماء المستخدمين أو كلمات المرور).

تتضمن العملية إنشاء `SaslClient` أو `SaslServer`، وتوفير معالج رد اتصال `CallbackHandler` لإدارة بيانات المصادقة، والمشاركة في تبادل التحدي والاستجابة حتى اكتمال المصادقة.

---

### **خطوات استخدام javax.security.sasl**

#### **1. تحديد دورك (عميل أم خادم)**
قرر ما إذا كان تطبيقك يعمل كعميل (يقوم بالمصادقة على الخادم) أو كخادم (يقوم بمصادقة عميل). هذا يحدد ما إذا كنت ستستخدم `SaslClient` أم `SaslServer`.

#### **2. اختر آلية SASL**
تدعم SASL آليات متنوعة، مثل:
- `PLAIN`: مصادقة اسم مستخدم/كلمة مرور بسيطة (بدون تشفير).
- `DIGEST-MD5`: تعتمد على كلمة المرور مع تحدي واستجابة.
- `GSSAPI`: مصادقة تعتمد على Kerberos.

اختر آلية مدعومة من قبل كل من العميل والخادم. للتبسيط، يستخدم هذا الدليل آلية `PLAIN` كمثال.

#### **3. نفذ معالج رد اتصال CallbackHandler**
مطلوب `CallbackHandler` لتوفير أو التحقق من بيانات اعتماد المصادقة. ستحتاج إلى تنفيذ واجهة `javax.security.auth.callback.CallbackHandler`.

- **للعميل**: قم بتوفير بيانات الاعتماد مثل اسم المستخدم وكلمة المرور.
- **للخادم**: تحقق من بيانات اعتماد العميل أو وفر بيانات مصادقة من جانب الخادم.

إليك مثالاً على `CallbackHandler` من جانب العميل لآلية `PLAIN`:

```java
import javax.security.auth.callback.*;
import java.io.IOException;

public class ClientCallbackHandler implements CallbackHandler {
    private final String username;
    private final String password;

    public ClientCallbackHandler(String username, String password) {
        this.username = username;
        this.password = password;
    }

    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                ((NameCallback) callback).setName(username);
            } else if (callback instanceof PasswordCallback) {
                ((PasswordCallback) callback).setPassword(password.toCharArray());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

بالنسبة للخادم، قد تقوم بالتحقق من بيانات الاعتماد مقابل قاعدة بيانات:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // استرجع كلمة المرور المتوقعة لاسم المستخدم من قاعدة بيانات
            } else if (callback instanceof PasswordCallback) {
                // عيّن كلمة المرور المتوقعة للتحقق
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. التنفيذ من جانب العميل**
للمصادقة كعميل:

1. **إنشاء SaslClient**:
   استخدم `Sasl.createSaslClient` مع الآلية والبروتوكول واسم الخادم والخصائص ومعالج رد الاتصال.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // اختياري؛ null إذا كان مطابقًا لمعرف المصادقة
   String protocol = "ldap"; // على سبيل المثال، "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // خصائص اختيارية، مثل QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **تعامل مع تبادل التحدي والاستجابة**:
   - تحقق من وجود استجابة أولية (شائع في الآليات التي يبدأها العميل مثل `PLAIN`).
   - أرسل الردود إلى الخادم وقم بمعالجة التحديات حتى تكتمل المصادقة.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // أرسل الرد إلى الخادم (يعتمد على البروتوكول، مثلاً عبر مقبس أو طلب LDAP BindRequest)
   }

   // استقبل تحديًا من الخادم (يعتمد على البروتوكول)
   byte[] challenge = /* اقرأ من الخادم */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // أرسل الرد إلى الخادم
       if (sc.isComplete()) break;
       challenge = /* اقرأ التحدي التالي من الخادم */;
   }

   // اكتملت المصادقة؛ تحقق من النجاح عبر وسائل تعتمد على البروتوكول
   ```

   بالنسبة لـ `PLAIN`، يرسل العميل بيانات الاعتماد في الرد الأولي، ويستجيب الخادم عادةً بالنجاح أو الفشل دون تحديات إضافية.

#### **5. التنفيذ من جانب الخادم**
لمصادقة عميل كخادم:

1. **إنشاء SaslServer**:
   استخدم `Sasl.createSaslServer` مع الآلية والبروتوكول واسم الخادم والخصائص ومعالج رد الاتصال.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslServer;
   import java.util.HashMap;

   String mechanism = "PLAIN";
   String protocol = "ldap";
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null;
   CallbackHandler cbh = new ServerCallbackHandler();

   SaslServer ss = Sasl.createSaslServer(mechanism, protocol, serverName, props, cbh);
   ```

2. **تعامل مع تبادل التحدي والاستجابة**:
   - معالجة الرد الأولي للعميل وإنشاء التحديات حتى تكتمل المصادقة.

   ```java
   byte[] response = /* اقرأ الرد الأولي من العميل */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // أرسل التحدي إلى العميل (يعتمد على البروتوكول)

   while (!ss.isComplete()) {
       response = /* اقرأ الرد التالي من العميل */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // اكتملت المصادقة
           break;
       }
       // أرسل التحدي إلى العميل
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // تابع مع المستخدم المصرح له
   }
   ```

   بالنسبة لـ `PLAIN`، يتحقق الخادم من بيانات الاعتماد في الرد الأولي ويكمل المصادقة دون تحديات إضافية.

#### **6. اختياري: استخدام طبقات الأمان**
إذا كانت الآلية (مثل `DIGEST-MD5`) تدعم طبقة أمان:
- استخدم `sc.wrap()` و `sc.unwrap()` على العميل، أو `ss.wrap()` و `ss.unwrap()` على الخادم، لتشفير/فك تشفير الرسائل بعد المصادقة.
- `PLAIN` لا يدعم طبقات الأمان.

---

### **نقاط رئيسية**
- **التكامل**: قم بتضمين تبادل SASL في بروتوكول اتصال تطبيقك (مثل طلبات LDAP Bind، أو أوامر IMAP AUTHENTICATE).
- **معالجة الأخطاء**: لف الكود في كتل try-catch للتعامل مع `SaslException` والأخطاء المحتملة الأخرى.
- **الخصائص**: استخدم خريطة `props` لتكوين خيارات مثل جودة الحماية (`"javax.security.sasl.qop"`) إذا كانت مدعومة من قبل الآلية.

---

### **مثال على حالة الاستخدام**
لعميل LDAP يقوم بالمصادقة باستخدام `PLAIN`:
1. قم بإنشاء `SaslClient` بآلية `PLAIN`.
2. أرسل طلب LDAP `BindRequest` مع الآلية والرد الأولي (`sc.evaluateChallenge(new byte[0])`).
3. معالجة `BindResponse` من الخادم لتأكيد النجاح.

لبروتوكول مخصص، استبدل الخطوات المحددة لـ LDAP بأوامر المصادقة الخاصة بالبروتوكول الخاص بك.

---

باتباع هذه الخطوات، يمكنك استخدام `javax.security.sasl` بشكل فعال لتنفيذ مصادقة SASL في تطبيق جافا الخاص بك، وتخصيص العملية للآلية والبروتوكول المختارين.