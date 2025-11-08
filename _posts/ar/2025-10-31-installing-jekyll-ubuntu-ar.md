---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تثبيت جيكل على أوبونتو
translated: true
type: note
---

### إعداد وتشغيل Jekyll على أوبونتو

بناءً على خطأك ("Command 'bundle' not found") والأوامر التي تحاول تشغيلها، يبدو أنك بحاجة إلى تثبيت Ruby وBundler وJekyll بشكل صحيح أولاً. أوبونتو لا يأتي مع هذه الأدوات بشكل افتراضي، لكن العملية مباشرة باستخدام الدليل الرسمي لـ Jekyll. سأرشدك خلال عملية الإعداد الكاملة خطوة بخطوة، ثم كيفية تشغيل أوامرك المحددة.

#### الخطوة 1: تثبيت تبعيات النظام
افتح طرفيتك وقم بتشغيل هذا الأمر لتثبيت Ruby وأدوات البناء (هذا يتضمن Ruby 3.x عبر `ruby-full`):

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

- هذا يُجهز Ruby (تحقق باستخدام `ruby -v`—يجب أن تظهر نسخة مثل 3.0+).
- إذا كنت تستخدم إصدارًا حديثًا من أوبونتو (مثل 22.04+)، فهذا يعمل مباشرة. تجنب استخدام Snap لـ Ruby إذا أمكن، لأنه قد يسبب مشاكل في المسارات.

#### الخطوة 2: إعداد دليل Gems للمستخدم (موصى به لتجنب Sudo)
لتثبيت gems دون صلاحيات root (يمنع أخطاء الصلاحيات لاحقًا):

```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- تحقق: شغل `gem env`—يجب أن يظهر `GEM_HOME` الخاص بك كـ `~/gems`.

#### الخطوة 3: تثبيت Jekyll وBundler
الآن قم بتثبيت الأدوات:

```bash
gem install jekyll bundler
```

- هذا يضيف أوامر `gem`، `jekyll`، و `bundle` إلى مسار التنفيذ PATH الخاص بك.
- إذا حصلت على أخطاء صلاحيات، راجع الخطوة 2 مرة أخرى أو استخدم `sudo` مؤقتًا (لكن تجنبه على المدى الطويل).

#### الخطوة 4: إنشاء وتشغيل مدونتك
الآن يمكنك تشغيل الأوامر من مقتطفك. سأشرح كل واحد:

1. **إنشاء موقع Jekyll جديد**:
   ```bash
   jekyll new myblog
   ```
   - هذا يُنشئ موقعًا أساسيًا في مجلد `myblog`.

2. **الدخول إلى المجلد**:
   ```bash
   cd myblog
   ```

3. **تثبيت التبعيات** (هنا فشل أمرك الأصلي `bundle install`—الآن يجب أن يعمل):
   ```bash
   bundle install
   ```
   - يسحب gems مثل إضافات Jekyll.

4. **تشغيل الموقع** (يبدأ خادمًا محليًا على http://127.0.0.1:4000):
   ```bash
   bundle exec jekyll serve
   ```
   - افتح متصفحك على هذا الرابط لرؤية موقعك.

5. **التشغيل مع إعادة بناء تدريجية** (أسرع للتطوير، يعيد بناء الملفات المتغيرة فقط):
   ```bash
   bundle exec jekyll serve --incremental
   ```

6. **التشغيل متضمنًا المسودات** (يعرض المنشورات غير المنشورة):
   ```bash
   bundle exec jekyll serve --draft
   ```

7. **إذا حصلت على خطأ "webrick"** (شائع على Ruby 3+، لأنه غير مضمن افتراضيًا):
   ```bash
   bundle add webrick
   ```
   - ثم أعد تشغيل أمر serve: `bundle exec jekyll serve`.
   - بدلاً من ذلك، أضف `gem "webrick"` إلى ملف `Gemfile` الخاص بك وشغل `bundle install`.

8. **تشغيل سريع بدون Bundler** (إذا تخطيت `bundle exec`):
   ```bash
   jekyll serve
   ```
   - لكن استخدم `bundle exec` للاتساق في المشاريع.

#### استكشاف الأخطاء وإصلاحها
- **لا يزال "bundle not found"?** تأكد من أن الخطوة 2 قامت بتحميل `~/.bashrc` بشكل صحيح (`source ~/.bashrc`)، ثم أعد تشغيل طرفيتك أو شغل `hash -r`. تحقق باستخدام `which bundle`.
- **مشاكل صلاحيات مع gems?** التزم بإعداد دليل المستخدم في الخطوة 2.
- **إصدار Ruby قديم جدًا?** إذا كان `ruby -v` أقل من 3.0، ففكر في استخدام rbenv لإصدار أحدث (ثبته via `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash`، ثم `rbenv install 3.2.0`).
- **جدار حماية يمنع المنفذ 4000?** أوبونتو عادة لا يمنعه، لكن اختبر باستخدام `curl http://127.0.0.1:4000`.
- مشروعك موجود في `~/projects/blog-source`—شغل هذه الأوامر من هناك أو عدّل المسارات.

بمجرد التشغيل، قم بتعديل الملفات في `_posts/` أو `_config.yml` واحفظ — Jekyll يعيد البناء تلقائيًا. للإنتاج، ابنِ باستخدام `jekyll build` ونشّر على GitHub Pages أو Netlify.

[Jekyll Ubuntu Installation Guide](https://jekyllrb.com/docs/installation/ubuntu/)