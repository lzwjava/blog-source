---
audio: false
generated: false
image: false
lang: ar
layout: post
title: بناء منصة مراجعة الكود الفعالة باستخدام Vue.js
translated: true
type: post
---

في عالم التطوير السريع اليوم، جودة الكود هي أمر حاسم. يمكن أن يرفع عملية مراجعة الكود الجيدة من إنتاج الفريق وتحسين مهارات الأفراد. مؤخرًا، استكشفت مشروعًا مثيرًا - خدمة مراجعة الكود مبنية باستخدام Vue.js التي تربط المطورين مع مراجعين خبراء لتحسين قواعدهم. دعونا نغوص في الأساسيات الفنية لهذه المنصة، مع التركيز على معماريتها الأمامية، تصميم المكونات، ووسائل التجميل.

## الصورة الكبيرة: Vue.js كأساس

تستفيد المنصة من Vue.js، إطار عمل JavaScript التقدمي، لإنشاء واجهة مستخدم تفاعلية وموضوعة. قاعدة الكود التي فحصتها هي تطبيق صفحة واحدة (SPA) مع فصل واضح للاهتمامات - قوالب HTML للهيكل، JavaScript لللوغيك، وStylus للتجميل. هذه الثلاثية تجعلها دراسة حالة جيدة للتطوير الويب الحديث.

في قلب التطبيق، هناك صفحة رئيسية تحتوي على أقسام مثل شريط البطل، ميزات مميزة، عرض مراجعين، ومثال مراجعات. كل قسم مصمم بعناية لتوجيه المستخدمين من خلال قيمة الخدمة، من اكتشاف مراجعين خبراء إلى استكشاف حالات مراجعة الكود في العالم الحقيقي.

## تحليل القالب: المكونات والإعادة الديناميكية

القالب HTML هو خليط من المحتوى الثابت والمكونات Vue الديناميكية. إليك مقطع من قسم البطل:

```html
<section class="slide">
  <div class="bg">
    <h1>أفضل خدمة مراجعة الكود</h1>
    <h2>مراجعة الكود، تساعدك بسرعة في تحسين القوة التنافسية الأساسية</h2>
    <a href="./belief.html"><button class="help">2016، أردت أن أفعل شيئًا صغيرًا للجميع</button></a>
  </div>
</section>
```

هذا القسم بسيط ولكن يضع الطابع مع صورة خلفية جريئة ودعوة للفعل. ومع ذلك، يحدث السحر الحقيقي في الأقسام الديناميكية مثل "مثال مراجعات الكود":

```html
<section class="example">
  <div class="container">
    <h2>مثال مراجعات الكود</h2>
    <ul class="list">
      <div class="row">
        <li class="clo-1" @click="goDetail(reviews[0].reviewId)">
          <div class="info">
            <button class="author" v-for="author in reviews[0].authors">{{author.authorName}}</button>
            <img :src="reviews[0].coverUrl">
            <div class="text">
              <h6 class="title" v-html="reviews[0].title"></h6>
              <h6 class="tips">
                <span v-for="tag in reviews[0].tags">#{{tag.tagName}}</span>
              </h6>
            </div>
          </div>
        </li>
        <!-- المزيد من عناصر القائمة -->
      </div>
    </ul>
  </div>
</section>
```

### الميزات الرئيسية:
1. **ربط البيانات الديناميكي**: يُربط المخرجات `:src` و `v-html` البيانات من مصفوفة `reviews` (محدد في النص) إلى القالب. وهذا يسمح للتطبيق بإعادة عرض المحتوى ديناميكيًا بناءً على البيانات المستخرجة أو المكتوبة.
2. **معالجة الأحداث**: يُشغل المخرج `@click="goDetail(reviews[0].reviewId)"` طريقة لتوجيه إلى عرض تفصيلي للمراجعة، مما يوضح نظام الأحداث السلس لـ Vue.
3. **دورات مع `v-for`**: يُكرر المخرج `v-for` على مصفوفات مثل `authors` و `tags`، مما يتيح إعادة عرض عناصر متعددة بشكل فعال. وهذا مثالي لعرض العديد من المساهمين أو البيانات الإضافية دون كتابة.

تحدد البيانات `reviews` في النص:

```javascript
reviews: [
  {
    reviewId: 1,
    coverUrl: 'http://7xotd0.com1.z0.glb.clouddn.com/photo-1450849608880-6f787542c88a.jpeg',
    title: 'كيف <br> بناء <br> بيئة تطوير ممتعة',
    tags: [{tagName: 'XCode'}, {tagName: 'iOS'}],
    authors: [{authorName: '叶孤城'}]
  },
  // المزيد من كائنات المراجعة
]
```

يمكن استبدال هذه المصفوفة بسهولة بطلب API، مما يجعل التطبيق قابلًا للتوسيع للاستخدام في العالم الحقيقي.

## معمارية المكونات: إعادة الاستخدام والتجزئة

يستخدم التطبيق المكونات Vue بشكل كبير، يتم استيرادها في أعلى النص:

```javascript
import reviewerCard from '../components/reviewer-card.vue';
import Guide from '../components/guide.vue';
import Overlay from '../components/overlay.vue';
import Contactus from '../components/contactus.vue';
```

تسجل هذه المكونات وتستخدم في القالب، مثل `<reviewer :reviewers="reviewers"></reviewer>` و `<guide></guide>`. هذا النهج التجزئي:
- **يقلل من التكرار**: يتم إعادة استخدام عناصر واجهة المستخدم الشائعة (مثل بطاقات المراجعين) عبر الصفحات.
- **يحسن الصيانة**: كل مكون يحوي منطقًا ووسائل تجميل خاصًا به.

على سبيل المثال، يغطي مكون `Overlay` المحتوى الديناميكي:

```html
<overlay :overlay.sync="overlayStatus">
  <component :is="currentView"></component>
</overlay>
```

هنا، `:overlay.sync` ينسق مرئية الغطاء مع خاصية البيانات `overlayStatus`، بينما `:is` يعرض مكون `currentView` الديناميكيًا (على سبيل المثال، `Contactus`). هذا هو طريقة قوية للتعامل مع النوافذ المتحركة أو النوافذ المتحركة دون إفساد القالب الرئيسي.

## استخراج البيانات: طلبات HTTP والتنشيط

يبدأ التنشيط في `created` في دورة الحياة:

```javascript
created() {
  this.$http.get(serviceUrl.reviewers, { page: "home" }).then((resp) => {
    if (util.filterError(this, resp)) {
      this.reviewers = resp.data.result;
    }
  }, util.httpErrorFn(this));
  this.$http.get(serviceUrl.reviewsGet, { limit: 6 }).then((resp) => {
    if (util.filterError(this, resp)) {
      var reviews = resp.data.result;
      // تحديث المراجعات الديناميكيًا إذا لزم الأمر
    }
  }, util.httpErrorFn(this));
  this.checkSessionToken();
}
```

- **تحميل البيانات المزدوجة**: يستخدم التطبيق `$http` لـ Vue (ربما Vue Resource أو Axios) لاستخراج بيانات المراجعين والمراجعات من API الخلفية.
- **إدارة الأخطاء**: يضمن `util.filterError` إدارة الأخطاء القوية، مما يظل واجهة المستخدم مستقرة.
- **إدارة الجلسة**: يوفر `checkSessionToken` طريقة لتوثيق المستخدم عبر متغيرات الاستعلام، وتحديد ملفات تعريف الارتباط وإعادة توجيه حسب الحاجة.

## التجميل باستخدام Stylus: مرن ومجيد

الوسائل التجميلية، المكتوبة في Stylus، تجمع بين المرونة والجمال. إليك قسم `.example`:

```stylus
.example
  margin 0 auto
  padding-top 5px
  background #FDFFFF
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
```

### النقاط البارزة:
- **أحداث التمرير**: يوسع `&:hover` الصور ويزحزح النص، مما يخلق تجربة تفاعلية سلسة.
- **المرونة**: يضمن `clearfix()` و `pull-left()` تصميم الشبكة الاستجابة.
- **اللمعان البصري**: الأظلال والمتغيرات (على سبيل المثال، `transition: all 0.35s ease 0s`) تضيف العمق والسمو.

استخدام المتغيرات من `variables.styl` (على سبيل المثال، الألوان مثل `#1CB2EF`) يضمن التوافق عبر التطبيق.

## استنتاجات لمشروعك القادم

تقدم هذه المنصة مراجعة الكود دروسًا قيمة:
1. **استغل تفاعلية Vue**: ربط البيانات الديناميكيًا واستخدام المكونات لحفظ تطبيقك التجزئي.
2. **خطط للتوسيع**: استبدل البيانات المكتوبة بطلبات API مع نمو تطبيقك.
3. **تجميل ذكي**: استخدم مسبقات مثل Stylus للحصول على أساليب قابلة للصيانة ومتكررة.
4. **تركيز على تجربة المستخدم**: الانتقالات السلسة ودعوات الفعل الواضحة تزيد من مشاركة المستخدم.

ما هو مشروعك القادم؟ دعونا نواصل محادثة جودة الكود!