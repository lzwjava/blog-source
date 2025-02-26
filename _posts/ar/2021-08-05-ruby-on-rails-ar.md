---
audio: false
lang: ar
layout: post
title: استخدام Ruby on Rails
translated: true
---

خلال فترة عملي في ShowMeBug، ساهمت في مشروع تكامل WeChat للشركات. وهذا يتضمن تكامل ShowMeBug مع WeChat للشركات، مما يوفر وصولًا سلسًا إلى أدوات المقابلة الفنية داخل بيئة WeChat للشركات. استخدمت تقنيات مثل Ruby، Ruby on Rails، PostgreSQL، و WeChat SDK لإنشاء تجربة مستخدم سلسة للمقابلة والمتقدمين.

نشر هذا المقال بمساعدة الذكاء الاصطناعي في فبراير 2025.

---

Ruby on Rails (يُعرف أحيانًا بـ "Rails") هو إطار عمل تطوير ويب قوي مبني على لغة البرمجة Ruby. تم تصميمه لتجعل بناء تطبيقات الويب سريعًا وممتعًا من خلال التركيز على الاتفاقات بدلاً من التكوين و مبادئ DRY (لا تكرر نفسك). دعونا نمر عبر إعداده و إنشاء تطبيق بسيط.

#### الخطوة 1: تثبيت Ruby و Rails
أولًا، تحتاج إلى تثبيت Ruby، حيث أن Rails هو حزمة Ruby (مكتبة). معظم الأنظمة لا تأتي مع Ruby مسبقًا، لذلك إليك كيفية إعداده:

- **على macOS/Linux:**
  - استخدم مدير الإصدارات مثل `rbenv` أو `rvm` للحصول على مرونة. قم بتثبيته عبر Homebrew (`brew install rbenv`), ثم قم بتشغيل:
    ```bash
    rbenv install 3.2.2  # إصدار Ruby مستقر اعتبارًا من 2025
    rbenv global 3.2.2
    ```
  - تثبيت Rails:
    ```bash
    gem install rails
    ```

- **على Windows:**
  - استخدم RubyInstaller (تحميل من rubyinstaller.org). اختر إصدارًا مثل 3.2.2 مع DevKit.
  - بعد تثبيت Ruby، افتح نافذة الأوامر و قم بتشغيل:
    ```bash
    gem install rails
    ```

تأكيد التثبيت:
```bash
ruby -v  # يجب أن يظهر شيئًا مثل ruby 3.2.2
rails -v # يجب أن يظهر أحدث إصدار Rails، مثل 7.1.x
```

#### الخطوة 2: إنشاء مشروع Rails جديد
بعد تثبيت Rails، قم بإنشاء تطبيق جديد:
```bash
rails new myapp --database=sqlite3
cd myapp
```
هذا يخلق مجلدًا يسمى `myapp` مع بنية Rails كاملة، باستخدام SQLite كقاعدة بيانات افتراضية (ممتازة للتنمية).

#### الخطوة 3: تشغيل الخادم
قم بتشغيل الخادم المدمج في Rails:
```bash
rails server
```
افتح متصفحك إلى `http://localhost:3000`. ستشاهد صفحة ترحيب. تهانينا، تطبيق Rails يعمل!

#### الخطوة 4: بناء شيء بسيط
دعونا نخلق ميزة "Posts" أساسية لفهم نمط MVC (Model-View-Controller) في Rails.

- **إنشاء نموذج وController:**
  ```bash
  rails generate scaffold Post title:string body:text
  ```
  هذا يخلق نموذج `Post`، هجرة قاعدة البيانات، Controller، و مشاهد—جميعها مرتبطة معًا.

- **تشغيل الهجرة:**
  ```bash
  rails db:migrate
  ```
  هذا يحدد جدول قاعدة البيانات للمقالات.

- **التحقق من ذلك:**
  اعيد تشغيل الخادم (`rails server`) و زور `http://localhost:3000/posts`. ستشاهد واجهة CRUD لإنشاء، قراءة، تحديث، و حذف المقالات.

#### الخطوة 5: استكشاف المفاهيم الرئيسية
- **الطرق:** افتح `config/routes.rb`. ستشاهد `resources :posts`، الذي يولد تلقائيًا طرق RESTful مثل `/posts/new` أو `/posts/1/edit`.
- **Controllers:** انظر إلى `app/controllers/posts_controller.rb`. يسيطر على الطلبات والإجابات.
- **Views:** تحقق من `app/views/posts/`. هذه هي قوالب ERB (HTML مع Ruby مدمج).
- **Models:** انظر إلى `app/models/post.rb`. يربط بالقاعدة البيانات ويمكن أن يتضمن التحققات (مثل `validates :title, presence: true`).

#### الخطوة 6: تخصيص و نشر
- أضف بعض الأسلوب باستخدام CSS في `app/assets/stylesheets/`.
- للإنتاج، قم بتغيير قاعدة البيانات إلى PostgreSQL (`rails new myapp --database=postgresql`) ونشر على منصّة مثل Render أو Heroku. قم بتحديث `Gemfile` مع `gem "pg"` و قم بتشغيل `bundle install`.

#### نصائح محترفة
- استخدم `rails console` للتجربة مع نماذجك في الوقت الفعلي.
- قم بتشغيل `rails generate --help` لرؤية جميع اختصارات Rails.
- استغل الحجارة الكريمة مثل `devise` للتصديق أو `pundit` للصلاحيات—أضفهم إلى `Gemfile` و قم بتكوينهم حسب الحاجة.

هذا هو كل شيء! لديك تطبيق Rails أساسي يعمل. من هنا، استكشف الدلائل الرسمية لـ Rails (guides.rubyonrails.org) أو بناء شيء حقيقي لتثبيت مهاراتك. ما نوع المشروع الذي تفكر فيه؟