---
audio: false
generated: true
lang: ar
layout: post
title: استخدام httpmine
translated: true
---

أعتقد أنك قصدت "httpmime.jar" بدلاً من "httpmine.jar"، لأن "httpmime" هي مكتبة معروفة من Apache HttpComponents المستخدمة لمعالجة كيانات MIME متعددة الأجزاء في طلبات HTTP (مثل تحميل الملفات). إذا كنت مخطئًا، يرجى توضيح! إليك كيفية استخدام `httpmime.jar` في مشروع Java:

---

### ما هو `httpmime.jar`؟
`httpmime.jar` جزء من مشروع Apache HttpComponents. يوسع `httpclient.jar` من خلال توفير دعم للطلبات `multipart/form-data`، والتي تستخدم بشكل شائع لتحميل الملفات أو إرسال بيانات معقدة عبر HTTP.

لاستخدامه، ستحتاج أيضًا إلى اعتماداته مثل `httpclient.jar` و `httpcore.jar`، لأن `httpmime` يبني على هذه المكتبات.

---

### خطوات لاستخدام `httpmime.jar` في مشروع Java

#### 1. **تحميل ملف JAR**
- زور صفحة [تحميلات Apache HttpComponents](https://hc.apache.org/downloads.cgi) أو مخزن Maven لـ `httpmime` (على سبيل المثال، [النسخة 4.5.14](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpmime)).
- تحميل ملف `httpmime-<version>.jar` (على سبيل المثال، `httpmime-4.5.14.jar`).
- ستحتاج أيضًا إلى:
  - `httpclient-<version>.jar` (على سبيل المثال، `httpclient-4.5.14.jar`)
  - `httpcore-<version>.jar` (على سبيل المثال، `httpcore-4.4.16.jar`)
- تأكد من أن الأصدارات متوافقة (تحقق من [اعتمادات المشروع](https://hc.apache.org/httpcomponents-client-4.5.x/httpmime/dependencies.html)).

إذا كنت تستخدم Maven أو Gradle، قف عن التحميل اليدوي وأضفها عبر أداة البناء (انظر الخطوة 2).

#### 2. **إضافة JAR إلى مشروعك**
- **طريقة يدوية (بدون أدوات بناء):**
  - ضع ملفات `httpmime.jar` و `httpclient.jar` و `httpcore.jar` المحمولة في مجلد (على سبيل المثال، `lib/` في مجلد المشروع).
  - إذا كنت تستخدم IDE مثل Eclipse أو IntelliJ:
    - **Eclipse**: انقر بالزر الأيمن على مشروعك > خصائص > مسار بناء Java > مكتبات > إضافة JARات خارجية > اختر JARs > تطبيق.
    - **IntelliJ**: ملف > بنية المشروع > وحدات > اعتمادات > "+" > JARs أو مجلدات > اختر JARs > موافق.
  - إذا كنت تعمل من سطر الأوامر، أضف JARs إلى مسارك:
    ```bash
    javac -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar" YourClass.java
    java -cp "lib/httpmime-4.5.14.jar;lib/httpclient-4.5.14.jar;lib/httpcore-4.4.16.jar;." YourClass
    ```

- **استخدام Maven (موصى به):**
  أضف هذا إلى `pom.xml`:
  ```xml
  <dependency>
      <groupId>org.apache.httpcomponents</groupId>
      <artifactId>httpmime</artifactId>
      <version>4.5.14</version> <!-- استخدم أحدث الإصدار -->
  </dependency>
  ```
  سيعتمد Maven تلقائيًا على `httpclient` و `httpcore` كاعتمادات انتقالية.

- **استخدام Gradle:**
  أضف هذا إلى `build.gradle`:
  ```gradle
  implementation 'org.apache.httpcomponents:httpmime:4.5.14'
  ```

#### 3. **كتابة الكود لاستخدام `httpmime`**
هنا مثال لاستخدام `httpmime` لتحميل ملف عبر طلب HTTP POST متعدد الأجزاء:

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

        // تعريف URL لإرسال الطلب إليه
        String url = "http://example.com/upload";
        HttpPost httpPost = new HttpPost(url);

        // بناء الكيان متعدد الأجزاء
        File file = new File("path/to/your/file.txt"); // استبدل بمسار ملفك
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        builder.addPart("file", new FileBody(file)); // أضف الملف
        builder.addTextBody("description", "This is a test file"); // أضف حقل نص (اختياري)

        // تعيين الكيان إلى طلب POST
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

#### 4. **الصفوف الرئيسية واستخدامها**
- **`MultipartEntityBuilder`**: يستخدم لبناء الكيان متعدد الأجزاء. يمكنك إضافة ملفات (`addPart`), نص (`addTextBody`), أو بيانات ثنائية (`addBinaryBody`).
- **`FileBody`**: يمثل ملفًا يتم تحميله.
- **`CloseableHttpClient`**: العميل HTTP من `httpclient.jar` لإجراء الطلب.

#### 5. **تشغيل برنامجك**
- إذا كنت تستخدم IDE، فقط قم بتشغيل البرنامج.
- إذا كنت تستخدم سطر الأوامر، قم بتجميعه وتشغيله مع مسار كما هو موضح أعلاه.

#### 6. **إصلاح الأخطاء**
- **ClassNotFoundException**: تأكد من أن جميع JARs المطلوبة (`httpmime`, `httpclient`, `httpcore`) في مسارك.
- **اختلاف الإصدار**: استخدم إصدارات متوافقة من JARs (على سبيل المثال، `httpmime-4.5.14` مع `httpclient-4.5.14` و `httpcore-4.4.16`).
- **مشاريع Android**: Android لديها حزمة `org.apache.http` الخاصة بها، والتي قد تتعارض. إما استبعاد الإصدار المدمج أو استخدام JAR إعادة التعبئة (على سبيل المثال، عبر JarJar).

---

### حالة استخدام مثالية
إذا كنت تحميل ملف إلى خادم (مثل API REST)، فإن `httpmime` يسهل إنشاء الطلب `multipart/form-data`، وهو المعيار لتحميل الملفات.

أعلمني إذا كنت تحتاج إلى توضيح أو مساعدة في حالة معينة!