---
audio: false
generated: true
lang: ar
layout: post
title: 'تسريع عمليات بناء جيكيل: استكشاف نهجيات التعددية الخيطية'
translated: true
type: note
---

عملية البناء في Jekyll أحادية الخيط افتراضيًا، مما قد يكون بطيئًا للمواقع الكبيرة. بينما لا يوجد خيار تكوين مدمج في Jekyll لتمكين عمليات البناء متعددة الخيوط، يمكنك استكشاف بعض النهج لتحقيق التوازي. أدناه، أشرح الاحتمالات، التحديات، والخطوات العملية بناءً على المعلومات المتاحة والاعتبارات التقنية.

### لماذا عمليات بناء Jekyll أحادية الخيط
تقوم Jekyll بمعالجة الصفحات بشكل تسلسلي لضمان معالجة التبعيات (مثل `site.related_posts` أو قوالب Liquid) بشكل صحيح. بعض المكونات، مثل Liquid وبعض الإضافات، قد لا تكون آمنة للخيوط (thread-safe)، مما يعقد التعددية (). يعطي هذا التصميم الأولوية للصحة على السرعة، ولكن للمواقع الكبيرة، يمكن أن يؤدي هذا إلى أوقات بناء تصل إلى عدة دقائق (,).[](https://github.com/jekyll/jekyll/issues/9485)[](https://github.com/jekyll/jekyll/issues/1855)[](https://github.com/jekyll/jekyll/issues/4297)

### نهج لعمليات بناء Jekyll متعددة الخيوط
إليك الطرق المحتملة لإدخال التوازي إلى عمليات بناء Jekyll، خاصة في سياق سير عمل GitHub Actions مثل الذي قدمته:

#### 1. **استخدم إضافة مخصصة للتقديم متعدد الخيوط**
تم اقتراح إضافة proof-of-concept للتقديم متعدد الخيوط (). لقد قللت وقت البناء من 45 ثانية إلى 10 ثوان في حالة اختبار ولكن كانت بها مشاكل في أمان الخيوط، مما أدى إلى محتوى صفحة غير صحيح. كما تعارضت الإضافة مع إضافات مثل `jekyll-feed`، التي تعتمد على التقديم التسلسلي.[](https://github.com/jekyll/jekyll/issues/9485)

**خطوات لتجربة إضافة مخصصة:**
- **إنشاء إضافة**: نفذ إضافة Ruby تمتد من فئة `Site` في Jekلسل لتوازي تقديم الصفحات. على سبيل المثال، يمكنك تعديل طريقة `render_pages` لاستخدام فئة `Thread` في Ruby أو مجموعة خيوط (thread pool).([](https://github.com/jekyll/jekyll/issues/9485)
  ```ruby
  module Jekyll
    module UlyssesZhan::MultithreadRendering
      def render_pages(*args)
        @rendering_threads = []
        super # استدعاء الطريقة الأصلية
        @rendering_threads.each(&:join) # انتظر اكتمال الخيوط
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::UlyssesZhan::MultithreadRendering)
  ```
- **أضف إلى Gemfile**: ضع الإضافة في دليل `_plugins` الخاص بك وتأكد من تحميلها بواسطة Jekyll.
- **اختبر من أجل أمان الخيوط**: نظرًا لأن Liquid وبعض الإضافات (مثل `jekyll-feed`) قد يتعطلان، اختبر بدقة. قد تحتاج إلى تصحيح Liquid أو تجنب التعددية لبعض الميزات ().[](https://github.com/jekyll/jekyll/issues/9485)
- **دمج مع GitHub Actions**: حدّث سير العمل الخاص بك لتشمل الإضافة في مستودعك. تأكد من أن إجراء `jekyll-build-pages` يستخدم إعداد Jekyll المخصص الخاص بك:
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
    env:
      BUNDLE_GEMFILE: ./Gemfile # تأكد من استخدام Gemfile المخصص الخاص بك مع الإضافة
  ```

**التحديات**:
- مشاكل أمان الخيوط مع Liquid والإضافات مثل `jekyll-feed`.([](https://github.com/jekyll/jekyll/issues/9485)
- إمكانية تقديم صفحة بشكل غير صحيح (مثل ظهور محتوى صفحة في أخرى).
- يتطلب خبرة في Ruby لتصحيح الأخطاء والصيانة.

#### 2. **وازن عمليات البناء باستخدام تكوينات متعددة**
بدلاً من تعددية الخيوط في بناء واحد، يمكنك تقسيم موقعك إلى أجزاء أصغر (مثل حسب collection أو الدليل) وبنائها بشكل متوازٍ باستخدام عمليات Jekyll متعددة. يتجنب هذا النهج مشاكل أمان الخيوط ولكنه يتطلب إعدادًا أكثر.

**الخطوات**:
- **قسّم الموقع**: نظم موقعك إلى collections (مثل `posts`, `pages`, `docs`) أو أدلة وأنشئ ملفات `_config.yml` منفصلة لكل منها (,).([](https://amcrouch.medium.com/configuring-environments-when-building-sites-with-jekyll-dd6eb2603c39)[](https://coderwall.com/p/tfcj2g/using-different-build-configuration-in-jekyll-site)
  ```yaml
  # _config_posts.yml
  collections:
    posts:
      output: true
  destination: ./_site/posts

  # _config_pages.yml
  collections:
    pages:
      output: true
  destination: ./_site/pages
  ```
- **حدّث سير عمل GitHub Actions**: عدّل سير العمل الخاص بك لتشغيل عمليات بناء Jekyll متعددة بشكل متوازٍ، كل منها باستخدام ملف تكوين مختلف.
  ```yaml
  name: Build Jekyll Site
  on:
    push:
      branches: [main]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Setup Ruby
          uses: ruby/setup-ruby@v1
          with:
            ruby-version: '3.1'
            bundler-cache: true
        - name: Build Posts
          run: bundle exec jekyll build --config _config_posts.yml
        - name: Build Pages
          run: bundle exec jekyll build --config _config_pages.yml
        - name: Combine Outputs
          run: |
            mkdir -p ./_site
            cp -r ./_site/posts/* ./_site/
            cp -r ./_site/pages/* ./_site/
        - name: Deploy
          uses: actions/upload-artifact@v4
          with:
            name: site
            path: ./_site
  ```
- **ادمج المخرجات**: بعد عمليات البناء المتوازية، ادمج أدلة المخرجات في مجلد `_site` واحد للنشر.

**التحديات**:
- إدارة التبعيات المتبادلة بين collections (مثل `site.related_posts`).
- زيادة التعقيد في التكوين والنشر.
- قد لا يكون قابل للتطوير بشكل جيد للمواقع ذات المحتوى المترابط بشدة.

#### 3. **استخدم مجموعة خيوط (Thread Pool) للمواقع الكبيرة**
اقترح pull request لإضافة `amp-jekyll` استخدام مجموعة خيوط لمعالجة الصفحات، مع عدد قابل للتكوين من الخيوط لتجنب إرباك النظام (). يوازن هذا النهج بين الأداء واستخدام الموارد.[](https://github.com/juusaw/amp-jekyll/pull/26)

**الخطوات**:
- **نفّذ مجموعة خيوط**: عدّل أو أنشئ إضافة لاستخدام `Thread::Queue` في Ruby لإدارة عدد ثابت من خيوط العمل (مثل 4 أو 8، اعتمادًا على نظامك).
  ```ruby
  require 'thread'

  module Jekyll
    module ThreadPoolRendering
      def render_pages(*args)
        queue = Queue.new
        site.pages.each { |page| queue << page }
        threads = (1..4).map do # 4 خيوط
          Thread.new do
            until queue.empty?
              page = queue.pop(true) rescue nil
              page&.render_with_liquid(site)
            end
          end
        end
        threads.each(&:join)
        super
      end
    end
  end
  Jekyll::Site.prepend(Jekyll::ThreadPoolRendering)
  ```
- **أضف خيار تكوين**: اسمح للمستخدمين بتبديل التعددية أو تعيين عدد الخيوط في `_config.yml`:
  ```yaml
  multithreading:
    enabled: true
    thread_count: 4
  ```
- **دمج مع سير العمل**: تأكد من تضمين الإضافة في مستودعك وتحمل أثناء بناء GitHub Actions.

**التحديات**:
- مشاكل أمان الخيوط المشابهة للنهج الأول.
- حمل تبديل السياق (context-switching) للمواقع الكبيرة ذات المهام القصيرة العديدة ().[](https://github.com/juusaw/amp-jekyll/pull/26)
- يتطلب اختبارًا لضمان التوافق مع جميع الإضافات.

#### 4. **حسّن بدون تعددية الخيوط**
إذا ثبت أن تعددية الخيوط معقدة أو محفوفة بالمخاطر، يمكنك تحسين عملية البناء أحادية الخيط:
- **مكّن عمليات البناء التدريجي**: استخدم `jekyll build --incremental` لإعادة بناء الملفات المتغيرة فقط (,). أضف إلى سير العمل الخاص بك:[](https://github.com/jekyll/jekyll/blob/master/lib/jekyll/commands/build.rb)[](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  ```yaml
  - name: Build with Jekyll
    uses: actions/jekyll-build-pages@v1
    with:
      source: ./
      destination: ./_site
      incremental: true
  ```
- **قلّل استخدام الإضافات**: يمكن للإضافات المخصصة أن تبطئ عمليات البناء بشكل كبير (). راجع وأزل الإضافات غير الضرورية.[](https://github.com/jekyll/jekyll/issues/4297)
- **استخدم محولات أسرع**: انتقل من Kramdown إلى معالج markdown أسرع مثل CommonMark، أو اختبر Pandoc لحالات استخدام محددة ().[](https://github.com/jekyll/jekyll/issues/9485)
- **خبّء التبعيات**: تأكد من `bundler-cache: true` في سير عمل GitHub Actions الخاص بك لتجنب إعادة تثبيت gems.([](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

### التوصيات
- **ابدأ بعمليات البناء التدريجي**: هذه هي أبسط طريقة لتسريع عمليات البناء دون المخاطرة بمشاكل أمان الخيوط. أضف `--incremental` إلى سير العمل الخاص بك واختبر تأثيره.
- **جرب إضافة مجموعة خيوط**: إذا كانت لديك خبرة في Ruby، جرب تنفيذ إضافة مجموعة خيوط بعدد قابل للتكوين من الخيوط (الخيار 3). ابدأ بموقع صغير لاختبار أمان الخيوط.
- **تجنب التعددية الكاملة للخيوط الآن**: نظرًا لمخاوف أمان الخيوط مع Liquid والإضافات ()، قد تتطلب التعددية الكاملة للخيوط إعادة هيكلة كبيرة أو fork مخصص لـ Liquid، مما قد لا يكون عمليًا إلا إذا كنت تساهم في التطوير الأساسي لـ Jekyll.[](https://github.com/jekyll/jekyll/issues/9485)
- **راقب أوقات البناء**: استخدم سجلات GitHub Actions لقياس أوقات البناء وتحديد الاختناقات. على سبيل المثال، موقع يستغرق 6 دقائق للبناء () يشير إلى أن الإضافات أو معالجة الأصول الكبيرة قد تكون هي المشكلة.[](https://github.com/jekyll/jekyll/issues/1855)

### مثال GitHub Actions مع عمليات البناء التدريجي الممكنة
إليك نسخة محدثة من سير العمل الخاص بك مع تمكين عمليات البناء التدريجي:
```yaml
name: Build Jekyll Site
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'
          bundler-cache: true
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          incremental: true
      - name: Deploy
        uses: actions/upload-artifact@v4
        with:
          name: site
          path: ./_site
```

### محاذير
- **أمان الخيوط**: التعددية في Jekyll تجريبية وقد تكسر الإضافات أو تنتج مخرجات غير صحيحة (). اختبر بدقة على موقع صغير أولاً.[](https://github.com/jekyll/jekyll/issues/9485)
- **حدود GitHub Actions**: عمليات البناء المتوازية (الخيار 2) تزيد من استخدام الموارد، لذا تأكد من بقاء سير العمل ضمن حدود الطبقة المجانية في GitHub.
- **إمكانية Jekyll 5**: قد تعالج الإصدارات المستقبلية من Jekyll التعددية بشكل أصلي، كما تمت مناقشته (). في الوقت الحالي، هناك حاجة إلى حلول مخصصة.[](https://github.com/jekyll/jekyll/issues/9485)

إذا كنت بحاجة إلى مساعدة في تنفيذ نهج معين (مثل كتابة إضافة أو تقسيم عمليات البناء)، دعني أعلم، ويمكنني تقديم إرشادات أو كود أكثر تفصيلاً!