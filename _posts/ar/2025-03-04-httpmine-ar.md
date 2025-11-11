---
audio: false
generated: true
lang: ar
layout: post
title: استخدام إتش تي تي بي ماين
translated: true
type: note
---

أفترض أنك قصدت "httpmime.jar" وليس "httpmine.jar"، حيث أن "httpmime" هي مكتبة معروفة من Apache HttpComponents تُستخدم لمعالجة كيانات MIME متعددة الأجزاء في طلبات HTTP (مثل تحميل الملفات). إذا كنت مخطئًا في هذا، يرجى التوضيح! إليك كيفية استخدام `httpmime.jar` في مشروع جافا:

---

### ما هو `httpmime.jar`؟
`httpmime.jar` هو جزء من مشروع Apache HttpComponents. فهو يمتد وظائف `httpclient.jar` من خلال توفير الدعم لطلبات multipart/form-data، والتي تُستخدم عادة لتحميل الملفات أو إرسال بيانات معقدة عبر HTTP.

لاستخدامه، ستحتاج أيضًا إلى تبعياته، مثل `httpclient.jar` و `httpcore.jar`، حيث أن `httpmime` يُبنى على هذه المكتبات.

---

### خطوات استخدام `httpmime.jar` في مشروع جافا الخاص بك

#### 1. **تحميل ملف JAR**
- قم بزيارة [صفحة تحميل Apache HttpComponents](https://hc.apache.org/downloads.cgi) أو مستودع Maven لـ `httpmime` (مثال: [الإصدار 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)).
- قم بتحميل ملف `httpmime-<version>.jar` (مثال: `httpmime-4.5.14.jar`).
- ستحتاج أيضًا إلى:
  - `httpclient-<version>.jar` (مثال: `httpclient-4.5.14.jar`)
  - `httpcore-<version>.jar` (مثال: `httpcore-4.4.16.jar`)
- تأكد من توافق الإصدارات (تحقق من [تبعيات المشروع](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)).

بدلاً من ذلك، إذا كنت تستخدم Maven أو Gradle، فتخطّ التحميل اليدوي وأضفه عبر أداة البناء الخاصة بك (انظر الخطوة 2).

#### 2. **إضافة ملف JAR إلى مشروعك**
- **الطريقة اليدوية (بدون أدوات بناء):**
  - ضع ملفات `httpmime.jar`، `httpclient.jar`، و `httpcore.jar` التي تم تحميلها في مجلد (مثال: `lib/` في دليل مشروعك).
  - إذا كنت تستخدم بيئة تطوير مثل Eclipse أو IntelliJ:
    - **Eclipse**: انقر بزر الماوس الأيمن على مشروعك > Properties > Java Build Path > Libraries > Add External JARs > اختر ملفات JAR > Apply.
    - **IntelliJ**: File > Project Structure > Modules > Dependencies > "+" > JARs or directories > اختر ملفات JAR > OK.
  - إذا كنت تشغّل من سطر الأوامر، فقم بتضمين ملفات JAR في classpath الخاص بك:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **باستخدام Maven (مُوصى به):**
  أضف هذا إلى ملف `pom.xml` الخاص بك:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- استخدم أحدث إصدار -->
  </dependency>
  ```
  سيقوم Maven تلقائيًا بسحب `httpclient` و `httpcore` كتبعيات متعدية.

- **باستخدام Gradle:**
  أضف هذا إلى ملف `build.gradle` الخاص بك:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **اكتب كودًا لاستخدام `httpmime`**
إليك مثالاً على استخدام `httpmime` لتحميل ملف عبر طلب HTTP POST متعدد الأجزاء:

```java
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.HttpResponse;
import java.io.File;

public class FileUploadExample {
    public static void main(String[] args) throws Exception {
        // إنشاء عميل HTTP
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // تعريف عنوان URL لإرسال الطلب إليه
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // بناء كيان multipart
        File file = new File("path/to/your/file.txt"); // استبدل بمسار ملفك
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // إضافة الملف
        builder.addTextBody("description", "This is a test file"); // إضافة حقل نصي (اختياري)

        // تعيين الكيان لطلب POST
        httpPost.setEntity(builder.build());

        // تنفيذ الطلب
        HttpResponse response = httpClient.execute(httpPost);

        // طباعة حالة الاستجابة
        System.out.println("Response Code: " + response.getStatusLine().getStatusCode());

        // التنظيف
        httpClient.close();
    }
}
```

#### 4. **الفئات الرئيسية والاستخدام**
- **`MultipartEntityBuilder`**: يُستخدم لبناء كيان multipart. يمكنك إضافة ملفات (`addPart`)، أو نص (`addTextBody`)، أو بيانات ثنائية (`addBinaryBody`).
- **`FileBody`**: يمثل ملفًا ليتم تحميله.
- **`CloseableHttpClient`**: عميل HTTP من `httpclient.jar` لتنفيذ الطلب.

#### 5. **تشغيل برنامجك**
- إذا كنت تستخدم بيئة تطوير، فقط شغّل البرنامج.
- إذا كنت تستخدم سطر الأوامر، فقم بالتجميع والتشغيل مع classpath كما هو موضح أعلاه.

#### 6. **استكشاف الأخطاء وإصلاحها**
- **ClassNotFoundException**: تأكد من أن جميع ملفات JAR المطلوبة (`httpmime`, `httpclient`, `httpcore`) موجودة في classpath الخاص بك.
- **عدم تطابق الإصدارات**: استخدم إصدارات متوافقة من ملفات JAR (مثال: `httpmime-4.5.14` مع `httpclient-4.5.14` و `httpcore-4.4.16`).
- **مشاريع Android**: نظام Android لديه حزمة `org.apache.http` الخاصة به، والتي قد تتعارض. إما استبعد الإصدار المدمج أو استخدم ملف JAR معاد تعبئته (مثال: عبر JarJar).

---

### مثال على حالة الاستخدام
إذا كنت تقوم بتحميل ملف إلى خادم (مثل REST API)، فإن `httpmime` يبسط عملية إنشاء طلب `multipart/form-data`، وهو المعيار المعتاد لتحميل الملفات.

دعني أعلم إذا كنت بحاجة إلى توضيح أو مساعدة في سيناريو معين!