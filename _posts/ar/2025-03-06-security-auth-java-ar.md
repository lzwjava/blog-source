---
audio: false
generated: true
lang: ar
layout: post
title: التحقق من الهوية والتسجيل في جاڤا
translated: true
---

لاستخدام حزمة `javax.security.auth` في جاڤا، عليك أن تفهم أنها جزء من إطار عمل خدمة التحقق من الهوية والتأهيل (JAAS). توفر هذه الحزمة فئات وواجهات للتحقق من هوية المستخدمين (التحقق من من هم) وتأهيلهم (تحديد ما يمكنهم فعله). أدناه دليل خطوة بخطوة لاستخدام `javax.security.auth` في سيناريو التحقق من الهوية الأساسي مثل التحقق من هوية المستخدم باستخدام اسم المستخدم وكلمة المرور.

---

### **نظرة عامة على المفاهيم الرئيسية**
قبل الغوص في الخطوات، إليك شرح موجز للمكونات الأساسية في `javax.security.auth`:

- **الموضوع (Subject)**: يمثل كيانًا (مثل المستخدم أو الخدمة) يتم التحقق من هويته. يمكن أن يكون له هويات متعددة (Principals) ووسائل التحقق (مثل كلمات المرور أو الشهادات).
- **المبادئ (Principal)**: هوية أو دور مرتبط بموضوع، مثل اسم المستخدم أو عضوية مجموعة.
- **وسائل التحقق (Credential)**: معلومات تستخدم للتحقق من هوية الموضوع، مثل كلمة المرور أو مفتاح تشفير.
- **وحدة تسجيل الدخول (LoginModule)**: مكون قابل للتبديل يقوم بتطبيق منطق التحقق من الهوية (مثل التحقق من اسم المستخدم وكلمة المرور في قاعدة البيانات).
- **سياق تسجيل الدخول (LoginContext)**: الفئة المركزية التي تنسق عملية التحقق من الهوية باستخدام وحدة تسجيل الدخول أو أكثر.
- **معامل التفاعل (CallbackHandler)**: واجهة للتفاعل مع المستخدم، مثل طلب اسم المستخدم وكلمة المرور.

مع هذه المفاهيم في ذهنك، دعونا نستكشف كيفية استخدام الحزمة.

---

### **خطوات لاستخدام `javax.security.auth`**

#### **1. إعداد تكوين JAAS**
تتم عملية التحقق من الهوية على أساس تكوين يحدد أي وحدة تسجيل الدخول (LoginModule) يجب استخدامها. يمكن تعريف هذا في ملف تكوين أو برمجيًا.

على سبيل المثال، قم بإنشاء ملف باسم `jaas.config` مع المحتوى التالي:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: اسم التطبيق أو السياق الذي ستشير إليه في كودك.
- **`com.example.MyLoginModule`**: الاسم الكامل لمодуلك الخاص `LoginModule` (ستقوم بإدخاله لاحقًا).
- **`required`**: علم يشير إلى أن هذا المودول يجب أن ينجح للتحقق من الهوية. تشمل الأعلام الأخرى `requisite`، `sufficient`، و `optional`، والتي تسمح بتطبيق منطق أكثر تعقيدًا مع وحدات متعددة.

قم بتعيين خاصية النظام لإشارة إلى هذا الملف:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

بدلاً من ذلك، يمكنك تعيين التكوين برمجيًا، ولكن الملف أسهل في معظم الحالات.

#### **2. تنفيذ معامل التفاعل (CallbackHandler)**
يجمع `CallbackHandler` المدخلات من المستخدم، مثل اسم المستخدم وكلمة المرور. إليك مثال بسيط باستخدام الواجهة:

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

- **NameCallback**: يطلب ويثبت اسم المستخدم.
- **PasswordCallback**: يطلب ويثبت كلمة المرور (مخزنة ك `char[]` لأغراض الأمان).

#### **3. تنفيذ وحدة تسجيل الدخول (LoginModule)**
تحدد وحدة تسجيل الدخول منطق التحقق من الهوية. إليك مثال أساسي يحدد التحقق من اسم المستخدم وكلمة المرور المحددين (في الممارسة العملية، ستستخدم قاعدة بيانات أو خدمة خارجية):

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

    // Initialize the module
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // Perform authentication
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

            // Hardcoded check (replace with real logic in practice)
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

    // Commit the authentication (add Principals to the Subject)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // Abort the authentication process
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Logout the Subject
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// Simple Principal implementation
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

- **login()**: يستخدم `CallbackHandler` للحصول على الوسائل التحقق من الهوية ويحققها.
- **commit()**: إذا نجح التحقق من الهوية، يضيف `Principal` إلى `Subject`.
- **abort()** و **logout()**: يتعاملان مع التنظيف أو الإلغاء.

#### **4. التحقق من الهوية باستخدام LoginContext**
الآن، استخدم `LoginContext` لإجراء التحقق من الهوية في تطبيقك الرئيسي:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // Ensure the JAAS configuration is set
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // Create LoginContext with the configuration name and CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // Perform authentication
            lc.login();

            // Get the authenticated Subject
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // Print the Subject's Principals
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // Logout when done
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: يربط بـ `"MyApp"` التكوين ويستخدم `MyCallbackHandler`.
- **`lc.login()`**: يثير عملية التحقق من الهوية.
- **`lc.getSubject()`**: يثبت الموضوع المحقق من هويته.

#### **5. تنفيذ الإجراءات المصرح بها (اختياري)**
بعد التحقق من الهوية، يمكنك استخدام الموضوع لتنفيذ الكود مع امتيازات باستخدام `Subject.doAs()`:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // Perform privileged actions here
        return null;
    }
});
```

هذا مفيد للتأهيل، حيث يتم تقيد الإجراءات بناءً على `Principals` للموضوع.

---

### **جمع كل شيء معًا**
1. **التكوين**: قم بتعريف `jaas.config` مع وحدة تسجيل الدخول الخاصة بك.
2. **معامل التفاعل (CallbackHandler)**: قم بإدخال `MyCallbackHandler` لجمع المدخلات من المستخدم.
3. **وحدة تسجيل الدخول (LoginModule)**: قم بإدخال `MyLoginModule` مع منطق التحقق من هوية المستخدم.
4. **الكود الرئيسي**: استخدم `LoginContext` للتحقق من الهوية واسترجاع موضوع.
5. **التأهيل**: استخدم `Subject.doAs()` للعمليات المصرح بها إذا لزم الأمر.

عندما تنفذ الفئة الرئيسية، ستقوم:
- طلب اسم المستخدم وكلمة المرور.
- التحقق من الهوية باستخدام `MyLoginModule`.
- طباعة الموضوع و `Principals` إذا كان النجاح.

---

### **ملاحظات إضافية**
- **الاستخدام في العالم الحقيقي**: استبدل الوسائل التحقق من الهوية المحددين في `MyLoginModule` بالتحقق من قاعدة بيانات، LDAP، أو خدمة خارجية. يوفر جاڤا وحدات قياسية مثل `Krb5LoginModule` (Kerberos) أو `JndiLoginModule` (LDAP)، ولكن قد تتطلب إعدادات إضافية.
- **وحدات تسجيل الدخول متعددة**: يمكن أن يحدد التكوين وحدات متعددة مع أعلام (`required`، `sufficient`، إلخ.) لإنشاء تدفقات التحقق من الهوية المعقدة.
- **الأمن**: استخدم الممارسات الآمنة، مثل تجنب استخدام `String` لكلمات المرور (استخدم `char[]`) ودمجها مع إطار عمل أمني موجود.

يغطي هذا الدليل أساسيات استخدام `javax.security.auth` للتحقق من الهوية والتأهيل في جاڤا!