---
audio: false
generated: false
image: false
lang: ar
layout: post
title: تجديد منصة مراجعة الكود باستخدام Stylus
translated: true
---

عند بناء تطبيق ويب حديث، فإن التزيين هو أكثر من مجرد جعل الأشياء تبدو جيدة - إنه عن إنشاء تجربة مستخدم مفهومة، متفاعلة، ومتفاعلة. لقد استكشفت مؤخرًا ملفات التزيين المستندة إلى Stylus لمصنع مراجعة الكود الذي يعمل بواسطة Vue.js، وعمارة CSS له هي كنز من التقنيات التي يستحق فكها. دعونا نغوص في كيفية استخدام هذا التطبيق Stylus لإنشاء واجهة مستخدم ملساء، من تنظيم التكوين إلى تأثيرات التمرير، بينما نبقى بالرمز قابلاً للتصحيح والتوسيع.

## لماذا Stylus؟ مقدمة سريعة

Stylus هو معالج CSS قبل التجميع الذي يبعد عن التكرار في CSS التقليدي (لا تحتاج إلى أقواس أو فاصل) ويضيف ميزات قوية مثل المتغيرات، المزيج، والتداخل. يورد الكود المتغيرات من `variables.styl` ومجموعة أساسية من `base.styl`، مما يضع الأساس لمجموعة من الأسلوبات المتجانسة والمتكررة. على سبيل المثال، قد يكون اللون الأساسي `#1CB2EF` محددًا في `variables.styl` ويستخدم مرة أخرى عبر الأزرار والألوان الخلفية.

## تنظيم التكوين: الأقسام والأوعية

يتم تقسيم الصفحة الرئيسية للمتجر إلى أقسام منفصلة - `.slide`, `.feature`, `.reviewer`, `.example`, و `.contact` - لكل منها استراتيجية تزيين خاصة بها. إليك كيفية تزيين قسم `.slide` (البطاقة الرئيسية):

```stylus
.slide
  height 800px
  position relative
  color #fff
  width 100%
  overflow hidden
  .bg
    background url("../img/home/hero.jpg") no-repeat
    background-size cover
    background-position-y 40%
    position 200% 200%
    width 100%
    height 100%
    padding-top 280px
```

### التقنيات الرئيسية:
- **بطاقة رئيسية كاملة الشاشة**: `height 800px` و `width 100%` يخلقان بطاقة رئيسية كبيرة، و `overflow hidden` يضمن عدم تسرب المحتوى.
- **صورة الخلفية**: تستخدم فئة `.bg` `background-size cover` لتكبير الصورة الرئيسية بشكل متناسب، بينما `background-position-y 40%` يحدد التزامن العمودي للتصوير البصري.
- **التداخل**: يظل التداخل في Stylus مع مجموعة من الأسلوبات ذات الصلة، مما يحسن من قابلية القراءة مقارنة بالCSS المسطح.

## شبكات متفاعلة مع Flexbox و clearfix

يظهر قسم `.feature` في تصميم ثلاثي الأعمدة:

```stylus
.feature
  height 450px
  padding 125px 0
  background white
  .list
    width 1160px
    margin 0 auto
    display flex
    flex-direction row
    li
      height 200px
      padding-left 50px
      flex-grow 1
      &:first-child
        padding-left 0
      .short
        width 235px
        height 200px
        margin 0 auto
```

### النقاط البارزة:
- **Flexbox**: `display flex` و `flex-direction row` يوزع العناصر في القائمة أفقيًا، بينما `flex-grow 1` يضمن أن تتوسع العناصر بشكل متساوٍ لتملأ الحاوية.
- **المركز**: `width 1160px` مع `margin 0 auto` يركز المحتوى، وهي تقنية تقليدية للتصميمات ذات العرض الثابت.
- **سحر الفئة الوهمية**: يبعد `&:first-child` من التزامن الأول، مما يمنع التزامن غير الطبيعي.

يأخذ قسم `.example` هذا إلى أبعد من ذلك مع شبكة من بطاقات المراجعة، باستخدام مزيج `clearfix()`:

```stylus
.example
  .list
    clearfix()
    .row
      clearfix()
      li:first-child
        margin-left 0
    li
      height 354px
      margin-left 48px
      pull-left()
      margin-bottom 48px
```

- **clearfix**: هذا المزيج (ربما محدد في `base.styl`) يدير إزالة التمرير، مما يضمن أن تتداخل الصفوف بشكل صحيح في المتصفحات القديمة أو التصميمات المخصصة.
- **شبكة التمرير**: `pull-left()` (مزيج من الخدمات) يطفو العناصر إلى اليسار، مع `margin-left 48px` يضيف فترات، وهذا النهج يكمّل Flexbox للتوافقية الأوسع.

## تزيين التفاعل: تأثيرات التمرير والتحولات

تلمع بطاقات المراجعة في `.example` مع تفاعلات التمرير السلسة:

```stylus
li
  .info
    position relative
    height 354px
    width 100%
    color white
    box-shadow 0 4px 4px 1px rgba(135,135,135,.1)
    overflow hidden
    cursor pointer
    &:hover
      img
        transform scale(1.2,1.2)
        -webkit-filter brightness(0.6)
      .title
        -webkit-transform translate(0, -20px)
        opacity 1.0
      .tips
        -webkit-transform translate(0, -10px)
        opacity 0.8
    img
      height 100%
      -webkit-filter brightness(0.4)
      transition all 0.35s ease 0s
```

### تحليل:
- **تأثيرات التمرير**: عند التمرير، تتكبير الصورة (`transform scale(1.2,1.2)`) وتضيء (`-webkit-filter brightness(0.6)`)، بينما تتحرك العناصر النصية إلى الأعلى مع `translate` وتعدل الشفافية.
- **التحولات**: `transition all 0.35s ease 0s` يضمن أن تكون التحولات لائقة لجميع الخصائص، مع مدة 350 مللي ثانية وموجة تسوية.
- **التداخل**: `position absolute` على `.text` يحددها فوق الصورة، مع `z-index 2` يضمن الرؤية.

يستجيب زر `.author` أيضًا:

```stylus
.author
  position absolute
  background black
  margin-left 30px
  margin-top 30px
  height 30px
  padding-left 20px
  padding-right 20px
  transition all 0.35s ease 0s
  &:hover
    background #1cb2ef
```

تغيير بسيط في اللون من الأسود إلى اللون التجاري `#1CB2EF` عند التمرير يضيف لمسًا مريحًا.

## تلميع بصري: الظلال، الأزرار، والأيقونات

تزيد الظلال في العمق، كما في `box-shadow 0 4px 4px 1px rgba(135,135,135,.1)` في `.info`. الأزرار، مثل في `.contact`، يتم تزيينها بعناية:

```stylus
.contact
  .rightbtn
    .more
      width 127px
      height 50px
      color #1CB2EF
      background white
      border-radius 3px
      border 1px solid #00A3E6
      -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset, 0px 1px 2px rgba(0,0,0,0.15)
```

- **الظل الداخلي**: الظل الداخلي (`inset`) مع الظل الخارجي يخلق تأثير زر مضغوط.
- **التزامن**: لون الحدود `#00A3E6` يتوافق مع لوحة الألوان التجارية.

الأيقونات، مثل `.icon_crown`، تستخدم صور الخلفية:

```stylus
.icon_crown
  background url("../img/icon/crown@2x.png") no-repeat
  background-size contain
  width 49px
  height 52px
```

يشير اللاحقة `@2x` إلى الأصول جاهزة للريتينا، مع `background-size contain` يضمن التكبير الصحيح.

## أفضل الممارسات والتوصيات

يقدم هذا تنفيذ Stylus دروسًا لأي مشروع CSS:
1. **استخدام المعالجات**: يسرع Stylus التداخل والمزيج (مثل `clearfix()`) تصميمات معقدة.
2. **توازن التكوين**: قم بدمج Flexbox للمتصفحات الحديثة مع حلول التمرير للتوافقية.
3. **تحسين تجربة المستخدم**: التحولات السلسة والتأثيرات التمريرية تجعل الواجهة المستخدمية تبدو حية.
4. **إبقاءها قابلة للتصحيح**: استغل المتغيرات والإدخالات للتزامن عبر قواعد كبيرة.

ما إذا كنت تزيين مصنع مراجعة الكود أو ملف شخصي، يمكن أن يرفع هذه التقنيات من مستوى CSS الخاص بك. في المرة القادمة التي تكتب فيها ملفات التزيين، فكر في كيفية التداخل والتحولات والظل الذي يمكن أن يتحول تصميمك!