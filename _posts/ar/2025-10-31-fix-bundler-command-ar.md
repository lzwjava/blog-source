---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إصلاح أمر Bundler غير موجود
translated: true
type: note
---

### فهم المشكلة
نجح أمر `gem install jekyll bundler` الخاص بك (قام بتثبيت 30 جوهرة، بما في ذلك Bundler 2.7.2)، ولكن أمر `bundle` غير موجود. هذه مشكلة شائعة في المتغير البيئي PATH على أنظمة Ubuntu/Debian بعد تثبيت `sudo gem install` على مستوى النظام. تقوم ثنائيات Gems بالتثبيت في `/usr/local/bin` (أو ما شابه)، ولكن قد لا يتضمن مسار shell الخاص بك `$PATH` هذا الدليل، أو أن التغيير لم ينتشر بعد (مثل الحاجة إلى إعادة تحميل ملف التعريف الخاص بك).

اقتراح النظام `apt install ruby-bundler` سيقوم بتثبيت إصدار أقدم (2.4.20) عبر apt، مما قد يتعارض مع Bundler 2.7.2 المثبت عبر gem — تجنب ذلك في الوقت الحالي. الأمر نفسه بالنسبة لـ snap؛ فقد يعزل Ruby بطريقة تعطل مسارات gem.

### الإصلاح السريع: التحقق من Bundler المثبت واستخدامه
1. **التحقق من مكان تثبيت `bundle`**:
   ```
   gem environment
   ```
   - ابحث عن "EXECUTABLE DIRECTORY" (على الأرجح `/usr/local/bin`). لاحظ هذا المسار.

2. **تحديد موقع `bundle` واختباره مباشرة**:
   ```
   which bundle  # إذا لم يظهر شيء، جرب: find /usr/local -name bundle 2>/dev/null
   /usr/local/bin/bundle --version  # يجب أن يظهر الإخراج "Bundler version 2.7.2"
   ```
   - إذا عمل، ممتاز! استخدم المسار الكامل مؤقتًا: `/usr/local/bin/bundle install`

3. **تشغيل إعداد Jekyll الخاص بك باستخدام المسار الكامل**:
   - في `~/projects/blog-source` (بافتراض أنه يحتوي على `Gemfile`):
     ```
     /usr/local/bin/bundle install
     /usr/local/bin/bundle exec jekyll serve
     ```
   - يجب أن يقوم هذا بتثبيت تبعيات Jekyll ويبدأ الخادم (عادةً على http://127.0.0.1:4000).

### الإصلاح الدائم: تحديث PATH الخاص بك
إذا لم يكن `/usr/local/bin` موجودًا في `$PATH` الخاص بك، أضفه:
1. قم بتحرير `~/.bashrc` (أو `~/.profile` لأصداف تسجيل الدخول):
   ```
   nano ~/.bashrc
   ```
   أضف هذا السطر في النهاية:
   ```
   export PATH="/usr/local/bin:$PATH"
   ```

2. أعد تحميل الصدفة الخاصة بك:
   ```
   source ~/.bashrc
   ```

3. تحقق:
   ```
   echo $PATH  # يجب أن يتضمن الآن /usr/local/bin
   bundle --version  # يجب أن يعمل بدون المسار الكامل
   ```

الآن أعد المحاولة:
```
bundle install
bundle exec jekyll serve
```

### إذا لم ينجح ذلك
- **مشاكل في الأذونات؟** (نادرة، ولكن sudo قد يسببها.) أعد التثبيت بدون sudo (تثبيت محلي للمستخدم):
  ```
  gem install --user-install bundler jekyll
  ```
  ثم أضف `export PATH="$HOME/.local/share/gem/ruby/*/bin:$PATH"` إلى `~/.bashrc` (اضبط المسار من `gem environment`).

- **عدم تطابق إصدار Ruby؟** تحقق باستخدام `ruby --version`. إذا كان نظام Ruby (مثل 2.7.x)، ففكر في استخدام مديري إصدارات Ruby مثل `rbenv` (قم بتثبيته عبر `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`، ثم اتبع الإعداد). هذا يتجنب التعارضات مع النظام على المدى الطويل.

- **هل الوكيل (Proxy) لا يزال فعالاً؟** إذا كانت متغيرات البيئة الخاصة بك (`http_proxy`، إلخ) مضبوطة، فيجب أن يرثها Bundler — فقط تأكد من تصديرها قبل التشغيل.

يجب أن يعمل إعدادك بسلاسة بعد تعديل PATH. إذا واجهت أخطاء (مثل إخراج `gem environment`)، الصقها للحصول على مساعدة أكثر تحديدًا!