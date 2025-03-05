---
audio: false
generated: true
lang: ar
layout: post
title: التحقق من SASL في جاڤا
translated: true
---

لاستخدام حزمة `javax.security.sasl` في Java، يجب عليك استغلال فئاتها وواجهاتها لتطبيق آليات طبقة التحقق من الهوية والامن البسيطة (SASL) للتحقق من الهوية، واختيارياً، أمان البيانات في تطبيقات العميل-الخادم. الفئات الرئيسية المعنية هي `Sasl`، `SaslClient`، و `SaslServer`. أدناه دليل شامل على كيفية استخدام هذه الحزمة، بما في ذلك الخطوات والشيفرة المثالية لكل من تطبيقات العميل والخادم.

---

### **نظرة عامة على javax.security.sasl**
توفر حزمة `javax.security.sasl` إطارًا لتطبيق التحقق من الهوية SASL، والذي يستخدم بشكل شائع في بروتوكولات مثل LDAP، IMAP، أو التطبيقات المخصصة. وتشمل:
- **`Sasl`**: فئة مساعدة تحتوي على طرق ثابتة لإنشاء instances من `SaslClient` و `SaslServer`.
- **`SaslClient`**: يمثل الجانب العميل من عملية التحقق من الهوية SASL.
- **`SaslServer`**: يمثل الجانب الخادم من عملية التحقق من الهوية SASL.
- **`CallbackHandler`**: واجهة يجب عليك تنفيذها لتعامل مع استدعاءات التحقق من الهوية (مثل تقديم أسماء المستخدمين أو كلمات المرور).

يتضمن العملية إنشاء `SaslClient` أو `SaslServer`، وتقديم معالج استدعاء لإدارة بيانات التحقق من الهوية، وقيام بمبادلة التحدي والإجابة حتى يتم إكمال التحقق من الهوية.

---

### **خطوات لاستخدام javax.security.sasl**

#### **1. تحديد دورك (عميل أو خادم)**
قم بتحديد ما إذا كان تطبيقك يعمل كعميل (تحقق من الهوية إلى خادم) أو خادم (تحقق من الهوية العميل). هذا يحدد ما إذا كنت ستستخدم `SaslClient` أو `SaslServer`.

#### **2. اختيار آلية SASL**
يقدم SASL آليات مختلفة مثل:
- `PLAIN`: التحقق من الهوية البسيطة باسم المستخدم وكلمة المرور (بدون تشفير).
- `DIGEST-MD5`: التحقق من الهوية بناءً على كلمة المرور مع التحدي والإجابة.
- `GSSAPI`: التحقق من الهوية بناءً على Kerberos.

اختر آلية يدعمها كل من العميل والخادم. من أجل البساطة، يستخدم هذا الدليل آلية `PLAIN` كمثال.

#### **3. تنفيذ CallbackHandler**
يحتاج `CallbackHandler` إلى تقديم أو التحقق من بيانات التحقق من الهوية. يجب عليك تنفيذ واجهة `javax.security.auth.callback.CallbackHandler`.

- **لعميل**: تقديم بيانات مثل اسم المستخدم وكلمة المرور.
- **لخادم**: التحقق من بيانات التحقق من الهوية العميل أو تقديم بيانات التحقق من الهوية من جانب الخادم.

هنا مثال على `CallbackHandler` من جانب العميل لآلية `PLAIN`:

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

لخادم، قد تحقق من بيانات التحقق من الهوية ضد قاعدة بيانات:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // استرجاع كلمة المرور المتوقعة لاسم المستخدم من قاعدة بيانات
            } else if (callback instanceof PasswordCallback) {
                // تعيين كلمة المرور المتوقعة للتحقق منها
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. تنفيذ العميل**
لتحقق من الهوية كعميل:

1. **إنشاء SaslClient**:
   استخدم `Sasl.createSaslClient` مع الآلية، البروتوكول، اسم الخادم، الخصائص، ومعالج الاستدعاء.

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // اختياري؛ null إذا كان نفس الهوية التحقق من الهوية
   String protocol = "ldap"; // مثلا، "ldap"، "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // خصائص اختيارية، مثلا، QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **التعامل مع مبادلة التحدي والإجابة**:
   - التحقق من وجود إجابة أولية (شائعة في آليات العميل الأول مثل `PLAIN`).
   - إرسال الإجابات إلى الخادم وتعمل على التحديات حتى يتم إكمال التحقق من الهوية.

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // إرسال الإجابة إلى الخادم (محدد بالبروتوكول، مثلا، عبر الماسح الضوئي أو LDAP BindRequest)
   }

   // استلام تحدي الخادم (محدد بالبروتوكول)
   byte[] challenge = /* قراءة من الخادم */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // إرسال الإجابة إلى الخادم
       if (sc.isComplete()) break;
       challenge = /* قراءة التحدي التالي من الخادم */;
   }

   // إكمال التحقق من الهوية؛ التحقق من النجاح عبر وسائل محددة بالبروتوكول
   ```

   بالنسبة لـ `PLAIN`، يرسل العميل بيانات التحقق من الهوية في الإجابة الأولية، ويجيب الخادم عادةً بنجاح أو فشل دون تحديات إضافية.

#### **5. تنفيذ الخادم**
لتحقق من الهوية العميل كخادم:

1. **إنشاء SaslServer**:
   استخدم `Sasl.createSaslServer` مع الآلية، البروتوكول، اسم الخادم، الخصائص، ومعالج الاستدعاء.

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

2. **التعامل مع مبادلة التحدي والإجابة**:
   - معالجة الإجابة الأولية للعميل وإنتاج التحديات حتى يتم إكمال التحقق من الهوية.

   ```java
   byte[] response = /* قراءة الإجابة الأولية من العميل */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // إرسال التحدي إلى العميل (محدد بالبروتوكول)

   while (!ss.isComplete()) {
       response = /* قراءة الإجابة التالية من العميل */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // إكمال التحقق من الهوية
           break;
       }
       // إرسال التحدي إلى العميل
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // الاستمرار مع المستخدم المصرح له
   }
   ```

   بالنسبة لـ `PLAIN`، يثبت الخادم من بيانات التحقق من الهوية في الإجابة الأولية ويكمل التحقق من الهوية دون تحديات إضافية.

#### **6. اختياري: استخدام طبقات الأمان**
إذا دعمت الآلية (مثل `DIGEST-MD5`) طبقة أمان:
- استخدم `sc.wrap()` و `sc.unwrap()` على العميل، أو `ss.wrap()` و `ss.unwrap()` على الخادم، لتشفير/فك تشفير الرسائل بعد التحقق من الهوية.
- لا تدعم `PLAIN` طبقات الأمان.

---

### **نقاط رئيسية**
- **الدمج**: ادخل مبادلة SASL في بروتوكول الاتصال الخاص بتطبيقك (مثل طلبات LDAP Bind، أوامر IMAP AUTHENTICATE).
- **التعامل مع الأخطاء**: احاط الكود في كتلة try-catch لتعامل مع `SaslException` وجميع الأخطاء المحتملة الأخرى.
- **الخصائص**: استخدم خريطة `props` لتكوين خيارات مثل جودة الحماية (`"javax.security.sasl.qop"`) إذا دعمتها الآلية.

---

### **مثال على حالة استخدام**
لعميل LDAP يثبت من هوية باستخدام `PLAIN`:
1. إنشاء `SaslClient` مع آلية `PLAIN`.
2. إرسال طلب LDAP `BindRequest` مع الآلية والإجابة الأولية (`sc.evaluateChallenge(new byte[0])`).
3. معالجة إجابة الخادم `BindResponse` لتأكيد النجاح.

لبروتوكول مخصص، استبدل الخطوات المحددة بـ LDAP بخطوات التحقق من الهوية الخاصة ببروتوكولك.

---

بالتالي، يمكنك استخدام `javax.security.sasl` بشكل فعال لتطبيق التحقق من الهوية SASL في تطبيق Java الخاص بك، وتخصيص العملية وفقًا لآلية وبروتوكولك المختارين.