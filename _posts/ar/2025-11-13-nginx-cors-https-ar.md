---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة CORS و HTTPS في Nginx
translated: true
type: note
---

```nginx
# تعريف خريطة للتعامل مع النطاقات المسموح بها
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### ما الذي يفعله
- ينشئ متغير `$cors_origin` بناءً على قيمة رأس `Origin` الوارد (`$http_origin`).
- إذا كان الطلب قادمًا من `http://localhost:3000`، أو `https://example.com`، أو `https://www.example.com`، فإنه يعيد نفس النطاق بالضبط.
- بالنسبة لأي نطاق آخر (أو في حالة عدم وجود نطاق)، فإنه يستخدم القيمة الافتراضية `https://example.com`.
- يُستخدم هذا لاحقًا لتعيين رأس `Access-Control-Allow-Origin` بشكل ديناميكي، مما يُمكن CORS فقط للنطاقات الأمامية الموثوقة.

---

```nginx
# إعادة توجيه HTTP إلى HTTPS
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### ما الذي يفعله
- يستمع على المنفذ 80 (HTTP).
- يطابق الطلبات الموجهة إلى `example.com` أو `api.example.com`.
- يعيد توجيه جميع حركة المرور بشكل دائم (301) إلى نسخة HTTPS من نفس الرابط.
- يُلزم استخدام اتصالات آمنة؛ ولا يُسمح بالوصول عبر HTTP العادي.

---

```nginx
# تهيئة الموقع الرئيسي لـ example.com
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    root /home/project/project-web;
    index index.html index.htm index.php default.html default.htm default.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires 30d;
    }

    location ~ .*\.(js|css)?$ {
        expires 12h;
    }

    error_page 404 /index.html;
}
```

### ما الذي يفعله
- **خادم HTTPS** لـ `example.com` على المنفذ 443 مع تمكين SSL.
- يستخدم شهادات **Let’s Encrypt** (قابلة للتجديد تلقائيًا ومجانية).
- يفرض إصدارات TLS حديثة (`TLSv1.2`، `TLSv1.3`) وخوارزميات تشفير قوية للأمان.
- يخدم الملفات الثابتة من `/home/project/project-web`.
- يحاول خدمة الملف المطلوب → المجلد → 404.
- يضبط **رؤوس التخزين المؤقت**:
  - الصور: تخزين مؤقت لمدة 30 يومًا.
  - JS/CSS: تخزين مؤقت لمدة 12 ساعة.
- يتم توجيه جميع أخطاء 404 إلى `index.html` → يُمكن ذلك من **توجيه تطبيقات الصفحة الواحدة (SPA)** (مثل React, Vue).

---

```nginx
# تهيئة API لـ api.example.com
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # مسح أي رؤوس Access-Control موجودة مسبقًا
        more_clear_headers 'Access-Control-Allow-Origin';

        # التعامل مع طلبات CORS المبدئية (Preflight)
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' $cors_origin;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
            add_header 'Access-Control-Allow-Headers' 'Origin, Content-Type, Accept, Authorization, X-Client-Info, X-Trace-Id, X-Requested-With, X-HTTP-Method-Override, DNT, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range';
            add_header 'Access-Control-Max-Age' 3600;
            return 204;
        }

        add_header 'Access-Control-Allow-Origin' $cors_origin always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
        add_header 'Access-Control-Allow-Headers' '...' always;

        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }
}
```

### ما الذي يفعله
- **وكيل عكسي (Reverse Proxy) لـ HTTPS** لـ `api.example.com`.
- يستخدم **شهادة Let’s Encrypt منفصلة** (على الأرجح بسبب وجود نطاقات متعددة/SANs).
- يتم تمرير كل حركة المرور إلى **خلفية محلية** تعمل على `localhost:5000` (مثل Flask, Node.js، إلخ).

#### التعامل مع CORS
- يستخدم خريطة `$cors_origin` **للسماح ديناميكيًا** فقط للنطاقات المعتمدة.
- **يمسح أي رأس** `Access-Control-Allow-Origin` موجود مسبقًا لمنع التعارضات.
- يتعامل مع **الطلبات المبدئية (Preflight) OPTIONS**:
  - يُرجع `204 No Content` فورًا.
  - يسمح بالطرق والرؤوس الشائعة.
  - يخزن نتائج الطلب المبدئي لمدة ساعة واحدة (`Max-Age: 3600`).
- بالنسبة للطلبات الفعلية، يضيف رؤوس CORS مع `always` بحيث تظهر حتى في استجابات الخطأ.

#### إعدادات الوكيل (Proxy)
- يُمرر عنوان IP الحقيقي للعميل ومعلومات البروتوكول إلى الخلفية.
- مهلات طويلة (10 دقائق) → مناسبة للعمليات طويلة المدى في API (مثل رفع الملفات، حسابات معقدة).

---

### ملخص البنية

| المكون               | الغرض |
|---------------------|--------|
| `example.com`       | يخدم تطبيق SPA الثابت (React/Vue/etc.) |
| `api.example.com`   | بوابة API آمنة → الخلفية على المنفذ 5000 |
| HTTP → HTTPS        | جميع حركة المرور مفروضة عبر TLS |
| CORS                | مقيدة على `example.com`، `www`، و `localhost:3000` |
| التخزين المؤقت      | مُحسّن للأداء |
| SSL                 | Let’s Encrypt، خوارزميات تشفير حديثة |

### ملاحظات الأمان
- تهيئة TLS قوية (من المحتمل الحصول على تقييم A+ من SSL Labs).
- CORS **ليست wildcard** → تمنع المواقع غير المصرح لها من استدعاء API.
- يتم التعامل مع الطلبات المبدئية بكفاءة.
- يتم تمرير عنوان IP الحقيقي → مفيد لتسجيل الأحداث/الحد من المعدل في الخلفية.

دعني أعلم إذا كنت تريد رسمًا بيانيًا أو نسخة معدة للتشغيل في Docker!