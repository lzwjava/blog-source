---
audio: false
generated: true
lang: ar
layout: post
title: المصادقة والتفويض في جافا
translated: true
type: note
---

لاستخدام حزمة `javax.security.auth` في جافا، تحتاج إلى فهم أنها جزء من إطار عمل Java Authentication and Authorization Service (JAAS). توفر هذه الحزمة فئات وواجهات للمصادقة على المستخدمين (التحقق من هويتهم) والتفويض لهم (تحديد ما يمكنهم القيام به). فيما يلي دليل خطوة بخطوة لاستخدام `javax.security.auth` في سيناريو مصادقة أساسي، مثل مصادقة مستخدم باسم مستخدم وكلمة مرور.

---

### **نظرة عامة على المفاهيم الأساسية**
قبل الخوض في الخطوات، إليك شرح موجز للمكونات الأساسية في `javax.security.auth`:

- **الموضوع (Subject)**: يمثل كيانًا (مثل مستخدم أو خدمة) يتم مصادقته. يمكن أن يحتوي على هويات متعددة (Principals) ومعلومات اعتماد (مثل كلمات المرور أو الشهادات).
- **الرئيسي (Principal)**: هوية أو دور مرتبط بموضوع، مثل اسم مستخدم أو عضوية في مجموعة.
- **بيان الاعتماد (Credential)**: معلومات تستخدم للمصادقة على موضوع، مثل كلمة مرور أو مفتاح تشفير.
- **وحدة تسجيل الدخول (LoginModule)**: مكون قابل للإضافة ينفذ منطق المصادقة (مثل التحقق من اسم المستخدم وكلمة المرور مقابل قاعدة بيانات).
- **سياق تسجيل الدخول (LoginContext)**: الفئة المركزية التي تنسق عملية المصادقة باستخدام واحدة أو أكثر من وحدات LoginModule.
- **معالج الاستدعاء (CallbackHandler)**: واجهة للتفاعل مع المستخدم، مثل طلب اسم المستخدم وكلمة المرور.

مع أخذ هذه المفاهيم في الاعتبار، دعنا نستكشف كيفية استخدام الحزمة.

---

### **خطوات استخدام `javax.security.auth`**

#### **1. إعداد تكوين JAAS**
تعتمد عملية المصادقة على تكوين يحدد أي وحدات `LoginModule` سيتم استخدامها. يمكن تعريف هذا في ملف تكوين أو برمجيًا.

على سبيل المثال، أنشئ ملفًا باسم `jaas.config` بالمحتوى التالي:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: اسم التطبيق أو السياق، والذي ستشير إليه في الكود الخاص بك.
- **`com.example.MyLoginModule`**: الاسم الكامل المحدد لوحدة `LoginModule` المخصصة الخاصة بك (ستقوم بتنفيذها لاحقًا).
- **`required`**: علم يشير إلى أن هذه الوحدة يجب أن تنجح لكي تمر المصادقة. تشمل الأعلام الأخرى `requisite`، و`sufficient`، و`optional`، والتي تسمح بمنطق أكثر تعقيدًا مع وحدات متعددة.

عيّن خاصية النظام للإشارة إلى هذا الملف:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

بدلاً من ذلك، يمكنك تعيين التكوين برمجيًا، لكن استخدام الملف أبسط في معظم الحالات.

#### **2. تنفيذ معالج استدعاء (CallbackHandler)**
يجمع `CallbackHandler` المدخلات من المستخدم، مثل اسم المستخدم وكلمة المرور. إليك تنفيذ بسيط باستخدام وحدة التحكم:

```java
import javax.security.auth.callback.*;
import java.io.*;

public class MyCallbackHandler implements CallbackHandler {
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                NameCallback nc = (NameCallback) callback;
                System.out.print(nc.getPrompt());
                nc.setName(System.console().readLine());
            } else if (callback instanceof PasswordCallback) {
                PasswordCallback pc = (PasswordCallback) callback;
                System.out.print(pc.getPrompt());
                pc.setPassword(System.console().readPassword());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

- **NameCallback**: يطلب ويسترد اسم المستخدم.
- **PasswordCallback**: يطلب ويسترد كلمة المرور (يتم تخزينها كـ `char[]` للأمان).

#### **3. تنفيذ وحدة تسجيل دخول (LoginModule)**
تحدد `LoginModule` منطق المصادقة. فيما يلي مثال أساسي يتحقق من اسم مستخدم وكلمة مرور ثابتة (في الممارسة العملية، ستستخدم قاعدة بيانات أو خدمة خارجية):

```java
import javax.security.auth.*;
import javax.security.auth.callback.*;
import javax.security.auth.login.*;
import javax.security.auth.spi.*;
import java.security.Principal;
import java.util.*;

public class MyLoginModule implements LoginModule {
    private Subject subject;
    private CallbackHandler callbackHandler;
    private boolean succeeded = false;

    // تهيئة الوحدة
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // تنفيذ المصادقة
    public boolean login() throws LoginException {
        if (callbackHandler == null) {
            throw new LoginException("No callback handler provided");
        }

        try {
            NameCallback nameCallback = new NameCallback("Username: ");
            PasswordCallback passwordCallback = new PasswordCallback("Password: ", false);
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});

            String username = nameCallback.getName();
            char[] password = passwordCallback.getPassword();

            // فحص ثابت (استبدل بمنطق حقيقي في الممارسة العملية)
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Authentication failed");
            }
        } catch (Exception e) {
            throw new LoginException("Login error: " + e.getMessage());
        }
    }

    // إتمام المصادقة (إضافة Principals إلى Subject)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // إحباط عملية المصادقة
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // تسجيل خروج Subject
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// تنفيذ بسيط لـ Principal
class MyPrincipal implements Principal {
    private String name;

    public MyPrincipal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

- **login()**: يستخدم `CallbackHandler` للحصول على بيانات الاعتماد والتحقق منها.
- **commit()**: إذا نجحت المصادقة، يضيف `Principal` إلى `Subject`.
- **abort()** و **logout()**: يتعاملان مع التنظيف أو الإلغاء.

#### **4. المصادقة باستخدام LoginContext**
الآن، استخدم `LoginContext` لتنفيذ المصادقة في تطبيقك الرئيسي:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // تأكد من تعيين تكوين JAAS
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // إنشاء LoginContext باسم التكوين و CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // تنفيذ المصادقة
            lc.login();

            // الحصول على Subject الذي تمت مصادقته
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // طباعة Principals الخاصة بـ Subject
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // تسجيل الخروج عند الانتهاء
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: يربط بتكوين `"MyApp"` ويستخدم `MyCallbackHandler`.
- **`lc.login()`**: يشغل عملية المصادقة.
- **`lc.getSubject()`**: يسترد `Subject` الذي تمت مصادقته.

#### **5. تنفيذ إجراءات مصرح بها (اختياري)**
بمجرد المصادقة، يمكنك استخدام `Subject` لتنفيذ الكود مع امتيازاته باستخدام `Subject.doAs()`:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // نفّذ الإجراءات المميزة هنا
        return null;
    }
});
```

هذا مفيد للتفويض، حيث يتم تقييد الإجراءات بناءً على `Principals` الخاصة بـ `Subject`.

---

### **دمج كل شيء معًا**
1. **التكوين**: حدد `jaas.config` مع `LoginModule` الخاص بك.
2. **معالج الاستدعاء**: نفّذ `MyCallbackHandler` لجمع مدخلات المستخدم.
3. **وحدة تسجيل الدخول**: نفّذ `MyLoginModule` بمنطق المصادقة الخاص بك.
4. **الكود الرئيسي**: استخدم `LoginContext` للمصادقة واسترداد `Subject`.
5. **التفويض**: استخدم `Subject.doAs()` للإجراءات المميزة إذا لزم الأمر.

عند تشغيل الفئة `Main`، سوف:
- تطلب اسم مستخدم وكلمة مرور.
- تصادق باستخدام `MyLoginModule`.
- تطبع `Subject` و `Principals` الخاصة به إذا نجحت العملية.

---

### **ملاحظات إضافية**
- **الاستخدام في العالم الحقيقي**: استبدل بيانات الاعتماد الثابتة في `MyLoginModule` بفحوصات مقابل قاعدة بيانات، أو LDAP، أو خدمة أخرى. توفر جافا وحدات قياسية مثل `Krb5LoginModule` (Kerberos) أو `JndiLoginModule` (LDAP)، لكنها قد تتطلب إعدادًا إضافيًا.
- **وحدات تسجيل دخول متعددة**: يمكن للتكوين تحديد وحدات متعددة مع أعلام (`required`، `sufficient`، إلخ) لإنشاء عمليات مصادقة معقدة.
- **الأمان**: استخدم ممارسات آمنة، مثل تجنب `String` لكلمات المرور (استخدم `char[]`) والتكامل مع أطر الأمان الحالية.

يغطي هذا الدليل أساسيات استخدام `javax.security.auth` للمصادقة والتفويض في جافا!