---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل تغيير منفذ إن جينكس على نظام ماك أو إس
translated: true
type: note
---

تريد أن يستمع Nginx على نظام macOS إلى **منفذ مختلف** عن الإفتراضي (80 لـ HTTP، 443 لـ HTTPS). إليك دليل واضح خطوة بخطوة:

---

### 1. ابحث عن ملف تهيئة Nginx الخاص بك

* إذا قمت بالتثبيت عبر **Homebrew**، فعادةً ما يكون ملف التهيئة الافتراضي هو:

  ```
  /usr/local/etc/nginx/nginx.conf
  ```

  أو، على أجهزة Apple Silicon:

  ```
  /opt/homebrew/etc/nginx/nginx.conf
  ```
* إذا قمت بالتثبيت يدويًا، فقد يكون الموقع هو `/usr/local/nginx/conf/nginx.conf`.

---

### 2. عدل توجيه `listen`

1. افتح ملف التهيئة في محرر نصوص:

   ```bash
   nano /opt/homebrew/etc/nginx/nginx.conf
   ```
2. ابحث عن كتلة `server`:

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           root   html;
           index  index.html index.htm;
       }
   }
   ```
3. غيّر `listen 80;` إلى المنفذ الذي تريده، على سبيل المثال، 8080:

   ```nginx
   listen 8080;
   ```

---

### 3. اختبر التهيئة

شغّل الأمر:

```bash
nginx -t
```

* إذا ظهرت الرسالة `syntax is ok` و `test is successful`، فهذا يعني أن التهيئة صالحة.
* إذا كانت هناك أخطاء، فتحقق من أرقام الأسطر التي تم الإبلاغ عنها.

---

### 4. أعِد تشغيل Nginx

* إذا كان مثبتًا عبر Homebrew:

```bash
brew services restart nginx
```

* أو يدويًا:

```bash
sudo nginx -s reload
```

---

### 5. الوصول عبر المنفذ الجديد

* في متصفحك أو باستخدام curl:

```
http://localhost:8080
```

---

**ملاحظات إضافية:**

* المنافذ **الأقل من 1024** تتطلب استخدام `sudo` على نظام macOS. لذا، استخدام منافذ مثل 80 سيتطلب صلاحيات root، بينما لا يتطلب ذلك منافذ مثل 8080 أو 3000.
* إذا كنت تريد تشغيل عدة خوادم Nginx في وقت واحد، **يجب أن يكون لكل منها منفذ فريد**.

---

يمكنني أيضًا إعطاؤك **خدعة سريعة لتشغيل Nginx مؤقتًا على أي منفذ دون تعديل ملف nginx.conf** باستخدام وسيط سطر الأوامر. إنها مفيدة للاختبار. هل تريد مني أن أعرضها؟