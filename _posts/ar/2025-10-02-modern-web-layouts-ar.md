---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: أساليب وتخطيطات الويب الحديثة
translated: true
type: note
---

### نظرة عامة
يبدو أن هذا كود CSS مكتوب بصيغة SCSS (Sass)، ويضم تداخلاً للعناصر، ومحددات علامة العطف (&) للفئات الزائفة، وتوجيهات @extend. فهو يحدد أنماطاً لتخطيط صفحة ويب أساسية، والنماذج، والأزرار، والأدوات المساعدة، بمظهر حديث وأنيق (مثل الزوايا الدائرية، والظلال الناعمة، وحركات التمرير عند التحويم). الخصائص بدون وحدات قياس (مثل `font-size 16px`) هي اختصار لصيغة SCSS. سأقوم بتحليله قسمًا بقسم، موضحًا المحددات وتأثيراتها.

### الأنماط العامة (html, body)
```css
html, body
  font-family Verdana
  font-size 16px
  height 100%
  background-color #D2D2D2
```
- يطبق مجموعة خطوط بسيطة (Verdana كخط احتياطي إذا لزم الأمر) بحجم 16 بكسل.
- يضبط الارتفاع الكامل (100%) لتخطيط صفحة كاملة، غالبًا من أجل التمركز أو تغطية منفذ العرض.
- لون الخلفية هو رمادي فاتح (#D2D2D2) كأساس محايد.

### أنماط القوائم والروابط (ul, a)
```css
ul
  list-style-type none
  padding 0
  margin 0

a
  color #000
  cursor pointer
  text-decoration none
```
- يزيل النقاط التلقائية، والحشوة، والهوامش من القوائم غير المرتبة للحصول على تنسيق أنظف ومخصص.
- الروابط باللون الأسود (#000)، ولها مؤشر يدوي عند التمرير، وبدون خطوط تحتها، مما يجعلها تبدو كأزرار.

### أداة الألوان والنص (.a-blue)
```css
.a-blue
  color #00BDEF
```
- فئة للنص الأزرق (#00BDEF، أزرق فاتح)، غالبًا للاستخدام كلمسات لونية.

### أنماط الأزرار (.btn, .btn-blue, .btn-gray, .btn-gray-2)
```css
.btn
  border-radius 3px
  padding 10px

.btn-blue
  background #00BDEF
  color #fff
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #00ABD8
    transition .5s

.btn-gray
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  -webkit-box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  box-shadow 0px 1px 0px rgba(255,255,255,0.15) inset,0px 1px 2px rgba(0,0,0,0.15)
  &:hover
    background #ddd
    transition 0.5s

.btn-gray-2
  background #eee
  color #333
  border 1px solid #d5d5d5
  border-radius 3px
  &:hover
    background #ddd
    transition 0.5s
```
- `.btn` هي فئة أساسية للزوايا الدائرية بقيمة 3 بكسل وحشوة داخلية بقيمة 10 بكسل.
- `.btn-blue`: زر أزرق (خلفية #00BDEF، نص أبيض) مع إبرازات داخلية وظلال خارجية لإضافة عمق. عند التمرير، يغمق اللون الأزرق بانتقال سلس مدته 0.5 ثانية.
- `.btn-gray` و `.btn-gray-2`: أزرار رمادية (خلفية فاتحة #eee، نص غامق #333، حدود خفيفة #d5d5d5) بظلال متشابهة. `.btn-gray-2` لا يحتوي على box-shadow صريح ولكن له نفس تأثير التمرير (يضيء إلى #ddd). مفيد للإجراءات الثانوية.

### أدوات التموضع (.absolute-center, .full-space)
```css
.absolute-center
    margin auto
    position absolute
    top 0
    left 0
    bottom 0
    right 0

.full-space
    position absolute
    top 0
    left 0
    bottom 0
    right 0
```
- `.absolute-center`: يمركز العنصر بشكل مطلق داخل العنصر الأب (بداية/نهاية/يمين/يسار عند 0، مع هوامش تلقائية).
- `.full-space`: يجعل العنصر يملأ المساحة الكاملة للعنصر الأب بشكل مطلق.

### أنماط النماذج (.base-form, input/textarea/select, button)
```css
.base-form
  @extend .absolute-center
  max-width 350px
  height 400px
  background #fff
  border-radius 20px
  text-align center
  padding 20px 10px

input, textarea, select
  box-sizing border-box
  border none
  outline none
  &:focus
    border none
    outline none
    box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)
    -webkit-box-shadow 0px 1px 4px 0px rgba(0,0,0,.06)

button
  border-style none
  outline none
```
- `.base-form`: يوسع `.absolute-center` لتمرير نموذج يشبه النافذة المنبثقة (أقصى عرض 350 بكسل، ارتفاع 400 بكسل، خلفية بيضاء، زوايا دائرية 20 بكسل، نص في المنتصف، حشوة داخلية). مثالي لنماذج تسجيل الدخول أو الاشتراك.
- حقول الإدخال، ومناطق النص، والقوائم المنسدلة: بدون حدود مع box-sizing لتضمين الحشوة في العرض؛ بدون حدود خارجية عند التركيز، ولكن يضيف ظلًا رماديًا خفيفًا عند التركيز لتحسين تجربة المستخدم.
- الأزرار: يزيل الحدود والحدود الخارجية الافتراضية، على افتراض استخدام أنماط `.btn` للحصول على مظهر أفضل.

يقوم هذا الكود بإعداد صفحة نموذج مستجيبة ومركزة مع أزرار وحقول إدخال مخصصة. إذا كنت تستخدم SCSS، قم بتحويله إلى CSS قياسي. للتخصيص، قم بتعديل الألوان أو الأحجام حسب الحاجة.